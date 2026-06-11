"""
49_reversal_patterns — Base Features 076-150
Domain: intraday/multi-bar named reversal candlestick pattern recognition at/near lows
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
NEW patterns added: three white soldiers, bullish abandoned baby, bullish kicker,
belt hold (bullish), three inside up, three outside up.
Also covers: island reversal, multi-pattern composites, doji/dragonfly, recency scores,
downtrend context.
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


# ── Internal pattern helpers (to avoid cross-file dependency) ─────────────────

def _eng_flag(o, c, h, l):
    prev_bear = c.shift(1) < o.shift(1)
    today_bull = c > o
    engulfs = (o <= c.shift(1)) & (c >= o.shift(1))
    return (prev_bear & today_bull & engulfs)


def _hammer_flag(o, c, h, l):
    rng = _range(h, l)
    body = _body_abs(o, c)
    lw = _lower_wick(o, c, l)
    uw = _upper_wick(o, c, h)
    small_body = body <= rng * 0.33
    long_lower = lw >= body * 2.0
    short_upper = uw <= body * 0.5
    body_upper_half = pd.concat([o, c], axis=1).min(axis=1) >= l + rng * 0.5
    return small_body & long_lower & short_upper & body_upper_half


def _inv_hammer_flag(o, c, h, l):
    rng = _range(h, l)
    body = _body_abs(o, c)
    lw = _lower_wick(o, c, l)
    uw = _upper_wick(o, c, h)
    small_body = body <= rng * 0.33
    long_upper = uw >= body * 2.0
    short_lower = lw <= body * 0.5
    body_lower_half = pd.concat([o, c], axis=1).max(axis=1) <= l + rng * 0.5
    return small_body & long_upper & short_lower & body_lower_half


def _morning_star_flag(o, c, h, l):
    bar1_bear = c.shift(2) < o.shift(2)
    bar1_body = _body_abs(o.shift(2), c.shift(2))
    bar2_small = _body_abs(o.shift(1), c.shift(1)) <= bar1_body * 0.35
    bar3_bull = c > o
    bar3_recovers = c > (o.shift(2) + c.shift(2)) / 2.0
    return bar1_bear & bar2_small & bar3_bull & bar3_recovers


def _harami_flag(o, c, h, l):
    prev_bear = c.shift(1) < o.shift(1)
    today_bull = c > o
    contained = (o > c.shift(1)) & (o < o.shift(1)) & (c > c.shift(1)) & (c < o.shift(1))
    return prev_bear & today_bull & contained


def _tweezer_flag(o, c, h, l):
    atr14 = _atr(c, h, l, 14)
    tol = atr14 * 0.10
    matching_lows = (l - l.shift(1)).abs() <= tol
    prior_down = c.shift(1) < c.shift(2)
    return matching_lows & prior_down


def _krd_flag(o, c, h, l):
    new_low = l < _rolling_min(l.shift(1), _TD_MON)
    closes_up = c > c.shift(1)
    return new_low & closes_up


def _piercing_flag(o, c, h, l):
    prev_bear = c.shift(1) < o.shift(1)
    prior_mid = (o.shift(1) + c.shift(1)) / 2.0
    opens_below = o < l.shift(1)
    closes_above_mid = c > prior_mid
    today_bull = c > o
    return prev_bear & opens_below & closes_above_mid & today_bull


def _outside_up_flag(o, c, h, l):
    outside = (h > h.shift(1)) & (l < l.shift(1))
    closes_bull = c > o
    closes_near_high = c >= (l + (h - l) * 0.60)
    return outside & closes_bull & closes_near_high


def _three_white_soldiers_flag(o, c, h, l):
    """Three consecutive long bullish candles, each opening within prior body, closing near high."""
    atr14 = _atr(c, h, l, 14)
    # Each bar is bullish
    b3_bull = c > o
    b2_bull = c.shift(1) > o.shift(1)
    b1_bull = c.shift(2) > o.shift(2)
    # Each body is substantial (> 0.5 ATR)
    b3_long = _body_abs(o, c) > atr14 * 0.5
    b2_long = _body_abs(o.shift(1), c.shift(1)) > atr14 * 0.5
    b1_long = _body_abs(o.shift(2), c.shift(2)) > atr14 * 0.5
    # Each opens within the prior bar's body
    b3_opens_in_b2 = (o >= o.shift(1)) & (o <= c.shift(1))
    b2_opens_in_b1 = (o.shift(1) >= o.shift(2)) & (o.shift(1) <= c.shift(2))
    # Each closes higher than prior close
    b3_higher = c > c.shift(1)
    b2_higher = c.shift(1) > c.shift(2)
    # Each closes near its high (small upper wick <= 20% of body)
    b3_near_high = _upper_wick(o, c, h) <= _body_abs(o, c) * 0.20
    b2_near_high = _upper_wick(o.shift(1), c.shift(1), h.shift(1)) <= _body_abs(o.shift(1), c.shift(1)) * 0.20
    return (b3_bull & b2_bull & b1_bull
            & b3_long & b2_long & b1_long
            & b3_opens_in_b2 & b2_opens_in_b1
            & b3_higher & b2_higher
            & b3_near_high & b2_near_high)


def _abandoned_baby_flag(o, c, h, l):
    """Bullish abandoned baby: gap-down doji isolated by gaps, then gap-up bullish candle."""
    rng2 = _range(h.shift(1), l.shift(1))
    body2 = _body_abs(o.shift(1), c.shift(1))
    is_doji_mid = body2 <= rng2 * 0.10
    # Gap down into bar2 (bar1 low > bar2 high)
    gap_down_in = l.shift(2) > h.shift(1)
    # Gap up out of bar2 (bar3 low > bar2 high) — confirmed on bar3
    gap_up_out = l > h.shift(1)
    bar3_bull = c > o
    return gap_down_in & is_doji_mid & gap_up_out & bar3_bull


def _kicker_flag(o, c, h, l):
    """Bullish kicker: prior bar bearish, today gaps above prior open (open2 > open1)."""
    bar1_bear = c.shift(1) < o.shift(1)
    gap_up_open = o > o.shift(1)
    bar2_bull = c > o
    return bar1_bear & gap_up_open & bar2_bull


def _belt_hold_flag(o, c, h, l):
    """Belt hold bullish: opens at/near its low (tiny lower wick), long bullish body after downtrend."""
    atr14 = _atr(c, h, l, 14)
    lw = _lower_wick(o, c, l)
    body = _body_abs(o, c)
    bar_bull = c > o
    # Very small lower wick (open near the low)
    tiny_lw = lw <= atr14 * 0.05
    # Long body
    long_body = body >= atr14 * 0.7
    # Prior downtrend: close 3 bars ago higher than close 1 bar ago
    prior_down = c.shift(1) < c.shift(3)
    return bar_bull & tiny_lw & long_body & prior_down


def _three_inside_up_flag(o, c, h, l):
    """Three inside up: bar1 bear, bar2 inside (harami), bar3 bull closing above bar2 close."""
    # Bar1: bearish
    b1_bear = c.shift(2) < o.shift(2)
    # Bar2: inside bar (harami-like: body inside bar1 body)
    b2_inside = (o.shift(1) > c.shift(2)) & (o.shift(1) < o.shift(2)) & (c.shift(1) > c.shift(2)) & (c.shift(1) < o.shift(2))
    # Bar3: bullish, closes above bar2 close
    b3_bull = c > o
    b3_higher = c > c.shift(1)
    return b1_bear & b2_inside & b3_bull & b3_higher


def _three_outside_up_flag(o, c, h, l):
    """Three outside up: bar1 bear, bar2 engulfs bar1 (bullish engulfing), bar3 closes higher."""
    # Bar1: bearish
    b1_bear = c.shift(2) < o.shift(2)
    # Bar2: bullish engulfing of bar1
    b2_bull = c.shift(1) > o.shift(1)
    b2_engulfs = (o.shift(1) <= c.shift(2)) & (c.shift(1) >= o.shift(2))
    # Bar3: bullish, closes above bar2 close
    b3_bull = c > o
    b3_higher = c > c.shift(1)
    return b1_bear & b2_bull & b2_engulfs & b3_bull & b3_higher


def _any_pattern_flag(o, c, h, l):
    total = (
        _eng_flag(o, c, h, l).astype(float)
        + _hammer_flag(o, c, h, l).astype(float)
        + _inv_hammer_flag(o, c, h, l).astype(float)
        + _morning_star_flag(o, c, h, l).astype(float)
        + _harami_flag(o, c, h, l).astype(float)
        + _tweezer_flag(o, c, h, l).astype(float)
        + _krd_flag(o, c, h, l).astype(float)
        + _piercing_flag(o, c, h, l).astype(float)
        + _outside_up_flag(o, c, h, l).astype(float)
        + _three_white_soldiers_flag(o, c, h, l).astype(float)
        + _abandoned_baby_flag(o, c, h, l).astype(float)
        + _kicker_flag(o, c, h, l).astype(float)
        + _belt_hold_flag(o, c, h, l).astype(float)
        + _three_inside_up_flag(o, c, h, l).astype(float)
        + _three_outside_up_flag(o, c, h, l).astype(float)
    )
    return (total > 0).astype(float)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-083): Island Reversal ---

def rev_076_island_reversal_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: bullish island reversal — gap down into island, gap up out of island."""
    gap_down_in = high.shift(2) < low.shift(1)
    gap_up_out = low > high.shift(1)
    return (gap_down_in & gap_up_out).astype(float)


def rev_077_island_reversal_near_low_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Island reversal completing at/near the 21-day closing low."""
    ir = rev_076_island_reversal_flag(open, close, high, low).astype(bool)
    near = _near_low(close, low, _TD_MON)
    return (ir & near).astype(float)


def rev_078_island_reversal_count_63d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of island reversals completing in trailing 63 days."""
    return _rolling_sum(rev_076_island_reversal_flag(open, close, high, low), _TD_QTR)


def rev_079_island_reversal_days_since(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Days since most recent island reversal completion."""
    flag = rev_076_island_reversal_flag(open, close, high, low).astype(bool)
    return _days_since(flag)


def rev_080_island_reversal_vol_spike(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Island reversal where escape-gap day volume > 2x 21-day average."""
    ir = rev_076_island_reversal_flag(open, close, high, low).astype(bool)
    avg_vol = _rolling_mean(volume, _TD_MON)
    return (ir & (volume > avg_vol * 2.0)).astype(float)


def rev_081_island_reversal_near_52wk_low(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Island reversal completing within 15% of 252-day closing low."""
    ir = rev_076_island_reversal_flag(open, close, high, low).astype(bool)
    low52 = _rolling_min(close, _TD_YEAR)
    near = close <= low52 * 1.15
    return (ir & near).astype(float)


def rev_082_island_reversal_gap_magnitude(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Island reversal: escape-gap magnitude ATR-normalized; else 0."""
    flag = rev_076_island_reversal_flag(open, close, high, low).astype(bool)
    atr14 = _atr(close, high, low, 14)
    gap = _safe_div(low - high.shift(1), atr14)
    return gap.where(flag, 0.0)


def rev_083_island_body_bull_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Island reversal where the escape bar is also a bullish body (close > open)."""
    ir = rev_076_island_reversal_flag(open, close, high, low).astype(bool)
    bull_body = close > open
    return (ir & bull_body).astype(float)


# --- Group I (084-093): Three White Soldiers ---

def rev_084_three_white_soldiers_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: three white soldiers — three consecutive long bullish candles after a decline,
    each opening within the prior body and closing near its high."""
    return _three_white_soldiers_flag(open, close, high, low).astype(float)


def rev_085_three_white_soldiers_near_low_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Three white soldiers completing at/near the 21-day closing low."""
    tws = _three_white_soldiers_flag(open, close, high, low)
    near = _near_low(close, low, _TD_MON)
    return (tws & near).astype(float)


def rev_086_three_white_soldiers_near_52wk_low(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Three white soldiers completing within 10% of the 252-day closing low."""
    tws = _three_white_soldiers_flag(open, close, high, low)
    low52 = _rolling_min(close, _TD_YEAR)
    near = close <= low52 * 1.10
    return (tws & near).astype(float)


def rev_087_three_white_soldiers_count_63d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of three white soldiers patterns completing in trailing 63 days."""
    return _rolling_sum(rev_084_three_white_soldiers_flag(open, close, high, low), _TD_QTR)


def rev_088_three_white_soldiers_count_252d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of three white soldiers patterns completing in trailing 252 days."""
    return _rolling_sum(rev_084_three_white_soldiers_flag(open, close, high, low), _TD_YEAR)


def rev_089_three_white_soldiers_days_since(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Days since most recent three white soldiers pattern."""
    flag = rev_084_three_white_soldiers_flag(open, close, high, low).astype(bool)
    return _days_since(flag)


def rev_090_three_white_soldiers_vol_confirm(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Three white soldiers with bar-3 volume exceeding 21-day average (conviction)."""
    tws = _three_white_soldiers_flag(open, close, high, low)
    avg_vol = _rolling_mean(volume, _TD_MON)
    return (tws & (volume > avg_vol)).astype(float)


def rev_091_three_white_soldiers_body_expansion(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """On three white soldiers bars: bar-3 body relative to bar-1 body (expansion ratio); else 0."""
    flag = _three_white_soldiers_flag(open, close, high, low)
    b3_body = _body_abs(open, close)
    b1_body = _body_abs(open.shift(2), close.shift(2)).replace(0, np.nan)
    ratio = b3_body / b1_body
    return ratio.where(flag, 0.0)


# --- Group J (092-101): Bullish Abandoned Baby ---

def rev_092_abandoned_baby_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: bullish abandoned baby — gap-down doji isolated by gaps, then gap-up bullish candle."""
    return _abandoned_baby_flag(open, close, high, low).astype(float)


def rev_093_abandoned_baby_near_low_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Bullish abandoned baby completing at/near the 21-day closing low."""
    ab = _abandoned_baby_flag(open, close, high, low)
    near = _near_low(close, low, _TD_MON)
    return (ab & near).astype(float)


def rev_094_abandoned_baby_near_52wk_low(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Bullish abandoned baby within 10% of the 252-day closing low."""
    ab = _abandoned_baby_flag(open, close, high, low)
    low52 = _rolling_min(close, _TD_YEAR)
    near = close <= low52 * 1.10
    return (ab & near).astype(float)


def rev_095_abandoned_baby_count_252d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of bullish abandoned baby patterns in trailing 252 days."""
    return _rolling_sum(rev_092_abandoned_baby_flag(open, close, high, low), _TD_YEAR)


def rev_096_abandoned_baby_days_since(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Days since most recent bullish abandoned baby pattern."""
    flag = rev_092_abandoned_baby_flag(open, close, high, low).astype(bool)
    return _days_since(flag)


def rev_097_abandoned_baby_gap_size(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """On abandoned baby bars: escape-gap magnitude ATR-normalized; else 0."""
    flag = _abandoned_baby_flag(open, close, high, low)
    atr14 = _atr(close, high, low, 14)
    gap = _safe_div(low - high.shift(1), atr14)
    return gap.where(flag, 0.0)


def rev_098_abandoned_baby_vol_confirm(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Abandoned baby with bar-3 volume above 21-day average."""
    ab = _abandoned_baby_flag(open, close, high, low)
    avg_vol = _rolling_mean(volume, _TD_MON)
    return (ab & (volume > avg_vol)).astype(float)


# --- Group K (099-107): Bullish Kicker ---

def rev_099_kicker_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: bullish kicker — sharp gap-up bullish candle immediately after a bearish candle;
    open of bar2 gaps above open of bar1 (strong sentiment-reversal signal)."""
    return _kicker_flag(open, close, high, low).astype(float)


def rev_100_kicker_near_low_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Bullish kicker at/near the 21-day closing low."""
    kicker = _kicker_flag(open, close, high, low)
    near = _near_low(close, low, _TD_MON)
    return (kicker & near).astype(float)


def rev_101_kicker_near_52wk_low(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Bullish kicker within 10% of the 252-day closing low."""
    kicker = _kicker_flag(open, close, high, low)
    low52 = _rolling_min(close, _TD_YEAR)
    near = close <= low52 * 1.10
    return (kicker & near).astype(float)


def rev_102_kicker_count_21d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of bullish kicker patterns in trailing 21 days."""
    return _rolling_sum(rev_099_kicker_flag(open, close, high, low), _TD_MON)


def rev_103_kicker_count_63d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of bullish kicker patterns in trailing 63 days."""
    return _rolling_sum(rev_099_kicker_flag(open, close, high, low), _TD_QTR)


def rev_104_kicker_days_since(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Days since most recent bullish kicker pattern."""
    flag = rev_099_kicker_flag(open, close, high, low).astype(bool)
    return _days_since(flag)


def rev_105_kicker_gap_size_atr(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Bullish kicker gap size (open2 - open1) ATR-normalized; else 0."""
    flag = _kicker_flag(open, close, high, low)
    atr14 = _atr(close, high, low, 14)
    gap = _safe_div(open - open.shift(1), atr14)
    return gap.where(flag, 0.0)


def rev_106_kicker_vol_confirm(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Bullish kicker with above-average volume (stronger conviction)."""
    kicker = _kicker_flag(open, close, high, low)
    avg_vol = _rolling_mean(volume, _TD_MON)
    return (kicker & (volume > avg_vol)).astype(float)


def rev_107_kicker_count_252d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of bullish kicker patterns in trailing 252 days."""
    return _rolling_sum(rev_099_kicker_flag(open, close, high, low), _TD_YEAR)


# --- Group L (108-115): Belt Hold (Bullish) ---

def rev_108_belt_hold_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: bullish belt hold — long bullish candle opening at/near its low (no lower wick)
    after a downtrend; strong single-bar reversal signal."""
    return _belt_hold_flag(open, close, high, low).astype(float)


def rev_109_belt_hold_near_low_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Bullish belt hold at/near the 21-day closing low."""
    bh = _belt_hold_flag(open, close, high, low)
    near = _near_low(close, low, _TD_MON)
    return (bh & near).astype(float)


def rev_110_belt_hold_near_52wk_low(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Bullish belt hold within 10% of the 252-day closing low."""
    bh = _belt_hold_flag(open, close, high, low)
    low52 = _rolling_min(close, _TD_YEAR)
    near = close <= low52 * 1.10
    return (bh & near).astype(float)


def rev_111_belt_hold_count_21d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of bullish belt hold patterns in trailing 21 days."""
    return _rolling_sum(rev_108_belt_hold_flag(open, close, high, low), _TD_MON)


def rev_112_belt_hold_count_63d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of bullish belt hold patterns in trailing 63 days."""
    return _rolling_sum(rev_108_belt_hold_flag(open, close, high, low), _TD_QTR)


def rev_113_belt_hold_days_since(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Days since most recent bullish belt hold pattern."""
    flag = rev_108_belt_hold_flag(open, close, high, low).astype(bool)
    return _days_since(flag)


def rev_114_belt_hold_body_atr_ratio(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Belt hold body size ATR-normalized on pattern days; else 0."""
    flag = _belt_hold_flag(open, close, high, low)
    atr14 = _atr(close, high, low, 14)
    ratio = _safe_div(_body_abs(open, close), atr14)
    return ratio.where(flag, 0.0)


def rev_115_belt_hold_vol_confirm(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Bullish belt hold with above-average volume."""
    bh = _belt_hold_flag(open, close, high, low)
    avg_vol = _rolling_mean(volume, _TD_MON)
    return (bh & (volume > avg_vol)).astype(float)


# --- Group M (116-124): Three Inside Up ---

def rev_116_three_inside_up_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: three inside up — bullish harami on bars 1-2, then bar 3 closes above bar 2;
    confirms the harami reversal signal."""
    return _three_inside_up_flag(open, close, high, low).astype(float)


def rev_117_three_inside_up_near_low_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Three inside up completing at/near the 21-day closing low."""
    tiu = _three_inside_up_flag(open, close, high, low)
    near = _near_low(close, low, _TD_MON)
    return (tiu & near).astype(float)


def rev_118_three_inside_up_near_52wk_low(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Three inside up within 10% of the 252-day closing low."""
    tiu = _three_inside_up_flag(open, close, high, low)
    low52 = _rolling_min(close, _TD_YEAR)
    near = close <= low52 * 1.10
    return (tiu & near).astype(float)


def rev_119_three_inside_up_count_63d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of three inside up patterns completing in trailing 63 days."""
    return _rolling_sum(rev_116_three_inside_up_flag(open, close, high, low), _TD_QTR)


def rev_120_three_inside_up_count_252d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of three inside up patterns completing in trailing 252 days."""
    return _rolling_sum(rev_116_three_inside_up_flag(open, close, high, low), _TD_YEAR)


def rev_121_three_inside_up_days_since(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Days since most recent three inside up pattern."""
    flag = rev_116_three_inside_up_flag(open, close, high, low).astype(bool)
    return _days_since(flag)


def rev_122_three_inside_up_vol_confirm(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Three inside up with bar-3 volume above 21-day average (confirmation bar conviction)."""
    tiu = _three_inside_up_flag(open, close, high, low)
    avg_vol = _rolling_mean(volume, _TD_MON)
    return (tiu & (volume > avg_vol)).astype(float)


def rev_123_three_inside_up_bar3_body_atr(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """On three inside up bars: bar-3 body ATR-normalized (confirmation strength); else 0."""
    flag = _three_inside_up_flag(open, close, high, low)
    atr14 = _atr(close, high, low, 14)
    ratio = _safe_div(_body_abs(open, close), atr14)
    return ratio.where(flag, 0.0)


# --- Group N (124-132): Three Outside Up ---

def rev_124_three_outside_up_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: three outside up — bullish engulfing on bars 1-2, then bar 3 closes higher;
    confirms the engulfing reversal signal."""
    return _three_outside_up_flag(open, close, high, low).astype(float)


def rev_125_three_outside_up_near_low_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Three outside up completing at/near the 21-day closing low."""
    tou = _three_outside_up_flag(open, close, high, low)
    near = _near_low(close, low, _TD_MON)
    return (tou & near).astype(float)


def rev_126_three_outside_up_near_52wk_low(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Three outside up within 10% of the 252-day closing low."""
    tou = _three_outside_up_flag(open, close, high, low)
    low52 = _rolling_min(close, _TD_YEAR)
    near = close <= low52 * 1.10
    return (tou & near).astype(float)


def rev_127_three_outside_up_count_63d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of three outside up patterns completing in trailing 63 days."""
    return _rolling_sum(rev_124_three_outside_up_flag(open, close, high, low), _TD_QTR)


def rev_128_three_outside_up_count_252d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of three outside up patterns completing in trailing 252 days."""
    return _rolling_sum(rev_124_three_outside_up_flag(open, close, high, low), _TD_YEAR)


def rev_129_three_outside_up_days_since(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Days since most recent three outside up pattern."""
    flag = rev_124_three_outside_up_flag(open, close, high, low).astype(bool)
    return _days_since(flag)


def rev_130_three_outside_up_vol_confirm(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Three outside up with bar-3 volume above 21-day average."""
    tou = _three_outside_up_flag(open, close, high, low)
    avg_vol = _rolling_mean(volume, _TD_MON)
    return (tou & (volume > avg_vol)).astype(float)


def rev_131_three_outside_up_bar3_close_strength(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """On three outside up bars: bar-3 body ATR-normalized; else 0."""
    flag = _three_outside_up_flag(open, close, high, low)
    atr14 = _atr(close, high, low, 14)
    ratio = _safe_div(_body_abs(open, close), atr14)
    return ratio.where(flag, 0.0)


# --- Group O (132-142): Multi-pattern composites (new patterns included) ---

def rev_132_any_new_pattern_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: any of the 6 new patterns (tws, abandoned baby, kicker, belt hold, tiu, tou)."""
    total = (
        _three_white_soldiers_flag(open, close, high, low).astype(float)
        + _abandoned_baby_flag(open, close, high, low).astype(float)
        + _kicker_flag(open, close, high, low).astype(float)
        + _belt_hold_flag(open, close, high, low).astype(float)
        + _three_inside_up_flag(open, close, high, low).astype(float)
        + _three_outside_up_flag(open, close, high, low).astype(float)
    )
    return (total > 0).astype(float)


def rev_133_any_reversal_pattern_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: any of the full set of reversal patterns fires on the current bar."""
    return _any_pattern_flag(open, close, high, low)


def rev_134_any_reversal_pattern_count_21d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of bars showing any core reversal pattern in trailing 21 days."""
    return _rolling_sum(rev_133_any_reversal_pattern_flag(open, close, high, low), _TD_MON)


def rev_135_any_reversal_pattern_count_63d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of bars showing any core reversal pattern in trailing 63 days."""
    return _rolling_sum(rev_133_any_reversal_pattern_flag(open, close, high, low), _TD_QTR)


def rev_136_any_reversal_pattern_count_252d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of bars showing any core reversal pattern in trailing 252 days."""
    return _rolling_sum(rev_133_any_reversal_pattern_flag(open, close, high, low), _TD_YEAR)


def rev_137_simultaneous_pattern_count(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Number of distinct reversal patterns that simultaneously fire on today's bar."""
    return (
        _eng_flag(open, close, high, low).astype(float)
        + _hammer_flag(open, close, high, low).astype(float)
        + _inv_hammer_flag(open, close, high, low).astype(float)
        + _morning_star_flag(open, close, high, low).astype(float)
        + _harami_flag(open, close, high, low).astype(float)
        + _tweezer_flag(open, close, high, low).astype(float)
        + _krd_flag(open, close, high, low).astype(float)
        + _piercing_flag(open, close, high, low).astype(float)
        + _three_white_soldiers_flag(open, close, high, low).astype(float)
        + _abandoned_baby_flag(open, close, high, low).astype(float)
        + _kicker_flag(open, close, high, low).astype(float)
        + _belt_hold_flag(open, close, high, low).astype(float)
        + _three_inside_up_flag(open, close, high, low).astype(float)
        + _three_outside_up_flag(open, close, high, low).astype(float)
    )


def rev_138_reversal_density_21d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Fraction of last 21 bars that show any reversal pattern."""
    return _rolling_mean(rev_133_any_reversal_pattern_flag(open, close, high, low), _TD_MON)


def rev_139_reversal_density_63d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Fraction of last 63 bars that show any reversal pattern."""
    return _rolling_mean(rev_133_any_reversal_pattern_flag(open, close, high, low), _TD_QTR)


def rev_140_any_reversal_days_since(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Days since the most recent bar with any core reversal pattern."""
    flag = rev_133_any_reversal_pattern_flag(open, close, high, low).astype(bool)
    return _days_since(flag)


def rev_141_reversal_cluster_21d_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: 3 or more reversal pattern bars within the last 21 days (cluster signal)."""
    count21 = rev_134_any_reversal_pattern_count_21d(open, close, high, low)
    return (count21 >= 3).astype(float)


# --- Group P (142-150): Downtrend context and distress scoring ---

def rev_142_reversal_after_5d_decline_count_63d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of reversal patterns occurring after a 5-day decline in trailing 63 days."""
    flag = rev_133_any_reversal_pattern_flag(open, close, high, low).astype(bool)
    five_d_decline = close.shift(1) < close.shift(6)
    return _rolling_sum((flag & five_d_decline).astype(float), _TD_QTR)


def rev_143_reversal_below_sma50_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: any reversal pattern fires while close is below 50-day SMA (downtrend context)."""
    flag = rev_133_any_reversal_pattern_flag(open, close, high, low).astype(bool)
    sma50 = _rolling_mean(close, 50)
    below_sma = close < sma50
    return (flag & below_sma).astype(float)


def rev_144_reversal_at_52wk_low_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Any reversal pattern firing within 5% of the 252-day closing low."""
    flag = rev_133_any_reversal_pattern_flag(open, close, high, low).astype(bool)
    low52 = _rolling_min(close, _TD_YEAR)
    at_low = close <= low52 * 1.05
    return (flag & at_low).astype(float)


def rev_145_reversal_at_52wk_low_count_252d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of reversal patterns at/near 52-week low in trailing 252 days."""
    return _rolling_sum(rev_144_reversal_at_52wk_low_flag(open, close, high, low), _TD_YEAR)


def rev_146_reversal_vol_expansion_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Reversal pattern with volume >= 150% of 21-day average (strong conviction)."""
    flag = rev_133_any_reversal_pattern_flag(open, close, high, low).astype(bool)
    avg_vol = _rolling_mean(volume, _TD_MON)
    high_vol = volume >= avg_vol * 1.50
    return (flag & high_vol).astype(float)


def rev_147_any_pattern_recency_score_21d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Exponentially decayed any-reversal-pattern signal over 21-day EWM span."""
    flag = rev_133_any_reversal_pattern_flag(open, close, high, low)
    return flag.ewm(span=_TD_MON, min_periods=1).mean()


def rev_148_new_patterns_recency_score_21d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """EWM-decayed signal of the 6 new candlestick patterns over 21-day span."""
    flag = rev_132_any_new_pattern_flag(open, close, high, low)
    return flag.ewm(span=_TD_MON, min_periods=1).mean()


def rev_149_reversal_pattern_zscore_21d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Z-score of 21-day reversal pattern count relative to 252-day distribution."""
    count21 = rev_134_any_reversal_pattern_count_21d(open, close, high, low)
    m = _rolling_mean(count21, _TD_YEAR)
    s = _rolling_std(count21, _TD_YEAR)
    return _safe_div(count21 - m, s)


def rev_150_combined_reversal_distress_index(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Combined distress index: pattern-recency score * vol-norm * (1 + at-52wk-low flag)."""
    recency = rev_147_any_pattern_recency_score_21d(open, close, high, low)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    at_low_boost = 1.0 + rev_144_reversal_at_52wk_low_flag(open, close, high, low)
    return recency * vol_norm * at_low_boost


# ── Registry ──────────────────────────────────────────────────────────────────

REVERSAL_PATTERNS_REGISTRY_076_150 = {
    "rev_076_island_reversal_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_076_island_reversal_flag},
    "rev_077_island_reversal_near_low_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_077_island_reversal_near_low_flag},
    "rev_078_island_reversal_count_63d": {"inputs": ["open", "close", "high", "low"], "func": rev_078_island_reversal_count_63d},
    "rev_079_island_reversal_days_since": {"inputs": ["open", "close", "high", "low"], "func": rev_079_island_reversal_days_since},
    "rev_080_island_reversal_vol_spike": {"inputs": ["open", "close", "high", "low", "volume"], "func": rev_080_island_reversal_vol_spike},
    "rev_081_island_reversal_near_52wk_low": {"inputs": ["open", "close", "high", "low"], "func": rev_081_island_reversal_near_52wk_low},
    "rev_082_island_reversal_gap_magnitude": {"inputs": ["open", "close", "high", "low"], "func": rev_082_island_reversal_gap_magnitude},
    "rev_083_island_body_bull_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_083_island_body_bull_flag},
    "rev_084_three_white_soldiers_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_084_three_white_soldiers_flag},
    "rev_085_three_white_soldiers_near_low_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_085_three_white_soldiers_near_low_flag},
    "rev_086_three_white_soldiers_near_52wk_low": {"inputs": ["open", "close", "high", "low"], "func": rev_086_three_white_soldiers_near_52wk_low},
    "rev_087_three_white_soldiers_count_63d": {"inputs": ["open", "close", "high", "low"], "func": rev_087_three_white_soldiers_count_63d},
    "rev_088_three_white_soldiers_count_252d": {"inputs": ["open", "close", "high", "low"], "func": rev_088_three_white_soldiers_count_252d},
    "rev_089_three_white_soldiers_days_since": {"inputs": ["open", "close", "high", "low"], "func": rev_089_three_white_soldiers_days_since},
    "rev_090_three_white_soldiers_vol_confirm": {"inputs": ["open", "close", "high", "low", "volume"], "func": rev_090_three_white_soldiers_vol_confirm},
    "rev_091_three_white_soldiers_body_expansion": {"inputs": ["open", "close", "high", "low"], "func": rev_091_three_white_soldiers_body_expansion},
    "rev_092_abandoned_baby_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_092_abandoned_baby_flag},
    "rev_093_abandoned_baby_near_low_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_093_abandoned_baby_near_low_flag},
    "rev_094_abandoned_baby_near_52wk_low": {"inputs": ["open", "close", "high", "low"], "func": rev_094_abandoned_baby_near_52wk_low},
    "rev_095_abandoned_baby_count_252d": {"inputs": ["open", "close", "high", "low"], "func": rev_095_abandoned_baby_count_252d},
    "rev_096_abandoned_baby_days_since": {"inputs": ["open", "close", "high", "low"], "func": rev_096_abandoned_baby_days_since},
    "rev_097_abandoned_baby_gap_size": {"inputs": ["open", "close", "high", "low"], "func": rev_097_abandoned_baby_gap_size},
    "rev_098_abandoned_baby_vol_confirm": {"inputs": ["open", "close", "high", "low", "volume"], "func": rev_098_abandoned_baby_vol_confirm},
    "rev_099_kicker_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_099_kicker_flag},
    "rev_100_kicker_near_low_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_100_kicker_near_low_flag},
    "rev_101_kicker_near_52wk_low": {"inputs": ["open", "close", "high", "low"], "func": rev_101_kicker_near_52wk_low},
    "rev_102_kicker_count_21d": {"inputs": ["open", "close", "high", "low"], "func": rev_102_kicker_count_21d},
    "rev_103_kicker_count_63d": {"inputs": ["open", "close", "high", "low"], "func": rev_103_kicker_count_63d},
    "rev_104_kicker_days_since": {"inputs": ["open", "close", "high", "low"], "func": rev_104_kicker_days_since},
    "rev_105_kicker_gap_size_atr": {"inputs": ["open", "close", "high", "low"], "func": rev_105_kicker_gap_size_atr},
    "rev_106_kicker_vol_confirm": {"inputs": ["open", "close", "high", "low", "volume"], "func": rev_106_kicker_vol_confirm},
    "rev_107_kicker_count_252d": {"inputs": ["open", "close", "high", "low"], "func": rev_107_kicker_count_252d},
    "rev_108_belt_hold_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_108_belt_hold_flag},
    "rev_109_belt_hold_near_low_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_109_belt_hold_near_low_flag},
    "rev_110_belt_hold_near_52wk_low": {"inputs": ["open", "close", "high", "low"], "func": rev_110_belt_hold_near_52wk_low},
    "rev_111_belt_hold_count_21d": {"inputs": ["open", "close", "high", "low"], "func": rev_111_belt_hold_count_21d},
    "rev_112_belt_hold_count_63d": {"inputs": ["open", "close", "high", "low"], "func": rev_112_belt_hold_count_63d},
    "rev_113_belt_hold_days_since": {"inputs": ["open", "close", "high", "low"], "func": rev_113_belt_hold_days_since},
    "rev_114_belt_hold_body_atr_ratio": {"inputs": ["open", "close", "high", "low"], "func": rev_114_belt_hold_body_atr_ratio},
    "rev_115_belt_hold_vol_confirm": {"inputs": ["open", "close", "high", "low", "volume"], "func": rev_115_belt_hold_vol_confirm},
    "rev_116_three_inside_up_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_116_three_inside_up_flag},
    "rev_117_three_inside_up_near_low_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_117_three_inside_up_near_low_flag},
    "rev_118_three_inside_up_near_52wk_low": {"inputs": ["open", "close", "high", "low"], "func": rev_118_three_inside_up_near_52wk_low},
    "rev_119_three_inside_up_count_63d": {"inputs": ["open", "close", "high", "low"], "func": rev_119_three_inside_up_count_63d},
    "rev_120_three_inside_up_count_252d": {"inputs": ["open", "close", "high", "low"], "func": rev_120_three_inside_up_count_252d},
    "rev_121_three_inside_up_days_since": {"inputs": ["open", "close", "high", "low"], "func": rev_121_three_inside_up_days_since},
    "rev_122_three_inside_up_vol_confirm": {"inputs": ["open", "close", "high", "low", "volume"], "func": rev_122_three_inside_up_vol_confirm},
    "rev_123_three_inside_up_bar3_body_atr": {"inputs": ["open", "close", "high", "low"], "func": rev_123_three_inside_up_bar3_body_atr},
    "rev_124_three_outside_up_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_124_three_outside_up_flag},
    "rev_125_three_outside_up_near_low_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_125_three_outside_up_near_low_flag},
    "rev_126_three_outside_up_near_52wk_low": {"inputs": ["open", "close", "high", "low"], "func": rev_126_three_outside_up_near_52wk_low},
    "rev_127_three_outside_up_count_63d": {"inputs": ["open", "close", "high", "low"], "func": rev_127_three_outside_up_count_63d},
    "rev_128_three_outside_up_count_252d": {"inputs": ["open", "close", "high", "low"], "func": rev_128_three_outside_up_count_252d},
    "rev_129_three_outside_up_days_since": {"inputs": ["open", "close", "high", "low"], "func": rev_129_three_outside_up_days_since},
    "rev_130_three_outside_up_vol_confirm": {"inputs": ["open", "close", "high", "low", "volume"], "func": rev_130_three_outside_up_vol_confirm},
    "rev_131_three_outside_up_bar3_close_strength": {"inputs": ["open", "close", "high", "low"], "func": rev_131_three_outside_up_bar3_close_strength},
    "rev_132_any_new_pattern_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_132_any_new_pattern_flag},
    "rev_133_any_reversal_pattern_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_133_any_reversal_pattern_flag},
    "rev_134_any_reversal_pattern_count_21d": {"inputs": ["open", "close", "high", "low"], "func": rev_134_any_reversal_pattern_count_21d},
    "rev_135_any_reversal_pattern_count_63d": {"inputs": ["open", "close", "high", "low"], "func": rev_135_any_reversal_pattern_count_63d},
    "rev_136_any_reversal_pattern_count_252d": {"inputs": ["open", "close", "high", "low"], "func": rev_136_any_reversal_pattern_count_252d},
    "rev_137_simultaneous_pattern_count": {"inputs": ["open", "close", "high", "low"], "func": rev_137_simultaneous_pattern_count},
    "rev_138_reversal_density_21d": {"inputs": ["open", "close", "high", "low"], "func": rev_138_reversal_density_21d},
    "rev_139_reversal_density_63d": {"inputs": ["open", "close", "high", "low"], "func": rev_139_reversal_density_63d},
    "rev_140_any_reversal_days_since": {"inputs": ["open", "close", "high", "low"], "func": rev_140_any_reversal_days_since},
    "rev_141_reversal_cluster_21d_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_141_reversal_cluster_21d_flag},
    "rev_142_reversal_after_5d_decline_count_63d": {"inputs": ["open", "close", "high", "low"], "func": rev_142_reversal_after_5d_decline_count_63d},
    "rev_143_reversal_below_sma50_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_143_reversal_below_sma50_flag},
    "rev_144_reversal_at_52wk_low_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_144_reversal_at_52wk_low_flag},
    "rev_145_reversal_at_52wk_low_count_252d": {"inputs": ["open", "close", "high", "low"], "func": rev_145_reversal_at_52wk_low_count_252d},
    "rev_146_reversal_vol_expansion_flag": {"inputs": ["open", "close", "high", "low", "volume"], "func": rev_146_reversal_vol_expansion_flag},
    "rev_147_any_pattern_recency_score_21d": {"inputs": ["open", "close", "high", "low"], "func": rev_147_any_pattern_recency_score_21d},
    "rev_148_new_patterns_recency_score_21d": {"inputs": ["open", "close", "high", "low"], "func": rev_148_new_patterns_recency_score_21d},
    "rev_149_reversal_pattern_zscore_21d": {"inputs": ["open", "close", "high", "low"], "func": rev_149_reversal_pattern_zscore_21d},
    "rev_150_combined_reversal_distress_index": {"inputs": ["open", "close", "high", "low", "volume"], "func": rev_150_combined_reversal_distress_index},
}
