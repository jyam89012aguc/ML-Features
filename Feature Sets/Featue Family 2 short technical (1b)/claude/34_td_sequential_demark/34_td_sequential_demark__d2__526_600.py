"""34_td_sequential_demark d2 features 526-600 — order-2 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff().diff(). Self-contained; helpers redefined locally per HANDOFF."""
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

def _sma(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).mean()

def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=n).mean()

def _bars_since_true(flag):
    f = (flag.fillna(0) > 0).astype(int)
    idx = np.arange(len(f))
    last = np.where(f.values == 1, idx, np.nan)
    last_ffill = pd.Series(last, index=f.index).ffill()
    return pd.Series(idx, index=f.index) - last_ffill

def _value_at_event(value: pd.Series, event_flag: pd.Series) -> pd.Series:
    return value.where(event_flag.fillna(0) == 1, np.nan).ffill()

def _nth_most_recent_event_offset(flag, n_th, max_lookback):
    f = (flag.fillna(0) > 0).astype(int).values
    out = np.full(len(f), np.nan)
    for t in range(len(f)):
        start = max(0, t - max_lookback + 1)
        events = [i for i in range(t, start - 1, -1) if f[i] == 1]
        if len(events) >= n_th:
            out[t] = float(t - events[n_th - 1])
    return pd.Series(out, index=flag.index)

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

def _td_pivot_x(open_, high, low, close):
    """DeMark's conditional pivot base X. Uses prior bar's OHLC to project today's reference."""
    po = open_.shift(1)
    ph = high.shift(1)
    pl = low.shift(1)
    pc = close.shift(1)
    x = pd.Series(np.nan, index=close.index)
    x = x.mask(pc < po, ph + 2.0 * pl + pc)
    x = x.mask(pc > po, 2.0 * ph + pl + pc)
    x = x.mask(pc == po, ph + pl + 2.0 * pc)
    return x

def _td_pivot_mid(open_, high, low, close):
    """TD Pivot (mid) = X / 4."""
    return _td_pivot_x(open_, high, low, close) / 4.0

def _td_pivot_resistance(open_, high, low, close):
    """TD projected resistance = X/2 - prior low."""
    return _td_pivot_x(open_, high, low, close) / 2.0 - low.shift(1)

def _td_pivot_support(open_, high, low, close):
    """TD projected support = X/2 - prior high."""
    return _td_pivot_x(open_, high, low, close) / 2.0 - high.shift(1)

def _bb(close, n=20, k=2.0):
    m = _sma(close, n)
    sd = close.rolling(n, min_periods=max(n // 3, 2)).std()
    return (m, m + k * sd, m - k * sd)

def _keltner_upper(high, low, close, n=20, atr_mult=2.0):
    return _ema(close, n) + atr_mult * _atr(high, low, close, n)

def _td_event_panel(close, high, low):
    """Combined TD-event flag series: setup-9 + countdown-13-fire (events of interest)."""
    sc = _td_sell_setup_count(close)
    s9 = (sc == 9).astype(float).fillna(0)
    cd = _td_sell_countdown_count(close, high, low)
    c13 = ((cd == 13) & (cd.shift(1) < 13)).astype(float).fillna(0)
    return s9 + c13

def f34_tdsq_526_td_pivot_mid_value_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TD Pivot (mid) level — DeMark's conditional pivot projection."""
    return _td_pivot_mid(open, high, low, close).diff().diff()

def f34_tdsq_527_td_pivot_resistance_value_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TD projected resistance level (X/2 - prior low)."""
    return _td_pivot_resistance(open, high, low, close).diff().diff()

def f34_tdsq_528_td_pivot_support_value_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TD projected support level (X/2 - prior high)."""
    return _td_pivot_support(open, high, low, close).diff().diff()

def f34_tdsq_529_close_above_td_pivot_mid_indicator_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+1 when close > TD Pivot mid."""
    piv = _td_pivot_mid(open, high, low, close)
    return (close > piv).astype(float).where(piv.notna(), np.nan).diff().diff()

def f34_tdsq_530_close_above_td_pivot_resistance_indicator_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+1 when close > TD projected resistance (breakout above resistance)."""
    res = _td_pivot_resistance(open, high, low, close)
    return (close > res).astype(float).where(res.notna(), np.nan).diff().diff()

def f34_tdsq_531_close_below_td_pivot_support_indicator_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+1 when close < TD projected support (breakdown below support)."""
    sup = _td_pivot_support(open, high, low, close)
    return (close < sup).astype(float).where(sup.notna(), np.nan).diff().diff()

def f34_tdsq_532_distance_close_to_td_pivot_resistance_atr_norm_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - TD resistance) / ATR(21) — signed distance in vol units."""
    res = _td_pivot_resistance(open, high, low, close)
    return _safe_div(close - res, _atr(high, low, close, MDAYS)).diff().diff()

def f34_tdsq_533_distance_close_to_td_pivot_support_atr_norm_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - TD support) / ATR(21)."""
    sup = _td_pivot_support(open, high, low, close)
    return _safe_div(close - sup, _atr(high, low, close, MDAYS)).diff().diff()

def f34_tdsq_534_td_pivot_resistance_break_event_indicator_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+1 on bar where close newly crosses above TD resistance."""
    res = _td_pivot_resistance(open, high, low, close)
    above = (close > res).astype(int)
    return ((above == 1) & (above.shift(1) == 0)).astype(float).where(res.notna() & above.shift(1).notna(), np.nan).diff().diff()

def f34_tdsq_535_td_pivot_support_break_event_indicator_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+1 on bar where close newly crosses below TD support."""
    sup = _td_pivot_support(open, high, low, close)
    below = (close < sup).astype(int)
    return ((below == 1) & (below.shift(1) == 0)).astype(float).where(sup.notna() & below.shift(1).notna(), np.nan).diff().diff()

def f34_tdsq_536_td_pivot_resistance_break_count_252d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of TD resistance-break events in trailing 252d."""
    res = _td_pivot_resistance(open, high, low, close)
    above = (close > res).astype(int)
    flag = ((above == 1) & (above.shift(1) == 0)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f34_tdsq_537_td_pivot_support_break_count_252d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of TD support-break events in trailing 252d."""
    sup = _td_pivot_support(open, high, low, close)
    below = (close < sup).astype(int)
    flag = ((below == 1) & (below.shift(1) == 0)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f34_tdsq_538_close_position_in_td_pivot_band_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close position within the TD support-resistance band [0..1]."""
    res = _td_pivot_resistance(open, high, low, close)
    sup = _td_pivot_support(open, high, low, close)
    return _safe_div(close - sup, res - sup).diff().diff()

def f34_tdsq_539_td_pivot_resistance_failed_break_indicator_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+1 when close was > TD resistance 5 bars ago BUT < TD resistance today (failed break)."""
    res = _td_pivot_resistance(open, high, low, close)
    was_above = (close.shift(WDAYS) > res.shift(WDAYS)).astype(float)
    not_above = (close <= res).astype(float)
    return (was_above * not_above).where(res.notna() & res.shift(WDAYS).notna(), np.nan).diff().diff()

def f34_tdsq_540_td_pivot_resistance_break_at_252d_high_indicator_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+1 when close breaks above TD resistance AND close near 252d max."""
    res = _td_pivot_resistance(open, high, low, close)
    above = (close > res).astype(int)
    flag = ((above == 1) & (above.shift(1) == 0)).astype(float)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (flag * near).where(flag.notna() & near.notna(), np.nan).diff().diff()

def f34_tdsq_541_td_event_density_5d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of TD events (setup-9 + countdown-13) in trailing 5d."""
    return _td_event_panel(close, high, low).rolling(WDAYS, min_periods=1).sum().diff().diff()

def f34_tdsq_542_td_event_density_10d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of TD events in trailing 10d."""
    return _td_event_panel(close, high, low).rolling(10, min_periods=2).sum().diff().diff()

def f34_tdsq_543_td_event_density_21d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of TD events in trailing 21d."""
    return _td_event_panel(close, high, low).rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f34_tdsq_544_td_event_density_42d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of TD events in trailing 42d."""
    return _td_event_panel(close, high, low).rolling(42, min_periods=10).sum().diff().diff()

def f34_tdsq_545_td_event_density_63d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of TD events in trailing 63d."""
    return _td_event_panel(close, high, low).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f34_tdsq_546_td_event_density_21d_zscore_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of 21d TD-event density over 252d."""
    dens = _td_event_panel(close, high, low).rolling(MDAYS, min_periods=WDAYS).sum()
    return _rolling_zscore(dens, YDAYS).diff().diff()

def f34_tdsq_547_td_event_density_acceleration_5d_vs_21d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """TD-event density per day in 5d minus per day in 21d — clustering acceleration."""
    panel = _td_event_panel(close, high, low)
    d5 = panel.rolling(WDAYS, min_periods=1).sum() / WDAYS
    d21 = panel.rolling(MDAYS, min_periods=WDAYS).sum() / MDAYS
    return (d5 - d21).diff().diff()

def f34_tdsq_548_td_event_cluster_indicator_3_in_10d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when 3+ TD events occurred in trailing 10d (cluster)."""
    dens = _td_event_panel(close, high, low).rolling(10, min_periods=2).sum()
    return (dens >= 3).astype(float).diff().diff()

def f34_tdsq_549_td_event_density_pct_rank_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 21d TD-event density within trailing 252d."""
    dens = _td_event_panel(close, high, low).rolling(MDAYS, min_periods=WDAYS).sum()
    return _pct_rank(dens, YDAYS).diff().diff()

def f34_tdsq_550_perfected_setup_density_63d_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Count of perfected setup-9 events in trailing 63d."""
    return _td_perfected_sell_setup_9_event(close, high).fillna(0).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f34_tdsq_551_rei_overbought_density_21d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of trailing 21d bars with REI > 60 — REI-overbought cluster density."""
    return (_td_rei(close, high, low) > 60).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f34_tdsq_552_setup_9_density_63d_d2(close: pd.Series) -> pd.Series:
    """Count of setup-9 fires in trailing 63d."""
    return (_td_sell_setup_count(close) == 9).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f34_tdsq_553_countdown_13_density_126d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of countdown-13 fires in trailing 126d."""
    cd = _td_sell_countdown_count(close, high, low)
    fire = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    return fire.rolling(126, min_periods=QDAYS).sum().diff().diff()

def f34_tdsq_554_td_event_density_at_252d_high_indicator_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when 21d TD-event density >= 2 AND close near 252d max (clustered TD signals at top)."""
    dens = _td_event_panel(close, high, low).rolling(MDAYS, min_periods=WDAYS).sum()
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return ((dens >= 2) & (near == 1)).astype(float).where(dens.notna() & near.notna(), np.nan).diff().diff()

def f34_tdsq_555_td_event_density_63d_slope_21d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21d slope of 63d TD-event density — is signal-clustering trending up?"""
    dens = _td_event_panel(close, high, low).rolling(QDAYS, min_periods=MDAYS).sum()
    return _rolling_slope(dens, MDAYS).diff().diff()

def f34_tdsq_556_time_setup_count_above_7_in_63d_d2(close: pd.Series) -> pd.Series:
    """Count of trailing 63d bars where sell-setup count >= 7 (deep-setup time)."""
    return (_td_sell_setup_count(close) >= 7).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f34_tdsq_557_time_setup_count_above_9_in_252d_d2(close: pd.Series) -> pd.Series:
    """Count of trailing 252d bars where sell-setup count >= 9."""
    return (_td_sell_setup_count(close) >= 9).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f34_tdsq_558_time_countdown_above_10_in_63d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of trailing 63d bars where countdown count >= 10 (late-countdown time)."""
    cd = _td_sell_countdown_count(close, high, low)
    return (cd >= 10).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f34_tdsq_559_time_countdown_active_in_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of trailing 252d bars where countdown is active (count > 0)."""
    cd = _td_sell_countdown_count(close, high, low)
    return (cd > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f34_tdsq_560_time_rei_above_60_in_63d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of trailing 63d bars with REI > 60."""
    return (_td_rei(close, high, low) > 60).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f34_tdsq_561_time_rei_above_80_in_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of trailing 252d bars with REI > 80 (extreme-REI time)."""
    return (_td_rei(close, high, low) > 80).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f34_tdsq_562_fraction_setup_active_252d_d2(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252d bars where sell-setup count > 0."""
    return (_td_sell_setup_count(close) > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f34_tdsq_563_fraction_buy_setup_active_252d_d2(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252d bars where buy-setup count > 0."""
    return (_td_buy_setup_count(close) > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f34_tdsq_564_longest_setup_active_streak_252d_d2(close: pd.Series) -> pd.Series:
    """Longest consecutive-bar streak with sell-setup count > 0 in trailing 252d."""
    flag = (_td_sell_setup_count(close) > 0).astype(int)
    grp = (flag == 0).cumsum()
    run = flag.groupby(grp).cumsum().astype(float)
    return run.rolling(YDAYS, min_periods=QDAYS).max().diff().diff()

def f34_tdsq_565_longest_countdown_active_streak_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Longest consecutive-bar streak with countdown active in trailing 252d."""
    cd = _td_sell_countdown_count(close, high, low)
    flag = (cd > 0).astype(int)
    grp = (flag == 0).cumsum()
    run = flag.groupby(grp).cumsum().astype(float)
    return run.rolling(YDAYS, min_periods=QDAYS).max().diff().diff()

def f34_tdsq_566_time_setup_above_5_at_252d_high_in_63d_d2(close: pd.Series) -> pd.Series:
    """Count of trailing 63d bars where setup count >= 5 AND close near 252d max."""
    sc_high = (_td_sell_setup_count(close) >= 5).astype(float)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (sc_high * near).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f34_tdsq_567_fraction_rei_above_60_63d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of trailing 63d bars with REI > 60."""
    return (_td_rei(close, high, low) > 60).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().diff().diff()

def f34_tdsq_568_time_setup_or_countdown_active_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of trailing 252d bars where EITHER setup OR countdown is active."""
    sc_active = (_td_sell_setup_count(close) > 0).astype(float)
    cd_active = (_td_sell_countdown_count(close, high, low) > 0).astype(float)
    either = (sc_active + cd_active > 0).astype(float)
    return either.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f34_tdsq_569_time_setup_count_at_9_in_504d_d2(close: pd.Series) -> pd.Series:
    """Count of trailing 504d bars where setup count == 9 exactly."""
    return (_td_sell_setup_count(close) == 9).astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).sum().diff().diff()

def f34_tdsq_570_time_in_late_countdown_pct_rank_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 63d-count-of-bars-with-countdown>=10 within trailing 252d."""
    cd = _td_sell_countdown_count(close, high, low)
    late = (cd >= 10).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return _pct_rank(late, YDAYS).diff().diff()

def f34_tdsq_571_open_vs_td_ref_close_log_diff_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    """log(open / close[t-4]) — today's open relative to TD reference (setup-comparison) close."""
    return (_safe_log(open) - _safe_log(close.shift(4))).diff().diff()

def f34_tdsq_572_open_above_td_ref_close_indicator_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    """+1 when today's open > close 4 bars ago (TD reference)."""
    return (open > close.shift(4)).astype(float).where(close.shift(4).notna(), np.nan).diff().diff()

def f34_tdsq_573_open_vs_td_ref_close_at_setup_9_bar_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    """log(open / ref-close) captured at most-recent setup-9 bar (held forward)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    diff = _safe_log(open) - _safe_log(close.shift(4))
    return _value_at_event(diff, fires).diff().diff()

def f34_tdsq_574_open_above_td_ref_close_persistence_21d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    """Count of trailing 21d bars where open > TD reference close."""
    return (open > close.shift(4)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f34_tdsq_575_open_gap_vs_td_ref_close_atr_norm_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(open - close[t-4]) / ATR(21) — TD-reference gap in vol units."""
    return _safe_div(open - close.shift(4), _atr(high, low, close, MDAYS)).diff().diff()

def f34_tdsq_576_close_vs_td_ref_close_at_countdown_13_bar_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """log(close / ref-close) captured at most-recent countdown-13 fire bar."""
    cd = _td_sell_countdown_count(close, high, low)
    fire = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    diff = _safe_log(close) - _safe_log(close.shift(4))
    return _value_at_event(diff, fire).diff().diff()

def f34_tdsq_577_open_above_td_ref_close_streak_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where open > TD reference close."""
    flag = (open > close.shift(4)).astype(int).fillna(0)
    grp = (flag == 0).cumsum()
    return flag.groupby(grp).cumsum().astype(float).diff().diff()

def f34_tdsq_578_open_vs_td_ref_close_zscore_252d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score over 252d of log(open / ref-close)."""
    diff = _safe_log(open) - _safe_log(close.shift(4))
    return _rolling_zscore(diff, YDAYS).diff().diff()

def f34_tdsq_579_open_above_td_ref_close_at_setup_9_indicator_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    """+1 when setup-9 fires AND today's open > TD reference close (gap-confirmed setup)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    open_above = (open > close.shift(4)).astype(float)
    return (fires * open_above).where(fires.notna() & open_above.notna(), np.nan).diff().diff()

def f34_tdsq_580_open_vs_td_ref_close_pct_rank_252d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of log(open / ref-close) within trailing 252d."""
    diff = _safe_log(open) - _safe_log(close.shift(4))
    return _pct_rank(diff, YDAYS).diff().diff()

def f34_tdsq_581_most_recent_setup_9_is_1st_in_63d_indicator_d2(close: pd.Series) -> pd.Series:
    """+1 when the current bars-since-setup-9 corresponds to the only (1st) setup-9 in trailing 63d."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    o1 = _nth_most_recent_event_offset(fires, 1, QDAYS)
    o2 = _nth_most_recent_event_offset(fires, 2, QDAYS)
    return (o1.notna() & o2.isna()).astype(float).diff().diff()

def f34_tdsq_582_most_recent_setup_9_is_2nd_plus_in_63d_indicator_d2(close: pd.Series) -> pd.Series:
    """+1 when there are 2+ setup-9 events in trailing 63d (clustered setups)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    o2 = _nth_most_recent_event_offset(fires, 2, QDAYS)
    return o2.notna().astype(float).diff().diff()

def f34_tdsq_583_most_recent_setup_9_is_3rd_plus_in_126d_indicator_d2(close: pd.Series) -> pd.Series:
    """+1 when there are 3+ setup-9 events in trailing 126d."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    o3 = _nth_most_recent_event_offset(fires, 3, 126)
    return o3.notna().astype(float).diff().diff()

def f34_tdsq_584_setup_9_ordinal_count_in_63d_d2(close: pd.Series) -> pd.Series:
    """How many setup-9 events have occurred in trailing 63d (ordinal density 0..N)."""
    return (_td_sell_setup_count(close) == 9).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f34_tdsq_585_setup_9_ordinal_count_in_126d_d2(close: pd.Series) -> pd.Series:
    """How many setup-9 events have occurred in trailing 126d."""
    return (_td_sell_setup_count(close) == 9).astype(float).rolling(126, min_periods=QDAYS).sum().diff().diff()

def f34_tdsq_586_countdown_13_ordinal_count_in_126d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """How many countdown-13 events in trailing 126d."""
    cd = _td_sell_countdown_count(close, high, low)
    fire = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    return fire.rolling(126, min_periods=QDAYS).sum().diff().diff()

def f34_tdsq_587_most_recent_setup_9_is_3rd_plus_in_252d_indicator_d2(close: pd.Series) -> pd.Series:
    """+1 when there are 3+ setup-9 events in trailing 252d."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    o3 = _nth_most_recent_event_offset(fires, 3, YDAYS)
    return o3.notna().astype(float).diff().diff()

def f34_tdsq_588_setup_9_is_4th_plus_in_252d_indicator_d2(close: pd.Series) -> pd.Series:
    """+1 when there are 4+ setup-9 events in trailing 252d (heavy-cluster regime)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    o4 = _nth_most_recent_event_offset(fires, 4, YDAYS)
    return o4.notna().astype(float).diff().diff()

def f34_tdsq_589_bars_to_4th_most_recent_setup_9_252d_d2(close: pd.Series) -> pd.Series:
    """Bars-back to the 4th most-recent setup-9 in trailing 252d."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    return _nth_most_recent_event_offset(fires, 4, YDAYS).diff().diff()

def f34_tdsq_590_setup_9_ordinal_count_in_252d_at_high_indicator_d2(close: pd.Series) -> pd.Series:
    """+1 when 3+ setup-9 events in trailing 252d AND close near 252d max (repeated setups into top)."""
    cnt = (_td_sell_setup_count(close) == 9).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return ((cnt >= 3) & (near == 1)).astype(float).where(cnt.notna() & near.notna(), np.nan).diff().diff()

def f34_tdsq_591_setup_9_with_close_above_bb_upper_indicator_d2(close: pd.Series) -> pd.Series:
    """+1 when setup-9 fires AND close > Bollinger upper band (20, 2)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    _, ubb, _ = _bb(close, 20, 2.0)
    above = (close > ubb).astype(float)
    return (fires * above).where(fires.notna() & above.notna(), np.nan).diff().diff()

def f34_tdsq_592_countdown_13_with_close_above_bb_upper_indicator_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when countdown-13 fires AND close > Bollinger upper band."""
    cd = _td_sell_countdown_count(close, high, low)
    fire = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    _, ubb, _ = _bb(close, 20, 2.0)
    above = (close > ubb).astype(float)
    return (fire * above).where(fire.notna() & above.notna(), np.nan).diff().diff()

def f34_tdsq_593_setup_9_with_close_above_keltner_upper_indicator_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when setup-9 fires AND close > Keltner upper channel (20, 2×ATR)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    ku = _keltner_upper(high, low, close, 20, 2.0)
    above = (close > ku).astype(float)
    return (fires * above).where(fires.notna() & above.notna(), np.nan).diff().diff()

def f34_tdsq_594_setup_9_in_bb_squeeze_indicator_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when setup-9 fires AND Bollinger Bands are inside Keltner Channels (squeeze)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    _, ubb, lbb = _bb(close, 20, 2.0)
    ku = _keltner_upper(high, low, close, 20, 2.0)
    kl = _ema(close, 20) - 2.0 * _atr(high, low, close, 20)
    squeeze = ((ubb < ku) & (lbb > kl)).astype(float)
    return (fires * squeeze).where(fires.notna() & squeeze.notna(), np.nan).diff().diff()

def f34_tdsq_595_setup_9_with_close_at_donchian_high_indicator_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """+1 when setup-9 fires AND close >= 21d-trailing-max(high) (Donchian-high touch)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    dhigh = high.rolling(MDAYS, min_periods=WDAYS).max()
    at_high = (close >= dhigh).astype(float)
    return (fires * at_high).where(fires.notna() & at_high.notna(), np.nan).diff().diff()

def f34_tdsq_596_countdown_13_with_close_at_donchian_high_indicator_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when countdown-13 fires AND close >= 21d-trailing-max(high)."""
    cd = _td_sell_countdown_count(close, high, low)
    fire = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    dhigh = high.rolling(MDAYS, min_periods=WDAYS).max()
    at_high = (close >= dhigh).astype(float)
    return (fire * at_high).where(fire.notna() & at_high.notna(), np.nan).diff().diff()

def f34_tdsq_597_setup_9_with_bb_pct_b_above_1_indicator_d2(close: pd.Series) -> pd.Series:
    """+1 when setup-9 fires AND Bollinger %B > 1 (close above upper band)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    m, ubb, lbb = _bb(close, 20, 2.0)
    pct_b = _safe_div(close - lbb, ubb - lbb)
    return (fires * (pct_b > 1.0).astype(float)).where(fires.notna() & pct_b.notna(), np.nan).diff().diff()

def f34_tdsq_598_setup_9_with_bb_width_top_decile_indicator_d2(close: pd.Series) -> pd.Series:
    """+1 when setup-9 fires AND Bollinger-band width is in 252d top decile (wide-band setup)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    m, ubb, lbb = _bb(close, 20, 2.0)
    width = _safe_div(ubb - lbb, m)
    wide = (_pct_rank(width, YDAYS) >= 0.9).astype(float)
    return (fires * wide).where(fires.notna() & wide.notna(), np.nan).diff().diff()

def f34_tdsq_599_setup_9_with_bb_width_bottom_decile_indicator_d2(close: pd.Series) -> pd.Series:
    """+1 when setup-9 fires AND Bollinger-band width is in 252d bottom decile (compressed-band setup)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    m, ubb, lbb = _bb(close, 20, 2.0)
    width = _safe_div(ubb - lbb, m)
    tight = (_pct_rank(width, YDAYS) <= 0.1).astype(float)
    return (fires * tight).where(fires.notna() & tight.notna(), np.nan).diff().diff()

def f34_tdsq_600_countdown_13_with_close_above_keltner_upper_at_252d_high_indicator_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when countdown-13 fires AND close > Keltner upper AND close near 252d max — triple conjunction."""
    cd = _td_sell_countdown_count(close, high, low)
    fire = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    ku = _keltner_upper(high, low, close, 20, 2.0)
    above = (close > ku).astype(float)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (fire * above * near).where(fire.notna() & above.notna() & near.notna(), np.nan).diff().diff()
TD_SEQUENTIAL_DEMARK_D2_REGISTRY_526_600 = {'f34_tdsq_526_td_pivot_mid_value_d2': {'inputs': ['open', 'high', 'low', 'close'], 'func': f34_tdsq_526_td_pivot_mid_value_d2}, 'f34_tdsq_527_td_pivot_resistance_value_d2': {'inputs': ['open', 'high', 'low', 'close'], 'func': f34_tdsq_527_td_pivot_resistance_value_d2}, 'f34_tdsq_528_td_pivot_support_value_d2': {'inputs': ['open', 'high', 'low', 'close'], 'func': f34_tdsq_528_td_pivot_support_value_d2}, 'f34_tdsq_529_close_above_td_pivot_mid_indicator_d2': {'inputs': ['open', 'high', 'low', 'close'], 'func': f34_tdsq_529_close_above_td_pivot_mid_indicator_d2}, 'f34_tdsq_530_close_above_td_pivot_resistance_indicator_d2': {'inputs': ['open', 'high', 'low', 'close'], 'func': f34_tdsq_530_close_above_td_pivot_resistance_indicator_d2}, 'f34_tdsq_531_close_below_td_pivot_support_indicator_d2': {'inputs': ['open', 'high', 'low', 'close'], 'func': f34_tdsq_531_close_below_td_pivot_support_indicator_d2}, 'f34_tdsq_532_distance_close_to_td_pivot_resistance_atr_norm_d2': {'inputs': ['open', 'high', 'low', 'close'], 'func': f34_tdsq_532_distance_close_to_td_pivot_resistance_atr_norm_d2}, 'f34_tdsq_533_distance_close_to_td_pivot_support_atr_norm_d2': {'inputs': ['open', 'high', 'low', 'close'], 'func': f34_tdsq_533_distance_close_to_td_pivot_support_atr_norm_d2}, 'f34_tdsq_534_td_pivot_resistance_break_event_indicator_d2': {'inputs': ['open', 'high', 'low', 'close'], 'func': f34_tdsq_534_td_pivot_resistance_break_event_indicator_d2}, 'f34_tdsq_535_td_pivot_support_break_event_indicator_d2': {'inputs': ['open', 'high', 'low', 'close'], 'func': f34_tdsq_535_td_pivot_support_break_event_indicator_d2}, 'f34_tdsq_536_td_pivot_resistance_break_count_252d_d2': {'inputs': ['open', 'high', 'low', 'close'], 'func': f34_tdsq_536_td_pivot_resistance_break_count_252d_d2}, 'f34_tdsq_537_td_pivot_support_break_count_252d_d2': {'inputs': ['open', 'high', 'low', 'close'], 'func': f34_tdsq_537_td_pivot_support_break_count_252d_d2}, 'f34_tdsq_538_close_position_in_td_pivot_band_d2': {'inputs': ['open', 'high', 'low', 'close'], 'func': f34_tdsq_538_close_position_in_td_pivot_band_d2}, 'f34_tdsq_539_td_pivot_resistance_failed_break_indicator_d2': {'inputs': ['open', 'high', 'low', 'close'], 'func': f34_tdsq_539_td_pivot_resistance_failed_break_indicator_d2}, 'f34_tdsq_540_td_pivot_resistance_break_at_252d_high_indicator_d2': {'inputs': ['open', 'high', 'low', 'close'], 'func': f34_tdsq_540_td_pivot_resistance_break_at_252d_high_indicator_d2}, 'f34_tdsq_541_td_event_density_5d_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_541_td_event_density_5d_d2}, 'f34_tdsq_542_td_event_density_10d_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_542_td_event_density_10d_d2}, 'f34_tdsq_543_td_event_density_21d_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_543_td_event_density_21d_d2}, 'f34_tdsq_544_td_event_density_42d_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_544_td_event_density_42d_d2}, 'f34_tdsq_545_td_event_density_63d_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_545_td_event_density_63d_d2}, 'f34_tdsq_546_td_event_density_21d_zscore_252d_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_546_td_event_density_21d_zscore_252d_d2}, 'f34_tdsq_547_td_event_density_acceleration_5d_vs_21d_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_547_td_event_density_acceleration_5d_vs_21d_d2}, 'f34_tdsq_548_td_event_cluster_indicator_3_in_10d_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_548_td_event_cluster_indicator_3_in_10d_d2}, 'f34_tdsq_549_td_event_density_pct_rank_252d_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_549_td_event_density_pct_rank_252d_d2}, 'f34_tdsq_550_perfected_setup_density_63d_d2': {'inputs': ['close', 'high'], 'func': f34_tdsq_550_perfected_setup_density_63d_d2}, 'f34_tdsq_551_rei_overbought_density_21d_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_551_rei_overbought_density_21d_d2}, 'f34_tdsq_552_setup_9_density_63d_d2': {'inputs': ['close'], 'func': f34_tdsq_552_setup_9_density_63d_d2}, 'f34_tdsq_553_countdown_13_density_126d_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_553_countdown_13_density_126d_d2}, 'f34_tdsq_554_td_event_density_at_252d_high_indicator_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_554_td_event_density_at_252d_high_indicator_d2}, 'f34_tdsq_555_td_event_density_63d_slope_21d_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_555_td_event_density_63d_slope_21d_d2}, 'f34_tdsq_556_time_setup_count_above_7_in_63d_d2': {'inputs': ['close'], 'func': f34_tdsq_556_time_setup_count_above_7_in_63d_d2}, 'f34_tdsq_557_time_setup_count_above_9_in_252d_d2': {'inputs': ['close'], 'func': f34_tdsq_557_time_setup_count_above_9_in_252d_d2}, 'f34_tdsq_558_time_countdown_above_10_in_63d_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_558_time_countdown_above_10_in_63d_d2}, 'f34_tdsq_559_time_countdown_active_in_252d_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_559_time_countdown_active_in_252d_d2}, 'f34_tdsq_560_time_rei_above_60_in_63d_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_560_time_rei_above_60_in_63d_d2}, 'f34_tdsq_561_time_rei_above_80_in_252d_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_561_time_rei_above_80_in_252d_d2}, 'f34_tdsq_562_fraction_setup_active_252d_d2': {'inputs': ['close'], 'func': f34_tdsq_562_fraction_setup_active_252d_d2}, 'f34_tdsq_563_fraction_buy_setup_active_252d_d2': {'inputs': ['close'], 'func': f34_tdsq_563_fraction_buy_setup_active_252d_d2}, 'f34_tdsq_564_longest_setup_active_streak_252d_d2': {'inputs': ['close'], 'func': f34_tdsq_564_longest_setup_active_streak_252d_d2}, 'f34_tdsq_565_longest_countdown_active_streak_252d_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_565_longest_countdown_active_streak_252d_d2}, 'f34_tdsq_566_time_setup_above_5_at_252d_high_in_63d_d2': {'inputs': ['close'], 'func': f34_tdsq_566_time_setup_above_5_at_252d_high_in_63d_d2}, 'f34_tdsq_567_fraction_rei_above_60_63d_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_567_fraction_rei_above_60_63d_d2}, 'f34_tdsq_568_time_setup_or_countdown_active_252d_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_568_time_setup_or_countdown_active_252d_d2}, 'f34_tdsq_569_time_setup_count_at_9_in_504d_d2': {'inputs': ['close'], 'func': f34_tdsq_569_time_setup_count_at_9_in_504d_d2}, 'f34_tdsq_570_time_in_late_countdown_pct_rank_252d_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_570_time_in_late_countdown_pct_rank_252d_d2}, 'f34_tdsq_571_open_vs_td_ref_close_log_diff_d2': {'inputs': ['open', 'close'], 'func': f34_tdsq_571_open_vs_td_ref_close_log_diff_d2}, 'f34_tdsq_572_open_above_td_ref_close_indicator_d2': {'inputs': ['open', 'close'], 'func': f34_tdsq_572_open_above_td_ref_close_indicator_d2}, 'f34_tdsq_573_open_vs_td_ref_close_at_setup_9_bar_d2': {'inputs': ['open', 'close'], 'func': f34_tdsq_573_open_vs_td_ref_close_at_setup_9_bar_d2}, 'f34_tdsq_574_open_above_td_ref_close_persistence_21d_d2': {'inputs': ['open', 'close'], 'func': f34_tdsq_574_open_above_td_ref_close_persistence_21d_d2}, 'f34_tdsq_575_open_gap_vs_td_ref_close_atr_norm_d2': {'inputs': ['open', 'high', 'low', 'close'], 'func': f34_tdsq_575_open_gap_vs_td_ref_close_atr_norm_d2}, 'f34_tdsq_576_close_vs_td_ref_close_at_countdown_13_bar_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_576_close_vs_td_ref_close_at_countdown_13_bar_d2}, 'f34_tdsq_577_open_above_td_ref_close_streak_d2': {'inputs': ['open', 'close'], 'func': f34_tdsq_577_open_above_td_ref_close_streak_d2}, 'f34_tdsq_578_open_vs_td_ref_close_zscore_252d_d2': {'inputs': ['open', 'close'], 'func': f34_tdsq_578_open_vs_td_ref_close_zscore_252d_d2}, 'f34_tdsq_579_open_above_td_ref_close_at_setup_9_indicator_d2': {'inputs': ['open', 'close'], 'func': f34_tdsq_579_open_above_td_ref_close_at_setup_9_indicator_d2}, 'f34_tdsq_580_open_vs_td_ref_close_pct_rank_252d_d2': {'inputs': ['open', 'close'], 'func': f34_tdsq_580_open_vs_td_ref_close_pct_rank_252d_d2}, 'f34_tdsq_581_most_recent_setup_9_is_1st_in_63d_indicator_d2': {'inputs': ['close'], 'func': f34_tdsq_581_most_recent_setup_9_is_1st_in_63d_indicator_d2}, 'f34_tdsq_582_most_recent_setup_9_is_2nd_plus_in_63d_indicator_d2': {'inputs': ['close'], 'func': f34_tdsq_582_most_recent_setup_9_is_2nd_plus_in_63d_indicator_d2}, 'f34_tdsq_583_most_recent_setup_9_is_3rd_plus_in_126d_indicator_d2': {'inputs': ['close'], 'func': f34_tdsq_583_most_recent_setup_9_is_3rd_plus_in_126d_indicator_d2}, 'f34_tdsq_584_setup_9_ordinal_count_in_63d_d2': {'inputs': ['close'], 'func': f34_tdsq_584_setup_9_ordinal_count_in_63d_d2}, 'f34_tdsq_585_setup_9_ordinal_count_in_126d_d2': {'inputs': ['close'], 'func': f34_tdsq_585_setup_9_ordinal_count_in_126d_d2}, 'f34_tdsq_586_countdown_13_ordinal_count_in_126d_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_586_countdown_13_ordinal_count_in_126d_d2}, 'f34_tdsq_587_most_recent_setup_9_is_3rd_plus_in_252d_indicator_d2': {'inputs': ['close'], 'func': f34_tdsq_587_most_recent_setup_9_is_3rd_plus_in_252d_indicator_d2}, 'f34_tdsq_588_setup_9_is_4th_plus_in_252d_indicator_d2': {'inputs': ['close'], 'func': f34_tdsq_588_setup_9_is_4th_plus_in_252d_indicator_d2}, 'f34_tdsq_589_bars_to_4th_most_recent_setup_9_252d_d2': {'inputs': ['close'], 'func': f34_tdsq_589_bars_to_4th_most_recent_setup_9_252d_d2}, 'f34_tdsq_590_setup_9_ordinal_count_in_252d_at_high_indicator_d2': {'inputs': ['close'], 'func': f34_tdsq_590_setup_9_ordinal_count_in_252d_at_high_indicator_d2}, 'f34_tdsq_591_setup_9_with_close_above_bb_upper_indicator_d2': {'inputs': ['close'], 'func': f34_tdsq_591_setup_9_with_close_above_bb_upper_indicator_d2}, 'f34_tdsq_592_countdown_13_with_close_above_bb_upper_indicator_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_592_countdown_13_with_close_above_bb_upper_indicator_d2}, 'f34_tdsq_593_setup_9_with_close_above_keltner_upper_indicator_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_593_setup_9_with_close_above_keltner_upper_indicator_d2}, 'f34_tdsq_594_setup_9_in_bb_squeeze_indicator_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_594_setup_9_in_bb_squeeze_indicator_d2}, 'f34_tdsq_595_setup_9_with_close_at_donchian_high_indicator_d2': {'inputs': ['close', 'high'], 'func': f34_tdsq_595_setup_9_with_close_at_donchian_high_indicator_d2}, 'f34_tdsq_596_countdown_13_with_close_at_donchian_high_indicator_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_596_countdown_13_with_close_at_donchian_high_indicator_d2}, 'f34_tdsq_597_setup_9_with_bb_pct_b_above_1_indicator_d2': {'inputs': ['close'], 'func': f34_tdsq_597_setup_9_with_bb_pct_b_above_1_indicator_d2}, 'f34_tdsq_598_setup_9_with_bb_width_top_decile_indicator_d2': {'inputs': ['close'], 'func': f34_tdsq_598_setup_9_with_bb_width_top_decile_indicator_d2}, 'f34_tdsq_599_setup_9_with_bb_width_bottom_decile_indicator_d2': {'inputs': ['close'], 'func': f34_tdsq_599_setup_9_with_bb_width_bottom_decile_indicator_d2}, 'f34_tdsq_600_countdown_13_with_close_above_keltner_upper_at_252d_high_indicator_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_600_countdown_13_with_close_above_keltner_upper_at_252d_high_indicator_d2}}