"""candlestick_reversal_catalog base features 001-075 — Pipeline 1b-technical.

Bearish candlestick reversal patterns, especially AT or NEAR a multi-year
high. SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers.
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


# Common compact gates ----

def _near_252d_high_atr(high, low, close, k=1.0):
    """Bool series: today's high within k*ATR21 of 252d rolling max."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    return (rmax - high) <= (k * atr)


def f06_cscr_001_body_to_range_ratio(open_, high, low, close):
    """|close-open| / (high-low) — small = doji-like."""
    return _safe_div((close - open_).abs(), high - low)


def f06_cscr_002_doji_indicator_at_252d_high(open_, high, low, close):
    """1 if today's body <= 10% of range AND high is the 252d max."""
    body = (close - open_).abs()
    rng = high - low
    is_doji = (_safe_div(body, rng) <= 0.10).astype(float)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = (high >= rmax).astype(float)
    return (is_doji * at_peak).where(is_doji.notna() & at_peak.notna(), np.nan)


def f06_cscr_003_dragonfly_doji_score(open_, high, low, close):
    """Dragonfly doji score."""
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = high - body_top
    lower = body_bot - low
    score = (1.0 - body / rng) * (lower / rng)
    return score.where(_safe_div(upper, rng) <= 0.1, 0.0)


def f06_cscr_004_gravestone_doji_score(open_, high, low, close):
    """Gravestone doji score."""
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = high - body_top
    lower = body_bot - low
    score = (1.0 - body / rng) * (upper / rng)
    return score.where(_safe_div(lower, rng) <= 0.1, 0.0)


def f06_cscr_005_long_legged_doji_score(open_, high, low, close):
    """Long-legged doji score."""
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = (high - body_top) / rng
    lower = (body_bot - low) / rng
    small_body = (body / rng) <= 0.1
    return (upper * lower).where(small_body, 0.0)


def f06_cscr_006_four_price_doji_proxy(open_, high, low, close):
    """Four-price doji proxy."""
    rng_norm = _safe_div(high - low, close)
    same = (open_ == close) & (high == low)
    return (same.astype(float) + (rng_norm < 0.001).astype(float)) / 2.0


def f06_cscr_007_doji_within_atr_of_252d_high(open_, high, low, close):
    """Doji within 1 ATR of 252d high."""
    body_ratio = _safe_div((close - open_).abs(), high - low)
    is_doji = (body_ratio <= 0.10).astype(float)
    near = _near_252d_high_atr(high, low, close, k=1.0).astype(float)
    return (is_doji * near).where(body_ratio.notna() & near.notna(), np.nan)


def f06_cscr_008_doji_count_21d_while_near_252d_high(open_, high, low, close):
    """Doji count, 21d near 252d high."""
    body_ratio = _safe_div((close - open_).abs(), high - low)
    is_doji = (body_ratio <= 0.10).astype(float)
    near = _near_252d_high_atr(high, low, close, k=2.0).astype(float)
    flag = is_doji * near
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f06_cscr_009_doji_count_63d_while_near_252d_high(open_, high, low, close):
    """Doji count, 63d near 252d high."""
    body_ratio = _safe_div((close - open_).abs(), high - low)
    is_doji = (body_ratio <= 0.10).astype(float)
    near = _near_252d_high_atr(high, low, close, k=2.0).astype(float)
    flag = is_doji * near
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f06_cscr_010_doji_after_strong_advance(open_, high, low, close):
    """Doji after strong 5d advance."""
    body_ratio = _safe_div((close - open_).abs(), high - low)
    is_doji = (body_ratio <= 0.10).astype(float)
    ret5 = _safe_log(close) - _safe_log(close.shift(WDAYS))
    advance = (ret5 > 0.08).astype(float)
    return (is_doji * advance).where(is_doji.notna() & ret5.notna(), np.nan)


def f06_cscr_011_body_engulf_bearish_indicator(open_, close):
    """Bearish body-engulf indicator."""
    prev_o = open_.shift(1)
    prev_c = close.shift(1)
    today_red = close < open_
    prev_green = prev_c > prev_o
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    prev_top = pd.concat([prev_o, prev_c], axis=1).max(axis=1)
    prev_bot = pd.concat([prev_o, prev_c], axis=1).min(axis=1)
    engulf = (today_top >= prev_top) & (today_bot <= prev_bot)
    flag = (today_red & prev_green & engulf).astype(float)
    return flag.where(prev_c.notna(), np.nan)


def f06_cscr_012_range_engulf_bearish_indicator(open_, high, low, close):
    """Bearish range-engulf indicator."""
    prev_h = high.shift(1)
    prev_l = low.shift(1)
    today_red = close < open_
    engulf = (high >= prev_h) & (low <= prev_l)
    flag = (today_red & engulf).astype(float)
    return flag.where(prev_h.notna(), np.nan)


def f06_cscr_013_bearish_engulfing_severity(open_, close):
    """Engulf severity (today body / prior body)."""
    prev_o = open_.shift(1)
    prev_c = close.shift(1)
    today_red = close < open_
    prev_green = prev_c > prev_o
    today_body = (open_ - close).where(today_red, np.nan)
    prev_body = (prev_c - prev_o).where(prev_green, np.nan)
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    prev_top = pd.concat([prev_o, prev_c], axis=1).max(axis=1)
    prev_bot = pd.concat([prev_o, prev_c], axis=1).min(axis=1)
    engulf = (today_top >= prev_top) & (today_bot <= prev_bot)
    severity = _safe_div(today_body, prev_body)
    return severity.where(engulf & today_red & prev_green, np.nan)


def f06_cscr_014_bearish_engulf_at_252d_high(open_, high, low, close):
    """Bearish engulf at 252d high."""
    prev_o = open_.shift(1)
    prev_c = close.shift(1)
    today_red = close < open_
    prev_green = prev_c > prev_o
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    prev_top = pd.concat([prev_o, prev_c], axis=1).max(axis=1)
    prev_bot = pd.concat([prev_o, prev_c], axis=1).min(axis=1)
    engulf = (today_top >= prev_top) & (today_bot <= prev_bot)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = high >= rmax
    flag = (today_red & prev_green & engulf & at_peak).astype(float)
    return flag.where(prev_c.notna() & at_peak.notna(), np.nan)


def f06_cscr_015_bearish_engulf_within_atr_of_252d_high(open_, high, low, close):
    """Bearish engulf within 1 ATR of 252d max."""
    prev_o = open_.shift(1)
    prev_c = close.shift(1)
    today_red = close < open_
    prev_green = prev_c > prev_o
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    prev_top = pd.concat([prev_o, prev_c], axis=1).max(axis=1)
    prev_bot = pd.concat([prev_o, prev_c], axis=1).min(axis=1)
    engulf = (today_top >= prev_top) & (today_bot <= prev_bot)
    near = _near_252d_high_atr(high, low, close, k=1.0)
    flag = (today_red & prev_green & engulf & near).astype(float)
    return flag.where(near.notna(), np.nan)


def f06_cscr_016_bearish_engulf_volume_confirmed(open_, close, volume):
    """Bearish engulf, volume confirmed."""
    prev_o = open_.shift(1)
    prev_c = close.shift(1)
    today_red = close < open_
    prev_green = prev_c > prev_o
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    prev_top = pd.concat([prev_o, prev_c], axis=1).max(axis=1)
    prev_bot = pd.concat([prev_o, prev_c], axis=1).min(axis=1)
    engulf = (today_top >= prev_top) & (today_bot <= prev_bot)
    vavg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    vol_ok = volume > 1.5 * vavg
    flag = (today_red & prev_green & engulf & vol_ok).astype(float)
    return flag.where(vavg.notna(), np.nan)


def f06_cscr_017_bearish_engulf_count_63d(open_, close):
    """Bearish engulf count (63d)."""
    prev_o = open_.shift(1)
    prev_c = close.shift(1)
    today_red = close < open_
    prev_green = prev_c > prev_o
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    prev_top = pd.concat([prev_o, prev_c], axis=1).max(axis=1)
    prev_bot = pd.concat([prev_o, prev_c], axis=1).min(axis=1)
    engulf = (today_top >= prev_top) & (today_bot <= prev_bot)
    flag = (today_red & prev_green & engulf).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f06_cscr_018_bearish_engulf_count_252d_at_high(open_, high, low, close):
    """Bearish engulf count, 252d at high."""
    prev_o = open_.shift(1)
    prev_c = close.shift(1)
    today_red = close < open_
    prev_green = prev_c > prev_o
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    prev_top = pd.concat([prev_o, prev_c], axis=1).max(axis=1)
    prev_bot = pd.concat([prev_o, prev_c], axis=1).min(axis=1)
    engulf = (today_top >= prev_top) & (today_bot <= prev_bot)
    near = _near_252d_high_atr(high, low, close, k=2.0)
    flag = (today_red & prev_green & engulf & near).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f06_cscr_019_bars_since_last_bearish_engulf_at_high(open_, high, low, close):
    """Bars since last bearish engulf at high."""
    prev_o = open_.shift(1)
    prev_c = close.shift(1)
    today_red = close < open_
    prev_green = prev_c > prev_o
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    prev_top = pd.concat([prev_o, prev_c], axis=1).max(axis=1)
    prev_bot = pd.concat([prev_o, prev_c], axis=1).min(axis=1)
    engulf = (today_top >= prev_top) & (today_bot <= prev_bot)
    near = _near_252d_high_atr(high, low, close, k=2.0)
    flag = (today_red & prev_green & engulf & near).astype(float).to_numpy(copy=True)
    n = len(flag)
    out = np.full(n, np.nan, dtype=float)
    last = -1
    for i in range(n):
        if not np.isnan(flag[i]):
            if flag[i] > 0:
                last = i
            if last >= 0:
                out[i] = float(i - last)
    return pd.Series(out, index=close.index)


def f06_cscr_020_atr_normalized_engulf_body_ratio(open_, high, low, close):
    """Engulf body / ATR21."""
    prev_o = open_.shift(1)
    prev_c = close.shift(1)
    today_red = close < open_
    prev_green = prev_c > prev_o
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    prev_top = pd.concat([prev_o, prev_c], axis=1).max(axis=1)
    prev_bot = pd.concat([prev_o, prev_c], axis=1).min(axis=1)
    engulf = (today_top >= prev_top) & (today_bot <= prev_bot)
    body = open_ - close
    atr = _atr(high, low, close, n=MDAYS)
    val = _safe_div(body, atr)
    return val.where(today_red & prev_green & engulf, np.nan)


def f06_cscr_021_hanging_man_at_252d_high(open_, high, low, close):
    """Hanging man at 252d high."""
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = high - body_top
    lower = body_bot - low
    small_body = (body / rng) <= 0.3
    long_lower = lower >= 2.0 * body
    short_upper = (upper / rng) <= 0.1
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = high >= rmax
    flag = (small_body & long_lower & short_upper & at_peak).astype(float)
    return flag.where(rng.notna() & at_peak.notna(), np.nan)


def f06_cscr_022_hanging_man_lower_shadow_to_body_ratio(open_, high, low, close):
    """Hanging-man lower-shadow / body ratio."""
    body = (close - open_).abs().replace(0, np.nan)
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = high - body_top
    lower = body_bot - low
    ratio = lower / body
    qualifies = ((body / rng) <= 0.4) & ((upper / rng) <= 0.2)
    return ratio.where(qualifies, np.nan)


def f06_cscr_023_hanging_man_volume_confirmed(open_, high, low, close, volume):
    """Hanging man, volume confirmed."""
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = high - body_top
    lower = body_bot - low
    small_body = (body / rng) <= 0.3
    long_lower = lower >= 2.0 * body
    short_upper = (upper / rng) <= 0.1
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = high >= rmax
    vavg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    vol_ok = volume > 1.2 * vavg
    flag = (small_body & long_lower & short_upper & at_peak & vol_ok).astype(float)
    return flag.where(rng.notna() & vavg.notna(), np.nan)


def f06_cscr_024_hammer_after_decline_no_followthrough(open_, high, low, close):
    """Hammer after decline (no follow-through)."""
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = high - body_top
    lower = body_bot - low
    small_body = (body / rng) <= 0.3
    long_lower = lower >= 2.0 * body
    short_upper = (upper / rng) <= 0.1
    decline = (close - close.shift(WDAYS)) < 0
    hammer = small_body & long_lower & short_upper & decline
    return hammer.astype(float).where(rng.notna(), np.nan)


def f06_cscr_025_hanging_man_count_21d_at_high(open_, high, low, close):
    """Hanging-man count, 21d at high."""
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = high - body_top
    lower = body_bot - low
    small_body = (body / rng) <= 0.3
    long_lower = lower >= 2.0 * body
    short_upper = (upper / rng) <= 0.1
    near = _near_252d_high_atr(high, low, close, k=2.0)
    flag = (small_body & long_lower & short_upper & near).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f06_cscr_026_hanging_man_count_63d_at_high(open_, high, low, close):
    """Hanging-man count, 63d at high."""
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = high - body_top
    lower = body_bot - low
    small_body = (body / rng) <= 0.3
    long_lower = lower >= 2.0 * body
    short_upper = (upper / rng) <= 0.1
    near = _near_252d_high_atr(high, low, close, k=2.0)
    flag = (small_body & long_lower & short_upper & near).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f06_cscr_027_hanging_man_followthrough_indicator(open_, high, low, close):
    """Hanging-man followthrough indicator."""
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = high - body_top
    lower = body_bot - low
    small_body = (body / rng) <= 0.3
    long_lower = lower >= 2.0 * body
    short_upper = (upper / rng) <= 0.1
    red = close < open_
    rmax21 = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    prior_peak = high.shift(1) >= rmax21
    flag = (small_body & long_lower & short_upper & red & prior_peak).astype(float)
    return flag.where(rng.notna() & rmax21.notna(), np.nan)


def f06_cscr_028_hanging_man_atr_norm_lower_shadow(open_, high, low, close):
    """Hanging-man lower shadow / ATR."""
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = high - body_top
    lower = body_bot - low
    small_body = (body / rng) <= 0.3
    long_lower = lower >= 2.0 * body
    short_upper = (upper / rng) <= 0.1
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = high >= rmax
    atr = _atr(high, low, close, n=MDAYS)
    val = _safe_div(lower, atr)
    return val.where(small_body & long_lower & short_upper & at_peak, np.nan)


def f06_cscr_029_shooting_star_at_252d_high(open_, high, low, close):
    """Shooting star at 252d high."""
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = high - body_top
    lower = body_bot - low
    small_body = (body / rng) <= 0.3
    long_upper = upper >= 2.0 * body
    short_lower = (lower / rng) <= 0.1
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = high >= rmax
    flag = (small_body & long_upper & short_lower & at_peak).astype(float)
    return flag.where(rng.notna() & at_peak.notna(), np.nan)


def f06_cscr_030_shooting_star_upper_shadow_to_body_ratio(open_, high, low, close):
    """Shooting-star upper-shadow / body ratio."""
    body = (close - open_).abs().replace(0, np.nan)
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = high - body_top
    lower = body_bot - low
    ratio = upper / body
    qualifies = ((body / rng) <= 0.4) & ((lower / rng) <= 0.2)
    return ratio.where(qualifies, np.nan)


def f06_cscr_031_shooting_star_within_atr_of_252d_high(open_, high, low, close):
    """Shooting star within 1 ATR of 252d max."""
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = high - body_top
    lower = body_bot - low
    small_body = (body / rng) <= 0.3
    long_upper = upper >= 2.0 * body
    short_lower = (lower / rng) <= 0.1
    near = _near_252d_high_atr(high, low, close, k=1.0)
    flag = (small_body & long_upper & short_lower & near).astype(float)
    return flag.where(rng.notna() & near.notna(), np.nan)


def f06_cscr_032_inverted_hammer_failure(open_, high, low, close):
    """Inverted hammer at 252d high (failure context)."""
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = high - body_top
    lower = body_bot - low
    small_body = (body / rng) <= 0.3
    long_upper = upper >= 2.0 * body
    short_lower = (lower / rng) <= 0.1
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = high >= rmax
    flag = (small_body & long_upper & short_lower & at_peak).astype(float)
    return flag.where(rng.notna() & at_peak.notna(), np.nan)


def f06_cscr_033_shooting_star_count_21d_at_high(open_, high, low, close):
    """Shooting-star count, 21d at high."""
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = high - body_top
    lower = body_bot - low
    small_body = (body / rng) <= 0.3
    long_upper = upper >= 2.0 * body
    short_lower = (lower / rng) <= 0.1
    near = _near_252d_high_atr(high, low, close, k=2.0)
    flag = (small_body & long_upper & short_lower & near).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f06_cscr_034_shooting_star_count_63d_at_high(open_, high, low, close):
    """Shooting-star count, 63d at high."""
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = high - body_top
    lower = body_bot - low
    small_body = (body / rng) <= 0.3
    long_upper = upper >= 2.0 * body
    short_lower = (lower / rng) <= 0.1
    near = _near_252d_high_atr(high, low, close, k=2.0)
    flag = (small_body & long_upper & short_lower & near).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f06_cscr_035_shooting_star_atr_norm_upper_shadow(open_, high, low, close):
    """Shooting-star upper shadow / ATR."""
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = high - body_top
    lower = body_bot - low
    small_body = (body / rng) <= 0.3
    long_upper = upper >= 2.0 * body
    short_lower = (lower / rng) <= 0.1
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = high >= rmax
    atr = _atr(high, low, close, n=MDAYS)
    val = _safe_div(upper, atr)
    return val.where(small_body & long_upper & short_lower & at_peak, np.nan)


def f06_cscr_036_shooting_star_volume_confirmed(open_, high, low, close, volume):
    """Shooting star, volume confirmed."""
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = high - body_top
    lower = body_bot - low
    small_body = (body / rng) <= 0.3
    long_upper = upper >= 2.0 * body
    short_lower = (lower / rng) <= 0.1
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = high >= rmax
    vavg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    vol_ok = volume > 1.2 * vavg
    flag = (small_body & long_upper & short_lower & at_peak & vol_ok).astype(float)
    return flag.where(vavg.notna() & at_peak.notna(), np.nan)


def f06_cscr_037_tweezer_top_indicator(high, close, open_):
    """Tweezer top indicator."""
    prev_h = high.shift(1)
    prev_o = open_.shift(1)
    prev_c = close.shift(1)
    near_eq = (high - prev_h).abs() / prev_h.replace(0, np.nan) <= 0.001
    prev_green = prev_c > prev_o
    today_red = close < open_
    flag = (near_eq & prev_green & today_red).astype(float)
    return flag.where(prev_h.notna(), np.nan)


def f06_cscr_038_tweezer_top_at_252d_high(open_, high, low, close):
    """Tweezer top at 252d high."""
    prev_h = high.shift(1)
    prev_o = open_.shift(1)
    prev_c = close.shift(1)
    near_eq = (high - prev_h).abs() / prev_h.replace(0, np.nan) <= 0.001
    prev_green = prev_c > prev_o
    today_red = close < open_
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = (prev_h >= rmax.shift(1)) | (high >= rmax)
    flag = (near_eq & prev_green & today_red & at_peak).astype(float)
    return flag.where(rmax.notna(), np.nan)


def f06_cscr_039_tweezer_top_count_63d(open_, high, close):
    """Tweezer-top count (63d)."""
    prev_h = high.shift(1)
    prev_o = open_.shift(1)
    prev_c = close.shift(1)
    near_eq = (high - prev_h).abs() / prev_h.replace(0, np.nan) <= 0.001
    prev_green = prev_c > prev_o
    today_red = close < open_
    flag = (near_eq & prev_green & today_red).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f06_cscr_040_max_consecutive_near_eq_highs_21d(high):
    """Max consecutive near-equal-highs run, 21d."""
    prev_h = high.shift(1)
    near_eq = ((high - prev_h).abs() / prev_h.replace(0, np.nan) <= 0.002).astype(float).to_numpy(copy=True)
    near_eq[0] = 0.0
    n = len(near_eq)
    streak = np.zeros(n, dtype=float)
    cur = 0
    for i in range(n):
        if near_eq[i] > 0:
            cur += 1
        else:
            cur = 0
        streak[i] = cur
    s = pd.Series(streak, index=high.index)
    return s.rolling(MDAYS, min_periods=WDAYS).max()


def f06_cscr_041_tweezer_top_atr_norm_high_match_tightness(high, low, close):
    """Tweezer high-match tightness (ATR units)."""
    prev_h = high.shift(1)
    atr = _atr(high, low, close, n=MDAYS)
    return _safe_div((high - prev_h).abs(), atr)


def f06_cscr_042_three_bar_tweezer_top_indicator(high, open_, close):
    """Three-bar tweezer-top indicator."""
    prev_h1 = high.shift(1)
    prev_h2 = high.shift(2)
    near1 = (high - prev_h1).abs() / prev_h1.replace(0, np.nan) <= 0.002
    near2 = (prev_h1 - prev_h2).abs() / prev_h2.replace(0, np.nan) <= 0.002
    today_red = close < open_
    flag = (near1 & near2 & today_red).astype(float)
    return flag.where(prev_h2.notna(), np.nan)


def f06_cscr_043_dark_cloud_cover_indicator(open_, high, low, close):
    """Dark cloud cover indicator."""
    prev_o = open_.shift(1)
    prev_c = close.shift(1)
    prev_h = high.shift(1)
    prev_green = prev_c > prev_o
    gap_open = open_ > prev_h
    prev_mid = (prev_o + prev_c) / 2.0
    cls_below_mid = close < prev_mid
    cls_above_prev_open = close > prev_o
    flag = (prev_green & gap_open & cls_below_mid & cls_above_prev_open).astype(float)
    return flag.where(prev_h.notna(), np.nan)


def f06_cscr_044_dark_cloud_penetration_depth(open_, close):
    """Dark-cloud penetration depth."""
    prev_o = open_.shift(1)
    prev_c = close.shift(1)
    prev_body = (prev_c - prev_o)
    pen = _safe_div(prev_c - close, prev_body)
    qualifies = (prev_c > prev_o) & (close < ((prev_o + prev_c) / 2.0)) & (close > prev_o)
    return pen.where(qualifies, np.nan)


def f06_cscr_045_dark_cloud_at_252d_high(open_, high, low, close):
    """Dark cloud at 252d high."""
    prev_o = open_.shift(1)
    prev_c = close.shift(1)
    prev_h = high.shift(1)
    prev_green = prev_c > prev_o
    gap_open = open_ > prev_h
    prev_mid = (prev_o + prev_c) / 2.0
    cls_below_mid = close < prev_mid
    cls_above_prev_open = close > prev_o
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = prev_h >= rmax.shift(1)
    flag = (prev_green & gap_open & cls_below_mid & cls_above_prev_open & at_peak).astype(float)
    return flag.where(rmax.notna(), np.nan)


def f06_cscr_046_dark_cloud_count_252d(open_, high, low, close):
    """Dark-cloud count (252d)."""
    prev_o = open_.shift(1)
    prev_c = close.shift(1)
    prev_h = high.shift(1)
    prev_green = prev_c > prev_o
    gap_open = open_ > prev_h
    prev_mid = (prev_o + prev_c) / 2.0
    cls_below_mid = close < prev_mid
    cls_above_prev_open = close > prev_o
    flag = (prev_green & gap_open & cls_below_mid & cls_above_prev_open).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f06_cscr_047_dark_cloud_volume_confirmed(open_, high, low, close, volume):
    """Dark cloud, volume confirmed."""
    prev_o = open_.shift(1)
    prev_c = close.shift(1)
    prev_h = high.shift(1)
    prev_green = prev_c > prev_o
    gap_open = open_ > prev_h
    prev_mid = (prev_o + prev_c) / 2.0
    cls_below_mid = close < prev_mid
    cls_above_prev_open = close > prev_o
    vavg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    vol_ok = volume > 1.3 * vavg
    flag = (prev_green & gap_open & cls_below_mid & cls_above_prev_open & vol_ok).astype(float)
    return flag.where(vavg.notna(), np.nan)


def f06_cscr_048_dark_cloud_followthrough_5d(open_, high, low, close):
    """Dark cloud + next-day follow-through count (63d)."""
    prev_o = open_.shift(1)
    prev_c = close.shift(1)
    prev_h = high.shift(1)
    prev_green = prev_c > prev_o
    gap_open = open_ > prev_h
    prev_mid = (prev_o + prev_c) / 2.0
    cls_below_mid = close < prev_mid
    cls_above_prev_open = close > prev_o
    flag = (prev_green & gap_open & cls_below_mid & cls_above_prev_open).astype(float)
    # next-day confirmation: shift result forward by 1, but to avoid lookahead we
    # detect the prior-day-event AND today's close down.
    prior_event = flag.shift(1)
    today_down = (close < close.shift(1)).astype(float)
    confirmed = (prior_event * today_down)
    return confirmed.rolling(QDAYS, min_periods=MDAYS).sum()


def f06_cscr_049_bearish_harami_indicator(open_, close):
    """Bearish harami indicator."""
    prev_o = open_.shift(1)
    prev_c = close.shift(1)
    prev_green = prev_c > prev_o
    today_red = close < open_
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    inside = (today_top <= prev_c) & (today_bot >= prev_o)
    flag = (prev_green & today_red & inside).astype(float)
    return flag.where(prev_c.notna(), np.nan)


def f06_cscr_050_bearish_harami_at_252d_high(open_, high, low, close):
    """Bearish harami at 252d high."""
    prev_o = open_.shift(1)
    prev_c = close.shift(1)
    prev_h = high.shift(1)
    prev_green = prev_c > prev_o
    today_red = close < open_
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    inside = (today_top <= prev_c) & (today_bot >= prev_o)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = prev_h >= rmax.shift(1)
    flag = (prev_green & today_red & inside & at_peak).astype(float)
    return flag.where(rmax.notna(), np.nan)


def f06_cscr_051_bearish_harami_body_compression_ratio(open_, close):
    """Bearish harami body compression ratio."""
    prev_o = open_.shift(1)
    prev_c = close.shift(1)
    prev_body = (prev_c - prev_o)
    today_body = (open_ - close)
    prev_green = prev_c > prev_o
    today_red = close < open_
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    inside = (today_top <= prev_c) & (today_bot >= prev_o)
    qualifies = prev_green & today_red & inside
    return _safe_div(today_body, prev_body).where(qualifies, np.nan)


def f06_cscr_052_harami_cross_at_high(open_, high, low, close):
    """Harami cross at 252d high."""
    prev_o = open_.shift(1)
    prev_c = close.shift(1)
    prev_h = high.shift(1)
    prev_green = prev_c > prev_o
    today_body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    is_doji = (today_body / rng) <= 0.05
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    inside = (today_top <= prev_c) & (today_bot >= prev_o)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = prev_h >= rmax.shift(1)
    flag = (prev_green & is_doji & inside & at_peak).astype(float)
    return flag.where(rmax.notna(), np.nan)


def f06_cscr_053_bearish_harami_count_252d(open_, close):
    """Bearish harami count (252d)."""
    prev_o = open_.shift(1)
    prev_c = close.shift(1)
    prev_green = prev_c > prev_o
    today_red = close < open_
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    inside = (today_top <= prev_c) & (today_bot >= prev_o)
    flag = (prev_green & today_red & inside).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f06_cscr_054_bearish_harami_volume_confirmed(open_, close, volume):
    """Bearish harami, volume confirmed."""
    prev_o = open_.shift(1)
    prev_c = close.shift(1)
    prev_green = prev_c > prev_o
    today_red = close < open_
    today_top = pd.concat([open_, close], axis=1).max(axis=1)
    today_bot = pd.concat([open_, close], axis=1).min(axis=1)
    inside = (today_top <= prev_c) & (today_bot >= prev_o)
    vavg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    vol_ok = volume > 1.2 * vavg
    flag = (prev_green & today_red & inside & vol_ok).astype(float)
    return flag.where(vavg.notna(), np.nan)


def f06_cscr_055_evening_star_indicator(open_, high, low, close):
    """Evening star indicator."""
    o1 = open_.shift(2); c1 = close.shift(2)
    o2 = open_.shift(1); c2 = close.shift(1)
    h2 = high.shift(1); l2 = low.shift(1)
    body1 = (c1 - o1)
    body2 = (c2 - o2).abs()
    rng2 = (h2 - l2).replace(0, np.nan)
    body3 = (open_ - close)
    bar1_green = body1 > 0
    bar2_small = (body2 / rng2) <= 0.3
    bar3_red = body3 > 0
    mid1 = (o1 + c1) / 2.0
    bar3_below_mid1 = close < mid1
    flag = (bar1_green & bar2_small & bar3_red & bar3_below_mid1).astype(float)
    return flag.where(o1.notna(), np.nan)


def f06_cscr_056_evening_star_at_252d_high(open_, high, low, close):
    """Evening star at 252d high."""
    o1 = open_.shift(2); c1 = close.shift(2)
    o2 = open_.shift(1); c2 = close.shift(1)
    h2 = high.shift(1); l2 = low.shift(1)
    body1 = (c1 - o1)
    body2 = (c2 - o2).abs()
    rng2 = (h2 - l2).replace(0, np.nan)
    body3 = (open_ - close)
    bar1_green = body1 > 0
    bar2_small = (body2 / rng2) <= 0.3
    bar3_red = body3 > 0
    mid1 = (o1 + c1) / 2.0
    bar3_below_mid1 = close < mid1
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = h2 >= rmax.shift(1)
    flag = (bar1_green & bar2_small & bar3_red & bar3_below_mid1 & at_peak).astype(float)
    return flag.where(rmax.notna(), np.nan)


def f06_cscr_057_evening_doji_star_indicator(open_, high, low, close):
    """Evening doji star."""
    o1 = open_.shift(2); c1 = close.shift(2)
    o2 = open_.shift(1); c2 = close.shift(1)
    h2 = high.shift(1); l2 = low.shift(1)
    body1 = (c1 - o1)
    body2 = (c2 - o2).abs()
    rng2 = (h2 - l2).replace(0, np.nan)
    body3 = (open_ - close)
    bar1_green = body1 > 0
    bar2_doji = (body2 / rng2) <= 0.05
    bar3_red = body3 > 0
    mid1 = (o1 + c1) / 2.0
    bar3_below_mid1 = close < mid1
    flag = (bar1_green & bar2_doji & bar3_red & bar3_below_mid1).astype(float)
    return flag.where(o1.notna(), np.nan)


def f06_cscr_058_three_black_crows_indicator(open_, close):
    """Three black crows."""
    o0 = open_; c0 = close
    o1 = open_.shift(1); c1 = close.shift(1)
    o2 = open_.shift(2); c2 = close.shift(2)
    red0 = c0 < o0
    red1 = c1 < o1
    red2 = c2 < o2
    lower_lows = (c0 < c1) & (c1 < c2)
    open_in_body = (o0 < o1) & (o0 > c1) & (o1 < o2) & (o1 > c2)
    flag = (red0 & red1 & red2 & lower_lows & open_in_body).astype(float)
    return flag.where(c2.notna(), np.nan)


def f06_cscr_059_three_inside_down_indicator(open_, close):
    """Three-inside-down indicator."""
    o1 = open_.shift(2); c1 = close.shift(2)
    o2 = open_.shift(1); c2 = close.shift(1)
    o3 = open_; c3 = close
    bar1_green = c1 > o1
    bar2_red = c2 < o2
    top2 = pd.concat([o2, c2], axis=1).max(axis=1)
    bot2 = pd.concat([o2, c2], axis=1).min(axis=1)
    inside = (top2 <= c1) & (bot2 >= o1)
    bar3_red = c3 < o3
    bar3_break = c3 < c1
    flag = (bar1_green & bar2_red & inside & bar3_red & bar3_break).astype(float)
    return flag.where(c1.notna(), np.nan)


def f06_cscr_060_three_line_strike_bearish(open_, close):
    """Bearish three-line strike."""
    o1 = open_.shift(3); c1 = close.shift(3)
    o2 = open_.shift(2); c2 = close.shift(2)
    o3 = open_.shift(1); c3 = close.shift(1)
    o4 = open_; c4 = close
    red1 = c1 < o1
    red2 = c2 < o2
    red3 = c3 < o3
    lower_lows = (c2 < c1) & (c3 < c2)
    green4 = c4 > o4
    spec_open = o4 < c3
    spec_close = c4 > o1
    flag = (red1 & red2 & red3 & lower_lows & green4 & spec_open & spec_close).astype(float)
    return flag.where(c1.notna(), np.nan)


def f06_cscr_061_abandoned_baby_top_indicator(open_, high, low, close):
    """Abandoned baby top."""
    o1 = open_.shift(2); c1 = close.shift(2); h1 = high.shift(2)
    o2 = open_.shift(1); c2 = close.shift(1); h2 = high.shift(1); l2 = low.shift(1)
    o3 = open_; c3 = close
    body1 = (c1 - o1)
    body2 = (c2 - o2).abs()
    rng2 = (h2 - l2).replace(0, np.nan)
    body3 = (o3 - c3)
    bar1_green = body1 > 0
    bar2_doji = (body2 / rng2) <= 0.05
    bar3_red = body3 > 0
    gap_up_b2 = l2 > h1
    gap_down_b3 = pd.concat([o3, c3], axis=1).max(axis=1) < l2
    flag = (bar1_green & bar2_doji & bar3_red & gap_up_b2 & gap_down_b3).astype(float)
    return flag.where(o1.notna(), np.nan)


def f06_cscr_062_three_black_crows_count_252d(open_, close):
    """Three-black-crows count (252d)."""
    o0 = open_; c0 = close
    o1 = open_.shift(1); c1 = close.shift(1)
    o2 = open_.shift(2); c2 = close.shift(2)
    red0 = c0 < o0
    red1 = c1 < o1
    red2 = c2 < o2
    lower_lows = (c0 < c1) & (c1 < c2)
    open_in_body = (o0 < o1) & (o0 > c1) & (o1 < o2) & (o1 > c2)
    flag = (red0 & red1 & red2 & lower_lows & open_in_body).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f06_cscr_063_evening_star_count_252d_at_high(open_, high, low, close):
    """Evening-star count, 252d at high."""
    o1 = open_.shift(2); c1 = close.shift(2)
    o2 = open_.shift(1); c2 = close.shift(1)
    h2 = high.shift(1); l2 = low.shift(1)
    body1 = (c1 - o1)
    body2 = (c2 - o2).abs()
    rng2 = (h2 - l2).replace(0, np.nan)
    body3 = (open_ - close)
    bar1_green = body1 > 0
    bar2_small = (body2 / rng2) <= 0.3
    bar3_red = body3 > 0
    mid1 = (o1 + c1) / 2.0
    bar3_below_mid1 = close < mid1
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = h2 >= rmax.shift(1)
    flag = (bar1_green & bar2_small & bar3_red & bar3_below_mid1 & at_peak).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f06_cscr_064_spinning_top_indicator(open_, high, low, close):
    """Spinning top indicator."""
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = (high - body_top) / rng
    lower = (body_bot - low) / rng
    small_body = (body / rng) <= 0.3
    bal = (upper >= 0.25) & (lower >= 0.25)
    flag = (small_body & bal).astype(float)
    return flag.where(rng.notna(), np.nan)


def f06_cscr_065_high_wave_candle_indicator(open_, high, low, close):
    """High-wave candle indicator."""
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = (high - body_top) / rng
    lower = (body_bot - low) / rng
    small_body = (body / rng) <= 0.15
    long_shadows = (upper >= 0.4) & (lower >= 0.4)
    flag = (small_body & long_shadows).astype(float)
    return flag.where(rng.notna(), np.nan)


def f06_cscr_066_spinning_top_count_21d_at_high(open_, high, low, close):
    """Spinning-top count, 21d at high."""
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = (high - body_top) / rng
    lower = (body_bot - low) / rng
    small_body = (body / rng) <= 0.3
    bal = (upper >= 0.25) & (lower >= 0.25)
    near = _near_252d_high_atr(high, low, close, k=2.0)
    flag = (small_body & bal & near).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f06_cscr_067_high_wave_count_63d_at_high(open_, high, low, close):
    """High-wave count, 63d at high."""
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper = (high - body_top) / rng
    lower = (body_bot - low) / rng
    small_body = (body / rng) <= 0.15
    long_shadows = (upper >= 0.4) & (lower >= 0.4)
    near = _near_252d_high_atr(high, low, close, k=2.0)
    flag = (small_body & long_shadows & near).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f06_cscr_068_star_shape_score(open_, high, low, close):
    """Star-shape score (bearish-weighted)."""
    prev_o = open_.shift(1); prev_c = close.shift(1); prev_h = high.shift(1)
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    small = 1.0 - (body / rng)
    gap = (low - prev_h).clip(lower=0)
    today_red = (close < open_).astype(float)
    return small * gap * today_red


def f06_cscr_069_bearish_marubozu_indicator(open_, high, low, close):
    """Bearish marubozu indicator."""
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    red = close < open_
    big_body = (body / rng) >= 0.9
    flag = (red & big_body).astype(float)
    return flag.where(rng.notna(), np.nan)


def f06_cscr_070_bearish_marubozu_at_252d_high(open_, high, low, close):
    """Bearish marubozu at 252d high."""
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    red = close < open_
    big_body = (body / rng) >= 0.9
    prev_h = high.shift(1)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak_prior = prev_h >= rmax.shift(1)
    flag = (red & big_body & at_peak_prior).astype(float)
    return flag.where(rmax.notna(), np.nan)


def f06_cscr_071_marubozu_failure_within_5d(open_, high, low, close):
    """Marubozu failure within 5 bars, count (63d)."""
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    green = close > open_
    big = (body / rng) >= 0.9
    bull_maru = (green & big).astype(float)
    # for each bar, check the marubozu k-bars-ago and whether today's close < its open
    fails = pd.Series(0.0, index=close.index)
    for k in range(1, WDAYS + 1):
        mar = bull_maru.shift(k)
        mar_open = open_.shift(k)
        fail_today = (mar > 0) & (close < mar_open)
        fails = fails + fail_today.astype(float)
    fails = (fails > 0).astype(float)
    return fails.rolling(QDAYS, min_periods=MDAYS).sum()


def f06_cscr_072_bullish_marubozu_then_doji_indicator(open_, high, low, close):
    """Bullish marubozu then doji."""
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    prev_body = (close.shift(1) - open_.shift(1))
    prev_rng = (high.shift(1) - low.shift(1)).replace(0, np.nan)
    prev_bull_maru = (close.shift(1) > open_.shift(1)) & ((prev_body.abs() / prev_rng) >= 0.9)
    today_doji = (body / rng) <= 0.1
    flag = (prev_bull_maru & today_doji).astype(float)
    return flag.where(rng.notna() & prev_rng.notna(), np.nan)


def f06_cscr_073_bearish_kicker_pattern(open_, close):
    """Bearish kicker pattern."""
    prev_o = open_.shift(1); prev_c = close.shift(1)
    prev_green = prev_c > prev_o
    gap_down = open_ < prev_o
    today_red = close < open_
    flag = (prev_green & gap_down & today_red).astype(float)
    return flag.where(prev_c.notna(), np.nan)


def f06_cscr_074_bearish_kicker_at_252d_high(open_, high, low, close):
    """Bearish kicker at 252d high."""
    prev_o = open_.shift(1); prev_c = close.shift(1); prev_h = high.shift(1)
    prev_green = prev_c > prev_o
    gap_down = open_ < prev_o
    today_red = close < open_
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = prev_h >= rmax.shift(1)
    flag = (prev_green & gap_down & today_red & at_peak).astype(float)
    return flag.where(rmax.notna(), np.nan)


def f06_cscr_075_bearish_kicker_severity_atr(open_, high, low, close):
    """Bearish kicker severity (ATR units)."""
    prev_o = open_.shift(1); prev_c = close.shift(1)
    prev_green = prev_c > prev_o
    gap_down = open_ < prev_o
    today_red = close < open_
    qualifies = prev_green & gap_down & today_red
    atr = _atr(high, low, close, n=MDAYS)
    val = _safe_div(prev_o - open_, atr)
    return val.where(qualifies, np.nan)


CANDLESTICK_REVERSAL_CATALOG_BASE_REGISTRY_001_075 = {
    "f06_cscr_001_body_to_range_ratio": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_001_body_to_range_ratio},
    "f06_cscr_002_doji_indicator_at_252d_high": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_002_doji_indicator_at_252d_high},
    "f06_cscr_003_dragonfly_doji_score": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_003_dragonfly_doji_score},
    "f06_cscr_004_gravestone_doji_score": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_004_gravestone_doji_score},
    "f06_cscr_005_long_legged_doji_score": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_005_long_legged_doji_score},
    "f06_cscr_006_four_price_doji_proxy": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_006_four_price_doji_proxy},
    "f06_cscr_007_doji_within_atr_of_252d_high": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_007_doji_within_atr_of_252d_high},
    "f06_cscr_008_doji_count_21d_while_near_252d_high": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_008_doji_count_21d_while_near_252d_high},
    "f06_cscr_009_doji_count_63d_while_near_252d_high": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_009_doji_count_63d_while_near_252d_high},
    "f06_cscr_010_doji_after_strong_advance": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_010_doji_after_strong_advance},
    "f06_cscr_011_body_engulf_bearish_indicator": {"inputs": ["open", "close"], "func": f06_cscr_011_body_engulf_bearish_indicator},
    "f06_cscr_012_range_engulf_bearish_indicator": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_012_range_engulf_bearish_indicator},
    "f06_cscr_013_bearish_engulfing_severity": {"inputs": ["open", "close"], "func": f06_cscr_013_bearish_engulfing_severity},
    "f06_cscr_014_bearish_engulf_at_252d_high": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_014_bearish_engulf_at_252d_high},
    "f06_cscr_015_bearish_engulf_within_atr_of_252d_high": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_015_bearish_engulf_within_atr_of_252d_high},
    "f06_cscr_016_bearish_engulf_volume_confirmed": {"inputs": ["open", "close", "volume"], "func": f06_cscr_016_bearish_engulf_volume_confirmed},
    "f06_cscr_017_bearish_engulf_count_63d": {"inputs": ["open", "close"], "func": f06_cscr_017_bearish_engulf_count_63d},
    "f06_cscr_018_bearish_engulf_count_252d_at_high": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_018_bearish_engulf_count_252d_at_high},
    "f06_cscr_019_bars_since_last_bearish_engulf_at_high": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_019_bars_since_last_bearish_engulf_at_high},
    "f06_cscr_020_atr_normalized_engulf_body_ratio": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_020_atr_normalized_engulf_body_ratio},
    "f06_cscr_021_hanging_man_at_252d_high": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_021_hanging_man_at_252d_high},
    "f06_cscr_022_hanging_man_lower_shadow_to_body_ratio": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_022_hanging_man_lower_shadow_to_body_ratio},
    "f06_cscr_023_hanging_man_volume_confirmed": {"inputs": ["open", "high", "low", "close", "volume"], "func": f06_cscr_023_hanging_man_volume_confirmed},
    "f06_cscr_024_hammer_after_decline_no_followthrough": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_024_hammer_after_decline_no_followthrough},
    "f06_cscr_025_hanging_man_count_21d_at_high": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_025_hanging_man_count_21d_at_high},
    "f06_cscr_026_hanging_man_count_63d_at_high": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_026_hanging_man_count_63d_at_high},
    "f06_cscr_027_hanging_man_followthrough_indicator": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_027_hanging_man_followthrough_indicator},
    "f06_cscr_028_hanging_man_atr_norm_lower_shadow": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_028_hanging_man_atr_norm_lower_shadow},
    "f06_cscr_029_shooting_star_at_252d_high": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_029_shooting_star_at_252d_high},
    "f06_cscr_030_shooting_star_upper_shadow_to_body_ratio": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_030_shooting_star_upper_shadow_to_body_ratio},
    "f06_cscr_031_shooting_star_within_atr_of_252d_high": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_031_shooting_star_within_atr_of_252d_high},
    "f06_cscr_032_inverted_hammer_failure": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_032_inverted_hammer_failure},
    "f06_cscr_033_shooting_star_count_21d_at_high": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_033_shooting_star_count_21d_at_high},
    "f06_cscr_034_shooting_star_count_63d_at_high": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_034_shooting_star_count_63d_at_high},
    "f06_cscr_035_shooting_star_atr_norm_upper_shadow": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_035_shooting_star_atr_norm_upper_shadow},
    "f06_cscr_036_shooting_star_volume_confirmed": {"inputs": ["open", "high", "low", "close", "volume"], "func": f06_cscr_036_shooting_star_volume_confirmed},
    "f06_cscr_037_tweezer_top_indicator": {"inputs": ["high", "close", "open"], "func": f06_cscr_037_tweezer_top_indicator},
    "f06_cscr_038_tweezer_top_at_252d_high": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_038_tweezer_top_at_252d_high},
    "f06_cscr_039_tweezer_top_count_63d": {"inputs": ["open", "high", "close"], "func": f06_cscr_039_tweezer_top_count_63d},
    "f06_cscr_040_max_consecutive_near_eq_highs_21d": {"inputs": ["high"], "func": f06_cscr_040_max_consecutive_near_eq_highs_21d},
    "f06_cscr_041_tweezer_top_atr_norm_high_match_tightness": {"inputs": ["high", "low", "close"], "func": f06_cscr_041_tweezer_top_atr_norm_high_match_tightness},
    "f06_cscr_042_three_bar_tweezer_top_indicator": {"inputs": ["high", "open", "close"], "func": f06_cscr_042_three_bar_tweezer_top_indicator},
    "f06_cscr_043_dark_cloud_cover_indicator": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_043_dark_cloud_cover_indicator},
    "f06_cscr_044_dark_cloud_penetration_depth": {"inputs": ["open", "close"], "func": f06_cscr_044_dark_cloud_penetration_depth},
    "f06_cscr_045_dark_cloud_at_252d_high": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_045_dark_cloud_at_252d_high},
    "f06_cscr_046_dark_cloud_count_252d": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_046_dark_cloud_count_252d},
    "f06_cscr_047_dark_cloud_volume_confirmed": {"inputs": ["open", "high", "low", "close", "volume"], "func": f06_cscr_047_dark_cloud_volume_confirmed},
    "f06_cscr_048_dark_cloud_followthrough_5d": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_048_dark_cloud_followthrough_5d},
    "f06_cscr_049_bearish_harami_indicator": {"inputs": ["open", "close"], "func": f06_cscr_049_bearish_harami_indicator},
    "f06_cscr_050_bearish_harami_at_252d_high": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_050_bearish_harami_at_252d_high},
    "f06_cscr_051_bearish_harami_body_compression_ratio": {"inputs": ["open", "close"], "func": f06_cscr_051_bearish_harami_body_compression_ratio},
    "f06_cscr_052_harami_cross_at_high": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_052_harami_cross_at_high},
    "f06_cscr_053_bearish_harami_count_252d": {"inputs": ["open", "close"], "func": f06_cscr_053_bearish_harami_count_252d},
    "f06_cscr_054_bearish_harami_volume_confirmed": {"inputs": ["open", "close", "volume"], "func": f06_cscr_054_bearish_harami_volume_confirmed},
    "f06_cscr_055_evening_star_indicator": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_055_evening_star_indicator},
    "f06_cscr_056_evening_star_at_252d_high": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_056_evening_star_at_252d_high},
    "f06_cscr_057_evening_doji_star_indicator": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_057_evening_doji_star_indicator},
    "f06_cscr_058_three_black_crows_indicator": {"inputs": ["open", "close"], "func": f06_cscr_058_three_black_crows_indicator},
    "f06_cscr_059_three_inside_down_indicator": {"inputs": ["open", "close"], "func": f06_cscr_059_three_inside_down_indicator},
    "f06_cscr_060_three_line_strike_bearish": {"inputs": ["open", "close"], "func": f06_cscr_060_three_line_strike_bearish},
    "f06_cscr_061_abandoned_baby_top_indicator": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_061_abandoned_baby_top_indicator},
    "f06_cscr_062_three_black_crows_count_252d": {"inputs": ["open", "close"], "func": f06_cscr_062_three_black_crows_count_252d},
    "f06_cscr_063_evening_star_count_252d_at_high": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_063_evening_star_count_252d_at_high},
    "f06_cscr_064_spinning_top_indicator": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_064_spinning_top_indicator},
    "f06_cscr_065_high_wave_candle_indicator": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_065_high_wave_candle_indicator},
    "f06_cscr_066_spinning_top_count_21d_at_high": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_066_spinning_top_count_21d_at_high},
    "f06_cscr_067_high_wave_count_63d_at_high": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_067_high_wave_count_63d_at_high},
    "f06_cscr_068_star_shape_score": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_068_star_shape_score},
    "f06_cscr_069_bearish_marubozu_indicator": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_069_bearish_marubozu_indicator},
    "f06_cscr_070_bearish_marubozu_at_252d_high": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_070_bearish_marubozu_at_252d_high},
    "f06_cscr_071_marubozu_failure_within_5d": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_071_marubozu_failure_within_5d},
    "f06_cscr_072_bullish_marubozu_then_doji_indicator": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_072_bullish_marubozu_then_doji_indicator},
    "f06_cscr_073_bearish_kicker_pattern": {"inputs": ["open", "close"], "func": f06_cscr_073_bearish_kicker_pattern},
    "f06_cscr_074_bearish_kicker_at_252d_high": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_074_bearish_kicker_at_252d_high},
    "f06_cscr_075_bearish_kicker_severity_atr": {"inputs": ["open", "high", "low", "close"], "func": f06_cscr_075_bearish_kicker_severity_atr},
}
