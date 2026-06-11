"""candlestick_reversal_catalog d2 features 076-150 — Pipeline 1b-technical.

Bearish candlestick reversal patterns at multi-year highs (continued):
piercing-line failure, body asymmetry & shadow geometry, pattern density,
composite severity indices, gap-based reversal kickers. SEP OHLCV only.
PIT-clean.
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


def _near_252d_high_atr(high, low, close, k=1.0):
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    return (rmax - high) <= (k * atr)


def f06_cscr_076_piercing_line_indicator(open_, close):
    """Piercing line (bullish cue)."""
    prev_o = open_.shift(1); prev_c = close.shift(1)
    prev_red = prev_c < prev_o
    gap_down_open = open_ < prev_c
    prev_mid = (prev_o + prev_c) / 2.0
    cls_above_mid = close > prev_mid
    cls_below_prev_open = close < prev_o
    flag = (prev_red & gap_down_open & cls_above_mid & cls_below_prev_open).astype(float)
    return flag.where(prev_c.notna(), np.nan)


def f06_cscr_077_piercing_line_failure_within_5d(open_, close):
    """Piercing-line failure within 5 bars, count in 63d."""
    prev_o = open_.shift(1); prev_c = close.shift(1)
    prev_red = prev_c < prev_o
    gap_down_open = open_ < prev_c
    prev_mid = (prev_o + prev_c) / 2.0
    cls_above_mid = close > prev_mid
    cls_below_prev_open = close < prev_o
    pl_today = (prev_red & gap_down_open & cls_above_mid & cls_below_prev_open).astype(float)
    fail = pd.Series(0.0, index=close.index)
    for k in range(1, WDAYS + 1):
        pl_k = pl_today.shift(k)
        trig_close = close.shift(k)
        fail = fail + ((pl_k > 0) & (close < trig_close)).astype(float)
    fail = (fail > 0).astype(float)
    return fail.rolling(QDAYS, min_periods=MDAYS).sum()


def f06_cscr_078_morning_star_failure_within_5d(open_, high, low, close):
    """Morning-star (bullish 3-bar reversal) that fails within 5 bars — counted in 63d."""
    o1 = open_.shift(2); c1 = close.shift(2)
    o2 = open_.shift(1); c2 = close.shift(1)
    h2 = high.shift(1); l2 = low.shift(1)
    body1 = (o1 - c1)
    body2 = (c2 - o2).abs()
    rng2 = (h2 - l2).replace(0, np.nan)
    body3 = (close - open_)
    bar1_red = body1 > 0
    bar2_small = (body2 / rng2) <= 0.3
    bar3_green = body3 > 0
    mid1 = (o1 + c1) / 2.0
    bar3_above_mid1 = close > mid1
    ms_today = (bar1_red & bar2_small & bar3_green & bar3_above_mid1).astype(float)
    fail = pd.Series(0.0, index=close.index)
    for k in range(1, WDAYS + 1):
        ms_k = ms_today.shift(k)
        trig_low = low.shift(k)
        fail = fail + ((ms_k > 0) & (close < trig_low)).astype(float)
    fail = (fail > 0).astype(float)
    return fail.rolling(QDAYS, min_periods=MDAYS).sum()


def f06_cscr_079_bullish_engulf_failure_within_5d(open_, close):
    """Bullish-engulf failure within 5 bars."""
    prev_o = open_.shift(1); prev_c = close.shift(1)
    today_green = close > open_
    prev_red = prev_c < prev_o
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    prev_top = pd.concat([prev_o, prev_c], axis=1).max(axis=1)
    prev_bot = pd.concat([prev_o, prev_c], axis=1).min(axis=1)
    engulf = (today_top >= prev_top) & (today_bot <= prev_bot)
    be_today = (today_green & prev_red & engulf).astype(float)
    fail = pd.Series(0.0, index=close.index)
    for k in range(1, WDAYS + 1):
        be_k = be_today.shift(k)
        trig_open = open_.shift(k)
        fail = fail + ((be_k > 0) & (close < trig_open)).astype(float)
    fail = (fail > 0).astype(float)
    return fail.rolling(QDAYS, min_periods=MDAYS).sum()


def f06_cscr_080_failed_bull_signal_density_at_high_63d(open_, high, low, close):
    """Failed-bull-signal density near 252d max, 63d."""
    # Bullish engulf failure
    prev_o = open_.shift(1); prev_c = close.shift(1)
    today_green = close > open_
    prev_red = prev_c < prev_o
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    prev_top = pd.concat([prev_o, prev_c], axis=1).max(axis=1)
    prev_bot = pd.concat([prev_o, prev_c], axis=1).min(axis=1)
    engulf = (today_top >= prev_top) & (today_bot <= prev_bot)
    be = (today_green & prev_red & engulf).astype(float)
    # Hammer
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = high - body_top
    lower = body_bot - low
    hammer = (((body / rng) <= 0.3) & (lower >= 2.0 * body) & ((upper / rng) <= 0.1)).astype(float)
    triggers = ((be + hammer) > 0).astype(float)
    fail = pd.Series(0.0, index=close.index)
    for k in range(1, WDAYS + 1):
        tk = triggers.shift(k)
        tl = low.shift(k)
        fail = fail + ((tk > 0) & (close < tl)).astype(float)
    fail = (fail > 0).astype(float)
    near = _near_252d_high_atr(high, low, close, k=2.0).astype(float)
    return (fail * near).rolling(QDAYS, min_periods=MDAYS).sum()


def f06_cscr_081_piercing_line_count_252d(open_, close):
    """Count of piercing-line patterns in trailing 252d."""
    prev_o = open_.shift(1); prev_c = close.shift(1)
    prev_red = prev_c < prev_o
    gap_down_open = open_ < prev_c
    prev_mid = (prev_o + prev_c) / 2.0
    cls_above_mid = close > prev_mid
    cls_below_prev_open = close < prev_o
    flag = (prev_red & gap_down_open & cls_above_mid & cls_below_prev_open).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f06_cscr_082_morning_star_at_high_then_fail_indicator(open_, high, low, close):
    """Morning-star at high then immediate fail."""
    o1 = open_.shift(2); c1 = close.shift(2)
    o2 = open_.shift(1); c2 = close.shift(1)
    h2 = high.shift(1); l2 = low.shift(1)
    body1 = (o1 - c1)
    body2 = (c2 - o2).abs()
    rng2 = (h2 - l2).replace(0, np.nan)
    body3 = (close - open_)
    bar1_red = body1 > 0
    bar2_small = (body2 / rng2) <= 0.3
    bar3_green = body3 > 0
    mid1 = (o1 + c1) / 2.0
    bar3_above_mid1 = close > mid1
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = high >= rmax
    ms = bar1_red & bar2_small & bar3_green & bar3_above_mid1 & at_peak
    ms_prior = ms.shift(1)
    today_down = close < close.shift(1)
    return (ms_prior & today_down).astype(float).where(rmax.notna(), np.nan)


def f06_cscr_083_upper_shadow_to_range_ratio(open_, high, low, close):
    """Upper shadow / range."""
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    return _safe_div(high - body_top, high - low)


def f06_cscr_084_lower_shadow_to_range_ratio(open_, high, low, close):
    """Lower shadow / range."""
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    return _safe_div(body_bot - low, high - low)


def f06_cscr_085_shadow_asymmetry_upper_minus_lower(open_, high, low, close):
    """Shadow asymmetry."""
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = high - body_top
    lower = body_bot - low
    return _safe_div(upper - lower, high - low)


def f06_cscr_086_body_center_position_in_range(open_, high, low, close):
    """Body center position in range."""
    center = (open_ + close) / 2.0
    return _safe_div(center - low, high - low)


def f06_cscr_087_close_to_high_distance_atr(high, low, close):
    """(high - close) / ATR21."""
    atr = _atr(high, low, close, n=MDAYS)
    return _safe_div(high - close, atr)


def f06_cscr_088_open_to_high_proximity(open_, high, low, close):
    """(high - open) / range."""
    return _safe_div(high - open_, high - low)


def f06_cscr_089_red_body_streak(open_, close):
    """Red-body streak length."""
    red = (close < open_).astype(float).to_numpy(copy=True)
    n = len(red)
    out = np.full(n, np.nan, dtype=float)
    s = 0
    for i in range(n):
        if np.isnan(red[i]):
            s = 0
            out[i] = np.nan
        else:
            s = s + 1 if red[i] > 0 else 0
            out[i] = float(s)
    return pd.Series(out, index=close.index)


def f06_cscr_090_green_body_streak_break_event(open_, close):
    """Green-streak break event."""
    green = (close > open_).astype(float)
    red = (close < open_).astype(float)
    # green streak ending today implies yesterday was end of streak; today is red.
    green_prev = green.shift(1).rolling(3, min_periods=3).sum() == 3
    flag = (green_prev & (red > 0)).astype(float)
    return flag.where(green.notna() & red.notna(), np.nan)


def f06_cscr_091_avg_upper_shadow_ratio_21d_at_high(open_, high, low, close):
    """21d mean upper-shadow ratio at high."""
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    upper = high - body_top
    ratio = _safe_div(upper, high - low)
    near = _near_252d_high_atr(high, low, close, k=2.0).astype(float)
    weighted = ratio * near
    cnt = near.rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(weighted.rolling(MDAYS, min_periods=WDAYS).sum(), cnt)


def f06_cscr_092_avg_body_color_imbalance_21d(open_, close):
    """21d body color imbalance."""
    red = (close < open_).astype(float)
    green = (close > open_).astype(float)
    rsum = red.rolling(MDAYS, min_periods=WDAYS).sum()
    gsum = green.rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(rsum - gsum, rsum + gsum)


def f06_cscr_093_long_upper_shadow_count_21d(open_, high, low, close):
    """Count of bars in trailing 21d with upper-shadow >= 50% of range."""
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    ratio = _safe_div(high - body_top, high - low)
    flag = (ratio >= 0.5).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f06_cscr_094_body_top_at_session_low_indicator(open_, high, low, close):
    """Body top near session low."""
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    return ((_safe_div(body_top - low, high - low) <= 0.1)).astype(float)


def f06_cscr_095_close_in_bottom_quartile_after_high_test(high, low, close):
    """Close in bottom quartile after 21d high test."""
    pos = _safe_div(close - low, high - low)
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    flag = ((pos <= 0.25) & (high >= rmax21)).astype(float)
    return flag.where(pos.notna() & rmax21.notna(), np.nan)


def f06_cscr_096_total_bearish_reversal_count_21d_at_high(open_, high, low, close):
    """Total bearish-reversal pattern count, 21d at high."""
    prev_o = open_.shift(1); prev_c = close.shift(1)
    today_red = close < open_; prev_green = prev_c > prev_o
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    prev_top = pd.concat([prev_o, prev_c], axis=1).max(axis=1)
    prev_bot = pd.concat([prev_o, prev_c], axis=1).min(axis=1)
    engulf = (today_top >= prev_top) & (today_bot <= prev_bot)
    be = (today_red & prev_green & engulf).astype(float)
    # Hanging man
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = high - body_top
    lower = body_bot - low
    hm = (((body / rng) <= 0.3) & (lower >= 2.0 * body) & ((upper / rng) <= 0.1)).astype(float)
    # Shooting star
    ss = (((body / rng) <= 0.3) & (upper >= 2.0 * body) & ((lower / rng) <= 0.1)).astype(float)
    # Dark cloud
    prev_h = high.shift(1)
    prev_mid = (prev_o + prev_c) / 2.0
    dc = (prev_green & (open_ > prev_h) & (close < prev_mid) & (close > prev_o)).astype(float)
    total = be + hm + ss + dc
    near = _near_252d_high_atr(high, low, close, k=2.0).astype(float)
    return (total * near).rolling(MDAYS, min_periods=WDAYS).sum()


def f06_cscr_097_total_bearish_reversal_count_63d_at_high(open_, high, low, close):
    """Total bearish-reversal pattern count, 63d at high."""
    prev_o = open_.shift(1); prev_c = close.shift(1)
    today_red = close < open_; prev_green = prev_c > prev_o
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    prev_top = pd.concat([prev_o, prev_c], axis=1).max(axis=1)
    prev_bot = pd.concat([prev_o, prev_c], axis=1).min(axis=1)
    engulf = (today_top >= prev_top) & (today_bot <= prev_bot)
    be = (today_red & prev_green & engulf).astype(float)
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = high - body_top
    lower = body_bot - low
    hm = (((body / rng) <= 0.3) & (lower >= 2.0 * body) & ((upper / rng) <= 0.1)).astype(float)
    ss = (((body / rng) <= 0.3) & (upper >= 2.0 * body) & ((lower / rng) <= 0.1)).astype(float)
    prev_h = high.shift(1)
    prev_mid = (prev_o + prev_c) / 2.0
    dc = (prev_green & (open_ > prev_h) & (close < prev_mid) & (close > prev_o)).astype(float)
    total = be + hm + ss + dc
    near = _near_252d_high_atr(high, low, close, k=2.0).astype(float)
    return (total * near).rolling(QDAYS, min_periods=MDAYS).sum()


def f06_cscr_098_total_bearish_reversal_count_252d_at_high(open_, high, low, close):
    """Total bearish-reversal pattern count, 252d at high."""
    prev_o = open_.shift(1); prev_c = close.shift(1)
    today_red = close < open_; prev_green = prev_c > prev_o
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    prev_top = pd.concat([prev_o, prev_c], axis=1).max(axis=1)
    prev_bot = pd.concat([prev_o, prev_c], axis=1).min(axis=1)
    engulf = (today_top >= prev_top) & (today_bot <= prev_bot)
    be = (today_red & prev_green & engulf).astype(float)
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = high - body_top
    lower = body_bot - low
    hm = (((body / rng) <= 0.3) & (lower >= 2.0 * body) & ((upper / rng) <= 0.1)).astype(float)
    ss = (((body / rng) <= 0.3) & (upper >= 2.0 * body) & ((lower / rng) <= 0.1)).astype(float)
    prev_h = high.shift(1)
    prev_mid = (prev_o + prev_c) / 2.0
    dc = (prev_green & (open_ > prev_h) & (close < prev_mid) & (close > prev_o)).astype(float)
    total = be + hm + ss + dc
    near = _near_252d_high_atr(high, low, close, k=2.0).astype(float)
    return (total * near).rolling(YDAYS, min_periods=QDAYS).sum()


def f06_cscr_099_bars_since_last_bearish_reversal_at_high(open_, high, low, close):
    """Bars since last bearish reversal candle at high."""
    prev_o = open_.shift(1); prev_c = close.shift(1)
    today_red = close < open_; prev_green = prev_c > prev_o
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    prev_top = pd.concat([prev_o, prev_c], axis=1).max(axis=1)
    prev_bot = pd.concat([prev_o, prev_c], axis=1).min(axis=1)
    engulf = (today_top >= prev_top) & (today_bot <= prev_bot)
    be = (today_red & prev_green & engulf).astype(float)
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = high - body_top
    lower = body_bot - low
    hm = (((body / rng) <= 0.3) & (lower >= 2.0 * body) & ((upper / rng) <= 0.1)).astype(float)
    ss = (((body / rng) <= 0.3) & (upper >= 2.0 * body) & ((lower / rng) <= 0.1)).astype(float)
    prev_h = high.shift(1)
    prev_mid = (prev_o + prev_c) / 2.0
    dc = (prev_green & (open_ > prev_h) & (close < prev_mid) & (close > prev_o)).astype(float)
    near = _near_252d_high_atr(high, low, close, k=2.0).astype(float)
    total = ((be + hm + ss + dc) * near).to_numpy(copy=True)
    n = len(total)
    out = np.full(n, np.nan, dtype=float)
    last = -1
    for i in range(n):
        if not np.isnan(total[i]):
            if total[i] > 0:
                last = i
            if last >= 0:
                out[i] = float(i - last)
    return pd.Series(out, index=close.index)


def f06_cscr_100_cluster_score_within_5d(open_, high, low, close):
    """Bearish-reversal cluster score in last 5d."""
    prev_o = open_.shift(1); prev_c = close.shift(1)
    today_red = close < open_; prev_green = prev_c > prev_o
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    prev_top = pd.concat([prev_o, prev_c], axis=1).max(axis=1)
    prev_bot = pd.concat([prev_o, prev_c], axis=1).min(axis=1)
    engulf = (today_top >= prev_top) & (today_bot <= prev_bot)
    be = (today_red & prev_green & engulf).astype(float)
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = high - body_top
    lower = body_bot - low
    hm = (((body / rng) <= 0.3) & (lower >= 2.0 * body) & ((upper / rng) <= 0.1)).astype(float)
    ss = (((body / rng) <= 0.3) & (upper >= 2.0 * body) & ((lower / rng) <= 0.1)).astype(float)
    total = (be + hm + ss).astype(float)
    return total.rolling(WDAYS, min_periods=2).sum() / float(WDAYS)


def f06_cscr_101_distinct_pattern_types_count_21d(open_, high, low, close):
    """Distinct bearish pattern-type count in 21d."""
    prev_o = open_.shift(1); prev_c = close.shift(1)
    today_red = close < open_; prev_green = prev_c > prev_o
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    prev_top = pd.concat([prev_o, prev_c], axis=1).max(axis=1)
    prev_bot = pd.concat([prev_o, prev_c], axis=1).min(axis=1)
    engulf = (today_top >= prev_top) & (today_bot <= prev_bot)
    be = (today_red & prev_green & engulf).astype(float)
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = high - body_top
    lower = body_bot - low
    hm = (((body / rng) <= 0.3) & (lower >= 2.0 * body) & ((upper / rng) <= 0.1)).astype(float)
    ss = (((body / rng) <= 0.3) & (upper >= 2.0 * body) & ((lower / rng) <= 0.1)).astype(float)
    prev_h = high.shift(1)
    prev_mid = (prev_o + prev_c) / 2.0
    dc = (prev_green & (open_ > prev_h) & (close < prev_mid) & (close > prev_o)).astype(float)
    be_n = (be.rolling(MDAYS, min_periods=WDAYS).sum() > 0).astype(float)
    hm_n = (hm.rolling(MDAYS, min_periods=WDAYS).sum() > 0).astype(float)
    ss_n = (ss.rolling(MDAYS, min_periods=WDAYS).sum() > 0).astype(float)
    dc_n = (dc.rolling(MDAYS, min_periods=WDAYS).sum() > 0).astype(float)
    return be_n + hm_n + ss_n + dc_n


def f06_cscr_102_pattern_density_zscore_252d(open_, high, low, close):
    """Pattern-density z-score (252d)."""
    prev_o = open_.shift(1); prev_c = close.shift(1)
    today_red = close < open_; prev_green = prev_c > prev_o
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    prev_top = pd.concat([prev_o, prev_c], axis=1).max(axis=1)
    prev_bot = pd.concat([prev_o, prev_c], axis=1).min(axis=1)
    engulf = (today_top >= prev_top) & (today_bot <= prev_bot)
    be = (today_red & prev_green & engulf).astype(float)
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = high - body_top
    lower = body_bot - low
    hm = (((body / rng) <= 0.3) & (lower >= 2.0 * body) & ((upper / rng) <= 0.1)).astype(float)
    ss = (((body / rng) <= 0.3) & (upper >= 2.0 * body) & ((lower / rng) <= 0.1)).astype(float)
    total = (be + hm + ss).astype(float)
    dens = total.rolling(MDAYS, min_periods=WDAYS).sum()
    return _rolling_zscore(dens, YDAYS, min_periods=QDAYS)


def f06_cscr_103_max_pattern_run_length_21d(open_, high, low, close):
    """Max consecutive pattern-fire run in 21d."""
    prev_o = open_.shift(1); prev_c = close.shift(1)
    today_red = close < open_; prev_green = prev_c > prev_o
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    prev_top = pd.concat([prev_o, prev_c], axis=1).max(axis=1)
    prev_bot = pd.concat([prev_o, prev_c], axis=1).min(axis=1)
    engulf = (today_top >= prev_top) & (today_bot <= prev_bot)
    be = (today_red & prev_green & engulf).astype(float)
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = high - body_top
    lower = body_bot - low
    hm = (((body / rng) <= 0.3) & (lower >= 2.0 * body) & ((upper / rng) <= 0.1)).astype(float)
    ss = (((body / rng) <= 0.3) & (upper >= 2.0 * body) & ((lower / rng) <= 0.1)).astype(float)
    fire = ((be + hm + ss) > 0).astype(float).to_numpy(copy=True)
    n = len(fire)
    streak = np.zeros(n, dtype=float)
    cur = 0
    for i in range(n):
        if fire[i] > 0:
            cur += 1
        else:
            cur = 0
        streak[i] = cur
    s = pd.Series(streak, index=close.index)
    return s.rolling(MDAYS, min_periods=WDAYS).max()


def f06_cscr_104_gap_between_consecutive_bear_signals_21d(open_, high, low, close):
    """Mean gap between bear signals in 21d."""
    prev_o = open_.shift(1); prev_c = close.shift(1)
    today_red = close < open_; prev_green = prev_c > prev_o
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    prev_top = pd.concat([prev_o, prev_c], axis=1).max(axis=1)
    prev_bot = pd.concat([prev_o, prev_c], axis=1).min(axis=1)
    engulf = (today_top >= prev_top) & (today_bot <= prev_bot)
    be = (today_red & prev_green & engulf).astype(float)
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = high - body_top
    lower = body_bot - low
    hm = (((body / rng) <= 0.3) & (lower >= 2.0 * body) & ((upper / rng) <= 0.1)).astype(float)
    ss = (((body / rng) <= 0.3) & (upper >= 2.0 * body) & ((lower / rng) <= 0.1)).astype(float)
    fire = ((be + hm + ss) > 0).astype(float)
    def _mg(w):
        idx = np.where(w > 0)[0]
        if idx.size < 2:
            return np.nan
        return float(np.diff(idx).mean())
    return fire.rolling(MDAYS, min_periods=WDAYS).apply(_mg, raw=True)


def f06_cscr_105_bear_reversal_to_total_red_ratio_63d(open_, close, high, low):
    """Bear-reversal / red-bar ratio (63d)."""
    prev_o = open_.shift(1); prev_c = close.shift(1)
    today_red = close < open_; prev_green = prev_c > prev_o
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    prev_top = pd.concat([prev_o, prev_c], axis=1).max(axis=1)
    prev_bot = pd.concat([prev_o, prev_c], axis=1).min(axis=1)
    engulf = (today_top >= prev_top) & (today_bot <= prev_bot)
    be = (today_red & prev_green & engulf).astype(float)
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = high - body_top
    lower = body_bot - low
    hm = (((body / rng) <= 0.3) & (lower >= 2.0 * body) & ((upper / rng) <= 0.1)).astype(float)
    ss = (((body / rng) <= 0.3) & (upper >= 2.0 * body) & ((lower / rng) <= 0.1)).astype(float)
    fire = (be + hm + ss).astype(float)
    red = today_red.astype(float)
    return _safe_div(fire.rolling(QDAYS, min_periods=MDAYS).sum(),
                     red.rolling(QDAYS, min_periods=MDAYS).sum())


def f06_cscr_106_doji_density_252d(open_, high, low, close):
    """Doji density (252d)."""
    body = (close - open_).abs()
    rng = (high - low)
    is_doji = (_safe_div(body, rng) <= 0.10).astype(float)
    return is_doji.rolling(YDAYS, min_periods=QDAYS).sum()


def f06_cscr_107_engulf_to_doji_ratio_63d(open_, high, low, close):
    """Engulf / doji count ratio (63d)."""
    prev_o = open_.shift(1); prev_c = close.shift(1)
    today_red = close < open_; prev_green = prev_c > prev_o
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    prev_top = pd.concat([prev_o, prev_c], axis=1).max(axis=1)
    prev_bot = pd.concat([prev_o, prev_c], axis=1).min(axis=1)
    engulf = (today_top >= prev_top) & (today_bot <= prev_bot)
    be = (today_red & prev_green & engulf).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    body = (close - open_).abs()
    rng = (high - low)
    dj = (_safe_div(body, rng) <= 0.10).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(be, dj)


def f06_cscr_108_long_upper_shadow_to_long_lower_shadow_ratio_21d(open_, high, low, close):
    """Long-upper / long-lower shadow ratio (21d)."""
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = _safe_div(high - body_top, high - low)
    lower = _safe_div(body_bot - low, high - low)
    up_cnt = (upper >= 0.5).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    lo_cnt = (lower >= 0.5).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(up_cnt, lo_cnt)


def f06_cscr_109_dwell_above_atr_upper_shadow_threshold_21d(open_, high, low, close):
    """Bars with upper shadow > 1 ATR, 21d."""
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    upper = high - body_top
    atr = _atr(high, low, close, n=MDAYS)
    flag = (upper > atr).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f06_cscr_110_dwell_atr_upper_shadow_at_252d_high_63d(open_, high, low, close):
    """Bars with upper shadow > 0.5 ATR at high, 63d."""
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    upper = high - body_top
    atr = _atr(high, low, close, n=MDAYS)
    near = _near_252d_high_atr(high, low, close, k=2.0)
    flag = ((upper > 0.5 * atr) & near).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f06_cscr_111_composite_severity_index(open_, high, low, close):
    """Composite single-bar bearish severity index."""
    rng = (high - low).replace(0, np.nan)
    body = (close - open_).abs() / rng
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = (high - body_top) / rng
    pos_low = 1.0 - (body_top - low) / rng
    today_red = (close < open_).astype(float)
    return today_red * (body + upper + pos_low) / 3.0


def f06_cscr_112_composite_severity_at_252d_high(open_, high, low, close):
    """Composite severity gated to near 252d max."""
    rng = (high - low).replace(0, np.nan)
    body = (close - open_).abs() / rng
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = (high - body_top) / rng
    pos_low = 1.0 - (body_top - low) / rng
    today_red = (close < open_).astype(float)
    sev = today_red * (body + upper + pos_low) / 3.0
    near = _near_252d_high_atr(high, low, close, k=2.0).astype(float)
    return sev * near


def f06_cscr_113_two_bar_reversal_strength(open_, high, low, close):
    """Two-bar reversal strength in ATR units."""
    prev_o = open_.shift(1); prev_c = close.shift(1)
    prev_green = prev_c > prev_o
    today_red = close < open_
    atr = _atr(high, low, close, n=MDAYS)
    val = _safe_div(prev_c - close, atr)
    return val.where(prev_green & today_red, np.nan)


def f06_cscr_114_three_bar_reversal_strength(open_, high, low, close):
    """Three-bar top-to-current drop in ATR units."""
    h_max3 = high.rolling(3, min_periods=3).max()
    atr = _atr(high, low, close, n=MDAYS)
    today_red = close < open_
    val = _safe_div(h_max3 - close, atr)
    return val.where(today_red, np.nan)


def f06_cscr_115_max_composite_severity_21d(open_, high, low, close):
    """21d max composite severity."""
    rng = (high - low).replace(0, np.nan)
    body = (close - open_).abs() / rng
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    upper = (high - body_top) / rng
    pos_low = 1.0 - (body_top - low) / rng
    today_red = (close < open_).astype(float)
    sev = today_red * (body + upper + pos_low) / 3.0
    return sev.rolling(MDAYS, min_periods=WDAYS).max()


def f06_cscr_116_mean_composite_severity_63d(open_, high, low, close):
    """63d mean composite severity."""
    rng = (high - low).replace(0, np.nan)
    body = (close - open_).abs() / rng
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    upper = (high - body_top) / rng
    pos_low = 1.0 - (body_top - low) / rng
    today_red = (close < open_).astype(float)
    sev = today_red * (body + upper + pos_low) / 3.0
    return sev.rolling(QDAYS, min_periods=MDAYS).mean()


def f06_cscr_117_severity_with_volume_weight(open_, high, low, close, volume):
    """Volume-weighted severity."""
    rng = (high - low).replace(0, np.nan)
    body = (close - open_).abs() / rng
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    upper = (high - body_top) / rng
    pos_low = 1.0 - (body_top - low) / rng
    today_red = (close < open_).astype(float)
    sev = today_red * (body + upper + pos_low) / 3.0
    vavg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    vmul = _safe_div(volume, vavg)
    return sev * vmul


def f06_cscr_118_severity_minus_prior_bull_score(open_, high, low, close):
    """Severity minus prior-day bull score."""
    rng = (high - low).replace(0, np.nan)
    body = (close - open_).abs() / rng
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    upper = (high - body_top) / rng
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    lower = (body_bot - low) / rng
    pos_low = 1.0 - (body_top - low) / rng
    pos_high = (body_bot - low) / rng
    today_red = (close < open_).astype(float)
    today_green = (close > open_).astype(float)
    bear = today_red * (body + upper + pos_low) / 3.0
    bull = today_green * (body + lower + pos_high) / 3.0
    return bear - bull.shift(1)


def f06_cscr_119_atr_normalized_reversal_drop_5d(open_, high, low, close):
    """5d-max-to-close drop in ATR units."""
    rmax = high.rolling(WDAYS, min_periods=2).max()
    atr = _atr(high, low, close, n=MDAYS)
    return _safe_div(rmax - close, atr)


def f06_cscr_120_atr_normalized_reversal_drop_21d(high, low, close):
    """21d-max-to-close drop in ATR units."""
    rmax = high.rolling(MDAYS, min_periods=WDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    return _safe_div(rmax - close, atr)


def f06_cscr_121_severity_breakout_count_252d(open_, high, low, close):
    """Count of extreme-severity bars (252d)."""
    rng = (high - low).replace(0, np.nan)
    body = (close - open_).abs() / rng
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    upper = (high - body_top) / rng
    pos_low = 1.0 - (body_top - low) / rng
    today_red = (close < open_).astype(float)
    sev = today_red * (body + upper + pos_low) / 3.0
    flag = (sev > 0.7).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f06_cscr_122_severity_z_score_252d(open_, high, low, close):
    """Severity z-score (252d)."""
    rng = (high - low).replace(0, np.nan)
    body = (close - open_).abs() / rng
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    upper = (high - body_top) / rng
    pos_low = 1.0 - (body_top - low) / rng
    today_red = (close < open_).astype(float)
    sev = today_red * (body + upper + pos_low) / 3.0
    return _rolling_zscore(sev, YDAYS, min_periods=QDAYS)


def f06_cscr_123_aggregate_bearish_pattern_score(open_, high, low, close):
    """Aggregate bearish pattern score."""
    prev_o = open_.shift(1); prev_c = close.shift(1)
    today_red = close < open_; prev_green = prev_c > prev_o
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    prev_top = pd.concat([prev_o, prev_c], axis=1).max(axis=1)
    prev_bot = pd.concat([prev_o, prev_c], axis=1).min(axis=1)
    engulf = (today_top >= prev_top) & (today_bot <= prev_bot)
    be = (today_red & prev_green & engulf).astype(float)
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = high - body_top
    lower = body_bot - low
    hm = (((body / rng) <= 0.3) & (lower >= 2.0 * body) & ((upper / rng) <= 0.1)).astype(float)
    ss = (((body / rng) <= 0.3) & (upper >= 2.0 * body) & ((lower / rng) <= 0.1)).astype(float)
    prev_h = high.shift(1)
    prev_mid = (prev_o + prev_c) / 2.0
    dc = (prev_green & (open_ > prev_h) & (close < prev_mid) & (close > prev_o)).astype(float)
    total = be + hm + ss + dc
    body_ratio = body / rng
    return total * body_ratio


def f06_cscr_124_aggregate_pattern_score_at_high(open_, high, low, close):
    """Aggregate pattern score at high."""
    prev_o = open_.shift(1); prev_c = close.shift(1)
    today_red = close < open_; prev_green = prev_c > prev_o
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    prev_top = pd.concat([prev_o, prev_c], axis=1).max(axis=1)
    prev_bot = pd.concat([prev_o, prev_c], axis=1).min(axis=1)
    engulf = (today_top >= prev_top) & (today_bot <= prev_bot)
    be = (today_red & prev_green & engulf).astype(float)
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = high - body_top
    lower = body_bot - low
    hm = (((body / rng) <= 0.3) & (lower >= 2.0 * body) & ((upper / rng) <= 0.1)).astype(float)
    ss = (((body / rng) <= 0.3) & (upper >= 2.0 * body) & ((lower / rng) <= 0.1)).astype(float)
    prev_h = high.shift(1)
    prev_mid = (prev_o + prev_c) / 2.0
    dc = (prev_green & (open_ > prev_h) & (close < prev_mid) & (close > prev_o)).astype(float)
    total = be + hm + ss + dc
    near = _near_252d_high_atr(high, low, close, k=2.0).astype(float)
    return total * near


def f06_cscr_125_cumulative_reversal_score_63d(open_, high, low, close):
    """Cumulative reversal score (63d)."""
    rng = (high - low).replace(0, np.nan)
    body = (close - open_).abs() / rng
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    upper = (high - body_top) / rng
    pos_low = 1.0 - (body_top - low) / rng
    today_red = (close < open_).astype(float)
    sev = today_red * (body + upper + pos_low) / 3.0
    return sev.rolling(QDAYS, min_periods=MDAYS).sum()


def f06_cscr_126_gap_up_then_red_bar(open_, close, high, low):
    """Gap-up then red bar."""
    prev_h = high.shift(1)
    gap_up = open_ > prev_h
    today_red = close < open_
    flag = (gap_up & today_red).astype(float)
    return flag.where(prev_h.notna(), np.nan)


def f06_cscr_127_gap_up_then_close_below_open_gap_size_atr(open_, high, low, close):
    """Gap-up-then-red gap size (ATR)."""
    prev_h = high.shift(1)
    gap_up = open_ > prev_h
    today_red = close < open_
    atr = _atr(high, low, close, n=MDAYS)
    val = _safe_div(open_ - prev_h, atr)
    return val.where(gap_up & today_red, np.nan)


def f06_cscr_128_island_top_bearish_bar_indicator(open_, high, low, close):
    """Bearish island-top bar."""
    prev_h = high.shift(1); prev_l = low.shift(1)
    gap_up = low > prev_h
    today_red = close < open_
    cls_below_prev_low = close < prev_l
    flag = (gap_up & today_red & cls_below_prev_low).astype(float)
    return flag.where(prev_l.notna(), np.nan)


def f06_cscr_129_gap_down_after_large_green_bar(open_, high, low, close):
    """Gap-down after large green bar."""
    body_today = (close - open_).abs()
    atr = _atr(high, low, close, n=MDAYS)
    large_green = ((close > open_) & (body_today >= 2.0 * atr)).astype(float)
    prev_large = large_green.shift(1)
    prev_l = low.shift(1)
    gap_down = open_ < prev_l
    flag = (prev_large > 0) & gap_down
    return flag.astype(float).where(prev_large.notna(), np.nan)


def f06_cscr_130_gap_down_atr_severity(open_, high, low, close):
    """Gap-down severity (ATR units)."""
    prev_l = low.shift(1)
    gap_down = open_ < prev_l
    atr = _atr(high, low, close, n=MDAYS)
    val = _safe_div(prev_l - open_, atr)
    return val.where(gap_down, np.nan)


def f06_cscr_131_gap_up_failure_count_63d(open_, high, low, close):
    """Gap-up failure count (63d)."""
    prev_h = high.shift(1)
    gap_up = open_ > prev_h
    today_red = close < open_
    flag = (gap_up & today_red).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f06_cscr_132_gap_up_failure_at_252d_high_count_252d(open_, high, low, close):
    """Gap-up failure at 252d high count (252d)."""
    prev_h = high.shift(1)
    gap_up = open_ > prev_h
    today_red = close < open_
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = high >= rmax
    flag = (gap_up & today_red & at_peak).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f06_cscr_133_exhaustion_gap_score(open_, high, low, close):
    """Exhaustion-gap composite score."""
    ret5 = _safe_log(close.shift(1)) - _safe_log(close.shift(WDAYS + 1))
    advance = ret5 >= 0.10
    prev_h = high.shift(1)
    gap_up = open_ > prev_h
    today_red = close < open_
    flag = (advance & gap_up & today_red).astype(float)
    return flag.where(ret5.notna() & prev_h.notna(), np.nan)


def f06_cscr_134_runaway_gap_up_no_followthrough(open_, high, low, close):
    """Runaway gap up with no follow-through."""
    prev_h = high.shift(1)
    big_gap = open_ >= 1.02 * prev_h
    pos = _safe_div(close - low, high - low)
    weak_close = pos <= 0.5
    flag = (big_gap & weak_close).astype(float)
    return flag.where(prev_h.notna(), np.nan)


def f06_cscr_135_inside_bar_after_gap_up(open_, high, low, close):
    """Inside bar after gap-up."""
    gap_up2 = (open_.shift(2) > high.shift(3))
    h2 = high.shift(2); l2 = low.shift(2)
    inside = (high <= h2) & (low >= l2)
    flag = (gap_up2 & inside).astype(float)
    return flag.where(h2.notna() & high.notna(), np.nan)


def f06_cscr_136_outside_reversal_bar_indicator(open_, high, low, close):
    """Outside reversal bar."""
    prev_h = high.shift(1); prev_l = low.shift(1)
    out_bar = (high > prev_h) & (low < prev_l)
    today_red = close < open_
    flag = (out_bar & today_red).astype(float)
    return flag.where(prev_h.notna(), np.nan)


def f06_cscr_137_outside_reversal_at_252d_high(open_, high, low, close):
    """Outside reversal at 252d high."""
    prev_h = high.shift(1); prev_l = low.shift(1)
    out_bar = (high > prev_h) & (low < prev_l)
    today_red = close < open_
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = high >= rmax
    flag = (out_bar & today_red & at_peak).astype(float)
    return flag.where(rmax.notna(), np.nan)


def f06_cscr_138_outside_reversal_severity_atr(open_, high, low, close):
    """Outside reversal severity (ATR units)."""
    prev_h = high.shift(1); prev_l = low.shift(1)
    out_bar = (high > prev_h) & (low < prev_l)
    today_red = close < open_
    atr = _atr(high, low, close, n=MDAYS)
    val = _safe_div(high - close, atr)
    return val.where(out_bar & today_red, np.nan)


def f06_cscr_139_key_reversal_bar_indicator(open_, high, low, close):
    """Key reversal bar."""
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    new_high = high >= rmax21
    today_red = close < open_
    cls_below_prev = close < close.shift(1)
    flag = (new_high & today_red & cls_below_prev).astype(float)
    return flag.where(rmax21.notna(), np.nan)


def f06_cscr_140_key_reversal_bar_at_252d_high(open_, high, low, close):
    """Key reversal bar at 252d high."""
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    rmax252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    new_high = high >= rmax21
    at_long_peak = high >= rmax252
    today_red = close < open_
    cls_below_prev = close < close.shift(1)
    flag = (new_high & at_long_peak & today_red & cls_below_prev).astype(float)
    return flag.where(rmax252.notna(), np.nan)


def f06_cscr_141_two_consecutive_bear_engulfs_indicator(open_, close):
    """Two consecutive bearish engulfs."""
    prev_o = open_.shift(1); prev_c = close.shift(1)
    today_red = close < open_; prev_green = prev_c > prev_o
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    prev_top = pd.concat([prev_o, prev_c], axis=1).max(axis=1)
    prev_bot = pd.concat([prev_o, prev_c], axis=1).min(axis=1)
    engulf = (today_top >= prev_top) & (today_bot <= prev_bot)
    be_today = (today_red & prev_green & engulf).astype(float)
    be_prev = be_today.shift(1)
    flag = ((be_today > 0) & (be_prev > 0)).astype(float)
    return flag.where(be_prev.notna(), np.nan)


def f06_cscr_142_reversal_then_lower_high_5d(open_, high, low, close):
    """Reversal then 5d of no new high."""
    prev_o = open_.shift(1); prev_c = close.shift(1)
    today_red = close < open_; prev_green = prev_c > prev_o
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    prev_top = pd.concat([prev_o, prev_c], axis=1).max(axis=1)
    prev_bot = pd.concat([prev_o, prev_c], axis=1).min(axis=1)
    engulf = (today_top >= prev_top) & (today_bot <= prev_bot)
    be = (today_red & prev_green & engulf).astype(float)
    # Did pattern fire 6 bars ago, and have last 5 bars all had high <= trigger high?
    trig_high = high.shift(WDAYS + 1)
    fired = be.shift(WDAYS + 1)
    rmax5 = high.rolling(WDAYS, min_periods=2).max()
    no_break = rmax5 <= trig_high
    flag = ((fired > 0) & no_break).astype(float)
    return flag.where(trig_high.notna(), np.nan)


def f06_cscr_143_reversal_followed_by_close_below_low(open_, high, low, close):
    """Reversal followed by close below its low."""
    prev_o = open_.shift(1); prev_c = close.shift(1)
    today_red = close < open_; prev_green = prev_c > prev_o
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    prev_top = pd.concat([prev_o, prev_c], axis=1).max(axis=1)
    prev_bot = pd.concat([prev_o, prev_c], axis=1).min(axis=1)
    engulf = (today_top >= prev_top) & (today_bot <= prev_bot)
    be = (today_red & prev_green & engulf).astype(float)
    fired = pd.Series(0.0, index=close.index)
    for k in range(1, 4):
        bk = be.shift(k)
        lk = low.shift(k)
        fired = fired + ((bk > 0) & (close < lk)).astype(float)
    return (fired > 0).astype(float)


def f06_cscr_144_reversal_strength_normalized_by_prior_range(open_, high, low, close):
    """Range compression on reversal day."""
    rng_today = high - low
    rng_prev = (high.shift(1) - low.shift(1))
    today_red = close < open_
    val = _safe_div(rng_prev - rng_today, rng_prev)
    return val.where(today_red, np.nan)


def f06_cscr_145_close_at_session_low_indicator(open_, high, low, close):
    """Close at session low indicator."""
    pos = _safe_div(close - low, high - low)
    return (pos <= 0.05).astype(float).where(pos.notna(), np.nan)


def f06_cscr_146_close_at_session_low_count_21d_at_high(open_, high, low, close):
    """Weak-close count, 21d at high."""
    pos = _safe_div(close - low, high - low)
    weak = (pos <= 0.10).astype(float)
    near = _near_252d_high_atr(high, low, close, k=2.0).astype(float)
    return (weak * near).rolling(MDAYS, min_periods=WDAYS).sum()


def f06_cscr_147_reversal_severity_x_volume_zscore(open_, high, low, close, volume):
    """Severity x volume z-score."""
    rng = (high - low).replace(0, np.nan)
    body = (close - open_).abs() / rng
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    upper = (high - body_top) / rng
    pos_low = 1.0 - (body_top - low) / rng
    today_red = (close < open_).astype(float)
    sev = today_red * (body + upper + pos_low) / 3.0
    vz = _rolling_zscore(volume, QDAYS, min_periods=MDAYS)
    return sev * vz


def f06_cscr_148_consecutive_bear_severity_streak(open_, high, low, close):
    """Consecutive bear-severity streak."""
    rng = (high - low).replace(0, np.nan)
    body = (close - open_).abs() / rng
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    upper = (high - body_top) / rng
    pos_low = 1.0 - (body_top - low) / rng
    today_red = (close < open_).astype(float)
    sev = today_red * (body + upper + pos_low) / 3.0
    fire = (sev > 0.4).astype(float).to_numpy(copy=True)
    n = len(fire)
    out = np.full(n, np.nan, dtype=float)
    s = 0
    for i in range(n):
        if np.isnan(fire[i]):
            s = 0
            out[i] = np.nan
        else:
            s = s + 1 if fire[i] > 0 else 0
            out[i] = float(s)
    return pd.Series(out, index=close.index)


def f06_cscr_149_severity_imbalance_21d_minus_63d_mean(open_, high, low, close):
    """21d minus 63d mean severity."""
    rng = (high - low).replace(0, np.nan)
    body = (close - open_).abs() / rng
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    upper = (high - body_top) / rng
    pos_low = 1.0 - (body_top - low) / rng
    today_red = (close < open_).astype(float)
    sev = today_red * (body + upper + pos_low) / 3.0
    m21 = sev.rolling(MDAYS, min_periods=WDAYS).mean()
    m63 = sev.rolling(QDAYS, min_periods=MDAYS).mean()
    return m21 - m63


def f06_cscr_150_terminal_reversal_score(open_, high, low, close, volume):
    """Terminal reversal indicator."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = high >= rmax
    rng = (high - low).replace(0, np.nan)
    body = (close - open_).abs() / rng
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    upper = (high - body_top) / rng
    pos_low = 1.0 - (body_top - low) / rng
    today_red = (close < open_).astype(float)
    sev = today_red * (body + upper + pos_low) / 3.0
    vavg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    vol_ok = volume > 1.5 * vavg
    flag = (at_peak & (sev > 0.5) & vol_ok).astype(float)
    return flag.where(rmax.notna() & vavg.notna(), np.nan)




def f06_cscr_076_piercing_line_indicator_d2(open_, close):
    return f06_cscr_076_piercing_line_indicator(open_, close).diff().diff()


def f06_cscr_077_piercing_line_failure_within_5d_d2(open_, close):
    return f06_cscr_077_piercing_line_failure_within_5d(open_, close).diff().diff()


def f06_cscr_078_morning_star_failure_within_5d_d2(open_, high, low, close):
    return f06_cscr_078_morning_star_failure_within_5d(open_, high, low, close).diff().diff()


def f06_cscr_079_bullish_engulf_failure_within_5d_d2(open_, close):
    return f06_cscr_079_bullish_engulf_failure_within_5d(open_, close).diff().diff()


def f06_cscr_080_failed_bull_signal_density_at_high_63d_d2(open_, high, low, close):
    return f06_cscr_080_failed_bull_signal_density_at_high_63d(open_, high, low, close).diff().diff()


def f06_cscr_081_piercing_line_count_252d_d2(open_, close):
    return f06_cscr_081_piercing_line_count_252d(open_, close).diff().diff()


def f06_cscr_082_morning_star_at_high_then_fail_indicator_d2(open_, high, low, close):
    return f06_cscr_082_morning_star_at_high_then_fail_indicator(open_, high, low, close).diff().diff()


def f06_cscr_083_upper_shadow_to_range_ratio_d2(open_, high, low, close):
    return f06_cscr_083_upper_shadow_to_range_ratio(open_, high, low, close).diff().diff()


def f06_cscr_084_lower_shadow_to_range_ratio_d2(open_, high, low, close):
    return f06_cscr_084_lower_shadow_to_range_ratio(open_, high, low, close).diff().diff()


def f06_cscr_085_shadow_asymmetry_upper_minus_lower_d2(open_, high, low, close):
    return f06_cscr_085_shadow_asymmetry_upper_minus_lower(open_, high, low, close).diff().diff()


def f06_cscr_086_body_center_position_in_range_d2(open_, high, low, close):
    return f06_cscr_086_body_center_position_in_range(open_, high, low, close).diff().diff()


def f06_cscr_087_close_to_high_distance_atr_d2(high, low, close):
    return f06_cscr_087_close_to_high_distance_atr(high, low, close).diff().diff()


def f06_cscr_088_open_to_high_proximity_d2(open_, high, low, close):
    return f06_cscr_088_open_to_high_proximity(open_, high, low, close).diff().diff()


def f06_cscr_089_red_body_streak_d2(open_, close):
    return f06_cscr_089_red_body_streak(open_, close).diff().diff()


def f06_cscr_090_green_body_streak_break_event_d2(open_, close):
    return f06_cscr_090_green_body_streak_break_event(open_, close).diff().diff()


def f06_cscr_091_avg_upper_shadow_ratio_21d_at_high_d2(open_, high, low, close):
    return f06_cscr_091_avg_upper_shadow_ratio_21d_at_high(open_, high, low, close).diff().diff()


def f06_cscr_092_avg_body_color_imbalance_21d_d2(open_, close):
    return f06_cscr_092_avg_body_color_imbalance_21d(open_, close).diff().diff()


def f06_cscr_093_long_upper_shadow_count_21d_d2(open_, high, low, close):
    return f06_cscr_093_long_upper_shadow_count_21d(open_, high, low, close).diff().diff()


def f06_cscr_094_body_top_at_session_low_indicator_d2(open_, high, low, close):
    return f06_cscr_094_body_top_at_session_low_indicator(open_, high, low, close).diff().diff()


def f06_cscr_095_close_in_bottom_quartile_after_high_test_d2(high, low, close):
    return f06_cscr_095_close_in_bottom_quartile_after_high_test(high, low, close).diff().diff()


def f06_cscr_096_total_bearish_reversal_count_21d_at_high_d2(open_, high, low, close):
    return f06_cscr_096_total_bearish_reversal_count_21d_at_high(open_, high, low, close).diff().diff()


def f06_cscr_097_total_bearish_reversal_count_63d_at_high_d2(open_, high, low, close):
    return f06_cscr_097_total_bearish_reversal_count_63d_at_high(open_, high, low, close).diff().diff()


def f06_cscr_098_total_bearish_reversal_count_252d_at_high_d2(open_, high, low, close):
    return f06_cscr_098_total_bearish_reversal_count_252d_at_high(open_, high, low, close).diff().diff()


def f06_cscr_099_bars_since_last_bearish_reversal_at_high_d2(open_, high, low, close):
    return f06_cscr_099_bars_since_last_bearish_reversal_at_high(open_, high, low, close).diff().diff()


def f06_cscr_100_cluster_score_within_5d_d2(open_, high, low, close):
    return f06_cscr_100_cluster_score_within_5d(open_, high, low, close).diff().diff()


def f06_cscr_101_distinct_pattern_types_count_21d_d2(open_, high, low, close):
    return f06_cscr_101_distinct_pattern_types_count_21d(open_, high, low, close).diff().diff()


def f06_cscr_102_pattern_density_zscore_252d_d2(open_, high, low, close):
    return f06_cscr_102_pattern_density_zscore_252d(open_, high, low, close).diff().diff()


def f06_cscr_103_max_pattern_run_length_21d_d2(open_, high, low, close):
    return f06_cscr_103_max_pattern_run_length_21d(open_, high, low, close).diff().diff()


def f06_cscr_104_gap_between_consecutive_bear_signals_21d_d2(open_, high, low, close):
    return f06_cscr_104_gap_between_consecutive_bear_signals_21d(open_, high, low, close).diff().diff()


def f06_cscr_105_bear_reversal_to_total_red_ratio_63d_d2(open_, close, high, low):
    return f06_cscr_105_bear_reversal_to_total_red_ratio_63d(open_, close, high, low).diff().diff()


def f06_cscr_106_doji_density_252d_d2(open_, high, low, close):
    return f06_cscr_106_doji_density_252d(open_, high, low, close).diff().diff()


def f06_cscr_107_engulf_to_doji_ratio_63d_d2(open_, high, low, close):
    return f06_cscr_107_engulf_to_doji_ratio_63d(open_, high, low, close).diff().diff()


def f06_cscr_108_long_upper_shadow_to_long_lower_shadow_ratio_21d_d2(open_, high, low, close):
    return f06_cscr_108_long_upper_shadow_to_long_lower_shadow_ratio_21d(open_, high, low, close).diff().diff()


def f06_cscr_109_dwell_above_atr_upper_shadow_threshold_21d_d2(open_, high, low, close):
    return f06_cscr_109_dwell_above_atr_upper_shadow_threshold_21d(open_, high, low, close).diff().diff()


def f06_cscr_110_dwell_atr_upper_shadow_at_252d_high_63d_d2(open_, high, low, close):
    return f06_cscr_110_dwell_atr_upper_shadow_at_252d_high_63d(open_, high, low, close).diff().diff()


def f06_cscr_111_composite_severity_index_d2(open_, high, low, close):
    return f06_cscr_111_composite_severity_index(open_, high, low, close).diff().diff()


def f06_cscr_112_composite_severity_at_252d_high_d2(open_, high, low, close):
    return f06_cscr_112_composite_severity_at_252d_high(open_, high, low, close).diff().diff()


def f06_cscr_113_two_bar_reversal_strength_d2(open_, high, low, close):
    return f06_cscr_113_two_bar_reversal_strength(open_, high, low, close).diff().diff()


def f06_cscr_114_three_bar_reversal_strength_d2(open_, high, low, close):
    return f06_cscr_114_three_bar_reversal_strength(open_, high, low, close).diff().diff()


def f06_cscr_115_max_composite_severity_21d_d2(open_, high, low, close):
    return f06_cscr_115_max_composite_severity_21d(open_, high, low, close).diff().diff()


def f06_cscr_116_mean_composite_severity_63d_d2(open_, high, low, close):
    return f06_cscr_116_mean_composite_severity_63d(open_, high, low, close).diff().diff()


def f06_cscr_117_severity_with_volume_weight_d2(open_, high, low, close, volume):
    return f06_cscr_117_severity_with_volume_weight(open_, high, low, close, volume).diff().diff()


def f06_cscr_118_severity_minus_prior_bull_score_d2(open_, high, low, close):
    return f06_cscr_118_severity_minus_prior_bull_score(open_, high, low, close).diff().diff()


def f06_cscr_119_atr_normalized_reversal_drop_5d_d2(open_, high, low, close):
    return f06_cscr_119_atr_normalized_reversal_drop_5d(open_, high, low, close).diff().diff()


def f06_cscr_120_atr_normalized_reversal_drop_21d_d2(high, low, close):
    return f06_cscr_120_atr_normalized_reversal_drop_21d(high, low, close).diff().diff()


def f06_cscr_121_severity_breakout_count_252d_d2(open_, high, low, close):
    return f06_cscr_121_severity_breakout_count_252d(open_, high, low, close).diff().diff()


def f06_cscr_122_severity_z_score_252d_d2(open_, high, low, close):
    return f06_cscr_122_severity_z_score_252d(open_, high, low, close).diff().diff()


def f06_cscr_123_aggregate_bearish_pattern_score_d2(open_, high, low, close):
    return f06_cscr_123_aggregate_bearish_pattern_score(open_, high, low, close).diff().diff()


def f06_cscr_124_aggregate_pattern_score_at_high_d2(open_, high, low, close):
    return f06_cscr_124_aggregate_pattern_score_at_high(open_, high, low, close).diff().diff()


def f06_cscr_125_cumulative_reversal_score_63d_d2(open_, high, low, close):
    return f06_cscr_125_cumulative_reversal_score_63d(open_, high, low, close).diff().diff()


def f06_cscr_126_gap_up_then_red_bar_d2(open_, close, high, low):
    return f06_cscr_126_gap_up_then_red_bar(open_, close, high, low).diff().diff()


def f06_cscr_127_gap_up_then_close_below_open_gap_size_atr_d2(open_, high, low, close):
    return f06_cscr_127_gap_up_then_close_below_open_gap_size_atr(open_, high, low, close).diff().diff()


def f06_cscr_128_island_top_bearish_bar_indicator_d2(open_, high, low, close):
    return f06_cscr_128_island_top_bearish_bar_indicator(open_, high, low, close).diff().diff()


def f06_cscr_129_gap_down_after_large_green_bar_d2(open_, high, low, close):
    return f06_cscr_129_gap_down_after_large_green_bar(open_, high, low, close).diff().diff()


def f06_cscr_130_gap_down_atr_severity_d2(open_, high, low, close):
    return f06_cscr_130_gap_down_atr_severity(open_, high, low, close).diff().diff()


def f06_cscr_131_gap_up_failure_count_63d_d2(open_, high, low, close):
    return f06_cscr_131_gap_up_failure_count_63d(open_, high, low, close).diff().diff()


def f06_cscr_132_gap_up_failure_at_252d_high_count_252d_d2(open_, high, low, close):
    return f06_cscr_132_gap_up_failure_at_252d_high_count_252d(open_, high, low, close).diff().diff()


def f06_cscr_133_exhaustion_gap_score_d2(open_, high, low, close):
    return f06_cscr_133_exhaustion_gap_score(open_, high, low, close).diff().diff()


def f06_cscr_134_runaway_gap_up_no_followthrough_d2(open_, high, low, close):
    return f06_cscr_134_runaway_gap_up_no_followthrough(open_, high, low, close).diff().diff()


def f06_cscr_135_inside_bar_after_gap_up_d2(open_, high, low, close):
    return f06_cscr_135_inside_bar_after_gap_up(open_, high, low, close).diff().diff()


def f06_cscr_136_outside_reversal_bar_indicator_d2(open_, high, low, close):
    return f06_cscr_136_outside_reversal_bar_indicator(open_, high, low, close).diff().diff()


def f06_cscr_137_outside_reversal_at_252d_high_d2(open_, high, low, close):
    return f06_cscr_137_outside_reversal_at_252d_high(open_, high, low, close).diff().diff()


def f06_cscr_138_outside_reversal_severity_atr_d2(open_, high, low, close):
    return f06_cscr_138_outside_reversal_severity_atr(open_, high, low, close).diff().diff()


def f06_cscr_139_key_reversal_bar_indicator_d2(open_, high, low, close):
    return f06_cscr_139_key_reversal_bar_indicator(open_, high, low, close).diff().diff()


def f06_cscr_140_key_reversal_bar_at_252d_high_d2(open_, high, low, close):
    return f06_cscr_140_key_reversal_bar_at_252d_high(open_, high, low, close).diff().diff()


def f06_cscr_141_two_consecutive_bear_engulfs_indicator_d2(open_, close):
    return f06_cscr_141_two_consecutive_bear_engulfs_indicator(open_, close).diff().diff()


def f06_cscr_142_reversal_then_lower_high_5d_d2(open_, high, low, close):
    return f06_cscr_142_reversal_then_lower_high_5d(open_, high, low, close).diff().diff()


def f06_cscr_143_reversal_followed_by_close_below_low_d2(open_, high, low, close):
    return f06_cscr_143_reversal_followed_by_close_below_low(open_, high, low, close).diff().diff()


def f06_cscr_144_reversal_strength_normalized_by_prior_range_d2(open_, high, low, close):
    return f06_cscr_144_reversal_strength_normalized_by_prior_range(open_, high, low, close).diff().diff()


def f06_cscr_145_close_at_session_low_indicator_d2(open_, high, low, close):
    return f06_cscr_145_close_at_session_low_indicator(open_, high, low, close).diff().diff()


def f06_cscr_146_close_at_session_low_count_21d_at_high_d2(open_, high, low, close):
    return f06_cscr_146_close_at_session_low_count_21d_at_high(open_, high, low, close).diff().diff()


def f06_cscr_147_reversal_severity_x_volume_zscore_d2(open_, high, low, close, volume):
    return f06_cscr_147_reversal_severity_x_volume_zscore(open_, high, low, close, volume).diff().diff()


def f06_cscr_148_consecutive_bear_severity_streak_d2(open_, high, low, close):
    return f06_cscr_148_consecutive_bear_severity_streak(open_, high, low, close).diff().diff()


def f06_cscr_149_severity_imbalance_21d_minus_63d_mean_d2(open_, high, low, close):
    return f06_cscr_149_severity_imbalance_21d_minus_63d_mean(open_, high, low, close).diff().diff()


def f06_cscr_150_terminal_reversal_score_d2(open_, high, low, close, volume):
    return f06_cscr_150_terminal_reversal_score(open_, high, low, close, volume).diff().diff()


CANDLESTICK_REVERSAL_CATALOG_D2_REGISTRY_076_150 = {
    "f06_cscr_076_piercing_line_indicator_d2": {"inputs": ["open", "close"], "func": f06_cscr_076_piercing_line_indicator_d2},
    "f06_cscr_077_piercing_line_failure_within_5d_d2": {"inputs": ["open", "close"], "func": f06_cscr_077_piercing_line_failure_within_5d_d2},
    "f06_cscr_078_morning_star_failure_within_5d_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_078_morning_star_failure_within_5d_d2},
    "f06_cscr_079_bullish_engulf_failure_within_5d_d2": {"inputs": ["open", "close"], "func": f06_cscr_079_bullish_engulf_failure_within_5d_d2},
    "f06_cscr_080_failed_bull_signal_density_at_high_63d_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_080_failed_bull_signal_density_at_high_63d_d2},
    "f06_cscr_081_piercing_line_count_252d_d2": {"inputs": ["open", "close"], "func": f06_cscr_081_piercing_line_count_252d_d2},
    "f06_cscr_082_morning_star_at_high_then_fail_indicator_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_082_morning_star_at_high_then_fail_indicator_d2},
    "f06_cscr_083_upper_shadow_to_range_ratio_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_083_upper_shadow_to_range_ratio_d2},
    "f06_cscr_084_lower_shadow_to_range_ratio_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_084_lower_shadow_to_range_ratio_d2},
    "f06_cscr_085_shadow_asymmetry_upper_minus_lower_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_085_shadow_asymmetry_upper_minus_lower_d2},
    "f06_cscr_086_body_center_position_in_range_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_086_body_center_position_in_range_d2},
    "f06_cscr_087_close_to_high_distance_atr_d2": {"inputs": ["high", "low", "close"], "func": f06_cscr_087_close_to_high_distance_atr_d2},
    "f06_cscr_088_open_to_high_proximity_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_088_open_to_high_proximity_d2},
    "f06_cscr_089_red_body_streak_d2": {"inputs": ["open", "close"], "func": f06_cscr_089_red_body_streak_d2},
    "f06_cscr_090_green_body_streak_break_event_d2": {"inputs": ["open", "close"], "func": f06_cscr_090_green_body_streak_break_event_d2},
    "f06_cscr_091_avg_upper_shadow_ratio_21d_at_high_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_091_avg_upper_shadow_ratio_21d_at_high_d2},
    "f06_cscr_092_avg_body_color_imbalance_21d_d2": {"inputs": ["open", "close"], "func": f06_cscr_092_avg_body_color_imbalance_21d_d2},
    "f06_cscr_093_long_upper_shadow_count_21d_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_093_long_upper_shadow_count_21d_d2},
    "f06_cscr_094_body_top_at_session_low_indicator_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_094_body_top_at_session_low_indicator_d2},
    "f06_cscr_095_close_in_bottom_quartile_after_high_test_d2": {"inputs": ["high", "low", "close"], "func": f06_cscr_095_close_in_bottom_quartile_after_high_test_d2},
    "f06_cscr_096_total_bearish_reversal_count_21d_at_high_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_096_total_bearish_reversal_count_21d_at_high_d2},
    "f06_cscr_097_total_bearish_reversal_count_63d_at_high_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_097_total_bearish_reversal_count_63d_at_high_d2},
    "f06_cscr_098_total_bearish_reversal_count_252d_at_high_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_098_total_bearish_reversal_count_252d_at_high_d2},
    "f06_cscr_099_bars_since_last_bearish_reversal_at_high_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_099_bars_since_last_bearish_reversal_at_high_d2},
    "f06_cscr_100_cluster_score_within_5d_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_100_cluster_score_within_5d_d2},
    "f06_cscr_101_distinct_pattern_types_count_21d_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_101_distinct_pattern_types_count_21d_d2},
    "f06_cscr_102_pattern_density_zscore_252d_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_102_pattern_density_zscore_252d_d2},
    "f06_cscr_103_max_pattern_run_length_21d_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_103_max_pattern_run_length_21d_d2},
    "f06_cscr_104_gap_between_consecutive_bear_signals_21d_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_104_gap_between_consecutive_bear_signals_21d_d2},
    "f06_cscr_105_bear_reversal_to_total_red_ratio_63d_d2": {"inputs": ["open", "close", "high", "low"], "func": f06_cscr_105_bear_reversal_to_total_red_ratio_63d_d2},
    "f06_cscr_106_doji_density_252d_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_106_doji_density_252d_d2},
    "f06_cscr_107_engulf_to_doji_ratio_63d_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_107_engulf_to_doji_ratio_63d_d2},
    "f06_cscr_108_long_upper_shadow_to_long_lower_shadow_ratio_21d_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_108_long_upper_shadow_to_long_lower_shadow_ratio_21d_d2},
    "f06_cscr_109_dwell_above_atr_upper_shadow_threshold_21d_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_109_dwell_above_atr_upper_shadow_threshold_21d_d2},
    "f06_cscr_110_dwell_atr_upper_shadow_at_252d_high_63d_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_110_dwell_atr_upper_shadow_at_252d_high_63d_d2},
    "f06_cscr_111_composite_severity_index_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_111_composite_severity_index_d2},
    "f06_cscr_112_composite_severity_at_252d_high_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_112_composite_severity_at_252d_high_d2},
    "f06_cscr_113_two_bar_reversal_strength_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_113_two_bar_reversal_strength_d2},
    "f06_cscr_114_three_bar_reversal_strength_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_114_three_bar_reversal_strength_d2},
    "f06_cscr_115_max_composite_severity_21d_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_115_max_composite_severity_21d_d2},
    "f06_cscr_116_mean_composite_severity_63d_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_116_mean_composite_severity_63d_d2},
    "f06_cscr_117_severity_with_volume_weight_d2": {"inputs": ["open", "high", "low", "close", "volume"], "func": f06_cscr_117_severity_with_volume_weight_d2},
    "f06_cscr_118_severity_minus_prior_bull_score_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_118_severity_minus_prior_bull_score_d2},
    "f06_cscr_119_atr_normalized_reversal_drop_5d_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_119_atr_normalized_reversal_drop_5d_d2},
    "f06_cscr_120_atr_normalized_reversal_drop_21d_d2": {"inputs": ["high", "low", "close"], "func": f06_cscr_120_atr_normalized_reversal_drop_21d_d2},
    "f06_cscr_121_severity_breakout_count_252d_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_121_severity_breakout_count_252d_d2},
    "f06_cscr_122_severity_z_score_252d_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_122_severity_z_score_252d_d2},
    "f06_cscr_123_aggregate_bearish_pattern_score_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_123_aggregate_bearish_pattern_score_d2},
    "f06_cscr_124_aggregate_pattern_score_at_high_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_124_aggregate_pattern_score_at_high_d2},
    "f06_cscr_125_cumulative_reversal_score_63d_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_125_cumulative_reversal_score_63d_d2},
    "f06_cscr_126_gap_up_then_red_bar_d2": {"inputs": ["open", "close", "high", "low"], "func": f06_cscr_126_gap_up_then_red_bar_d2},
    "f06_cscr_127_gap_up_then_close_below_open_gap_size_atr_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_127_gap_up_then_close_below_open_gap_size_atr_d2},
    "f06_cscr_128_island_top_bearish_bar_indicator_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_128_island_top_bearish_bar_indicator_d2},
    "f06_cscr_129_gap_down_after_large_green_bar_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_129_gap_down_after_large_green_bar_d2},
    "f06_cscr_130_gap_down_atr_severity_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_130_gap_down_atr_severity_d2},
    "f06_cscr_131_gap_up_failure_count_63d_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_131_gap_up_failure_count_63d_d2},
    "f06_cscr_132_gap_up_failure_at_252d_high_count_252d_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_132_gap_up_failure_at_252d_high_count_252d_d2},
    "f06_cscr_133_exhaustion_gap_score_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_133_exhaustion_gap_score_d2},
    "f06_cscr_134_runaway_gap_up_no_followthrough_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_134_runaway_gap_up_no_followthrough_d2},
    "f06_cscr_135_inside_bar_after_gap_up_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_135_inside_bar_after_gap_up_d2},
    "f06_cscr_136_outside_reversal_bar_indicator_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_136_outside_reversal_bar_indicator_d2},
    "f06_cscr_137_outside_reversal_at_252d_high_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_137_outside_reversal_at_252d_high_d2},
    "f06_cscr_138_outside_reversal_severity_atr_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_138_outside_reversal_severity_atr_d2},
    "f06_cscr_139_key_reversal_bar_indicator_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_139_key_reversal_bar_indicator_d2},
    "f06_cscr_140_key_reversal_bar_at_252d_high_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_140_key_reversal_bar_at_252d_high_d2},
    "f06_cscr_141_two_consecutive_bear_engulfs_indicator_d2": {"inputs": ["open", "close"], "func": f06_cscr_141_two_consecutive_bear_engulfs_indicator_d2},
    "f06_cscr_142_reversal_then_lower_high_5d_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_142_reversal_then_lower_high_5d_d2},
    "f06_cscr_143_reversal_followed_by_close_below_low_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_143_reversal_followed_by_close_below_low_d2},
    "f06_cscr_144_reversal_strength_normalized_by_prior_range_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_144_reversal_strength_normalized_by_prior_range_d2},
    "f06_cscr_145_close_at_session_low_indicator_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_145_close_at_session_low_indicator_d2},
    "f06_cscr_146_close_at_session_low_count_21d_at_high_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_146_close_at_session_low_count_21d_at_high_d2},
    "f06_cscr_147_reversal_severity_x_volume_zscore_d2": {"inputs": ["open", "high", "low", "close", "volume"], "func": f06_cscr_147_reversal_severity_x_volume_zscore_d2},
    "f06_cscr_148_consecutive_bear_severity_streak_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_148_consecutive_bear_severity_streak_d2},
    "f06_cscr_149_severity_imbalance_21d_minus_63d_mean_d2": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_149_severity_imbalance_21d_minus_63d_mean_d2},
    "f06_cscr_150_terminal_reversal_score_d2": {"inputs": ["open", "high", "low", "close", "volume"], "func": f06_cscr_150_terminal_reversal_score_d2},
}
