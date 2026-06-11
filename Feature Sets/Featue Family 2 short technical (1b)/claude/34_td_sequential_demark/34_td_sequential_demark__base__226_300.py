"""td_sequential_demark base features 226-300 — Pipeline 1b-technical (gap-fill extension).

Extends 001-225 with TD D-Wave (wave counter), TD Demand/Supply Lines (slope-of-pivot
trendlines), TD Channels 1/2, TD Waldo bar patterns, TD POQ (Price Oscillator Qualifier),
TD ROC, TD Relative/Absolute Retracement targets, TD Moving Averages 1/2, TD Sequential
signal conjunctions at 5-year highs, and master DeMark plurality composites.

Inputs: SEP OHLCV only. PIT-clean. Self-contained helpers.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_5Y = 1260


# ---------------------------- standard helpers ----------------------------

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


def _pct_rank(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).rank(pct=True)


def _bars_since_true(flag):
    f = (flag.fillna(0) > 0).astype(int)
    idx = np.arange(len(f))
    last = np.where(f.values == 1, idx, np.nan)
    last_ffill = pd.Series(last, index=f.index).ffill()
    return pd.Series(idx, index=f.index) - last_ffill


def _sma(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).mean()


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


# ---------------------------- TD setup helpers ----------------------------

def _td_sell_setup_count(close: pd.Series) -> pd.Series:
    qual = (close > close.shift(4)).astype(int)
    qual = qual.where(close.shift(4).notna(), np.nan).fillna(0).astype(int)
    grp = (qual == 0).cumsum()
    return qual.groupby(grp).cumsum().astype(float)


def _td_buy_setup_count(close: pd.Series) -> pd.Series:
    qual = (close < close.shift(4)).astype(int)
    qual = qual.where(close.shift(4).notna(), np.nan).fillna(0).astype(int)
    grp = (qual == 0).cumsum()
    return qual.groupby(grp).cumsum().astype(float)


def _td_sell_countdown_count(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    sc = _td_sell_setup_count(close).values
    bc = _td_buy_setup_count(close).values
    cl = close.values; hi = high.values
    n = len(close)
    out = np.zeros(n)
    active = False; cnt = 0
    for i in range(n):
        if not active and i >= 8 and sc[i] >= 9:
            active = True; cnt = 0
        if active and i >= 8 and bc[i] >= 9:
            active = False; cnt = 0
        if active:
            if i >= 2 and cl[i] >= hi[i - 2] and cnt < 13:
                cnt += 1
            out[i] = cnt
    return pd.Series(out, index=close.index)


# ---------------------------- TD D-Wave / Lines / Channels helpers ----------------------------

def _td_d_wave_higher_high_streak_21(close: pd.Series) -> pd.Series:
    """Approximated TD D-Wave segment count: consecutive bars where close > close 21 ago
    AND close 21 ago > close 42 ago (uptrend wave structure)."""
    flag = ((close > close.shift(21)) & (close.shift(21) > close.shift(42))).astype(int).fillna(0)
    grp = (flag == 0).cumsum()
    return flag.groupby(grp).cumsum().astype(float)


def _td_d_wave_lower_low_streak_21(close: pd.Series) -> pd.Series:
    """Approximated bearish D-Wave: consecutive bars where close < close 21 ago AND close 21 < close 42."""
    flag = ((close < close.shift(21)) & (close.shift(21) < close.shift(42))).astype(int).fillna(0)
    grp = (flag == 0).cumsum()
    return flag.groupby(grp).cumsum().astype(float)


def _two_extreme_slope(s: pd.Series, n: int, mode: str) -> pd.Series:
    """Slope of the line through the 2 largest (mode='max') or smallest (mode='min')
    values in trailing n bars (TD Supply/Demand Line proxy)."""
    def _line_slope(w):
        if np.all(np.isnan(w)):
            return np.nan
        if mode == "max":
            idx = np.argsort(w)[-2:]
        else:
            idx = np.argsort(w)[:2]
        i1, i2 = sorted([int(x) for x in idx])
        if i2 == i1:
            return 0.0
        return float((w[i2] - w[i1]) / (i2 - i1))
    return s.rolling(n, min_periods=max(n // 3, 2)).apply(_line_slope, raw=True)


def _td_channel_1_upper(high: pd.Series, n: int = 8) -> pd.Series:
    return high.rolling(n, min_periods=max(n // 3, 2)).max()


def _td_channel_1_lower(low: pd.Series, n: int = 8) -> pd.Series:
    return low.rolling(n, min_periods=max(n // 3, 2)).min()


def _td_channel_2_upper(high: pd.Series, n: int = 21) -> pd.Series:
    return high.rolling(n, min_periods=max(n // 3, 2)).max()


def _td_channel_2_lower(low: pd.Series, n: int = 21) -> pd.Series:
    return low.rolling(n, min_periods=max(n // 3, 2)).min()


# ---------------------------- Waldo / POQ / ROC / Retracement helpers ----------------------------

def _waldo_2_bearish_event(open_: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bearish Waldo 2: today's close < prior close AND today's open is within upper half of today's range
    AND today's close is at/below low + 0.25 × today's range."""
    rng = (high - low).replace(0, np.nan)
    open_pos = _safe_div(open_ - low, rng)
    close_pos = _safe_div(close - low, rng)
    return ((close < close.shift(1)) & (open_pos > 0.5) & (close_pos < 0.25)).astype(float)


def _waldo_3_bearish_event(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bearish Waldo 3: today's high > prior high BUT today's close < midpoint of today's range
    (failed-thrust pattern)."""
    rng = (high - low).replace(0, np.nan)
    return ((high > high.shift(1)) & (_safe_div(close - low, rng) < 0.5)).astype(float)


def _waldo_5_bearish_event(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bearish Waldo 5: 3-bar pattern — bar 1 is up bar, bar 2 makes new high but lower close,
    bar 3 closes below bar 2 close."""
    return ((close.shift(2) > close.shift(3))
            & (high.shift(1) > high.shift(2)) & (close.shift(1) < close.shift(2))
            & (close < close.shift(1))).astype(float)


def _td_poq_sell_event(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TD POQ sell qualifier (bearish): today's open > prior high (gap-up), today's close < prior high
    AND today's close < today's open (failed gap-up that closes below prior resistance)."""
    return ((open_ > high.shift(1)) & (close < high.shift(1)) & (close < open_)).astype(float)


def _td_relative_retracement_38pct_level(high: pd.Series, low: pd.Series, n: int = YDAYS) -> pd.Series:
    rng = high.rolling(n, min_periods=max(n // 3, 2)).max() - low.rolling(n, min_periods=max(n // 3, 2)).min()
    return low.rolling(n, min_periods=max(n // 3, 2)).min() + 0.382 * rng


def _td_relative_retracement_62pct_level(high: pd.Series, low: pd.Series, n: int = YDAYS) -> pd.Series:
    rng = high.rolling(n, min_periods=max(n // 3, 2)).max() - low.rolling(n, min_periods=max(n // 3, 2)).min()
    return low.rolling(n, min_periods=max(n // 3, 2)).min() + 0.618 * rng


# ---------------------------- divergence helpers ----------------------------

def _slope_div_sign(price, osc, n):
    ps = _rolling_slope(_safe_log(price), n)
    osl = _rolling_slope(osc, n)
    bear = ((ps > 0) & (osl < 0)).astype(float)
    bull = ((ps < 0) & (osl > 0)).astype(float)
    return (bear - bull).where(ps.notna() & osl.notna(), np.nan)


# ============================================================
# Bucket VVV — TD D-Wave (226-235)
# ============================================================

def f34_tdsq_226_td_d_wave_higher_high_streak_21d(close: pd.Series) -> pd.Series:
    """Approximated TD D-Wave bullish-wave segment count: consecutive HH-21d streak."""
    return _td_d_wave_higher_high_streak_21(close)


def f34_tdsq_227_td_d_wave_lower_low_streak_21d(close: pd.Series) -> pd.Series:
    """Approximated TD D-Wave bearish-wave segment count: consecutive LL-21d streak."""
    return _td_d_wave_lower_low_streak_21(close)


def f34_tdsq_228_td_d_wave_max_higher_high_streak_252d(close: pd.Series) -> pd.Series:
    """Maximum bullish-wave segment length within trailing 252d."""
    return _td_d_wave_higher_high_streak_21(close).rolling(YDAYS, min_periods=QDAYS).max()


def f34_tdsq_229_td_d_wave_count_completions_252d(close: pd.Series) -> pd.Series:
    """Count of bars in trailing 252d where bullish-wave streak reset from > 0 to 0 (wave completions)."""
    s = _td_d_wave_higher_high_streak_21(close)
    end = ((s == 0) & (s.shift(1) > 0)).astype(float)
    return end.rolling(YDAYS, min_periods=QDAYS).sum()


def f34_tdsq_230_td_d_wave_5wave_indicator(close: pd.Series) -> pd.Series:
    """+1 when bullish-wave streak >= 5 bars (5-wave Elliott-like advance)."""
    s = _td_d_wave_higher_high_streak_21(close)
    return (s >= 5).astype(float).where(s.notna(), np.nan)


def f34_tdsq_231_td_d_wave_pct_rank_streak_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of current bullish-wave streak in trailing 252d."""
    return _pct_rank(_td_d_wave_higher_high_streak_21(close), YDAYS)


def f34_tdsq_232_td_d_wave_amplitude_252d(close: pd.Series) -> pd.Series:
    """252d-max close / 252d-min close — full wave amplitude (always >= 1)."""
    return _safe_div(close.rolling(YDAYS, min_periods=QDAYS).max(),
                     close.rolling(YDAYS, min_periods=QDAYS).min())


def f34_tdsq_233_td_d_wave_exhaustion_indicator(close: pd.Series) -> pd.Series:
    """+1 when bullish-wave streak >= 5 AND price within 1% of 252d max (potential 5-wave exhaustion at high)."""
    s = _td_d_wave_higher_high_streak_21(close)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return ((s >= 5) & (near == 1)).astype(float).where(s.notna() & near.notna(), np.nan)


def f34_tdsq_234_td_d_wave_bearish_streak_acceleration_indicator(close: pd.Series) -> pd.Series:
    """+1 when bearish-wave (LL-21d) streak just incremented from 0 → 1 (wave start)."""
    s = _td_d_wave_lower_low_streak_21(close)
    return ((s == 1) & (s.shift(1) == 0)).astype(float).where(s.notna() & s.shift(1).notna(), np.nan)


def f34_tdsq_235_td_d_wave_segment_count_504d(close: pd.Series) -> pd.Series:
    """Count of distinct bullish-wave segments (each ≥ 1 bar) in trailing 504d."""
    s = _td_d_wave_higher_high_streak_21(close)
    starts = ((s == 1) & (s.shift(1) == 0)).astype(float)
    return starts.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


# ============================================================
# Bucket WWW — TD Demand / Supply Lines (slope-of-2-pivots) (236-245)
# ============================================================

def f34_tdsq_236_td_supply_line_slope_63d(high: pd.Series) -> pd.Series:
    """Slope of the line through the 2 highest highs in trailing 63d (TD Supply Line proxy)."""
    return _two_extreme_slope(high, QDAYS, "max")


def f34_tdsq_237_td_supply_line_slope_252d(high: pd.Series) -> pd.Series:
    """Slope of TD Supply Line over 252d (secular)."""
    return _two_extreme_slope(high, YDAYS, "max")


def f34_tdsq_238_td_demand_line_slope_63d(low: pd.Series) -> pd.Series:
    """Slope of the line through the 2 lowest lows in trailing 63d (TD Demand Line proxy)."""
    return _two_extreme_slope(low, QDAYS, "min")


def f34_tdsq_239_td_demand_line_slope_252d(low: pd.Series) -> pd.Series:
    """Slope of TD Demand Line over 252d."""
    return _two_extreme_slope(low, YDAYS, "min")


def f34_tdsq_240_td_supply_line_falling_indicator_63d(high: pd.Series) -> pd.Series:
    """+1 when 63d Supply-Line slope < 0 (downward-sloping resistance — bearish structure)."""
    s = _two_extreme_slope(high, QDAYS, "max")
    return (s < 0).astype(float).where(s.notna(), np.nan)


def f34_tdsq_241_td_supply_line_rising_x_at_252d_high_indicator(high: pd.Series, close: pd.Series) -> pd.Series:
    """+1 when 63d Supply-Line slope > 0 (rising resistance) AND close within 1% of 252d max — overhead resistance."""
    s = _two_extreme_slope(high, QDAYS, "max")
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return ((s > 0) & (near == 1)).astype(float).where(s.notna() & near.notna(), np.nan)


def f34_tdsq_242_supply_minus_demand_slope_diff_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Supply-line slope - Demand-line slope (63d) — channel-converging if negative."""
    return _two_extreme_slope(high, QDAYS, "max") - _two_extreme_slope(low, QDAYS, "min")


def f34_tdsq_243_td_lines_channel_converging_indicator_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when (Supply slope - Demand slope) < 0 AND Supply slope < 0 — converging channel narrowing top."""
    diff = _two_extreme_slope(high, QDAYS, "max") - _two_extreme_slope(low, QDAYS, "min")
    sup_falling = _two_extreme_slope(high, QDAYS, "max") < 0
    return ((diff < 0) & sup_falling).astype(float).where(diff.notna(), np.nan)


def f34_tdsq_244_td_supply_line_break_event_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+1 when close > 63d-rolling-max(high) for first time in 21d (supply-line break event)."""
    rmax_prev = high.shift(1).rolling(QDAYS - 1, min_periods=max(QDAYS // 3, 2)).max()
    flag = (close > rmax_prev).astype(int)
    return ((flag == 1) & (flag.shift(1) == 0)).astype(float).where(rmax_prev.notna() & flag.shift(1).notna(), np.nan)


def f34_tdsq_245_td_demand_line_break_event_indicator(close: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when close < 63d-rolling-min(low) for first time in 21d (demand-line break)."""
    rmin_prev = low.shift(1).rolling(QDAYS - 1, min_periods=max(QDAYS // 3, 2)).min()
    flag = (close < rmin_prev).astype(int)
    return ((flag == 1) & (flag.shift(1) == 0)).astype(float).where(rmin_prev.notna() & flag.shift(1).notna(), np.nan)


# ============================================================
# Bucket XXX — TD Channels 1 / 2 (246-253)
# ============================================================

def f34_tdsq_246_td_channel_1_upper(high: pd.Series) -> pd.Series:
    """TD Channel 1 upper band: highest high in trailing 8 bars."""
    return _td_channel_1_upper(high, 8)


def f34_tdsq_247_td_channel_1_lower(low: pd.Series) -> pd.Series:
    """TD Channel 1 lower band: lowest low in trailing 8 bars."""
    return _td_channel_1_lower(low, 8)


def f34_tdsq_248_close_position_in_td_channel_1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close position within TD Channel 1 [0, 1]."""
    u = _td_channel_1_upper(high, 8); l = _td_channel_1_lower(low, 8)
    return _safe_div(close - l, u - l)


def f34_tdsq_249_close_at_td_channel_1_upper_indicator(close: pd.Series, high: pd.Series) -> pd.Series:
    """+1 when close equals TD Channel 1 upper (8d-high touch)."""
    u = _td_channel_1_upper(high, 8)
    return (close >= u).astype(float).where(u.notna(), np.nan)


def f34_tdsq_250_td_channel_2_upper(high: pd.Series) -> pd.Series:
    """TD Channel 2 upper band: highest high in trailing 21 bars."""
    return _td_channel_2_upper(high, 21)


def f34_tdsq_251_td_channel_2_lower(low: pd.Series) -> pd.Series:
    """TD Channel 2 lower band: lowest low in trailing 21 bars."""
    return _td_channel_2_lower(low, 21)


def f34_tdsq_252_close_position_in_td_channel_2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close position within TD Channel 2 [0, 1]."""
    u = _td_channel_2_upper(high, 21); l = _td_channel_2_lower(low, 21)
    return _safe_div(close - l, u - l)


def f34_tdsq_253_td_channel_persistence_at_upper_21d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Count of trailing 21d bars where close was at TD Channel 1 upper (walking-the-upper-band)."""
    u = _td_channel_1_upper(high, 8)
    return (close >= u).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


# ============================================================
# Bucket YYY — TD Waldo Patterns (254-261)
# ============================================================

def f34_tdsq_254_td_waldo_2_bearish_event_indicator(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 on bar where Waldo-2 bearish pattern fires."""
    return _waldo_2_bearish_event(open, close, high, low)


def f34_tdsq_255_td_waldo_2_count_252d(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of Waldo-2 events in trailing 252d."""
    return _waldo_2_bearish_event(open, close, high, low).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum()


def f34_tdsq_256_td_waldo_3_bearish_event_indicator(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 on bar where Waldo-3 bearish pattern fires (failed-thrust)."""
    return _waldo_3_bearish_event(close, high, low)


def f34_tdsq_257_td_waldo_3_count_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of Waldo-3 events in trailing 252d."""
    return _waldo_3_bearish_event(close, high, low).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum()


def f34_tdsq_258_td_waldo_5_bearish_event_indicator(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 on bar where Waldo-5 bearish pattern fires (3-bar topping)."""
    return _waldo_5_bearish_event(close, high, low)


def f34_tdsq_259_td_waldo_5_count_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of Waldo-5 events in trailing 252d."""
    return _waldo_5_bearish_event(close, high, low).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum()


def f34_tdsq_260_td_waldo_breadth_3patterns_indicator(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when at least 1 of 3 Waldo bearish patterns fires today."""
    a = _waldo_2_bearish_event(open, close, high, low).fillna(0)
    b = _waldo_3_bearish_event(close, high, low).fillna(0)
    c = _waldo_5_bearish_event(close, high, low).fillna(0)
    return ((a + b + c) >= 1).astype(float)


def f34_tdsq_261_td_waldo_x_at_252d_high_count_252d(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of Waldo-pattern firings at near-252d-high bars in trailing 252d."""
    a = _waldo_2_bearish_event(open, close, high, low).fillna(0)
    b = _waldo_3_bearish_event(close, high, low).fillna(0)
    c = _waldo_5_bearish_event(close, high, low).fillna(0)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return ((a + b + c) * near).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket ZZZ — TD POQ (Price Oscillator Qualifier) (262-267)
# ============================================================

def f34_tdsq_262_td_poq_sell_event_indicator(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+1 on bar where TD POQ sell qualifier fires (failed gap-up that closes below prior high)."""
    return _td_poq_sell_event(open, high, low, close)


def f34_tdsq_263_td_poq_sell_count_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of TD POQ sell events in trailing 252d."""
    return _td_poq_sell_event(open, high, low, close).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum()


def f34_tdsq_264_days_since_td_poq_sell(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since most recent TD POQ sell event."""
    return _bars_since_true(_td_poq_sell_event(open, high, low, close))


def f34_tdsq_265_td_poq_sell_x_close_at_252d_high_indicator(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+1 when POQ-sell fires AND close within 1% of 252d max (gap-up exhaustion at top)."""
    f = _td_poq_sell_event(open, high, low, close)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (f * near).where(f.notna() & near.notna(), np.nan)


def f34_tdsq_266_td_poq_sell_count_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of POQ-sell events in trailing 63d (acute)."""
    return _td_poq_sell_event(open, high, low, close).fillna(0).rolling(QDAYS, min_periods=MDAYS).sum()


def f34_tdsq_267_td_poq_sell_count_at_high_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of POQ-sell at-high conjunctions in 252d."""
    f = _td_poq_sell_event(open, high, low, close).fillna(0)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (f * near).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket AAAA — TD ROC (DeMark special ROC) (268-273)
# ============================================================

def f34_tdsq_268_td_roc_13d_pct(close: pd.Series) -> pd.Series:
    """TD ROC (13d): close / close 13 bars ago × 100."""
    return 100.0 * _safe_div(close, close.shift(13))


def f34_tdsq_269_td_roc_13d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of TD ROC(13) over 252d."""
    return _rolling_zscore(100.0 * _safe_div(close, close.shift(13)), YDAYS)


def f34_tdsq_270_td_roc_13d_above_threshold_indicator(close: pd.Series) -> pd.Series:
    """+1 when TD ROC(13) > 110 (10% move in 13 days — strong momentum)."""
    r = 100.0 * _safe_div(close, close.shift(13))
    return (r > 110).astype(float).where(r.notna(), np.nan)


def f34_tdsq_271_td_roc_25d_value(close: pd.Series) -> pd.Series:
    """TD ROC at 25-day horizon."""
    return 100.0 * _safe_div(close, close.shift(25))


def f34_tdsq_272_td_roc_13d_slope_div_sign_63d(close: pd.Series) -> pd.Series:
    """Bearish slope-divergence — close vs TD ROC(13), 63d."""
    return _slope_div_sign(close, 100.0 * _safe_div(close, close.shift(13)), QDAYS)


def f34_tdsq_273_td_roc_extreme_persistence_21d(close: pd.Series) -> pd.Series:
    """Count of trailing 21d bars where TD ROC(13) > 110."""
    r = 100.0 * _safe_div(close, close.shift(13))
    return (r > 110).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


# ============================================================
# Bucket BBBB — TD Relative / Absolute Retracement (274-281)
# ============================================================

def f34_tdsq_274_td_relative_retracement_38pct_level(high: pd.Series, low: pd.Series) -> pd.Series:
    """TD Relative 38.2% Retracement level (from 252d swing)."""
    return _td_relative_retracement_38pct_level(high, low, YDAYS)


def f34_tdsq_275_td_relative_retracement_62pct_level(high: pd.Series, low: pd.Series) -> pd.Series:
    """TD Relative 61.8% Retracement level (from 252d swing)."""
    return _td_relative_retracement_62pct_level(high, low, YDAYS)


def f34_tdsq_276_close_above_td_retracement_62pct_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+1 when close > 61.8% retracement level (above golden-ratio of 252d swing)."""
    l = _td_relative_retracement_62pct_level(high, low, YDAYS)
    return (close > l).astype(float).where(l.notna(), np.nan)


def f34_tdsq_277_close_distance_to_td_retracement_62pct_atr_norm(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - 61.8% retracement) / ATR(21)."""
    l = _td_relative_retracement_62pct_level(high, low, YDAYS)
    return _safe_div(close - l, _atr(high, low, close, MDAYS))


def f34_tdsq_278_td_absolute_retracement_38_x_swing_lookback_504d(high: pd.Series, low: pd.Series) -> pd.Series:
    """TD Absolute 38.2% retracement from 504d swing."""
    return _td_relative_retracement_38pct_level(high, low, DDAYS_2Y)


def f34_tdsq_279_td_absolute_retracement_62_x_swing_lookback_504d(high: pd.Series, low: pd.Series) -> pd.Series:
    """TD Absolute 61.8% retracement from 504d swing."""
    return _td_relative_retracement_62pct_level(high, low, DDAYS_2Y)


def f34_tdsq_280_close_position_in_252d_swing_range(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Position of close within 252d swing [0, 1]."""
    h = high.rolling(YDAYS, min_periods=QDAYS).max()
    l = low.rolling(YDAYS, min_periods=QDAYS).min()
    return _safe_div(close - l, h - l)


def f34_tdsq_281_close_position_in_1260d_swing_range(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Position of close within 1260d (5y) swing [0, 1]."""
    h = high.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    l = low.rolling(DDAYS_5Y, min_periods=YDAYS).min()
    return _safe_div(close - l, h - l)


# ============================================================
# Bucket CCCC — TD Moving Averages 1 / 2 (282-286)
# ============================================================

def f34_tdsq_282_td_ma_1_value(close: pd.Series) -> pd.Series:
    """TD MA 1: 35-bar SMA (intermediate-term)."""
    return _sma(close, 35)


def f34_tdsq_283_td_ma_2_value(close: pd.Series) -> pd.Series:
    """TD MA 2: 70-bar SMA (longer-term)."""
    return _sma(close, 70)


def f34_tdsq_284_close_above_td_ma_2_indicator(close: pd.Series) -> pd.Series:
    """+1 when close > TD MA 2 (above long-term average)."""
    ma2 = _sma(close, 70)
    return (close > ma2).astype(float).where(ma2.notna(), np.nan)


def f34_tdsq_285_td_ma_1_minus_td_ma_2_diff_atr_norm(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """(TD MA1 - TD MA2) / ATR(21) — separation between intermediate and long MAs."""
    return _safe_div(_sma(close, 35) - _sma(close, 70), _atr(high, low, close, MDAYS))


def f34_tdsq_286_td_ma_bearish_cross_event_indicator(close: pd.Series) -> pd.Series:
    """+1 on bar where TD MA1 crosses below TD MA2 (intermediate weakens vs long — bearish cross)."""
    diff = _sma(close, 35) - _sma(close, 70)
    return ((diff.shift(1) > 0) & (diff <= 0)).astype(float).where(diff.notna() & diff.shift(1).notna(), np.nan)


# ============================================================
# Bucket DDDD — TD Sequential signals at 5-year highs (287-296)
# ============================================================

def f34_tdsq_287_setup_9_x_close_at_1260d_high_indicator(close: pd.Series) -> pd.Series:
    """+1 when sell-setup-9 fires AND close within 2% of 1260d max."""
    fire = (_td_sell_setup_count(close) == 9).astype(float)
    near = (close >= close.rolling(DDAYS_5Y, min_periods=YDAYS).max() * 0.98).astype(float)
    return (fire * near).where(fire.notna() & near.notna(), np.nan)


def f34_tdsq_288_setup_9_within_21d_x_close_at_1260d_high_indicator(close: pd.Series) -> pd.Series:
    """+1 when sell-setup-9 fired within last 21d AND close within 2% of 1260d max."""
    fire = (_td_sell_setup_count(close) == 9).astype(float).rolling(MDAYS, min_periods=1).max()
    near = (close >= close.rolling(DDAYS_5Y, min_periods=YDAYS).max() * 0.98).astype(float)
    return (fire * near).where(fire.notna() & near.notna(), np.nan)


def f34_tdsq_289_countdown_13_x_close_at_1260d_high_indicator(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when sell-countdown-13 fires AND close within 2% of 1260d max."""
    cd = _td_sell_countdown_count(close, high, low)
    fire = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    near = (close >= close.rolling(DDAYS_5Y, min_periods=YDAYS).max() * 0.98).astype(float)
    return (fire * near).where(fire.notna() & near.notna(), np.nan)


def f34_tdsq_290_setup_x_d_wave_x_1260d_high_triple_indicator(close: pd.Series) -> pd.Series:
    """+1 when sell-setup-9 active in last 21d AND D-wave streak >= 5 AND close near 1260d max."""
    fire = (_td_sell_setup_count(close) == 9).astype(float).rolling(MDAYS, min_periods=1).max()
    wave = (_td_d_wave_higher_high_streak_21(close) >= 5).astype(float)
    near = (close >= close.rolling(DDAYS_5Y, min_periods=YDAYS).max() * 0.98).astype(float)
    return (fire * wave * near).where(fire.notna() & wave.notna() & near.notna(), np.nan)


def f34_tdsq_291_setup_9_x_close_pct_rank_1260d_top_5pct(close: pd.Series) -> pd.Series:
    """+1 when sell-setup-9 fires AND close-pct-rank-1260d > 0.95 (top 5% of 5y)."""
    fire = (_td_sell_setup_count(close) == 9).astype(float)
    rk = _pct_rank(close, DDAYS_5Y)
    return ((fire == 1) & (rk > 0.95)).astype(float).where(fire.notna() & rk.notna(), np.nan)


def f34_tdsq_292_td_d_wave_5_x_at_1260d_high_indicator(close: pd.Series) -> pd.Series:
    """+1 when bullish-wave streak >= 5 AND close within 2% of 1260d max."""
    s = _td_d_wave_higher_high_streak_21(close)
    near = (close >= close.rolling(DDAYS_5Y, min_periods=YDAYS).max() * 0.98).astype(float)
    return ((s >= 5) & (near == 1)).astype(float).where(s.notna() & near.notna(), np.nan)


def f34_tdsq_293_waldo_x_close_at_1260d_high_count_252d(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of Waldo-pattern firings at near-1260d-high bars in trailing 252d."""
    a = _waldo_2_bearish_event(open, close, high, low).fillna(0)
    b = _waldo_3_bearish_event(close, high, low).fillna(0)
    c = _waldo_5_bearish_event(close, high, low).fillna(0)
    near = (close >= close.rolling(DDAYS_5Y, min_periods=YDAYS).max() * 0.98).astype(float)
    return ((a + b + c) * near).rolling(YDAYS, min_periods=QDAYS).sum()


def f34_tdsq_294_poq_x_close_at_1260d_high_indicator(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+1 when POQ-sell fires AND close within 2% of 1260d max."""
    f = _td_poq_sell_event(open, high, low, close)
    near = (close >= close.rolling(DDAYS_5Y, min_periods=YDAYS).max() * 0.98).astype(float)
    return (f * near).where(f.notna() & near.notna(), np.nan)


def f34_tdsq_295_supply_line_falling_x_1260d_high_indicator(high: pd.Series, close: pd.Series) -> pd.Series:
    """+1 when 252d Supply-Line slope < 0 AND close within 2% of 1260d max."""
    s = _two_extreme_slope(high, YDAYS, "max")
    near = (close >= close.rolling(DDAYS_5Y, min_periods=YDAYS).max() * 0.98).astype(float)
    return ((s < 0) & (near == 1)).astype(float).where(s.notna() & near.notna(), np.nan)


def f34_tdsq_296_td_full_signal_breadth_x_1260d_high(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of 5 TD-pattern signals firing in last 21d AT 1260d-high (setup-9, countdown-13, POQ-sell, Waldo-3, Waldo-5)."""
    s1 = (_td_sell_setup_count(close) == 9).astype(float).rolling(MDAYS, min_periods=1).max()
    cd = _td_sell_countdown_count(close, high, low)
    s2 = ((cd == 13) & (cd.shift(1) < 13)).astype(float).rolling(MDAYS, min_periods=1).max()
    s3 = _td_poq_sell_event(open, high, low, close).fillna(0).rolling(MDAYS, min_periods=1).max()
    s4 = _waldo_3_bearish_event(close, high, low).fillna(0).rolling(MDAYS, min_periods=1).max()
    s5 = _waldo_5_bearish_event(close, high, low).fillna(0).rolling(MDAYS, min_periods=1).max()
    cnt = s1.fillna(0) + s2.fillna(0) + s3 + s4 + s5
    near = (close >= close.rolling(DDAYS_5Y, min_periods=YDAYS).max() * 0.98).astype(float)
    return cnt * near


# ============================================================
# Bucket EEEE — Master DeMark plurality composites (297-300)
# ============================================================

def f34_tdsq_297_master_demark_plurality_score_252d(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Weighted DeMark plurality (252d normalized counts):
    0.3 × setup-9 count + 0.3 × countdown-13 count + 0.2 × POQ-sell count
    + 0.1 × (Waldo-2 + Waldo-3 + Waldo-5) count + 0.1 × Anti-Differential count,
    all normalized by 252."""
    s9 = (_td_sell_setup_count(close) == 9).astype(float).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum() / YDAYS
    cd = _td_sell_countdown_count(close, high, low)
    c13 = ((cd == 13) & (cd.shift(1) < 13)).astype(float).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum() / YDAYS
    poq = _td_poq_sell_event(open, high, low, close).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum() / YDAYS
    waldo_total = (_waldo_2_bearish_event(open, close, high, low).fillna(0)
                   + _waldo_3_bearish_event(close, high, low).fillna(0)
                   + _waldo_5_bearish_event(close, high, low).fillna(0))
    w = waldo_total.rolling(YDAYS, min_periods=QDAYS).sum() / YDAYS
    # Anti-Differential proxy via inline
    pc = close.shift(1); ppc = close.shift(2); plow = low.shift(1); pplow = low.shift(2); phigh = high.shift(1)
    anti = ((pc > ppc) & (close < pc) & ((pc - plow) > (ppc - pplow)) & ((high - close) > (phigh - pc))).astype(float).fillna(0)
    a = anti.rolling(YDAYS, min_periods=QDAYS).sum() / YDAYS
    return 0.3 * s9 + 0.3 * c13 + 0.2 * poq + 0.1 * w + 0.1 * a


def f34_tdsq_298_master_demark_topping_score_zscore_252d(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score (over 252d) of master DeMark plurality (297)."""
    return _rolling_zscore(f34_tdsq_297_master_demark_plurality_score_252d(open, close, high, low), YDAYS)


def f34_tdsq_299_master_demark_signal_breadth_5d_indicator(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when AT LEAST 3 of 5 TD-pattern signals fired in last 5d (broad-front DeMark topping)."""
    s1 = (_td_sell_setup_count(close) == 9).astype(float).fillna(0).rolling(WDAYS, min_periods=1).max()
    cd = _td_sell_countdown_count(close, high, low)
    s2 = ((cd == 13) & (cd.shift(1) < 13)).astype(float).fillna(0).rolling(WDAYS, min_periods=1).max()
    s3 = _td_poq_sell_event(open, high, low, close).fillna(0).rolling(WDAYS, min_periods=1).max()
    s4 = _waldo_3_bearish_event(close, high, low).fillna(0).rolling(WDAYS, min_periods=1).max()
    s5 = _waldo_5_bearish_event(close, high, low).fillna(0).rolling(WDAYS, min_periods=1).max()
    return ((s1 + s2 + s3 + s4 + s5) >= 3).astype(float)


def f34_tdsq_300_master_demark_topping_x_at_1260d_high_indicator(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when master DeMark z-score (over 252d) > 1.0 AND close within 2% of 1260d max."""
    z = f34_tdsq_298_master_demark_topping_score_zscore_252d(open, close, high, low)
    near = (close >= close.rolling(DDAYS_5Y, min_periods=YDAYS).max() * 0.98).astype(float)
    return ((z > 1.0) & (near == 1)).astype(float).where(z.notna() & near.notna(), np.nan)


# ============================================================
# REGISTRY
# ============================================================

TD_SEQUENTIAL_DEMARK_BASE_REGISTRY_226_300 = {
    "f34_tdsq_226_td_d_wave_higher_high_streak_21d": {"inputs": ["close"], "func": f34_tdsq_226_td_d_wave_higher_high_streak_21d},
    "f34_tdsq_227_td_d_wave_lower_low_streak_21d": {"inputs": ["close"], "func": f34_tdsq_227_td_d_wave_lower_low_streak_21d},
    "f34_tdsq_228_td_d_wave_max_higher_high_streak_252d": {"inputs": ["close"], "func": f34_tdsq_228_td_d_wave_max_higher_high_streak_252d},
    "f34_tdsq_229_td_d_wave_count_completions_252d": {"inputs": ["close"], "func": f34_tdsq_229_td_d_wave_count_completions_252d},
    "f34_tdsq_230_td_d_wave_5wave_indicator": {"inputs": ["close"], "func": f34_tdsq_230_td_d_wave_5wave_indicator},
    "f34_tdsq_231_td_d_wave_pct_rank_streak_252d": {"inputs": ["close"], "func": f34_tdsq_231_td_d_wave_pct_rank_streak_252d},
    "f34_tdsq_232_td_d_wave_amplitude_252d": {"inputs": ["close"], "func": f34_tdsq_232_td_d_wave_amplitude_252d},
    "f34_tdsq_233_td_d_wave_exhaustion_indicator": {"inputs": ["close"], "func": f34_tdsq_233_td_d_wave_exhaustion_indicator},
    "f34_tdsq_234_td_d_wave_bearish_streak_acceleration_indicator": {"inputs": ["close"], "func": f34_tdsq_234_td_d_wave_bearish_streak_acceleration_indicator},
    "f34_tdsq_235_td_d_wave_segment_count_504d": {"inputs": ["close"], "func": f34_tdsq_235_td_d_wave_segment_count_504d},
    "f34_tdsq_236_td_supply_line_slope_63d": {"inputs": ["high"], "func": f34_tdsq_236_td_supply_line_slope_63d},
    "f34_tdsq_237_td_supply_line_slope_252d": {"inputs": ["high"], "func": f34_tdsq_237_td_supply_line_slope_252d},
    "f34_tdsq_238_td_demand_line_slope_63d": {"inputs": ["low"], "func": f34_tdsq_238_td_demand_line_slope_63d},
    "f34_tdsq_239_td_demand_line_slope_252d": {"inputs": ["low"], "func": f34_tdsq_239_td_demand_line_slope_252d},
    "f34_tdsq_240_td_supply_line_falling_indicator_63d": {"inputs": ["high"], "func": f34_tdsq_240_td_supply_line_falling_indicator_63d},
    "f34_tdsq_241_td_supply_line_rising_x_at_252d_high_indicator": {"inputs": ["high", "close"], "func": f34_tdsq_241_td_supply_line_rising_x_at_252d_high_indicator},
    "f34_tdsq_242_supply_minus_demand_slope_diff_63d": {"inputs": ["high", "low"], "func": f34_tdsq_242_supply_minus_demand_slope_diff_63d},
    "f34_tdsq_243_td_lines_channel_converging_indicator_63d": {"inputs": ["high", "low"], "func": f34_tdsq_243_td_lines_channel_converging_indicator_63d},
    "f34_tdsq_244_td_supply_line_break_event_indicator": {"inputs": ["high", "low", "close"], "func": f34_tdsq_244_td_supply_line_break_event_indicator},
    "f34_tdsq_245_td_demand_line_break_event_indicator": {"inputs": ["close", "low"], "func": f34_tdsq_245_td_demand_line_break_event_indicator},
    "f34_tdsq_246_td_channel_1_upper": {"inputs": ["high"], "func": f34_tdsq_246_td_channel_1_upper},
    "f34_tdsq_247_td_channel_1_lower": {"inputs": ["low"], "func": f34_tdsq_247_td_channel_1_lower},
    "f34_tdsq_248_close_position_in_td_channel_1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_248_close_position_in_td_channel_1},
    "f34_tdsq_249_close_at_td_channel_1_upper_indicator": {"inputs": ["close", "high"], "func": f34_tdsq_249_close_at_td_channel_1_upper_indicator},
    "f34_tdsq_250_td_channel_2_upper": {"inputs": ["high"], "func": f34_tdsq_250_td_channel_2_upper},
    "f34_tdsq_251_td_channel_2_lower": {"inputs": ["low"], "func": f34_tdsq_251_td_channel_2_lower},
    "f34_tdsq_252_close_position_in_td_channel_2": {"inputs": ["close", "high", "low"], "func": f34_tdsq_252_close_position_in_td_channel_2},
    "f34_tdsq_253_td_channel_persistence_at_upper_21d": {"inputs": ["close", "high"], "func": f34_tdsq_253_td_channel_persistence_at_upper_21d},
    "f34_tdsq_254_td_waldo_2_bearish_event_indicator": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_254_td_waldo_2_bearish_event_indicator},
    "f34_tdsq_255_td_waldo_2_count_252d": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_255_td_waldo_2_count_252d},
    "f34_tdsq_256_td_waldo_3_bearish_event_indicator": {"inputs": ["close", "high", "low"], "func": f34_tdsq_256_td_waldo_3_bearish_event_indicator},
    "f34_tdsq_257_td_waldo_3_count_252d": {"inputs": ["close", "high", "low"], "func": f34_tdsq_257_td_waldo_3_count_252d},
    "f34_tdsq_258_td_waldo_5_bearish_event_indicator": {"inputs": ["close", "high", "low"], "func": f34_tdsq_258_td_waldo_5_bearish_event_indicator},
    "f34_tdsq_259_td_waldo_5_count_252d": {"inputs": ["close", "high", "low"], "func": f34_tdsq_259_td_waldo_5_count_252d},
    "f34_tdsq_260_td_waldo_breadth_3patterns_indicator": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_260_td_waldo_breadth_3patterns_indicator},
    "f34_tdsq_261_td_waldo_x_at_252d_high_count_252d": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_261_td_waldo_x_at_252d_high_count_252d},
    "f34_tdsq_262_td_poq_sell_event_indicator": {"inputs": ["open", "high", "low", "close"], "func": f34_tdsq_262_td_poq_sell_event_indicator},
    "f34_tdsq_263_td_poq_sell_count_252d": {"inputs": ["open", "high", "low", "close"], "func": f34_tdsq_263_td_poq_sell_count_252d},
    "f34_tdsq_264_days_since_td_poq_sell": {"inputs": ["open", "high", "low", "close"], "func": f34_tdsq_264_days_since_td_poq_sell},
    "f34_tdsq_265_td_poq_sell_x_close_at_252d_high_indicator": {"inputs": ["open", "high", "low", "close"], "func": f34_tdsq_265_td_poq_sell_x_close_at_252d_high_indicator},
    "f34_tdsq_266_td_poq_sell_count_63d": {"inputs": ["open", "high", "low", "close"], "func": f34_tdsq_266_td_poq_sell_count_63d},
    "f34_tdsq_267_td_poq_sell_count_at_high_252d": {"inputs": ["open", "high", "low", "close"], "func": f34_tdsq_267_td_poq_sell_count_at_high_252d},
    "f34_tdsq_268_td_roc_13d_pct": {"inputs": ["close"], "func": f34_tdsq_268_td_roc_13d_pct},
    "f34_tdsq_269_td_roc_13d_zscore_252d": {"inputs": ["close"], "func": f34_tdsq_269_td_roc_13d_zscore_252d},
    "f34_tdsq_270_td_roc_13d_above_threshold_indicator": {"inputs": ["close"], "func": f34_tdsq_270_td_roc_13d_above_threshold_indicator},
    "f34_tdsq_271_td_roc_25d_value": {"inputs": ["close"], "func": f34_tdsq_271_td_roc_25d_value},
    "f34_tdsq_272_td_roc_13d_slope_div_sign_63d": {"inputs": ["close"], "func": f34_tdsq_272_td_roc_13d_slope_div_sign_63d},
    "f34_tdsq_273_td_roc_extreme_persistence_21d": {"inputs": ["close"], "func": f34_tdsq_273_td_roc_extreme_persistence_21d},
    "f34_tdsq_274_td_relative_retracement_38pct_level": {"inputs": ["high", "low"], "func": f34_tdsq_274_td_relative_retracement_38pct_level},
    "f34_tdsq_275_td_relative_retracement_62pct_level": {"inputs": ["high", "low"], "func": f34_tdsq_275_td_relative_retracement_62pct_level},
    "f34_tdsq_276_close_above_td_retracement_62pct_indicator": {"inputs": ["high", "low", "close"], "func": f34_tdsq_276_close_above_td_retracement_62pct_indicator},
    "f34_tdsq_277_close_distance_to_td_retracement_62pct_atr_norm": {"inputs": ["high", "low", "close"], "func": f34_tdsq_277_close_distance_to_td_retracement_62pct_atr_norm},
    "f34_tdsq_278_td_absolute_retracement_38_x_swing_lookback_504d": {"inputs": ["high", "low"], "func": f34_tdsq_278_td_absolute_retracement_38_x_swing_lookback_504d},
    "f34_tdsq_279_td_absolute_retracement_62_x_swing_lookback_504d": {"inputs": ["high", "low"], "func": f34_tdsq_279_td_absolute_retracement_62_x_swing_lookback_504d},
    "f34_tdsq_280_close_position_in_252d_swing_range": {"inputs": ["close", "high", "low"], "func": f34_tdsq_280_close_position_in_252d_swing_range},
    "f34_tdsq_281_close_position_in_1260d_swing_range": {"inputs": ["close", "high", "low"], "func": f34_tdsq_281_close_position_in_1260d_swing_range},
    "f34_tdsq_282_td_ma_1_value": {"inputs": ["close"], "func": f34_tdsq_282_td_ma_1_value},
    "f34_tdsq_283_td_ma_2_value": {"inputs": ["close"], "func": f34_tdsq_283_td_ma_2_value},
    "f34_tdsq_284_close_above_td_ma_2_indicator": {"inputs": ["close"], "func": f34_tdsq_284_close_above_td_ma_2_indicator},
    "f34_tdsq_285_td_ma_1_minus_td_ma_2_diff_atr_norm": {"inputs": ["close", "high", "low"], "func": f34_tdsq_285_td_ma_1_minus_td_ma_2_diff_atr_norm},
    "f34_tdsq_286_td_ma_bearish_cross_event_indicator": {"inputs": ["close"], "func": f34_tdsq_286_td_ma_bearish_cross_event_indicator},
    "f34_tdsq_287_setup_9_x_close_at_1260d_high_indicator": {"inputs": ["close"], "func": f34_tdsq_287_setup_9_x_close_at_1260d_high_indicator},
    "f34_tdsq_288_setup_9_within_21d_x_close_at_1260d_high_indicator": {"inputs": ["close"], "func": f34_tdsq_288_setup_9_within_21d_x_close_at_1260d_high_indicator},
    "f34_tdsq_289_countdown_13_x_close_at_1260d_high_indicator": {"inputs": ["close", "high", "low"], "func": f34_tdsq_289_countdown_13_x_close_at_1260d_high_indicator},
    "f34_tdsq_290_setup_x_d_wave_x_1260d_high_triple_indicator": {"inputs": ["close"], "func": f34_tdsq_290_setup_x_d_wave_x_1260d_high_triple_indicator},
    "f34_tdsq_291_setup_9_x_close_pct_rank_1260d_top_5pct": {"inputs": ["close"], "func": f34_tdsq_291_setup_9_x_close_pct_rank_1260d_top_5pct},
    "f34_tdsq_292_td_d_wave_5_x_at_1260d_high_indicator": {"inputs": ["close"], "func": f34_tdsq_292_td_d_wave_5_x_at_1260d_high_indicator},
    "f34_tdsq_293_waldo_x_close_at_1260d_high_count_252d": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_293_waldo_x_close_at_1260d_high_count_252d},
    "f34_tdsq_294_poq_x_close_at_1260d_high_indicator": {"inputs": ["open", "high", "low", "close"], "func": f34_tdsq_294_poq_x_close_at_1260d_high_indicator},
    "f34_tdsq_295_supply_line_falling_x_1260d_high_indicator": {"inputs": ["high", "close"], "func": f34_tdsq_295_supply_line_falling_x_1260d_high_indicator},
    "f34_tdsq_296_td_full_signal_breadth_x_1260d_high": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_296_td_full_signal_breadth_x_1260d_high},
    "f34_tdsq_297_master_demark_plurality_score_252d": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_297_master_demark_plurality_score_252d},
    "f34_tdsq_298_master_demark_topping_score_zscore_252d": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_298_master_demark_topping_score_zscore_252d},
    "f34_tdsq_299_master_demark_signal_breadth_5d_indicator": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_299_master_demark_signal_breadth_5d_indicator},
    "f34_tdsq_300_master_demark_topping_x_at_1260d_high_indicator": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_300_master_demark_topping_x_at_1260d_high_indicator},
}
