"""34_td_sequential_demark d3 features 376-450 — order-3 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff().diff().diff(). Self-contained; helpers redefined locally per HANDOFF."""
import numpy as np
import pandas as pd
YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
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
    idx = num.index if hasattr(num, 'index') else None
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

def _pct_rank(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).rank(pct=True)

def _sma(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).mean()

def _bars_since_true(flag):
    f = (flag.fillna(0) > 0).astype(int)
    idx = np.arange(len(f))
    last = np.where(f.values == 1, idx, np.nan)
    last_ffill = pd.Series(last, index=f.index).ffill()
    return pd.Series(idx, index=f.index) - last_ffill

def _value_at_event(value: pd.Series, event_flag: pd.Series) -> pd.Series:
    return value.where(event_flag.fillna(0) == 1, np.nan).ffill()

def _td_sell_setup_count(close: pd.Series) -> pd.Series:
    qual = (close > close.shift(4)).astype(int).fillna(0).astype(int)
    grp = (qual == 0).cumsum()
    return qual.groupby(grp).cumsum().astype(float)

def _td_buy_setup_count(close: pd.Series) -> pd.Series:
    qual = (close < close.shift(4)).astype(int).fillna(0).astype(int)
    grp = (qual == 0).cumsum()
    return qual.groupby(grp).cumsum().astype(float)

def _td_perfected_sell_setup_9_event(close: pd.Series, high: pd.Series) -> pd.Series:
    sc = _td_sell_setup_count(close)
    fires = (sc == 9).astype(float)
    h6 = high.shift(3)
    h7 = high.shift(2)
    h8 = high.shift(1)
    h9 = high
    bar_max = pd.concat([h6, h7], axis=1).max(axis=1)
    perfected = ((h8 >= bar_max) | (h9 >= bar_max)).astype(float)
    return (fires * perfected).where(sc.notna(), np.nan)

def _td_sell_countdown_count(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    sc = _td_sell_setup_count(close).values
    bc = _td_buy_setup_count(close).values
    cl = close.values
    hi = high.values
    n = len(close)
    out = np.zeros(n)
    active = False
    cnt = 0
    for i in range(n):
        if not active and i >= 8 and (sc[i] >= 9):
            active = True
            cnt = 0
        if active and i >= 8 and (bc[i] >= 9):
            active = False
            cnt = 0
        if active:
            if i >= 2 and cl[i] >= hi[i - 2] and (cnt < 13):
                cnt += 1
            out[i] = cnt
    return pd.Series(out, index=close.index)

def _td_sell_combo_count(close: pd.Series, high: pd.Series) -> pd.Series:
    sc = _td_sell_setup_count(close).values
    bc = _td_buy_setup_count(close).values
    cl = close.values
    hi = high.values
    n = len(close)
    out = np.zeros(n)
    active = False
    cnt = 0
    for i in range(n):
        if not active and i >= 8 and (sc[i] >= 9):
            active = True
            cnt = 0
        if active and i >= 8 and (bc[i] >= 9):
            active = False
            cnt = 0
        if active and i >= 2:
            qual = cl[i] >= hi[i - 2]
            if qual and cnt < 13:
                cnt += 1
            elif not qual:
                cnt = 0
            out[i] = cnt
    return pd.Series(out, index=close.index)

def _td_rei(close: pd.Series, high: pd.Series, low: pd.Series, n: int=5) -> pd.Series:
    high_mom = high - high.shift(2)
    low_mom = low - low.shift(2)
    abs_h = high_mom.abs()
    abs_l = low_mom.abs()
    cond1 = (high.shift(2) >= close.shift(7)) | (high.shift(2) >= close.shift(8))
    cond2 = (high >= low.shift(5)) | (high >= low.shift(6))
    cond3 = (low.shift(2) <= close.shift(7)) | (low.shift(2) <= close.shift(8))
    cond4 = (low <= high.shift(5)) | (low <= high.shift(6))
    weight = (cond1 & cond2 | cond3 & cond4).astype(float)
    return 100.0 * _safe_div(((high_mom + low_mom) * weight).rolling(n, min_periods=max(n // 3, 2)).sum(), (abs_h + abs_l).rolling(n, min_periods=max(n // 3, 2)).sum())

def _within_last_setup(sc):
    """Mask: True only for bars where sell-setup count > 0 (active setup)."""
    return sc > 0

def _waldo_4_bearish_event(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Waldo 4 (approximation): today's high > prior high, today's close < prior close, today's close in lower half of bar."""
    rng = (high - low).replace(0, np.nan)
    close_pos = _safe_div(close - low, rng)
    return ((high > high.shift(1)) & (close < close.shift(1)) & (close_pos < 0.5)).astype(float)

def _waldo_6_bearish_event(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Waldo 6 (approximation): 2-bar pattern — bar 1 is wide-up, bar 2 is bearish inside-bar."""
    rng1 = high.shift(1) - low.shift(1)
    bar1_up = (close.shift(1) > close.shift(2)) & (rng1 > rng1.rolling(MDAYS, min_periods=WDAYS).mean())
    bar2_inside = (high < high.shift(1)) & (low > low.shift(1))
    bar2_bear = close < close.shift(1)
    return (bar1_up & bar2_inside & bar2_bear).astype(float)

def _waldo_7_bearish_event(close: pd.Series, high: pd.Series) -> pd.Series:
    """Waldo 7 (approximation): today's close < prior close, today's high > 2-bar-ago high (new short-term high failure)."""
    return ((close < close.shift(1)) & (high > high.shift(2))).astype(float)

def _waldo_8_bearish_event(close: pd.Series, open_: pd.Series, high: pd.Series) -> pd.Series:
    """Waldo 8 (approximation): gap-up open AND bearish close, with body in upper third of bar."""
    rng = (high - high.shift(1)).abs()
    bear_close = (close < open_) & (open_ > high.shift(1))
    return bear_close.astype(float)

def f34_tdsq_376_setup_count_at_or_above_5_indicator_d3(close: pd.Series) -> pd.Series:
    """+1 when TD sell-setup count >= 5 (past the mid-point of setup)."""
    sc = _td_sell_setup_count(close)
    return (sc >= 5).astype(float).where(sc.notna(), np.nan).diff().diff().diff()

def f34_tdsq_377_setup_count_at_or_above_7_indicator_d3(close: pd.Series) -> pd.Series:
    """+1 when TD sell-setup count >= 7 (very near completion)."""
    sc = _td_sell_setup_count(close)
    return (sc >= 7).astype(float).where(sc.notna(), np.nan).diff().diff().diff()

def f34_tdsq_378_setup_count_exactly_8_indicator_d3(close: pd.Series) -> pd.Series:
    """+1 when TD sell-setup count == 8 (one bar from completion)."""
    sc = _td_sell_setup_count(close)
    return (sc == 8).astype(float).where(sc.notna(), np.nan).diff().diff().diff()

def f34_tdsq_379_setup_count_above_9_indicator_d3(close: pd.Series) -> pd.Series:
    """+1 when TD sell-setup count > 9 (extended sell-streak — late-stage exhaustion zone)."""
    sc = _td_sell_setup_count(close)
    return (sc > 9).astype(float).where(sc.notna(), np.nan).diff().diff().diff()

def f34_tdsq_380_setup_count_at_3_indicator_d3(close: pd.Series) -> pd.Series:
    """+1 when TD sell-setup count == 3 (early setup confirmation)."""
    sc = _td_sell_setup_count(close)
    return (sc == 3).astype(float).where(sc.notna(), np.nan).diff().diff().diff()

def f34_tdsq_381_setup_count_at_6_indicator_d3(close: pd.Series) -> pd.Series:
    """+1 when TD sell-setup count == 6 (mid-setup)."""
    sc = _td_sell_setup_count(close)
    return (sc == 6).astype(float).where(sc.notna(), np.nan).diff().diff().diff()

def f34_tdsq_382_buy_setup_count_active_indicator_d3(close: pd.Series) -> pd.Series:
    """+1 when TD buy-setup count > 0 (buy-setup running — contrarian top signal possible)."""
    bc = _td_buy_setup_count(close)
    return (bc > 0).astype(float).where(bc.notna(), np.nan).diff().diff().diff()

def f34_tdsq_383_max_setup_or_buy_count_value_d3(close: pd.Series) -> pd.Series:
    """Max of (sell-setup-count, buy-setup-count) — whichever direction is dominant."""
    sc = _td_sell_setup_count(close)
    bc = _td_buy_setup_count(close)
    return pd.concat([sc.rename('s'), bc.rename('b')], axis=1).max(axis=1).diff().diff().diff()

def f34_tdsq_384_setup_count_top_quintile_252d_d3(close: pd.Series) -> pd.Series:
    """Percentile rank of current sell-setup count within trailing 252d (0..1)."""
    return _pct_rank(_td_sell_setup_count(close), YDAYS).diff().diff().diff()

def f34_tdsq_385_setup_count_above_5_persistence_21d_d3(close: pd.Series) -> pd.Series:
    """Count of trailing 21d bars where TD sell-setup count >= 5."""
    sc = _td_sell_setup_count(close)
    return (sc >= 5).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff().diff().diff()

def f34_tdsq_386_volume_zscore_at_countdown_1_bar_d3(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol z-score(63d) captured at the most-recent countdown==1 bar (held forward)."""
    cd = _td_sell_countdown_count(close, high, low)
    fires = (cd == 1).astype(float)
    return _value_at_event(_rolling_zscore(volume, QDAYS), fires).diff().diff().diff()

def f34_tdsq_387_volume_zscore_at_countdown_5_bar_d3(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol z-score(63d) captured at most-recent countdown==5 bar."""
    cd = _td_sell_countdown_count(close, high, low)
    fires = (cd == 5).astype(float)
    return _value_at_event(_rolling_zscore(volume, QDAYS), fires).diff().diff().diff()

def f34_tdsq_388_volume_zscore_at_countdown_13_bar_d3(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol z-score(63d) captured at most-recent countdown==13 fire bar."""
    cd = _td_sell_countdown_count(close, high, low)
    fires = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    return _value_at_event(_rolling_zscore(volume, QDAYS), fires).diff().diff().diff()

def f34_tdsq_389_vol_progression_at_countdown_13_over_1_d3(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol-at-countdown-13 / vol-at-countdown-1 (held forward) — vol growth across countdown."""
    cd = _td_sell_countdown_count(close, high, low)
    v_at_1 = volume.where(cd == 1, np.nan).ffill()
    v_at_13 = volume.where((cd == 13) & (cd.shift(1) < 13), np.nan).ffill()
    return _safe_div(v_at_13, v_at_1).diff().diff().diff()

def f34_tdsq_390_countdown_13_on_high_volume_count_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of trailing 252d countdown-13 events that fired on top-decile-vol(252d) bars."""
    cd = _td_sell_countdown_count(close, high, low)
    fire = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    top_vol = (_pct_rank(volume, YDAYS) >= 0.9).astype(float)
    return (fire * top_vol).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f34_tdsq_391_countdown_13_on_low_volume_count_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of trailing 252d countdown-13 events on bottom-decile-vol bars."""
    cd = _td_sell_countdown_count(close, high, low)
    fire = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    bot_vol = (_pct_rank(volume, YDAYS) <= 0.1).astype(float)
    return (fire * bot_vol).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f34_tdsq_392_dollar_vol_pct_rank_252d_at_countdown_13_bar_d3(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar-volume 252d-pct-rank captured at most-recent countdown-13 fire bar."""
    cd = _td_sell_countdown_count(close, high, low)
    fire = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    return _value_at_event(_pct_rank(close * volume, YDAYS), fire).diff().diff().diff()

def f34_tdsq_393_vol_zscore_at_combo_13_bar_d3(close: pd.Series, high: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol z-score(63d) captured at most-recent TD Combo-13 fire bar."""
    cb = _td_sell_combo_count(close, high)
    fire = ((cb == 13) & (cb.shift(1) < 13)).astype(float)
    return _value_at_event(_rolling_zscore(volume, QDAYS), fire).diff().diff().diff()

def f34_tdsq_394_bar_range_atr_norm_at_countdown_13_bar_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bar-range / ATR(21) captured at most-recent countdown-13 fire bar."""
    cd = _td_sell_countdown_count(close, high, low)
    fire = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    return _value_at_event(_safe_div(high - low, _atr(high, low, close, MDAYS)), fire).diff().diff().diff()

def f34_tdsq_395_gap_pct_at_countdown_13_bar_d3(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """% gap (open vs prior close) captured at most-recent countdown-13 fire bar."""
    cd = _td_sell_countdown_count(close, high, low)
    fire = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    gap = open / close.shift(1) - 1.0
    return _value_at_event(gap, fire).diff().diff().diff()

def f34_tdsq_396_count_high_vol_bars_during_last_setup_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars that were both 'in active sell-setup' AND high-vol (z(63)>1)."""
    sc = _td_sell_setup_count(close)
    in_setup = _within_last_setup(sc).astype(float)
    high_vol = (_rolling_zscore(volume, QDAYS) > 1.0).astype(float)
    return (in_setup * high_vol).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f34_tdsq_397_count_wide_range_bars_during_last_setup_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Trailing 252d count of bars in active setup AND top-decile-range (252d)."""
    sc = _td_sell_setup_count(close)
    in_setup = _within_last_setup(sc).astype(float)
    wide = (_pct_rank(high - low, YDAYS) >= 0.9).astype(float)
    return (in_setup * wide).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f34_tdsq_398_count_gap_up_bars_during_last_setup_252d_d3(close: pd.Series, open: pd.Series, high: pd.Series) -> pd.Series:
    """Trailing 252d count of bars in active setup AND gap-up (open > prior high)."""
    sc = _td_sell_setup_count(close)
    in_setup = _within_last_setup(sc).astype(float)
    gap_up = (open > high.shift(1)).astype(float)
    return (in_setup * gap_up).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f34_tdsq_399_count_doji_bars_during_last_setup_252d_d3(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Trailing 252d count of bars in active setup AND doji (body < 10% of range)."""
    sc = _td_sell_setup_count(close)
    in_setup = _within_last_setup(sc).astype(float)
    rng = (high - low).replace(0, np.nan)
    doji = ((close - open).abs() / rng < 0.1).astype(float)
    return (in_setup * doji).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f34_tdsq_400_max_vol_zscore_during_last_setup_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Maximum vol z-score(63d) observed during active setup, rolling 252d-max — most extreme vol during a setup."""
    sc = _td_sell_setup_count(close)
    in_setup_vz = _rolling_zscore(volume, QDAYS).where(_within_last_setup(sc), np.nan)
    return in_setup_vz.rolling(YDAYS, min_periods=QDAYS).max().diff().diff().diff()

def f34_tdsq_401_mean_vol_zscore_during_last_setup_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean vol z-score during active-setup bars over trailing 252d."""
    sc = _td_sell_setup_count(close)
    in_setup_vz = _rolling_zscore(volume, QDAYS).where(_within_last_setup(sc), np.nan)
    return in_setup_vz.rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f34_tdsq_402_max_bar_range_atr_norm_during_last_setup_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Max bar-range / ATR(21) observed during active-setup bars, rolling 252d max."""
    sc = _td_sell_setup_count(close)
    rng_norm = _safe_div(high - low, _atr(high, low, close, MDAYS)).where(_within_last_setup(sc), np.nan)
    return rng_norm.rolling(YDAYS, min_periods=QDAYS).max().diff().diff().diff()

def f34_tdsq_403_setup_breakaway_gap_at_1_indicator_d3(close: pd.Series, open: pd.Series, high: pd.Series) -> pd.Series:
    """+1 when setup-count == 1 AND today's open > prior bar's high (breakaway gap starting setup)."""
    sc = _td_sell_setup_count(close)
    at_start = (sc == 1).astype(float)
    gap_up = (open > high.shift(1)).astype(float)
    return (at_start * gap_up).where(at_start.notna() & gap_up.notna(), np.nan).diff().diff().diff()

def f34_tdsq_404_setup_exhaustion_gap_at_9_indicator_d3(close: pd.Series, open: pd.Series, high: pd.Series) -> pd.Series:
    """+1 when setup-count == 9 AND today's open > prior bar's high (exhaustion gap at completion)."""
    sc = _td_sell_setup_count(close)
    at_end = (sc == 9).astype(float)
    gap_up = (open > high.shift(1)).astype(float)
    return (at_end * gap_up).where(at_end.notna() & gap_up.notna(), np.nan).diff().diff().diff()

def f34_tdsq_405_setup_run_through_count_252d_d3(close: pd.Series) -> pd.Series:
    """Count of clean 9-bar setups (start-to-9 in exactly 9 bars) in trailing 252d."""
    sc = _td_sell_setup_count(close)
    started = (sc == 1).astype(float)
    bars_since_start = _bars_since_true(started)
    fires = (sc == 9).astype(int)
    clean = ((bars_since_start == 8) & (fires == 1)).astype(float)
    return clean.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f34_tdsq_406_td_waldo_4_bearish_event_indicator_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 on bar where Waldo-4 bearish (approx) fires."""
    return _waldo_4_bearish_event(close, high, low).diff().diff().diff()

def f34_tdsq_407_td_waldo_6_bearish_event_indicator_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 on bar where Waldo-6 bearish (approx) fires."""
    return _waldo_6_bearish_event(close, high, low).diff().diff().diff()

def f34_tdsq_408_td_waldo_7_bearish_event_indicator_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """+1 on bar where Waldo-7 bearish (approx) fires."""
    return _waldo_7_bearish_event(close, high).diff().diff().diff()

def f34_tdsq_409_td_waldo_8_bearish_event_indicator_d3(open: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    """+1 on bar where Waldo-8 bearish (approx) fires."""
    return _waldo_8_bearish_event(close, open, high).diff().diff().diff()

def f34_tdsq_410_td_waldo_count_5patterns_252d_d3(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of Waldo-4/6/7/8 events in trailing 252d (4 patterns summed)."""
    total = _waldo_4_bearish_event(close, high, low).fillna(0) + _waldo_6_bearish_event(close, high, low).fillna(0) + _waldo_7_bearish_event(close, high).fillna(0) + _waldo_8_bearish_event(close, open, high).fillna(0)
    return total.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f34_tdsq_411_bars_since_td_waldo_4_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since most recent Waldo-4 event."""
    return _bars_since_true(_waldo_4_bearish_event(close, high, low)).diff().diff().diff()

def f34_tdsq_412_bars_since_td_waldo_6_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since most recent Waldo-6 event."""
    return _bars_since_true(_waldo_6_bearish_event(close, high, low)).diff().diff().diff()

def f34_tdsq_413_bars_since_td_waldo_7_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Bars since most recent Waldo-7 event."""
    return _bars_since_true(_waldo_7_bearish_event(close, high)).diff().diff().diff()

def f34_tdsq_414_bars_since_td_waldo_8_d3(open: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    """Bars since most recent Waldo-8 event."""
    return _bars_since_true(_waldo_8_bearish_event(close, open, high)).diff().diff().diff()

def f34_tdsq_415_td_waldo_alignment_3of4_in_5d_indicator_d3(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when at least 3 of the 4 new Waldo patterns (4/6/7/8) fired within trailing 5 bars."""
    a = _waldo_4_bearish_event(close, high, low).fillna(0).rolling(WDAYS, min_periods=1).max()
    b = _waldo_6_bearish_event(close, high, low).fillna(0).rolling(WDAYS, min_periods=1).max()
    c = _waldo_7_bearish_event(close, high).fillna(0).rolling(WDAYS, min_periods=1).max()
    d = _waldo_8_bearish_event(close, open, high).fillna(0).rolling(WDAYS, min_periods=1).max()
    return (a + b + c + d >= 3).astype(float).diff().diff().diff()

def f34_tdsq_416_rei_above_80_indicator_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when REI > 80 (extreme overbought)."""
    r = _td_rei(close, high, low)
    return (r > 80).astype(float).where(r.notna(), np.nan).diff().diff().diff()

def f34_tdsq_417_rei_below_40_indicator_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when REI < -40 (oversold)."""
    r = _td_rei(close, high, low)
    return (r < -40).astype(float).where(r.notna(), np.nan).diff().diff().diff()

def f34_tdsq_418_rei_above_60_persistence_5d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of trailing 5d bars where REI > 60."""
    r = _td_rei(close, high, low)
    return (r > 60).astype(float).rolling(WDAYS, min_periods=1).sum().diff().diff().diff()

def f34_tdsq_419_rei_above_60_persistence_21d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of trailing 21d bars where REI > 60."""
    r = _td_rei(close, high, low)
    return (r > 60).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff().diff().diff()

def f34_tdsq_420_rei_above_80_persistence_5d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of trailing 5d bars where REI > 80."""
    r = _td_rei(close, high, low)
    return (r > 80).astype(float).rolling(WDAYS, min_periods=1).sum().diff().diff().diff()

def f34_tdsq_421_rei_max_in_5d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Max REI over trailing 5d."""
    return _td_rei(close, high, low).rolling(WDAYS, min_periods=1).max().diff().diff().diff()

def f34_tdsq_422_rei_max_in_63d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Max REI over trailing 63d."""
    return _td_rei(close, high, low).rolling(QDAYS, min_periods=MDAYS).max().diff().diff().diff()

def f34_tdsq_423_bars_since_rei_above_80_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since REI was last above 80."""
    return _bars_since_true((_td_rei(close, high, low) > 80).astype(float)).diff().diff().diff()

def f34_tdsq_424_rei_zscore_252d_at_setup_9_bar_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """REI z-score(252d) captured at most-recent setup-9 bar (held forward)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    return _value_at_event(_rolling_zscore(_td_rei(close, high, low), YDAYS), fires).diff().diff().diff()

def f34_tdsq_425_rei_above_60_count_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of trailing 252d bars where REI > 60."""
    r = _td_rei(close, high, low)
    return (r > 60).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f34_tdsq_426_log_dist_close_to_252d_max_at_setup_9_d3(close: pd.Series) -> pd.Series:
    """Log distance close-to-252d-max captured at most-recent setup-9 bar."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return _value_at_event(_safe_log(close) - _safe_log(rmax), fires).diff().diff().diff()

def f34_tdsq_427_log_dist_close_to_504d_max_at_setup_9_d3(close: pd.Series) -> pd.Series:
    """Log distance close-to-504d-max captured at most-recent setup-9 bar."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    rmax = close.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    return _value_at_event(_safe_log(close) - _safe_log(rmax), fires).diff().diff().diff()

def f34_tdsq_428_log_dist_close_to_1260d_max_at_setup_9_d3(close: pd.Series) -> pd.Series:
    """Log distance close-to-1260d-max captured at most-recent setup-9 bar."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    rmax = close.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    return _value_at_event(_safe_log(close) - _safe_log(rmax), fires).diff().diff().diff()

def f34_tdsq_429_atr_dist_close_to_252d_max_at_setup_9_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """(close - 252d-max) / ATR(21) captured at most-recent setup-9 bar."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dist = _safe_div(close - rmax, _atr(high, low, close, MDAYS))
    return _value_at_event(dist, fires).diff().diff().diff()

def f34_tdsq_430_close_pct_rank_252d_at_setup_9_d3(close: pd.Series) -> pd.Series:
    """Close 252d-pct-rank captured at most-recent setup-9 bar."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    return _value_at_event(_pct_rank(close, YDAYS), fires).diff().diff().diff()

def f34_tdsq_431_close_pct_rank_1260d_at_setup_9_d3(close: pd.Series) -> pd.Series:
    """Close 1260d-pct-rank captured at most-recent setup-9 bar."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    return _value_at_event(_pct_rank(close, DDAYS_5Y), fires).diff().diff().diff()

def f34_tdsq_432_log_dist_close_to_252d_max_at_countdown_13_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Log dist close-to-252d-max captured at most-recent countdown-13 fire bar."""
    cd = _td_sell_countdown_count(close, high, low)
    fire = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return _value_at_event(_safe_log(close) - _safe_log(rmax), fire).diff().diff().diff()

def f34_tdsq_433_log_dist_close_to_1260d_max_at_countdown_13_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Log dist close-to-1260d-max captured at most-recent countdown-13 fire bar."""
    cd = _td_sell_countdown_count(close, high, low)
    fire = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    rmax = close.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    return _value_at_event(_safe_log(close) - _safe_log(rmax), fire).diff().diff().diff()

def f34_tdsq_434_close_pct_rank_252d_at_perfected_setup_9_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Close 252d-pct-rank captured at most-recent PERFECTED setup-9 bar."""
    fires = _td_perfected_sell_setup_9_event(close, high)
    return _value_at_event(_pct_rank(close, YDAYS), fires).diff().diff().diff()

def f34_tdsq_435_close_pct_rank_252d_at_combo_13_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Close 252d-pct-rank captured at most-recent TD Combo-13 fire bar."""
    cb = _td_sell_combo_count(close, high)
    fire = ((cb == 13) & (cb.shift(1) < 13)).astype(float)
    return _value_at_event(_pct_rank(close, YDAYS), fire).diff().diff().diff()

def f34_tdsq_436_bars_between_last_setup_9_and_last_perfected_9_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Bars between most-recent setup-9 and most-recent perfected-9 (positive = perfected before normal)."""
    s9 = _bars_since_true((_td_sell_setup_count(close) == 9).astype(float))
    p9 = _bars_since_true(_td_perfected_sell_setup_9_event(close, high))
    return (p9 - s9).diff().diff().diff()

def f34_tdsq_437_bars_between_last_setup_9_and_last_countdown_13_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars between most-recent setup-9 and most-recent countdown-13."""
    cd = _td_sell_countdown_count(close, high, low)
    c13 = _bars_since_true(((cd == 13) & (cd.shift(1) < 13)).astype(float))
    s9 = _bars_since_true((_td_sell_setup_count(close) == 9).astype(float))
    return (c13 - s9).diff().diff().diff()

def f34_tdsq_438_bars_between_last_countdown_13_and_last_combo_13_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars between most-recent countdown-13 and most-recent combo-13."""
    cd = _td_sell_countdown_count(close, high, low)
    cb = _td_sell_combo_count(close, high)
    c13 = _bars_since_true(((cd == 13) & (cd.shift(1) < 13)).astype(float))
    cb13 = _bars_since_true(((cb == 13) & (cb.shift(1) < 13)).astype(float))
    return (cb13 - c13).diff().diff().diff()

def f34_tdsq_439_was_setup_9_followed_by_countdown_13_within_42d_indicator_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when a setup-9 fired within the last 42d AND a countdown-13 has fired since."""
    sc = _td_sell_setup_count(close)
    setup_recent = (sc == 9).astype(float).rolling(42, min_periods=1).max()
    cd = _td_sell_countdown_count(close, high, low)
    cd_fire_recent = ((cd == 13) & (cd.shift(1) < 13)).astype(float).rolling(42, min_periods=1).max()
    return (setup_recent * cd_fire_recent).where(setup_recent.notna() & cd_fire_recent.notna(), np.nan).diff().diff().diff()

def f34_tdsq_440_was_setup_9_followed_by_termination_within_42d_indicator_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when setup-9 fired within last 42d AND countdown terminated (reset from >0 to 0) since."""
    sc = _td_sell_setup_count(close)
    setup_recent = (sc == 9).astype(float).rolling(42, min_periods=1).max()
    cd = _td_sell_countdown_count(close, high, low)
    term_recent = ((cd == 0) & (cd.shift(1) > 0)).astype(float).rolling(42, min_periods=1).max()
    return (setup_recent * term_recent).where(setup_recent.notna() & term_recent.notna(), np.nan).diff().diff().diff()

def f34_tdsq_441_count_setup_9_followed_by_completion_in_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of trailing 252d setup-9 events that resulted in subsequent countdown-13 completion within 42d."""
    sc = _td_sell_setup_count(close)
    setup_events = (sc == 9).astype(int)
    cd = _td_sell_countdown_count(close, high, low)
    cd_fire = ((cd == 13) & (cd.shift(1) < 13)).astype(int)
    cd_within_42d_forward = cd_fire.rolling(42, min_periods=1).max().shift(41).fillna(0)
    confirmed = (setup_events * cd_within_42d_forward).shift(42).fillna(0)
    return confirmed.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f34_tdsq_442_count_setup_9_followed_by_termination_in_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of trailing 252d setup-9 events that resulted in subsequent countdown termination within 42d."""
    sc = _td_sell_setup_count(close)
    setup_events = (sc == 9).astype(int)
    cd = _td_sell_countdown_count(close, high, low)
    term = ((cd == 0) & (cd.shift(1) > 0)).astype(int)
    term_within_42d_forward = term.rolling(42, min_periods=1).max().shift(41).fillna(0)
    failed = (setup_events * term_within_42d_forward).shift(42).fillna(0)
    return failed.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f34_tdsq_443_ratio_setup9_to_countdown13_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio: trailing 252d setup-9 count / trailing 252d countdown-13 count."""
    s = (_td_sell_setup_count(close) == 9).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    cd = _td_sell_countdown_count(close, high, low)
    c = ((cd == 13) & (cd.shift(1) < 13)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(s, c).diff().diff().diff()

def f34_tdsq_444_ratio_setup9_to_perfected9_252d_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Ratio: trailing 252d setup-9 count / trailing 252d perfected-9 count."""
    s = (_td_sell_setup_count(close) == 9).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    p = _td_perfected_sell_setup_9_event(close, high).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(s, p).diff().diff().diff()

def f34_tdsq_445_ratio_completion_to_termination_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio: trailing 252d countdown-13 completions / trailing 252d countdown-terminations."""
    cd = _td_sell_countdown_count(close, high, low)
    c = ((cd == 13) & (cd.shift(1) < 13)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    t = ((cd == 0) & (cd.shift(1) > 0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(c, t).diff().diff().diff()

def f34_tdsq_446_setup_9_with_close_above_open_indicator_d3(close: pd.Series, open: pd.Series) -> pd.Series:
    """+1 when setup-9 fires AND today's close > today's open (bullish bar at setup-9)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    bullish = (close > open).astype(float)
    return (fires * bullish).where(fires.notna() & bullish.notna(), np.nan).diff().diff().diff()

def f34_tdsq_447_setup_9_with_close_below_open_indicator_d3(close: pd.Series, open: pd.Series) -> pd.Series:
    """+1 when setup-9 fires AND today's close < today's open (bearish bar at setup-9 — already weak)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    bearish = (close < open).astype(float)
    return (fires * bearish).where(fires.notna() & bearish.notna(), np.nan).diff().diff().diff()

def f34_tdsq_448_setup_9_open_in_lower_half_of_prior_bar_indicator_d3(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when setup-9 fires AND today's open is in lower 50% of prior bar's range."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    rng_p = (high.shift(1) - low.shift(1)).replace(0, np.nan)
    pos = _safe_div(open - low.shift(1), rng_p)
    return (fires * (pos < 0.5).astype(float)).where(fires.notna() & pos.notna(), np.nan).diff().diff().diff()

def f34_tdsq_449_setup_9_open_in_upper_half_of_prior_bar_indicator_d3(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when setup-9 fires AND today's open is in upper 50% of prior bar's range."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    rng_p = (high.shift(1) - low.shift(1)).replace(0, np.nan)
    pos = _safe_div(open - low.shift(1), rng_p)
    return (fires * (pos >= 0.5).astype(float)).where(fires.notna() & pos.notna(), np.nan).diff().diff().diff()

def f34_tdsq_450_setup_9_outside_bar_indicator_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when setup-9 fires AND today's range FULLY contains prior bar (high > prior high AND low < prior low)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    outside = ((high > high.shift(1)) & (low < low.shift(1))).astype(float)
    return (fires * outside).where(fires.notna() & outside.notna(), np.nan).diff().diff().diff()
TD_SEQUENTIAL_DEMARK_D3_REGISTRY_376_450 = {'f34_tdsq_376_setup_count_at_or_above_5_indicator_d3': {'inputs': ['close'], 'func': f34_tdsq_376_setup_count_at_or_above_5_indicator_d3}, 'f34_tdsq_377_setup_count_at_or_above_7_indicator_d3': {'inputs': ['close'], 'func': f34_tdsq_377_setup_count_at_or_above_7_indicator_d3}, 'f34_tdsq_378_setup_count_exactly_8_indicator_d3': {'inputs': ['close'], 'func': f34_tdsq_378_setup_count_exactly_8_indicator_d3}, 'f34_tdsq_379_setup_count_above_9_indicator_d3': {'inputs': ['close'], 'func': f34_tdsq_379_setup_count_above_9_indicator_d3}, 'f34_tdsq_380_setup_count_at_3_indicator_d3': {'inputs': ['close'], 'func': f34_tdsq_380_setup_count_at_3_indicator_d3}, 'f34_tdsq_381_setup_count_at_6_indicator_d3': {'inputs': ['close'], 'func': f34_tdsq_381_setup_count_at_6_indicator_d3}, 'f34_tdsq_382_buy_setup_count_active_indicator_d3': {'inputs': ['close'], 'func': f34_tdsq_382_buy_setup_count_active_indicator_d3}, 'f34_tdsq_383_max_setup_or_buy_count_value_d3': {'inputs': ['close'], 'func': f34_tdsq_383_max_setup_or_buy_count_value_d3}, 'f34_tdsq_384_setup_count_top_quintile_252d_d3': {'inputs': ['close'], 'func': f34_tdsq_384_setup_count_top_quintile_252d_d3}, 'f34_tdsq_385_setup_count_above_5_persistence_21d_d3': {'inputs': ['close'], 'func': f34_tdsq_385_setup_count_above_5_persistence_21d_d3}, 'f34_tdsq_386_volume_zscore_at_countdown_1_bar_d3': {'inputs': ['close', 'high', 'low', 'volume'], 'func': f34_tdsq_386_volume_zscore_at_countdown_1_bar_d3}, 'f34_tdsq_387_volume_zscore_at_countdown_5_bar_d3': {'inputs': ['close', 'high', 'low', 'volume'], 'func': f34_tdsq_387_volume_zscore_at_countdown_5_bar_d3}, 'f34_tdsq_388_volume_zscore_at_countdown_13_bar_d3': {'inputs': ['close', 'high', 'low', 'volume'], 'func': f34_tdsq_388_volume_zscore_at_countdown_13_bar_d3}, 'f34_tdsq_389_vol_progression_at_countdown_13_over_1_d3': {'inputs': ['close', 'high', 'low', 'volume'], 'func': f34_tdsq_389_vol_progression_at_countdown_13_over_1_d3}, 'f34_tdsq_390_countdown_13_on_high_volume_count_252d_d3': {'inputs': ['close', 'high', 'low', 'volume'], 'func': f34_tdsq_390_countdown_13_on_high_volume_count_252d_d3}, 'f34_tdsq_391_countdown_13_on_low_volume_count_252d_d3': {'inputs': ['close', 'high', 'low', 'volume'], 'func': f34_tdsq_391_countdown_13_on_low_volume_count_252d_d3}, 'f34_tdsq_392_dollar_vol_pct_rank_252d_at_countdown_13_bar_d3': {'inputs': ['close', 'high', 'low', 'volume'], 'func': f34_tdsq_392_dollar_vol_pct_rank_252d_at_countdown_13_bar_d3}, 'f34_tdsq_393_vol_zscore_at_combo_13_bar_d3': {'inputs': ['close', 'high', 'volume'], 'func': f34_tdsq_393_vol_zscore_at_combo_13_bar_d3}, 'f34_tdsq_394_bar_range_atr_norm_at_countdown_13_bar_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_394_bar_range_atr_norm_at_countdown_13_bar_d3}, 'f34_tdsq_395_gap_pct_at_countdown_13_bar_d3': {'inputs': ['close', 'open', 'high', 'low'], 'func': f34_tdsq_395_gap_pct_at_countdown_13_bar_d3}, 'f34_tdsq_396_count_high_vol_bars_during_last_setup_252d_d3': {'inputs': ['close', 'volume'], 'func': f34_tdsq_396_count_high_vol_bars_during_last_setup_252d_d3}, 'f34_tdsq_397_count_wide_range_bars_during_last_setup_252d_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_397_count_wide_range_bars_during_last_setup_252d_d3}, 'f34_tdsq_398_count_gap_up_bars_during_last_setup_252d_d3': {'inputs': ['close', 'open', 'high'], 'func': f34_tdsq_398_count_gap_up_bars_during_last_setup_252d_d3}, 'f34_tdsq_399_count_doji_bars_during_last_setup_252d_d3': {'inputs': ['close', 'open', 'high', 'low'], 'func': f34_tdsq_399_count_doji_bars_during_last_setup_252d_d3}, 'f34_tdsq_400_max_vol_zscore_during_last_setup_252d_d3': {'inputs': ['close', 'volume'], 'func': f34_tdsq_400_max_vol_zscore_during_last_setup_252d_d3}, 'f34_tdsq_401_mean_vol_zscore_during_last_setup_252d_d3': {'inputs': ['close', 'volume'], 'func': f34_tdsq_401_mean_vol_zscore_during_last_setup_252d_d3}, 'f34_tdsq_402_max_bar_range_atr_norm_during_last_setup_252d_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_402_max_bar_range_atr_norm_during_last_setup_252d_d3}, 'f34_tdsq_403_setup_breakaway_gap_at_1_indicator_d3': {'inputs': ['close', 'open', 'high'], 'func': f34_tdsq_403_setup_breakaway_gap_at_1_indicator_d3}, 'f34_tdsq_404_setup_exhaustion_gap_at_9_indicator_d3': {'inputs': ['close', 'open', 'high'], 'func': f34_tdsq_404_setup_exhaustion_gap_at_9_indicator_d3}, 'f34_tdsq_405_setup_run_through_count_252d_d3': {'inputs': ['close'], 'func': f34_tdsq_405_setup_run_through_count_252d_d3}, 'f34_tdsq_406_td_waldo_4_bearish_event_indicator_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_406_td_waldo_4_bearish_event_indicator_d3}, 'f34_tdsq_407_td_waldo_6_bearish_event_indicator_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_407_td_waldo_6_bearish_event_indicator_d3}, 'f34_tdsq_408_td_waldo_7_bearish_event_indicator_d3': {'inputs': ['close', 'high'], 'func': f34_tdsq_408_td_waldo_7_bearish_event_indicator_d3}, 'f34_tdsq_409_td_waldo_8_bearish_event_indicator_d3': {'inputs': ['open', 'close', 'high'], 'func': f34_tdsq_409_td_waldo_8_bearish_event_indicator_d3}, 'f34_tdsq_410_td_waldo_count_5patterns_252d_d3': {'inputs': ['open', 'close', 'high', 'low'], 'func': f34_tdsq_410_td_waldo_count_5patterns_252d_d3}, 'f34_tdsq_411_bars_since_td_waldo_4_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_411_bars_since_td_waldo_4_d3}, 'f34_tdsq_412_bars_since_td_waldo_6_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_412_bars_since_td_waldo_6_d3}, 'f34_tdsq_413_bars_since_td_waldo_7_d3': {'inputs': ['close', 'high'], 'func': f34_tdsq_413_bars_since_td_waldo_7_d3}, 'f34_tdsq_414_bars_since_td_waldo_8_d3': {'inputs': ['open', 'close', 'high'], 'func': f34_tdsq_414_bars_since_td_waldo_8_d3}, 'f34_tdsq_415_td_waldo_alignment_3of4_in_5d_indicator_d3': {'inputs': ['open', 'close', 'high', 'low'], 'func': f34_tdsq_415_td_waldo_alignment_3of4_in_5d_indicator_d3}, 'f34_tdsq_416_rei_above_80_indicator_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_416_rei_above_80_indicator_d3}, 'f34_tdsq_417_rei_below_40_indicator_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_417_rei_below_40_indicator_d3}, 'f34_tdsq_418_rei_above_60_persistence_5d_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_418_rei_above_60_persistence_5d_d3}, 'f34_tdsq_419_rei_above_60_persistence_21d_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_419_rei_above_60_persistence_21d_d3}, 'f34_tdsq_420_rei_above_80_persistence_5d_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_420_rei_above_80_persistence_5d_d3}, 'f34_tdsq_421_rei_max_in_5d_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_421_rei_max_in_5d_d3}, 'f34_tdsq_422_rei_max_in_63d_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_422_rei_max_in_63d_d3}, 'f34_tdsq_423_bars_since_rei_above_80_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_423_bars_since_rei_above_80_d3}, 'f34_tdsq_424_rei_zscore_252d_at_setup_9_bar_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_424_rei_zscore_252d_at_setup_9_bar_d3}, 'f34_tdsq_425_rei_above_60_count_252d_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_425_rei_above_60_count_252d_d3}, 'f34_tdsq_426_log_dist_close_to_252d_max_at_setup_9_d3': {'inputs': ['close'], 'func': f34_tdsq_426_log_dist_close_to_252d_max_at_setup_9_d3}, 'f34_tdsq_427_log_dist_close_to_504d_max_at_setup_9_d3': {'inputs': ['close'], 'func': f34_tdsq_427_log_dist_close_to_504d_max_at_setup_9_d3}, 'f34_tdsq_428_log_dist_close_to_1260d_max_at_setup_9_d3': {'inputs': ['close'], 'func': f34_tdsq_428_log_dist_close_to_1260d_max_at_setup_9_d3}, 'f34_tdsq_429_atr_dist_close_to_252d_max_at_setup_9_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_429_atr_dist_close_to_252d_max_at_setup_9_d3}, 'f34_tdsq_430_close_pct_rank_252d_at_setup_9_d3': {'inputs': ['close'], 'func': f34_tdsq_430_close_pct_rank_252d_at_setup_9_d3}, 'f34_tdsq_431_close_pct_rank_1260d_at_setup_9_d3': {'inputs': ['close'], 'func': f34_tdsq_431_close_pct_rank_1260d_at_setup_9_d3}, 'f34_tdsq_432_log_dist_close_to_252d_max_at_countdown_13_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_432_log_dist_close_to_252d_max_at_countdown_13_d3}, 'f34_tdsq_433_log_dist_close_to_1260d_max_at_countdown_13_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_433_log_dist_close_to_1260d_max_at_countdown_13_d3}, 'f34_tdsq_434_close_pct_rank_252d_at_perfected_setup_9_d3': {'inputs': ['close', 'high'], 'func': f34_tdsq_434_close_pct_rank_252d_at_perfected_setup_9_d3}, 'f34_tdsq_435_close_pct_rank_252d_at_combo_13_d3': {'inputs': ['close', 'high'], 'func': f34_tdsq_435_close_pct_rank_252d_at_combo_13_d3}, 'f34_tdsq_436_bars_between_last_setup_9_and_last_perfected_9_d3': {'inputs': ['close', 'high'], 'func': f34_tdsq_436_bars_between_last_setup_9_and_last_perfected_9_d3}, 'f34_tdsq_437_bars_between_last_setup_9_and_last_countdown_13_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_437_bars_between_last_setup_9_and_last_countdown_13_d3}, 'f34_tdsq_438_bars_between_last_countdown_13_and_last_combo_13_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_438_bars_between_last_countdown_13_and_last_combo_13_d3}, 'f34_tdsq_439_was_setup_9_followed_by_countdown_13_within_42d_indicator_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_439_was_setup_9_followed_by_countdown_13_within_42d_indicator_d3}, 'f34_tdsq_440_was_setup_9_followed_by_termination_within_42d_indicator_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_440_was_setup_9_followed_by_termination_within_42d_indicator_d3}, 'f34_tdsq_441_count_setup_9_followed_by_completion_in_252d_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_441_count_setup_9_followed_by_completion_in_252d_d3}, 'f34_tdsq_442_count_setup_9_followed_by_termination_in_252d_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_442_count_setup_9_followed_by_termination_in_252d_d3}, 'f34_tdsq_443_ratio_setup9_to_countdown13_252d_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_443_ratio_setup9_to_countdown13_252d_d3}, 'f34_tdsq_444_ratio_setup9_to_perfected9_252d_d3': {'inputs': ['close', 'high'], 'func': f34_tdsq_444_ratio_setup9_to_perfected9_252d_d3}, 'f34_tdsq_445_ratio_completion_to_termination_252d_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_445_ratio_completion_to_termination_252d_d3}, 'f34_tdsq_446_setup_9_with_close_above_open_indicator_d3': {'inputs': ['close', 'open'], 'func': f34_tdsq_446_setup_9_with_close_above_open_indicator_d3}, 'f34_tdsq_447_setup_9_with_close_below_open_indicator_d3': {'inputs': ['close', 'open'], 'func': f34_tdsq_447_setup_9_with_close_below_open_indicator_d3}, 'f34_tdsq_448_setup_9_open_in_lower_half_of_prior_bar_indicator_d3': {'inputs': ['close', 'open', 'high', 'low'], 'func': f34_tdsq_448_setup_9_open_in_lower_half_of_prior_bar_indicator_d3}, 'f34_tdsq_449_setup_9_open_in_upper_half_of_prior_bar_indicator_d3': {'inputs': ['close', 'open', 'high', 'low'], 'func': f34_tdsq_449_setup_9_open_in_upper_half_of_prior_bar_indicator_d3}, 'f34_tdsq_450_setup_9_outside_bar_indicator_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_450_setup_9_outside_bar_indicator_d3}}