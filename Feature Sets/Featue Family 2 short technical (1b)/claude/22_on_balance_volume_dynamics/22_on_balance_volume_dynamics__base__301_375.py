"""on_balance_volume_dynamics base features 301-375 — Pipeline 1b-technical (extension #3).

ML-focused individual signals: OBV behavior on specific candle patterns, calendar effects,
OBV trend events, divergence patterns, OBV zone/level signals, momentum events.

Inputs: SEP OHLCV only. PIT-clean. Self-contained helpers.
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


def _consecutive_true_streak(b):
    grp = (~b.fillna(False)).cumsum()
    return b.fillna(False).astype(int).groupby(grp).cumsum()


def _obv(close, volume):
    sgn = np.sign(close.diff()).fillna(0.0)
    return (sgn * volume).cumsum()


def _safe_dow(idx, target):
    if isinstance(idx, pd.DatetimeIndex):
        return pd.Series((idx.dayofweek == target).astype(float), index=idx)
    return pd.Series(np.nan, index=idx)


# Bucket BA — OBV-diff on candle patterns (301-315)

def f22_obvd_301_obv_diff_on_doji_at_252d_high_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean OBV-diff z(252d) on doji bars at 252d high."""
    rng = (high - low).replace(0, np.nan)
    body = (close - close.shift(1)).abs() / rng
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    cond = (body < 0.1) & (high >= rmax)
    z = _rolling_zscore(_obv(close, volume).diff(), YDAYS)
    return z.where(cond, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_302_obv_diff_on_engulfing_bars_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean OBV-diff z(252d) on bearish-engulfing bars."""
    engulf = (high > high.shift(1)) & (low < low.shift(1)) & (close < close.shift(1))
    z = _rolling_zscore(_obv(close, volume).diff(), YDAYS)
    return z.where(engulf, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_303_obv_diff_on_hammer_bars_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean OBV-diff z(252d) on hammer bars (small body at top, long lower wick)."""
    pos = _safe_div(close - low, high - low)
    body = (close - close.shift(1)).abs()
    lower_wick = pd.concat([close, close.shift(1)], axis=1).min(axis=1) - low
    hammer = (pos >= 0.67) & (lower_wick > 2.0 * body)
    z = _rolling_zscore(_obv(close, volume).diff(), YDAYS)
    return z.where(hammer, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_304_obv_diff_on_shooting_star_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean OBV-diff z(252d) on shooting-star bars (close in bottom third, long upper wick)."""
    pos = _safe_div(close - low, high - low)
    body = (close - close.shift(1)).abs()
    upper_wick = high - pd.concat([close, close.shift(1)], axis=1).max(axis=1)
    star = (pos <= 0.33) & (upper_wick > 2.0 * body)
    z = _rolling_zscore(_obv(close, volume).diff(), YDAYS)
    return z.where(star, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_305_obv_diff_on_3_consec_up_days_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean OBV-diff z(252d) on bars completing a 3-up sequence."""
    up = close > close.shift(1)
    three_up = up & up.shift(1) & up.shift(2)
    z = _rolling_zscore(_obv(close, volume).diff(), YDAYS)
    return z.where(three_up, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_306_obv_diff_on_3_consec_down_days_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean OBV-diff z(252d) on bars completing a 3-down sequence."""
    dn = close < close.shift(1)
    three_dn = dn & dn.shift(1) & dn.shift(2)
    z = _rolling_zscore(_obv(close, volume).diff(), YDAYS)
    return z.where(three_dn, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_307_obv_diff_on_gap_up_bars_252d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean OBV-diff z(252d) on gap-up bars."""
    gap_up = open > 1.005 * close.shift(1)
    z = _rolling_zscore(_obv(close, volume).diff(), YDAYS)
    return z.where(gap_up, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_308_obv_diff_on_gap_down_bars_252d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean OBV-diff z(252d) on gap-down bars."""
    gap_dn = open < 0.995 * close.shift(1)
    z = _rolling_zscore(_obv(close, volume).diff(), YDAYS)
    return z.where(gap_dn, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_309_obv_diff_on_inside_days_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean OBV-diff z(252d) on inside-day bars."""
    inside = (high < high.shift(1)) & (low > low.shift(1))
    z = _rolling_zscore(_obv(close, volume).diff(), YDAYS)
    return z.where(inside, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_310_obv_diff_on_outside_days_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean OBV-diff z(252d) on outside-day bars."""
    outside = (high > high.shift(1)) & (low < low.shift(1))
    z = _rolling_zscore(_obv(close, volume).diff(), YDAYS)
    return z.where(outside, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_311_obv_diff_on_nr7_bars_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean OBV-diff z(252d) on NR7 bars (narrowest range of last 7 bars)."""
    rng = high - low
    is_nr7 = rng == rng.rolling(7, min_periods=3).min()
    z = _rolling_zscore(_obv(close, volume).diff(), YDAYS)
    return z.where(is_nr7, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_312_obv_diff_on_wide_range_bars_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean OBV-diff z(252d) on wide-range bars (TR > 2× ATR21)."""
    pc = close.shift(1)
    tr = pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.rolling(MDAYS, min_periods=WDAYS).mean()
    wide = tr > 2.0 * atr
    z = _rolling_zscore(_obv(close, volume).diff(), YDAYS)
    return z.where(wide, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_313_obv_diff_on_at_252d_high_bars_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean OBV-diff z(252d) on bars where high at 252d max."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    z = _rolling_zscore(_obv(close, volume).diff(), YDAYS)
    return z.where(high >= rmax, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_314_obv_diff_on_at_252d_low_bars_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean OBV-diff z(252d) on bars where low at 252d min."""
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    z = _rolling_zscore(_obv(close, volume).diff(), YDAYS)
    return z.where(low <= rmin, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_315_obv_diff_on_at_alltime_high_bars(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean OBV-diff z(252d) on bars where close at expanding 5y max."""
    rmax = close.expanding(min_periods=YDAYS).max()
    z = _rolling_zscore(_obv(close, volume).diff(), YDAYS)
    return z.where(close >= rmax, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


# Bucket BB — OBV calendar effects (316-325)

def f22_obvd_316_obv_diff_avg_monday_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean OBV-diff on Mondays over trailing 252d."""
    is_d = _safe_dow(close.index, 0)
    return _obv(close, volume).diff().where(is_d == 1.0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_317_obv_diff_avg_tuesday_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean OBV-diff on Tuesdays over trailing 252d."""
    is_d = _safe_dow(close.index, 1)
    return _obv(close, volume).diff().where(is_d == 1.0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_318_obv_diff_avg_wednesday_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean OBV-diff on Wednesdays over trailing 252d."""
    is_d = _safe_dow(close.index, 2)
    return _obv(close, volume).diff().where(is_d == 1.0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_319_obv_diff_avg_thursday_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean OBV-diff on Thursdays over trailing 252d."""
    is_d = _safe_dow(close.index, 3)
    return _obv(close, volume).diff().where(is_d == 1.0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_320_obv_diff_avg_friday_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean OBV-diff on Fridays over trailing 252d."""
    is_d = _safe_dow(close.index, 4)
    return _obv(close, volume).diff().where(is_d == 1.0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_321_obv_diff_first_5_days_of_month_avg(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean OBV-diff on first 5 trading days of month over 252d."""
    if isinstance(close.index, pd.DatetimeIndex):
        is_first = pd.Series(close.index.day <= 5, index=close.index).astype(float)
    else:
        is_first = pd.Series(np.nan, index=close.index)
    return _obv(close, volume).diff().where(is_first == 1.0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_322_obv_diff_last_5_days_of_month_avg(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean OBV-diff on last 5 trading days of month over 252d."""
    if isinstance(close.index, pd.DatetimeIndex):
        is_last = pd.Series(close.index.day >= 25, index=close.index).astype(float)
    else:
        is_last = pd.Series(np.nan, index=close.index)
    return _obv(close, volume).diff().where(is_last == 1.0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_323_obv_diff_quarter_end_avg(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean OBV-diff on quarter-end days over 252d."""
    if isinstance(close.index, pd.DatetimeIndex):
        is_qe = pd.Series((close.index.month.isin([3, 6, 9, 12])) & (close.index.day >= 25), index=close.index).astype(float)
    else:
        is_qe = pd.Series(np.nan, index=close.index)
    return _obv(close, volume).diff().where(is_qe == 1.0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_324_obv_diff_year_end_avg(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean OBV-diff on year-end days over 252d."""
    if isinstance(close.index, pd.DatetimeIndex):
        is_ye = pd.Series((close.index.month == 12) & (close.index.day >= 24), index=close.index).astype(float)
    else:
        is_ye = pd.Series(np.nan, index=close.index)
    return _obv(close, volume).diff().where(is_ye == 1.0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_325_obv_diff_first_day_of_month_avg(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean OBV-diff on the first trading day of each month over 252d."""
    if isinstance(close.index, pd.DatetimeIndex):
        is_fd = pd.Series(close.index.day == 1, index=close.index).astype(float)
    else:
        is_fd = pd.Series(np.nan, index=close.index)
    return _obv(close, volume).diff().where(is_fd == 1.0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


# Bucket BC — Specific OBV trend events (326-340)

def f22_obvd_326_obv_slope_flipped_negative_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when 63d OBV slope is negative now AND was positive 5 bars ago."""
    obv = _obv(close, volume)
    slope = (obv - obv.shift(QDAYS)) / float(QDAYS)
    return ((slope < 0) & (slope.shift(WDAYS) > 0)).astype(float)


def f22_obvd_327_obv_slope_flipped_negative_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of OBV-slope-flipped-negative events."""
    obv = _obv(close, volume)
    slope = (obv - obv.shift(QDAYS)) / float(QDAYS)
    return ((slope < 0) & (slope.shift(WDAYS) > 0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_328_obv_slope_flipped_positive_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when 63d OBV slope is positive now AND was negative 5 bars ago."""
    obv = _obv(close, volume)
    slope = (obv - obv.shift(QDAYS)) / float(QDAYS)
    return ((slope > 0) & (slope.shift(WDAYS) < 0)).astype(float)


def f22_obvd_329_obv_long_term_neg_short_pos_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when 252d slope < 0 AND 63d slope > 0 — dead-cat-bounce signature."""
    obv = _obv(close, volume)
    s252 = (obv - obv.shift(YDAYS)) / float(YDAYS)
    s63 = (obv - obv.shift(QDAYS)) / float(QDAYS)
    return ((s252 < 0) & (s63 > 0)).astype(float)


def f22_obvd_330_obv_long_term_pos_short_neg_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when 252d slope > 0 AND 63d slope < 0 — distribution within an uptrend."""
    obv = _obv(close, volume)
    s252 = (obv - obv.shift(YDAYS)) / float(YDAYS)
    s63 = (obv - obv.shift(QDAYS)) / float(QDAYS)
    return ((s252 > 0) & (s63 < 0)).astype(float)


def f22_obvd_331_obv_slope_max_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max 63d-OBV-slope observed in trailing 252d."""
    obv = _obv(close, volume)
    slope = (obv - obv.shift(QDAYS)) / float(QDAYS)
    return slope.rolling(YDAYS, min_periods=QDAYS).max()


def f22_obvd_332_obv_slope_min_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Min 63d-OBV-slope observed in trailing 252d."""
    obv = _obv(close, volume)
    slope = (obv - obv.shift(QDAYS)) / float(QDAYS)
    return slope.rolling(YDAYS, min_periods=QDAYS).min()


def f22_obvd_333_obv_slope_range_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(Max - min) 63d-OBV-slope in trailing 252d."""
    obv = _obv(close, volume)
    slope = (obv - obv.shift(QDAYS)) / float(QDAYS)
    return slope.rolling(YDAYS, min_periods=QDAYS).max() - slope.rolling(YDAYS, min_periods=QDAYS).min()


def f22_obvd_334_obv_acceleration_recent_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when 21d slope today > 21d slope 21 bars ago (OBV trend accelerating)."""
    obv = _obv(close, volume)
    s21 = (obv - obv.shift(MDAYS)) / float(MDAYS)
    return (s21 > s21.shift(MDAYS)).astype(float)


def f22_obvd_335_obv_deceleration_recent_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when 21d slope today < 21d slope 21 bars ago (OBV trend decelerating)."""
    obv = _obv(close, volume)
    s21 = (obv - obv.shift(MDAYS)) / float(MDAYS)
    return (s21 < s21.shift(MDAYS)).astype(float)


def f22_obvd_336_obv_v_pattern_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when today's OBV is the local minimum of a 21d window centered approximation (PIT-safe via lagged check)."""
    obv = _obv(close, volume)
    # check that 10 bars ago, OBV was the trailing 21d min (using PIT-safe data)
    rmin21 = obv.rolling(MDAYS, min_periods=WDAYS).min().shift(11)  # min over the prior 21d ending 11 days ago
    return (obv.shift(11) <= rmin21).astype(float)


def f22_obvd_337_obv_inverted_v_pattern_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when 11 bars ago, OBV was the trailing 21d max (peak in trailing data)."""
    obv = _obv(close, volume)
    rmax21 = obv.rolling(MDAYS, min_periods=WDAYS).max().shift(11)
    return (obv.shift(11) >= rmax21).astype(float)


def f22_obvd_338_obv_double_bottom_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when 2 OBV lows within 1% of each other in trailing 63d (lower window)."""
    obv = _obv(close, volume)
    rmin = obv.rolling(QDAYS, min_periods=MDAYS).min()
    near_min = (obv - rmin).abs() / (obv.abs() + 1.0) < 0.01
    return (near_min & near_min.shift(MDAYS)).astype(float)


def f22_obvd_339_obv_double_top_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when 2 OBV highs within 1% of each other in trailing 63d."""
    obv = _obv(close, volume)
    rmax = obv.rolling(QDAYS, min_periods=MDAYS).max()
    near_max = (rmax - obv).abs() / (obv.abs() + 1.0) < 0.01
    return (near_max & near_max.shift(MDAYS)).astype(float)


def f22_obvd_340_obv_trend_line_break_event_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when sign of 63d OBV slope changed today (event marker)."""
    obv = _obv(close, volume)
    slope = (obv - obv.shift(QDAYS)) / float(QDAYS)
    return (np.sign(slope) != np.sign(slope.shift(1))).astype(float)


# Bucket BD — Divergence patterns (341-355)

def f22_obvd_341_bullish_divergence_indicator(low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when price 63d low < prior 63d low BUT OBV 63d low > prior 63d low — bullish divergence."""
    obv = _obv(close, volume)
    p_ll = low.rolling(QDAYS, min_periods=MDAYS).min()
    o_min = obv.rolling(QDAYS, min_periods=MDAYS).min()
    return ((p_ll < p_ll.shift(QDAYS)) & (o_min > o_min.shift(QDAYS))).astype(float)


def f22_obvd_342_bearish_divergence_indicator(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when price 63d high > prior 63d high BUT OBV 63d high < prior 63d high — bearish divergence."""
    obv = _obv(close, volume)
    p_hh = high.rolling(QDAYS, min_periods=MDAYS).max()
    o_max = obv.rolling(QDAYS, min_periods=MDAYS).max()
    return ((p_hh > p_hh.shift(QDAYS)) & (o_max < o_max.shift(QDAYS))).astype(float)


def f22_obvd_343_hidden_bullish_divergence_indicator(low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when price 63d low > prior 63d low AND OBV 63d low < prior 63d low — hidden bullish divergence (uptrend continuation)."""
    obv = _obv(close, volume)
    p_hl = low.rolling(QDAYS, min_periods=MDAYS).min()
    o_ll = obv.rolling(QDAYS, min_periods=MDAYS).min()
    return ((p_hl > p_hl.shift(QDAYS)) & (o_ll < o_ll.shift(QDAYS))).astype(float)


def f22_obvd_344_hidden_bearish_divergence_indicator(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when price 63d high < prior 63d high AND OBV 63d high > prior 63d high — hidden bearish divergence."""
    obv = _obv(close, volume)
    p_lh = high.rolling(QDAYS, min_periods=MDAYS).max()
    o_hh = obv.rolling(QDAYS, min_periods=MDAYS).max()
    return ((p_lh < p_lh.shift(QDAYS)) & (o_hh > o_hh.shift(QDAYS))).astype(float)


def f22_obvd_345_bearish_divergence_count_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bearish divergence events."""
    obv = _obv(close, volume)
    p_hh = high.rolling(QDAYS, min_periods=MDAYS).max()
    o_max = obv.rolling(QDAYS, min_periods=MDAYS).max()
    return ((p_hh > p_hh.shift(QDAYS)) & (o_max < o_max.shift(QDAYS))).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_346_bullish_divergence_count_252d(low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bullish divergence events."""
    obv = _obv(close, volume)
    p_ll = low.rolling(QDAYS, min_periods=MDAYS).min()
    o_min = obv.rolling(QDAYS, min_periods=MDAYS).min()
    return ((p_ll < p_ll.shift(QDAYS)) & (o_min > o_min.shift(QDAYS))).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_347_divergence_persistence_score_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of bullish-div − bearish-div counts over trailing 252d."""
    obv = _obv(close, volume)
    p_hh = high.rolling(QDAYS, min_periods=MDAYS).max()
    o_max = obv.rolling(QDAYS, min_periods=MDAYS).max()
    p_ll = low.rolling(QDAYS, min_periods=MDAYS).min()
    o_min = obv.rolling(QDAYS, min_periods=MDAYS).min()
    bear = ((p_hh > p_hh.shift(QDAYS)) & (o_max < o_max.shift(QDAYS))).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    bull = ((p_ll < p_ll.shift(QDAYS)) & (o_min > o_min.shift(QDAYS))).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return bull - bear


def f22_obvd_348_triple_bearish_divergence_indicator(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when 3+ bearish-divergence events have happened in last 21d."""
    obv = _obv(close, volume)
    p_hh = high.rolling(QDAYS, min_periods=MDAYS).max()
    o_max = obv.rolling(QDAYS, min_periods=MDAYS).max()
    bear = ((p_hh > p_hh.shift(QDAYS)) & (o_max < o_max.shift(QDAYS))).astype(float)
    return (bear.rolling(MDAYS, min_periods=WDAYS).sum() >= 3).astype(float)


def f22_obvd_349_failed_bullish_divergence_count_252d(low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bullish-divergence events where price subsequently made a NEW lower low within 21d."""
    obv = _obv(close, volume)
    p_ll = low.rolling(QDAYS, min_periods=MDAYS).min()
    o_min = obv.rolling(QDAYS, min_periods=MDAYS).min()
    bull = (p_ll < p_ll.shift(QDAYS)) & (o_min > o_min.shift(QDAYS))
    new_ll_after = (low.rolling(MDAYS, min_periods=WDAYS).min() < p_ll)
    return (bull.shift(MDAYS) & new_ll_after).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_350_failed_bearish_divergence_count_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bearish-divergence events where price made a NEW higher high within 21d."""
    obv = _obv(close, volume)
    p_hh = high.rolling(QDAYS, min_periods=MDAYS).max()
    o_max = obv.rolling(QDAYS, min_periods=MDAYS).max()
    bear = (p_hh > p_hh.shift(QDAYS)) & (o_max < o_max.shift(QDAYS))
    new_hh_after = (high.rolling(MDAYS, min_periods=WDAYS).max() > p_hh)
    return (bear.shift(MDAYS) & new_hh_after).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_351_divergence_at_252d_high_indicator(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when bearish-divergence event AND today high at 252d max — distribution-at-peak signature."""
    obv = _obv(close, volume)
    p_hh = high.rolling(QDAYS, min_periods=MDAYS).max()
    o_max = obv.rolling(QDAYS, min_periods=MDAYS).max()
    bear = (p_hh > p_hh.shift(QDAYS)) & (o_max < o_max.shift(QDAYS))
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (bear & (high >= rmax)).astype(float)


def f22_obvd_352_divergence_at_252d_low_indicator(low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when bullish-divergence AND today low at 252d min."""
    obv = _obv(close, volume)
    p_ll = low.rolling(QDAYS, min_periods=MDAYS).min()
    o_min = obv.rolling(QDAYS, min_periods=MDAYS).min()
    bull = (p_ll < p_ll.shift(QDAYS)) & (o_min > o_min.shift(QDAYS))
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    return (bull & (low <= rmin)).astype(float)


def f22_obvd_353_divergence_with_above_med_vol_count_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bearish-divergences where vol z(252d) on that bar > 0."""
    obv = _obv(close, volume)
    p_hh = high.rolling(QDAYS, min_periods=MDAYS).max()
    o_max = obv.rolling(QDAYS, min_periods=MDAYS).max()
    bear = (p_hh > p_hh.shift(QDAYS)) & (o_max < o_max.shift(QDAYS))
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    return (bear & (z > 0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_354_divergence_followed_by_break_within_5d_count(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bearish-divergences followed within 5d by close < 21d-low."""
    obv = _obv(close, volume)
    p_hh = high.rolling(QDAYS, min_periods=MDAYS).max()
    o_max = obv.rolling(QDAYS, min_periods=MDAYS).max()
    bear_5d_ago = ((p_hh > p_hh.shift(QDAYS)) & (o_max < o_max.shift(QDAYS))).shift(5)
    rmin21 = low.rolling(MDAYS, min_periods=WDAYS).min().shift(1)
    return (bear_5d_ago & (close < rmin21)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_355_cumulative_divergence_strength_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d sum of |close pct-rank − OBV pct-rank| where bearish divergence is active."""
    obv = _obv(close, volume)
    p_hh = high.rolling(QDAYS, min_periods=MDAYS).max()
    o_max = obv.rolling(QDAYS, min_periods=MDAYS).max()
    bear = (p_hh > p_hh.shift(QDAYS)) & (o_max < o_max.shift(QDAYS))
    pr_c = close.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    pr_o = obv.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    diff = (pr_c - pr_o).abs()
    return diff.where(bear, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()


# Bucket BE — OBV zone/level signals (356-370)

def f22_obvd_356_obv_at_or_above_21d_high_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV ≥ trailing 21d max."""
    obv = _obv(close, volume)
    return (obv >= obv.rolling(MDAYS, min_periods=WDAYS).max()).astype(float)


def f22_obvd_357_obv_at_or_above_63d_high_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV ≥ trailing 63d max."""
    obv = _obv(close, volume)
    return (obv >= obv.rolling(QDAYS, min_periods=MDAYS).max()).astype(float)


def f22_obvd_358_obv_at_or_above_252d_high_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV ≥ trailing 252d max."""
    obv = _obv(close, volume)
    return (obv >= obv.rolling(YDAYS, min_periods=QDAYS).max()).astype(float)


def f22_obvd_359_obv_at_or_below_21d_low_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV ≤ trailing 21d min."""
    obv = _obv(close, volume)
    return (obv <= obv.rolling(MDAYS, min_periods=WDAYS).min()).astype(float)


def f22_obvd_360_obv_at_or_below_63d_low_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV ≤ trailing 63d min."""
    obv = _obv(close, volume)
    return (obv <= obv.rolling(QDAYS, min_periods=MDAYS).min()).astype(float)


def f22_obvd_361_obv_at_or_below_252d_low_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV ≤ trailing 252d min."""
    obv = _obv(close, volume)
    return (obv <= obv.rolling(YDAYS, min_periods=QDAYS).min()).astype(float)


def f22_obvd_362_obv_breakout_above_21d_high_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV crosses above its 21d trailing max (first day above)."""
    obv = _obv(close, volume)
    rmax21 = obv.rolling(MDAYS, min_periods=WDAYS).max()
    return ((obv >= rmax21) & (obv.shift(1) < rmax21.shift(1))).astype(float)


def f22_obvd_363_obv_breakdown_below_21d_low_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV crosses below its 21d trailing min (first day below)."""
    obv = _obv(close, volume)
    rmin21 = obv.rolling(MDAYS, min_periods=WDAYS).min()
    return ((obv <= rmin21) & (obv.shift(1) > rmin21.shift(1))).astype(float)


def f22_obvd_364_obv_breakdown_below_63d_low_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV crosses below its 63d trailing min."""
    obv = _obv(close, volume)
    rmin63 = obv.rolling(QDAYS, min_periods=MDAYS).min()
    return ((obv <= rmin63) & (obv.shift(1) > rmin63.shift(1))).astype(float)


def f22_obvd_365_obv_at_50pct_of_252d_range_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV within ±2% of 50% of 252d range midpoint."""
    obv = _obv(close, volume)
    rmax = obv.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = obv.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(obv - rmin, rmax - rmin)
    return ((pos >= 0.48) & (pos <= 0.52)).astype(float)


def f22_obvd_366_obv_at_top_third_of_252d_range_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV in top third of 252d range."""
    obv = _obv(close, volume)
    rmax = obv.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = obv.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(obv - rmin, rmax - rmin)
    return (pos >= 0.67).astype(float)


def f22_obvd_367_obv_at_bottom_third_of_252d_range_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV in bottom third of 252d range."""
    obv = _obv(close, volume)
    rmax = obv.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = obv.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(obv - rmin, rmax - rmin)
    return (pos <= 0.33).astype(float)


def f22_obvd_368_obv_failed_breakout_above_21d_high_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of OBV cross-up above 21d max that then re-crossed below within 3 bars."""
    obv = _obv(close, volume)
    rmax21 = obv.rolling(MDAYS, min_periods=WDAYS).max()
    cross_up = (obv >= rmax21) & (obv.shift(1) < rmax21.shift(1))
    cross_back = (obv < rmax21) & (obv.shift(1) >= rmax21.shift(1))
    # bars 1-3 ago had a cross_up AND current bar (or recent) has cross_back
    cup_recent = cross_up.shift(1).rolling(3, min_periods=1).max().fillna(False).astype(bool)
    return (cup_recent & cross_back).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_369_obv_pulled_back_from_high_within_5d_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where 5 bars ago OBV at 252d max but today OBV < that level."""
    obv = _obv(close, volume)
    rmax = obv.rolling(YDAYS, min_periods=QDAYS).max()
    was_at = obv.shift(5) >= rmax.shift(5)
    return (was_at & (obv < rmax)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_370_obv_close_above_all_emas_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV > 21EMA(OBV) > 63EMA(OBV) > 252EMA(OBV) — all stacked positive."""
    obv = _obv(close, volume)
    e21 = obv.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()
    e63 = obv.ewm(span=QDAYS, min_periods=MDAYS, adjust=False).mean()
    e252 = obv.ewm(span=YDAYS, min_periods=QDAYS, adjust=False).mean()
    return ((obv > e21) & (e21 > e63) & (e63 > e252)).astype(float)


# Bucket BF — OBV momentum events (371-375)

def f22_obvd_371_obv_momentum_3d_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV increased for 3 consecutive bars."""
    obv = _obv(close, volume)
    d = obv.diff()
    return ((d > 0) & (d.shift(1) > 0) & (d.shift(2) > 0)).astype(float)


def f22_obvd_372_obv_momentum_5d_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV increased for 5 consecutive bars."""
    obv = _obv(close, volume)
    d = obv.diff()
    return ((d > 0) & (d.shift(1) > 0) & (d.shift(2) > 0) & (d.shift(3) > 0) & (d.shift(4) > 0)).astype(float)


def f22_obvd_373_obv_negative_momentum_3d_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV decreased for 3 consecutive bars."""
    obv = _obv(close, volume)
    d = obv.diff()
    return ((d < 0) & (d.shift(1) < 0) & (d.shift(2) < 0)).astype(float)


def f22_obvd_374_obv_negative_momentum_5d_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV decreased for 5 consecutive bars."""
    obv = _obv(close, volume)
    d = obv.diff()
    return ((d < 0) & (d.shift(1) < 0) & (d.shift(2) < 0) & (d.shift(3) < 0) & (d.shift(4) < 0)).astype(float)


def f22_obvd_375_obv_momentum_streak_max_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max consec-bar positive-OBV-diff streak in trailing 252d."""
    obv = _obv(close, volume)
    pos_streak = _consecutive_true_streak(obv.diff() > 0).astype(float)
    return pos_streak.rolling(YDAYS, min_periods=QDAYS).max()


# ============================================================
#                         REGISTRY 301-375
# ============================================================

ON_BALANCE_VOLUME_DYNAMICS_BASE_REGISTRY_301_375 = {
    "f22_obvd_301_obv_diff_on_doji_at_252d_high_252d": {"inputs": ["high", "low", "close", "volume"], "func": f22_obvd_301_obv_diff_on_doji_at_252d_high_252d},
    "f22_obvd_302_obv_diff_on_engulfing_bars_252d": {"inputs": ["high", "low", "close", "volume"], "func": f22_obvd_302_obv_diff_on_engulfing_bars_252d},
    "f22_obvd_303_obv_diff_on_hammer_bars_252d": {"inputs": ["high", "low", "close", "volume"], "func": f22_obvd_303_obv_diff_on_hammer_bars_252d},
    "f22_obvd_304_obv_diff_on_shooting_star_252d": {"inputs": ["high", "low", "close", "volume"], "func": f22_obvd_304_obv_diff_on_shooting_star_252d},
    "f22_obvd_305_obv_diff_on_3_consec_up_days_252d": {"inputs": ["close", "volume"], "func": f22_obvd_305_obv_diff_on_3_consec_up_days_252d},
    "f22_obvd_306_obv_diff_on_3_consec_down_days_252d": {"inputs": ["close", "volume"], "func": f22_obvd_306_obv_diff_on_3_consec_down_days_252d},
    "f22_obvd_307_obv_diff_on_gap_up_bars_252d": {"inputs": ["open", "close", "volume"], "func": f22_obvd_307_obv_diff_on_gap_up_bars_252d},
    "f22_obvd_308_obv_diff_on_gap_down_bars_252d": {"inputs": ["open", "close", "volume"], "func": f22_obvd_308_obv_diff_on_gap_down_bars_252d},
    "f22_obvd_309_obv_diff_on_inside_days_252d": {"inputs": ["high", "low", "close", "volume"], "func": f22_obvd_309_obv_diff_on_inside_days_252d},
    "f22_obvd_310_obv_diff_on_outside_days_252d": {"inputs": ["high", "low", "close", "volume"], "func": f22_obvd_310_obv_diff_on_outside_days_252d},
    "f22_obvd_311_obv_diff_on_nr7_bars_252d": {"inputs": ["high", "low", "close", "volume"], "func": f22_obvd_311_obv_diff_on_nr7_bars_252d},
    "f22_obvd_312_obv_diff_on_wide_range_bars_252d": {"inputs": ["high", "low", "close", "volume"], "func": f22_obvd_312_obv_diff_on_wide_range_bars_252d},
    "f22_obvd_313_obv_diff_on_at_252d_high_bars_252d": {"inputs": ["high", "close", "volume"], "func": f22_obvd_313_obv_diff_on_at_252d_high_bars_252d},
    "f22_obvd_314_obv_diff_on_at_252d_low_bars_252d": {"inputs": ["high", "low", "close", "volume"], "func": f22_obvd_314_obv_diff_on_at_252d_low_bars_252d},
    "f22_obvd_315_obv_diff_on_at_alltime_high_bars": {"inputs": ["close", "volume"], "func": f22_obvd_315_obv_diff_on_at_alltime_high_bars},
    "f22_obvd_316_obv_diff_avg_monday_252d": {"inputs": ["close", "volume"], "func": f22_obvd_316_obv_diff_avg_monday_252d},
    "f22_obvd_317_obv_diff_avg_tuesday_252d": {"inputs": ["close", "volume"], "func": f22_obvd_317_obv_diff_avg_tuesday_252d},
    "f22_obvd_318_obv_diff_avg_wednesday_252d": {"inputs": ["close", "volume"], "func": f22_obvd_318_obv_diff_avg_wednesday_252d},
    "f22_obvd_319_obv_diff_avg_thursday_252d": {"inputs": ["close", "volume"], "func": f22_obvd_319_obv_diff_avg_thursday_252d},
    "f22_obvd_320_obv_diff_avg_friday_252d": {"inputs": ["close", "volume"], "func": f22_obvd_320_obv_diff_avg_friday_252d},
    "f22_obvd_321_obv_diff_first_5_days_of_month_avg": {"inputs": ["close", "volume"], "func": f22_obvd_321_obv_diff_first_5_days_of_month_avg},
    "f22_obvd_322_obv_diff_last_5_days_of_month_avg": {"inputs": ["close", "volume"], "func": f22_obvd_322_obv_diff_last_5_days_of_month_avg},
    "f22_obvd_323_obv_diff_quarter_end_avg": {"inputs": ["close", "volume"], "func": f22_obvd_323_obv_diff_quarter_end_avg},
    "f22_obvd_324_obv_diff_year_end_avg": {"inputs": ["close", "volume"], "func": f22_obvd_324_obv_diff_year_end_avg},
    "f22_obvd_325_obv_diff_first_day_of_month_avg": {"inputs": ["close", "volume"], "func": f22_obvd_325_obv_diff_first_day_of_month_avg},
    "f22_obvd_326_obv_slope_flipped_negative_indicator": {"inputs": ["close", "volume"], "func": f22_obvd_326_obv_slope_flipped_negative_indicator},
    "f22_obvd_327_obv_slope_flipped_negative_count_252d": {"inputs": ["close", "volume"], "func": f22_obvd_327_obv_slope_flipped_negative_count_252d},
    "f22_obvd_328_obv_slope_flipped_positive_indicator": {"inputs": ["close", "volume"], "func": f22_obvd_328_obv_slope_flipped_positive_indicator},
    "f22_obvd_329_obv_long_term_neg_short_pos_indicator": {"inputs": ["close", "volume"], "func": f22_obvd_329_obv_long_term_neg_short_pos_indicator},
    "f22_obvd_330_obv_long_term_pos_short_neg_indicator": {"inputs": ["close", "volume"], "func": f22_obvd_330_obv_long_term_pos_short_neg_indicator},
    "f22_obvd_331_obv_slope_max_252d": {"inputs": ["close", "volume"], "func": f22_obvd_331_obv_slope_max_252d},
    "f22_obvd_332_obv_slope_min_252d": {"inputs": ["close", "volume"], "func": f22_obvd_332_obv_slope_min_252d},
    "f22_obvd_333_obv_slope_range_252d": {"inputs": ["close", "volume"], "func": f22_obvd_333_obv_slope_range_252d},
    "f22_obvd_334_obv_acceleration_recent_indicator": {"inputs": ["close", "volume"], "func": f22_obvd_334_obv_acceleration_recent_indicator},
    "f22_obvd_335_obv_deceleration_recent_indicator": {"inputs": ["close", "volume"], "func": f22_obvd_335_obv_deceleration_recent_indicator},
    "f22_obvd_336_obv_v_pattern_indicator": {"inputs": ["close", "volume"], "func": f22_obvd_336_obv_v_pattern_indicator},
    "f22_obvd_337_obv_inverted_v_pattern_indicator": {"inputs": ["close", "volume"], "func": f22_obvd_337_obv_inverted_v_pattern_indicator},
    "f22_obvd_338_obv_double_bottom_indicator": {"inputs": ["close", "volume"], "func": f22_obvd_338_obv_double_bottom_indicator},
    "f22_obvd_339_obv_double_top_indicator": {"inputs": ["close", "volume"], "func": f22_obvd_339_obv_double_top_indicator},
    "f22_obvd_340_obv_trend_line_break_event_indicator": {"inputs": ["close", "volume"], "func": f22_obvd_340_obv_trend_line_break_event_indicator},
    "f22_obvd_341_bullish_divergence_indicator": {"inputs": ["low", "close", "volume"], "func": f22_obvd_341_bullish_divergence_indicator},
    "f22_obvd_342_bearish_divergence_indicator": {"inputs": ["high", "close", "volume"], "func": f22_obvd_342_bearish_divergence_indicator},
    "f22_obvd_343_hidden_bullish_divergence_indicator": {"inputs": ["low", "close", "volume"], "func": f22_obvd_343_hidden_bullish_divergence_indicator},
    "f22_obvd_344_hidden_bearish_divergence_indicator": {"inputs": ["high", "close", "volume"], "func": f22_obvd_344_hidden_bearish_divergence_indicator},
    "f22_obvd_345_bearish_divergence_count_252d": {"inputs": ["high", "close", "volume"], "func": f22_obvd_345_bearish_divergence_count_252d},
    "f22_obvd_346_bullish_divergence_count_252d": {"inputs": ["low", "close", "volume"], "func": f22_obvd_346_bullish_divergence_count_252d},
    "f22_obvd_347_divergence_persistence_score_252d": {"inputs": ["high", "low", "close", "volume"], "func": f22_obvd_347_divergence_persistence_score_252d},
    "f22_obvd_348_triple_bearish_divergence_indicator": {"inputs": ["high", "close", "volume"], "func": f22_obvd_348_triple_bearish_divergence_indicator},
    "f22_obvd_349_failed_bullish_divergence_count_252d": {"inputs": ["low", "close", "volume"], "func": f22_obvd_349_failed_bullish_divergence_count_252d},
    "f22_obvd_350_failed_bearish_divergence_count_252d": {"inputs": ["high", "close", "volume"], "func": f22_obvd_350_failed_bearish_divergence_count_252d},
    "f22_obvd_351_divergence_at_252d_high_indicator": {"inputs": ["high", "close", "volume"], "func": f22_obvd_351_divergence_at_252d_high_indicator},
    "f22_obvd_352_divergence_at_252d_low_indicator": {"inputs": ["low", "close", "volume"], "func": f22_obvd_352_divergence_at_252d_low_indicator},
    "f22_obvd_353_divergence_with_above_med_vol_count_252d": {"inputs": ["high", "close", "volume"], "func": f22_obvd_353_divergence_with_above_med_vol_count_252d},
    "f22_obvd_354_divergence_followed_by_break_within_5d_count": {"inputs": ["high", "low", "close", "volume"], "func": f22_obvd_354_divergence_followed_by_break_within_5d_count},
    "f22_obvd_355_cumulative_divergence_strength_252d": {"inputs": ["high", "low", "close", "volume"], "func": f22_obvd_355_cumulative_divergence_strength_252d},
    "f22_obvd_356_obv_at_or_above_21d_high_indicator": {"inputs": ["close", "volume"], "func": f22_obvd_356_obv_at_or_above_21d_high_indicator},
    "f22_obvd_357_obv_at_or_above_63d_high_indicator": {"inputs": ["close", "volume"], "func": f22_obvd_357_obv_at_or_above_63d_high_indicator},
    "f22_obvd_358_obv_at_or_above_252d_high_indicator": {"inputs": ["close", "volume"], "func": f22_obvd_358_obv_at_or_above_252d_high_indicator},
    "f22_obvd_359_obv_at_or_below_21d_low_indicator": {"inputs": ["close", "volume"], "func": f22_obvd_359_obv_at_or_below_21d_low_indicator},
    "f22_obvd_360_obv_at_or_below_63d_low_indicator": {"inputs": ["close", "volume"], "func": f22_obvd_360_obv_at_or_below_63d_low_indicator},
    "f22_obvd_361_obv_at_or_below_252d_low_indicator": {"inputs": ["close", "volume"], "func": f22_obvd_361_obv_at_or_below_252d_low_indicator},
    "f22_obvd_362_obv_breakout_above_21d_high_indicator": {"inputs": ["close", "volume"], "func": f22_obvd_362_obv_breakout_above_21d_high_indicator},
    "f22_obvd_363_obv_breakdown_below_21d_low_indicator": {"inputs": ["close", "volume"], "func": f22_obvd_363_obv_breakdown_below_21d_low_indicator},
    "f22_obvd_364_obv_breakdown_below_63d_low_indicator": {"inputs": ["close", "volume"], "func": f22_obvd_364_obv_breakdown_below_63d_low_indicator},
    "f22_obvd_365_obv_at_50pct_of_252d_range_indicator": {"inputs": ["close", "volume"], "func": f22_obvd_365_obv_at_50pct_of_252d_range_indicator},
    "f22_obvd_366_obv_at_top_third_of_252d_range_indicator": {"inputs": ["close", "volume"], "func": f22_obvd_366_obv_at_top_third_of_252d_range_indicator},
    "f22_obvd_367_obv_at_bottom_third_of_252d_range_indicator": {"inputs": ["close", "volume"], "func": f22_obvd_367_obv_at_bottom_third_of_252d_range_indicator},
    "f22_obvd_368_obv_failed_breakout_above_21d_high_count_252d": {"inputs": ["close", "volume"], "func": f22_obvd_368_obv_failed_breakout_above_21d_high_count_252d},
    "f22_obvd_369_obv_pulled_back_from_high_within_5d_count_252d": {"inputs": ["close", "volume"], "func": f22_obvd_369_obv_pulled_back_from_high_within_5d_count_252d},
    "f22_obvd_370_obv_close_above_all_emas_indicator": {"inputs": ["close", "volume"], "func": f22_obvd_370_obv_close_above_all_emas_indicator},
    "f22_obvd_371_obv_momentum_3d_indicator": {"inputs": ["close", "volume"], "func": f22_obvd_371_obv_momentum_3d_indicator},
    "f22_obvd_372_obv_momentum_5d_indicator": {"inputs": ["close", "volume"], "func": f22_obvd_372_obv_momentum_5d_indicator},
    "f22_obvd_373_obv_negative_momentum_3d_indicator": {"inputs": ["close", "volume"], "func": f22_obvd_373_obv_negative_momentum_3d_indicator},
    "f22_obvd_374_obv_negative_momentum_5d_indicator": {"inputs": ["close", "volume"], "func": f22_obvd_374_obv_negative_momentum_5d_indicator},
    "f22_obvd_375_obv_momentum_streak_max_252d": {"inputs": ["close", "volume"], "func": f22_obvd_375_obv_momentum_streak_max_252d},
}
