"""moving_average_ribbon_structure d2 features 151-225 - Pipeline 1b-technical.

Gap-fill extension covering Guppy GMMA short/long bundle dynamics, ribbon
angle/inclination, expansion/contraction velocity, touch persistence & breakdown,
multi-timeframe coherence, regime-conditional metrics, information-theoretic
ribbon entropy, fan-out / fan-in events, ribbon shape/symmetry, and narrow
mrib-internal composites.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no forward shifts. Self-contained helpers - no cross-family imports.

Standard ribbons used throughout this file:
- Eight-MA ribbon (lens=[10,20,30,50,80,100,150,200], EMA-based)
- Guppy GMMA short bundle (EMAs at 3,5,8,10,12,15)
- Guppy GMMA long bundle (EMAs at 30,35,40,45,50,60)
- Guppy full ribbon (concatenation of both bundles)
"""


import numpy as np


import pandas as pd


YDAYS = 252


QDAYS = 63


MDAYS = 21


WDAYS = 5


DDAYS_2Y = 504


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


def _rolling_pctrank(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    return s.rolling(window, min_periods=min_periods).rank(pct=True)


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


def _sma(s, n, mp=None):
    if mp is None:
        mp = max(n // 3, 2)
    return s.rolling(n, min_periods=mp).mean()


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=max(n // 3, 2)).mean()


def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()


_EIGHT_LENS = [10, 20, 30, 50, 80, 100, 150, 200]


_GMMA_SHORT_LENS = [3, 5, 8, 10, 12, 15]


_GMMA_LONG_LENS  = [30, 35, 40, 45, 50, 60]


def _ribbon_8ema(close: pd.Series) -> pd.DataFrame:
    mas = [_ema(close, n).rename(f"ma{n}") for n in _EIGHT_LENS]
    return pd.concat(mas, axis=1)


def _ribbon_gmma_short(close: pd.Series) -> pd.DataFrame:
    mas = [_ema(close, n).rename(f"s{n}") for n in _GMMA_SHORT_LENS]
    return pd.concat(mas, axis=1)


def _ribbon_gmma_long(close: pd.Series) -> pd.DataFrame:
    mas = [_ema(close, n).rename(f"l{n}") for n in _GMMA_LONG_LENS]
    return pd.concat(mas, axis=1)


def _ribbon_gmma_full(close: pd.Series) -> pd.DataFrame:
    return pd.concat([_ribbon_gmma_short(close), _ribbon_gmma_long(close)], axis=1)


def _ribbon_min(df: pd.DataFrame) -> pd.Series:
    return df.min(axis=1)


def _ribbon_max(df: pd.DataFrame) -> pd.Series:
    return df.max(axis=1)


def _ribbon_median(df: pd.DataFrame) -> pd.Series:
    return df.median(axis=1)


def _ribbon_bandwidth_norm(df: pd.DataFrame, ref: pd.Series) -> pd.Series:
    """(max - min) / |ref|, where ref is typically close or median."""
    return _safe_div(df.max(axis=1) - df.min(axis=1), ref.abs())


def _ribbon_std_norm(df: pd.DataFrame, ref: pd.Series) -> pd.Series:
    return _safe_div(df.std(axis=1), ref.abs())


def _bull_stack_strict(df: pd.DataFrame) -> pd.Series:
    """Strictly decreasing across columns ordered shortest -> longest (bullish stack)."""
    diffs = df.diff(axis=1).iloc[:, 1:]
    return (diffs < 0).all(axis=1).astype(float).where(df.notna().all(axis=1), np.nan)


def _bear_stack_strict(df: pd.DataFrame) -> pd.Series:
    diffs = df.diff(axis=1).iloc[:, 1:]
    return (diffs > 0).all(axis=1).astype(float).where(df.notna().all(axis=1), np.nan)


def _bars_since_true(b: pd.Series) -> pd.Series:
    """Bars since last True (NaN before any True). True at i resets to 0 at i."""
    arr = b.astype(float).values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        v = arr[i]
        if not np.isnan(v) and v > 0.5:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=b.index)


def _max_consecutive_true(b: pd.Series, window: int) -> pd.Series:
    """Rolling max consecutive True run length in window."""
    arr = b.astype(float).fillna(0).values
    n = len(arr)
    run = np.zeros(n, dtype=float)
    cur = 0
    for i in range(n):
        if arr[i] > 0.5:
            cur += 1
        else:
            cur = 0
        run[i] = cur
    s = pd.Series(run, index=b.index)
    return s.rolling(window, min_periods=max(window // 3, 2)).max()


def _current_streak(b: pd.Series) -> pd.Series:
    """Length of current True run."""
    arr = b.astype(float).fillna(0).values
    out = np.zeros(len(arr), dtype=float)
    cur = 0
    for i in range(len(arr)):
        if arr[i] > 0.5:
            cur += 1
        else:
            cur = 0
        out[i] = float(cur)
    return pd.Series(out, index=b.index)


def f12_mrib_151_gmma_short_group_compression_index_d2(close: pd.Series) -> pd.Series:
    """Std/mean of GMMA-short group EMAs - within-bundle compression for the fast bundle."""
    rib = _ribbon_gmma_short(close)
    return (_safe_div(rib.std(axis=1), rib.mean(axis=1).abs())).diff().diff()


def f12_mrib_152_gmma_long_group_compression_index_d2(close: pd.Series) -> pd.Series:
    """Std/mean of GMMA-long group EMAs - within-bundle compression for the slow bundle."""
    rib = _ribbon_gmma_long(close)
    return (_safe_div(rib.std(axis=1), rib.mean(axis=1).abs())).diff().diff()


def f12_mrib_153_gmma_short_minus_long_group_mean_distance_d2(close: pd.Series) -> pd.Series:
    """Log gap between GMMA-short mean EMA and GMMA-long mean EMA - inter-bundle separation."""
    s = _ribbon_gmma_short(close).mean(axis=1)
    l = _ribbon_gmma_long(close).mean(axis=1)
    return (_safe_log(s) - _safe_log(l)).diff().diff()


def f12_mrib_154_gmma_short_group_max_minus_min_spread_d2(close: pd.Series) -> pd.Series:
    """(max - min) of GMMA-short bundle normalized by close - fast-bundle internal spread."""
    rib = _ribbon_gmma_short(close)
    return (_safe_div(rib.max(axis=1) - rib.min(axis=1), close.abs())).diff().diff()


def f12_mrib_155_gmma_long_group_max_minus_min_spread_d2(close: pd.Series) -> pd.Series:
    """(max - min) of GMMA-long bundle normalized by close - slow-bundle internal spread."""
    rib = _ribbon_gmma_long(close)
    return (_safe_div(rib.max(axis=1) - rib.min(axis=1), close.abs())).diff().diff()


def f12_mrib_156_gmma_short_group_above_long_group_indicator_d2(close: pd.Series) -> pd.Series:
    """Indicator: every EMA in GMMA-short bundle strictly above every EMA in GMMA-long bundle."""
    s = _ribbon_gmma_short(close)
    l = _ribbon_gmma_long(close)
    s_min = s.min(axis=1)
    l_max = l.max(axis=1)
    valid = s.notna().all(axis=1) & l.notna().all(axis=1)
    return ((s_min > l_max).astype(float).where(valid, np.nan)).diff().diff()


def f12_mrib_157_gmma_short_group_fan_out_rate_21d_d2(close: pd.Series) -> pd.Series:
    """21d slope of GMMA-short compression index - positive = bundle expanding (fan-out)."""
    rib = _ribbon_gmma_short(close)
    compr = _safe_div(rib.std(axis=1), rib.mean(axis=1).abs())
    return (_rolling_slope(compr, MDAYS)).diff().diff()


def f12_mrib_158_gmma_long_group_persistence_index_d2(close: pd.Series) -> pd.Series:
    """Fraction of last 63d where GMMA-long bundle order is strictly bullish (slow-bundle stability)."""
    l = _ribbon_gmma_long(close)
    bull = _bull_stack_strict(l)
    return (bull.rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).mean()).diff().diff()


def f12_mrib_159_gmma_inversion_event_count_252d_d2(close: pd.Series) -> pd.Series:
    """Count of 252d events where GMMA-short bundle crosses from above to below GMMA-long bundle."""
    s = _ribbon_gmma_short(close).mean(axis=1)
    l = _ribbon_gmma_long(close).mean(axis=1)
    above = (s > l).astype(float)
    cross_down = ((above.shift(1) > 0.5) & (above < 0.5)).astype(float)
    return (cross_down.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()).diff().diff()


def f12_mrib_160_gmma_double_compression_event_d2(close: pd.Series) -> pd.Series:
    """Indicator: both GMMA-short AND GMMA-long compression indices below 20th percentile of 252d."""
    s_c = _safe_div(_ribbon_gmma_short(close).std(axis=1), _ribbon_gmma_short(close).mean(axis=1).abs())
    l_c = _safe_div(_ribbon_gmma_long(close).std(axis=1), _ribbon_gmma_long(close).mean(axis=1).abs())
    s_p = _rolling_pctrank(s_c, YDAYS)
    l_p = _rolling_pctrank(l_c, YDAYS)
    return (((s_p < 0.2) & (l_p < 0.2)).astype(float).where(s_p.notna() & l_p.notna(), np.nan)).diff().diff()


def _ribbon_mean_slope_angle(close: pd.Series, n: int) -> pd.Series:
    """Mean across 8ema MAs of arctan(slope_n / mean_ma) converted to degrees."""
    rib = _ribbon_8ema(close)
    slopes = []
    for col in rib.columns:
        m = rib[col]
        sl = _rolling_slope(m, n)
        norm = _safe_div(sl, m.abs())
        slopes.append(np.degrees(np.arctan(norm)).rename(col))
    df = pd.concat(slopes, axis=1)
    return df.mean(axis=1)


def f12_mrib_161_ribbon_mean_slope_angle_21d_d2(close: pd.Series) -> pd.Series:
    """Mean tilt angle (degrees) of 8ema ribbon MAs over 21d - aggregate inclination."""
    return (_ribbon_mean_slope_angle(close, MDAYS)).diff().diff()


def f12_mrib_162_ribbon_mean_slope_angle_63d_d2(close: pd.Series) -> pd.Series:
    """Mean tilt angle (degrees) of 8ema ribbon MAs over 63d - aggregate medium-horizon inclination."""
    return (_ribbon_mean_slope_angle(close, QDAYS)).diff().diff()


def f12_mrib_163_ribbon_angle_dispersion_8mas_d2(close: pd.Series) -> pd.Series:
    """Range (max - min) of per-MA tilt angles across 8ema ribbon (21d slope) - inclination disagreement."""
    rib = _ribbon_8ema(close)
    angles = []
    for col in rib.columns:
        m = rib[col]
        sl = _rolling_slope(m, MDAYS)
        norm = _safe_div(sl, m.abs())
        angles.append(np.degrees(np.arctan(norm)).rename(col))
    df = pd.concat(angles, axis=1)
    return (df.max(axis=1) - df.min(axis=1)).diff().diff()


def f12_mrib_164_ribbon_angle_acceleration_21d_d2(close: pd.Series) -> pd.Series:
    """21d change in mean ribbon angle - acceleration of ribbon tilt."""
    ang = _ribbon_mean_slope_angle(close, MDAYS)
    return (ang - ang.shift(MDAYS)).diff().diff()


def f12_mrib_165_ribbon_angle_decline_streak_max_63d_d2(close: pd.Series) -> pd.Series:
    """Max consecutive 63d run where mean ribbon angle was negative - persistent down-tilt run."""
    ang = _ribbon_mean_slope_angle(close, MDAYS)
    neg = (ang < 0).astype(float).where(ang.notna(), np.nan)
    return (_max_consecutive_true(neg, QDAYS)).diff().diff()


def f12_mrib_166_ribbon_angle_flip_to_negative_event_indicator_d2(close: pd.Series) -> pd.Series:
    """Indicator: mean ribbon angle crossed from >=0 yesterday to <0 today."""
    ang = _ribbon_mean_slope_angle(close, MDAYS)
    flip = ((ang.shift(1) >= 0) & (ang < 0)).astype(float)
    return (flip.where(ang.notna() & ang.shift(1).notna(), np.nan)).diff().diff()


def f12_mrib_167_ribbon_angle_consensus_negative_count_252d_d2(close: pd.Series) -> pd.Series:
    """Fraction of last 252d where ALL 8ema ribbon MAs have negative 21d slope - bearish consensus."""
    rib = _ribbon_8ema(close)
    flags = []
    for col in rib.columns:
        m = rib[col]
        sl = _rolling_slope(m, MDAYS)
        flags.append((sl < 0).rename(col))
    df = pd.concat(flags, axis=1)
    all_neg = df.all(axis=1).astype(float)
    return (all_neg.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).mean()).diff().diff()


def f12_mrib_168_ribbon_angle_volatility_63d_d2(close: pd.Series) -> pd.Series:
    """Rolling 63d std of mean ribbon angle - tilt stability."""
    ang = _ribbon_mean_slope_angle(close, MDAYS)
    return (ang.rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).std()).diff().diff()


def _ribbon_bandwidth_8ema(close: pd.Series) -> pd.Series:
    rib = _ribbon_8ema(close)
    return _safe_div(rib.max(axis=1) - rib.min(axis=1), close.abs())


def f12_mrib_169_ribbon_bandwidth_expansion_rate_21d_d2(close: pd.Series) -> pd.Series:
    """21d slope of 8ema ribbon bandwidth - dBW/dt, expansion velocity."""
    bw = _ribbon_bandwidth_8ema(close)
    return (_rolling_slope(bw, MDAYS)).diff().diff()


def f12_mrib_170_ribbon_bandwidth_expansion_rate_63d_d2(close: pd.Series) -> pd.Series:
    """63d slope of 8ema ribbon bandwidth - medium-horizon expansion velocity."""
    bw = _ribbon_bandwidth_8ema(close)
    return (_rolling_slope(bw, QDAYS)).diff().diff()


def f12_mrib_171_ribbon_bandwidth_max_in_252d_d2(close: pd.Series) -> pd.Series:
    """Rolling 252d maximum of 8ema ribbon bandwidth - regime envelope."""
    bw = _ribbon_bandwidth_8ema(close)
    return (bw.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).max()).diff().diff()


def f12_mrib_172_ribbon_bandwidth_zscore_252d_d2(close: pd.Series) -> pd.Series:
    """252d z-score of 8ema ribbon bandwidth - regime-adjusted dispersion."""
    bw = _ribbon_bandwidth_8ema(close)
    return (_rolling_zscore(bw, YDAYS)).diff().diff()


def f12_mrib_173_ribbon_bandwidth_acceleration_d2(close: pd.Series) -> pd.Series:
    """21d change in 21d slope of 8ema ribbon bandwidth - d2BW/dt2."""
    bw = _ribbon_bandwidth_8ema(close)
    sl = _rolling_slope(bw, MDAYS)
    return (sl - sl.shift(MDAYS)).diff().diff()


def f12_mrib_174_ribbon_bandwidth_mean_reversion_speed_d2(close: pd.Series) -> pd.Series:
    """Half-life proxy: -ln(2)/beta from regression bw_t - bw_{t-1} on bw_{t-1} - mean_252d, over 252d."""
    bw = _ribbon_bandwidth_8ema(close)
    mu = bw.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).mean()
    dev = bw - mu
    dbw = bw.diff()
    # Use rolling slope of dbw on dev over 252d
    pair = pd.concat([dbw.rename("dy"), dev.rename("x")], axis=1)
    def _beta(window):
        if window.shape[0] < max(YDAYS // 3, 2):
            return np.nan
        y = window[:, 0]; x = window[:, 1]
        m = ~np.isnan(y) & ~np.isnan(x)
        if m.sum() < max(YDAYS // 3, 2):
            return np.nan
        y = y[m]; x = x[m]
        xm = x.mean(); ym = y.mean()
        num = ((x - xm) * (y - ym)).sum()
        den = ((x - xm) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    # rolling apply on a 2D window via raw arrays - emulate via numpy
    arr = pair.values
    n = len(arr)
    out = np.full(n, np.nan, dtype=float)
    w = YDAYS
    for i in range(n):
        if i + 1 < max(YDAYS // 3, 2):
            continue
        s = max(0, i + 1 - w)
        out[i] = _beta(arr[s:i + 1, :])
    beta = pd.Series(out, index=close.index)
    # half-life = -ln(2) / log(1 + beta), guarded
    one_plus = 1.0 + beta
    safe = one_plus.where(one_plus > 0, np.nan)
    hl = -np.log(2.0) / np.log(safe)
    return (hl.replace([np.inf, -np.inf], np.nan)).diff().diff()


def f12_mrib_175_bandwidth_expansion_during_advance_indicator_d2(close: pd.Series) -> pd.Series:
    """Indicator: 8ema ribbon bandwidth rising AND close above its 50d SMA (expansion in uptrend)."""
    bw = _ribbon_bandwidth_8ema(close)
    bw_sl = _rolling_slope(bw, MDAYS)
    sma50 = _sma(close, 50)
    cond = (bw_sl > 0) & (close > sma50)
    valid = bw_sl.notna() & sma50.notna()
    return (cond.astype(float).where(valid, np.nan)).diff().diff()


def f12_mrib_176_bandwidth_contraction_at_high_indicator_d2(close: pd.Series) -> pd.Series:
    """Indicator: 8ema bandwidth contracting AND close within top 5pct of 252d range."""
    bw = _ribbon_bandwidth_8ema(close)
    bw_sl = _rolling_slope(bw, MDAYS)
    hi = close.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).max()
    lo = close.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).min()
    rng = (hi - lo).replace(0, np.nan)
    pos = (close - lo) / rng
    cond = (bw_sl < 0) & (pos >= 0.95)
    valid = bw_sl.notna() & pos.notna()
    return (cond.astype(float).where(valid, np.nan)).diff().diff()


def f12_mrib_177_bars_since_close_inside_ribbon_band_d2(close: pd.Series) -> pd.Series:
    """Bars since close was last between 8ema ribbon min and max (i.e. inside the ribbon band)."""
    rib = _ribbon_8ema(close)
    lo = _ribbon_min(rib); hi = _ribbon_max(rib)
    inside = ((close >= lo) & (close <= hi)).astype(float).where(rib.notna().all(axis=1), np.nan)
    return (_bars_since_true(inside)).diff().diff()


def f12_mrib_178_count_close_outside_ribbon_top_252d_d2(close: pd.Series) -> pd.Series:
    """Count of 252d bars where close > 8ema ribbon max - bars stretched above ribbon."""
    rib = _ribbon_8ema(close)
    hi = _ribbon_max(rib)
    above = (close > hi).astype(float).where(rib.notna().all(axis=1), np.nan)
    return (above.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()).diff().diff()


def f12_mrib_179_count_close_outside_ribbon_bottom_252d_d2(close: pd.Series) -> pd.Series:
    """Count of 252d bars where close < 8ema ribbon min - bars stretched below ribbon."""
    rib = _ribbon_8ema(close)
    lo = _ribbon_min(rib)
    below = (close < lo).astype(float).where(rib.notna().all(axis=1), np.nan)
    return (below.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()).diff().diff()


def f12_mrib_180_ribbon_top_touch_count_63d_d2(close: pd.Series) -> pd.Series:
    """Count of 63d bars where prior close was above ribbon max but current close is at/below it - top-touch events."""
    rib = _ribbon_8ema(close)
    hi = _ribbon_max(rib)
    above = (close > hi)
    touch = (above.shift(1) & ~above).astype(float).where(rib.notna().all(axis=1), np.nan)
    return (touch.rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).sum()).diff().diff()


def f12_mrib_181_ribbon_bottom_touch_count_63d_d2(close: pd.Series) -> pd.Series:
    """Count of 63d bars where prior close was below ribbon min but current close is at/above it - bottom-touch events."""
    rib = _ribbon_8ema(close)
    lo = _ribbon_min(rib)
    below = (close < lo)
    touch = (below.shift(1) & ~below).astype(float).where(rib.notna().all(axis=1), np.nan)
    return (touch.rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).sum()).diff().diff()


def f12_mrib_182_ribbon_band_break_below_event_indicator_d2(close: pd.Series) -> pd.Series:
    """Indicator: close was strictly above 8ema ribbon max yesterday but strictly below ribbon min today (full breakdown)."""
    rib = _ribbon_8ema(close)
    lo = _ribbon_min(rib); hi = _ribbon_max(rib)
    cond = (close.shift(1) > hi.shift(1)) & (close < lo)
    valid = rib.notna().all(axis=1) & rib.shift(1).notna().all(axis=1)
    return (cond.astype(float).where(valid, np.nan)).diff().diff()


def f12_mrib_183_ribbon_band_break_above_event_indicator_d2(close: pd.Series) -> pd.Series:
    """Indicator: close was strictly below 8ema ribbon min yesterday but strictly above ribbon max today (full breakout)."""
    rib = _ribbon_8ema(close)
    lo = _ribbon_min(rib); hi = _ribbon_max(rib)
    cond = (close.shift(1) < lo.shift(1)) & (close > hi)
    valid = rib.notna().all(axis=1) & rib.shift(1).notna().all(axis=1)
    return (cond.astype(float).where(valid, np.nan)).diff().diff()


def f12_mrib_184_ribbon_internal_pull_back_count_d2(close: pd.Series) -> pd.Series:
    """63d count: close re-enters ribbon band from above (above max -> inside band) WHILE ribbon order is still bullish."""
    rib = _ribbon_8ema(close)
    lo = _ribbon_min(rib); hi = _ribbon_max(rib)
    above = (close > hi)
    inside = (close >= lo) & (close <= hi)
    pullback = above.shift(1) & inside
    bull = _bull_stack_strict(rib) > 0.5
    cond = pullback & bull
    valid = rib.notna().all(axis=1) & rib.shift(1).notna().all(axis=1)
    return (cond.astype(float).where(valid, np.nan).rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).sum()).diff().diff()


def f12_mrib_185_failed_ribbon_break_count_63d_d2(close: pd.Series) -> pd.Series:
    """63d count of breakdowns (close drops below ribbon min) that reverse back above ribbon max within next 5 forward-completed bars - measured at t+5 using prior-window data only (PIT)."""
    rib = _ribbon_8ema(close)
    lo = _ribbon_min(rib); hi = _ribbon_max(rib)
    # Indicator at bar t computed at t = bar where the break OCCURRED 5 bars ago AND we now (at t) have recovered above ribbon max
    # PIT-clean: we evaluate event at bar t using past 5d window only; no forward shifts.
    broke = (close.shift(5) < lo.shift(5))
    recovered = (close > hi)
    valid = rib.notna().all(axis=1) & rib.shift(5).notna().all(axis=1)
    event = (broke & recovered).astype(float).where(valid, np.nan)
    return (event.rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).sum()).diff().diff()


def f12_mrib_186_ribbon_full_traversal_event_count_d2(close: pd.Series) -> pd.Series:
    """63d count of bars where close 5 bars ago was outside ribbon (one side) and today is outside the OTHER side - full traversal of ribbon in <=5d."""
    rib = _ribbon_8ema(close)
    lo = _ribbon_min(rib); hi = _ribbon_max(rib)
    up_then_dn = (close.shift(5) > hi.shift(5)) & (close < lo)
    dn_then_up = (close.shift(5) < lo.shift(5)) & (close > hi)
    valid = rib.notna().all(axis=1) & rib.shift(5).notna().all(axis=1)
    event = (up_then_dn | dn_then_up).astype(float).where(valid, np.nan)
    return (event.rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).sum()).diff().diff()


def _weekly_proxy_close(close: pd.Series) -> pd.Series:
    """Weekly close proxy: 5-day SMA of daily close."""
    return _sma(close, 5)


def _short_horizon_ribbon_sign(close: pd.Series) -> pd.Series:
    """+1 bullish, -1 bearish, 0 mixed for short-only ribbon (10/20/30/50)."""
    lens = [10, 20, 30, 50]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bull = (diffs < 0).all(axis=1)
    bear = (diffs > 0).all(axis=1)
    out = pd.Series(0.0, index=close.index)
    out = out.mask(bull, 1.0).mask(bear, -1.0)
    return out.where(df.notna().all(axis=1), np.nan)


def _long_horizon_ribbon_sign(close: pd.Series) -> pd.Series:
    """+1 bullish, -1 bearish, 0 mixed for long-only ribbon (80/100/150/200)."""
    lens = [80, 100, 150, 200]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bull = (diffs < 0).all(axis=1)
    bear = (diffs > 0).all(axis=1)
    out = pd.Series(0.0, index=close.index)
    out = out.mask(bull, 1.0).mask(bear, -1.0)
    return out.where(df.notna().all(axis=1), np.nan)


def _weekly_ribbon_sign_proxy(close: pd.Series) -> pd.Series:
    """Bullish/bearish sign on weekly-proxy (SMA-5 then 8ema ribbon) close."""
    wkly = _weekly_proxy_close(close)
    rib = pd.concat([_ema(wkly, n).rename(i) for i, n in enumerate(_EIGHT_LENS)], axis=1)
    diffs = rib.diff(axis=1).iloc[:, 1:]
    bull = (diffs < 0).all(axis=1)
    bear = (diffs > 0).all(axis=1)
    out = pd.Series(0.0, index=close.index)
    out = out.mask(bull, 1.0).mask(bear, -1.0)
    return out.where(rib.notna().all(axis=1), np.nan)


def f12_mrib_187_ribbon_consistency_with_higher_timeframe_d2(close: pd.Series) -> pd.Series:
    """Indicator: daily 8ema ribbon sign equals weekly-proxy 8ema ribbon sign (sign agreement, including 0)."""
    rib = _ribbon_8ema(close)
    diffs = rib.diff(axis=1).iloc[:, 1:]
    bull = (diffs < 0).all(axis=1)
    bear = (diffs > 0).all(axis=1)
    daily = pd.Series(0.0, index=close.index)
    daily = daily.mask(bull, 1.0).mask(bear, -1.0).where(rib.notna().all(axis=1), np.nan)
    weekly = _weekly_ribbon_sign_proxy(close)
    return ((daily == weekly).astype(float).where(daily.notna() & weekly.notna(), np.nan)).diff().diff()


def f12_mrib_188_short_horizon_vs_long_horizon_ribbon_sign_agreement_d2(close: pd.Series) -> pd.Series:
    """Indicator: short-horizon ribbon sign equals long-horizon ribbon sign."""
    s = _short_horizon_ribbon_sign(close)
    l = _long_horizon_ribbon_sign(close)
    return ((s == l).astype(float).where(s.notna() & l.notna(), np.nan)).diff().diff()


def f12_mrib_189_multi_timeframe_ribbon_flip_event_count_d2(close: pd.Series) -> pd.Series:
    """252d count of bars where daily and weekly-proxy ribbon signs newly DISagree (from agreement to disagreement)."""
    rib = _ribbon_8ema(close)
    diffs = rib.diff(axis=1).iloc[:, 1:]
    bull = (diffs < 0).all(axis=1)
    bear = (diffs > 0).all(axis=1)
    daily = pd.Series(0.0, index=close.index).mask(bull, 1.0).mask(bear, -1.0)
    weekly = _weekly_ribbon_sign_proxy(close)
    agree = (daily == weekly)
    flip = (agree.shift(1) & ~agree).astype(float)
    return (flip.where(daily.notna() & weekly.notna(), np.nan).rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()).diff().diff()


def f12_mrib_190_htf_lt_alignment_score_d2(close: pd.Series) -> pd.Series:
    """Product of short-horizon, long-horizon, and weekly-proxy ribbon signs - in {-1,0,+1}; +1 is full alignment."""
    s = _short_horizon_ribbon_sign(close)
    l = _long_horizon_ribbon_sign(close)
    w = _weekly_ribbon_sign_proxy(close)
    score = s * l * w
    return (score.where(s.notna() & l.notna() & w.notna(), np.nan)).diff().diff()


def f12_mrib_191_weekly_ribbon_proxy_break_event_d2(close: pd.Series) -> pd.Series:
    """Indicator: weekly-proxy 8ema ribbon sign flipped today (vs yesterday)."""
    w = _weekly_ribbon_sign_proxy(close)
    flip = (w != w.shift(1)).astype(float)
    return (flip.where(w.notna() & w.shift(1).notna(), np.nan)).diff().diff()


def f12_mrib_192_htf_lt_disagreement_streak_d2(close: pd.Series) -> pd.Series:
    """Current consecutive bars of disagreement between short-horizon and long-horizon ribbon signs."""
    s = _short_horizon_ribbon_sign(close)
    l = _long_horizon_ribbon_sign(close)
    dis = (s != l).astype(float).where(s.notna() & l.notna(), np.nan)
    return (_current_streak(dis.fillna(0))).diff().diff()


def f12_mrib_193_coherence_persistence_in_bullish_regime_d2(close: pd.Series) -> pd.Series:
    """63d fraction of bars where daily AND weekly-proxy ribbon signs are BOTH +1 (joint bullish coherence)."""
    rib = _ribbon_8ema(close)
    diffs = rib.diff(axis=1).iloc[:, 1:]
    bull = (diffs < 0).all(axis=1)
    daily_bull = bull.astype(float).where(rib.notna().all(axis=1), np.nan)
    w = _weekly_ribbon_sign_proxy(close)
    weekly_bull = (w == 1).astype(float).where(w.notna(), np.nan)
    joint = (daily_bull * weekly_bull)
    return (joint.rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).mean()).diff().diff()


def f12_mrib_194_coherence_persistence_in_bearish_regime_d2(close: pd.Series) -> pd.Series:
    """63d fraction of bars where daily AND weekly-proxy ribbon signs are BOTH -1 (joint bearish coherence)."""
    rib = _ribbon_8ema(close)
    diffs = rib.diff(axis=1).iloc[:, 1:]
    bear = (diffs > 0).all(axis=1)
    daily_bear = bear.astype(float).where(rib.notna().all(axis=1), np.nan)
    w = _weekly_ribbon_sign_proxy(close)
    weekly_bear = (w == -1).astype(float).where(w.notna(), np.nan)
    joint = (daily_bear * weekly_bear)
    return (joint.rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).mean()).diff().diff()


def f12_mrib_195_ribbon_dispersion_conditional_on_within_5pct_of_252d_high_d2(close: pd.Series) -> pd.Series:
    """8ema ribbon std/|close| only on bars where close is within 5pct of trailing 252d high - dispersion at peaks."""
    rib = _ribbon_8ema(close)
    disp = _safe_div(rib.std(axis=1), close.abs())
    hi = close.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).max()
    cond = close >= (hi * 0.95)
    return (disp.where(cond, np.nan)).diff().diff()


def f12_mrib_196_ribbon_compression_conditional_on_high_vol_regime_d2(close: pd.Series) -> pd.Series:
    """8ema ribbon compression (std/|mean|) only on bars where 21d return-vol pctrank > 0.7."""
    rib = _ribbon_8ema(close)
    compr = _safe_div(rib.std(axis=1), rib.mean(axis=1).abs())
    ret = close.pct_change()
    vol = ret.rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).std()
    vol_p = _rolling_pctrank(vol, YDAYS)
    return (compr.where(vol_p > 0.7, np.nan)).diff().diff()


def f12_mrib_197_ribbon_compression_conditional_on_low_vol_regime_d2(close: pd.Series) -> pd.Series:
    """8ema ribbon compression on bars where 21d return-vol pctrank < 0.3 - quiet-regime compression."""
    rib = _ribbon_8ema(close)
    compr = _safe_div(rib.std(axis=1), rib.mean(axis=1).abs())
    ret = close.pct_change()
    vol = ret.rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).std()
    vol_p = _rolling_pctrank(vol, YDAYS)
    return (compr.where(vol_p < 0.3, np.nan)).diff().diff()


def f12_mrib_198_mean_ribbon_angle_during_new_high_days_d2(close: pd.Series) -> pd.Series:
    """Mean 21d ribbon angle restricted to bars where close == trailing 252d high - tilt at new highs."""
    ang = _ribbon_mean_slope_angle(close, MDAYS)
    hi = close.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).max()
    cond = close >= hi
    return (ang.where(cond, np.nan)).diff().diff()


def f12_mrib_199_ribbon_band_width_during_drawdown_periods_d2(close: pd.Series) -> pd.Series:
    """8ema bandwidth restricted to drawdown bars (close < trailing 252d high by >=10pct)."""
    bw = _ribbon_bandwidth_8ema(close)
    hi = close.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).max()
    dd = close / hi.replace(0, np.nan) - 1.0
    return (bw.where(dd <= -0.10, np.nan)).diff().diff()


def f12_mrib_200_ribbon_consistency_during_uptrend_d2(close: pd.Series) -> pd.Series:
    """8ema bull-stack indicator restricted to bars where close > 50d SMA (uptrend bars)."""
    rib = _ribbon_8ema(close)
    bull = _bull_stack_strict(rib)
    sma50 = _sma(close, 50)
    return (bull.where(close > sma50, np.nan)).diff().diff()


def f12_mrib_201_ribbon_consistency_during_downtrend_d2(close: pd.Series) -> pd.Series:
    """8ema bear-stack indicator restricted to bars where close < 50d SMA (downtrend bars)."""
    rib = _ribbon_8ema(close)
    bear = _bear_stack_strict(rib)
    sma50 = _sma(close, 50)
    return (bear.where(close < sma50, np.nan)).diff().diff()


def f12_mrib_202_ribbon_dispersion_skewness_by_regime_d2(close: pd.Series) -> pd.Series:
    """Difference between 63d-mean ribbon dispersion in uptrend bars vs downtrend bars (close vs 200d SMA)."""
    rib = _ribbon_8ema(close)
    disp = _safe_div(rib.std(axis=1), close.abs())
    sma200 = _sma(close, 200)
    up = disp.where(close > sma200, np.nan)
    dn = disp.where(close < sma200, np.nan)
    up_mean = up.rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).mean()
    dn_mean = dn.rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).mean()
    return (up_mean - dn_mean).diff().diff()


def _ribbon_order_hash(close: pd.Series) -> pd.Series:
    """Hash of the rank-permutation of 8ema MAs at each bar (0..K-1 ordering as a tuple-id)."""
    rib = _ribbon_8ema(close)
    ranks = rib.rank(axis=1, method="first").astype(float)
    # Encode each row's permutation as integer 0..K!-1 via Lehmer code
    K = ranks.shape[1]
    fact = [1] * (K + 1)
    for i in range(1, K + 1):
        fact[i] = fact[i - 1] * i
    arr = ranks.values
    out = np.full(arr.shape[0], np.nan, dtype=float)
    for i in range(arr.shape[0]):
        row = arr[i]
        if np.any(np.isnan(row)):
            continue
        perm = (row - 1).astype(int)
        if perm.min() < 0 or perm.max() >= K:
            continue
        used = [False] * K
        code = 0
        for j in range(K):
            cnt = 0
            for k in range(perm[j]):
                if not used[k]:
                    cnt += 1
            code += cnt * fact[K - j - 1]
            used[perm[j]] = True
        out[i] = float(code)
    return pd.Series(out, index=close.index)


def f12_mrib_203_shannon_entropy_of_ribbon_order_252d_d2(close: pd.Series) -> pd.Series:
    """Shannon entropy (bits) of distribution of distinct 8ema ribbon orderings observed in trailing 252d."""
    h = _ribbon_order_hash(close)
    arr = h.values
    n = len(arr)
    out = np.full(n, np.nan, dtype=float)
    w = YDAYS
    mp = max(w // 3, 2)
    for i in range(n):
        s = max(0, i + 1 - w)
        window = arr[s:i + 1]
        valid = window[~np.isnan(window)]
        if valid.size < mp:
            continue
        _, counts = np.unique(valid, return_counts=True)
        p = counts / counts.sum()
        out[i] = float(-(p * np.log2(p)).sum())
    return (pd.Series(out, index=close.index)).diff().diff()


def f12_mrib_204_gini_of_ma_spread_distribution_63d_d2(close: pd.Series) -> pd.Series:
    """Gini coefficient of |close - MA| spreads across 8ema ribbon, time-averaged over 63d."""
    rib = _ribbon_8ema(close)
    spreads = (rib.subtract(close, axis=0)).abs()
    def _gini_row(row):
        v = row[~np.isnan(row)]
        if v.size < 2:
            return np.nan
        v = np.sort(v)
        n = v.size
        s = v.sum()
        if s == 0:
            return 0.0
        cum = np.cumsum(v)
        return float((n + 1 - 2 * (cum.sum() / s)) / n)
    g = spreads.apply(_gini_row, axis=1, raw=True)
    return (g.rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).mean()).diff().diff()


def f12_mrib_205_ribbon_order_transition_matrix_entropy_d2(close: pd.Series) -> pd.Series:
    """Shannon entropy (bits) of distribution of (state_{t-1}, state_t) transitions of ribbon ordering over 252d."""
    h = _ribbon_order_hash(close).values
    n = len(h)
    out = np.full(n, np.nan, dtype=float)
    w = YDAYS
    mp = max(w // 3, 2)
    for i in range(1, n):
        s = max(1, i + 1 - w)
        prev = h[s - 1:i]
        cur = h[s:i + 1]
        mask = ~np.isnan(prev) & ~np.isnan(cur)
        if mask.sum() < mp:
            continue
        a = prev[mask].astype(np.int64); b = cur[mask].astype(np.int64)
        keys = a * 10_000_000 + b  # combine
        _, counts = np.unique(keys, return_counts=True)
        p = counts / counts.sum()
        out[i] = float(-(p * np.log2(p)).sum())
    return (pd.Series(out, index=close.index)).diff().diff()


def f12_mrib_206_ribbon_state_richness_count_d2(close: pd.Series) -> pd.Series:
    """Number of distinct ribbon orderings observed in trailing 252d."""
    h = _ribbon_order_hash(close).values
    n = len(h)
    out = np.full(n, np.nan, dtype=float)
    w = YDAYS
    mp = max(w // 3, 2)
    for i in range(n):
        s = max(0, i + 1 - w)
        window = h[s:i + 1]
        valid = window[~np.isnan(window)]
        if valid.size < mp:
            continue
        out[i] = float(np.unique(valid).size)
    return (pd.Series(out, index=close.index)).diff().diff()


def f12_mrib_207_ribbon_state_dominant_probability_d2(close: pd.Series) -> pd.Series:
    """Frequency of most-common 8ema ribbon ordering in trailing 252d (in [0,1])."""
    h = _ribbon_order_hash(close).values
    n = len(h)
    out = np.full(n, np.nan, dtype=float)
    w = YDAYS
    mp = max(w // 3, 2)
    for i in range(n):
        s = max(0, i + 1 - w)
        window = h[s:i + 1]
        valid = window[~np.isnan(window)]
        if valid.size < mp:
            continue
        _, counts = np.unique(valid, return_counts=True)
        out[i] = float(counts.max() / counts.sum())
    return (pd.Series(out, index=close.index)).diff().diff()


def f12_mrib_208_ribbon_state_change_rate_per_bar_d2(close: pd.Series) -> pd.Series:
    """63d fraction of bars where ribbon ordering changed from previous bar."""
    h = _ribbon_order_hash(close)
    change = (h != h.shift(1)).astype(float).where(h.notna() & h.shift(1).notna(), np.nan)
    return (change.rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).mean()).diff().diff()


def f12_mrib_209_ribbon_fan_out_event_indicator_d2(close: pd.Series) -> pd.Series:
    """Indicator: today's 8ema bandwidth > 1.5x its 21d trailing mean - sudden fan-out."""
    bw = _ribbon_bandwidth_8ema(close)
    mu = bw.rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).mean()
    cond = bw > 1.5 * mu
    valid = bw.notna() & mu.notna()
    return (cond.astype(float).where(valid, np.nan)).diff().diff()


def f12_mrib_210_ribbon_fan_in_event_indicator_d2(close: pd.Series) -> pd.Series:
    """Indicator: today's 8ema bandwidth < 0.67x its 21d trailing mean - sudden fan-in."""
    bw = _ribbon_bandwidth_8ema(close)
    mu = bw.rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).mean()
    cond = bw < (mu / 1.5)
    valid = bw.notna() & mu.notna()
    return (cond.astype(float).where(valid, np.nan)).diff().diff()


def f12_mrib_211_fan_out_intensity_score_d2(close: pd.Series) -> pd.Series:
    """Magnitude: (today's BW - 21d trailing mean BW) / std of BW over 21d - z-score of fan-out."""
    bw = _ribbon_bandwidth_8ema(close)
    mu = bw.rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).mean()
    sd = bw.rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).std()
    return ((bw - mu) / sd.replace(0, np.nan)).diff().diff()


def f12_mrib_212_fan_in_intensity_score_d2(close: pd.Series) -> pd.Series:
    """Magnitude: (21d trailing mean BW - today's BW) / std of BW over 21d - z-score of fan-in (positive when contracting)."""
    bw = _ribbon_bandwidth_8ema(close)
    mu = bw.rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).mean()
    sd = bw.rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).std()
    return ((mu - bw) / sd.replace(0, np.nan)).diff().diff()


def f12_mrib_213_fan_out_to_fan_in_cycle_count_252d_d2(close: pd.Series) -> pd.Series:
    """252d count of fan-out events immediately followed (within 21d window) by fan-in events - cycle count."""
    bw = _ribbon_bandwidth_8ema(close)
    mu = bw.rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).mean()
    out_ev = (bw > 1.5 * mu).astype(float)
    in_ev = (bw < (mu / 1.5)).astype(float)
    # cycle event = fan-in today AND any fan-out within last 21d
    recent_out = out_ev.rolling(MDAYS, min_periods=1).max()
    cycle = ((in_ev > 0.5) & (recent_out > 0.5)).astype(float)
    valid = bw.notna() & mu.notna()
    return (cycle.where(valid, np.nan).rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).sum()).diff().diff()


def f12_mrib_214_mean_time_between_fan_events_d2(close: pd.Series) -> pd.Series:
    """Mean gap (in bars) between consecutive fan-out OR fan-in events over trailing 252d (NaN if <2 events)."""
    bw = _ribbon_bandwidth_8ema(close)
    mu = bw.rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).mean()
    event = ((bw > 1.5 * mu) | (bw < (mu / 1.5))).astype(float).where(bw.notna() & mu.notna(), np.nan)
    arr = event.values
    idx_array = np.arange(len(arr))
    n = len(arr)
    out = np.full(n, np.nan, dtype=float)
    w = YDAYS
    mp = max(w // 3, 2)
    for i in range(n):
        s = max(0, i + 1 - w)
        window = arr[s:i + 1]
        idxs = np.where(window > 0.5)[0]
        if idxs.size < 2:
            continue
        diffs = np.diff(idxs)
        out[i] = float(diffs.mean())
    return (pd.Series(out, index=close.index)).diff().diff()


def f12_mrib_215_fan_event_volume_confirmation_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Indicator: fan-out event AND volume > 1.5x its 21d mean (volume-confirmed expansion)."""
    bw = _ribbon_bandwidth_8ema(close)
    mu = bw.rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).mean()
    fan_out = bw > 1.5 * mu
    vol_mu = volume.rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).mean()
    vol_spike = volume > 1.5 * vol_mu
    valid = bw.notna() & mu.notna() & vol_mu.notna()
    return ((fan_out & vol_spike).astype(float).where(valid, np.nan)).diff().diff()


def f12_mrib_216_terminal_fan_out_score_d2(close: pd.Series) -> pd.Series:
    """Fan-out intensity score multiplied by indicator that close is within 5pct of 252d high - terminal blow-off proxy."""
    bw = _ribbon_bandwidth_8ema(close)
    mu = bw.rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).mean()
    sd = bw.rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).std()
    z = (bw - mu) / sd.replace(0, np.nan)
    hi = close.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).max()
    near_hi = (close >= hi * 0.95).astype(float)
    return (z * near_hi).diff().diff()


def f12_mrib_217_ribbon_symmetry_score_d2(close: pd.Series) -> pd.Series:
    """abs( mean(MAs) - median(MAs) ) / std(MAs) - low score means symmetric distribution of 8ema ribbon."""
    rib = _ribbon_8ema(close)
    m = rib.mean(axis=1); med = rib.median(axis=1); sd = rib.std(axis=1)
    return (_safe_div((m - med).abs(), sd)).diff().diff()


def f12_mrib_218_ribbon_skew_index_d2(close: pd.Series) -> pd.Series:
    """(# MAs below close - # MAs above close) / N for 8ema ribbon - directional asymmetry vs price."""
    rib = _ribbon_8ema(close)
    below = rib.lt(close, axis=0).sum(axis=1).astype(float)
    above = rib.gt(close, axis=0).sum(axis=1).astype(float)
    N = rib.notna().sum(axis=1).astype(float)
    return (_safe_div(below - above, N)).diff().diff()


def f12_mrib_219_ribbon_left_tail_dominance_d2(close: pd.Series) -> pd.Series:
    """Mean rank (within 8ema ribbon sorted ascending) of LONG-period MAs (last 4 lens). High value (close to N) -> long MAs sit at top; low value -> long MAs at bottom (left tail)."""
    rib = _ribbon_8ema(close)
    ranks = rib.rank(axis=1, method="average")
    long_cols = rib.columns[-4:]
    return (ranks[long_cols].mean(axis=1)).diff().diff()


def f12_mrib_220_ribbon_right_tail_dominance_d2(close: pd.Series) -> pd.Series:
    """Mean rank of SHORT-period MAs (first 4 lens) in 8ema ribbon. High value -> short MAs sit on top (right tail)."""
    rib = _ribbon_8ema(close)
    ranks = rib.rank(axis=1, method="average")
    short_cols = rib.columns[:4]
    return (ranks[short_cols].mean(axis=1)).diff().diff()


def f12_mrib_221_ribbon_shape_stability_63d_d2(close: pd.Series) -> pd.Series:
    """Inverse of std of ribbon-ordering hash over 63d - high value = stable shape."""
    h = _ribbon_order_hash(close)
    sd = h.rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).std()
    return (1.0 / sd.replace(0, np.nan)).diff().diff()


def f12_mrib_222_ribbon_shape_drift_velocity_d2(close: pd.Series) -> pd.Series:
    """21d count of bars where 8ema ribbon ordering changed (state transitions per 21d)."""
    h = _ribbon_order_hash(close)
    change = (h != h.shift(1)).astype(float).where(h.notna() & h.shift(1).notna(), np.nan)
    return (change.rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).sum()).diff().diff()


def f12_mrib_223_gmma_compression_x_angle_inversion_composite_d2(close: pd.Series) -> pd.Series:
    """Composite: GMMA double-compression event AND mean ribbon angle flipped to negative today."""
    s_c = _safe_div(_ribbon_gmma_short(close).std(axis=1), _ribbon_gmma_short(close).mean(axis=1).abs())
    l_c = _safe_div(_ribbon_gmma_long(close).std(axis=1), _ribbon_gmma_long(close).mean(axis=1).abs())
    s_p = _rolling_pctrank(s_c, YDAYS)
    l_p = _rolling_pctrank(l_c, YDAYS)
    double_compr = (s_p < 0.2) & (l_p < 0.2)
    ang = _ribbon_mean_slope_angle(close, MDAYS)
    flip_neg = (ang.shift(1) >= 0) & (ang < 0)
    cond = double_compr & flip_neg
    valid = s_p.notna() & l_p.notna() & ang.notna() & ang.shift(1).notna()
    return (cond.astype(float).where(valid, np.nan)).diff().diff()


def f12_mrib_224_multi_timeframe_ribbon_breakdown_composite_d2(close: pd.Series) -> pd.Series:
    """Composite: ribbon_band_break_below_event AND short-horizon ribbon sign flipped to -1 today AND weekly-proxy sign is non-positive."""
    rib = _ribbon_8ema(close)
    lo = _ribbon_min(rib); hi = _ribbon_max(rib)
    break_below = (close.shift(1) > hi.shift(1)) & (close < lo)
    s = _short_horizon_ribbon_sign(close)
    short_flip_to_neg = (s.shift(1) > -0.5) & (s == -1.0)
    w = _weekly_ribbon_sign_proxy(close)
    weekly_non_pos = (w <= 0)
    cond = break_below & short_flip_to_neg & weekly_non_pos
    valid = (rib.notna().all(axis=1) & rib.shift(1).notna().all(axis=1) &
             s.notna() & s.shift(1).notna() & w.notna())
    return (cond.astype(float).where(valid, np.nan)).diff().diff()


def f12_mrib_225_terminal_ribbon_breakdown_score_d2(close: pd.Series) -> pd.Series:
    """Composite z-score: -bandwidth z * (1 - shape stability rank) * indicator(close at recent peak) - elevated when ribbon contracts near a high with state churn (terminal regime risk)."""
    bw = _ribbon_bandwidth_8ema(close)
    bw_z = _rolling_zscore(bw, YDAYS)
    h = _ribbon_order_hash(close)
    sd_h = h.rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).std()
    churn = sd_h  # higher -> more churn
    churn_p = _rolling_pctrank(churn, YDAYS)
    hi = close.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).max()
    near_peak = (close >= hi * 0.97).astype(float)
    score = (-bw_z) * churn_p * near_peak
    return (score).diff().diff()


MOVING_AVERAGE_RIBBON_STRUCTURE_D2_REGISTRY_151_225 = {
    "f12_mrib_151_gmma_short_group_compression_index_d2": {"inputs": ["close"], "func": f12_mrib_151_gmma_short_group_compression_index_d2},
    "f12_mrib_152_gmma_long_group_compression_index_d2": {"inputs": ["close"], "func": f12_mrib_152_gmma_long_group_compression_index_d2},
    "f12_mrib_153_gmma_short_minus_long_group_mean_distance_d2": {"inputs": ["close"], "func": f12_mrib_153_gmma_short_minus_long_group_mean_distance_d2},
    "f12_mrib_154_gmma_short_group_max_minus_min_spread_d2": {"inputs": ["close"], "func": f12_mrib_154_gmma_short_group_max_minus_min_spread_d2},
    "f12_mrib_155_gmma_long_group_max_minus_min_spread_d2": {"inputs": ["close"], "func": f12_mrib_155_gmma_long_group_max_minus_min_spread_d2},
    "f12_mrib_156_gmma_short_group_above_long_group_indicator_d2": {"inputs": ["close"], "func": f12_mrib_156_gmma_short_group_above_long_group_indicator_d2},
    "f12_mrib_157_gmma_short_group_fan_out_rate_21d_d2": {"inputs": ["close"], "func": f12_mrib_157_gmma_short_group_fan_out_rate_21d_d2},
    "f12_mrib_158_gmma_long_group_persistence_index_d2": {"inputs": ["close"], "func": f12_mrib_158_gmma_long_group_persistence_index_d2},
    "f12_mrib_159_gmma_inversion_event_count_252d_d2": {"inputs": ["close"], "func": f12_mrib_159_gmma_inversion_event_count_252d_d2},
    "f12_mrib_160_gmma_double_compression_event_d2": {"inputs": ["close"], "func": f12_mrib_160_gmma_double_compression_event_d2},
    "f12_mrib_161_ribbon_mean_slope_angle_21d_d2": {"inputs": ["close"], "func": f12_mrib_161_ribbon_mean_slope_angle_21d_d2},
    "f12_mrib_162_ribbon_mean_slope_angle_63d_d2": {"inputs": ["close"], "func": f12_mrib_162_ribbon_mean_slope_angle_63d_d2},
    "f12_mrib_163_ribbon_angle_dispersion_8mas_d2": {"inputs": ["close"], "func": f12_mrib_163_ribbon_angle_dispersion_8mas_d2},
    "f12_mrib_164_ribbon_angle_acceleration_21d_d2": {"inputs": ["close"], "func": f12_mrib_164_ribbon_angle_acceleration_21d_d2},
    "f12_mrib_165_ribbon_angle_decline_streak_max_63d_d2": {"inputs": ["close"], "func": f12_mrib_165_ribbon_angle_decline_streak_max_63d_d2},
    "f12_mrib_166_ribbon_angle_flip_to_negative_event_indicator_d2": {"inputs": ["close"], "func": f12_mrib_166_ribbon_angle_flip_to_negative_event_indicator_d2},
    "f12_mrib_167_ribbon_angle_consensus_negative_count_252d_d2": {"inputs": ["close"], "func": f12_mrib_167_ribbon_angle_consensus_negative_count_252d_d2},
    "f12_mrib_168_ribbon_angle_volatility_63d_d2": {"inputs": ["close"], "func": f12_mrib_168_ribbon_angle_volatility_63d_d2},
    "f12_mrib_169_ribbon_bandwidth_expansion_rate_21d_d2": {"inputs": ["close"], "func": f12_mrib_169_ribbon_bandwidth_expansion_rate_21d_d2},
    "f12_mrib_170_ribbon_bandwidth_expansion_rate_63d_d2": {"inputs": ["close"], "func": f12_mrib_170_ribbon_bandwidth_expansion_rate_63d_d2},
    "f12_mrib_171_ribbon_bandwidth_max_in_252d_d2": {"inputs": ["close"], "func": f12_mrib_171_ribbon_bandwidth_max_in_252d_d2},
    "f12_mrib_172_ribbon_bandwidth_zscore_252d_d2": {"inputs": ["close"], "func": f12_mrib_172_ribbon_bandwidth_zscore_252d_d2},
    "f12_mrib_173_ribbon_bandwidth_acceleration_d2": {"inputs": ["close"], "func": f12_mrib_173_ribbon_bandwidth_acceleration_d2},
    "f12_mrib_174_ribbon_bandwidth_mean_reversion_speed_d2": {"inputs": ["close"], "func": f12_mrib_174_ribbon_bandwidth_mean_reversion_speed_d2},
    "f12_mrib_175_bandwidth_expansion_during_advance_indicator_d2": {"inputs": ["close"], "func": f12_mrib_175_bandwidth_expansion_during_advance_indicator_d2},
    "f12_mrib_176_bandwidth_contraction_at_high_indicator_d2": {"inputs": ["close"], "func": f12_mrib_176_bandwidth_contraction_at_high_indicator_d2},
    "f12_mrib_177_bars_since_close_inside_ribbon_band_d2": {"inputs": ["close"], "func": f12_mrib_177_bars_since_close_inside_ribbon_band_d2},
    "f12_mrib_178_count_close_outside_ribbon_top_252d_d2": {"inputs": ["close"], "func": f12_mrib_178_count_close_outside_ribbon_top_252d_d2},
    "f12_mrib_179_count_close_outside_ribbon_bottom_252d_d2": {"inputs": ["close"], "func": f12_mrib_179_count_close_outside_ribbon_bottom_252d_d2},
    "f12_mrib_180_ribbon_top_touch_count_63d_d2": {"inputs": ["close"], "func": f12_mrib_180_ribbon_top_touch_count_63d_d2},
    "f12_mrib_181_ribbon_bottom_touch_count_63d_d2": {"inputs": ["close"], "func": f12_mrib_181_ribbon_bottom_touch_count_63d_d2},
    "f12_mrib_182_ribbon_band_break_below_event_indicator_d2": {"inputs": ["close"], "func": f12_mrib_182_ribbon_band_break_below_event_indicator_d2},
    "f12_mrib_183_ribbon_band_break_above_event_indicator_d2": {"inputs": ["close"], "func": f12_mrib_183_ribbon_band_break_above_event_indicator_d2},
    "f12_mrib_184_ribbon_internal_pull_back_count_d2": {"inputs": ["close"], "func": f12_mrib_184_ribbon_internal_pull_back_count_d2},
    "f12_mrib_185_failed_ribbon_break_count_63d_d2": {"inputs": ["close"], "func": f12_mrib_185_failed_ribbon_break_count_63d_d2},
    "f12_mrib_186_ribbon_full_traversal_event_count_d2": {"inputs": ["close"], "func": f12_mrib_186_ribbon_full_traversal_event_count_d2},
    "f12_mrib_187_ribbon_consistency_with_higher_timeframe_d2": {"inputs": ["close"], "func": f12_mrib_187_ribbon_consistency_with_higher_timeframe_d2},
    "f12_mrib_188_short_horizon_vs_long_horizon_ribbon_sign_agreement_d2": {"inputs": ["close"], "func": f12_mrib_188_short_horizon_vs_long_horizon_ribbon_sign_agreement_d2},
    "f12_mrib_189_multi_timeframe_ribbon_flip_event_count_d2": {"inputs": ["close"], "func": f12_mrib_189_multi_timeframe_ribbon_flip_event_count_d2},
    "f12_mrib_190_htf_lt_alignment_score_d2": {"inputs": ["close"], "func": f12_mrib_190_htf_lt_alignment_score_d2},
    "f12_mrib_191_weekly_ribbon_proxy_break_event_d2": {"inputs": ["close"], "func": f12_mrib_191_weekly_ribbon_proxy_break_event_d2},
    "f12_mrib_192_htf_lt_disagreement_streak_d2": {"inputs": ["close"], "func": f12_mrib_192_htf_lt_disagreement_streak_d2},
    "f12_mrib_193_coherence_persistence_in_bullish_regime_d2": {"inputs": ["close"], "func": f12_mrib_193_coherence_persistence_in_bullish_regime_d2},
    "f12_mrib_194_coherence_persistence_in_bearish_regime_d2": {"inputs": ["close"], "func": f12_mrib_194_coherence_persistence_in_bearish_regime_d2},
    "f12_mrib_195_ribbon_dispersion_conditional_on_within_5pct_of_252d_high_d2": {"inputs": ["close"], "func": f12_mrib_195_ribbon_dispersion_conditional_on_within_5pct_of_252d_high_d2},
    "f12_mrib_196_ribbon_compression_conditional_on_high_vol_regime_d2": {"inputs": ["close"], "func": f12_mrib_196_ribbon_compression_conditional_on_high_vol_regime_d2},
    "f12_mrib_197_ribbon_compression_conditional_on_low_vol_regime_d2": {"inputs": ["close"], "func": f12_mrib_197_ribbon_compression_conditional_on_low_vol_regime_d2},
    "f12_mrib_198_mean_ribbon_angle_during_new_high_days_d2": {"inputs": ["close"], "func": f12_mrib_198_mean_ribbon_angle_during_new_high_days_d2},
    "f12_mrib_199_ribbon_band_width_during_drawdown_periods_d2": {"inputs": ["close"], "func": f12_mrib_199_ribbon_band_width_during_drawdown_periods_d2},
    "f12_mrib_200_ribbon_consistency_during_uptrend_d2": {"inputs": ["close"], "func": f12_mrib_200_ribbon_consistency_during_uptrend_d2},
    "f12_mrib_201_ribbon_consistency_during_downtrend_d2": {"inputs": ["close"], "func": f12_mrib_201_ribbon_consistency_during_downtrend_d2},
    "f12_mrib_202_ribbon_dispersion_skewness_by_regime_d2": {"inputs": ["close"], "func": f12_mrib_202_ribbon_dispersion_skewness_by_regime_d2},
    "f12_mrib_203_shannon_entropy_of_ribbon_order_252d_d2": {"inputs": ["close"], "func": f12_mrib_203_shannon_entropy_of_ribbon_order_252d_d2},
    "f12_mrib_204_gini_of_ma_spread_distribution_63d_d2": {"inputs": ["close"], "func": f12_mrib_204_gini_of_ma_spread_distribution_63d_d2},
    "f12_mrib_205_ribbon_order_transition_matrix_entropy_d2": {"inputs": ["close"], "func": f12_mrib_205_ribbon_order_transition_matrix_entropy_d2},
    "f12_mrib_206_ribbon_state_richness_count_d2": {"inputs": ["close"], "func": f12_mrib_206_ribbon_state_richness_count_d2},
    "f12_mrib_207_ribbon_state_dominant_probability_d2": {"inputs": ["close"], "func": f12_mrib_207_ribbon_state_dominant_probability_d2},
    "f12_mrib_208_ribbon_state_change_rate_per_bar_d2": {"inputs": ["close"], "func": f12_mrib_208_ribbon_state_change_rate_per_bar_d2},
    "f12_mrib_209_ribbon_fan_out_event_indicator_d2": {"inputs": ["close"], "func": f12_mrib_209_ribbon_fan_out_event_indicator_d2},
    "f12_mrib_210_ribbon_fan_in_event_indicator_d2": {"inputs": ["close"], "func": f12_mrib_210_ribbon_fan_in_event_indicator_d2},
    "f12_mrib_211_fan_out_intensity_score_d2": {"inputs": ["close"], "func": f12_mrib_211_fan_out_intensity_score_d2},
    "f12_mrib_212_fan_in_intensity_score_d2": {"inputs": ["close"], "func": f12_mrib_212_fan_in_intensity_score_d2},
    "f12_mrib_213_fan_out_to_fan_in_cycle_count_252d_d2": {"inputs": ["close"], "func": f12_mrib_213_fan_out_to_fan_in_cycle_count_252d_d2},
    "f12_mrib_214_mean_time_between_fan_events_d2": {"inputs": ["close"], "func": f12_mrib_214_mean_time_between_fan_events_d2},
    "f12_mrib_215_fan_event_volume_confirmation_d2": {"inputs": ["close", "volume"], "func": f12_mrib_215_fan_event_volume_confirmation_d2},
    "f12_mrib_216_terminal_fan_out_score_d2": {"inputs": ["close"], "func": f12_mrib_216_terminal_fan_out_score_d2},
    "f12_mrib_217_ribbon_symmetry_score_d2": {"inputs": ["close"], "func": f12_mrib_217_ribbon_symmetry_score_d2},
    "f12_mrib_218_ribbon_skew_index_d2": {"inputs": ["close"], "func": f12_mrib_218_ribbon_skew_index_d2},
    "f12_mrib_219_ribbon_left_tail_dominance_d2": {"inputs": ["close"], "func": f12_mrib_219_ribbon_left_tail_dominance_d2},
    "f12_mrib_220_ribbon_right_tail_dominance_d2": {"inputs": ["close"], "func": f12_mrib_220_ribbon_right_tail_dominance_d2},
    "f12_mrib_221_ribbon_shape_stability_63d_d2": {"inputs": ["close"], "func": f12_mrib_221_ribbon_shape_stability_63d_d2},
    "f12_mrib_222_ribbon_shape_drift_velocity_d2": {"inputs": ["close"], "func": f12_mrib_222_ribbon_shape_drift_velocity_d2},
    "f12_mrib_223_gmma_compression_x_angle_inversion_composite_d2": {"inputs": ["close"], "func": f12_mrib_223_gmma_compression_x_angle_inversion_composite_d2},
    "f12_mrib_224_multi_timeframe_ribbon_breakdown_composite_d2": {"inputs": ["close"], "func": f12_mrib_224_multi_timeframe_ribbon_breakdown_composite_d2},
    "f12_mrib_225_terminal_ribbon_breakdown_score_d2": {"inputs": ["close"], "func": f12_mrib_225_terminal_ribbon_breakdown_score_d2},
}
