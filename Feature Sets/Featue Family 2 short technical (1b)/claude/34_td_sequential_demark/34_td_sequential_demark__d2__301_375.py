"""34_td_sequential_demark d2 features 301-375 — order-2 difference of corresponding base features.

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
    """At each bar, the value at the most-recent True event (held forward)."""
    return value.where(event_flag.fillna(0) == 1, np.nan).ffill()

def _nth_most_recent_event_offset(flag, n_th, max_lookback):
    """Bars-back to the N-th most-recent True event in trailing max_lookback (NaN if fewer than n_th)."""
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

def _td_camouflage_bearish_event(open_: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    pc = close.shift(1)
    po = open_.shift(1)
    pch = pd.concat([high, close.shift(1)], axis=1).max(axis=1)
    p_pch = pch.shift(1)
    flag = (close < pc) & (close >= po) & (pch > p_pch)
    return flag.astype(float).where(pc.notna() & po.notna() & p_pch.notna(), np.nan)

def _rsi_wilder(close, n=14):
    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = (-delta).clip(lower=0)
    ag = gain.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    al = loss.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    rs = _safe_div(ag, al)
    return 100.0 - 100.0 / (1.0 + rs)

def _stoch_k(high, low, close, n=14):
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    return 100.0 * _safe_div(close - ll, hh - ll)

def _macd_line(close, fast=12, slow=26):
    return _ema(close, fast) - _ema(close, slow)

def _bbands_upper(close, n=20, k=2.0):
    m = _sma(close, n)
    sd = close.rolling(n, min_periods=max(n // 3, 2)).std()
    return m + k * sd

def f34_tdsq_301_volume_zscore_63d_at_setup_9_bar_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol z-score(63d) captured at the most-recent setup-9 bar (held forward)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    return _value_at_event(_rolling_zscore(volume, QDAYS), fires).diff().diff()

def f34_tdsq_302_volume_zscore_252d_at_setup_9_bar_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol z-score(252d) captured at the most-recent setup-9 bar (held forward)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    return _value_at_event(_rolling_zscore(volume, YDAYS), fires).diff().diff()

def f34_tdsq_303_dollar_volume_pct_rank_252d_at_setup_9_bar_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar-volume 252d-pct-rank captured at most-recent setup-9 bar."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    return _value_at_event(_pct_rank(close * volume, YDAYS), fires).diff().diff()

def f34_tdsq_304_volume_relative_to_21d_mean_at_setup_9_bar_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """volume / 21d-rolling-mean(volume) captured at most-recent setup-9 bar."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    return _value_at_event(_safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean()), fires).diff().diff()

def f34_tdsq_305_setup_9_on_top_decile_volume_count_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of trailing 252d setup-9 bars that fired on a top-decile-vol(252d) bar."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    top_vol = (_pct_rank(volume, YDAYS) >= 0.9).astype(float)
    return (fires * top_vol).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f34_tdsq_306_setup_9_on_bottom_decile_volume_count_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of trailing 252d setup-9 bars on a bottom-decile-vol bar."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    bot_vol = (_pct_rank(volume, YDAYS) <= 0.1).astype(float)
    return (fires * bot_vol).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f34_tdsq_307_volume_zscore_63d_at_perfected_setup_9_bar_d2(close: pd.Series, high: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol z(63d) captured at most-recent PERFECTED setup-9 bar."""
    fires = _td_perfected_sell_setup_9_event(close, high)
    return _value_at_event(_rolling_zscore(volume, QDAYS), fires).diff().diff()

def f34_tdsq_308_3d_sum_volume_relative_at_setup_9_bar_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(3-day volume sum / 21d-mean × 3) captured at most-recent setup-9 bar (3-day burst factor)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    v3 = volume.rolling(3, min_periods=1).sum()
    v_baseline = volume.rolling(MDAYS, min_periods=WDAYS).mean() * 3.0
    return _value_at_event(_safe_div(v3, v_baseline), fires).diff().diff()

def f34_tdsq_309_setup_9_on_volume_below_21d_mean_indicator_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when setup-9 fires today AND today's vol < 21d-mean (suspect setup-9 with no conviction)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    below = (volume < volume.rolling(MDAYS, min_periods=WDAYS).mean()).astype(float)
    return (fires * below).where(fires.notna() & below.notna(), np.nan).diff().diff()

def f34_tdsq_310_bars_since_high_volume_setup_9_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since last setup-9 that fired on a high-vol-z(63d) > 1 bar."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    vz_high = (_rolling_zscore(volume, QDAYS) > 1.0).astype(float)
    return _bars_since_true(fires * vz_high).diff().diff()

def f34_tdsq_311_bar_range_atr_norm_at_setup_9_bar_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's range / ATR(21) captured at most-recent setup-9 bar."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    return _value_at_event(_safe_div(high - low, _atr(high, low, close, MDAYS)), fires).diff().diff()

def f34_tdsq_312_bar_range_pct_rank_252d_at_setup_9_bar_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bar-range 252d-pct-rank captured at most-recent setup-9 bar."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    return _value_at_event(_pct_rank(high - low, YDAYS), fires).diff().diff()

def f34_tdsq_313_setup_9_on_wide_range_bar_count_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of setup-9 bars on top-decile-range bars in trailing 252d."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    wide = (_pct_rank(high - low, YDAYS) >= 0.9).astype(float)
    return (fires * wide).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f34_tdsq_314_setup_9_on_narrow_range_bar_count_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of setup-9 bars on bottom-decile-range bars in trailing 252d."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    narrow = (_pct_rank(high - low, YDAYS) <= 0.1).astype(float)
    return (fires * narrow).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f34_tdsq_315_bar_range_atr_norm_at_perfected_setup_9_bar_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Range/ATR(21) at most-recent PERFECTED setup-9 bar."""
    fires = _td_perfected_sell_setup_9_event(close, high)
    return _value_at_event(_safe_div(high - low, _atr(high, low, close, MDAYS)), fires).diff().diff()

def f34_tdsq_316_gap_pct_at_setup_9_bar_d2(close: pd.Series, open: pd.Series) -> pd.Series:
    """% gap (open vs prior close) captured at most-recent setup-9 bar."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    gap = open / close.shift(1) - 1.0
    return _value_at_event(gap, fires).diff().diff()

def f34_tdsq_317_setup_9_on_gap_up_bar_indicator_d2(close: pd.Series, open: pd.Series, high: pd.Series) -> pd.Series:
    """+1 when setup-9 fires AND open > prior high (gap-up setup-9 — extension signal)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    gap_up = (open > high.shift(1)).astype(float)
    return (fires * gap_up).where(fires.notna() & gap_up.notna(), np.nan).diff().diff()

def f34_tdsq_318_setup_9_on_gap_down_bar_indicator_d2(close: pd.Series, open: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when setup-9 fires AND open < prior low (gap-down setup-9 — strange combination, top exhaustion?)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    gap_down = (open < low.shift(1)).astype(float)
    return (fires * gap_down).where(fires.notna() & gap_down.notna(), np.nan).diff().diff()

def f34_tdsq_319_close_position_in_bar_at_setup_9_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close-position-in-bar (0..1) at most-recent setup-9 bar."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    pos = _safe_div(close - low, high - low)
    return _value_at_event(pos, fires).diff().diff()

def f34_tdsq_320_setup_9_on_close_in_top_decile_of_bar_count_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of trailing 252d setup-9 bars where close was in top 10% of bar's range."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    pos = _safe_div(close - low, high - low)
    high_pos = (pos >= 0.9).astype(float)
    return (fires * high_pos).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f34_tdsq_321_setup_9_on_doji_bar_indicator_d2(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when setup-9 fires AND bar is a doji (body < 10% of range)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    rng = (high - low).replace(0, np.nan)
    doji = ((close - open).abs() / rng < 0.1).astype(float)
    return (fires * doji).where(fires.notna() & doji.notna(), np.nan).diff().diff()

def f34_tdsq_322_setup_9_on_marubozu_bullish_bar_indicator_d2(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when setup-9 fires AND bar is bullish marubozu (body >= 95% of range, close > open)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    rng = (high - low).replace(0, np.nan)
    mar = (((close - open) / rng >= 0.95) & (close > open)).astype(float)
    return (fires * mar).where(fires.notna() & mar.notna(), np.nan).diff().diff()

def f34_tdsq_323_setup_9_on_long_upper_wick_bar_indicator_d2(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when setup-9 AND upper wick > 50% of bar range (rejection)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    rng = (high - low).replace(0, np.nan)
    uw = (high - pd.concat([open, close], axis=1).max(axis=1)) / rng
    long_uw = (uw > 0.5).astype(float)
    return (fires * long_uw).where(fires.notna() & long_uw.notna(), np.nan).diff().diff()

def f34_tdsq_324_setup_9_on_long_lower_wick_bar_indicator_d2(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when setup-9 AND lower wick > 50% of bar range (support tested)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    rng = (high - low).replace(0, np.nan)
    lw = (pd.concat([open, close], axis=1).min(axis=1) - low) / rng
    long_lw = (lw > 0.5).astype(float)
    return (fires * long_lw).where(fires.notna() & long_lw.notna(), np.nan).diff().diff()

def f34_tdsq_325_countdown_13_on_doji_bar_indicator_d2(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 on bar where sell-countdown-13 fires AND bar is a doji."""
    cd = _td_sell_countdown_count(close, high, low)
    fire = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    rng = (high - low).replace(0, np.nan)
    doji = ((close - open).abs() / rng < 0.1).astype(float)
    return (fire * doji).where(fire.notna() & doji.notna(), np.nan).diff().diff()

def f34_tdsq_326_countdown_13_on_wide_range_bar_indicator_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 on bar where sell-countdown-13 fires AND today's range > 1.5 × 21d-mean."""
    cd = _td_sell_countdown_count(close, high, low)
    fire = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    rng = high - low
    wide = (rng > 1.5 * rng.rolling(MDAYS, min_periods=WDAYS).mean()).astype(float)
    return (fire * wide).where(fire.notna() & wide.notna(), np.nan).diff().diff()

def f34_tdsq_327_countdown_13_on_high_volume_bar_indicator_d2(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 on bar where sell-countdown-13 fires AND vol z(63d) > 1."""
    cd = _td_sell_countdown_count(close, high, low)
    fire = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    vz_high = (_rolling_zscore(volume, QDAYS) > 1.0).astype(float)
    return (fire * vz_high).where(fire.notna() & vz_high.notna(), np.nan).diff().diff()

def f34_tdsq_328_bar_body_pct_at_setup_9_bar_d2(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Body-pct (|close-open| / range) captured at most-recent setup-9 bar."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    body = (close - open).abs() / (high - low).replace(0, np.nan)
    return _value_at_event(body, fires).diff().diff()

def f34_tdsq_329_upper_wick_pct_at_setup_9_bar_d2(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Upper-wick-pct (upper-wick / range) captured at most-recent setup-9 bar."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    uw = (high - pd.concat([open, close], axis=1).max(axis=1)) / (high - low).replace(0, np.nan)
    return _value_at_event(uw, fires).diff().diff()

def f34_tdsq_330_lower_wick_pct_at_setup_9_bar_d2(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Lower-wick-pct (lower-wick / range) captured at most-recent setup-9 bar."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    lw = (pd.concat([open, close], axis=1).min(axis=1) - low) / (high - low).replace(0, np.nan)
    return _value_at_event(lw, fires).diff().diff()

def f34_tdsq_331_bars_to_1st_most_recent_setup_9_252d_d2(close: pd.Series) -> pd.Series:
    """Bars-back-to-1st-most-recent setup-9 in trailing 252d."""
    return _nth_most_recent_event_offset((_td_sell_setup_count(close) == 9).astype(float), 1, YDAYS).diff().diff()

def f34_tdsq_332_bars_to_2nd_most_recent_setup_9_252d_d2(close: pd.Series) -> pd.Series:
    """Bars-back-to-2nd-most-recent setup-9 in trailing 252d."""
    return _nth_most_recent_event_offset((_td_sell_setup_count(close) == 9).astype(float), 2, YDAYS).diff().diff()

def f34_tdsq_333_bars_to_3rd_most_recent_setup_9_252d_d2(close: pd.Series) -> pd.Series:
    """Bars-back-to-3rd-most-recent setup-9 in trailing 252d."""
    return _nth_most_recent_event_offset((_td_sell_setup_count(close) == 9).astype(float), 3, YDAYS).diff().diff()

def f34_tdsq_334_gap_1st_to_2nd_setup_9_252d_d2(close: pd.Series) -> pd.Series:
    """Bars between 1st and 2nd most-recent setup-9 in trailing 252d."""
    flag = (_td_sell_setup_count(close) == 9).astype(float)
    return (_nth_most_recent_event_offset(flag, 2, YDAYS) - _nth_most_recent_event_offset(flag, 1, YDAYS)).diff().diff()

def f34_tdsq_335_gap_2nd_to_3rd_setup_9_252d_d2(close: pd.Series) -> pd.Series:
    """Bars between 2nd and 3rd most-recent setup-9 in trailing 252d."""
    flag = (_td_sell_setup_count(close) == 9).astype(float)
    return (_nth_most_recent_event_offset(flag, 3, YDAYS) - _nth_most_recent_event_offset(flag, 2, YDAYS)).diff().diff()

def f34_tdsq_336_bars_to_1st_most_recent_perfected_9_252d_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Bars-back-to-1st-most-recent perfected sell-setup-9 in trailing 252d."""
    return _nth_most_recent_event_offset(_td_perfected_sell_setup_9_event(close, high), 1, YDAYS).diff().diff()

def f34_tdsq_337_bars_to_2nd_most_recent_perfected_9_252d_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Bars-back-to-2nd-most-recent perfected sell-setup-9 in trailing 252d."""
    return _nth_most_recent_event_offset(_td_perfected_sell_setup_9_event(close, high), 2, YDAYS).diff().diff()

def f34_tdsq_338_bars_to_1st_most_recent_countdown_13_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars-back-to-1st-most-recent countdown-13-fire in trailing 252d."""
    cd = _td_sell_countdown_count(close, high, low)
    flag = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    return _nth_most_recent_event_offset(flag, 1, YDAYS).diff().diff()

def f34_tdsq_339_bars_to_2nd_most_recent_countdown_13_504d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars-back-to-2nd-most-recent countdown-13-fire in trailing 504d."""
    cd = _td_sell_countdown_count(close, high, low)
    flag = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    return _nth_most_recent_event_offset(flag, 2, DDAYS_2Y).diff().diff()

def f34_tdsq_340_bars_to_3rd_most_recent_countdown_13_504d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars-back-to-3rd-most-recent countdown-13-fire in trailing 504d."""
    cd = _td_sell_countdown_count(close, high, low)
    flag = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    return _nth_most_recent_event_offset(flag, 3, DDAYS_2Y).diff().diff()

def f34_tdsq_341_bars_to_1st_most_recent_combo_13_252d_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Bars-back-to-1st-most-recent TD Combo-13-fire in trailing 252d."""
    cb = _td_sell_combo_count(close, high)
    flag = ((cb == 13) & (cb.shift(1) < 13)).astype(float)
    return _nth_most_recent_event_offset(flag, 1, YDAYS).diff().diff()

def f34_tdsq_342_bars_to_2nd_most_recent_combo_13_252d_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Bars-back-to-2nd-most-recent TD Combo-13-fire in trailing 252d."""
    cb = _td_sell_combo_count(close, high)
    flag = ((cb == 13) & (cb.shift(1) < 13)).astype(float)
    return _nth_most_recent_event_offset(flag, 2, YDAYS).diff().diff()

def f34_tdsq_343_bars_to_1st_most_recent_rei_above_60_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars-back-to-1st-most-recent bar with REI > 60 in trailing 252d."""
    flag = (_td_rei(close, high, low) > 60).astype(float)
    return _nth_most_recent_event_offset(flag, 1, YDAYS).diff().diff()

def f34_tdsq_344_bars_to_2nd_most_recent_rei_above_60_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars-back-to-2nd-most-recent bar with REI > 60 in trailing 252d."""
    flag = (_td_rei(close, high, low) > 60).astype(float)
    return _nth_most_recent_event_offset(flag, 2, YDAYS).diff().diff()

def f34_tdsq_345_bars_to_1st_most_recent_camouflage_252d_d2(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars-back-to-1st-most-recent bearish-Camouflage event in trailing 252d."""
    flag = _td_camouflage_bearish_event(open, close, high, low)
    return _nth_most_recent_event_offset(flag, 1, YDAYS).diff().diff()

def f34_tdsq_346_setup_count_progression_rate_5d_d2(close: pd.Series) -> pd.Series:
    """5d slope of TD sell-setup count (rate of count progression)."""
    return _rolling_slope(_td_sell_setup_count(close), WDAYS).diff().diff()

def f34_tdsq_347_setup_count_progression_rate_21d_d2(close: pd.Series) -> pd.Series:
    """21d slope of TD sell-setup count."""
    return _rolling_slope(_td_sell_setup_count(close), MDAYS).diff().diff()

def f34_tdsq_348_time_to_complete_last_setup_from_start_to_9_d2(close: pd.Series) -> pd.Series:
    """At each setup-9 bar, the number of bars since count was last 1 (held forward).
    Note: a 'clean' 9-bar setup completes in exactly 9 bars; longer = recycled/restarted."""
    sc = _td_sell_setup_count(close)
    started = (sc == 1).astype(float)
    bars_since_start = _bars_since_true(started)
    fires = (sc == 9).astype(float)
    return _value_at_event(bars_since_start, fires).diff().diff()

def f34_tdsq_349_median_setup_completion_time_252d_d2(close: pd.Series) -> pd.Series:
    """Median completion time (start-to-9 bars) over trailing 252d."""
    sc = _td_sell_setup_count(close)
    started = (sc == 1).astype(float)
    bars_since_start = _bars_since_true(started)
    fires = (sc == 9).astype(int)
    completion_times = bars_since_start.where(fires == 1, np.nan)
    return completion_times.rolling(YDAYS, min_periods=QDAYS).median().diff().diff()

def f34_tdsq_350_last_setup_completion_fast_indicator_d2(close: pd.Series) -> pd.Series:
    """+1 if last setup-9 fired in <= 9 bars from start (no restart/recycle)."""
    sc = _td_sell_setup_count(close)
    started = (sc == 1).astype(float)
    bars_since_start = _bars_since_true(started)
    fires = (sc == 9).astype(float)
    last_time = _value_at_event(bars_since_start, fires)
    return (last_time <= 9.0).astype(float).where(last_time.notna(), np.nan).diff().diff()

def f34_tdsq_351_last_setup_completion_slow_indicator_d2(close: pd.Series) -> pd.Series:
    """+1 if last setup-9 took > 12 bars to complete (recycled or paused setup)."""
    sc = _td_sell_setup_count(close)
    started = (sc == 1).astype(float)
    bars_since_start = _bars_since_true(started)
    fires = (sc == 9).astype(float)
    last_time = _value_at_event(bars_since_start, fires)
    return (last_time > 12.0).astype(float).where(last_time.notna(), np.nan).diff().diff()

def f34_tdsq_352_setup_completion_rate_per_starts_252d_d2(close: pd.Series) -> pd.Series:
    """Ratio: 252d count-of-completions(setup-9 fires) / 252d count-of-starts(setup count == 1 bars)."""
    sc = _td_sell_setup_count(close)
    starts = (sc == 1).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    completions = (sc == 9).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(completions, starts).diff().diff()

def f34_tdsq_353_setup_count_5d_change_d2(close: pd.Series) -> pd.Series:
    """Current setup count - setup count 5 bars ago."""
    return (_td_sell_setup_count(close) - _td_sell_setup_count(close).shift(WDAYS)).diff().diff()

def f34_tdsq_354_setup_count_velocity_at_signal_bar_d2(close: pd.Series) -> pd.Series:
    """5d slope of setup count captured at most-recent setup-9 bar (how fast did the setup advance)."""
    sc = _td_sell_setup_count(close)
    fires = (sc == 9).astype(float)
    velocity = _rolling_slope(sc, WDAYS)
    return _value_at_event(velocity, fires).diff().diff()

def f34_tdsq_355_setup_count_max_in_5d_d2(close: pd.Series) -> pd.Series:
    """Max sell-setup count over trailing 5d."""
    return _td_sell_setup_count(close).rolling(WDAYS, min_periods=1).max().diff().diff()

def f34_tdsq_356_tr_at_setup_bar_1_held_forward_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range at the bar where setup count == 1 (held forward through setup until reset)."""
    sc = _td_sell_setup_count(close)
    tr = _true_range(high, low, close)
    return tr.where(sc == 1, np.nan).ffill().diff().diff()

def f34_tdsq_357_tr_at_setup_bar_5_held_forward_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range at the bar where setup count == 5 (held forward)."""
    sc = _td_sell_setup_count(close)
    tr = _true_range(high, low, close)
    return tr.where(sc == 5, np.nan).ffill().diff().diff()

def f34_tdsq_358_tr_at_setup_bar_9_held_forward_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range at the bar where setup count == 9 (held forward)."""
    sc = _td_sell_setup_count(close)
    tr = _true_range(high, low, close)
    return tr.where(sc == 9, np.nan).ffill().diff().diff()

def f34_tdsq_359_tr_progression_ratio_9_over_1_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """TR at setup-9 / TR at setup-1 (held forward) — TR growth across setup."""
    sc = _td_sell_setup_count(close)
    tr = _true_range(high, low, close)
    tr_at_1 = tr.where(sc == 1, np.nan).ffill()
    tr_at_9 = tr.where(sc == 9, np.nan).ffill()
    return _safe_div(tr_at_9, tr_at_1).diff().diff()

def f34_tdsq_360_tr_max_during_last_setup_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Max true-range during last setup window (setup_count > 0 only), held forward.
    Approximated via rolling max of TR over a 12d window (typical setup duration)."""
    sc = _td_sell_setup_count(close)
    tr = _true_range(high, low, close)
    tr_in_setup = tr.where(sc > 0, np.nan)
    return tr_in_setup.rolling(12, min_periods=1).max().ffill().diff().diff()

def f34_tdsq_361_tr_zscore_252d_at_setup_9_bar_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """TR z-score(252d) captured at most-recent setup-9 bar."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    return _value_at_event(_rolling_zscore(_true_range(high, low, close), YDAYS), fires).diff().diff()

def f34_tdsq_362_avg_tr_during_last_12d_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean of true-range over last 12 bars (typical setup window length)."""
    return _true_range(high, low, close).rolling(12, min_periods=4).mean().diff().diff()

def f34_tdsq_363_atr_expansion_during_last_21d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR21 today / ATR21 21 bars ago — volatility expansion ratio."""
    atr = _atr(high, low, close, MDAYS)
    return _safe_div(atr, atr.shift(MDAYS)).diff().diff()

def f34_tdsq_364_bar_range_slope_during_setup_5d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5d slope of bar range, masked to setup-active bars only (held forward)."""
    sc = _td_sell_setup_count(close)
    rng = high - low
    return _rolling_slope(rng, WDAYS).where(sc > 0, np.nan).ffill().diff().diff()

def f34_tdsq_365_setup_9_during_atr_expansion_regime_indicator_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when setup-9 fires AND ATR21 > 1.5 × ATR252 (vol-expansion regime)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    a21 = _atr(high, low, close, MDAYS)
    a252 = _atr(high, low, close, YDAYS)
    expand = (a21 > 1.5 * a252).astype(float)
    return (fires * expand).where(fires.notna() & expand.notna(), np.nan).diff().diff()

def f34_tdsq_366_setup_9_with_close_at_252d_high_indicator_d2(close: pd.Series) -> pd.Series:
    """+1 when setup-9 fires AND close within 0.5% of 252d max (very precise top conjunction)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.995).astype(float)
    return (fires * near).where(fires.notna() & near.notna(), np.nan).diff().diff()

def f34_tdsq_367_setup_9_with_close_at_504d_high_indicator_d2(close: pd.Series) -> pd.Series:
    """+1 when setup-9 fires AND close within 1% of 504d max."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    near = (close >= close.rolling(DDAYS_2Y, min_periods=YDAYS).max() * 0.99).astype(float)
    return (fires * near).where(fires.notna() & near.notna(), np.nan).diff().diff()

def f34_tdsq_368_setup_9_with_high_at_252d_high_indicator_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """+1 when setup-9 fires AND today's HIGH equals 252d-trailing-max(high)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    new_high = (high == high.rolling(YDAYS, min_periods=QDAYS).max()).astype(float)
    return (fires * new_high).where(fires.notna() & new_high.notna(), np.nan).diff().diff()

def f34_tdsq_369_setup_9_with_close_in_top_5pct_of_252d_range_indicator_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when setup-9 fires AND close-position in 252d high/low range is in top 5%."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    h252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    l252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - l252, h252 - l252)
    top5 = (pos >= 0.95).astype(float)
    return (fires * top5).where(fires.notna() & top5.notna(), np.nan).diff().diff()

def f34_tdsq_370_setup_9_with_rsi14_above_70_indicator_d2(close: pd.Series) -> pd.Series:
    """+1 when setup-9 fires AND RSI(14) > 70 (overbought conjunction)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    rsi_ob = (_rsi_wilder(close, 14) > 70).astype(float)
    return (fires * rsi_ob).where(fires.notna() & rsi_ob.notna(), np.nan).diff().diff()

def f34_tdsq_371_setup_9_with_stoch_above_80_indicator_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when setup-9 fires AND Stoch %K > 80."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    sk_ob = (_stoch_k(high, low, close, 14) > 80).astype(float)
    return (fires * sk_ob).where(fires.notna() & sk_ob.notna(), np.nan).diff().diff()

def f34_tdsq_372_setup_9_with_macd_line_above_zero_indicator_d2(close: pd.Series) -> pd.Series:
    """+1 when setup-9 fires AND MACD line > 0."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    macd_pos = (_macd_line(close, 12, 26) > 0).astype(float)
    return (fires * macd_pos).where(fires.notna() & macd_pos.notna(), np.nan).diff().diff()

def f34_tdsq_373_setup_9_with_close_above_bb_upper_indicator_d2(close: pd.Series) -> pd.Series:
    """+1 when setup-9 fires AND close > Bollinger upper band (20, 2)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    above_ubb = (close > _bbands_upper(close, 20, 2.0)).astype(float)
    return (fires * above_ubb).where(fires.notna() & above_ubb.notna(), np.nan).diff().diff()

def f34_tdsq_374_setup_9_with_volume_zscore_above_2_indicator_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when setup-9 fires AND vol z-score(252d) > 2 (extreme volume conjunction)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    vz_extreme = (_rolling_zscore(volume, YDAYS) > 2.0).astype(float)
    return (fires * vz_extreme).where(fires.notna() & vz_extreme.notna(), np.nan).diff().diff()

def f34_tdsq_375_setup_9_with_close_below_vwap21_indicator_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when setup-9 fires AND close < VWMA(21) (weak setup-9 — below 21d volume-weighted average)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    pv = (close * volume).rolling(MDAYS, min_periods=WDAYS).sum()
    v = volume.rolling(MDAYS, min_periods=WDAYS).sum()
    vwma = _safe_div(pv, v)
    below = (close < vwma).astype(float)
    return (fires * below).where(fires.notna() & below.notna(), np.nan).diff().diff()
TD_SEQUENTIAL_DEMARK_D2_REGISTRY_301_375 = {'f34_tdsq_301_volume_zscore_63d_at_setup_9_bar_d2': {'inputs': ['close', 'volume'], 'func': f34_tdsq_301_volume_zscore_63d_at_setup_9_bar_d2}, 'f34_tdsq_302_volume_zscore_252d_at_setup_9_bar_d2': {'inputs': ['close', 'volume'], 'func': f34_tdsq_302_volume_zscore_252d_at_setup_9_bar_d2}, 'f34_tdsq_303_dollar_volume_pct_rank_252d_at_setup_9_bar_d2': {'inputs': ['close', 'volume'], 'func': f34_tdsq_303_dollar_volume_pct_rank_252d_at_setup_9_bar_d2}, 'f34_tdsq_304_volume_relative_to_21d_mean_at_setup_9_bar_d2': {'inputs': ['close', 'volume'], 'func': f34_tdsq_304_volume_relative_to_21d_mean_at_setup_9_bar_d2}, 'f34_tdsq_305_setup_9_on_top_decile_volume_count_252d_d2': {'inputs': ['close', 'volume'], 'func': f34_tdsq_305_setup_9_on_top_decile_volume_count_252d_d2}, 'f34_tdsq_306_setup_9_on_bottom_decile_volume_count_252d_d2': {'inputs': ['close', 'volume'], 'func': f34_tdsq_306_setup_9_on_bottom_decile_volume_count_252d_d2}, 'f34_tdsq_307_volume_zscore_63d_at_perfected_setup_9_bar_d2': {'inputs': ['close', 'high', 'volume'], 'func': f34_tdsq_307_volume_zscore_63d_at_perfected_setup_9_bar_d2}, 'f34_tdsq_308_3d_sum_volume_relative_at_setup_9_bar_d2': {'inputs': ['close', 'volume'], 'func': f34_tdsq_308_3d_sum_volume_relative_at_setup_9_bar_d2}, 'f34_tdsq_309_setup_9_on_volume_below_21d_mean_indicator_d2': {'inputs': ['close', 'volume'], 'func': f34_tdsq_309_setup_9_on_volume_below_21d_mean_indicator_d2}, 'f34_tdsq_310_bars_since_high_volume_setup_9_d2': {'inputs': ['close', 'volume'], 'func': f34_tdsq_310_bars_since_high_volume_setup_9_d2}, 'f34_tdsq_311_bar_range_atr_norm_at_setup_9_bar_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_311_bar_range_atr_norm_at_setup_9_bar_d2}, 'f34_tdsq_312_bar_range_pct_rank_252d_at_setup_9_bar_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_312_bar_range_pct_rank_252d_at_setup_9_bar_d2}, 'f34_tdsq_313_setup_9_on_wide_range_bar_count_252d_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_313_setup_9_on_wide_range_bar_count_252d_d2}, 'f34_tdsq_314_setup_9_on_narrow_range_bar_count_252d_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_314_setup_9_on_narrow_range_bar_count_252d_d2}, 'f34_tdsq_315_bar_range_atr_norm_at_perfected_setup_9_bar_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_315_bar_range_atr_norm_at_perfected_setup_9_bar_d2}, 'f34_tdsq_316_gap_pct_at_setup_9_bar_d2': {'inputs': ['close', 'open'], 'func': f34_tdsq_316_gap_pct_at_setup_9_bar_d2}, 'f34_tdsq_317_setup_9_on_gap_up_bar_indicator_d2': {'inputs': ['close', 'open', 'high'], 'func': f34_tdsq_317_setup_9_on_gap_up_bar_indicator_d2}, 'f34_tdsq_318_setup_9_on_gap_down_bar_indicator_d2': {'inputs': ['close', 'open', 'low'], 'func': f34_tdsq_318_setup_9_on_gap_down_bar_indicator_d2}, 'f34_tdsq_319_close_position_in_bar_at_setup_9_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_319_close_position_in_bar_at_setup_9_d2}, 'f34_tdsq_320_setup_9_on_close_in_top_decile_of_bar_count_252d_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_320_setup_9_on_close_in_top_decile_of_bar_count_252d_d2}, 'f34_tdsq_321_setup_9_on_doji_bar_indicator_d2': {'inputs': ['close', 'open', 'high', 'low'], 'func': f34_tdsq_321_setup_9_on_doji_bar_indicator_d2}, 'f34_tdsq_322_setup_9_on_marubozu_bullish_bar_indicator_d2': {'inputs': ['close', 'open', 'high', 'low'], 'func': f34_tdsq_322_setup_9_on_marubozu_bullish_bar_indicator_d2}, 'f34_tdsq_323_setup_9_on_long_upper_wick_bar_indicator_d2': {'inputs': ['close', 'open', 'high', 'low'], 'func': f34_tdsq_323_setup_9_on_long_upper_wick_bar_indicator_d2}, 'f34_tdsq_324_setup_9_on_long_lower_wick_bar_indicator_d2': {'inputs': ['close', 'open', 'high', 'low'], 'func': f34_tdsq_324_setup_9_on_long_lower_wick_bar_indicator_d2}, 'f34_tdsq_325_countdown_13_on_doji_bar_indicator_d2': {'inputs': ['close', 'open', 'high', 'low'], 'func': f34_tdsq_325_countdown_13_on_doji_bar_indicator_d2}, 'f34_tdsq_326_countdown_13_on_wide_range_bar_indicator_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_326_countdown_13_on_wide_range_bar_indicator_d2}, 'f34_tdsq_327_countdown_13_on_high_volume_bar_indicator_d2': {'inputs': ['close', 'high', 'low', 'volume'], 'func': f34_tdsq_327_countdown_13_on_high_volume_bar_indicator_d2}, 'f34_tdsq_328_bar_body_pct_at_setup_9_bar_d2': {'inputs': ['close', 'open', 'high', 'low'], 'func': f34_tdsq_328_bar_body_pct_at_setup_9_bar_d2}, 'f34_tdsq_329_upper_wick_pct_at_setup_9_bar_d2': {'inputs': ['close', 'open', 'high', 'low'], 'func': f34_tdsq_329_upper_wick_pct_at_setup_9_bar_d2}, 'f34_tdsq_330_lower_wick_pct_at_setup_9_bar_d2': {'inputs': ['close', 'open', 'high', 'low'], 'func': f34_tdsq_330_lower_wick_pct_at_setup_9_bar_d2}, 'f34_tdsq_331_bars_to_1st_most_recent_setup_9_252d_d2': {'inputs': ['close'], 'func': f34_tdsq_331_bars_to_1st_most_recent_setup_9_252d_d2}, 'f34_tdsq_332_bars_to_2nd_most_recent_setup_9_252d_d2': {'inputs': ['close'], 'func': f34_tdsq_332_bars_to_2nd_most_recent_setup_9_252d_d2}, 'f34_tdsq_333_bars_to_3rd_most_recent_setup_9_252d_d2': {'inputs': ['close'], 'func': f34_tdsq_333_bars_to_3rd_most_recent_setup_9_252d_d2}, 'f34_tdsq_334_gap_1st_to_2nd_setup_9_252d_d2': {'inputs': ['close'], 'func': f34_tdsq_334_gap_1st_to_2nd_setup_9_252d_d2}, 'f34_tdsq_335_gap_2nd_to_3rd_setup_9_252d_d2': {'inputs': ['close'], 'func': f34_tdsq_335_gap_2nd_to_3rd_setup_9_252d_d2}, 'f34_tdsq_336_bars_to_1st_most_recent_perfected_9_252d_d2': {'inputs': ['close', 'high'], 'func': f34_tdsq_336_bars_to_1st_most_recent_perfected_9_252d_d2}, 'f34_tdsq_337_bars_to_2nd_most_recent_perfected_9_252d_d2': {'inputs': ['close', 'high'], 'func': f34_tdsq_337_bars_to_2nd_most_recent_perfected_9_252d_d2}, 'f34_tdsq_338_bars_to_1st_most_recent_countdown_13_252d_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_338_bars_to_1st_most_recent_countdown_13_252d_d2}, 'f34_tdsq_339_bars_to_2nd_most_recent_countdown_13_504d_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_339_bars_to_2nd_most_recent_countdown_13_504d_d2}, 'f34_tdsq_340_bars_to_3rd_most_recent_countdown_13_504d_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_340_bars_to_3rd_most_recent_countdown_13_504d_d2}, 'f34_tdsq_341_bars_to_1st_most_recent_combo_13_252d_d2': {'inputs': ['close', 'high'], 'func': f34_tdsq_341_bars_to_1st_most_recent_combo_13_252d_d2}, 'f34_tdsq_342_bars_to_2nd_most_recent_combo_13_252d_d2': {'inputs': ['close', 'high'], 'func': f34_tdsq_342_bars_to_2nd_most_recent_combo_13_252d_d2}, 'f34_tdsq_343_bars_to_1st_most_recent_rei_above_60_252d_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_343_bars_to_1st_most_recent_rei_above_60_252d_d2}, 'f34_tdsq_344_bars_to_2nd_most_recent_rei_above_60_252d_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_344_bars_to_2nd_most_recent_rei_above_60_252d_d2}, 'f34_tdsq_345_bars_to_1st_most_recent_camouflage_252d_d2': {'inputs': ['open', 'close', 'high', 'low'], 'func': f34_tdsq_345_bars_to_1st_most_recent_camouflage_252d_d2}, 'f34_tdsq_346_setup_count_progression_rate_5d_d2': {'inputs': ['close'], 'func': f34_tdsq_346_setup_count_progression_rate_5d_d2}, 'f34_tdsq_347_setup_count_progression_rate_21d_d2': {'inputs': ['close'], 'func': f34_tdsq_347_setup_count_progression_rate_21d_d2}, 'f34_tdsq_348_time_to_complete_last_setup_from_start_to_9_d2': {'inputs': ['close'], 'func': f34_tdsq_348_time_to_complete_last_setup_from_start_to_9_d2}, 'f34_tdsq_349_median_setup_completion_time_252d_d2': {'inputs': ['close'], 'func': f34_tdsq_349_median_setup_completion_time_252d_d2}, 'f34_tdsq_350_last_setup_completion_fast_indicator_d2': {'inputs': ['close'], 'func': f34_tdsq_350_last_setup_completion_fast_indicator_d2}, 'f34_tdsq_351_last_setup_completion_slow_indicator_d2': {'inputs': ['close'], 'func': f34_tdsq_351_last_setup_completion_slow_indicator_d2}, 'f34_tdsq_352_setup_completion_rate_per_starts_252d_d2': {'inputs': ['close'], 'func': f34_tdsq_352_setup_completion_rate_per_starts_252d_d2}, 'f34_tdsq_353_setup_count_5d_change_d2': {'inputs': ['close'], 'func': f34_tdsq_353_setup_count_5d_change_d2}, 'f34_tdsq_354_setup_count_velocity_at_signal_bar_d2': {'inputs': ['close'], 'func': f34_tdsq_354_setup_count_velocity_at_signal_bar_d2}, 'f34_tdsq_355_setup_count_max_in_5d_d2': {'inputs': ['close'], 'func': f34_tdsq_355_setup_count_max_in_5d_d2}, 'f34_tdsq_356_tr_at_setup_bar_1_held_forward_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_356_tr_at_setup_bar_1_held_forward_d2}, 'f34_tdsq_357_tr_at_setup_bar_5_held_forward_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_357_tr_at_setup_bar_5_held_forward_d2}, 'f34_tdsq_358_tr_at_setup_bar_9_held_forward_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_358_tr_at_setup_bar_9_held_forward_d2}, 'f34_tdsq_359_tr_progression_ratio_9_over_1_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_359_tr_progression_ratio_9_over_1_d2}, 'f34_tdsq_360_tr_max_during_last_setup_252d_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_360_tr_max_during_last_setup_252d_d2}, 'f34_tdsq_361_tr_zscore_252d_at_setup_9_bar_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_361_tr_zscore_252d_at_setup_9_bar_d2}, 'f34_tdsq_362_avg_tr_during_last_12d_252d_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_362_avg_tr_during_last_12d_252d_d2}, 'f34_tdsq_363_atr_expansion_during_last_21d_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_363_atr_expansion_during_last_21d_d2}, 'f34_tdsq_364_bar_range_slope_during_setup_5d_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_364_bar_range_slope_during_setup_5d_d2}, 'f34_tdsq_365_setup_9_during_atr_expansion_regime_indicator_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_365_setup_9_during_atr_expansion_regime_indicator_d2}, 'f34_tdsq_366_setup_9_with_close_at_252d_high_indicator_d2': {'inputs': ['close'], 'func': f34_tdsq_366_setup_9_with_close_at_252d_high_indicator_d2}, 'f34_tdsq_367_setup_9_with_close_at_504d_high_indicator_d2': {'inputs': ['close'], 'func': f34_tdsq_367_setup_9_with_close_at_504d_high_indicator_d2}, 'f34_tdsq_368_setup_9_with_high_at_252d_high_indicator_d2': {'inputs': ['close', 'high'], 'func': f34_tdsq_368_setup_9_with_high_at_252d_high_indicator_d2}, 'f34_tdsq_369_setup_9_with_close_in_top_5pct_of_252d_range_indicator_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_369_setup_9_with_close_in_top_5pct_of_252d_range_indicator_d2}, 'f34_tdsq_370_setup_9_with_rsi14_above_70_indicator_d2': {'inputs': ['close'], 'func': f34_tdsq_370_setup_9_with_rsi14_above_70_indicator_d2}, 'f34_tdsq_371_setup_9_with_stoch_above_80_indicator_d2': {'inputs': ['close', 'high', 'low'], 'func': f34_tdsq_371_setup_9_with_stoch_above_80_indicator_d2}, 'f34_tdsq_372_setup_9_with_macd_line_above_zero_indicator_d2': {'inputs': ['close'], 'func': f34_tdsq_372_setup_9_with_macd_line_above_zero_indicator_d2}, 'f34_tdsq_373_setup_9_with_close_above_bb_upper_indicator_d2': {'inputs': ['close'], 'func': f34_tdsq_373_setup_9_with_close_above_bb_upper_indicator_d2}, 'f34_tdsq_374_setup_9_with_volume_zscore_above_2_indicator_d2': {'inputs': ['close', 'volume'], 'func': f34_tdsq_374_setup_9_with_volume_zscore_above_2_indicator_d2}, 'f34_tdsq_375_setup_9_with_close_below_vwap21_indicator_d2': {'inputs': ['close', 'volume'], 'func': f34_tdsq_375_setup_9_with_close_below_vwap21_indicator_d2}}