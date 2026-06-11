"""
49_reversal_patterns — Base Features 001-075
Domain: intraday/multi-bar named reversal candlestick pattern recognition at/near lows
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
Patterns: bullish engulfing, hammer / inverted hammer, piercing line, morning star
(and morning doji star), bullish harami, tweezer bottom, key / outside reversal.
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


def _body(o: pd.Series, c: pd.Series) -> pd.Series:
    """Signed body: positive for bull candle, negative for bear."""
    return c - o


def _body_abs(o: pd.Series, c: pd.Series) -> pd.Series:
    """Absolute body size."""
    return (c - o).abs()


def _range(h: pd.Series, l: pd.Series) -> pd.Series:
    """High-low range."""
    return (h - l).replace(0, np.nan)


def _upper_wick(o: pd.Series, c: pd.Series, h: pd.Series) -> pd.Series:
    """Upper shadow = high minus the higher of open/close."""
    return h - pd.concat([o, c], axis=1).max(axis=1)


def _lower_wick(o: pd.Series, c: pd.Series, l: pd.Series) -> pd.Series:
    """Lower shadow = the lower of open/close minus low."""
    return pd.concat([o, c], axis=1).min(axis=1) - l


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    """Count of True values in trailing w periods."""
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


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


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Bullish Engulfing ---

def rev_001_bullish_engulfing_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: classic 2-bar bullish engulfing (prior bear bar entirely engulfed by today's bull bar)."""
    prev_bear = close.shift(1) < open.shift(1)
    today_bull = close > open
    engulfs_body = (open <= close.shift(1)) & (close >= open.shift(1))
    return (prev_bear & today_bull & engulfs_body).astype(float)


def rev_002_bullish_engulfing_near_low_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Bullish engulfing occurring when price is near a 21-day closing low."""
    eng = rev_001_bullish_engulfing_flag(open, close, high, low).astype(bool)
    near = _near_low(close, low, _TD_MON)
    return (eng & near).astype(float)


def rev_003_bullish_engulfing_body_ratio(
    open: pd.Series, close: pd.Series
) -> pd.Series:
    """On engulfing days: ratio of today's body to prior bar's body (engulfment size)."""
    prev_bear = close.shift(1) < open.shift(1)
    today_bull = close > open
    engulfs_body = (open <= close.shift(1)) & (close >= open.shift(1))
    flag = prev_bear & today_bull & engulfs_body
    today_body = _body_abs(open, close)
    prior_body = _body_abs(open.shift(1), close.shift(1)).replace(0, np.nan)
    ratio = today_body / prior_body
    return ratio.where(flag, 0.0)


def rev_004_bullish_engulfing_vol_confirm(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Bullish engulfing with volume on engulfing day above 21-day average volume."""
    eng = rev_001_bullish_engulfing_flag(open, close, high, low).astype(bool)
    avg_vol = _rolling_mean(volume, _TD_MON)
    return (eng & (volume > avg_vol)).astype(float)


def rev_005_bullish_engulfing_count_21d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of bullish engulfing patterns in the trailing 21 days."""
    flag = rev_001_bullish_engulfing_flag(open, close, high, low)
    return _rolling_sum(flag, _TD_MON)


def rev_006_bullish_engulfing_count_63d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of bullish engulfing patterns in the trailing 63 days."""
    flag = rev_001_bullish_engulfing_flag(open, close, high, low)
    return _rolling_sum(flag, _TD_QTR)


def rev_007_bullish_engulfing_strength(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Engulfing strength: bull-body size relative to ATR on pattern days, else 0."""
    flag = rev_001_bullish_engulfing_flag(open, close, high, low).astype(bool)
    atr14 = _atr(close, high, low, 14)
    strength = _safe_div(_body_abs(open, close), atr14)
    return strength.where(flag, 0.0)


def rev_008_bullish_engulfing_days_since(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Days elapsed since the most recent bullish engulfing pattern (recency)."""
    flag = rev_001_bullish_engulfing_flag(open, close, high, low).astype(bool)
    return _days_since(flag)


def rev_009_bullish_engulfing_near_52wk_low(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Bullish engulfing occurring within 10% of the 252-day closing low."""
    eng = rev_001_bullish_engulfing_flag(open, close, high, low).astype(bool)
    low52 = _rolling_min(close, _TD_YEAR)
    near = close <= low52 * 1.10
    return (eng & near).astype(float)


def rev_010_bullish_engulfing_pct_rank_252d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Percentile rank of 21-day engulfing count within trailing 252 days."""
    count21 = rev_005_bullish_engulfing_count_21d(open, close, high, low)
    return count21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group B (011-020): Hammer and Inverted Hammer ---

def rev_011_hammer_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: hammer — small body in upper half of range, long lower wick >= 2x body."""
    rng = _range(high, low)
    body = _body_abs(open, close)
    lw = _lower_wick(open, close, low)
    uw = _upper_wick(open, close, high)
    small_body = body <= rng * 0.33
    long_lower = lw >= body * 2.0
    short_upper = uw <= body * 0.5
    body_upper_half = pd.concat([open, close], axis=1).min(axis=1) >= low + rng * 0.5
    return (small_body & long_lower & short_upper & body_upper_half).astype(float)


def rev_012_hammer_near_low_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Hammer pattern at/near the 21-day closing low."""
    h = rev_011_hammer_flag(open, close, high, low).astype(bool)
    near = _near_low(close, low, _TD_MON)
    return (h & near).astype(float)


def rev_013_hammer_lower_wick_ratio(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """On hammer days: lower wick as fraction of total range; else 0."""
    flag = rev_011_hammer_flag(open, close, high, low).astype(bool)
    rng = _range(high, low)
    lw = _lower_wick(open, close, low)
    ratio = _safe_div(lw, rng)
    return ratio.where(flag, 0.0)


def rev_014_hammer_count_21d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of hammer patterns in trailing 21 days."""
    return _rolling_sum(rev_011_hammer_flag(open, close, high, low), _TD_MON)


def rev_015_hammer_count_63d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of hammer patterns in trailing 63 days."""
    return _rolling_sum(rev_011_hammer_flag(open, close, high, low), _TD_QTR)


def rev_016_inverted_hammer_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: inverted hammer — small body in lower half, long upper wick >= 2x body."""
    rng = _range(high, low)
    body = _body_abs(open, close)
    lw = _lower_wick(open, close, low)
    uw = _upper_wick(open, close, high)
    small_body = body <= rng * 0.33
    long_upper = uw >= body * 2.0
    short_lower = lw <= body * 0.5
    body_lower_half = pd.concat([open, close], axis=1).max(axis=1) <= low + rng * 0.5
    return (small_body & long_upper & short_lower & body_lower_half).astype(float)


def rev_017_inverted_hammer_near_low_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Inverted hammer at/near the 21-day closing low."""
    ih = rev_016_inverted_hammer_flag(open, close, high, low).astype(bool)
    near = _near_low(close, low, _TD_MON)
    return (ih & near).astype(float)


def rev_018_inverted_hammer_count_21d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of inverted hammer patterns in trailing 21 days."""
    return _rolling_sum(rev_016_inverted_hammer_flag(open, close, high, low), _TD_MON)


def rev_019_hammer_or_inverted_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: either hammer or inverted hammer on the current bar."""
    h = rev_011_hammer_flag(open, close, high, low)
    ih = rev_016_inverted_hammer_flag(open, close, high, low)
    return ((h + ih) > 0).astype(float)


def rev_020_hammer_days_since(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Days elapsed since most recent hammer or inverted hammer."""
    flag = rev_019_hammer_or_inverted_flag(open, close, high, low).astype(bool)
    return _days_since(flag)


# --- Group C (021-030): Piercing Line ---

def rev_021_piercing_line_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: piercing line — prior bear candle, today opens below prior low, closes above prior midpoint."""
    prev_bear = close.shift(1) < open.shift(1)
    prior_mid = (open.shift(1) + close.shift(1)) / 2.0
    opens_below_prior_low = open < low.shift(1)
    closes_above_prior_mid = close > prior_mid
    today_bull = close > open
    return (prev_bear & opens_below_prior_low & closes_above_prior_mid & today_bull).astype(float)


def rev_022_piercing_line_near_low_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Piercing line at/near the 21-day closing low."""
    pl = rev_021_piercing_line_flag(open, close, high, low).astype(bool)
    near = _near_low(close, low, _TD_MON)
    return (pl & near).astype(float)


def rev_023_piercing_line_penetration_depth(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Piercing depth: fraction of prior bear body recovered today (0-1 scale, on pattern days)."""
    flag = rev_021_piercing_line_flag(open, close, high, low).astype(bool)
    prior_body_top = open.shift(1)
    prior_body_bot = close.shift(1)
    prior_body = (prior_body_top - prior_body_bot).replace(0, np.nan)
    penetration = (close - prior_body_bot) / prior_body
    return penetration.clip(0, 1).where(flag, 0.0)


def rev_024_piercing_line_count_21d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of piercing line patterns in trailing 21 days."""
    return _rolling_sum(rev_021_piercing_line_flag(open, close, high, low), _TD_MON)


def rev_025_piercing_line_count_63d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of piercing line patterns in trailing 63 days."""
    return _rolling_sum(rev_021_piercing_line_flag(open, close, high, low), _TD_QTR)


def rev_026_piercing_line_vol_confirm(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Piercing line on above-average volume (stronger signal)."""
    pl = rev_021_piercing_line_flag(open, close, high, low).astype(bool)
    avg_vol = _rolling_mean(volume, _TD_MON)
    return (pl & (volume > avg_vol)).astype(float)


def rev_027_piercing_line_days_since(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Days since most recent piercing line pattern."""
    flag = rev_021_piercing_line_flag(open, close, high, low).astype(bool)
    return _days_since(flag)


def rev_028_piercing_line_near_52wk_low(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Piercing line within 10% of the 252-day closing low."""
    pl = rev_021_piercing_line_flag(open, close, high, low).astype(bool)
    low52 = _rolling_min(close, _TD_YEAR)
    near = close <= low52 * 1.10
    return (pl & near).astype(float)


def rev_029_piercing_or_engulfing_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: either piercing line or bullish engulfing on the current bar."""
    pl = rev_021_piercing_line_flag(open, close, high, low)
    eng = rev_001_bullish_engulfing_flag(open, close, high, low)
    return ((pl + eng) > 0).astype(float)


def rev_030_piercing_or_engulfing_count_63d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of piercing line or bullish engulfing in trailing 63 days."""
    return _rolling_sum(rev_029_piercing_or_engulfing_flag(open, close, high, low), _TD_QTR)


# --- Group D (031-040): Morning Star (3-bar) ---

def rev_031_morning_star_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: classic 3-bar morning star (bear, small doji-like, bull recovering past bar-1 midpoint)."""
    bar1_bear = close.shift(2) < open.shift(2)
    bar1_body = _body_abs(open.shift(2), close.shift(2))
    bar2_small = _body_abs(open.shift(1), close.shift(1)) <= bar1_body * 0.35
    bar3_bull = close > open
    bar3_recovers = close > (open.shift(2) + close.shift(2)) / 2.0
    return (bar1_bear & bar2_small & bar3_bull & bar3_recovers).astype(float)


def rev_032_morning_star_near_low_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Morning star completing at/near the 21-day closing low."""
    ms = rev_031_morning_star_flag(open, close, high, low).astype(bool)
    near = _near_low(close, low, _TD_MON)
    return (ms & near).astype(float)


def rev_033_morning_star_count_63d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of morning star patterns completing in trailing 63 days."""
    return _rolling_sum(rev_031_morning_star_flag(open, close, high, low), _TD_QTR)


def rev_034_morning_star_count_252d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of morning star patterns completing in trailing 252 days."""
    return _rolling_sum(rev_031_morning_star_flag(open, close, high, low), _TD_YEAR)


def rev_035_morning_star_bar2_wick_ratio(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """On morning-star bars: lower wick of bar-2 (doji) as fraction of bar-2 range; else 0."""
    flag = rev_031_morning_star_flag(open, close, high, low).astype(bool)
    lw2 = _lower_wick(open.shift(1), close.shift(1), low.shift(1))
    rng2 = _range(high.shift(1), low.shift(1))
    ratio = _safe_div(lw2, rng2)
    return ratio.where(flag, 0.0)


def rev_036_morning_star_vol_confirm(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Morning star where bar-3 volume exceeds bar-1 volume (expanding interest)."""
    ms = rev_031_morning_star_flag(open, close, high, low).astype(bool)
    bar3_vol_up = volume > volume.shift(2)
    return (ms & bar3_vol_up).astype(float)


def rev_037_morning_star_days_since(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Days elapsed since most recent morning star pattern completion."""
    flag = rev_031_morning_star_flag(open, close, high, low).astype(bool)
    return _days_since(flag)


def rev_038_morning_star_recovery_depth(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """On morning star bars: fraction of bar-1 body recovered by bar-3 close; else 0."""
    flag = rev_031_morning_star_flag(open, close, high, low).astype(bool)
    bar1_top = open.shift(2)
    bar1_bot = close.shift(2)
    bar1_body = (bar1_top - bar1_bot).replace(0, np.nan)
    recovery = (close - bar1_bot) / bar1_body
    return recovery.clip(0, 2).where(flag, 0.0)


def rev_039_morning_doji_star_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Morning doji star: bar-2 is a true doji (body <= 5% of range) within 3-bar morning star."""
    ms_base = (
        (close.shift(2) < open.shift(2))
        & (close > open)
        & (close > (open.shift(2) + close.shift(2)) / 2.0)
    )
    rng2 = _range(high.shift(1), low.shift(1))
    body2 = _body_abs(open.shift(1), close.shift(1))
    is_doji = body2 <= rng2 * 0.05
    return (ms_base & is_doji).astype(float)


def rev_040_morning_star_near_52wk_low(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Morning star completing within 10% of 252-day closing low."""
    ms = rev_031_morning_star_flag(open, close, high, low).astype(bool)
    low52 = _rolling_min(close, _TD_YEAR)
    near = close <= low52 * 1.10
    return (ms & near).astype(float)


# --- Group E (041-050): Bullish Harami ---

def rev_041_bullish_harami_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: bullish harami — large prior bear bar contains today's small bull bar inside."""
    prev_bear = close.shift(1) < open.shift(1)
    today_bull = close > open
    contained = (
        (open > close.shift(1)) & (open < open.shift(1))
        & (close > close.shift(1)) & (close < open.shift(1))
    )
    return (prev_bear & today_bull & contained).astype(float)


def rev_042_bullish_harami_near_low_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Bullish harami at/near the 21-day closing low."""
    bh = rev_041_bullish_harami_flag(open, close, high, low).astype(bool)
    near = _near_low(close, low, _TD_MON)
    return (bh & near).astype(float)


def rev_043_bullish_harami_inner_body_ratio(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Harami: inner (today) body as fraction of outer (prior) body on pattern days."""
    flag = rev_041_bullish_harami_flag(open, close, high, low).astype(bool)
    inner = _body_abs(open, close)
    outer = _body_abs(open.shift(1), close.shift(1)).replace(0, np.nan)
    ratio = inner / outer
    return ratio.where(flag, 0.0)


def rev_044_bullish_harami_count_21d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of bullish harami patterns in trailing 21 days."""
    return _rolling_sum(rev_041_bullish_harami_flag(open, close, high, low), _TD_MON)


def rev_045_bullish_harami_count_63d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of bullish harami patterns in trailing 63 days."""
    return _rolling_sum(rev_041_bullish_harami_flag(open, close, high, low), _TD_QTR)


def rev_046_bullish_harami_days_since(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Days since most recent bullish harami pattern."""
    flag = rev_041_bullish_harami_flag(open, close, high, low).astype(bool)
    return _days_since(flag)


def rev_047_bullish_harami_cross_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Bullish harami cross: inner bar is a doji (body <= 5% of prior bar's body range)."""
    bh = rev_041_bullish_harami_flag(open, close, high, low).astype(bool)
    rng_prior = _range(high.shift(1), low.shift(1))
    body_today = _body_abs(open, close)
    is_doji = body_today <= rng_prior * 0.05
    return (bh & is_doji).astype(float)


def rev_048_bullish_harami_vol_expand(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Bullish harami where inner-bar volume is below prior bar (typical harami vol signature)."""
    bh = rev_041_bullish_harami_flag(open, close, high, low).astype(bool)
    vol_contracting = volume < volume.shift(1)
    return (bh & vol_contracting).astype(float)


def rev_049_harami_or_engulfing_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: either bullish harami or bullish engulfing on the current bar."""
    bh = rev_041_bullish_harami_flag(open, close, high, low)
    eng = rev_001_bullish_engulfing_flag(open, close, high, low)
    return ((bh + eng) > 0).astype(float)


def rev_050_harami_or_engulfing_count_63d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of bullish harami or engulfing patterns in trailing 63 days."""
    return _rolling_sum(rev_049_harami_or_engulfing_flag(open, close, high, low), _TD_QTR)


# --- Group F (051-060): Tweezer Bottom ---

def rev_051_tweezer_bottom_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Tweezer bottom: consecutive bars with matching lows (within 0.1% of ATR) after a down move."""
    atr14 = _atr(close, high, low, 14)
    tol = atr14 * 0.10
    matching_lows = (low - low.shift(1)).abs() <= tol
    prior_down = close.shift(1) < close.shift(2)
    return (matching_lows & prior_down).astype(float)


def rev_052_tweezer_bottom_near_low_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Tweezer bottom at/near the 21-day closing low."""
    tb = rev_051_tweezer_bottom_flag(open, close, high, low).astype(bool)
    near = _near_low(close, low, _TD_MON)
    return (tb & near).astype(float)


def rev_053_tweezer_bottom_count_21d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of tweezer bottom patterns in trailing 21 days."""
    return _rolling_sum(rev_051_tweezer_bottom_flag(open, close, high, low), _TD_MON)


def rev_054_tweezer_bottom_count_63d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of tweezer bottom patterns in trailing 63 days."""
    return _rolling_sum(rev_051_tweezer_bottom_flag(open, close, high, low), _TD_QTR)


def rev_055_tweezer_bottom_low_proximity(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """On tweezer days: how close the shared low is to the 21-day rolling min (0 = at min)."""
    flag = rev_051_tweezer_bottom_flag(open, close, high, low).astype(bool)
    low21 = _rolling_min(low, _TD_MON)
    atr14 = _atr(close, high, low, 14)
    dist = _safe_div(low - low21, atr14)
    return dist.where(flag, np.nan)


def rev_056_tweezer_bottom_vol_expand(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Tweezer bottom where today's volume exceeds prior bar (interest spike at low)."""
    tb = rev_051_tweezer_bottom_flag(open, close, high, low).astype(bool)
    vol_up = volume > volume.shift(1)
    return (tb & vol_up).astype(float)


def rev_057_tweezer_bottom_days_since(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Days since most recent tweezer bottom."""
    flag = rev_051_tweezer_bottom_flag(open, close, high, low).astype(bool)
    return _days_since(flag)


def rev_058_tweezer_bottom_bull_close(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Tweezer bottom where today's bar closes higher than prior bar (extra bullish variant)."""
    tb = rev_051_tweezer_bottom_flag(open, close, high, low).astype(bool)
    closes_higher = close > close.shift(1)
    return (tb & closes_higher).astype(float)


def rev_059_tweezer_bottom_strict_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Strict tweezer bottom: lows match exactly AND first bar is bear, second is bull."""
    atr14 = _atr(close, high, low, 14)
    tol = atr14 * 0.05
    exact_low = (low - low.shift(1)).abs() <= tol
    bar1_bear = close.shift(1) < open.shift(1)
    bar2_bull = close > open
    return (exact_low & bar1_bear & bar2_bull).astype(float)


def rev_060_tweezer_bottom_near_52wk_low(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Tweezer bottom within 10% of the 252-day closing low."""
    tb = rev_051_tweezer_bottom_flag(open, close, high, low).astype(bool)
    low52 = _rolling_min(close, _TD_YEAR)
    near = close <= low52 * 1.10
    return (tb & near).astype(float)


# --- Group G (061-075): Key Reversal Day and Outside-Up Bar ---

def rev_061_key_reversal_day_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Key reversal day: sets new N-day low intraday but closes ABOVE prior close."""
    new_low = low < _rolling_min(low.shift(1), _TD_MON)
    closes_up = close > close.shift(1)
    return (new_low & closes_up).astype(float)


def rev_062_key_reversal_day_near_low_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Key reversal day at/near the 63-day closing low."""
    krd = rev_061_key_reversal_day_flag(open, close, high, low).astype(bool)
    near = _near_low(close, low, _TD_QTR)
    return (krd & near).astype(float)


def rev_063_key_reversal_day_count_21d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of key reversal days in trailing 21 days."""
    return _rolling_sum(rev_061_key_reversal_day_flag(open, close, high, low), _TD_MON)


def rev_064_key_reversal_day_count_63d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of key reversal days in trailing 63 days."""
    return _rolling_sum(rev_061_key_reversal_day_flag(open, close, high, low), _TD_QTR)


def rev_065_key_reversal_day_low_undercut_depth(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Key reversal: depth of intraday undercut below prior rolling low (ATR-normalized); else 0."""
    flag = rev_061_key_reversal_day_flag(open, close, high, low).astype(bool)
    prior_low = _rolling_min(low.shift(1), _TD_MON)
    atr14 = _atr(close, high, low, 14)
    depth = _safe_div(prior_low - low, atr14)
    return depth.where(flag, 0.0)


def rev_066_key_reversal_day_vol_confirm(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Key reversal day with above-average volume."""
    krd = rev_061_key_reversal_day_flag(open, close, high, low).astype(bool)
    avg_vol = _rolling_mean(volume, _TD_MON)
    return (krd & (volume > avg_vol)).astype(float)


def rev_067_key_reversal_day_days_since(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Days since most recent key reversal day."""
    flag = rev_061_key_reversal_day_flag(open, close, high, low).astype(bool)
    return _days_since(flag)


def rev_068_outside_up_reversal_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Outside-up reversal bar: today's range fully outside prior range AND closes up strongly."""
    outside = (high > high.shift(1)) & (low < low.shift(1))
    closes_bull = close > open
    closes_near_high = close >= (low + (high - low) * 0.60)
    return (outside & closes_bull & closes_near_high).astype(float)


def rev_069_outside_up_reversal_near_low_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Outside-up reversal at/near the 21-day closing low."""
    ou = rev_068_outside_up_reversal_flag(open, close, high, low).astype(bool)
    near = _near_low(close, low, _TD_MON)
    return (ou & near).astype(float)


def rev_070_outside_up_reversal_count_63d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of outside-up reversal bars in trailing 63 days."""
    return _rolling_sum(rev_068_outside_up_reversal_flag(open, close, high, low), _TD_QTR)


def rev_071_outside_up_reversal_range_ratio(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Outside-up reversal: today's range relative to prior bar's range on pattern days."""
    flag = rev_068_outside_up_reversal_flag(open, close, high, low).astype(bool)
    today_rng = _range(high, low)
    prior_rng = _range(high.shift(1), low.shift(1))
    ratio = _safe_div(today_rng, prior_rng)
    return ratio.where(flag, 0.0)


def rev_072_outside_up_reversal_days_since(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Days since most recent outside-up reversal bar."""
    flag = rev_068_outside_up_reversal_flag(open, close, high, low).astype(bool)
    return _days_since(flag)


def rev_073_key_reversal_or_outside_up_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: either key reversal day or outside-up bar on the current bar."""
    krd = rev_061_key_reversal_day_flag(open, close, high, low)
    ou = rev_068_outside_up_reversal_flag(open, close, high, low)
    return ((krd + ou) > 0).astype(float)


def rev_074_key_reversal_or_outside_up_count_63d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of key reversal or outside-up bars in trailing 63 days."""
    return _rolling_sum(rev_073_key_reversal_or_outside_up_flag(open, close, high, low), _TD_QTR)


def rev_075_key_reversal_near_52wk_low(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Key reversal day within 10% of 252-day closing low."""
    krd = rev_061_key_reversal_day_flag(open, close, high, low).astype(bool)
    low52 = _rolling_min(close, _TD_YEAR)
    near = close <= low52 * 1.10
    return (krd & near).astype(float)


# ── Registry ──────────────────────────────────────────────────────────────────

REVERSAL_PATTERNS_REGISTRY_001_075 = {
    "rev_001_bullish_engulfing_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_001_bullish_engulfing_flag},
    "rev_002_bullish_engulfing_near_low_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_002_bullish_engulfing_near_low_flag},
    "rev_003_bullish_engulfing_body_ratio": {"inputs": ["open", "close"], "func": rev_003_bullish_engulfing_body_ratio},
    "rev_004_bullish_engulfing_vol_confirm": {"inputs": ["open", "close", "high", "low", "volume"], "func": rev_004_bullish_engulfing_vol_confirm},
    "rev_005_bullish_engulfing_count_21d": {"inputs": ["open", "close", "high", "low"], "func": rev_005_bullish_engulfing_count_21d},
    "rev_006_bullish_engulfing_count_63d": {"inputs": ["open", "close", "high", "low"], "func": rev_006_bullish_engulfing_count_63d},
    "rev_007_bullish_engulfing_strength": {"inputs": ["open", "close", "high", "low"], "func": rev_007_bullish_engulfing_strength},
    "rev_008_bullish_engulfing_days_since": {"inputs": ["open", "close", "high", "low"], "func": rev_008_bullish_engulfing_days_since},
    "rev_009_bullish_engulfing_near_52wk_low": {"inputs": ["open", "close", "high", "low"], "func": rev_009_bullish_engulfing_near_52wk_low},
    "rev_010_bullish_engulfing_pct_rank_252d": {"inputs": ["open", "close", "high", "low"], "func": rev_010_bullish_engulfing_pct_rank_252d},
    "rev_011_hammer_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_011_hammer_flag},
    "rev_012_hammer_near_low_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_012_hammer_near_low_flag},
    "rev_013_hammer_lower_wick_ratio": {"inputs": ["open", "close", "high", "low"], "func": rev_013_hammer_lower_wick_ratio},
    "rev_014_hammer_count_21d": {"inputs": ["open", "close", "high", "low"], "func": rev_014_hammer_count_21d},
    "rev_015_hammer_count_63d": {"inputs": ["open", "close", "high", "low"], "func": rev_015_hammer_count_63d},
    "rev_016_inverted_hammer_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_016_inverted_hammer_flag},
    "rev_017_inverted_hammer_near_low_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_017_inverted_hammer_near_low_flag},
    "rev_018_inverted_hammer_count_21d": {"inputs": ["open", "close", "high", "low"], "func": rev_018_inverted_hammer_count_21d},
    "rev_019_hammer_or_inverted_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_019_hammer_or_inverted_flag},
    "rev_020_hammer_days_since": {"inputs": ["open", "close", "high", "low"], "func": rev_020_hammer_days_since},
    "rev_021_piercing_line_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_021_piercing_line_flag},
    "rev_022_piercing_line_near_low_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_022_piercing_line_near_low_flag},
    "rev_023_piercing_line_penetration_depth": {"inputs": ["open", "close", "high", "low"], "func": rev_023_piercing_line_penetration_depth},
    "rev_024_piercing_line_count_21d": {"inputs": ["open", "close", "high", "low"], "func": rev_024_piercing_line_count_21d},
    "rev_025_piercing_line_count_63d": {"inputs": ["open", "close", "high", "low"], "func": rev_025_piercing_line_count_63d},
    "rev_026_piercing_line_vol_confirm": {"inputs": ["open", "close", "high", "low", "volume"], "func": rev_026_piercing_line_vol_confirm},
    "rev_027_piercing_line_days_since": {"inputs": ["open", "close", "high", "low"], "func": rev_027_piercing_line_days_since},
    "rev_028_piercing_line_near_52wk_low": {"inputs": ["open", "close", "high", "low"], "func": rev_028_piercing_line_near_52wk_low},
    "rev_029_piercing_or_engulfing_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_029_piercing_or_engulfing_flag},
    "rev_030_piercing_or_engulfing_count_63d": {"inputs": ["open", "close", "high", "low"], "func": rev_030_piercing_or_engulfing_count_63d},
    "rev_031_morning_star_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_031_morning_star_flag},
    "rev_032_morning_star_near_low_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_032_morning_star_near_low_flag},
    "rev_033_morning_star_count_63d": {"inputs": ["open", "close", "high", "low"], "func": rev_033_morning_star_count_63d},
    "rev_034_morning_star_count_252d": {"inputs": ["open", "close", "high", "low"], "func": rev_034_morning_star_count_252d},
    "rev_035_morning_star_bar2_wick_ratio": {"inputs": ["open", "close", "high", "low"], "func": rev_035_morning_star_bar2_wick_ratio},
    "rev_036_morning_star_vol_confirm": {"inputs": ["open", "close", "high", "low", "volume"], "func": rev_036_morning_star_vol_confirm},
    "rev_037_morning_star_days_since": {"inputs": ["open", "close", "high", "low"], "func": rev_037_morning_star_days_since},
    "rev_038_morning_star_recovery_depth": {"inputs": ["open", "close", "high", "low"], "func": rev_038_morning_star_recovery_depth},
    "rev_039_morning_doji_star_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_039_morning_doji_star_flag},
    "rev_040_morning_star_near_52wk_low": {"inputs": ["open", "close", "high", "low"], "func": rev_040_morning_star_near_52wk_low},
    "rev_041_bullish_harami_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_041_bullish_harami_flag},
    "rev_042_bullish_harami_near_low_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_042_bullish_harami_near_low_flag},
    "rev_043_bullish_harami_inner_body_ratio": {"inputs": ["open", "close", "high", "low"], "func": rev_043_bullish_harami_inner_body_ratio},
    "rev_044_bullish_harami_count_21d": {"inputs": ["open", "close", "high", "low"], "func": rev_044_bullish_harami_count_21d},
    "rev_045_bullish_harami_count_63d": {"inputs": ["open", "close", "high", "low"], "func": rev_045_bullish_harami_count_63d},
    "rev_046_bullish_harami_days_since": {"inputs": ["open", "close", "high", "low"], "func": rev_046_bullish_harami_days_since},
    "rev_047_bullish_harami_cross_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_047_bullish_harami_cross_flag},
    "rev_048_bullish_harami_vol_expand": {"inputs": ["open", "close", "high", "low", "volume"], "func": rev_048_bullish_harami_vol_expand},
    "rev_049_harami_or_engulfing_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_049_harami_or_engulfing_flag},
    "rev_050_harami_or_engulfing_count_63d": {"inputs": ["open", "close", "high", "low"], "func": rev_050_harami_or_engulfing_count_63d},
    "rev_051_tweezer_bottom_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_051_tweezer_bottom_flag},
    "rev_052_tweezer_bottom_near_low_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_052_tweezer_bottom_near_low_flag},
    "rev_053_tweezer_bottom_count_21d": {"inputs": ["open", "close", "high", "low"], "func": rev_053_tweezer_bottom_count_21d},
    "rev_054_tweezer_bottom_count_63d": {"inputs": ["open", "close", "high", "low"], "func": rev_054_tweezer_bottom_count_63d},
    "rev_055_tweezer_bottom_low_proximity": {"inputs": ["open", "close", "high", "low"], "func": rev_055_tweezer_bottom_low_proximity},
    "rev_056_tweezer_bottom_vol_expand": {"inputs": ["open", "close", "high", "low", "volume"], "func": rev_056_tweezer_bottom_vol_expand},
    "rev_057_tweezer_bottom_days_since": {"inputs": ["open", "close", "high", "low"], "func": rev_057_tweezer_bottom_days_since},
    "rev_058_tweezer_bottom_bull_close": {"inputs": ["open", "close", "high", "low"], "func": rev_058_tweezer_bottom_bull_close},
    "rev_059_tweezer_bottom_strict_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_059_tweezer_bottom_strict_flag},
    "rev_060_tweezer_bottom_near_52wk_low": {"inputs": ["open", "close", "high", "low"], "func": rev_060_tweezer_bottom_near_52wk_low},
    "rev_061_key_reversal_day_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_061_key_reversal_day_flag},
    "rev_062_key_reversal_day_near_low_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_062_key_reversal_day_near_low_flag},
    "rev_063_key_reversal_day_count_21d": {"inputs": ["open", "close", "high", "low"], "func": rev_063_key_reversal_day_count_21d},
    "rev_064_key_reversal_day_count_63d": {"inputs": ["open", "close", "high", "low"], "func": rev_064_key_reversal_day_count_63d},
    "rev_065_key_reversal_day_low_undercut_depth": {"inputs": ["open", "close", "high", "low"], "func": rev_065_key_reversal_day_low_undercut_depth},
    "rev_066_key_reversal_day_vol_confirm": {"inputs": ["open", "close", "high", "low", "volume"], "func": rev_066_key_reversal_day_vol_confirm},
    "rev_067_key_reversal_day_days_since": {"inputs": ["open", "close", "high", "low"], "func": rev_067_key_reversal_day_days_since},
    "rev_068_outside_up_reversal_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_068_outside_up_reversal_flag},
    "rev_069_outside_up_reversal_near_low_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_069_outside_up_reversal_near_low_flag},
    "rev_070_outside_up_reversal_count_63d": {"inputs": ["open", "close", "high", "low"], "func": rev_070_outside_up_reversal_count_63d},
    "rev_071_outside_up_reversal_range_ratio": {"inputs": ["open", "close", "high", "low"], "func": rev_071_outside_up_reversal_range_ratio},
    "rev_072_outside_up_reversal_days_since": {"inputs": ["open", "close", "high", "low"], "func": rev_072_outside_up_reversal_days_since},
    "rev_073_key_reversal_or_outside_up_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_073_key_reversal_or_outside_up_flag},
    "rev_074_key_reversal_or_outside_up_count_63d": {"inputs": ["open", "close", "high", "low"], "func": rev_074_key_reversal_or_outside_up_count_63d},
    "rev_075_key_reversal_near_52wk_low": {"inputs": ["open", "close", "high", "low"], "func": rev_075_key_reversal_near_52wk_low},
}
