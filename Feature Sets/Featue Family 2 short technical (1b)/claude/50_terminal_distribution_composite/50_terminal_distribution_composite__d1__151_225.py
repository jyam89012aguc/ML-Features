"""terminal_distribution_composite d1 features 151-225 — Pipeline 1b-technical.

Extends 001-150 with 75 distinct hypotheses across:
K: Wyckoff distribution-phase patterns (upthrust, no-demand, climactic action, etc).
L: Bearish candle patterns at top (shooting-star, gravestone-doji, bear-engulf, etc).
M: Multi-bar pattern detectors (double-top, bear-flag, rising-wedge, cup-with-handle-fail).
N: Volume profile / structural distribution (vol-at-high concentration, decline-rate).
O: Late-stage / cycle-end signatures (weeks-since-breakout, post-peak MA decay).

Inputs: SEP OHLCV. PIT-clean (right-anchored rolling, no centered, no shift(-N)).
Self-contained helpers — no cross-family imports.
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


def _sma(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).mean()


def _bars_since_true(mask: pd.Series) -> pd.Series:
    arr = mask.astype(bool).to_numpy()
    out = np.full(arr.shape, np.nan)
    last = -1
    for i in range(arr.size):
        if arr[i]:
            last = i
            out[i] = 0.0
        elif last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=mask.index)


def _streak_true(mask: pd.Series) -> pd.Series:
    arr = mask.astype(bool).to_numpy()
    out = np.zeros(arr.shape, dtype=float)
    c = 0
    for i in range(arr.size):
        c = c + 1 if arr[i] else 0
        out[i] = float(c)
    return pd.Series(out, index=mask.index)


# ============================================================
# Bucket K — Wyckoff distribution-phase patterns (151-165)
# ============================================================


def f50_tdco_151_upthrust_pattern_indicator_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Wyckoff upthrust: new 21d-high made AND close < open AND close in lower half of bar."""
    prior_h = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    mid = (high + low) / 2.0
    ev = (high > prior_h) & (close < open) & (close < mid)
    return (ev.astype(float).where(prior_h.notna(), np.nan)).diff()


def f50_tdco_152_upthrust_after_distribution_count_63_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of upthrusts in past 63 that occurred AFTER a 25-bar distribution-day cluster (>=3 dist days in 25)."""
    prior_h = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    mid = (high + low) / 2.0
    upthrust = (high > prior_h) & (close < open) & (close < mid)
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd = ((ret < -0.002) & (volume > vavg)).astype(float).rolling(25, min_periods=10).sum()
    has_cluster = (dd >= 3.0)
    ev = (upthrust & has_cluster).astype(float)
    return (ev.rolling(QDAYS, min_periods=MDAYS).sum().where(prior_h.notna() & vavg.notna(), np.nan)).diff()


def f50_tdco_153_secondary_test_failure_indicator_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Price tests prior 21d high (within 1%) on declining volume AND fails to exceed it — secondary-test failure."""
    prior_h = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    near_test = (high >= 0.99 * prior_h) & (high < prior_h)
    low_vol = (volume < vavg)
    return ((near_test & low_vol).astype(float).where(prior_h.notna() & vavg.notna(), np.nan)).diff()


def f50_tdco_154_stopping_volume_indicator_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Climactic vol on down day: vol > 2x prior 50d avg AND close in lower-quartile of bar range."""
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    rng = (high - low).replace(0, np.nan)
    pos = _safe_div(close - low, rng)
    ev = (volume > 2.0 * vavg) & (close < close.shift(1)) & (pos < 0.25)
    return (ev.astype(float).where(vavg.notna(), np.nan)).diff()


def f50_tdco_155_climactic_action_indicator_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Wide-range high-vol bar AT 252d high: range > 2*ATR21 AND vol > 2x avg AND high == 252d max."""
    atr = _atr(high, low, close, MDAYS)
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    rng = high - low
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    ev = (rng > 2.0 * atr) & (volume > 2.0 * vavg) & (high >= rmax)
    return (ev.astype(float).where(atr.notna() & vavg.notna() & rmax.notna(), np.nan)).diff()


def f50_tdco_156_effort_vs_result_divergence_63_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """High vol bars produce small returns: 63d corr( |return|, volume ) — low/negative = effort-vs-result divergence."""
    r = close.pct_change().abs()
    return (r.rolling(QDAYS, min_periods=MDAYS).corr(volume)).diff()


def f50_tdco_157_no_demand_day_indicator_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Wyckoff no-demand: small range up day on declining volume — close > prior close AND range < ATR/2 AND vol < avg."""
    atr = _atr(high, low, close, MDAYS)
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    rng = high - low
    ev = (close > close.shift(1)) & (rng < 0.5 * atr) & (volume < vavg)
    return (ev.astype(float).where(atr.notna() & vavg.notna(), np.nan)).diff()


def f50_tdco_158_no_supply_day_indicator_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Wyckoff no-supply: small range down day on declining volume — close < prior close AND range < ATR/2 AND vol < avg
    (context/contrast: bullish signal, used as inverse-context feature)."""
    atr = _atr(high, low, close, MDAYS)
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    rng = high - low
    ev = (close < close.shift(1)) & (rng < 0.5 * atr) & (volume < vavg)
    return (ev.astype(float).where(atr.notna() & vavg.notna(), np.nan)).diff()


def f50_tdco_159_distribution_phase_indicator_simplified_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if rolling top-dwell (21d-fraction near 252d-max) > 30% AND >= 3 distribution days in past 25."""
    top = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = (high >= 0.99 * top).astype(float).rolling(MDAYS, min_periods=WDAYS).mean()
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd = ((ret < -0.002) & (volume > vavg)).astype(float).rolling(25, min_periods=10).sum()
    ev = (near > 0.30) & (dd >= 3.0)
    return (ev.astype(float).where(top.notna() & vavg.notna(), np.nan)).diff()


def f50_tdco_160_markdown_phase_acceleration_63_d1(close: pd.Series) -> pd.Series:
    """63d slope of negative-only returns: more negative slope = markdown acceleration.
    Uses cumulative sum of min(ret,0)."""
    r = close.pct_change()
    neg_cum = r.clip(upper=0).rolling(QDAYS, min_periods=MDAYS).sum()
    return (_rolling_slope(neg_cum, QDAYS)).diff()


def f50_tdco_161_re_distribution_count_252_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of distinct distribution-day cluster onsets in past 252 (cluster = 25d dist-day count crossing >=3 from below)."""
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd = ((ret < -0.002) & (volume > vavg)).astype(float).rolling(25, min_periods=10).sum()
    onset = (dd.shift(1) < 3.0) & (dd >= 3.0)
    return (onset.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(vavg.notna(), np.nan)).diff()


def f50_tdco_162_false_breakout_above_top_count_252_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Count of past 252 where high > prior-252d-max but close <= prior-252d-max (false breakout)."""
    prior_top = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    ev = (high > prior_top) & (close <= prior_top)
    return (ev.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(prior_top.notna(), np.nan)).diff()


def f50_tdco_163_failed_test_of_recent_high_indicator_d1(high: pd.Series) -> pd.Series:
    """1 if today's high within 1% of prior 21d max AND today's high < prior 21d max — failed retest."""
    prior_h21 = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    ev = (high >= 0.99 * prior_h21) & (high < prior_h21)
    return (ev.astype(float).where(prior_h21.notna(), np.nan)).diff()


def f50_tdco_164_wide_range_red_at_resistance_count_63_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of past 63 bars with (range > 2*ATR21) AND (close < open-proxy: close < prior close) AND at 252d-high (>=95%)."""
    atr = _atr(high, low, close, MDAYS)
    rng = high - low
    top = high.rolling(YDAYS, min_periods=QDAYS).max()
    near_top = (high >= 0.95 * top)
    ev = (rng > 2.0 * atr) & (close < close.shift(1)) & near_top
    return (ev.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(atr.notna() & top.notna(), np.nan)).diff()


def f50_tdco_165_shake_out_pattern_indicator_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Brief drop below recent 21d-low (today's low < prior 21d low) followed by quick recovery (close > prior 21d low).
    Implemented PIT-cleanly: today's low < prior-21d-low AND close >= prior-21d-low."""
    prior_ll = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    ev = (low < prior_ll) & (close >= prior_ll)
    return (ev.astype(float).where(prior_ll.notna(), np.nan)).diff()


def f50_tdco_166_shooting_star_at_top_indicator_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Shooting star: long upper shadow (>=2x body), small body near low half, near 252d high."""
    body = (close - open).abs()
    upper = high - pd.concat([close, open], axis=1).max(axis=1)
    lower = pd.concat([close, open], axis=1).min(axis=1) - low
    rng = (high - low).replace(0, np.nan)
    near_low = (pd.concat([close, open], axis=1).min(axis=1) - low) <= 0.3 * rng
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_top = (high >= 0.95 * rmax)
    ev = (upper >= 2.0 * body) & (body <= 0.3 * rng) & near_low & (lower < 0.2 * rng) & at_top
    return (ev.astype(float).where(rmax.notna(), np.nan)).diff()


def f50_tdco_167_shooting_star_at_top_count_63_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of shooting-star-at-top events in past 63 bars."""
    body = (close - open).abs()
    upper = high - pd.concat([close, open], axis=1).max(axis=1)
    lower = pd.concat([close, open], axis=1).min(axis=1) - low
    rng = (high - low).replace(0, np.nan)
    near_low = (pd.concat([close, open], axis=1).min(axis=1) - low) <= 0.3 * rng
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_top = (high >= 0.95 * rmax)
    ev = ((upper >= 2.0 * body) & (body <= 0.3 * rng) & near_low & (lower < 0.2 * rng) & at_top).astype(float)
    return (ev.rolling(QDAYS, min_periods=MDAYS).sum().where(rmax.notna(), np.nan)).diff()


def f50_tdco_168_gravestone_doji_at_top_indicator_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Gravestone doji: open ~= close ~= low AND long upper shadow, at 252d high (>=95%)."""
    rng = (high - low).replace(0, np.nan)
    body = (close - open).abs()
    is_doji = body <= 0.10 * rng
    near_low = (pd.concat([close, open], axis=1).min(axis=1) - low) <= 0.10 * rng
    upper = high - pd.concat([close, open], axis=1).max(axis=1)
    long_up = upper >= 0.6 * rng
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_top = (high >= 0.95 * rmax)
    ev = is_doji & near_low & long_up & at_top
    return (ev.astype(float).where(rmax.notna(), np.nan)).diff()


def f50_tdco_169_hanging_man_indicator_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Hanging man: small body near top of bar, long lower shadow (>=2x body), after recent uptrend (21d return > 0)."""
    body = (close - open).abs()
    rng = (high - low).replace(0, np.nan)
    upper = high - pd.concat([close, open], axis=1).max(axis=1)
    lower = pd.concat([close, open], axis=1).min(axis=1) - low
    near_top = (high - pd.concat([close, open], axis=1).max(axis=1)) <= 0.15 * rng
    uptrend = close.shift(1).pct_change(MDAYS) > 0
    ev = (lower >= 2.0 * body) & (body <= 0.30 * rng) & near_top & (upper < 0.15 * rng) & uptrend
    return (ev.astype(float).where(uptrend.notna(), np.nan)).diff()


def f50_tdco_170_dark_cloud_cover_pattern_indicator_d1(open: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    """Dark cloud cover: yesterday bullish (close > open); today opens > yesterday high; today close < midpoint of yesterday body."""
    prev_bull = close.shift(1) > open.shift(1)
    today_open_above_prev_h = open > high.shift(1)
    prev_mid = (close.shift(1) + open.shift(1)) / 2.0
    today_below_mid = close < prev_mid
    ev = prev_bull & today_open_above_prev_h & today_below_mid & (close < open)
    return (ev.astype(float).where(prev_mid.notna(), np.nan)).diff()


def f50_tdco_171_bearish_engulfing_at_top_indicator_d1(open: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish engulfing at top: yesterday bullish; today bearish AND today open > yesterday close AND today close < yesterday open;
    at 252d high (>=95%)."""
    prev_bull = close.shift(1) > open.shift(1)
    today_bear = close < open
    engulf = (open > close.shift(1)) & (close < open.shift(1))
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_top = (high >= 0.95 * rmax)
    ev = prev_bull & today_bear & engulf & at_top
    return (ev.astype(float).where(rmax.notna(), np.nan)).diff()


def f50_tdco_172_evening_star_pattern_indicator_d1(open: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    """Evening star (3-bar): bar -2 bullish; bar -1 small-body (star); bar 0 bearish closing below bar -2 midpoint."""
    body2 = (close.shift(2) - open.shift(2)).abs()
    bull_2 = close.shift(2) > open.shift(2)
    rng2 = (high.shift(2) - close.shift(2).combine(open.shift(2), np.minimum)).replace(0, np.nan)
    body1 = (close.shift(1) - open.shift(1)).abs()
    small_star = body1 < 0.3 * body2
    bear_0 = close < open
    mid2 = (close.shift(2) + open.shift(2)) / 2.0
    closes_below = close < mid2
    ev = bull_2 & small_star & bear_0 & closes_below
    return (ev.astype(float).where(body2.notna(), np.nan)).diff()


def f50_tdco_173_three_black_crows_pattern_indicator_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Three black crows: 3 consecutive bars where close<open, each opens within prior body and closes lower than prior close."""
    bear = close < open
    bear2 = bear & bear.shift(1) & bear.shift(2)
    open_inside_1 = (open <= open.shift(1)) & (open >= close.shift(1))
    open_inside_2 = (open.shift(1) <= open.shift(2)) & (open.shift(1) >= close.shift(2))
    lower_close_1 = close < close.shift(1)
    lower_close_2 = close.shift(1) < close.shift(2)
    ev = bear2 & open_inside_1 & open_inside_2 & lower_close_1 & lower_close_2
    return (ev.astype(float).where(open.shift(2).notna(), np.nan)).diff()


def f50_tdco_174_dragonfly_doji_at_top_indicator_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Dragonfly doji: open ~= close ~= high AND long lower shadow, at 252d high (>=95%).
    Bearish at top because suggests failed rally extension."""
    rng = (high - low).replace(0, np.nan)
    body = (close - open).abs()
    is_doji = body <= 0.10 * rng
    near_high = (high - pd.concat([close, open], axis=1).max(axis=1)) <= 0.10 * rng
    lower = pd.concat([close, open], axis=1).min(axis=1) - low
    long_low = lower >= 0.6 * rng
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_top = (high >= 0.95 * rmax)
    ev = is_doji & near_high & long_low & at_top
    return (ev.astype(float).where(rmax.notna(), np.nan)).diff()


def f50_tdco_175_tweezers_top_indicator_d1(high: pd.Series) -> pd.Series:
    """Tweezers top: two consecutive bars with highs within 0.2% of each other AND at 252d high (>=95%)."""
    same_h = (high - high.shift(1)).abs() <= 0.002 * high
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_top = (high >= 0.95 * rmax)
    ev = same_h & at_top
    return (ev.astype(float).where(rmax.notna(), np.nan)).diff()


def f50_tdco_176_harami_at_top_indicator_d1(open: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish harami: yesterday bullish large-body; today small bearish body fully contained in yesterday body; at 252d high."""
    prev_bull = close.shift(1) > open.shift(1)
    prev_body = (close.shift(1) - open.shift(1)).abs()
    today_body = (close - open).abs()
    inside_body = (open.combine(close, np.maximum) <= close.shift(1)) & (open.combine(close, np.minimum) >= open.shift(1))
    today_small = today_body < 0.5 * prev_body
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_top = (high >= 0.95 * rmax)
    ev = prev_bull & (close < open) & inside_body & today_small & at_top
    return (ev.astype(float).where(rmax.notna(), np.nan)).diff()


def f50_tdco_177_doji_at_252_high_indicator_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Doji (body <= 10% of range) AND narrow range (range <= 1.5 * ATR21) AND high = 252d max."""
    rng = (high - low).replace(0, np.nan)
    body = (close - open).abs()
    is_doji = body <= 0.10 * rng
    atr = _atr(high, low, close, MDAYS)
    narrow = rng <= 1.5 * atr
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_top = (high >= rmax)
    ev = is_doji & narrow & at_top
    return (ev.astype(float).where(rmax.notna() & atr.notna(), np.nan)).diff()


def f50_tdco_178_long_upper_shadow_pct_in_range_63_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars with upper-shadow > 50% of range — top-shadow saturation."""
    rng = (high - low).replace(0, np.nan)
    upper = high - pd.concat([close, open], axis=1).max(axis=1)
    ev = (_safe_div(upper, rng) > 0.5).astype(float)
    return (ev.rolling(QDAYS, min_periods=MDAYS).mean().where(rng.notna(), np.nan)).diff()


def f50_tdco_179_long_upper_shadow_at_top_count_63_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of past 63 bars with upper-shadow > 50% of range AND price near 252d high (>=95%)."""
    rng = (high - low).replace(0, np.nan)
    upper = high - pd.concat([close, open], axis=1).max(axis=1)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near_top = (high >= 0.95 * rmax)
    ev = ((_safe_div(upper, rng) > 0.5) & near_top).astype(float)
    return (ev.rolling(QDAYS, min_periods=MDAYS).sum().where(rng.notna() & rmax.notna(), np.nan)).diff()


def f50_tdco_180_bearish_candle_cluster_score_21_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of distinct bearish-pattern events in past 21 bars: shooting-star, gravestone-doji, bear-engulf,
    dark-cloud, hanging-man — composite cluster intensity."""
    rng = (high - low).replace(0, np.nan)
    body = (close - open).abs()
    upper = high - pd.concat([close, open], axis=1).max(axis=1)
    lower = pd.concat([close, open], axis=1).min(axis=1) - low
    # shooting star
    ss = (upper >= 2.0 * body) & (body <= 0.30 * rng) & (lower < 0.2 * rng)
    # gravestone doji
    gd = (body <= 0.10 * rng) & (lower <= 0.10 * rng) & (upper >= 0.6 * rng)
    # bear engulf
    be = (close < open) & (close.shift(1) > open.shift(1)) & (open > close.shift(1)) & (close < open.shift(1))
    # dark cloud
    dc = (close.shift(1) > open.shift(1)) & (open > high.shift(1)) & (close < (close.shift(1) + open.shift(1)) / 2.0) & (close < open)
    # hanging man
    hm = (lower >= 2.0 * body) & (body <= 0.30 * rng) & (upper < 0.15 * rng) & (close.shift(1).pct_change(MDAYS) > 0)
    tot = (ss.astype(float).fillna(0) + gd.astype(float).fillna(0) + be.astype(float).fillna(0)
           + dc.astype(float).fillna(0) + hm.astype(float).fillna(0))
    return (tot.rolling(MDAYS, min_periods=WDAYS).sum().where(rng.notna(), np.nan)).diff()


def f50_tdco_181_double_top_pattern_indicator_63_d1(high: pd.Series) -> pd.Series:
    """Two distinct peaks within 1% of each other in past 63 — double-top.
    Simplified: max(high in [0..31]) and max(high in [32..63]) within 1% of each other, both at >= 90% of 252d-max."""
    h_recent = high.rolling(32, min_periods=10).max()
    h_prior = high.shift(32).rolling(32, min_periods=10).max()
    ratio = _safe_div(pd.concat([h_recent, h_prior], axis=1).min(axis=1), pd.concat([h_recent, h_prior], axis=1).max(axis=1))
    close_in_pct = ratio >= 0.99
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near_top = (pd.concat([h_recent, h_prior], axis=1).max(axis=1) >= 0.90 * rmax)
    ev = close_in_pct & near_top
    return (ev.astype(float).where(rmax.notna() & h_prior.notna(), np.nan)).diff()


def f50_tdco_182_triple_top_pattern_indicator_63_d1(high: pd.Series) -> pd.Series:
    """Three peaks within 1.5% of each other in past 63 — triple-top.
    Simplified: max in each of three 21d sub-windows mutually within 1.5%."""
    h1 = high.shift(42).rolling(MDAYS, min_periods=WDAYS).max()
    h2 = high.shift(21).rolling(MDAYS, min_periods=WDAYS).max()
    h3 = high.rolling(MDAYS, min_periods=WDAYS).max()
    stack = pd.concat([h1.rename(0), h2.rename(1), h3.rename(2)], axis=1)
    ratio = _safe_div(stack.min(axis=1), stack.max(axis=1))
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near_top = (stack.max(axis=1) >= 0.90 * rmax)
    ev = (ratio >= 0.985) & near_top
    return (ev.astype(float).where(rmax.notna() & h1.notna(), np.nan)).diff()


def f50_tdco_183_bear_flag_pattern_indicator_21_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bear flag: sharp decline in window [-21:-11] (return < -8%) followed by tight upward consolidation in [-10:0]
    (range/atr small, mild positive slope)."""
    r_decl = close.shift(11).pct_change(11)
    sl_recent = _rolling_slope(close.tail(0).combine_first(close).rolling(11, min_periods=5).mean(), 11)
    # use simpler: 11d slope on close
    sl11 = _rolling_slope(close, 11)
    rng10 = (high.rolling(11, min_periods=5).max() - low.rolling(11, min_periods=5).min())
    atr = _atr(high, low, close, MDAYS)
    tight = rng10 < 1.2 * atr
    ev = (r_decl < -0.08) & (sl11 >= 0) & tight
    return (ev.astype(float).where(atr.notna() & r_decl.notna(), np.nan)).diff()


def f50_tdco_184_bear_pennant_pattern_indicator_21_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bear pennant: sharp prior decline AND recent 10d range narrower than 21d range × 0.6 (converging trendlines).
    Distinct from flag in convergence."""
    r_decl = close.shift(11).pct_change(11)
    rng10 = (high.rolling(11, min_periods=5).max() - low.rolling(11, min_periods=5).min())
    rng21 = (high.rolling(MDAYS, min_periods=WDAYS).max() - low.rolling(MDAYS, min_periods=WDAYS).min())
    converging = rng10 < 0.6 * rng21
    ev = (r_decl < -0.08) & converging
    return (ev.astype(float).where(rng21.notna() & r_decl.notna(), np.nan)).diff()


def f50_tdco_185_rising_wedge_pattern_indicator_63_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Rising wedge: both highs slope up AND lows slope up, but lows-slope > highs-slope (converging upward).
    Bearish topping pattern."""
    sl_h = _rolling_slope(high, QDAYS)
    sl_l = _rolling_slope(low, QDAYS)
    ev = (sl_h > 0) & (sl_l > 0) & (sl_l > sl_h)
    return (ev.astype(float).where(sl_h.notna() & sl_l.notna(), np.nan)).diff()


def f50_tdco_186_descending_triangle_pattern_indicator_63_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Descending triangle: flat support (63d-low slope ~ 0) AND descending highs (63d-high slope < 0)."""
    sl_h = _rolling_slope(high, QDAYS)
    sl_l = _rolling_slope(low, QDAYS)
    # "flat" = |sl_l| small relative to recent low's range
    sl_l_abs = sl_l.abs()
    low_mag = (low.rolling(QDAYS, min_periods=MDAYS).std()).replace(0, np.nan)
    flat = _safe_div(sl_l_abs * float(QDAYS), low_mag) < 1.0
    ev = (sl_h < 0) & flat
    return (ev.astype(float).where(sl_h.notna() & sl_l.notna(), np.nan)).diff()


def f50_tdco_187_bump_run_reversal_proxy_63_d1(close: pd.Series) -> pd.Series:
    """Bump-and-run: gradual ascent in [-63:-21] then sharp acceleration in [-21:0] then break.
    Proxy: 42d return [-63:-21] < 10% AND 21d return [-21:0] > 20% AND today close < SMA10."""
    r_gradual = close.shift(21).pct_change(42)
    r_sharp = close.pct_change(21)
    s10 = _sma(close, 10)
    brk = close < s10
    ev = (r_gradual.abs() < 0.10) & (r_sharp > 0.20) & brk
    return (ev.astype(float).where(r_gradual.notna() & s10.notna(), np.nan)).diff()


def f50_tdco_188_cup_with_handle_failure_proxy_63_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Cup-with-handle failure proxy: U-shape completes (close back near 63d high) then breakdown (close < 21d-low within next bars).
    Simplified: high == 63d-max within last 10 bars AND today close < prior 21d-low."""
    h63 = high.rolling(QDAYS, min_periods=MDAYS).max()
    recent_at_top = (high.rolling(10, min_periods=3).max() >= 0.99 * h63)
    prior_ll21 = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    break_now = close < prior_ll21
    ev = recent_at_top & break_now
    return (ev.astype(float).where(h63.notna() & prior_ll21.notna(), np.nan)).diff()


def f50_tdco_189_dead_cat_bounce_indicator_d1(close: pd.Series) -> pd.Series:
    """Dead cat bounce: sharp 21d drop (>-15%), brief 5d bounce (>+5%), then 5d drop (<-3%).
    PIT-clean: window measured as close.shift(10).pct_change(21) < -0.15, close.shift(5).pct_change(5) > 0.05, close.pct_change(5) < -0.03."""
    decl_21 = close.shift(10).pct_change(21) < -0.15
    bounce_5 = close.shift(5).pct_change(5) > 0.05
    drop_5 = close.pct_change(5) < -0.03
    ev = decl_21 & bounce_5 & drop_5
    return (ev.astype(float).where(close.shift(36).notna(), np.nan)).diff()


def f50_tdco_190_three_drives_pattern_indicator_63_d1(high: pd.Series) -> pd.Series:
    """Three drives: three successive higher highs (5d-max) each with smaller incremental gain.
    Proxy: three 21d-spaced peaks: h(t) > h(t-21) > h(t-42) AND (h(t) - h(t-21)) < (h(t-21) - h(t-42))."""
    h_now = high.rolling(WDAYS, min_periods=2).max()
    h1 = h_now.shift(21)
    h2 = h_now.shift(42)
    ascending = (h_now > h1) & (h1 > h2)
    decel = (h_now - h1) < (h1 - h2)
    ev = ascending & decel
    return (ev.astype(float).where(h2.notna(), np.nan)).diff()


def f50_tdco_191_gartley_failure_proxy_63_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Gartley XABCD failure proxy: pattern completes near 0.786 retrace of XA, then reverses.
    Simplified: 63d-high made, 21d retrace ~ 30-50%, then close breaks 21d low."""
    h63 = high.rolling(QDAYS, min_periods=MDAYS).max()
    l63 = low.rolling(QDAYS, min_periods=MDAYS).min()
    xa = h63 - l63
    retrace = _safe_div(h63 - close, xa)
    in_zone = (retrace >= 0.30) & (retrace <= 0.50)
    prior_ll = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    brk = close < prior_ll
    ev = in_zone & brk
    return (ev.astype(float).where(xa.notna() & prior_ll.notna(), np.nan)).diff()


def f50_tdco_192_marubozu_red_at_top_indicator_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Marubozu red: long red bar with no shadows (body == range, close < open), at 252d high (>=95%)."""
    rng = (high - low).replace(0, np.nan)
    body = (close - open).abs()
    no_shadow = body >= 0.95 * rng
    red = close < open
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_top = (high >= 0.95 * rmax)
    ev = no_shadow & red & at_top
    return (ev.astype(float).where(rmax.notna(), np.nan)).diff()


def f50_tdco_193_spinning_top_at_252_high_indicator_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Spinning top: small body, long shadows on both sides, at 252d high."""
    rng = (high - low).replace(0, np.nan)
    body = (close - open).abs()
    small_body = body <= 0.25 * rng
    upper = high - pd.concat([close, open], axis=1).max(axis=1)
    lower = pd.concat([close, open], axis=1).min(axis=1) - low
    both_shadows = (upper >= 0.25 * rng) & (lower >= 0.25 * rng)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_top = (high >= 0.95 * rmax)
    ev = small_body & both_shadows & at_top
    return (ev.astype(float).where(rmax.notna(), np.nan)).diff()


def f50_tdco_194_counter_trend_thrust_failed_count_63_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of past 63 bars where an upthrust (new 21d-high, close<open, close in lower half) was immediately followed (next bar)
    by lower close — failed-thrust count. PIT-clean: today is the "next bar", look at yesterday's upthrust."""
    prior_h = high.shift(2).rolling(MDAYS, min_periods=WDAYS).max()
    mid_y = (high.shift(1) + low.shift(1)) / 2.0
    upthrust_y = (high.shift(1) > prior_h) & (close.shift(1) < open.shift(1)) & (close.shift(1) < mid_y)
    today_lower = close < close.shift(1)
    ev = (upthrust_y & today_lower).astype(float)
    return (ev.rolling(QDAYS, min_periods=MDAYS).sum().where(prior_h.notna(), np.nan)).diff()


def f50_tdco_195_failed_swing_low_violation_indicator_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Recent swing-low (prior 21d-low at t-10) was broken (close < low) AND recovered (close > low) AND broken again — proxy:
    today close < prior 21d-low AND past 10 bars contain >= 2 break-events."""
    prior_ll = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    brk = (close < prior_ll).astype(float)
    n_breaks_10 = brk.rolling(10, min_periods=3).sum()
    ev = (close < prior_ll) & (n_breaks_10 >= 2)
    return (ev.astype(float).where(prior_ll.notna(), np.nan)).diff()


def f50_tdco_196_volume_at_high_concentration_index_63_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of total 63d volume that occurred when close was in top 10% of 63d price range."""
    hh = high.rolling(QDAYS, min_periods=MDAYS).max()
    ll = low.rolling(QDAYS, min_periods=MDAYS).min()
    pos = _safe_div(close - ll, hh - ll)
    in_top = pos > 0.9
    v_top = volume.where(in_top, 0).rolling(QDAYS, min_periods=MDAYS).sum()
    v_tot = volume.rolling(QDAYS, min_periods=MDAYS).sum()
    return (_safe_div(v_top, v_tot)).diff()


def f50_tdco_197_volume_skew_post_peak_63_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63d skew of volume conditioned on bars within 63 bars after most-recent 252d-high.
    Else NaN. Captures uneven post-peak volume distribution."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs = _bars_since_true(high == rmax)
    post = (bs > 0) & (bs <= QDAYS)
    return (volume.where(post, np.nan).rolling(QDAYS, min_periods=MDAYS).skew()).diff()


def f50_tdco_198_volume_max_recently_vs_avg_63_d1(volume: pd.Series) -> pd.Series:
    """max(volume, 5) / avg(volume, 63) — recent peak vol relative to quarterly average."""
    return (_safe_div(volume.rolling(WDAYS, min_periods=2).max(),

                     volume.rolling(QDAYS, min_periods=MDAYS).mean())).diff()


def f50_tdco_199_down_volume_dominance_at_top_63_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Down-volume fraction (down_vol / total_vol) over past 63 bars, conditioned on close in 252h-zone (>=95%).
    Else NaN."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    in_zone = (close >= 0.95 * rmax)
    diff = close.diff()
    dv = volume.where(diff < 0, 0)
    out = _safe_div(dv.rolling(QDAYS, min_periods=MDAYS).sum(), volume.rolling(QDAYS, min_periods=MDAYS).sum())
    return (out.where(in_zone, np.nan)).diff()


def f50_tdco_200_largest_down_day_vol_in_post_peak_63_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max volume on a down-close day in past 63 conditioned on being post-peak (within 252 bars of 252d max)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs = _bars_since_true(high == rmax)
    post = (bs > 0) & (bs <= YDAYS)
    diff = close.diff()
    down_vol = volume.where(diff < 0, 0)
    return (down_vol.where(post, np.nan).rolling(QDAYS, min_periods=MDAYS).max()).diff()


def f50_tdco_201_volume_decline_rate_post_peak_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """63d rolling slope of volume conditioned on bars post-peak (within 252 of 252d max). Else NaN.
    Negative = decaying volume after peak (stale)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs = _bars_since_true(high == rmax)
    post = (bs > 0) & (bs <= YDAYS)
    return (_rolling_slope(volume, QDAYS).where(post, np.nan)).diff()


def f50_tdco_202_low_volume_bounce_count_63_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of past 63 bars with 5d return > 5% on volume < 0.8x prior 50d avg — weak rally count."""
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    bounce = close.pct_change(WDAYS) > 0.05
    low_vol = volume < 0.8 * vavg
    ev = (bounce & low_vol).astype(float)
    return (ev.rolling(QDAYS, min_periods=MDAYS).sum().where(vavg.notna(), np.nan)).diff()


def f50_tdco_203_high_volume_resistance_count_63_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of past 63 bars where high reached >=95% of 252d max BUT close < open-proxy (close < prior close)
    AND volume > 1.3x avg — failed-breakout on high volume."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_top = (high >= 0.95 * rmax)
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    ev = (at_top & (close < close.shift(1)) & (volume > 1.3 * vavg)).astype(float)
    return (ev.rolling(QDAYS, min_periods=MDAYS).sum().where(rmax.notna() & vavg.notna(), np.nan)).diff()


def f50_tdco_204_distribution_volume_concentration_252_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of past 252d volume that occurred on distribution days — distribution-volume concentration."""
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd = ((ret < -0.002) & (volume > vavg))
    dv = volume.where(dd, 0).rolling(YDAYS, min_periods=QDAYS).sum()
    tv = volume.rolling(YDAYS, min_periods=QDAYS).sum()
    return (_safe_div(dv, tv).where(vavg.notna(), np.nan)).diff()


def f50_tdco_205_turnover_to_atr_post_peak_63_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(63d avg dollar-volume) / ATR(21) conditioned on post-peak (within 252 of 252d max). Else NaN.
    Captures churning intensity per unit of vol."""
    dv = (close * volume).rolling(QDAYS, min_periods=MDAYS).mean()
    atr = _atr(high, low, close, MDAYS)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs = _bars_since_true(high == rmax)
    post = (bs > 0) & (bs <= YDAYS)
    return (_safe_div(dv, atr).where(post, np.nan)).diff()


def f50_tdco_206_volume_profile_resistance_violation_count_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of past 63 where close broke prior 21d-high BUT volume < prior 50d avg (low-vol breakout = suspect resistance)."""
    prior_h = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    ev = (close > prior_h) & (volume < vavg)
    return (ev.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(prior_h.notna() & vavg.notna(), np.nan)).diff()


def f50_tdco_207_heavy_volume_consolidation_at_top_63_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of past 63 bars with vol > 1.5x avg AND range < ATR21 AND at 252d-high (>=95%) — heavy-vol churning at top."""
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    atr = _atr(high, low, close, MDAYS)
    rng = high - low
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_top = (high >= 0.95 * rmax)
    ev = (volume > 1.5 * vavg) & (rng < atr) & at_top
    return (ev.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(vavg.notna() & atr.notna() & rmax.notna(), np.nan)).diff()


def f50_tdco_208_weak_bounce_volume_imbalance_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if today is an up-day (close > prior close) AND today's volume < yesterday's volume (which was a down day).
    Weak bounce after distribution."""
    today_up = close > close.shift(1)
    yesterday_down = close.shift(1) < close.shift(2)
    today_low_vol = volume < volume.shift(1)
    ev = today_up & yesterday_down & today_low_vol
    return (ev.astype(float).where(close.shift(2).notna(), np.nan)).diff()


def f50_tdco_209_stale_volume_indicator_post_peak_252_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if volume has been declining for 60+ days after the 252d peak: 60-bar slope of volume < 0 AND post-peak."""
    sl = _rolling_slope(volume, 60)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs = _bars_since_true(high == rmax)
    post = (bs > 60) & (bs <= YDAYS)
    ev = (sl < 0) & post
    return (ev.astype(float).where(sl.notna() & rmax.notna(), np.nan)).diff()


def f50_tdco_210_capitulation_volume_already_happened_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if past 63 bars contained a single bar with vol > 5x prior-50d-avg AND return < -5%.
    Capitulation already occurred (bear cleanup)."""
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    ret = close.pct_change()
    cap = ((volume > 5.0 * vavg) & (ret < -0.05)).astype(float)
    occurred = cap.rolling(QDAYS, min_periods=MDAYS).sum() > 0
    return (occurred.astype(float).where(vavg.notna(), np.nan)).diff()


def f50_tdco_211_weeks_since_breakout_252_d1(high: pd.Series) -> pd.Series:
    """Bars since the initial breakout above 252d-high (high == 252d-max event), divided by 5, capped at 50."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    ev = (high >= rmax) & (high.shift(1) < rmax.shift(1))
    bs = _bars_since_true(ev)
    weeks = bs / float(WDAYS)
    return (weeks.clip(upper=50.0)).diff()


def f50_tdco_212_pre_peak_extension_pct_from_50ma_at_peak_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """At bars where high == 252d-max: (close / SMA50) - 1. Else NaN, then forward-filled forward in time
    (carries the at-peak extension value forward — PIT-clean because peak event is in the past)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = (high >= rmax)
    s50 = _sma(close, 50)
    ext = (_safe_div(close, s50) - 1.0).where(at_peak, np.nan)
    return (ext.ffill()).diff()


def f50_tdco_213_pre_peak_extension_pct_from_200ma_at_peak_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """At bars where high == 252d-max: (close / SMA200) - 1. Else ffilled from prior peak."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = (high >= rmax)
    s200 = _sma(close, 200)
    ext = (_safe_div(close, s200) - 1.0).where(at_peak, np.nan)
    return (ext.ffill()).diff()


def f50_tdco_214_post_peak_50ma_distance_decay_63_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """63d slope of (close / SMA50 - 1) conditioned on post-peak (within 252 of 252d max). Else NaN.
    Negative = MA-distance compressing/inverting."""
    s50 = _sma(close, 50)
    dist = _safe_div(close, s50) - 1.0
    sl = _rolling_slope(dist, QDAYS)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs = _bars_since_true(high == rmax)
    post = (bs > 0) & (bs <= YDAYS)
    return (sl.where(post, np.nan)).diff()


def f50_tdco_215_post_peak_200ma_distance_decay_63_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """63d slope of (close / SMA200 - 1) conditioned on post-peak. Else NaN."""
    s200 = _sma(close, 200)
    dist = _safe_div(close, s200) - 1.0
    sl = _rolling_slope(dist, QDAYS)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs = _bars_since_true(high == rmax)
    post = (bs > 0) & (bs <= YDAYS)
    return (sl.where(post, np.nan)).diff()


def f50_tdco_216_blow_off_top_proxy_atr_normalized_63_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """At bars where high == 252d max: 21d return / ATR21. Else ffilled. Large positive = blow-off top."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = (high >= rmax)
    r21 = close.pct_change(MDAYS)
    atr_pct = _safe_div(_atr(high, low, close, MDAYS), close)
    bof = _safe_div(r21, atr_pct).where(at_peak, np.nan)
    return (bof.ffill()).diff()


def f50_tdco_217_ascending_top_failure_count_252_d1(high: pd.Series) -> pd.Series:
    """Count of past 252 where (5d-high > 5d-high from 63 bars ago) AND distance between successive higher highs
    is decreasing — accelerating-yet-failing ascent."""
    h5 = high.rolling(WDAYS, min_periods=2).max()
    higher = (h5 > h5.shift(QDAYS))
    gap_now = h5 - h5.shift(QDAYS)
    gap_prev = h5.shift(QDAYS) - h5.shift(2 * QDAYS)
    decel = (gap_now < gap_prev) & (gap_now > 0)
    ev = (higher & decel).astype(float)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum().where(gap_prev.notna(), np.nan)).diff()


def f50_tdco_218_range_high_resistance_clustering_252_d1(high: pd.Series) -> pd.Series:
    """Count of past 252 bars where high touched within 1% of 252d max — top-band touch count (clustering)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = (high >= 0.99 * rmax).astype(float)
    return (near.rolling(YDAYS, min_periods=QDAYS).sum().where(rmax.notna(), np.nan)).diff()


def f50_tdco_219_range_low_support_breaks_count_252_d1(low: pd.Series) -> pd.Series:
    """Count of past 252 bars where low touched within 1% of 252d min — bottom-band touch count (broken support cluster)."""
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    near = (low <= 1.01 * rmin).astype(float)
    return (near.rolling(YDAYS, min_periods=QDAYS).sum().where(rmin.notna(), np.nan)).diff()


def f50_tdco_220_post_peak_attempted_recovery_failure_aggregate_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Aggregate failure score conditioned on post-peak: sum of {failed-bounces in 63, lower-high count in 63, age of dd>10%}."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs = _bars_since_true(high == rmax)
    post = (bs > 0) & (bs <= YDAYS)
    h21 = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    bounce = close.pct_change(WDAYS) > 0.05
    failed = (bounce & (high < h21)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    h5 = high.rolling(WDAYS, min_periods=2).max()
    lh = (h5 < h5.shift(WDAYS)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    dd = _safe_div(rmax - close, rmax)
    age_dd = _streak_true(dd > 0.10)
    score = failed.fillna(0) + lh.fillna(0) + age_dd.fillna(0)
    return (score.where(post, np.nan)).diff()


def f50_tdco_221_cycle_age_indicator_252_normalized_d1(low: pd.Series) -> pd.Series:
    """(bars since most-recent 252d low) / 252 — cycle age (1.0 = full year, >1.0 = late cycle)."""
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    bs = _bars_since_true(low == rmin)
    return (bs / float(YDAYS)).diff()


def f50_tdco_222_distribution_intensity_score_252_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Weighted sum of distribution-day strength in past 252: sum of (|return| × volume/avg-volume) on down days."""
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    vratio = _safe_div(volume, vavg)
    w = (ret.where(ret < 0, 0).abs() * vratio).where(vavg.notna(), np.nan)
    return (w.rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f50_tdco_223_terminal_breakdown_aggregate_extended_score_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum across breakdown signals: {21d-low break count, 63d-low break count, SMA50-break count, SMA200-break count,
    death-cross event count, high-vol-break-of-63d-low count} in past 252."""
    prev_ll21 = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    prev_ll63 = low.shift(1).rolling(QDAYS, min_periods=MDAYS).min()
    s50 = _sma(close, 50); s200 = _sma(close, 200)
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    e1 = (close < prev_ll21).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    e2 = (close < prev_ll63).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    e3 = ((close.shift(1) >= s50.shift(1)) & (close < s50)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    e4 = ((close.shift(1) >= s200.shift(1)) & (close < s200)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    d = s50 - s200
    e5 = ((d.shift(1) >= 0) & (d < 0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    e6 = ((close < prev_ll63) & (volume > 1.5 * vavg)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    tot = (e1.fillna(0) + e2.fillna(0) + e3.fillna(0) + e4.fillna(0) + e5.fillna(0) + e6.fillna(0))
    return (tot.where(s200.notna() & vavg.notna(), np.nan)).diff()


def f50_tdco_224_full_market_topping_composite_score_v2_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Extension of master_score with Wyckoff + candle + multi-bar:
    sum of {upthrust in past 21, shooting-star-at-top in past 21, double-top, descending-triangle,
    high-vol-resistance-count >=2, distribution-day-count >=5, close < SMA50, close < SMA200}."""
    prior_h = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    mid = (high + low) / 2.0
    upthrust = ((high > prior_h) & (close < open) & (close < mid)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    body = (close - open).abs()
    rng = (high - low).replace(0, np.nan)
    upper = high - pd.concat([close, open], axis=1).max(axis=1)
    lower = pd.concat([close, open], axis=1).min(axis=1) - low
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_top = (high >= 0.95 * rmax)
    ss = ((upper >= 2.0 * body) & (body <= 0.3 * rng) & (lower < 0.2 * rng) & at_top).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    h_rec = high.rolling(32, min_periods=10).max()
    h_pr = high.shift(32).rolling(32, min_periods=10).max()
    dt_ratio = _safe_div(pd.concat([h_rec, h_pr], axis=1).min(axis=1), pd.concat([h_rec, h_pr], axis=1).max(axis=1))
    dt = ((dt_ratio >= 0.99) & (pd.concat([h_rec, h_pr], axis=1).max(axis=1) >= 0.90 * rmax)).astype(float)
    sl_h = _rolling_slope(high, QDAYS)
    sl_l = _rolling_slope(low, QDAYS)
    desc_tri = ((sl_h < 0) & (sl_l.abs() * float(QDAYS) < low.rolling(QDAYS, min_periods=MDAYS).std().replace(0, np.nan))).astype(float)
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    hvr = (((high >= 0.95 * rmax) & (close < close.shift(1)) & (volume > 1.3 * vavg)).astype(float)
           .rolling(QDAYS, min_periods=MDAYS).sum())
    ret = close.pct_change()
    dd_count = ((ret < -0.002) & (volume > vavg)).astype(float).rolling(25, min_periods=10).sum()
    s50 = _sma(close, 50); s200 = _sma(close, 200)
    score = ((upthrust >= 1.0).astype(float).fillna(0)
             + (ss >= 1.0).astype(float).fillna(0)
             + dt.fillna(0)
             + desc_tri.fillna(0)
             + (hvr >= 2.0).astype(float).fillna(0)
             + (dd_count >= 5.0).astype(float).fillna(0)
             + (close < s50).astype(float).fillna(0)
             + (close < s200).astype(float).fillna(0))
    return (score.where(s200.notna() & vavg.notna() & rmax.notna(), np.nan)).diff()


def f50_tdco_225_stuck_score_normalized_composite_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Stuck score = (drawdown_from_252max × time_underwater_below_20pct) normalized by 252d realized vol of returns.
    Larger = depth+duration stress per unit of vol."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    tu = (dd > 0.20).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    rv = close.pct_change().rolling(YDAYS, min_periods=QDAYS).std()
    return (_safe_div(dd * tu, rv)).diff()


# ============================================================
#                         REGISTRY 151-225 (d1)
# ============================================================

TERMINAL_DISTRIBUTION_COMPOSITE_D1_REGISTRY_151_225 = {
    "f50_tdco_151_upthrust_pattern_indicator_d1": {"inputs": ["open", "high", "low", "close"], "func": f50_tdco_151_upthrust_pattern_indicator_d1},
    "f50_tdco_152_upthrust_after_distribution_count_63_d1": {"inputs": ["open", "high", "low", "close", "volume"], "func": f50_tdco_152_upthrust_after_distribution_count_63_d1},
    "f50_tdco_153_secondary_test_failure_indicator_d1": {"inputs": ["high", "close", "volume"], "func": f50_tdco_153_secondary_test_failure_indicator_d1},
    "f50_tdco_154_stopping_volume_indicator_d1": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_154_stopping_volume_indicator_d1},
    "f50_tdco_155_climactic_action_indicator_d1": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_155_climactic_action_indicator_d1},
    "f50_tdco_156_effort_vs_result_divergence_63_d1": {"inputs": ["close", "volume"], "func": f50_tdco_156_effort_vs_result_divergence_63_d1},
    "f50_tdco_157_no_demand_day_indicator_d1": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_157_no_demand_day_indicator_d1},
    "f50_tdco_158_no_supply_day_indicator_d1": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_158_no_supply_day_indicator_d1},
    "f50_tdco_159_distribution_phase_indicator_simplified_d1": {"inputs": ["high", "close", "volume"], "func": f50_tdco_159_distribution_phase_indicator_simplified_d1},
    "f50_tdco_160_markdown_phase_acceleration_63_d1": {"inputs": ["close"], "func": f50_tdco_160_markdown_phase_acceleration_63_d1},
    "f50_tdco_161_re_distribution_count_252_d1": {"inputs": ["close", "volume"], "func": f50_tdco_161_re_distribution_count_252_d1},
    "f50_tdco_162_false_breakout_above_top_count_252_d1": {"inputs": ["high", "close"], "func": f50_tdco_162_false_breakout_above_top_count_252_d1},
    "f50_tdco_163_failed_test_of_recent_high_indicator_d1": {"inputs": ["high"], "func": f50_tdco_163_failed_test_of_recent_high_indicator_d1},
    "f50_tdco_164_wide_range_red_at_resistance_count_63_d1": {"inputs": ["high", "low", "close"], "func": f50_tdco_164_wide_range_red_at_resistance_count_63_d1},
    "f50_tdco_165_shake_out_pattern_indicator_d1": {"inputs": ["low", "close"], "func": f50_tdco_165_shake_out_pattern_indicator_d1},
    "f50_tdco_166_shooting_star_at_top_indicator_d1": {"inputs": ["open", "high", "low", "close"], "func": f50_tdco_166_shooting_star_at_top_indicator_d1},
    "f50_tdco_167_shooting_star_at_top_count_63_d1": {"inputs": ["open", "high", "low", "close"], "func": f50_tdco_167_shooting_star_at_top_count_63_d1},
    "f50_tdco_168_gravestone_doji_at_top_indicator_d1": {"inputs": ["open", "high", "low", "close"], "func": f50_tdco_168_gravestone_doji_at_top_indicator_d1},
    "f50_tdco_169_hanging_man_indicator_d1": {"inputs": ["open", "high", "low", "close"], "func": f50_tdco_169_hanging_man_indicator_d1},
    "f50_tdco_170_dark_cloud_cover_pattern_indicator_d1": {"inputs": ["open", "high", "close"], "func": f50_tdco_170_dark_cloud_cover_pattern_indicator_d1},
    "f50_tdco_171_bearish_engulfing_at_top_indicator_d1": {"inputs": ["open", "high", "close"], "func": f50_tdco_171_bearish_engulfing_at_top_indicator_d1},
    "f50_tdco_172_evening_star_pattern_indicator_d1": {"inputs": ["open", "high", "close"], "func": f50_tdco_172_evening_star_pattern_indicator_d1},
    "f50_tdco_173_three_black_crows_pattern_indicator_d1": {"inputs": ["open", "close"], "func": f50_tdco_173_three_black_crows_pattern_indicator_d1},
    "f50_tdco_174_dragonfly_doji_at_top_indicator_d1": {"inputs": ["open", "high", "low", "close"], "func": f50_tdco_174_dragonfly_doji_at_top_indicator_d1},
    "f50_tdco_175_tweezers_top_indicator_d1": {"inputs": ["high"], "func": f50_tdco_175_tweezers_top_indicator_d1},
    "f50_tdco_176_harami_at_top_indicator_d1": {"inputs": ["open", "high", "close"], "func": f50_tdco_176_harami_at_top_indicator_d1},
    "f50_tdco_177_doji_at_252_high_indicator_d1": {"inputs": ["open", "high", "low", "close"], "func": f50_tdco_177_doji_at_252_high_indicator_d1},
    "f50_tdco_178_long_upper_shadow_pct_in_range_63_d1": {"inputs": ["open", "high", "low", "close"], "func": f50_tdco_178_long_upper_shadow_pct_in_range_63_d1},
    "f50_tdco_179_long_upper_shadow_at_top_count_63_d1": {"inputs": ["open", "high", "low", "close"], "func": f50_tdco_179_long_upper_shadow_at_top_count_63_d1},
    "f50_tdco_180_bearish_candle_cluster_score_21_d1": {"inputs": ["open", "high", "low", "close"], "func": f50_tdco_180_bearish_candle_cluster_score_21_d1},
    "f50_tdco_181_double_top_pattern_indicator_63_d1": {"inputs": ["high"], "func": f50_tdco_181_double_top_pattern_indicator_63_d1},
    "f50_tdco_182_triple_top_pattern_indicator_63_d1": {"inputs": ["high"], "func": f50_tdco_182_triple_top_pattern_indicator_63_d1},
    "f50_tdco_183_bear_flag_pattern_indicator_21_d1": {"inputs": ["high", "low", "close"], "func": f50_tdco_183_bear_flag_pattern_indicator_21_d1},
    "f50_tdco_184_bear_pennant_pattern_indicator_21_d1": {"inputs": ["high", "low", "close"], "func": f50_tdco_184_bear_pennant_pattern_indicator_21_d1},
    "f50_tdco_185_rising_wedge_pattern_indicator_63_d1": {"inputs": ["high", "low"], "func": f50_tdco_185_rising_wedge_pattern_indicator_63_d1},
    "f50_tdco_186_descending_triangle_pattern_indicator_63_d1": {"inputs": ["high", "low"], "func": f50_tdco_186_descending_triangle_pattern_indicator_63_d1},
    "f50_tdco_187_bump_run_reversal_proxy_63_d1": {"inputs": ["close"], "func": f50_tdco_187_bump_run_reversal_proxy_63_d1},
    "f50_tdco_188_cup_with_handle_failure_proxy_63_d1": {"inputs": ["high", "low", "close"], "func": f50_tdco_188_cup_with_handle_failure_proxy_63_d1},
    "f50_tdco_189_dead_cat_bounce_indicator_d1": {"inputs": ["close"], "func": f50_tdco_189_dead_cat_bounce_indicator_d1},
    "f50_tdco_190_three_drives_pattern_indicator_63_d1": {"inputs": ["high"], "func": f50_tdco_190_three_drives_pattern_indicator_63_d1},
    "f50_tdco_191_gartley_failure_proxy_63_d1": {"inputs": ["high", "low", "close"], "func": f50_tdco_191_gartley_failure_proxy_63_d1},
    "f50_tdco_192_marubozu_red_at_top_indicator_d1": {"inputs": ["open", "high", "low", "close"], "func": f50_tdco_192_marubozu_red_at_top_indicator_d1},
    "f50_tdco_193_spinning_top_at_252_high_indicator_d1": {"inputs": ["open", "high", "low", "close"], "func": f50_tdco_193_spinning_top_at_252_high_indicator_d1},
    "f50_tdco_194_counter_trend_thrust_failed_count_63_d1": {"inputs": ["open", "high", "low", "close"], "func": f50_tdco_194_counter_trend_thrust_failed_count_63_d1},
    "f50_tdco_195_failed_swing_low_violation_indicator_d1": {"inputs": ["low", "close"], "func": f50_tdco_195_failed_swing_low_violation_indicator_d1},
    "f50_tdco_196_volume_at_high_concentration_index_63_d1": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_196_volume_at_high_concentration_index_63_d1},
    "f50_tdco_197_volume_skew_post_peak_63_d1": {"inputs": ["high", "volume"], "func": f50_tdco_197_volume_skew_post_peak_63_d1},
    "f50_tdco_198_volume_max_recently_vs_avg_63_d1": {"inputs": ["volume"], "func": f50_tdco_198_volume_max_recently_vs_avg_63_d1},
    "f50_tdco_199_down_volume_dominance_at_top_63_d1": {"inputs": ["high", "close", "volume"], "func": f50_tdco_199_down_volume_dominance_at_top_63_d1},
    "f50_tdco_200_largest_down_day_vol_in_post_peak_63_d1": {"inputs": ["high", "close", "volume"], "func": f50_tdco_200_largest_down_day_vol_in_post_peak_63_d1},
    "f50_tdco_201_volume_decline_rate_post_peak_d1": {"inputs": ["high", "volume"], "func": f50_tdco_201_volume_decline_rate_post_peak_d1},
    "f50_tdco_202_low_volume_bounce_count_63_d1": {"inputs": ["close", "volume"], "func": f50_tdco_202_low_volume_bounce_count_63_d1},
    "f50_tdco_203_high_volume_resistance_count_63_d1": {"inputs": ["high", "close", "volume"], "func": f50_tdco_203_high_volume_resistance_count_63_d1},
    "f50_tdco_204_distribution_volume_concentration_252_d1": {"inputs": ["close", "volume"], "func": f50_tdco_204_distribution_volume_concentration_252_d1},
    "f50_tdco_205_turnover_to_atr_post_peak_63_d1": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_205_turnover_to_atr_post_peak_63_d1},
    "f50_tdco_206_volume_profile_resistance_violation_count_d1": {"inputs": ["high", "close", "volume"], "func": f50_tdco_206_volume_profile_resistance_violation_count_d1},
    "f50_tdco_207_heavy_volume_consolidation_at_top_63_d1": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_207_heavy_volume_consolidation_at_top_63_d1},
    "f50_tdco_208_weak_bounce_volume_imbalance_indicator_d1": {"inputs": ["close", "volume"], "func": f50_tdco_208_weak_bounce_volume_imbalance_indicator_d1},
    "f50_tdco_209_stale_volume_indicator_post_peak_252_d1": {"inputs": ["high", "volume"], "func": f50_tdco_209_stale_volume_indicator_post_peak_252_d1},
    "f50_tdco_210_capitulation_volume_already_happened_indicator_d1": {"inputs": ["close", "volume"], "func": f50_tdco_210_capitulation_volume_already_happened_indicator_d1},
    "f50_tdco_211_weeks_since_breakout_252_d1": {"inputs": ["high"], "func": f50_tdco_211_weeks_since_breakout_252_d1},
    "f50_tdco_212_pre_peak_extension_pct_from_50ma_at_peak_d1": {"inputs": ["high", "close"], "func": f50_tdco_212_pre_peak_extension_pct_from_50ma_at_peak_d1},
    "f50_tdco_213_pre_peak_extension_pct_from_200ma_at_peak_d1": {"inputs": ["high", "close"], "func": f50_tdco_213_pre_peak_extension_pct_from_200ma_at_peak_d1},
    "f50_tdco_214_post_peak_50ma_distance_decay_63_d1": {"inputs": ["high", "close"], "func": f50_tdco_214_post_peak_50ma_distance_decay_63_d1},
    "f50_tdco_215_post_peak_200ma_distance_decay_63_d1": {"inputs": ["high", "close"], "func": f50_tdco_215_post_peak_200ma_distance_decay_63_d1},
    "f50_tdco_216_blow_off_top_proxy_atr_normalized_63_d1": {"inputs": ["high", "low", "close"], "func": f50_tdco_216_blow_off_top_proxy_atr_normalized_63_d1},
    "f50_tdco_217_ascending_top_failure_count_252_d1": {"inputs": ["high"], "func": f50_tdco_217_ascending_top_failure_count_252_d1},
    "f50_tdco_218_range_high_resistance_clustering_252_d1": {"inputs": ["high"], "func": f50_tdco_218_range_high_resistance_clustering_252_d1},
    "f50_tdco_219_range_low_support_breaks_count_252_d1": {"inputs": ["low"], "func": f50_tdco_219_range_low_support_breaks_count_252_d1},
    "f50_tdco_220_post_peak_attempted_recovery_failure_aggregate_d1": {"inputs": ["high", "close"], "func": f50_tdco_220_post_peak_attempted_recovery_failure_aggregate_d1},
    "f50_tdco_221_cycle_age_indicator_252_normalized_d1": {"inputs": ["low"], "func": f50_tdco_221_cycle_age_indicator_252_normalized_d1},
    "f50_tdco_222_distribution_intensity_score_252_d1": {"inputs": ["close", "volume"], "func": f50_tdco_222_distribution_intensity_score_252_d1},
    "f50_tdco_223_terminal_breakdown_aggregate_extended_score_d1": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_223_terminal_breakdown_aggregate_extended_score_d1},
    "f50_tdco_224_full_market_topping_composite_score_v2_d1": {"inputs": ["open", "high", "low", "close", "volume"], "func": f50_tdco_224_full_market_topping_composite_score_v2_d1},
    "f50_tdco_225_stuck_score_normalized_composite_d1": {"inputs": ["high", "close"], "func": f50_tdco_225_stuck_score_normalized_composite_d1},
}
