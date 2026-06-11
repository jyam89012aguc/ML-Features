"""ma_crossover_failure_dynamics d2 features 151-225 - Pipeline 1b-technical.

75 NEW distinct hypotheses extending the mcxf family with gap-fill features focused on
crossover quality magnitudes, multi-MA simultaneity, hysteresis-filtered crossovers,
failed-crossover sequence analysis, post-crossover momentum decay, slope-vs-slope
crossovers, Ichimoku Tenkan/Kijun/Senkou crossovers, adaptive-MA crossovers, and
regime-conditioned crossovers.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
NO centered windows, NO .shift(N) anywhere. Self-contained helpers - no cross-family imports.
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


def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat(
        [
            (high - low).rename("hl"),
            (high - pc).abs().rename("hpc"),
            (low - pc).abs().rename("lpc"),
        ],
        axis=1,
    ).max(axis=1)


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
        xm = x.mean()
        wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan

    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


def _sma(s, n, mp=None):
    if mp is None:
        mp = max(n // 3, 2)
    return s.rolling(n, min_periods=mp).mean()


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=max(n // 3, 2)).mean()


def _wma(s, n):
    w_full = np.arange(1, n + 1, dtype=float)

    def _f(x):
        valid = ~np.isnan(x)
        if valid.sum() < max(n // 3, 2):
            return np.nan
        if len(x) >= n:
            w = w_full
        else:
            w = w_full[-len(x):]
        xx = np.where(valid, x, 0.0)
        ww = np.where(valid, w[-len(x):], 0.0)
        ws = ww.sum()
        if ws == 0:
            return np.nan
        return float((xx * ww).sum() / ws)

    return s.rolling(n, min_periods=max(n // 3, 2)).apply(_f, raw=True)


def _hma(s, n):
    half = max(int(n / 2), 2)
    sqrtn = max(int(np.sqrt(n)), 2)
    wma_half = _wma(s, half)
    wma_full = _wma(s, n)
    return _wma(2.0 * wma_half - wma_full, sqrtn)


def _alma(s, n, sigma=6.0, offset=0.85):
    m = offset * (n - 1)
    w_full = np.exp(-((np.arange(n) - m) ** 2) / (2 * (n / sigma) ** 2))

    def _f(x):
        valid = ~np.isnan(x)
        if valid.sum() < max(n // 3, 2):
            return np.nan
        # align weights to actual window length (right-anchored: keep tail of w)
        if len(x) >= n:
            w = w_full
        else:
            w = w_full[-len(x):]
        xx = np.where(valid, x, 0.0)
        ww = np.where(valid, w[-len(x):], 0.0)
        ws = ww.sum()
        if ws == 0:
            return np.nan
        return float((xx * ww).sum() / ws)

    return s.rolling(n, min_periods=max(n // 3, 2)).apply(_f, raw=True)


def _vidya(s, n, cmo_n=9):
    """Chande's Variable Index Dynamic Average - VMA based on CMO absolute value."""
    diff = s.diff()
    up = diff.clip(lower=0.0).rolling(cmo_n, min_periods=max(cmo_n // 2, 2)).sum()
    dn = (-diff.clip(upper=0.0)).rolling(cmo_n, min_periods=max(cmo_n // 2, 2)).sum()
    denom = (up + dn).replace(0, np.nan)
    cmo_abs = ((up - dn) / denom).abs().fillna(0.0)
    alpha_base = 2.0 / (n + 1)
    alpha = (alpha_base * cmo_abs).clip(0.001, 1.0)
    arr = s.values
    a_arr = alpha.values
    out = np.full(len(arr), np.nan, dtype=float)
    prev = np.nan
    initialized = False
    for i in range(len(arr)):
        v = arr[i]
        if np.isnan(v):
            continue
        if not initialized:
            prev = float(v)
            initialized = True
            out[i] = prev
        else:
            a = float(a_arr[i]) if not np.isnan(a_arr[i]) else alpha_base
            prev = a * float(v) + (1.0 - a) * prev
            out[i] = prev
    return pd.Series(out, index=s.index)


def _jma(s, n, phase=0.0):
    """Jurik Moving Average (Mark Jurik's adaptive MA, simplified canonical form)."""
    arr = s.values
    out = np.full(len(arr), np.nan, dtype=float)
    beta = 0.45 * (n - 1) / (0.45 * (n - 1) + 2.0)
    pr = 0.5 if phase < -100 else (2.5 if phase > 100 else (phase / 100.0 + 1.5))
    alpha = beta ** pr
    e0 = e1 = e2 = jma_prev = np.nan
    initialized = False
    for i in range(len(arr)):
        v = arr[i]
        if np.isnan(v):
            continue
        if not initialized:
            e0 = e1 = e2 = jma_prev = float(v)
            initialized = True
            out[i] = jma_prev
        else:
            e0_new = (1.0 - alpha) * float(v) + alpha * e0
            e1_new = (float(v) - e0_new) * (1.0 - beta) + beta * e1
            e2_new = (e0_new + pr * e1_new - jma_prev) * (1.0 - alpha) ** 2 + (alpha ** 2) * e2
            jma_new = e2_new + jma_prev
            out[i] = jma_new
            e0, e1, e2, jma_prev = e0_new, e1_new, e2_new, jma_new
    return pd.Series(out, index=s.index)


def _bull_cross_events(a: pd.Series, b: pd.Series) -> pd.Series:
    """True at bars where a crosses ABOVE b (bullish cross). Bool series."""
    diff = (a - b)
    curr_above = diff > 0
    prev_above = curr_above.shift(1).fillna(False).astype(bool)
    return (curr_above & ~prev_above).fillna(False)


def _bear_cross_events(a: pd.Series, b: pd.Series) -> pd.Series:
    """True at bars where a crosses BELOW b (bearish cross). Bool series."""
    diff = (a - b)
    curr_below = diff < 0
    prev_below = curr_below.shift(1).fillna(False).astype(bool)
    return (curr_below & ~prev_below).fillna(False)


def _any_cross_events(a: pd.Series, b: pd.Series) -> pd.Series:
    """True at bars where a crosses through b (either direction)."""
    return (_bull_cross_events(a, b) | _bear_cross_events(a, b)).fillna(False)


def _last_event_value(value: pd.Series, event: pd.Series) -> pd.Series:
    """Forward-fill the value sampled at the most recent True event. NaN before first event."""
    masked = value.where(event.fillna(False))
    return masked.ffill()


def _bars_since_event(event: pd.Series) -> pd.Series:
    """Bars since the most recent True event. NaN before first event."""
    arr = event.fillna(False).values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=event.index)


def _consecutive_true_streak(b: pd.Series) -> pd.Series:
    """Length of current run of True. NaN-aware: NaN breaks streak to NaN."""
    arr = b.astype("float").values
    out = np.full(len(arr), np.nan, dtype=float)
    run = 0
    for i in range(len(arr)):
        v = arr[i]
        if np.isnan(v):
            run = 0
            out[i] = np.nan
        elif v > 0.5:
            run += 1
            out[i] = float(run)
        else:
            run = 0
            out[i] = 0.0
    return pd.Series(out, index=b.index)


def _max_streak_in_window(b: pd.Series, window: int) -> pd.Series:
    """Rolling maximum of the current True-run lengths over `window` bars."""
    streak = _consecutive_true_streak(b.fillna(False).astype(bool))
    return streak.rolling(window, min_periods=max(window // 3, 2)).max()


def _tenkan(high, low, n=9):
    return (high.rolling(n, min_periods=max(n // 2, 2)).max()
            + low.rolling(n, min_periods=max(n // 2, 2)).min()) / 2.0


def _kijun(high, low, n=26):
    return (high.rolling(n, min_periods=max(n // 2, 2)).max()
            + low.rolling(n, min_periods=max(n // 2, 2)).min()) / 2.0


def _senkou_a(high, low, n1=9, n2=26):
    # PIT-clean: use UNshifted current value (do NOT project forward).
    return (_tenkan(high, low, n1) + _kijun(high, low, n2)) / 2.0


def _senkou_b(high, low, n=52):
    # PIT-clean: unshifted current value.
    return (high.rolling(n, min_periods=max(n // 2, 2)).max()
            + low.rolling(n, min_periods=max(n // 2, 2)).min()) / 2.0


def f13_mcxf_151_sma50_200_crossover_magnitude_at_event_atr_d2(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """|sma50 - sma200| / ATR21 sampled at the bar of each sma50/200 cross event, ffilled."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    atr = _atr(high, low, close, 21)
    mag = _safe_div((fast - slow).abs(), atr)
    event = _any_cross_events(fast, slow)
    return (_last_event_value(mag, event)).diff().diff()


def f13_mcxf_152_ema21_50_crossover_magnitude_at_event_atr_d2(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """|ema21 - ema50| / ATR21 captured at each ema21/50 cross bar, ffilled."""
    fast = _ema(close, 21)
    slow = _ema(close, 50)
    atr = _atr(high, low, close, 21)
    mag = _safe_div((fast - slow).abs(), atr)
    event = _any_cross_events(fast, slow)
    return (_last_event_value(mag, event)).diff().diff()


def f13_mcxf_153_sma100_200_crossover_magnitude_at_event_atr_d2(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """|sma100 - sma200| / ATR21 captured at each sma100/200 cross bar, ffilled."""
    fast = _sma(close, 100)
    slow = _sma(close, 200)
    atr = _atr(high, low, close, 21)
    mag = _safe_div((fast - slow).abs(), atr)
    event = _any_cross_events(fast, slow)
    return (_last_event_value(mag, event)).diff().diff()


def f13_mcxf_154_crossover_slope_quality_sma50_200_d2(close: pd.Series) -> pd.Series:
    """5d log-slope of FAST sma50 at sma50/200 cross bars, ffilled - cross initiation steepness."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    slope = _rolling_slope(_safe_log(fast.replace(0, np.nan)), WDAYS)
    event = _any_cross_events(fast, slow)
    return (_last_event_value(slope, event)).diff().diff()


def f13_mcxf_155_crossover_volume_zscore_at_event_sma50_200_d2(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """252d z-score of volume sampled at each sma50/200 cross bar, ffilled - cross participation."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    vz = _rolling_zscore(volume.astype(float), YDAYS)
    event = _any_cross_events(fast, slow)
    return (_last_event_value(vz, event)).diff().diff()


def f13_mcxf_156_crossover_close_distance_to_intersection_atr_units_d2(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """|close - midpoint(sma50, sma200)| / ATR21 at sma50/200 cross bars - price location vs MA intersection."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    mid = (fast + slow) / 2.0
    atr = _atr(high, low, close, 21)
    d = _safe_div((close - mid).abs(), atr)
    event = _any_cross_events(fast, slow)
    return (_last_event_value(d, event)).diff().diff()


def f13_mcxf_157_crossover_durability_score_sma50_200_d2(close: pd.Series) -> pd.Series:
    """Bars-since-last-cross / mean-bars-between-crosses(252d) for sma50/200 - persistence ratio."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    event = _any_cross_events(fast, slow)
    bars_since = _bars_since_event(event)
    cnt = event.astype(float).rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()
    mean_cycle = _safe_div(pd.Series(float(YDAYS), index=close.index), cnt)
    return (_safe_div(bars_since, mean_cycle)).diff().diff()


def f13_mcxf_158_magnitude_decay_post_crossover_5d_sma50_200_d2(close: pd.Series) -> pd.Series:
    """Change in log|sma50-sma200| from cross bar to 5 bars later, sampled at cross bars then ffilled."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    spread = (fast - slow).abs().replace(0, np.nan)
    log_spread = _safe_log(spread)
    # decay = log_spread(t) - log_spread(t-5)  [PIT: backward shift only]
    decay = log_spread - log_spread.shift(5)
    event = _any_cross_events(fast, slow).shift(5).fillna(False).astype(bool)
    # event shifted FORWARD (i.e., past event) - we record decay observed 5 bars after a past cross
    return (_last_event_value(decay, event)).diff().diff()


def f13_mcxf_159_crossover_atr_normalized_separation_now_sma50_200_d2(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """Current |sma50 - sma200| / ATR21 (continuous) - separation expressed in ATR units, not event-sampled."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    atr = _atr(high, low, close, 21)
    return (_safe_div((fast - slow).abs(), atr)).diff().diff()


def f13_mcxf_160_crossover_quality_composite_sma50_200_d2(
    high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series
) -> pd.Series:
    """Composite cross quality: 0.5*z(slope) + 0.3*z(volume) + 0.2*z(|spread|/ATR) sampled at sma50/200 crosses."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    atr = _atr(high, low, close, 21)
    slope = _rolling_slope(_safe_log(fast.replace(0, np.nan)), MDAYS)
    spread_atr = _safe_div((fast - slow).abs(), atr)
    vz = _rolling_zscore(volume.astype(float), YDAYS)
    sl_z = _rolling_zscore(slope, YDAYS)
    sp_z = _rolling_zscore(spread_atr, YDAYS)
    comp = 0.5 * sl_z + 0.3 * vz + 0.2 * sp_z
    event = _any_cross_events(fast, slow)
    return (_last_event_value(comp, event)).diff().diff()


def f13_mcxf_161_triple_ma_bullish_alignment_event_count_252d_d2(close: pd.Series) -> pd.Series:
    """252d count of bars where sma50>sma100>sma200 alignment is newly achieved."""
    s50 = _sma(close, 50)
    s100 = _sma(close, 100)
    s200 = _sma(close, 200)
    aligned = (s50 > s100) & (s100 > s200)
    new_alignment = aligned & ~aligned.shift(1).fillna(False).astype(bool)
    return (new_alignment.astype(float).rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()).diff().diff()


def f13_mcxf_162_triple_ma_bearish_alignment_event_count_252d_d2(close: pd.Series) -> pd.Series:
    """252d count of bars where sma50<sma100<sma200 alignment is newly achieved."""
    s50 = _sma(close, 50)
    s100 = _sma(close, 100)
    s200 = _sma(close, 200)
    aligned = (s50 < s100) & (s100 < s200)
    new_alignment = aligned & ~aligned.shift(1).fillna(False).astype(bool)
    return (new_alignment.astype(float).rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()).diff().diff()


def f13_mcxf_163_quad_ma_simultaneous_crossover_count_252d_d2(close: pd.Series) -> pd.Series:
    """252d count of bars where ANY cross happens in >=2 of {sma20/50, sma50/100, sma50/200, sma100/200} same day."""
    pairs = [(20, 50), (50, 100), (50, 200), (100, 200)]
    events = []
    for a, b in pairs:
        events.append(_any_cross_events(_sma(close, a), _sma(close, b)).astype(int))
    df = pd.concat(events, axis=1).fillna(0)
    multi = (df.sum(axis=1) >= 2).astype(float)
    return (multi.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()).diff().diff()


def f13_mcxf_164_multi_ma_crossover_density_63d_d2(close: pd.Series) -> pd.Series:
    """63d total cross-event count across 4 MA pairs - crossover density measure."""
    pairs = [(20, 50), (50, 100), (50, 200), (100, 200)]
    total = pd.Series(0.0, index=close.index)
    for a, b in pairs:
        total = total + _any_cross_events(_sma(close, a), _sma(close, b)).astype(float)
    return (total.rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).sum()).diff().diff()


def f13_mcxf_165_crossover_breadth_bullish_21d_d2(close: pd.Series) -> pd.Series:
    """In a rolling 21d window, count how many of 4 MA pairs had a BULLISH cross - breadth score."""
    pairs = [(20, 50), (50, 100), (50, 200), (100, 200)]
    breadths = []
    for a, b in pairs:
        ev = _bull_cross_events(_sma(close, a), _sma(close, b)).astype(float)
        had = (ev.rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).sum() > 0).astype(float)
        breadths.append(had.rename(f"p{a}_{b}"))
    return (pd.concat(breadths, axis=1).sum(axis=1)).diff().diff()


def f13_mcxf_166_crossover_breadth_bearish_21d_d2(close: pd.Series) -> pd.Series:
    """In a rolling 21d window, count how many of 4 MA pairs had a BEARISH cross - bearish breadth score."""
    pairs = [(20, 50), (50, 100), (50, 200), (100, 200)]
    breadths = []
    for a, b in pairs:
        ev = _bear_cross_events(_sma(close, a), _sma(close, b)).astype(float)
        had = (ev.rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).sum() > 0).astype(float)
        breadths.append(had.rename(f"p{a}_{b}"))
    return (pd.concat(breadths, axis=1).sum(axis=1)).diff().diff()


def f13_mcxf_167_crossover_breadth_bullish_to_bearish_transition_event_d2(
    close: pd.Series,
) -> pd.Series:
    """Indicator: bullish breadth(21d) > 0 yesterday AND bearish breadth(21d) > 0 today - regime flip detected."""
    pairs = [(20, 50), (50, 100), (50, 200), (100, 200)]
    bull = pd.Series(0.0, index=close.index)
    bear = pd.Series(0.0, index=close.index)
    for a, b in pairs:
        bull = bull + _bull_cross_events(_sma(close, a), _sma(close, b)).astype(float)
        bear = bear + _bear_cross_events(_sma(close, a), _sma(close, b)).astype(float)
    bull_in_21 = bull.rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).sum() > 0
    bear_in_21 = bear.rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).sum() > 0
    return ((bull_in_21.shift(1).fillna(False) & bear_in_21).astype(float)).diff().diff()


def f13_mcxf_168_crossover_simultaneity_window_min_bars_d2(close: pd.Series) -> pd.Series:
    """For each bar, min bars-since-last-cross across 4 pairs - smallest cross still 'fresh'."""
    pairs = [(20, 50), (50, 100), (50, 200), (100, 200)]
    cols = []
    for a, b in pairs:
        ev = _any_cross_events(_sma(close, a), _sma(close, b))
        cols.append(_bars_since_event(ev).rename(f"p{a}_{b}"))
    return (pd.concat(cols, axis=1).min(axis=1)).diff().diff()


def _hysteresis_cross_events(a: pd.Series, b: pd.Series, n_bars: int) -> pd.Series:
    """Cross event only if a-b stays on the new side for n_bars consecutive bars."""
    diff = (a - b)
    above = (diff > 0).astype(float)
    below = (diff < 0).astype(float)
    above_streak = above.rolling(n_bars, min_periods=n_bars).sum()
    below_streak = below.rolling(n_bars, min_periods=n_bars).sum()
    confirmed_above = above_streak >= n_bars
    confirmed_below = below_streak >= n_bars
    # transition event = newly confirmed in either direction (relative to previous confirmation state)
    state = pd.Series(0, index=a.index, dtype=int)
    state = state.where(~confirmed_above, 1)
    state = state.where(~confirmed_below, -1)
    # forward-fill confirmation state
    state_ff = state.replace(0, np.nan).ffill().fillna(0)
    flip = (state_ff != state_ff.shift(1).fillna(0)) & (state_ff != 0)
    return flip.fillna(False)


def f13_mcxf_169_sma50_200_hysteresis_3bar_crossover_count_252d_d2(close: pd.Series) -> pd.Series:
    """252d count of sma50/200 crosses confirmed by 3-bar persistence beyond cross."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    ev = _hysteresis_cross_events(fast, slow, 3).astype(float)
    return (ev.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()).diff().diff()


def f13_mcxf_170_sma50_200_hysteresis_5bar_crossover_count_252d_d2(close: pd.Series) -> pd.Series:
    """252d count of sma50/200 crosses confirmed by 5-bar persistence beyond cross."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    ev = _hysteresis_cross_events(fast, slow, 5).astype(float)
    return (ev.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()).diff().diff()


def f13_mcxf_171_ema21_50_hysteresis_3bar_crossover_count_252d_d2(close: pd.Series) -> pd.Series:
    """252d count of ema21/50 crosses confirmed by 3-bar persistence beyond cross."""
    fast = _ema(close, 21)
    slow = _ema(close, 50)
    ev = _hysteresis_cross_events(fast, slow, 3).astype(float)
    return (ev.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()).diff().diff()


def f13_mcxf_172_hysteresis_filtered_recross_frequency_252d_d2(close: pd.Series) -> pd.Series:
    """Ratio: hysteresis-3bar cross count / raw cross count for sma50/200 over 252d - whipsaw filter strength."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    raw = _any_cross_events(fast, slow).astype(float).rolling(
        YDAYS, min_periods=max(YDAYS // 3, 2)
    ).sum()
    hys = _hysteresis_cross_events(fast, slow, 3).astype(float).rolling(
        YDAYS, min_periods=max(YDAYS // 3, 2)
    ).sum()
    return (_safe_div(hys, raw)).diff().diff()


def f13_mcxf_173_hysteresis_validated_crossover_failure_count_252d_d2(close: pd.Series) -> pd.Series:
    """Count of hysteresis-3bar validated sma50/200 crosses that later reverse within 21d (failure)."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    ev = _hysteresis_cross_events(fast, slow, 3)
    # at each event, record direction sign; check if direction reverses within next 21 bars
    diff = (fast - slow)
    sign_at_event = np.sign(diff).where(ev)
    # reverse = sign in [t+1..t+21] flips - PIT-clean: backward-look from t+21 perspective
    # We sample retrospectively: a confirmed event at t is "failed" if at t (i.e., now) the sign now != sign_at_event[t-21]
    sign_at_event_lag21 = sign_at_event.shift(21)
    failed_now = (np.sign(diff) != sign_at_event_lag21) & sign_at_event_lag21.notna() & (sign_at_event_lag21 != 0)
    return (failed_now.astype(float).rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()).diff().diff()


def f13_mcxf_174_atr_band_filtered_crossover_count_252d_d2(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """252d count of sma50/200 crosses where |spread| immediately clears 0.5*ATR21 band on cross bar."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    atr = _atr(high, low, close, 21)
    ev = _any_cross_events(fast, slow)
    cleared = (fast - slow).abs() >= 0.5 * atr
    valid = ev & cleared.fillna(False)
    return (valid.astype(float).rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()).diff().diff()


def f13_mcxf_175_volume_confirmed_crossover_count_252d_d2(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """252d count of sma50/200 crosses where volume on cross bar exceeds 63d mean volume."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    ev = _any_cross_events(fast, slow)
    vmean = volume.astype(float).rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).mean()
    confirmed = ev & (volume > vmean).fillna(False)
    return (confirmed.astype(float).rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()).diff().diff()


def f13_mcxf_176_hysteresis_persistence_quality_score_sma50_200_d2(close: pd.Series) -> pd.Series:
    """Average post-cross sign-persistence (sum of confirmed-side bars / window) across 63d - quality proxy."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    diff = (fast - slow)
    # streak of current sign of diff (continuous run length)
    sign = np.sign(diff).fillna(0)
    same_as_prev = (sign == sign.shift(1)).astype(float)
    # rolling mean over 63d
    return (same_as_prev.rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).mean()).diff().diff()


def _failed_cross_events(a: pd.Series, b: pd.Series, lookback: int) -> pd.Series:
    """At bar t, True if there was a bullish cross at t-lookback that has since reversed below,
    OR a bearish cross at t-lookback that has since reversed above. Sampled at t-lookback shifted to t."""
    bull = _bull_cross_events(a, b)
    bear = _bear_cross_events(a, b)
    sign_now = np.sign((a - b).fillna(0))
    # event at t-lookback: bull cross then now below (sign<0), or bear cross then now above (sign>0)
    bull_lag = bull.shift(lookback).fillna(False).astype(bool)
    bear_lag = bear.shift(lookback).fillna(False).astype(bool)
    failed = (bull_lag & (sign_now < 0)) | (bear_lag & (sign_now > 0))
    return failed.fillna(False)


def f13_mcxf_177_failed_sma50_200_crossovers_count_252d_d2(close: pd.Series) -> pd.Series:
    """252d count of sma50/200 crosses that reversed within 21d (failure event recorded at t = cross+21)."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    failed = _failed_cross_events(fast, slow, MDAYS)
    return (failed.astype(float).rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()).diff().diff()


def f13_mcxf_178_failed_ema21_50_crossovers_count_252d_d2(close: pd.Series) -> pd.Series:
    """252d count of ema21/50 crosses that reversed within 21d (failure event recorded at t = cross+21)."""
    fast = _ema(close, 21)
    slow = _ema(close, 50)
    failed = _failed_cross_events(fast, slow, MDAYS)
    return (failed.astype(float).rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()).diff().diff()


def f13_mcxf_179_failed_crossover_streak_max_252d_sma50_200_d2(close: pd.Series) -> pd.Series:
    """Max run of consecutive failed sma50/200 crosses (no successful one between) over 252d window."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    bull = _bull_cross_events(fast, slow)
    bear = _bear_cross_events(fast, slow)
    sign_now = np.sign((fast - slow).fillna(0))
    bull_lag = bull.shift(MDAYS).fillna(False).astype(bool)
    bear_lag = bear.shift(MDAYS).fillna(False).astype(bool)
    failed = (bull_lag & (sign_now < 0)) | (bear_lag & (sign_now > 0))
    succeeded = (bull_lag & (sign_now > 0)) | (bear_lag & (sign_now < 0))
    # Streak of failed without a succeed in between
    arr_f = failed.values.astype(bool)
    arr_s = succeeded.values.astype(bool)
    streak = np.zeros(len(arr_f), dtype=float)
    run = 0
    for i in range(len(arr_f)):
        if arr_s[i]:
            run = 0
        if arr_f[i]:
            run += 1
        streak[i] = float(run)
    s = pd.Series(streak, index=close.index)
    return (s.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).max()).diff().diff()


def f13_mcxf_180_mean_time_between_failed_crossovers_sma50_200_d2(close: pd.Series) -> pd.Series:
    """252d / failed-cross count for sma50/200 - mean bars between failure events."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    failed = _failed_cross_events(fast, slow, MDAYS).astype(float)
    cnt = failed.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()
    return (_safe_div(pd.Series(float(YDAYS), index=close.index), cnt)).diff().diff()


def f13_mcxf_181_failure_rate_sma50_200_504d_d2(close: pd.Series) -> pd.Series:
    """504d ratio: failed-cross count / total-cross count for sma50/200."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    raw = _any_cross_events(fast, slow).astype(float).rolling(
        DDAYS_2Y, min_periods=max(DDAYS_2Y // 3, 2)
    ).sum()
    fail = _failed_cross_events(fast, slow, MDAYS).astype(float).rolling(
        DDAYS_2Y, min_periods=max(DDAYS_2Y // 3, 2)
    ).sum()
    return (_safe_div(fail, raw)).diff().diff()


def f13_mcxf_182_failure_rate_ema21_50_504d_d2(close: pd.Series) -> pd.Series:
    """504d ratio: failed-cross count / total-cross count for ema21/50."""
    fast = _ema(close, 21)
    slow = _ema(close, 50)
    raw = _any_cross_events(fast, slow).astype(float).rolling(
        DDAYS_2Y, min_periods=max(DDAYS_2Y // 3, 2)
    ).sum()
    fail = _failed_cross_events(fast, slow, MDAYS).astype(float).rolling(
        DDAYS_2Y, min_periods=max(DDAYS_2Y // 3, 2)
    ).sum()
    return (_safe_div(fail, raw)).diff().diff()


def f13_mcxf_183_consecutive_failed_crossover_count_now_sma50_200_d2(close: pd.Series) -> pd.Series:
    """Current run of failed sma50/200 crosses (resets on a successful one)."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    bull = _bull_cross_events(fast, slow)
    bear = _bear_cross_events(fast, slow)
    sign_now = np.sign((fast - slow).fillna(0))
    bull_lag = bull.shift(MDAYS).fillna(False).astype(bool)
    bear_lag = bear.shift(MDAYS).fillna(False).astype(bool)
    failed = (bull_lag & (sign_now < 0)) | (bear_lag & (sign_now > 0))
    succeeded = (bull_lag & (sign_now > 0)) | (bear_lag & (sign_now < 0))
    arr_f = failed.values.astype(bool)
    arr_s = succeeded.values.astype(bool)
    out = np.zeros(len(arr_f), dtype=float)
    run = 0
    for i in range(len(arr_f)):
        if arr_s[i]:
            run = 0
        if arr_f[i]:
            run += 1
        out[i] = float(run)
    return (pd.Series(out, index=close.index)).diff().diff()


def f13_mcxf_184_consecutive_successful_crossover_count_now_sma50_200_d2(close: pd.Series) -> pd.Series:
    """Current run of successful sma50/200 crosses (resets on a failed one)."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    bull = _bull_cross_events(fast, slow)
    bear = _bear_cross_events(fast, slow)
    sign_now = np.sign((fast - slow).fillna(0))
    bull_lag = bull.shift(MDAYS).fillna(False).astype(bool)
    bear_lag = bear.shift(MDAYS).fillna(False).astype(bool)
    failed = (bull_lag & (sign_now < 0)) | (bear_lag & (sign_now > 0))
    succeeded = (bull_lag & (sign_now > 0)) | (bear_lag & (sign_now < 0))
    arr_f = failed.values.astype(bool)
    arr_s = succeeded.values.astype(bool)
    out = np.zeros(len(arr_f), dtype=float)
    run = 0
    for i in range(len(arr_f)):
        if arr_f[i]:
            run = 0
        if arr_s[i]:
            run += 1
        out[i] = float(run)
    return (pd.Series(out, index=close.index)).diff().diff()


def f13_mcxf_185_failure_then_extension_indicator_sma50_200_d2(close: pd.Series) -> pd.Series:
    """1 if 5d return AFTER failure event is in original (pre-failed-cross) direction, else 0; ffilled."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    bull = _bull_cross_events(fast, slow)
    bear = _bear_cross_events(fast, slow)
    sign_now = np.sign((fast - slow).fillna(0))
    bull_lag = bull.shift(MDAYS).fillna(False).astype(bool)
    bear_lag = bear.shift(MDAYS).fillna(False).astype(bool)
    failed_bull = bull_lag & (sign_now < 0)  # bull cross failed -> "original direction" had been up
    failed_bear = bear_lag & (sign_now > 0)  # bear cross failed -> "original direction" had been down
    ret5 = close - close.shift(5)
    bullext = (failed_bull & (ret5 > 0)).astype(float)
    bearext = (failed_bear & (ret5 < 0)).astype(float)
    # at failure event, code 1 if extension confirmed
    extended = bullext + bearext
    event = failed_bull | failed_bear
    return (_last_event_value(extended, event)).diff().diff()


def f13_mcxf_186_crossover_failure_clustering_index_sma50_200_d2(close: pd.Series) -> pd.Series:
    """Variance of inter-failure spacing(63d window) / squared mean - dispersion clustering (CV-squared)."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    failed = _failed_cross_events(fast, slow, MDAYS).astype(float)
    # bars-since-last-failure-event
    bars_since = _bars_since_event(failed.astype(bool))
    # rolling std vs mean
    mu = bars_since.rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).mean()
    sd = bars_since.rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).std()
    return (_safe_div(sd ** 2, mu ** 2)).diff().diff()


def f13_mcxf_187_post_golden_cross_close_above_50_streak_max_252d_d2(close: pd.Series) -> pd.Series:
    """Max consecutive bars close > sma50 after most recent sma50/200 golden cross, capped at 252d window."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    sma50 = fast
    bull = _bull_cross_events(fast, slow)
    # after each bull cross, count consecutive close>sma50 bars (until a break or new event)
    above = (close > sma50).astype(bool)
    # streak of above
    streak = _consecutive_true_streak(above)
    # at each bull cross event, capture the streak that follows - we sample bars-since-cross-where-streak-broken
    # Simpler: rolling max of streak only over post-cross period
    # Use: streak * is_post_cross_indicator (1 after last bull cross until contrarian event)
    last_bull = _bars_since_event(bull)
    valid = last_bull.notna()
    s = streak.where(valid, np.nan)
    return (s.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).max()).diff().diff()


def f13_mcxf_188_post_death_cross_close_below_50_streak_max_252d_d2(close: pd.Series) -> pd.Series:
    """Max consecutive bars close < sma50 after most recent sma50/200 death cross, capped at 252d window."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    sma50 = fast
    bear = _bear_cross_events(fast, slow)
    below = (close < sma50).astype(bool)
    streak = _consecutive_true_streak(below)
    last_bear = _bars_since_event(bear)
    valid = last_bear.notna()
    s = streak.where(valid, np.nan)
    return (s.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).max()).diff().diff()


def f13_mcxf_189_post_crossover_atr_expansion_21d_sma50_200_d2(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """ATR21 / ATR21-at-cross sampled at the most recent sma50/200 cross bar - volatility expansion ratio."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    atr = _atr(high, low, close, 21)
    event = _any_cross_events(fast, slow)
    atr_at_cross = _last_event_value(atr, event)
    return (_safe_div(atr, atr_at_cross)).diff().diff()


def f13_mcxf_190_post_crossover_volume_acceleration_21d_sma50_200_d2(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """Ratio: 21d mean volume / 21d-mean-volume-at-most-recent-sma50/200-cross."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    vmean21 = volume.astype(float).rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).mean()
    event = _any_cross_events(fast, slow)
    v_at_cross = _last_event_value(vmean21, event)
    return (_safe_div(vmean21, v_at_cross)).diff().diff()


def f13_mcxf_191_post_crossover_slope_acceleration_sma50_200_d2(close: pd.Series) -> pd.Series:
    """sma50 5d-slope / sma50 5d-slope-at-last-cross - slope acceleration since cross."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    slope5 = _rolling_slope(_safe_log(fast.replace(0, np.nan)), WDAYS)
    event = _any_cross_events(fast, slow)
    slope_at_cross = _last_event_value(slope5, event)
    return (_safe_div(slope5, slope_at_cross.replace(0, np.nan))).diff().diff()


def f13_mcxf_192_bars_to_first_retest_post_crossover_50_200_d2(close: pd.Series) -> pd.Series:
    """Bars from last sma50/200 cross to next bar where |close - sma200| <= 0.005*close (within 0.5%)."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    event = _any_cross_events(fast, slow)
    last_cross_at = _bars_since_event(event)
    retest = ((close - slow).abs() <= 0.005 * close).astype(bool)
    # bars from last cross to nearest retest at/before current bar
    bars_since_retest = _bars_since_event(retest)
    # at each bar, if there was a retest since the last cross, return cross_age - retest_age
    diff = last_cross_at - bars_since_retest
    diff = diff.where(diff >= 0, np.nan)
    # ffill only since the last cross
    return (diff).diff().diff()


def f13_mcxf_193_magnitude_of_first_retest_post_crossover_atr_sma50_200_d2(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """|close - sma200| / ATR21 evaluated at the first retest bar after a sma50/200 cross; ffilled."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    atr = _atr(high, low, close, 21)
    event = _any_cross_events(fast, slow)
    last_cross_at = _bars_since_event(event)
    retest = ((close - slow).abs() <= 0.005 * close).astype(bool)
    # bar is a "first retest" if there was a cross since the last retest before it
    bars_since_retest = _bars_since_event(retest)
    cond_first_retest = retest & (last_cross_at.notna()) & ((bars_since_retest <= last_cross_at) | bars_since_retest.isna())
    mag = _safe_div((close - slow).abs(), atr)
    return (_last_event_value(mag, cond_first_retest.fillna(False))).diff().diff()


def f13_mcxf_194_post_crossover_drawdown_max_63d_sma50_200_d2(close: pd.Series) -> pd.Series:
    """Max drawdown of close from rolling-63d-max as of t, restricted to post-cross period.

    Computed as (peak63 - close) / peak63 only when there is a most-recent cross within the 63d window."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    event = _any_cross_events(fast, slow)
    last_cross_at = _bars_since_event(event)
    peak = close.rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).max()
    dd = _safe_div(peak - close, peak)
    valid = (last_cross_at <= QDAYS) & last_cross_at.notna()
    return (dd.where(valid, np.nan)).diff().diff()


def f13_mcxf_195_sma50_slope_crosses_above_sma200_slope_event_count_252d_d2(close: pd.Series) -> pd.Series:
    """252d count of bars where sma50's 21d slope crosses ABOVE sma200's 21d slope."""
    s50 = _sma(close, 50)
    s200 = _sma(close, 200)
    sl50 = _rolling_slope(s50, MDAYS)
    sl200 = _rolling_slope(s200, MDAYS)
    ev = _bull_cross_events(sl50, sl200).astype(float)
    return (ev.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()).diff().diff()


def f13_mcxf_196_sma50_slope_crosses_below_sma200_slope_event_count_252d_d2(close: pd.Series) -> pd.Series:
    """252d count of bars where sma50's 21d slope crosses BELOW sma200's 21d slope."""
    s50 = _sma(close, 50)
    s200 = _sma(close, 200)
    sl50 = _rolling_slope(s50, MDAYS)
    sl200 = _rolling_slope(s200, MDAYS)
    ev = _bear_cross_events(sl50, sl200).astype(float)
    return (ev.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()).diff().diff()


def f13_mcxf_197_slope_crossover_leads_price_crossover_count_252d_d2(close: pd.Series) -> pd.Series:
    """252d count of bars where a slope-cross happened in the prior 21d but NO price-MA cross yet."""
    s50 = _sma(close, 50)
    s200 = _sma(close, 200)
    sl50 = _rolling_slope(s50, MDAYS)
    sl200 = _rolling_slope(s200, MDAYS)
    slope_ev = _any_cross_events(sl50, sl200).astype(float)
    price_ev = _any_cross_events(s50, s200).astype(float)
    slope_in_21 = slope_ev.rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).sum() > 0
    price_in_21 = price_ev.rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).sum() > 0
    leads = (slope_in_21 & ~price_in_21).astype(float)
    return (leads.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()).diff().diff()


def f13_mcxf_198_slope_crossover_lag_to_price_crossover_mean_252d_d2(close: pd.Series) -> pd.Series:
    """Rolling-mean (252d) of (bars_since_slope_cross - bars_since_price_cross) - lag distribution mean."""
    s50 = _sma(close, 50)
    s200 = _sma(close, 200)
    sl50 = _rolling_slope(s50, MDAYS)
    sl200 = _rolling_slope(s200, MDAYS)
    slope_ev = _any_cross_events(sl50, sl200)
    price_ev = _any_cross_events(s50, s200)
    bs_slope = _bars_since_event(slope_ev)
    bs_price = _bars_since_event(price_ev)
    diff = bs_slope - bs_price
    return (diff.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).mean()).diff().diff()


def f13_mcxf_199_ema21_slope_vs_ema50_slope_crossover_freq_252d_d2(close: pd.Series) -> pd.Series:
    """252d total count of crosses between ema21 21d-slope and ema50 21d-slope."""
    e21 = _ema(close, 21)
    e50 = _ema(close, 50)
    sl21 = _rolling_slope(e21, MDAYS)
    sl50 = _rolling_slope(e50, MDAYS)
    ev = _any_cross_events(sl21, sl50).astype(float)
    return (ev.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()).diff().diff()


def f13_mcxf_200_slope_crossover_then_price_crossover_followthrough_rate_252d_d2(close: pd.Series) -> pd.Series:
    """Conditional rate: prob that a slope-cross is followed by a price-MA cross within 21d, over 252d."""
    s50 = _sma(close, 50)
    s200 = _sma(close, 200)
    sl50 = _rolling_slope(s50, MDAYS)
    sl200 = _rolling_slope(s200, MDAYS)
    slope_ev = _any_cross_events(sl50, sl200).astype(float)
    price_ev = _any_cross_events(s50, s200).astype(float)
    # for each slope event, did a price event occur in t..t+21?  PIT-safe: at bar t+21, check if slope event happened at t-21
    slope_lag21 = slope_ev.shift(MDAYS).astype(bool)
    price_in_window = price_ev.rolling(MDAYS + 1, min_periods=2).sum() > 0  # backward window
    followed = (slope_lag21 & price_in_window).astype(float)
    num = followed.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()
    den = slope_lag21.astype(float).rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()
    return (_safe_div(num, den)).diff().diff()


def f13_mcxf_201_slope_inversion_event_count_63d_sma50_d2(close: pd.Series) -> pd.Series:
    """63d count of bars where sma50's 21d slope crosses zero (slope inversion event)."""
    s50 = _sma(close, 50)
    sl = _rolling_slope(s50, MDAYS)
    zero = pd.Series(0.0, index=close.index)
    ev = _any_cross_events(sl, zero).astype(float)
    return (ev.rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).sum()).diff().diff()


def f13_mcxf_202_slope_convergence_event_count_63d_sma50_200_d2(close: pd.Series) -> pd.Series:
    """63d count of bars where BOTH sma50 and sma200 slopes simultaneously converge toward zero
    (|slope50_t| < |slope50_t-5| AND |slope200_t| < |slope200_t-5|)."""
    s50 = _sma(close, 50)
    s200 = _sma(close, 200)
    sl50 = _rolling_slope(s50, MDAYS)
    sl200 = _rolling_slope(s200, MDAYS)
    cond = (sl50.abs() < sl50.shift(5).abs()) & (sl200.abs() < sl200.shift(5).abs())
    return (cond.astype(float).rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).sum()).diff().diff()


def f13_mcxf_203_tenkan_kijun_bullish_cross_event_count_252d_d2(
    high: pd.Series, low: pd.Series
) -> pd.Series:
    """252d count of bullish Tenkan(9)/Kijun(26) crosses."""
    t = _tenkan(high, low, 9)
    k = _kijun(high, low, 26)
    ev = _bull_cross_events(t, k).astype(float)
    return (ev.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()).diff().diff()


def f13_mcxf_204_tenkan_kijun_bearish_cross_event_count_252d_d2(
    high: pd.Series, low: pd.Series
) -> pd.Series:
    """252d count of bearish Tenkan(9)/Kijun(26) crosses."""
    t = _tenkan(high, low, 9)
    k = _kijun(high, low, 26)
    ev = _bear_cross_events(t, k).astype(float)
    return (ev.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()).diff().diff()


def f13_mcxf_205_tenkan_kijun_cross_above_kumo_indicator_d2(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """1 if Tenkan>Kijun AND close > max(SenkouA, SenkouB) (PIT-clean unshifted Kumo); else 0."""
    t = _tenkan(high, low, 9)
    k = _kijun(high, low, 26)
    sa = _senkou_a(high, low, 9, 26)
    sb = _senkou_b(high, low, 52)
    cloud_top = pd.concat([sa.rename("a"), sb.rename("b")], axis=1).max(axis=1)
    cond = (t > k) & (close > cloud_top)
    return (cond.astype(float)).diff().diff()


def f13_mcxf_206_tenkan_kijun_cross_below_kumo_indicator_d2(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """1 if Tenkan<Kijun AND close < min(SenkouA, SenkouB) (PIT-clean unshifted Kumo); else 0."""
    t = _tenkan(high, low, 9)
    k = _kijun(high, low, 26)
    sa = _senkou_a(high, low, 9, 26)
    sb = _senkou_b(high, low, 52)
    cloud_bot = pd.concat([sa.rename("a"), sb.rename("b")], axis=1).min(axis=1)
    cond = (t < k) & (close < cloud_bot)
    return (cond.astype(float)).diff().diff()


def f13_mcxf_207_tenkan_kijun_below_kumo_streak_max_252d_d2(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """252d max streak length of `Tenkan<Kijun AND close<Kumo_min` condition."""
    t = _tenkan(high, low, 9)
    k = _kijun(high, low, 26)
    sa = _senkou_a(high, low, 9, 26)
    sb = _senkou_b(high, low, 52)
    cloud_bot = pd.concat([sa.rename("a"), sb.rename("b")], axis=1).min(axis=1)
    cond = ((t < k) & (close < cloud_bot)).astype(bool)
    return (_max_streak_in_window(cond, YDAYS)).diff().diff()


def f13_mcxf_208_kumo_breakout_event_count_252d_d2(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """252d count of bars where close crosses above OR below the Kumo cloud (Senkou max/min)."""
    sa = _senkou_a(high, low, 9, 26)
    sb = _senkou_b(high, low, 52)
    cloud_top = pd.concat([sa.rename("a"), sb.rename("b")], axis=1).max(axis=1)
    cloud_bot = pd.concat([sa.rename("a"), sb.rename("b")], axis=1).min(axis=1)
    bull = _bull_cross_events(close, cloud_top).astype(float)
    bear = _bear_cross_events(close, cloud_bot).astype(float)
    ev = (bull + bear)
    return (ev.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()).diff().diff()


def f13_mcxf_209_kumo_inside_persistence_streak_252d_d2(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """252d max streak length where close is INSIDE the Kumo cloud (min<=close<=max)."""
    sa = _senkou_a(high, low, 9, 26)
    sb = _senkou_b(high, low, 52)
    cloud_top = pd.concat([sa.rename("a"), sb.rename("b")], axis=1).max(axis=1)
    cloud_bot = pd.concat([sa.rename("a"), sb.rename("b")], axis=1).min(axis=1)
    inside = ((close >= cloud_bot) & (close <= cloud_top)).astype(bool)
    return (_max_streak_in_window(inside, YDAYS)).diff().diff()


def f13_mcxf_210_senkou_b_crossover_above_close_event_count_252d_d2(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """252d count of bars where SenkouB crosses ABOVE close (close losing support to leading cloud bottom)."""
    sb = _senkou_b(high, low, 52)
    ev = _bull_cross_events(sb, close).astype(float)
    return (ev.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()).diff().diff()


def f13_mcxf_211_jma_50_vs_jma_200_crossover_count_252d_d2(close: pd.Series) -> pd.Series:
    """252d count of crosses between JMA(50) and JMA(200) - Jurik adaptive MA pair."""
    fast = _jma(close, 50)
    slow = _jma(close, 200)
    ev = _any_cross_events(fast, slow).astype(float)
    return (ev.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()).diff().diff()


def f13_mcxf_212_vidya_short_vs_long_crossover_count_252d_d2(close: pd.Series) -> pd.Series:
    """252d count of crosses between VIDYA(21) and VIDYA(63) - Chande's variable MA pair."""
    fast = _vidya(close, 21)
    slow = _vidya(close, 63)
    ev = _any_cross_events(fast, slow).astype(float)
    return (ev.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()).diff().diff()


def f13_mcxf_213_alma_short_vs_long_crossover_count_252d_d2(close: pd.Series) -> pd.Series:
    """252d count of crosses between ALMA(21) and ALMA(63) - Arnaud Legoux MA pair."""
    fast = _alma(close, 21)
    slow = _alma(close, 63)
    ev = _any_cross_events(fast, slow).astype(float)
    return (ev.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()).diff().diff()


def f13_mcxf_214_adaptive_jma_vs_static_sma50_crossover_count_252d_d2(close: pd.Series) -> pd.Series:
    """252d count of crosses between JMA(50) and SMA(50) - adaptive vs static comparison."""
    a = _jma(close, 50)
    b = _sma(close, 50)
    ev = _any_cross_events(a, b).astype(float)
    return (ev.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()).diff().diff()


def f13_mcxf_215_adaptive_crossover_lead_lag_vs_sma_252d_d2(close: pd.Series) -> pd.Series:
    """Mean lag in bars between JMA(50)/JMA(200) crosses and SMA(50)/SMA(200) crosses over 252d."""
    fast_a = _jma(close, 50)
    slow_a = _jma(close, 200)
    fast_s = _sma(close, 50)
    slow_s = _sma(close, 200)
    bs_adapt = _bars_since_event(_any_cross_events(fast_a, slow_a))
    bs_sma = _bars_since_event(_any_cross_events(fast_s, slow_s))
    diff = bs_sma - bs_adapt  # positive => adaptive cross happened more recently than SMA cross
    return (diff.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).mean()).diff().diff()


def f13_mcxf_216_adaptive_crossover_failure_rate_252d_d2(close: pd.Series) -> pd.Series:
    """252d ratio: failed JMA(50)/JMA(200) crosses (reverse within 21d) / total such crosses."""
    fast = _jma(close, 50)
    slow = _jma(close, 200)
    raw = _any_cross_events(fast, slow).astype(float).rolling(
        YDAYS, min_periods=max(YDAYS // 3, 2)
    ).sum()
    fail = _failed_cross_events(fast, slow, MDAYS).astype(float).rolling(
        YDAYS, min_periods=max(YDAYS // 3, 2)
    ).sum()
    return (_safe_div(fail, raw)).diff().diff()


def f13_mcxf_217_crossover_during_high_vol_regime_count_252d_d2(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """252d count of sma50/200 crosses occurring when ATR21 is in top tercile of 252d distribution."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    atr = _atr(high, low, close, 21)
    rank = atr.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).rank(pct=True)
    high_vol = (rank >= 2.0 / 3.0)
    ev = _any_cross_events(fast, slow) & high_vol.fillna(False)
    return (ev.astype(float).rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()).diff().diff()


def f13_mcxf_218_crossover_during_low_vol_regime_count_252d_d2(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """252d count of sma50/200 crosses occurring when ATR21 is in bottom tercile of 252d distribution."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    atr = _atr(high, low, close, 21)
    rank = atr.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).rank(pct=True)
    low_vol = (rank <= 1.0 / 3.0)
    ev = _any_cross_events(fast, slow) & low_vol.fillna(False)
    return (ev.astype(float).rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()).diff().diff()


def f13_mcxf_219_crossover_during_at_high_regime_count_252d_d2(close: pd.Series) -> pd.Series:
    """252d count of sma50/200 crosses occurring when close is within 5% of 252d rolling max."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    peak = close.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).max()
    near_high = (close >= 0.95 * peak)
    ev = _any_cross_events(fast, slow) & near_high.fillna(False)
    return (ev.astype(float).rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()).diff().diff()


def f13_mcxf_220_crossover_during_drawdown_regime_count_252d_d2(close: pd.Series) -> pd.Series:
    """252d count of sma50/200 crosses occurring when close is in a drawdown >10% from 252d rolling max."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    peak = close.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).max()
    dd = _safe_div(peak - close, peak)
    in_dd = (dd > 0.10)
    ev = _any_cross_events(fast, slow) & in_dd.fillna(False)
    return (ev.astype(float).rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()).diff().diff()


def f13_mcxf_221_regime_specific_failure_rate_near_high_504d_d2(close: pd.Series) -> pd.Series:
    """504d ratio: failed sma50/200 crosses occurring within 5% of 504d-high / all crosses near high."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    peak = close.rolling(DDAYS_2Y, min_periods=max(DDAYS_2Y // 3, 2)).max()
    near_high = (close >= 0.95 * peak).fillna(False)
    failed = _failed_cross_events(fast, slow, MDAYS) & near_high
    raw = _any_cross_events(fast, slow) & near_high
    num = failed.astype(float).rolling(DDAYS_2Y, min_periods=max(DDAYS_2Y // 3, 2)).sum()
    den = raw.astype(float).rolling(DDAYS_2Y, min_periods=max(DDAYS_2Y // 3, 2)).sum()
    return (_safe_div(num, den)).diff().diff()


def f13_mcxf_222_regime_specific_failure_rate_low_vol_504d_d2(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """504d ratio: failed sma50/200 crosses occurring in low-vol regime / all crosses in low-vol regime."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    atr = _atr(high, low, close, 21)
    rank = atr.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).rank(pct=True)
    low_vol = (rank <= 1.0 / 3.0).fillna(False)
    failed = _failed_cross_events(fast, slow, MDAYS) & low_vol
    raw = _any_cross_events(fast, slow) & low_vol
    num = failed.astype(float).rolling(DDAYS_2Y, min_periods=max(DDAYS_2Y // 3, 2)).sum()
    den = raw.astype(float).rolling(DDAYS_2Y, min_periods=max(DDAYS_2Y // 3, 2)).sum()
    return (_safe_div(num, den)).diff().diff()


def f13_mcxf_223_multi_pair_crossover_alignment_composite_d2(close: pd.Series) -> pd.Series:
    """Composite: (bullish_breadth_21d - bearish_breadth_21d) * sign(sma50>sma200) over rolling 21d window."""
    pairs = [(20, 50), (50, 100), (50, 200), (100, 200)]
    bull_breadth = pd.Series(0.0, index=close.index)
    bear_breadth = pd.Series(0.0, index=close.index)
    for a, b in pairs:
        evb = _bull_cross_events(_sma(close, a), _sma(close, b)).astype(float)
        evx = _bear_cross_events(_sma(close, a), _sma(close, b)).astype(float)
        bull_breadth = bull_breadth + (evb.rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).sum() > 0).astype(float)
        bear_breadth = bear_breadth + (evx.rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).sum() > 0).astype(float)
    side = np.sign((_sma(close, 50) - _sma(close, 200)).fillna(0))
    return ((bull_breadth - bear_breadth) * side).diff().diff()


def f13_mcxf_224_failed_crossover_clustering_x_volume_composite_d2(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """Composite: clustering-index(63d failure spacing CV^2) * z-score(volume,252d) - distress crowding signal."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    failed = _failed_cross_events(fast, slow, MDAYS).astype(float)
    bars_since = _bars_since_event(failed.astype(bool))
    mu = bars_since.rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).mean()
    sd = bars_since.rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).std()
    cv2 = _safe_div(sd ** 2, mu ** 2)
    vz = _rolling_zscore(volume.astype(float), YDAYS)
    return (cv2 * vz).diff().diff()


def f13_mcxf_225_terminal_crossover_breakdown_composite_d2(
    high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series
) -> pd.Series:
    """Composite: 0.4*Kumo-below-streak21d + 0.3*z(volume,252d) + 0.3*z(failure-rate-504d,252d) - regime breakdown."""
    # Component 1: bars in "below kumo" condition within last 21
    sa = _senkou_a(high, low, 9, 26)
    sb = _senkou_b(high, low, 52)
    cloud_bot = pd.concat([sa.rename("a"), sb.rename("b")], axis=1).min(axis=1)
    below_kumo = (close < cloud_bot).astype(float)
    kumo_frac = below_kumo.rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).mean()
    # Component 2: volume z
    vz = _rolling_zscore(volume.astype(float), YDAYS)
    # Component 3: rolling z of failure rate
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    raw = _any_cross_events(fast, slow).astype(float).rolling(
        DDAYS_2Y, min_periods=max(DDAYS_2Y // 3, 2)
    ).sum()
    fail = _failed_cross_events(fast, slow, MDAYS).astype(float).rolling(
        DDAYS_2Y, min_periods=max(DDAYS_2Y // 3, 2)
    ).sum()
    fr = _safe_div(fail, raw)
    fr_z = _rolling_zscore(fr, YDAYS)
    return (0.4 * kumo_frac + 0.3 * vz + 0.3 * fr_z).diff().diff()


MA_CROSSOVER_FAILURE_DYNAMICS_D2_REGISTRY_151_225 = {
    "f13_mcxf_151_sma50_200_crossover_magnitude_at_event_atr_d2": {"inputs": ["high", "low", "close"], "func": f13_mcxf_151_sma50_200_crossover_magnitude_at_event_atr_d2},
    "f13_mcxf_152_ema21_50_crossover_magnitude_at_event_atr_d2": {"inputs": ["high", "low", "close"], "func": f13_mcxf_152_ema21_50_crossover_magnitude_at_event_atr_d2},
    "f13_mcxf_153_sma100_200_crossover_magnitude_at_event_atr_d2": {"inputs": ["high", "low", "close"], "func": f13_mcxf_153_sma100_200_crossover_magnitude_at_event_atr_d2},
    "f13_mcxf_154_crossover_slope_quality_sma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_154_crossover_slope_quality_sma50_200_d2},
    "f13_mcxf_155_crossover_volume_zscore_at_event_sma50_200_d2": {"inputs": ["close", "volume"], "func": f13_mcxf_155_crossover_volume_zscore_at_event_sma50_200_d2},
    "f13_mcxf_156_crossover_close_distance_to_intersection_atr_units_d2": {"inputs": ["high", "low", "close"], "func": f13_mcxf_156_crossover_close_distance_to_intersection_atr_units_d2},
    "f13_mcxf_157_crossover_durability_score_sma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_157_crossover_durability_score_sma50_200_d2},
    "f13_mcxf_158_magnitude_decay_post_crossover_5d_sma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_158_magnitude_decay_post_crossover_5d_sma50_200_d2},
    "f13_mcxf_159_crossover_atr_normalized_separation_now_sma50_200_d2": {"inputs": ["high", "low", "close"], "func": f13_mcxf_159_crossover_atr_normalized_separation_now_sma50_200_d2},
    "f13_mcxf_160_crossover_quality_composite_sma50_200_d2": {"inputs": ["high", "low", "close", "volume"], "func": f13_mcxf_160_crossover_quality_composite_sma50_200_d2},
    "f13_mcxf_161_triple_ma_bullish_alignment_event_count_252d_d2": {"inputs": ["close"], "func": f13_mcxf_161_triple_ma_bullish_alignment_event_count_252d_d2},
    "f13_mcxf_162_triple_ma_bearish_alignment_event_count_252d_d2": {"inputs": ["close"], "func": f13_mcxf_162_triple_ma_bearish_alignment_event_count_252d_d2},
    "f13_mcxf_163_quad_ma_simultaneous_crossover_count_252d_d2": {"inputs": ["close"], "func": f13_mcxf_163_quad_ma_simultaneous_crossover_count_252d_d2},
    "f13_mcxf_164_multi_ma_crossover_density_63d_d2": {"inputs": ["close"], "func": f13_mcxf_164_multi_ma_crossover_density_63d_d2},
    "f13_mcxf_165_crossover_breadth_bullish_21d_d2": {"inputs": ["close"], "func": f13_mcxf_165_crossover_breadth_bullish_21d_d2},
    "f13_mcxf_166_crossover_breadth_bearish_21d_d2": {"inputs": ["close"], "func": f13_mcxf_166_crossover_breadth_bearish_21d_d2},
    "f13_mcxf_167_crossover_breadth_bullish_to_bearish_transition_event_d2": {"inputs": ["close"], "func": f13_mcxf_167_crossover_breadth_bullish_to_bearish_transition_event_d2},
    "f13_mcxf_168_crossover_simultaneity_window_min_bars_d2": {"inputs": ["close"], "func": f13_mcxf_168_crossover_simultaneity_window_min_bars_d2},
    "f13_mcxf_169_sma50_200_hysteresis_3bar_crossover_count_252d_d2": {"inputs": ["close"], "func": f13_mcxf_169_sma50_200_hysteresis_3bar_crossover_count_252d_d2},
    "f13_mcxf_170_sma50_200_hysteresis_5bar_crossover_count_252d_d2": {"inputs": ["close"], "func": f13_mcxf_170_sma50_200_hysteresis_5bar_crossover_count_252d_d2},
    "f13_mcxf_171_ema21_50_hysteresis_3bar_crossover_count_252d_d2": {"inputs": ["close"], "func": f13_mcxf_171_ema21_50_hysteresis_3bar_crossover_count_252d_d2},
    "f13_mcxf_172_hysteresis_filtered_recross_frequency_252d_d2": {"inputs": ["close"], "func": f13_mcxf_172_hysteresis_filtered_recross_frequency_252d_d2},
    "f13_mcxf_173_hysteresis_validated_crossover_failure_count_252d_d2": {"inputs": ["close"], "func": f13_mcxf_173_hysteresis_validated_crossover_failure_count_252d_d2},
    "f13_mcxf_174_atr_band_filtered_crossover_count_252d_d2": {"inputs": ["high", "low", "close"], "func": f13_mcxf_174_atr_band_filtered_crossover_count_252d_d2},
    "f13_mcxf_175_volume_confirmed_crossover_count_252d_d2": {"inputs": ["close", "volume"], "func": f13_mcxf_175_volume_confirmed_crossover_count_252d_d2},
    "f13_mcxf_176_hysteresis_persistence_quality_score_sma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_176_hysteresis_persistence_quality_score_sma50_200_d2},
    "f13_mcxf_177_failed_sma50_200_crossovers_count_252d_d2": {"inputs": ["close"], "func": f13_mcxf_177_failed_sma50_200_crossovers_count_252d_d2},
    "f13_mcxf_178_failed_ema21_50_crossovers_count_252d_d2": {"inputs": ["close"], "func": f13_mcxf_178_failed_ema21_50_crossovers_count_252d_d2},
    "f13_mcxf_179_failed_crossover_streak_max_252d_sma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_179_failed_crossover_streak_max_252d_sma50_200_d2},
    "f13_mcxf_180_mean_time_between_failed_crossovers_sma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_180_mean_time_between_failed_crossovers_sma50_200_d2},
    "f13_mcxf_181_failure_rate_sma50_200_504d_d2": {"inputs": ["close"], "func": f13_mcxf_181_failure_rate_sma50_200_504d_d2},
    "f13_mcxf_182_failure_rate_ema21_50_504d_d2": {"inputs": ["close"], "func": f13_mcxf_182_failure_rate_ema21_50_504d_d2},
    "f13_mcxf_183_consecutive_failed_crossover_count_now_sma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_183_consecutive_failed_crossover_count_now_sma50_200_d2},
    "f13_mcxf_184_consecutive_successful_crossover_count_now_sma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_184_consecutive_successful_crossover_count_now_sma50_200_d2},
    "f13_mcxf_185_failure_then_extension_indicator_sma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_185_failure_then_extension_indicator_sma50_200_d2},
    "f13_mcxf_186_crossover_failure_clustering_index_sma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_186_crossover_failure_clustering_index_sma50_200_d2},
    "f13_mcxf_187_post_golden_cross_close_above_50_streak_max_252d_d2": {"inputs": ["close"], "func": f13_mcxf_187_post_golden_cross_close_above_50_streak_max_252d_d2},
    "f13_mcxf_188_post_death_cross_close_below_50_streak_max_252d_d2": {"inputs": ["close"], "func": f13_mcxf_188_post_death_cross_close_below_50_streak_max_252d_d2},
    "f13_mcxf_189_post_crossover_atr_expansion_21d_sma50_200_d2": {"inputs": ["high", "low", "close"], "func": f13_mcxf_189_post_crossover_atr_expansion_21d_sma50_200_d2},
    "f13_mcxf_190_post_crossover_volume_acceleration_21d_sma50_200_d2": {"inputs": ["close", "volume"], "func": f13_mcxf_190_post_crossover_volume_acceleration_21d_sma50_200_d2},
    "f13_mcxf_191_post_crossover_slope_acceleration_sma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_191_post_crossover_slope_acceleration_sma50_200_d2},
    "f13_mcxf_192_bars_to_first_retest_post_crossover_50_200_d2": {"inputs": ["close"], "func": f13_mcxf_192_bars_to_first_retest_post_crossover_50_200_d2},
    "f13_mcxf_193_magnitude_of_first_retest_post_crossover_atr_sma50_200_d2": {"inputs": ["high", "low", "close"], "func": f13_mcxf_193_magnitude_of_first_retest_post_crossover_atr_sma50_200_d2},
    "f13_mcxf_194_post_crossover_drawdown_max_63d_sma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_194_post_crossover_drawdown_max_63d_sma50_200_d2},
    "f13_mcxf_195_sma50_slope_crosses_above_sma200_slope_event_count_252d_d2": {"inputs": ["close"], "func": f13_mcxf_195_sma50_slope_crosses_above_sma200_slope_event_count_252d_d2},
    "f13_mcxf_196_sma50_slope_crosses_below_sma200_slope_event_count_252d_d2": {"inputs": ["close"], "func": f13_mcxf_196_sma50_slope_crosses_below_sma200_slope_event_count_252d_d2},
    "f13_mcxf_197_slope_crossover_leads_price_crossover_count_252d_d2": {"inputs": ["close"], "func": f13_mcxf_197_slope_crossover_leads_price_crossover_count_252d_d2},
    "f13_mcxf_198_slope_crossover_lag_to_price_crossover_mean_252d_d2": {"inputs": ["close"], "func": f13_mcxf_198_slope_crossover_lag_to_price_crossover_mean_252d_d2},
    "f13_mcxf_199_ema21_slope_vs_ema50_slope_crossover_freq_252d_d2": {"inputs": ["close"], "func": f13_mcxf_199_ema21_slope_vs_ema50_slope_crossover_freq_252d_d2},
    "f13_mcxf_200_slope_crossover_then_price_crossover_followthrough_rate_252d_d2": {"inputs": ["close"], "func": f13_mcxf_200_slope_crossover_then_price_crossover_followthrough_rate_252d_d2},
    "f13_mcxf_201_slope_inversion_event_count_63d_sma50_d2": {"inputs": ["close"], "func": f13_mcxf_201_slope_inversion_event_count_63d_sma50_d2},
    "f13_mcxf_202_slope_convergence_event_count_63d_sma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_202_slope_convergence_event_count_63d_sma50_200_d2},
    "f13_mcxf_203_tenkan_kijun_bullish_cross_event_count_252d_d2": {"inputs": ["high", "low"], "func": f13_mcxf_203_tenkan_kijun_bullish_cross_event_count_252d_d2},
    "f13_mcxf_204_tenkan_kijun_bearish_cross_event_count_252d_d2": {"inputs": ["high", "low"], "func": f13_mcxf_204_tenkan_kijun_bearish_cross_event_count_252d_d2},
    "f13_mcxf_205_tenkan_kijun_cross_above_kumo_indicator_d2": {"inputs": ["high", "low", "close"], "func": f13_mcxf_205_tenkan_kijun_cross_above_kumo_indicator_d2},
    "f13_mcxf_206_tenkan_kijun_cross_below_kumo_indicator_d2": {"inputs": ["high", "low", "close"], "func": f13_mcxf_206_tenkan_kijun_cross_below_kumo_indicator_d2},
    "f13_mcxf_207_tenkan_kijun_below_kumo_streak_max_252d_d2": {"inputs": ["high", "low", "close"], "func": f13_mcxf_207_tenkan_kijun_below_kumo_streak_max_252d_d2},
    "f13_mcxf_208_kumo_breakout_event_count_252d_d2": {"inputs": ["high", "low", "close"], "func": f13_mcxf_208_kumo_breakout_event_count_252d_d2},
    "f13_mcxf_209_kumo_inside_persistence_streak_252d_d2": {"inputs": ["high", "low", "close"], "func": f13_mcxf_209_kumo_inside_persistence_streak_252d_d2},
    "f13_mcxf_210_senkou_b_crossover_above_close_event_count_252d_d2": {"inputs": ["high", "low", "close"], "func": f13_mcxf_210_senkou_b_crossover_above_close_event_count_252d_d2},
    "f13_mcxf_211_jma_50_vs_jma_200_crossover_count_252d_d2": {"inputs": ["close"], "func": f13_mcxf_211_jma_50_vs_jma_200_crossover_count_252d_d2},
    "f13_mcxf_212_vidya_short_vs_long_crossover_count_252d_d2": {"inputs": ["close"], "func": f13_mcxf_212_vidya_short_vs_long_crossover_count_252d_d2},
    "f13_mcxf_213_alma_short_vs_long_crossover_count_252d_d2": {"inputs": ["close"], "func": f13_mcxf_213_alma_short_vs_long_crossover_count_252d_d2},
    "f13_mcxf_214_adaptive_jma_vs_static_sma50_crossover_count_252d_d2": {"inputs": ["close"], "func": f13_mcxf_214_adaptive_jma_vs_static_sma50_crossover_count_252d_d2},
    "f13_mcxf_215_adaptive_crossover_lead_lag_vs_sma_252d_d2": {"inputs": ["close"], "func": f13_mcxf_215_adaptive_crossover_lead_lag_vs_sma_252d_d2},
    "f13_mcxf_216_adaptive_crossover_failure_rate_252d_d2": {"inputs": ["close"], "func": f13_mcxf_216_adaptive_crossover_failure_rate_252d_d2},
    "f13_mcxf_217_crossover_during_high_vol_regime_count_252d_d2": {"inputs": ["high", "low", "close"], "func": f13_mcxf_217_crossover_during_high_vol_regime_count_252d_d2},
    "f13_mcxf_218_crossover_during_low_vol_regime_count_252d_d2": {"inputs": ["high", "low", "close"], "func": f13_mcxf_218_crossover_during_low_vol_regime_count_252d_d2},
    "f13_mcxf_219_crossover_during_at_high_regime_count_252d_d2": {"inputs": ["close"], "func": f13_mcxf_219_crossover_during_at_high_regime_count_252d_d2},
    "f13_mcxf_220_crossover_during_drawdown_regime_count_252d_d2": {"inputs": ["close"], "func": f13_mcxf_220_crossover_during_drawdown_regime_count_252d_d2},
    "f13_mcxf_221_regime_specific_failure_rate_near_high_504d_d2": {"inputs": ["close"], "func": f13_mcxf_221_regime_specific_failure_rate_near_high_504d_d2},
    "f13_mcxf_222_regime_specific_failure_rate_low_vol_504d_d2": {"inputs": ["high", "low", "close"], "func": f13_mcxf_222_regime_specific_failure_rate_low_vol_504d_d2},
    "f13_mcxf_223_multi_pair_crossover_alignment_composite_d2": {"inputs": ["close"], "func": f13_mcxf_223_multi_pair_crossover_alignment_composite_d2},
    "f13_mcxf_224_failed_crossover_clustering_x_volume_composite_d2": {"inputs": ["close", "volume"], "func": f13_mcxf_224_failed_crossover_clustering_x_volume_composite_d2},
    "f13_mcxf_225_terminal_crossover_breakdown_composite_d2": {"inputs": ["high", "low", "close", "volume"], "func": f13_mcxf_225_terminal_crossover_breakdown_composite_d2},
}
