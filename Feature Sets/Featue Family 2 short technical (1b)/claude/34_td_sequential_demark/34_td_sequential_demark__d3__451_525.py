"""34_td_sequential_demark d3 features 451-525 — order-3 difference of corresponding base features.

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

def _pct_rank(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).rank(pct=True)

def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=n).mean()

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

def _td_aggressive_buy_countdown_count(close: pd.Series, low: pd.Series) -> pd.Series:
    """Aggressive TD BUY countdown: low <= low[t-2] qualifies, started by buy-setup-9, reset by sell-setup-9."""
    sc = _td_sell_setup_count(close).values
    bc = _td_buy_setup_count(close).values
    lo = low.values
    n = len(close)
    out = np.zeros(n)
    active = False
    cnt = 0
    for i in range(n):
        if not active and i >= 8 and (bc[i] >= 9):
            active = True
            cnt = 0
        if active and i >= 8 and (sc[i] >= 9):
            active = False
            cnt = 0
        if active:
            if i >= 2 and lo[i] <= lo[i - 2] and (cnt < 13):
                cnt += 1
            out[i] = cnt
    return pd.Series(out, index=close.index)

def _td_risk_level_setup_9(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """TD Risk Level: at most-recent setup-9 bar, takes the highest high of last 3 setup bars (7/8/9)
    plus that bar's true-range — provides a stop-loss reference. Held forward."""
    sc = _td_sell_setup_count(close)
    setup_high_max3 = high.rolling(3, min_periods=1).max()
    tr = _true_range(high, low, close)
    fires = (sc == 9).astype(float)
    risk_level = setup_high_max3 + tr
    return _value_at_event(risk_level, fires)

def _td_risk_level_perfected_setup_9(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """TD Risk Level at perfected setup-9 events (more selective)."""
    pf = _td_perfected_sell_setup_9_event(close, high)
    setup_high_max3 = high.rolling(3, min_periods=1).max()
    tr = _true_range(high, low, close)
    return _value_at_event(setup_high_max3 + tr, pf)

def _rsi_wilder(close, n=14):
    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = (-delta).clip(lower=0)
    ag = gain.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    al = loss.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    return 100.0 - 100.0 / (1.0 + _safe_div(ag, al))

def _stoch_k(high, low, close, n=14):
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    return 100.0 * _safe_div(close - ll, hh - ll)

def _mfi(high, low, close, volume, n=14):
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    delta = tp.diff()
    pos = rmf.where(delta > 0, 0).rolling(n, min_periods=max(n // 3, 2)).sum()
    neg = rmf.where(delta < 0, 0).rolling(n, min_periods=max(n // 3, 2)).sum()
    mr = _safe_div(pos, neg)
    return 100.0 - 100.0 / (1.0 + mr)

def _cci(high, low, close, n=20):
    tp = (high + low + close) / 3.0
    sma = tp.rolling(n, min_periods=max(n // 3, 2)).mean()
    mad = (tp - sma).abs().rolling(n, min_periods=max(n // 3, 2)).mean()
    return _safe_div(tp - sma, 0.015 * mad)

def _williams_r(high, low, close, n=14):
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    return -100.0 * _safe_div(hh - close, hh - ll)

def _bb_upper(close, n=20, k=2.5):
    m = _sma(close, n)
    sd = close.rolling(n, min_periods=max(n // 3, 2)).std()
    return m + k * sd

def f34_tdsq_451_td_risk_level_value_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """TD Risk Level: last setup-9 bar's max-3-bar high plus TR (held forward) — stop-loss reference."""
    return _td_risk_level_setup_9(close, high, low).diff().diff().diff()

def f34_tdsq_452_close_above_td_risk_level_indicator_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when close > TD Risk Level (setup-9 invalidation — bullish breakthrough)."""
    rl = _td_risk_level_setup_9(close, high, low)
    return (close > rl).astype(float).where(rl.notna(), np.nan).diff().diff().diff()

def f34_tdsq_453_days_since_close_above_td_risk_level_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since close was last above TD Risk Level."""
    rl = _td_risk_level_setup_9(close, high, low)
    flag = (close > rl).astype(float)
    return _bars_since_true(flag).diff().diff().diff()

def f34_tdsq_454_distance_close_to_td_risk_level_atr_norm_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """(close - TD Risk Level) / ATR(21) — signed distance in vol units."""
    rl = _td_risk_level_setup_9(close, high, low)
    return _safe_div(close - rl, _atr(high, low, close, MDAYS)).diff().diff().diff()

def f34_tdsq_455_distance_close_to_td_risk_level_pct_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """(close - TD Risk Level) / TD Risk Level — % distance."""
    rl = _td_risk_level_setup_9(close, high, low)
    return _safe_div(close - rl, rl).diff().diff().diff()

def f34_tdsq_456_td_risk_level_pct_rank_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of TD Risk Level within trailing 252d (relative-level position)."""
    return _pct_rank(_td_risk_level_setup_9(close, high, low), YDAYS).diff().diff().diff()

def f34_tdsq_457_bars_since_setup_9_below_risk_level_streak_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where close < TD Risk Level (signal intact)."""
    rl = _td_risk_level_setup_9(close, high, low)
    flag = (close < rl).astype(int).fillna(0)
    grp = (flag == 0).cumsum()
    return flag.groupby(grp).cumsum().astype(float).diff().diff().diff()

def f34_tdsq_458_td_risk_level_perfected_value_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """TD Risk Level at PERFECTED setup-9 events only — more selective stop-loss reference."""
    return _td_risk_level_perfected_setup_9(close, high, low).diff().diff().diff()

def f34_tdsq_459_close_above_perfected_td_risk_level_indicator_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when close > Perfected-setup-9 TD Risk Level."""
    rl = _td_risk_level_perfected_setup_9(close, high, low)
    return (close > rl).astype(float).where(rl.notna(), np.nan).diff().diff().diff()

def f34_tdsq_460_td_risk_level_at_close_252d_high_indicator_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when close > TD Risk Level AND close near 252d max (risk-level break at top)."""
    rl = _td_risk_level_setup_9(close, high, low)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return ((close > rl) & (near == 1)).astype(float).where(rl.notna() & near.notna(), np.nan).diff().diff().diff()

def f34_tdsq_461_continuation_bars_post_setup_9_above_setup_high_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Number of bars since most recent setup-9 where today's high > setup-9-bar's high (continuation count)."""
    sc = _td_sell_setup_count(close)
    fires = (sc == 9).astype(float)
    high_at_setup_9 = _value_at_event(high, fires)
    above = (high > high_at_setup_9).astype(int).fillna(0)
    grp = (above == 0).cumsum()
    return above.groupby(grp).cumsum().astype(float).diff().diff().diff()

def f34_tdsq_462_bars_since_setup_9_with_close_above_setup_9_close_d3(close: pd.Series) -> pd.Series:
    """Number of bars since most recent setup-9 where today's close > setup-9-bar's close."""
    sc = _td_sell_setup_count(close)
    fires = (sc == 9).astype(float)
    close_at_setup_9 = _value_at_event(close, fires)
    above = (close > close_at_setup_9).astype(int).fillna(0)
    grp = (above == 0).cumsum()
    return above.groupby(grp).cumsum().astype(float).diff().diff().diff()

def f34_tdsq_463_setup_9_followed_by_break_above_high_count_252d_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Count of trailing 252d bars where high broke above the last setup-9 high (continuation events)."""
    sc = _td_sell_setup_count(close)
    fires = (sc == 9).astype(float)
    high_at_setup_9 = _value_at_event(high, fires)
    return (high > high_at_setup_9).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f34_tdsq_464_setup_9_followed_by_break_below_low_count_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of trailing 252d bars where low broke below the last setup-9 low (confirmation events)."""
    sc = _td_sell_setup_count(close)
    fires = (sc == 9).astype(float)
    low_at_setup_9 = _value_at_event(low, fires)
    return (low < low_at_setup_9).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f34_tdsq_465_reset_after_setup_9_indicator_d3(close: pd.Series) -> pd.Series:
    """+1 when close < setup-9 bar's close (price retraced past setup completion — reset)."""
    sc = _td_sell_setup_count(close)
    fires = (sc == 9).astype(float)
    close_at_setup_9 = _value_at_event(close, fires)
    return (close < close_at_setup_9).astype(float).where(close_at_setup_9.notna(), np.nan).diff().diff().diff()

def f34_tdsq_466_bars_to_break_setup_9_high_from_event_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Bars since setup-9 fire where high first exceeded setup-9 high (held forward; NaN if not yet broken)."""
    sc = _td_sell_setup_count(close)
    fires = (sc == 9).astype(float)
    high_at_setup_9 = _value_at_event(high, fires)
    bars_since_setup_9 = _bars_since_true(fires)
    above = (high > high_at_setup_9).astype(int)
    first_break = (above & (above.cumsum() != above.cumsum().shift(1).fillna(0))).astype(float)
    return _value_at_event(bars_since_setup_9, first_break).diff().diff().diff()

def f34_tdsq_467_bars_to_break_setup_9_low_from_event_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since setup-9 fire where low first broke below setup-9 low."""
    sc = _td_sell_setup_count(close)
    fires = (sc == 9).astype(float)
    low_at_setup_9 = _value_at_event(low, fires)
    bars_since_setup_9 = _bars_since_true(fires)
    below = (low < low_at_setup_9).astype(int)
    first_break = (below & (below.cumsum() != below.cumsum().shift(1).fillna(0))).astype(float)
    return _value_at_event(bars_since_setup_9, first_break).diff().diff().diff()

def f34_tdsq_468_max_close_post_setup_9_252d_d3(close: pd.Series) -> pd.Series:
    """Maximum close observed in trailing 252d that occurred after a setup-9 event (held forward)."""
    sc = _td_sell_setup_count(close)
    fires = (sc == 9).astype(int).cumsum()
    by_group = close.groupby(fires).cummax()
    return by_group.where(fires > 0, np.nan).diff().diff().diff()

def f34_tdsq_469_min_close_post_setup_9_252d_d3(close: pd.Series) -> pd.Series:
    """Minimum close observed since most recent setup-9 event (held forward)."""
    sc = _td_sell_setup_count(close)
    fires = (sc == 9).astype(int).cumsum()
    by_group = close.groupby(fires).cummin()
    return by_group.where(fires > 0, np.nan).diff().diff().diff()

def f34_tdsq_470_retest_count_within_42d_post_setup_9_d3(close: pd.Series) -> pd.Series:
    """Count of bars within 42d post-setup-9 where close retraced below setup-9 close."""
    sc = _td_sell_setup_count(close)
    fires = (sc == 9).astype(float)
    close_at_setup_9 = _value_at_event(close, fires)
    below = (close < close_at_setup_9).astype(float)
    return below.rolling(42, min_periods=1).sum().diff().diff().diff()

def f34_tdsq_471_tr_at_countdown_1_held_forward_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range at the bar where countdown == 1 (held forward through countdown)."""
    cd = _td_sell_countdown_count(close, high, low)
    tr = _true_range(high, low, close)
    return tr.where(cd == 1, np.nan).ffill().diff().diff().diff()

def f34_tdsq_472_tr_at_countdown_5_held_forward_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range at countdown == 5 (held forward)."""
    cd = _td_sell_countdown_count(close, high, low)
    tr = _true_range(high, low, close)
    return tr.where(cd == 5, np.nan).ffill().diff().diff().diff()

def f34_tdsq_473_tr_at_countdown_13_held_forward_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range at countdown == 13 (held forward)."""
    cd = _td_sell_countdown_count(close, high, low)
    tr = _true_range(high, low, close)
    return tr.where(cd == 13, np.nan).ffill().diff().diff().diff()

def f34_tdsq_474_tr_progression_ratio_13_over_1_countdown_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """TR-at-countdown-13 / TR-at-countdown-1 (held forward) — vol-expansion through countdown."""
    cd = _td_sell_countdown_count(close, high, low)
    tr = _true_range(high, low, close)
    tr_1 = tr.where(cd == 1, np.nan).ffill()
    tr_13 = tr.where(cd == 13, np.nan).ffill()
    return _safe_div(tr_13, tr_1).diff().diff().diff()

def f34_tdsq_475_max_tr_during_last_countdown_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Max TR observed during the last countdown-active period (countdown > 0), held forward."""
    cd = _td_sell_countdown_count(close, high, low)
    tr = _true_range(high, low, close)
    tr_in_cd = tr.where(cd > 0, np.nan)
    return tr_in_cd.rolling(42, min_periods=1).max().ffill().diff().diff().diff()

def f34_tdsq_476_avg_tr_during_last_42d_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean TR over trailing 42d (typical countdown duration)."""
    return _true_range(high, low, close).rolling(42, min_periods=10).mean().diff().diff().diff()

def f34_tdsq_477_bar_range_progression_slope_countdown_5d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5d slope of bar-range, masked to countdown-active bars (held forward)."""
    cd = _td_sell_countdown_count(close, high, low)
    rng = high - low
    return _rolling_slope(rng, WDAYS).where(cd > 0, np.nan).ffill().diff().diff().diff()

def f34_tdsq_478_tr_zscore_252d_at_countdown_13_bar_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """TR z-score(252d) captured at most-recent countdown-13 fire bar (held forward)."""
    cd = _td_sell_countdown_count(close, high, low)
    fire = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    return _value_at_event(_rolling_zscore(_true_range(high, low, close), YDAYS), fire).diff().diff().diff()

def f34_tdsq_479_countdown_during_atr_expansion_indicator_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when countdown is currently active AND ATR21 > 1.5 × ATR252 (countdown in vol-expansion regime)."""
    cd_active = (_td_sell_countdown_count(close, high, low) > 0).astype(float)
    a21 = _atr(high, low, close, MDAYS)
    a252 = _atr(high, low, close, YDAYS)
    expand = (a21 > 1.5 * a252).astype(float)
    return (cd_active * expand).where(cd_active.notna() & expand.notna(), np.nan).diff().diff().diff()

def f34_tdsq_480_countdown_with_widening_ranges_indicator_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when last 5 countdown-active bars had increasing ranges (widening range during countdown)."""
    cd = _td_sell_countdown_count(close, high, low)
    rng = high - low
    in_cd = rng.where(cd > 0, np.nan)
    rng_slope = _rolling_slope(in_cd.ffill(), WDAYS)
    return ((cd > 0) & (rng_slope > 0)).astype(float).where(cd.notna() & rng_slope.notna(), np.nan).diff().diff().diff()

def f34_tdsq_481_vol_z_at_countdown_3_held_forward_d3(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol z-score(63d) captured at countdown == 3 (held forward)."""
    cd = _td_sell_countdown_count(close, high, low)
    return _rolling_zscore(volume, QDAYS).where(cd == 3, np.nan).ffill().diff().diff().diff()

def f34_tdsq_482_vol_z_at_countdown_8_held_forward_d3(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol z-score(63d) captured at countdown == 8."""
    cd = _td_sell_countdown_count(close, high, low)
    return _rolling_zscore(volume, QDAYS).where(cd == 8, np.nan).ffill().diff().diff().diff()

def f34_tdsq_483_vol_progression_ratio_13_over_5_countdown_d3(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol-at-countdown-13 / vol-at-countdown-5 (held forward) — late-stage vol growth."""
    cd = _td_sell_countdown_count(close, high, low)
    v5 = volume.where(cd == 5, np.nan).ffill()
    v13 = volume.where((cd == 13) & (cd.shift(1) < 13), np.nan).ffill()
    return _safe_div(v13, v5).diff().diff().diff()

def f34_tdsq_484_max_vol_z_during_last_countdown_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Maximum vol z-score(63d) observed during countdown-active bars in trailing 252d."""
    cd = _td_sell_countdown_count(close, high, low)
    vz_in_cd = _rolling_zscore(volume, QDAYS).where(cd > 0, np.nan)
    return vz_in_cd.rolling(YDAYS, min_periods=QDAYS).max().diff().diff().diff()

def f34_tdsq_485_mean_vol_z_during_last_countdown_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean vol z-score during countdown-active bars in trailing 252d."""
    cd = _td_sell_countdown_count(close, high, low)
    vz_in_cd = _rolling_zscore(volume, QDAYS).where(cd > 0, np.nan)
    return vz_in_cd.rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f34_tdsq_486_countdown_started_on_high_vol_indicator_d3(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 on bar where countdown started (count == 1) AND vol z(63) > 1 (conviction-start)."""
    cd = _td_sell_countdown_count(close, high, low)
    started = (cd == 1).astype(float)
    high_vol = (_rolling_zscore(volume, QDAYS) > 1.0).astype(float)
    return (started * high_vol).where(started.notna() & high_vol.notna(), np.nan).diff().diff().diff()

def f34_tdsq_487_countdown_completed_on_low_vol_indicator_d3(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 on countdown-13 fire bar where vol z(63) < -0.5 (no-conviction completion)."""
    cd = _td_sell_countdown_count(close, high, low)
    fire = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    low_vol = (_rolling_zscore(volume, QDAYS) < -0.5).astype(float)
    return (fire * low_vol).where(fire.notna() & low_vol.notna(), np.nan).diff().diff().diff()

def f34_tdsq_488_bars_in_last_countdown_with_top_decile_vol_d3(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of bars in trailing 42d with countdown > 0 AND vol in 252d top decile."""
    cd = _td_sell_countdown_count(close, high, low)
    in_cd = (cd > 0).astype(float)
    top_vol = (_pct_rank(volume, YDAYS) >= 0.9).astype(float)
    return (in_cd * top_vol).rolling(42, min_periods=5).sum().diff().diff().diff()

def f34_tdsq_489_countdown_vol_decay_indicator_d3(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when 5d-vol-slope < 0 AND countdown is currently active (vol declining during countdown)."""
    cd_active = (_td_sell_countdown_count(close, high, low) > 0).astype(float)
    v_slope = _rolling_slope(volume, WDAYS)
    return (cd_active * (v_slope < 0).astype(float)).where(cd_active.notna() & v_slope.notna(), np.nan).diff().diff().diff()

def f34_tdsq_490_countdown_vol_expansion_indicator_d3(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when 5d-vol-slope > 0 AND countdown is currently active (vol rising during countdown)."""
    cd_active = (_td_sell_countdown_count(close, high, low) > 0).astype(float)
    v_slope = _rolling_slope(volume, WDAYS)
    return (cd_active * (v_slope > 0).astype(float)).where(cd_active.notna() & v_slope.notna(), np.nan).diff().diff().diff()

def f34_tdsq_491_td_aggressive_buy_countdown_count_current_d3(close: pd.Series, low: pd.Series) -> pd.Series:
    """Current Aggressive TD BUY-countdown count (uses low <= low[t-2])."""
    return _td_aggressive_buy_countdown_count(close, low).diff().diff().diff()

def f34_tdsq_492_td_aggressive_buy_countdown_13_fires_indicator_d3(close: pd.Series, low: pd.Series) -> pd.Series:
    """+1 on bar where Aggressive Buy Countdown reaches 13."""
    cd = _td_aggressive_buy_countdown_count(close, low)
    return ((cd == 13) & (cd.shift(1) < 13)).astype(float).where(cd.notna() & cd.shift(1).notna(), np.nan).diff().diff().diff()

def f34_tdsq_493_days_since_aggressive_buy_countdown_13_d3(close: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since most recent Aggressive Buy Countdown-13 fire."""
    cd = _td_aggressive_buy_countdown_count(close, low)
    fire = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    return _bars_since_true(fire).diff().diff().diff()

def f34_tdsq_494_count_aggressive_buy_countdown_13_in_252d_d3(close: pd.Series, low: pd.Series) -> pd.Series:
    """Count of Aggressive Buy Countdown-13 fires in trailing 252d."""
    cd = _td_aggressive_buy_countdown_count(close, low)
    fire = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    return fire.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f34_tdsq_495_aggressive_buy_countdown_active_indicator_d3(close: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when Aggressive Buy Countdown is currently active (count > 0)."""
    cd = _td_aggressive_buy_countdown_count(close, low)
    return ((cd > 0) & (cd < 13)).astype(float).where(cd.notna(), np.nan).diff().diff().diff()

def f34_tdsq_496_aggressive_buy_countdown_progress_pct_d3(close: pd.Series, low: pd.Series) -> pd.Series:
    """Current Aggressive Buy Countdown count / 13."""
    return (_td_aggressive_buy_countdown_count(close, low) / 13.0).diff().diff().diff()

def f34_tdsq_497_aggressive_buy_countdown_max_252d_d3(close: pd.Series, low: pd.Series) -> pd.Series:
    """Max Aggressive Buy Countdown over trailing 252d."""
    return _td_aggressive_buy_countdown_count(close, low).rolling(YDAYS, min_periods=QDAYS).max().diff().diff().diff()

def f34_tdsq_498_aggressive_buy_countdown_recycled_indicator_252d_d3(close: pd.Series, low: pd.Series) -> pd.Series:
    """Count of trailing 252d bars where Aggressive Buy Countdown reset >0 → 0."""
    cd = _td_aggressive_buy_countdown_count(close, low)
    reset = ((cd == 0) & (cd.shift(1) > 0)).astype(float)
    return reset.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f34_tdsq_499_aggressive_buy_minus_sell_countdown_gap_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Aggressive-buy-countdown count minus aggressive-sell-countdown count (signed regime gauge)."""
    buy_cd = _td_aggressive_buy_countdown_count(close, low)
    sc = _td_sell_setup_count(close).values
    bc = _td_buy_setup_count(close).values
    hi = high.values
    n = len(close)
    sell_out = np.zeros(n)
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
            if i >= 2 and hi[i] >= hi[i - 2] and (cnt < 13):
                cnt += 1
            sell_out[i] = cnt
    sell_cd = pd.Series(sell_out, index=close.index)
    return (buy_cd - sell_cd).diff().diff().diff()

def f34_tdsq_500_aggressive_buy_countdown_13_at_close_252d_high_indicator_d3(close: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when Aggressive Buy Countdown-13 fires AND close within 1% of 252d max (rare — top exhaustion of dip-buyers)."""
    cd = _td_aggressive_buy_countdown_count(close, low)
    fire = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (fire * near).where(fire.notna() & near.notna(), np.nan).diff().diff().diff()

def f34_tdsq_501_bars_at_setup_count_2_in_21d_d3(close: pd.Series) -> pd.Series:
    """Count of trailing 21d bars where TD sell-setup count == 2."""
    sc = _td_sell_setup_count(close)
    return (sc == 2).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff().diff().diff()

def f34_tdsq_502_bars_at_setup_count_4_in_21d_d3(close: pd.Series) -> pd.Series:
    """Count of trailing 21d bars where TD sell-setup count == 4."""
    sc = _td_sell_setup_count(close)
    return (sc == 4).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff().diff().diff()

def f34_tdsq_503_bars_at_setup_count_6_in_21d_d3(close: pd.Series) -> pd.Series:
    """Count of trailing 21d bars where TD sell-setup count == 6."""
    sc = _td_sell_setup_count(close)
    return (sc == 6).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff().diff().diff()

def f34_tdsq_504_setup_started_within_5d_indicator_d3(close: pd.Series) -> pd.Series:
    """+1 when a new sell-setup started (count == 1) within trailing 5d."""
    sc = _td_sell_setup_count(close)
    started = (sc == 1).astype(float)
    return started.rolling(WDAYS, min_periods=1).max().where(sc.notna(), np.nan).diff().diff().diff()

def f34_tdsq_505_setup_started_within_21d_count_252d_d3(close: pd.Series) -> pd.Series:
    """Count of trailing 252d bars where sell-setup started (sc == 1)."""
    sc = _td_sell_setup_count(close)
    return (sc == 1).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f34_tdsq_506_time_since_setup_count_started_normalized_9_d3(close: pd.Series) -> pd.Series:
    """Bars-since-current-setup-started divided by 9 (normalized progress through setup)."""
    sc = _td_sell_setup_count(close)
    started = (sc == 1).astype(float)
    bars_since_start = _bars_since_true(started)
    return (bars_since_start / 9.0).diff().diff().diff()

def f34_tdsq_507_setup_count_change_1d_d3(close: pd.Series) -> pd.Series:
    """1-day change in TD sell-setup count."""
    return _td_sell_setup_count(close).diff().diff().diff().diff()

def f34_tdsq_508_setup_count_change_3d_d3(close: pd.Series) -> pd.Series:
    """3-day change in TD sell-setup count."""
    sc = _td_sell_setup_count(close)
    return (sc - sc.shift(3)).diff().diff().diff()

def f34_tdsq_509_setup_count_acceleration_5d_d3(close: pd.Series) -> pd.Series:
    """Slope-of-slope of TD sell-setup count over 5d (acceleration)."""
    sc = _td_sell_setup_count(close)
    s = _rolling_slope(sc, WDAYS)
    return _rolling_slope(s, WDAYS).diff().diff().diff()

def f34_tdsq_510_setup_count_velocity_zscore_252d_d3(close: pd.Series) -> pd.Series:
    """Z-score of 5d-slope of TD sell-setup count over 252d."""
    return _rolling_zscore(_rolling_slope(_td_sell_setup_count(close), WDAYS), YDAYS).diff().diff().diff()

def f34_tdsq_511_setup_count_skip_event_indicator_d3(close: pd.Series) -> pd.Series:
    """+1 on bar where TD sell-setup count jumped by >1 (impossible jump — usually anomaly or data gap)."""
    sc = _td_sell_setup_count(close)
    return (sc.diff() > 1).astype(float).where(sc.notna(), np.nan).diff().diff().diff()

def f34_tdsq_512_setup_count_stall_event_indicator_d3(close: pd.Series) -> pd.Series:
    """+1 when TD sell-setup count > 0 AND unchanged for last 2 bars (pause within setup)."""
    sc = _td_sell_setup_count(close)
    stall = ((sc > 0) & (sc == sc.shift(1)) & (sc.shift(1) == sc.shift(2))).astype(float)
    return stall.where(sc.notna() & sc.shift(2).notna(), np.nan).diff().diff().diff()

def f34_tdsq_513_setup_count_pause_during_active_setup_count_d3(close: pd.Series) -> pd.Series:
    """Count of bars in current setup where count did not increment from prior bar."""
    sc = _td_sell_setup_count(close)
    active = (sc > 0).astype(int)
    paused = ((sc > 0) & (sc == sc.shift(1))).astype(int)
    grp = (active == 0).cumsum()
    return paused.groupby(grp).cumsum().astype(float).diff().diff().diff()

def f34_tdsq_514_setup_progression_smoothness_index_d3(close: pd.Series) -> pd.Series:
    """Rolling-21d std of 1-day setup-count changes — low = smooth progression, high = choppy."""
    return _td_sell_setup_count(close).diff().rolling(MDAYS, min_periods=WDAYS).std().diff().diff().diff()

def f34_tdsq_515_setup_completion_within_9bars_indicator_d3(close: pd.Series) -> pd.Series:
    """+1 when last setup-9 fired in exactly 9 bars from start (clean run-through)."""
    sc = _td_sell_setup_count(close)
    started = (sc == 1).astype(float)
    bars_since_start = _bars_since_true(started)
    fires = (sc == 9).astype(float)
    last_time = _value_at_event(bars_since_start, fires)
    return (last_time == 8).astype(float).where(last_time.notna(), np.nan).diff().diff().diff()

def f34_tdsq_516_setup_9_with_rsi_above_80_indicator_d3(close: pd.Series) -> pd.Series:
    """+1 when setup-9 fires AND RSI(14) > 80 (severe overbought)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    rsi_extreme = (_rsi_wilder(close, 14) > 80).astype(float)
    return (fires * rsi_extreme).where(fires.notna() & rsi_extreme.notna(), np.nan).diff().diff().diff()

def f34_tdsq_517_setup_9_with_mfi_above_85_indicator_d3(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when setup-9 fires AND MFI(14) > 85 (severe money-flow overbought)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    mfi_extreme = (_mfi(high, low, close, volume, 14) > 85).astype(float)
    return (fires * mfi_extreme).where(fires.notna() & mfi_extreme.notna(), np.nan).diff().diff().diff()

def f34_tdsq_518_setup_9_with_stoch_above_90_indicator_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when setup-9 fires AND Stoch %K > 90 (extreme stoch overbought)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    stoch_extreme = (_stoch_k(high, low, close, 14) > 90).astype(float)
    return (fires * stoch_extreme).where(fires.notna() & stoch_extreme.notna(), np.nan).diff().diff().diff()

def f34_tdsq_519_setup_9_with_cci_above_200_indicator_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when setup-9 fires AND CCI(20) > +200 (extreme commodity-channel reading)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    cci_extreme = (_cci(high, low, close, 20) > 200).astype(float)
    return (fires * cci_extreme).where(fires.notna() & cci_extreme.notna(), np.nan).diff().diff().diff()

def f34_tdsq_520_setup_9_with_williams_r_above_minus_10_indicator_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when setup-9 fires AND Williams %R > -10 (extreme — top of range)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    wr_extreme = (_williams_r(high, low, close, 14) > -10).astype(float)
    return (fires * wr_extreme).where(fires.notna() & wr_extreme.notna(), np.nan).diff().diff().diff()

def f34_tdsq_521_countdown_13_with_rsi_above_80_indicator_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when countdown-13 fires AND RSI(14) > 80."""
    cd = _td_sell_countdown_count(close, high, low)
    fire = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    rsi_extreme = (_rsi_wilder(close, 14) > 80).astype(float)
    return (fire * rsi_extreme).where(fire.notna() & rsi_extreme.notna(), np.nan).diff().diff().diff()

def f34_tdsq_522_countdown_13_with_mfi_above_85_indicator_d3(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when countdown-13 fires AND MFI(14) > 85."""
    cd = _td_sell_countdown_count(close, high, low)
    fire = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    mfi_extreme = (_mfi(high, low, close, volume, 14) > 85).astype(float)
    return (fire * mfi_extreme).where(fire.notna() & mfi_extreme.notna(), np.nan).diff().diff().diff()

def f34_tdsq_523_countdown_13_with_stoch_above_90_indicator_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when countdown-13 fires AND Stoch %K > 90."""
    cd = _td_sell_countdown_count(close, high, low)
    fire = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    stoch_extreme = (_stoch_k(high, low, close, 14) > 90).astype(float)
    return (fire * stoch_extreme).where(fire.notna() & stoch_extreme.notna(), np.nan).diff().diff().diff()

def f34_tdsq_524_setup_9_with_close_above_bb_upper_2_5_indicator_d3(close: pd.Series) -> pd.Series:
    """+1 when setup-9 fires AND close > Bollinger upper band (20, 2.5×std) — extreme BB break."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    above_ubb = (close > _bb_upper(close, 20, 2.5)).astype(float)
    return (fires * above_ubb).where(fires.notna() & above_ubb.notna(), np.nan).diff().diff().diff()

def f34_tdsq_525_setup_9_with_atr_z_above_2_indicator_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when setup-9 fires AND ATR21 z-score(252d) > 2 (extreme vol regime at setup completion)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    atr_z_extreme = (_rolling_zscore(_atr(high, low, close, MDAYS), YDAYS) > 2.0).astype(float)
    return (fires * atr_z_extreme).where(fires.notna() & atr_z_extreme.notna(), np.nan).diff().diff().diff()
TD_SEQUENTIAL_DEMARK_D3_REGISTRY_451_525 = {'f34_tdsq_451_td_risk_level_value_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_451_td_risk_level_value_d3}, 'f34_tdsq_452_close_above_td_risk_level_indicator_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_452_close_above_td_risk_level_indicator_d3}, 'f34_tdsq_453_days_since_close_above_td_risk_level_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_453_days_since_close_above_td_risk_level_d3}, 'f34_tdsq_454_distance_close_to_td_risk_level_atr_norm_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_454_distance_close_to_td_risk_level_atr_norm_d3}, 'f34_tdsq_455_distance_close_to_td_risk_level_pct_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_455_distance_close_to_td_risk_level_pct_d3}, 'f34_tdsq_456_td_risk_level_pct_rank_252d_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_456_td_risk_level_pct_rank_252d_d3}, 'f34_tdsq_457_bars_since_setup_9_below_risk_level_streak_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_457_bars_since_setup_9_below_risk_level_streak_d3}, 'f34_tdsq_458_td_risk_level_perfected_value_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_458_td_risk_level_perfected_value_d3}, 'f34_tdsq_459_close_above_perfected_td_risk_level_indicator_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_459_close_above_perfected_td_risk_level_indicator_d3}, 'f34_tdsq_460_td_risk_level_at_close_252d_high_indicator_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_460_td_risk_level_at_close_252d_high_indicator_d3}, 'f34_tdsq_461_continuation_bars_post_setup_9_above_setup_high_d3': {'inputs': ['close', 'high'], 'func': f34_tdsq_461_continuation_bars_post_setup_9_above_setup_high_d3}, 'f34_tdsq_462_bars_since_setup_9_with_close_above_setup_9_close_d3': {'inputs': ['close'], 'func': f34_tdsq_462_bars_since_setup_9_with_close_above_setup_9_close_d3}, 'f34_tdsq_463_setup_9_followed_by_break_above_high_count_252d_d3': {'inputs': ['close', 'high'], 'func': f34_tdsq_463_setup_9_followed_by_break_above_high_count_252d_d3}, 'f34_tdsq_464_setup_9_followed_by_break_below_low_count_252d_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_464_setup_9_followed_by_break_below_low_count_252d_d3}, 'f34_tdsq_465_reset_after_setup_9_indicator_d3': {'inputs': ['close'], 'func': f34_tdsq_465_reset_after_setup_9_indicator_d3}, 'f34_tdsq_466_bars_to_break_setup_9_high_from_event_d3': {'inputs': ['close', 'high'], 'func': f34_tdsq_466_bars_to_break_setup_9_high_from_event_d3}, 'f34_tdsq_467_bars_to_break_setup_9_low_from_event_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_467_bars_to_break_setup_9_low_from_event_d3}, 'f34_tdsq_468_max_close_post_setup_9_252d_d3': {'inputs': ['close'], 'func': f34_tdsq_468_max_close_post_setup_9_252d_d3}, 'f34_tdsq_469_min_close_post_setup_9_252d_d3': {'inputs': ['close'], 'func': f34_tdsq_469_min_close_post_setup_9_252d_d3}, 'f34_tdsq_470_retest_count_within_42d_post_setup_9_d3': {'inputs': ['close'], 'func': f34_tdsq_470_retest_count_within_42d_post_setup_9_d3}, 'f34_tdsq_471_tr_at_countdown_1_held_forward_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_471_tr_at_countdown_1_held_forward_d3}, 'f34_tdsq_472_tr_at_countdown_5_held_forward_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_472_tr_at_countdown_5_held_forward_d3}, 'f34_tdsq_473_tr_at_countdown_13_held_forward_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_473_tr_at_countdown_13_held_forward_d3}, 'f34_tdsq_474_tr_progression_ratio_13_over_1_countdown_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_474_tr_progression_ratio_13_over_1_countdown_d3}, 'f34_tdsq_475_max_tr_during_last_countdown_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_475_max_tr_during_last_countdown_d3}, 'f34_tdsq_476_avg_tr_during_last_42d_252d_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_476_avg_tr_during_last_42d_252d_d3}, 'f34_tdsq_477_bar_range_progression_slope_countdown_5d_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_477_bar_range_progression_slope_countdown_5d_d3}, 'f34_tdsq_478_tr_zscore_252d_at_countdown_13_bar_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_478_tr_zscore_252d_at_countdown_13_bar_d3}, 'f34_tdsq_479_countdown_during_atr_expansion_indicator_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_479_countdown_during_atr_expansion_indicator_d3}, 'f34_tdsq_480_countdown_with_widening_ranges_indicator_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_480_countdown_with_widening_ranges_indicator_d3}, 'f34_tdsq_481_vol_z_at_countdown_3_held_forward_d3': {'inputs': ['close', 'high', 'low', 'volume'], 'func': f34_tdsq_481_vol_z_at_countdown_3_held_forward_d3}, 'f34_tdsq_482_vol_z_at_countdown_8_held_forward_d3': {'inputs': ['close', 'high', 'low', 'volume'], 'func': f34_tdsq_482_vol_z_at_countdown_8_held_forward_d3}, 'f34_tdsq_483_vol_progression_ratio_13_over_5_countdown_d3': {'inputs': ['close', 'high', 'low', 'volume'], 'func': f34_tdsq_483_vol_progression_ratio_13_over_5_countdown_d3}, 'f34_tdsq_484_max_vol_z_during_last_countdown_252d_d3': {'inputs': ['close', 'high', 'low', 'volume'], 'func': f34_tdsq_484_max_vol_z_during_last_countdown_252d_d3}, 'f34_tdsq_485_mean_vol_z_during_last_countdown_252d_d3': {'inputs': ['close', 'high', 'low', 'volume'], 'func': f34_tdsq_485_mean_vol_z_during_last_countdown_252d_d3}, 'f34_tdsq_486_countdown_started_on_high_vol_indicator_d3': {'inputs': ['close', 'high', 'low', 'volume'], 'func': f34_tdsq_486_countdown_started_on_high_vol_indicator_d3}, 'f34_tdsq_487_countdown_completed_on_low_vol_indicator_d3': {'inputs': ['close', 'high', 'low', 'volume'], 'func': f34_tdsq_487_countdown_completed_on_low_vol_indicator_d3}, 'f34_tdsq_488_bars_in_last_countdown_with_top_decile_vol_d3': {'inputs': ['close', 'high', 'low', 'volume'], 'func': f34_tdsq_488_bars_in_last_countdown_with_top_decile_vol_d3}, 'f34_tdsq_489_countdown_vol_decay_indicator_d3': {'inputs': ['close', 'high', 'low', 'volume'], 'func': f34_tdsq_489_countdown_vol_decay_indicator_d3}, 'f34_tdsq_490_countdown_vol_expansion_indicator_d3': {'inputs': ['close', 'high', 'low', 'volume'], 'func': f34_tdsq_490_countdown_vol_expansion_indicator_d3}, 'f34_tdsq_491_td_aggressive_buy_countdown_count_current_d3': {'inputs': ['close', 'low'], 'func': f34_tdsq_491_td_aggressive_buy_countdown_count_current_d3}, 'f34_tdsq_492_td_aggressive_buy_countdown_13_fires_indicator_d3': {'inputs': ['close', 'low'], 'func': f34_tdsq_492_td_aggressive_buy_countdown_13_fires_indicator_d3}, 'f34_tdsq_493_days_since_aggressive_buy_countdown_13_d3': {'inputs': ['close', 'low'], 'func': f34_tdsq_493_days_since_aggressive_buy_countdown_13_d3}, 'f34_tdsq_494_count_aggressive_buy_countdown_13_in_252d_d3': {'inputs': ['close', 'low'], 'func': f34_tdsq_494_count_aggressive_buy_countdown_13_in_252d_d3}, 'f34_tdsq_495_aggressive_buy_countdown_active_indicator_d3': {'inputs': ['close', 'low'], 'func': f34_tdsq_495_aggressive_buy_countdown_active_indicator_d3}, 'f34_tdsq_496_aggressive_buy_countdown_progress_pct_d3': {'inputs': ['close', 'low'], 'func': f34_tdsq_496_aggressive_buy_countdown_progress_pct_d3}, 'f34_tdsq_497_aggressive_buy_countdown_max_252d_d3': {'inputs': ['close', 'low'], 'func': f34_tdsq_497_aggressive_buy_countdown_max_252d_d3}, 'f34_tdsq_498_aggressive_buy_countdown_recycled_indicator_252d_d3': {'inputs': ['close', 'low'], 'func': f34_tdsq_498_aggressive_buy_countdown_recycled_indicator_252d_d3}, 'f34_tdsq_499_aggressive_buy_minus_sell_countdown_gap_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_499_aggressive_buy_minus_sell_countdown_gap_d3}, 'f34_tdsq_500_aggressive_buy_countdown_13_at_close_252d_high_indicator_d3': {'inputs': ['close', 'low'], 'func': f34_tdsq_500_aggressive_buy_countdown_13_at_close_252d_high_indicator_d3}, 'f34_tdsq_501_bars_at_setup_count_2_in_21d_d3': {'inputs': ['close'], 'func': f34_tdsq_501_bars_at_setup_count_2_in_21d_d3}, 'f34_tdsq_502_bars_at_setup_count_4_in_21d_d3': {'inputs': ['close'], 'func': f34_tdsq_502_bars_at_setup_count_4_in_21d_d3}, 'f34_tdsq_503_bars_at_setup_count_6_in_21d_d3': {'inputs': ['close'], 'func': f34_tdsq_503_bars_at_setup_count_6_in_21d_d3}, 'f34_tdsq_504_setup_started_within_5d_indicator_d3': {'inputs': ['close'], 'func': f34_tdsq_504_setup_started_within_5d_indicator_d3}, 'f34_tdsq_505_setup_started_within_21d_count_252d_d3': {'inputs': ['close'], 'func': f34_tdsq_505_setup_started_within_21d_count_252d_d3}, 'f34_tdsq_506_time_since_setup_count_started_normalized_9_d3': {'inputs': ['close'], 'func': f34_tdsq_506_time_since_setup_count_started_normalized_9_d3}, 'f34_tdsq_507_setup_count_change_1d_d3': {'inputs': ['close'], 'func': f34_tdsq_507_setup_count_change_1d_d3}, 'f34_tdsq_508_setup_count_change_3d_d3': {'inputs': ['close'], 'func': f34_tdsq_508_setup_count_change_3d_d3}, 'f34_tdsq_509_setup_count_acceleration_5d_d3': {'inputs': ['close'], 'func': f34_tdsq_509_setup_count_acceleration_5d_d3}, 'f34_tdsq_510_setup_count_velocity_zscore_252d_d3': {'inputs': ['close'], 'func': f34_tdsq_510_setup_count_velocity_zscore_252d_d3}, 'f34_tdsq_511_setup_count_skip_event_indicator_d3': {'inputs': ['close'], 'func': f34_tdsq_511_setup_count_skip_event_indicator_d3}, 'f34_tdsq_512_setup_count_stall_event_indicator_d3': {'inputs': ['close'], 'func': f34_tdsq_512_setup_count_stall_event_indicator_d3}, 'f34_tdsq_513_setup_count_pause_during_active_setup_count_d3': {'inputs': ['close'], 'func': f34_tdsq_513_setup_count_pause_during_active_setup_count_d3}, 'f34_tdsq_514_setup_progression_smoothness_index_d3': {'inputs': ['close'], 'func': f34_tdsq_514_setup_progression_smoothness_index_d3}, 'f34_tdsq_515_setup_completion_within_9bars_indicator_d3': {'inputs': ['close'], 'func': f34_tdsq_515_setup_completion_within_9bars_indicator_d3}, 'f34_tdsq_516_setup_9_with_rsi_above_80_indicator_d3': {'inputs': ['close'], 'func': f34_tdsq_516_setup_9_with_rsi_above_80_indicator_d3}, 'f34_tdsq_517_setup_9_with_mfi_above_85_indicator_d3': {'inputs': ['close', 'high', 'low', 'volume'], 'func': f34_tdsq_517_setup_9_with_mfi_above_85_indicator_d3}, 'f34_tdsq_518_setup_9_with_stoch_above_90_indicator_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_518_setup_9_with_stoch_above_90_indicator_d3}, 'f34_tdsq_519_setup_9_with_cci_above_200_indicator_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_519_setup_9_with_cci_above_200_indicator_d3}, 'f34_tdsq_520_setup_9_with_williams_r_above_minus_10_indicator_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_520_setup_9_with_williams_r_above_minus_10_indicator_d3}, 'f34_tdsq_521_countdown_13_with_rsi_above_80_indicator_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_521_countdown_13_with_rsi_above_80_indicator_d3}, 'f34_tdsq_522_countdown_13_with_mfi_above_85_indicator_d3': {'inputs': ['close', 'high', 'low', 'volume'], 'func': f34_tdsq_522_countdown_13_with_mfi_above_85_indicator_d3}, 'f34_tdsq_523_countdown_13_with_stoch_above_90_indicator_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_523_countdown_13_with_stoch_above_90_indicator_d3}, 'f34_tdsq_524_setup_9_with_close_above_bb_upper_2_5_indicator_d3': {'inputs': ['close'], 'func': f34_tdsq_524_setup_9_with_close_above_bb_upper_2_5_indicator_d3}, 'f34_tdsq_525_setup_9_with_atr_z_above_2_indicator_d3': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_525_setup_9_with_atr_z_above_2_indicator_d3}}