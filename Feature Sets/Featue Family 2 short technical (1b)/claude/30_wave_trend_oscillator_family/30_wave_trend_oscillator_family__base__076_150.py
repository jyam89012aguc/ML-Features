"""wave_trend_oscillator_family base features 076-150 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__001_075.py. Family theme:
LazyBear Wave Trend Oscillator (WT1/WT2), LazyBear Squeeze Momentum, Bollinger
Band / Keltner Channel squeeze states and band-walking dynamics.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-family
imports.
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


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=max(n // 3, 2)).mean()


# ---------------------------- indicator primitives ----------------------------

def _bb(close, n=20, mult=2.0):
    """Bollinger Bands. Returns (mid, upper, lower)."""
    mid = close.rolling(n, min_periods=max(n // 3, 2)).mean()
    sd = close.rolling(n, min_periods=max(n // 3, 2)).std()
    return mid, mid + mult * sd, mid - mult * sd


def _kc(high, low, close, n=20, mult=1.5):
    """Keltner Channel using SMA(TR). Returns (mid, upper, lower)."""
    mid = close.rolling(n, min_periods=max(n // 3, 2)).mean()
    tr = _true_range(high, low, close)
    rng = tr.rolling(n, min_periods=max(n // 3, 2)).mean()
    return mid, mid + mult * rng, mid - mult * rng


def _squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.5):
    """LazyBear squeeze-ON indicator: BB inside KC. Returns 0/1 with NaN where undefined."""
    _, bbu, bbl = _bb(close, n=n, mult=mult_bb)
    _, kcu, kcl = _kc(high, low, close, n=n, mult=mult_kc)
    on = (bbl > kcl) & (bbu < kcu)
    return on.astype(float).where(bbu.notna() & kcu.notna(), np.nan)


def _squeeze_momentum(high, low, close, n=20):
    """LazyBear squeeze momentum value: LinReg endpoint of (close - mid-of-channels) over n."""
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    sma_c = close.rolling(n, min_periods=max(n // 3, 2)).mean()
    val = close - ((hh + ll) / 2.0 + sma_c) / 2.0
    def _lr_end(w):
        valid = ~np.isnan(w)
        m = max(n // 3, 2)
        if valid.sum() < m:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        sx = ((x - xm) ** 2).sum()
        if sx == 0:
            return np.nan
        b = ((x - xm) * (wv - wm)).sum() / sx
        a = wm - b * xm
        return a + b * (len(w) - 1)
    return val.rolling(n, min_periods=max(n // 3, 2)).apply(_lr_end, raw=True)


# ============================================================
# Bucket D — BB-Squeeze states (076-100)
# ============================================================

def f30_wtof_076_bb_squeeze_on_indicator_classic(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Classic LazyBear squeeze-ON indicator (BB(20,2) inside KC(20,1.5))."""
    return _squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.5)


def f30_wtof_077_bb_squeeze_off_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: squeeze is OFF (1 − ON) — release / expansion state."""
    on = _squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.5)
    return (1.0 - on).where(on.notna(), np.nan)


def f30_wtof_078_bb_squeeze_on_dwell_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars in trailing 21d with squeeze ON — recent compression dwell."""
    on = _squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.5)
    return on.rolling(MDAYS, min_periods=WDAYS).sum()


def f30_wtof_079_bb_squeeze_on_dwell_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars in trailing 63d with squeeze ON — quarterly compression dwell."""
    on = _squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.5)
    return on.rolling(QDAYS, min_periods=MDAYS).sum()


def f30_wtof_080_bb_squeeze_max_consecutive_on_streak_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max consecutive-bar squeeze-ON run length in trailing 63d — longest compression streak."""
    on = _squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.5).fillna(0)
    arr = on.values
    # current streak at each bar
    streak = np.zeros(len(arr), dtype=float)
    s = 0
    for i in range(len(arr)):
        s = s + 1 if arr[i] > 0 else 0
        streak[i] = s
    streak_s = pd.Series(streak, index=on.index)
    return streak_s.rolling(QDAYS, min_periods=MDAYS).max()


def f30_wtof_081_bb_squeeze_current_on_streak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive-bar streak of squeeze-ON — length of ongoing compression."""
    on = _squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.5).fillna(0).values
    out = np.zeros(len(on), dtype=float)
    s = 0
    for i in range(len(on)):
        s = s + 1 if on[i] > 0 else 0
        out[i] = float(s)
    raw = _squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.5)
    return pd.Series(out, index=raw.index).where(raw.notna(), np.nan)


def f30_wtof_082_bb_squeeze_release_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: squeeze just released today (ON→OFF transition)."""
    on = _squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.5)
    cond = (on == 0) & (on.shift(1) == 1)
    return cond.astype(float).where(on.notna() & on.shift(1).notna(), np.nan)


def f30_wtof_083_bb_squeeze_release_with_negative_momentum(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: squeeze released today AND momentum < 0 — bearish release/breakdown."""
    on = _squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.5)
    rel = (on == 0) & (on.shift(1) == 1)
    mom = _squeeze_momentum(high, low, close, n=20)
    cond = rel & (mom < 0)
    return cond.astype(float).where(on.notna() & on.shift(1).notna() & mom.notna(), np.nan)


def f30_wtof_084_bb_squeeze_release_with_positive_momentum(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: squeeze released today AND momentum > 0 — bullish release/breakout."""
    on = _squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.5)
    rel = (on == 0) & (on.shift(1) == 1)
    mom = _squeeze_momentum(high, low, close, n=20)
    cond = rel & (mom > 0)
    return cond.astype(float).where(on.notna() & on.shift(1).notna() & mom.notna(), np.nan)


def f30_wtof_085_bb_squeeze_short_horizon_on_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Short-horizon squeeze-ON indicator (BB(10,1.5) inside KC(10,0.8)) — weekly compression."""
    return _squeeze_on(high, low, close, n=10, mult_bb=1.5, mult_kc=0.8)


def f30_wtof_086_bb_squeeze_long_horizon_on_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Long-horizon squeeze-ON indicator (BB(50,2) inside KC(50,1.5)) — multi-month compression."""
    return _squeeze_on(high, low, close, n=50, mult_bb=2.0, mult_kc=1.5)


def f30_wtof_087_bb_squeeze_multi_horizon_alignment(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of horizons (short/classic/long) with squeeze-ON — 0..3."""
    s = _squeeze_on(high, low, close, n=10, mult_bb=1.5, mult_kc=0.8).fillna(0)
    c = _squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.5).fillna(0)
    l = _squeeze_on(high, low, close, n=50, mult_bb=2.0, mult_kc=1.5).fillna(0)
    return s + c + l


def f30_wtof_088_bb_squeeze_post_release_5d_return(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5d log-return given squeeze released within prior 5 bars — post-release breakout magnitude."""
    on = _squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.5)
    rel = ((on == 0) & (on.shift(1) == 1)).astype(float)
    trig = rel.rolling(WDAYS, min_periods=2).max()
    ret = _safe_log(close) - _safe_log(close.shift(WDAYS))
    return ret.where(trig > 0, np.nan)


def f30_wtof_089_bb_squeeze_release_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of squeeze-release events in trailing 63d — release frequency."""
    on = _squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.5)
    rel = ((on == 0) & (on.shift(1) == 1)).astype(float)
    return rel.rolling(QDAYS, min_periods=MDAYS).sum()


def f30_wtof_090_bb_squeeze_short_release_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: short-horizon squeeze released today (10/1.5/0.8)."""
    on = _squeeze_on(high, low, close, n=10, mult_bb=1.5, mult_kc=0.8)
    cond = (on == 0) & (on.shift(1) == 1)
    return cond.astype(float).where(on.notna() & on.shift(1).notna(), np.nan)


def f30_wtof_091_bb_squeeze_long_release_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: long-horizon squeeze released today (50/2/1.5)."""
    on = _squeeze_on(high, low, close, n=50, mult_bb=2.0, mult_kc=1.5)
    cond = (on == 0) & (on.shift(1) == 1)
    return cond.astype(float).where(on.notna() & on.shift(1).notna(), np.nan)


def f30_wtof_092_bb_squeeze_bars_since_last_release(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since the last squeeze-release event — staleness of last release."""
    on = _squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.5)
    rel = ((on == 0) & (on.shift(1) == 1)).fillna(False).values
    out = np.full(len(rel), np.nan, dtype=float)
    last = -1
    for i in range(len(rel)):
        if rel[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    raw = on
    return pd.Series(out, index=raw.index).where(raw.notna(), np.nan)


def f30_wtof_093_bb_squeeze_on_dwell_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars in trailing 252d with squeeze ON — annual compression dwell."""
    on = _squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.5)
    return on.rolling(YDAYS, min_periods=QDAYS).sum()


def f30_wtof_094_bb_squeeze_post_release_momentum_sign(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sign of squeeze-momentum at bars where squeeze released within prior 5d."""
    on = _squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.5)
    rel = ((on == 0) & (on.shift(1) == 1)).astype(float)
    trig = rel.rolling(WDAYS, min_periods=2).max()
    mom = _squeeze_momentum(high, low, close, n=20)
    return np.sign(mom).where(trig > 0, np.nan)


def f30_wtof_095_bb_squeeze_release_after_long_compression_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: squeeze released today AND prior ON-streak was ≥ 10 bars — compressed-spring release."""
    on = _squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.5).fillna(0).values
    streak = np.zeros(len(on), dtype=float)
    s = 0
    for i in range(len(on)):
        s = s + 1 if on[i] > 0 else 0
        streak[i] = s
    raw = _squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.5)
    rel = ((raw == 0) & (raw.shift(1) == 1))
    prior_streak = pd.Series(streak, index=raw.index).shift(1)
    cond = rel & (prior_streak >= 10)
    return cond.astype(float).where(raw.notna() & raw.shift(1).notna(), np.nan)


def f30_wtof_096_bb_squeeze_on_fraction_504d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of trailing 504d with squeeze ON — biennial compression-regime share."""
    on = _squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.5)
    return on.rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f30_wtof_097_bb_squeeze_alignment_short_classic(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: short-horizon AND classic squeezes are both ON — multi-cycle compression alignment."""
    s = _squeeze_on(high, low, close, n=10, mult_bb=1.5, mult_kc=0.8)
    c = _squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.5)
    return ((s == 1) & (c == 1)).astype(float).where(s.notna() & c.notna(), np.nan)


def f30_wtof_098_bb_squeeze_classic_then_long_release(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: classic-squeeze released today AND long-horizon squeeze was ON within prior 21d."""
    c = _squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.5)
    l = _squeeze_on(high, low, close, n=50, mult_bb=2.0, mult_kc=1.5)
    rel = (c == 0) & (c.shift(1) == 1)
    l_recent = (l.fillna(0).rolling(MDAYS, min_periods=WDAYS).max() == 1)
    cond = rel & l_recent
    return cond.astype(float).where(c.notna() & c.shift(1).notna() & l.notna(), np.nan)


def f30_wtof_099_bb_squeeze_release_then_drawdown_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5d drawdown (min-low / close[t−5]) at bars where squeeze released within prior 5d."""
    on = _squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.5)
    rel = ((on == 0) & (on.shift(1) == 1)).astype(float)
    trig = rel.rolling(WDAYS, min_periods=2).max()
    rmin = low.rolling(WDAYS, min_periods=2).min()
    dd = _safe_div(rmin, close.shift(WDAYS)) - 1.0
    return dd.where(trig > 0, np.nan)


def f30_wtof_100_bb_squeeze_short_dwell_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars in trailing 5d with short-horizon squeeze ON — weekly compression dwell."""
    on = _squeeze_on(high, low, close, n=10, mult_bb=1.5, mult_kc=0.8)
    return on.rolling(WDAYS, min_periods=2).sum()


# ============================================================
# Bucket E — BB width / position / walking-the-band (101-125)
# ============================================================

def f30_wtof_101_bb_width_pct_of_mid_20d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """BB width as fraction of mid (upper−lower)/mid — volatility-cone width."""
    mid, u, l = _bb(close, n=20, mult=2.0)
    return _safe_div(u - l, mid)


def f30_wtof_102_bb_width_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of BB(20) width in trailing 252d — anomalously wide / narrow regime."""
    mid, u, l = _bb(close, n=20, mult=2.0)
    w = _safe_div(u - l, mid)
    return _rolling_zscore(w, YDAYS, min_periods=QDAYS)


def f30_wtof_103_bb_width_percentile_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of BB(20) width in trailing 252d — width position in cone."""
    mid, u, l = _bb(close, n=20, mult=2.0)
    w = _safe_div(u - l, mid)
    return w.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f30_wtof_104_bb_width_falling_from_63d_max_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: BB(20) width was within 1% of 63d max in prior 5 bars and is now falling."""
    mid, u, l = _bb(close, n=20, mult=2.0)
    w = _safe_div(u - l, mid)
    rmax = w.rolling(QDAYS, min_periods=MDAYS).max()
    near_max = (w >= 0.99 * rmax)
    cond = near_max.shift(1).fillna(False) & (w.diff() < 0)
    return cond.astype(float).where(w.notna(), np.nan)


def f30_wtof_105_bb_position_in_bands_20d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Position of close in BB(20,2): (close−lower)/(upper−lower). 0=lower band, 1=upper."""
    mid, u, l = _bb(close, n=20, mult=2.0)
    return _safe_div(close - l, u - l)


def f30_wtof_106_bb_above_upper_indicator_20d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: close above BB(20,2) upper — extended-above-band reading."""
    _, u, _ = _bb(close, n=20, mult=2.0)
    return (close > u).astype(float).where(u.notna(), np.nan)


def f30_wtof_107_bb_walking_upper_band_count_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count in trailing 21d of bars closing above BB(20,2) upper — walking-the-band tally."""
    _, u, _ = _bb(close, n=20, mult=2.0)
    above = (close > u).astype(float)
    return above.rolling(MDAYS, min_periods=WDAYS).sum()


def f30_wtof_108_bb_walking_upper_current_streak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive-bar streak of close > BB(20,2) upper — ongoing walking-band length."""
    _, u, _ = _bb(close, n=20, mult=2.0)
    above = (close > u)
    arr = above.fillna(False).values
    out = np.zeros(len(arr), dtype=float)
    s = 0
    for i in range(len(arr)):
        s = s + 1 if arr[i] else 0
        out[i] = float(s)
    return pd.Series(out, index=u.index).where(u.notna(), np.nan)


def f30_wtof_109_bb_walking_upper_max_streak_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max consecutive-bar walking-upper-band streak in trailing 63d."""
    _, u, _ = _bb(close, n=20, mult=2.0)
    above = (close > u).fillna(False).values
    streak = np.zeros(len(above), dtype=float)
    s = 0
    for i in range(len(above)):
        s = s + 1 if above[i] else 0
        streak[i] = s
    streak_s = pd.Series(streak, index=u.index)
    return streak_s.rolling(QDAYS, min_periods=MDAYS).max()


def f30_wtof_110_bb_atr_normalized_distance_above_upper(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21-normalized distance of close above BB(20,2) upper (negative when inside)."""
    _, u, _ = _bb(close, n=20, mult=2.0)
    atr = _atr(high, low, close, n=MDAYS)
    return _safe_div(close - u, atr)


def f30_wtof_111_bb_close_at_upper_dwell_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars in trailing 21d with close within 1% of BB(20,2) upper — sticky-at-upper dwell."""
    _, u, _ = _bb(close, n=20, mult=2.0)
    near = (close >= 0.99 * u).astype(float)
    return near.rolling(MDAYS, min_periods=WDAYS).sum()


def f30_wtof_112_bb_width_short_horizon_10d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Short-horizon BB(10,2) width % of mid — weekly-cycle volatility-cone width."""
    mid, u, l = _bb(close, n=10, mult=2.0)
    return _safe_div(u - l, mid)


def f30_wtof_113_bb_width_long_horizon_50d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Long-horizon BB(50,2) width % of mid — multi-month volatility-cone width."""
    mid, u, l = _bb(close, n=50, mult=2.0)
    return _safe_div(u - l, mid)


def f30_wtof_114_bb_width_short_minus_long_spread(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Short(10) − long(50) BB width — fast vs slow volatility-cone divergence."""
    m1, u1, l1 = _bb(close, n=10, mult=2.0)
    m2, u2, l2 = _bb(close, n=50, mult=2.0)
    return _safe_div(u1 - l1, m1) - _safe_div(u2 - l2, m2)


def f30_wtof_115_bb_walking_upper_then_inside_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: close was > BB(20,2) upper within last 5 bars and is now ≤ upper (band-walk failure)."""
    _, u, _ = _bb(close, n=20, mult=2.0)
    above = (close > u)
    recent = above.rolling(WDAYS, min_periods=2).max().fillna(False).astype(bool)
    cond = (recent.shift(1).fillna(False)) & (~above) & u.notna()
    return cond.astype(float).where(u.notna(), np.nan)


def f30_wtof_116_bb_close_above_upper_then_back_inside_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: yesterday close > BB(20,2) upper, today close ≤ upper — back-inside-band reversal."""
    _, u, _ = _bb(close, n=20, mult=2.0)
    cond = (close.shift(1) > u.shift(1)) & (close <= u)
    return cond.astype(float).where(u.notna() & u.shift(1).notna(), np.nan)


def f30_wtof_117_bb_width_skew_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63d skew of BB(20) width — directionality of width distribution."""
    mid, u, l = _bb(close, n=20, mult=2.0)
    w = _safe_div(u - l, mid)
    return w.rolling(QDAYS, min_periods=MDAYS).skew()


def f30_wtof_118_bb_position_above_one_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: BB(20,2) position > 1 (close above upper) — same as close>upper but on position."""
    mid, u, l = _bb(close, n=20, mult=2.0)
    pos = _safe_div(close - l, u - l)
    return (pos > 1.0).astype(float).where(pos.notna(), np.nan)


def f30_wtof_119_bb_distance_from_lower_band_atr_norm(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21-normalized distance of close above BB(20,2) lower — buffer from down-side band."""
    _, _, l = _bb(close, n=20, mult=2.0)
    atr = _atr(high, low, close, n=MDAYS)
    return _safe_div(close - l, atr)


def f30_wtof_120_bb_position_above_one_dwell_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars in trailing 63d with BB(20,2) position > 1 — quarterly above-upper dwell."""
    mid, u, l = _bb(close, n=20, mult=2.0)
    pos = _safe_div(close - l, u - l)
    above = (pos > 1.0).astype(float)
    return above.rolling(QDAYS, min_periods=MDAYS).sum()


def f30_wtof_121_bb_width_252d_log_change(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log-change of BB(20) width over 252d — annual volatility-cone trend."""
    mid, u, l = _bb(close, n=20, mult=2.0)
    w = _safe_div(u - l, mid)
    return _safe_log(w) - _safe_log(w.shift(YDAYS))


def f30_wtof_122_bb_walking_upper_releases_into_negative_momentum(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: close was > upper within last 5 bars, now ≤ upper, and momentum < 0 (band-walk fail with bearish mom)."""
    _, u, _ = _bb(close, n=20, mult=2.0)
    above = (close > u)
    recent = above.rolling(WDAYS, min_periods=2).max().fillna(False).astype(bool)
    fail = recent.shift(1, fill_value=False).astype(bool) & (~above.fillna(False).astype(bool))
    mom = _squeeze_momentum(high, low, close, n=20)
    cond = fail & (mom < 0)
    return cond.astype(float).where(u.notna() & mom.notna(), np.nan)


def f30_wtof_123_bb_position_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of BB(20,2) position in trailing 252d — anomalous position in bands."""
    mid, u, l = _bb(close, n=20, mult=2.0)
    pos = _safe_div(close - l, u - l)
    return _rolling_zscore(pos, YDAYS, min_periods=QDAYS)


def f30_wtof_124_bb_walking_upper_count_short_horizon_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count in trailing 5d of close > BB(10,2) upper — weekly walking-band intensity."""
    _, u, _ = _bb(close, n=10, mult=2.0)
    above = (close > u).astype(float)
    return above.rolling(WDAYS, min_periods=2).sum()


def f30_wtof_125_bb_width_5d_slope(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5d linear-regression slope of BB(20) width — short-horizon volatility-cone velocity."""
    mid, u, l = _bb(close, n=20, mult=2.0)
    w = _safe_div(u - l, mid)
    return _rolling_slope(w, WDAYS, min_periods=3)


# ============================================================
# Bucket F — BB-KC interactions / multi-band (126-140)
# ============================================================

def f30_wtof_126_kc_width_pct_of_mid_20d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Keltner(20,1.5) channel width as fraction of mid — true-range-based volatility cone."""
    mid, u, l = _kc(high, low, close, n=20, mult=1.5)
    return _safe_div(u - l, mid)


def f30_wtof_127_kc_width_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of KC(20,1.5) width in trailing 252d — anomalously wide/narrow KC regime."""
    mid, u, l = _kc(high, low, close, n=20, mult=1.5)
    w = _safe_div(u - l, mid)
    return _rolling_zscore(w, YDAYS, min_periods=QDAYS)


def f30_wtof_128_bb_minus_kc_width_ratio(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """BB(20,2) width / KC(20,1.5) width — squeeze-ratio (>1 = BB outside KC)."""
    mb, ub, lb = _bb(close, n=20, mult=2.0)
    mk, uk, lk = _kc(high, low, close, n=20, mult=1.5)
    return _safe_div(ub - lb, uk - lk)


def f30_wtof_129_bb_inside_kc_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: BB(20,2) entirely inside KC(20,1.5) — equivalent to LazyBear squeeze ON."""
    mb, ub, lb = _bb(close, n=20, mult=2.0)
    mk, uk, lk = _kc(high, low, close, n=20, mult=1.5)
    inside = (lb > lk) & (ub < uk)
    return inside.astype(float).where(ub.notna() & uk.notna(), np.nan)


def f30_wtof_130_bb_outside_kc_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: BB(20,2) entirely outside KC(20,1.5) — extreme-expansion regime."""
    mb, ub, lb = _bb(close, n=20, mult=2.0)
    mk, uk, lk = _kc(high, low, close, n=20, mult=1.5)
    outside = (lb < lk) & (ub > uk)
    return outside.astype(float).where(ub.notna() & uk.notna(), np.nan)


def f30_wtof_131_bb_kc_crossover_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of BB-vs-KC inside/outside state flips in trailing 63d — band-regime churn."""
    mb, ub, lb = _bb(close, n=20, mult=2.0)
    mk, uk, lk = _kc(high, low, close, n=20, mult=1.5)
    inside = ((lb > lk) & (ub < uk)).astype(float)
    flip = (inside != inside.shift(1)) & inside.notna() & inside.shift(1).notna()
    return flip.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f30_wtof_132_close_above_kc_upper_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: close above KC(20,1.5) upper — extension beyond Keltner channel."""
    mk, uk, lk = _kc(high, low, close, n=20, mult=1.5)
    return (close > uk).astype(float).where(uk.notna(), np.nan)


def f30_wtof_133_close_above_kc_upper_dwell_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars in trailing 21d with close > KC(20,1.5) upper — sustained KC-above dwell."""
    mk, uk, lk = _kc(high, low, close, n=20, mult=1.5)
    above = (close > uk).astype(float)
    return above.rolling(MDAYS, min_periods=WDAYS).sum()


def f30_wtof_134_multi_band_alignment_above_upper(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: close above BB upper AND above KC upper — multi-band-aligned overextension."""
    _, ub, _ = _bb(close, n=20, mult=2.0)
    _, uk, _ = _kc(high, low, close, n=20, mult=1.5)
    cond = (close > ub) & (close > uk)
    return cond.astype(float).where(ub.notna() & uk.notna(), np.nan)


def f30_wtof_135_bb_outside_kc_then_back_inside_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: BB was outside KC within prior 5 bars and is now inside-or-overlapping (expansion failure)."""
    mb, ub, lb = _bb(close, n=20, mult=2.0)
    mk, uk, lk = _kc(high, low, close, n=20, mult=1.5)
    outside = (lb < lk) & (ub > uk)
    recent_out = outside.rolling(WDAYS, min_periods=2).max().fillna(False).astype(bool)
    cond = recent_out.shift(1).fillna(False) & (~outside)
    return cond.astype(float).where(ub.notna() & uk.notna(), np.nan)


def f30_wtof_136_bb_kc_overlap_ratio(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Overlap fraction of BB inside KC: max(0, min(ub,uk) − max(lb,lk)) / (ub−lb)."""
    mb, ub, lb = _bb(close, n=20, mult=2.0)
    mk, uk, lk = _kc(high, low, close, n=20, mult=1.5)
    inter_top = pd.concat([ub, uk], axis=1).min(axis=1)
    inter_bot = pd.concat([lb, lk], axis=1).max(axis=1)
    inter = (inter_top - inter_bot).clip(lower=0.0)
    return _safe_div(inter, ub - lb)


def f30_wtof_137_kc_width_short_horizon_10d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Short-horizon KC(10,1.0) width % of mid — weekly Keltner-channel cone."""
    mid, u, l = _kc(high, low, close, n=10, mult=1.0)
    return _safe_div(u - l, mid)


def f30_wtof_138_kc_width_long_horizon_50d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Long-horizon KC(50,1.5) width % of mid — multi-month Keltner-channel cone."""
    mid, u, l = _kc(high, low, close, n=50, mult=1.5)
    return _safe_div(u - l, mid)


def f30_wtof_139_bb_kc_width_correlation_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63d rolling correlation of BB(20) width with KC(20) width — vol-source agreement."""
    mb, ub, lb = _bb(close, n=20, mult=2.0)
    mk, uk, lk = _kc(high, low, close, n=20, mult=1.5)
    wb = _safe_div(ub - lb, mb)
    wk = _safe_div(uk - lk, mk)
    return wb.rolling(QDAYS, min_periods=MDAYS).corr(wk)


def f30_wtof_140_bb_outside_kc_dwell_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars in trailing 63d with BB outside KC — expansion-regime dwell."""
    mb, ub, lb = _bb(close, n=20, mult=2.0)
    mk, uk, lk = _kc(high, low, close, n=20, mult=1.5)
    outside = ((lb < lk) & (ub > uk)).astype(float)
    return outside.rolling(QDAYS, min_periods=MDAYS).sum()


# ============================================================
# Bucket G — Composite WTO + Squeeze + Band (141-150)
# ============================================================

def _wto_local(high, low, close, n1=10, n2=21):
    ap = (high + low + close) / 3.0
    esa = _ema(ap, n1)
    d = _ema((ap - esa).abs(), n1)
    ci = _safe_div(ap - esa, 0.015 * d)
    tci = _ema(ci, n2)
    wt1 = tci
    wt2 = wt1.rolling(4, min_periods=2).mean()
    return wt1, wt2


def f30_wtof_141_wto_bearish_cross_and_squeeze_release(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: WT1/WT2 bearish cross AND squeeze just released — joint topping/release signal."""
    wt1, wt2 = _wto_local(high, low, close, 10, 21)
    bear = (wt1 < wt2) & (wt1.shift(1) >= wt2.shift(1))
    on = _squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.5)
    rel = (on == 0) & (on.shift(1) == 1)
    cond = bear & rel
    return cond.astype(float).where(wt1.notna() & on.notna() & on.shift(1).notna(), np.nan)


def f30_wtof_142_wto_overbought_and_bb_walking_upper(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: WT1 ≥ 60 AND close > BB(20,2) upper — overbought-and-walking-the-band."""
    wt1, _ = _wto_local(high, low, close, 10, 21)
    _, ub, _ = _bb(close, n=20, mult=2.0)
    cond = (wt1 >= 60.0) & (close > ub)
    return cond.astype(float).where(wt1.notna() & ub.notna(), np.nan)


def f30_wtof_143_topping_alignment_count(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of topping-aligned signals (0..4): WT1≥60, WT1<WT2, close>BBu, momentum<0."""
    wt1, wt2 = _wto_local(high, low, close, 10, 21)
    _, ub, _ = _bb(close, n=20, mult=2.0)
    mom = _squeeze_momentum(high, low, close, n=20)
    s1 = (wt1 >= 60.0).astype(float)
    s2 = (wt1 < wt2).astype(float)
    s3 = (close > ub).astype(float)
    s4 = (mom < 0).astype(float)
    cnt = s1 + s2 + s3 + s4
    return cnt.where(wt1.notna() & ub.notna() & mom.notna(), np.nan)


def f30_wtof_144_exhaustion_signal_density_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean over trailing 21d of: 0.25*(WT1≥60 + WT1<WT2 + close>BBu + mom<0) — density of topping."""
    wt1, wt2 = _wto_local(high, low, close, 10, 21)
    _, ub, _ = _bb(close, n=20, mult=2.0)
    mom = _squeeze_momentum(high, low, close, n=20)
    s = (wt1 >= 60.0).astype(float) + (wt1 < wt2).astype(float) + (close > ub).astype(float) + (mom < 0).astype(float)
    density = (s / 4.0)
    return density.rolling(MDAYS, min_periods=WDAYS).mean()


def f30_wtof_145_full_topping_complex_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: WT1 ≥ 60 AND WT1 < WT2 AND close > BBu AND momentum < 0 — all four aligned bearish."""
    wt1, wt2 = _wto_local(high, low, close, 10, 21)
    _, ub, _ = _bb(close, n=20, mult=2.0)
    mom = _squeeze_momentum(high, low, close, n=20)
    cond = (wt1 >= 60.0) & (wt1 < wt2) & (close > ub) & (mom < 0)
    return cond.astype(float).where(wt1.notna() & ub.notna() & mom.notna(), np.nan)


def f30_wtof_146_wto_bearish_cross_at_252d_high_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: WT1/WT2 bearish cross occurring AT or within 1% of 252d-rolling-high."""
    wt1, wt2 = _wto_local(high, low, close, 10, 21)
    bear = (wt1 < wt2) & (wt1.shift(1) >= wt2.shift(1))
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near_peak = (high >= 0.99 * rmax)
    cond = bear & near_peak
    return cond.astype(float).where(wt1.notna() & rmax.notna(), np.nan)


def f30_wtof_147_squeeze_momentum_neg_after_bb_walk(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: BB upper-band-walk in prior 21d AND today momentum < 0 — walk-then-fail to bearish mom."""
    _, ub, _ = _bb(close, n=20, mult=2.0)
    above = (close > ub).astype(float)
    walk = (above.rolling(MDAYS, min_periods=WDAYS).sum() >= 3)
    mom = _squeeze_momentum(high, low, close, n=20)
    cond = walk.shift(1).fillna(False) & (mom < 0)
    return cond.astype(float).where(ub.notna() & mom.notna(), np.nan)


def f30_wtof_148_compound_overbought_release_signal_dwell_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars in trailing 63d where: (WT1≥60 AND squeeze just released within 5d). Joint-event dwell."""
    wt1, _ = _wto_local(high, low, close, 10, 21)
    on = _squeeze_on(high, low, close, n=20, mult_bb=2.0, mult_kc=1.5)
    rel = ((on == 0) & (on.shift(1) == 1)).astype(float)
    recent_rel = rel.rolling(WDAYS, min_periods=2).max()
    flag = ((wt1 >= 60.0) & (recent_rel > 0)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f30_wtof_149_full_topping_complex_dwell_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars in trailing 21d where full topping complex is active — sustained topping-alignment dwell."""
    wt1, wt2 = _wto_local(high, low, close, 10, 21)
    _, ub, _ = _bb(close, n=20, mult=2.0)
    mom = _squeeze_momentum(high, low, close, n=20)
    cond = ((wt1 >= 60.0) & (wt1 < wt2) & (close > ub) & (mom < 0)).astype(float)
    return cond.rolling(MDAYS, min_periods=WDAYS).sum()


def f30_wtof_150_wto_long_horizon_and_squeeze_long_horizon_alignment(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: long-horizon WT1(20,50) ≥ 60 AND long-horizon squeeze (50/2/1.5) ON — slow-cycle topping setup."""
    wt1, _ = _wto_local(high, low, close, 20, 50)
    on = _squeeze_on(high, low, close, n=50, mult_bb=2.0, mult_kc=1.5)
    cond = (wt1 >= 60.0) & (on == 1)
    return cond.astype(float).where(wt1.notna() & on.notna(), np.nan)


# ============================================================
#                         REGISTRY 076-150
# ============================================================

WAVE_TREND_OSCILLATOR_FAMILY_BASE_REGISTRY_076_150 = {
    "f30_wtof_076_bb_squeeze_on_indicator_classic": {"inputs": ["high", "low", "close"], "func": f30_wtof_076_bb_squeeze_on_indicator_classic},
    "f30_wtof_077_bb_squeeze_off_indicator": {"inputs": ["high", "low", "close"], "func": f30_wtof_077_bb_squeeze_off_indicator},
    "f30_wtof_078_bb_squeeze_on_dwell_21d": {"inputs": ["high", "low", "close"], "func": f30_wtof_078_bb_squeeze_on_dwell_21d},
    "f30_wtof_079_bb_squeeze_on_dwell_63d": {"inputs": ["high", "low", "close"], "func": f30_wtof_079_bb_squeeze_on_dwell_63d},
    "f30_wtof_080_bb_squeeze_max_consecutive_on_streak_63d": {"inputs": ["high", "low", "close"], "func": f30_wtof_080_bb_squeeze_max_consecutive_on_streak_63d},
    "f30_wtof_081_bb_squeeze_current_on_streak": {"inputs": ["high", "low", "close"], "func": f30_wtof_081_bb_squeeze_current_on_streak},
    "f30_wtof_082_bb_squeeze_release_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_082_bb_squeeze_release_event},
    "f30_wtof_083_bb_squeeze_release_with_negative_momentum": {"inputs": ["high", "low", "close"], "func": f30_wtof_083_bb_squeeze_release_with_negative_momentum},
    "f30_wtof_084_bb_squeeze_release_with_positive_momentum": {"inputs": ["high", "low", "close"], "func": f30_wtof_084_bb_squeeze_release_with_positive_momentum},
    "f30_wtof_085_bb_squeeze_short_horizon_on_indicator": {"inputs": ["high", "low", "close"], "func": f30_wtof_085_bb_squeeze_short_horizon_on_indicator},
    "f30_wtof_086_bb_squeeze_long_horizon_on_indicator": {"inputs": ["high", "low", "close"], "func": f30_wtof_086_bb_squeeze_long_horizon_on_indicator},
    "f30_wtof_087_bb_squeeze_multi_horizon_alignment": {"inputs": ["high", "low", "close"], "func": f30_wtof_087_bb_squeeze_multi_horizon_alignment},
    "f30_wtof_088_bb_squeeze_post_release_5d_return": {"inputs": ["high", "low", "close"], "func": f30_wtof_088_bb_squeeze_post_release_5d_return},
    "f30_wtof_089_bb_squeeze_release_count_63d": {"inputs": ["high", "low", "close"], "func": f30_wtof_089_bb_squeeze_release_count_63d},
    "f30_wtof_090_bb_squeeze_short_release_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_090_bb_squeeze_short_release_event},
    "f30_wtof_091_bb_squeeze_long_release_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_091_bb_squeeze_long_release_event},
    "f30_wtof_092_bb_squeeze_bars_since_last_release": {"inputs": ["high", "low", "close"], "func": f30_wtof_092_bb_squeeze_bars_since_last_release},
    "f30_wtof_093_bb_squeeze_on_dwell_252d": {"inputs": ["high", "low", "close"], "func": f30_wtof_093_bb_squeeze_on_dwell_252d},
    "f30_wtof_094_bb_squeeze_post_release_momentum_sign": {"inputs": ["high", "low", "close"], "func": f30_wtof_094_bb_squeeze_post_release_momentum_sign},
    "f30_wtof_095_bb_squeeze_release_after_long_compression_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_095_bb_squeeze_release_after_long_compression_event},
    "f30_wtof_096_bb_squeeze_on_fraction_504d": {"inputs": ["high", "low", "close"], "func": f30_wtof_096_bb_squeeze_on_fraction_504d},
    "f30_wtof_097_bb_squeeze_alignment_short_classic": {"inputs": ["high", "low", "close"], "func": f30_wtof_097_bb_squeeze_alignment_short_classic},
    "f30_wtof_098_bb_squeeze_classic_then_long_release": {"inputs": ["high", "low", "close"], "func": f30_wtof_098_bb_squeeze_classic_then_long_release},
    "f30_wtof_099_bb_squeeze_release_then_drawdown_5d": {"inputs": ["high", "low", "close"], "func": f30_wtof_099_bb_squeeze_release_then_drawdown_5d},
    "f30_wtof_100_bb_squeeze_short_dwell_5d": {"inputs": ["high", "low", "close"], "func": f30_wtof_100_bb_squeeze_short_dwell_5d},
    "f30_wtof_101_bb_width_pct_of_mid_20d": {"inputs": ["high", "low", "close"], "func": f30_wtof_101_bb_width_pct_of_mid_20d},
    "f30_wtof_102_bb_width_zscore_252d": {"inputs": ["high", "low", "close"], "func": f30_wtof_102_bb_width_zscore_252d},
    "f30_wtof_103_bb_width_percentile_252d": {"inputs": ["high", "low", "close"], "func": f30_wtof_103_bb_width_percentile_252d},
    "f30_wtof_104_bb_width_falling_from_63d_max_indicator": {"inputs": ["high", "low", "close"], "func": f30_wtof_104_bb_width_falling_from_63d_max_indicator},
    "f30_wtof_105_bb_position_in_bands_20d": {"inputs": ["high", "low", "close"], "func": f30_wtof_105_bb_position_in_bands_20d},
    "f30_wtof_106_bb_above_upper_indicator_20d": {"inputs": ["high", "low", "close"], "func": f30_wtof_106_bb_above_upper_indicator_20d},
    "f30_wtof_107_bb_walking_upper_band_count_21d": {"inputs": ["high", "low", "close"], "func": f30_wtof_107_bb_walking_upper_band_count_21d},
    "f30_wtof_108_bb_walking_upper_current_streak": {"inputs": ["high", "low", "close"], "func": f30_wtof_108_bb_walking_upper_current_streak},
    "f30_wtof_109_bb_walking_upper_max_streak_63d": {"inputs": ["high", "low", "close"], "func": f30_wtof_109_bb_walking_upper_max_streak_63d},
    "f30_wtof_110_bb_atr_normalized_distance_above_upper": {"inputs": ["high", "low", "close"], "func": f30_wtof_110_bb_atr_normalized_distance_above_upper},
    "f30_wtof_111_bb_close_at_upper_dwell_21d": {"inputs": ["high", "low", "close"], "func": f30_wtof_111_bb_close_at_upper_dwell_21d},
    "f30_wtof_112_bb_width_short_horizon_10d": {"inputs": ["high", "low", "close"], "func": f30_wtof_112_bb_width_short_horizon_10d},
    "f30_wtof_113_bb_width_long_horizon_50d": {"inputs": ["high", "low", "close"], "func": f30_wtof_113_bb_width_long_horizon_50d},
    "f30_wtof_114_bb_width_short_minus_long_spread": {"inputs": ["high", "low", "close"], "func": f30_wtof_114_bb_width_short_minus_long_spread},
    "f30_wtof_115_bb_walking_upper_then_inside_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_115_bb_walking_upper_then_inside_event},
    "f30_wtof_116_bb_close_above_upper_then_back_inside_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_116_bb_close_above_upper_then_back_inside_event},
    "f30_wtof_117_bb_width_skew_63d": {"inputs": ["high", "low", "close"], "func": f30_wtof_117_bb_width_skew_63d},
    "f30_wtof_118_bb_position_above_one_indicator": {"inputs": ["high", "low", "close"], "func": f30_wtof_118_bb_position_above_one_indicator},
    "f30_wtof_119_bb_distance_from_lower_band_atr_norm": {"inputs": ["high", "low", "close"], "func": f30_wtof_119_bb_distance_from_lower_band_atr_norm},
    "f30_wtof_120_bb_position_above_one_dwell_63d": {"inputs": ["high", "low", "close"], "func": f30_wtof_120_bb_position_above_one_dwell_63d},
    "f30_wtof_121_bb_width_252d_log_change": {"inputs": ["high", "low", "close"], "func": f30_wtof_121_bb_width_252d_log_change},
    "f30_wtof_122_bb_walking_upper_releases_into_negative_momentum": {"inputs": ["high", "low", "close"], "func": f30_wtof_122_bb_walking_upper_releases_into_negative_momentum},
    "f30_wtof_123_bb_position_zscore_252d": {"inputs": ["high", "low", "close"], "func": f30_wtof_123_bb_position_zscore_252d},
    "f30_wtof_124_bb_walking_upper_count_short_horizon_5d": {"inputs": ["high", "low", "close"], "func": f30_wtof_124_bb_walking_upper_count_short_horizon_5d},
    "f30_wtof_125_bb_width_5d_slope": {"inputs": ["high", "low", "close"], "func": f30_wtof_125_bb_width_5d_slope},
    "f30_wtof_126_kc_width_pct_of_mid_20d": {"inputs": ["high", "low", "close"], "func": f30_wtof_126_kc_width_pct_of_mid_20d},
    "f30_wtof_127_kc_width_zscore_252d": {"inputs": ["high", "low", "close"], "func": f30_wtof_127_kc_width_zscore_252d},
    "f30_wtof_128_bb_minus_kc_width_ratio": {"inputs": ["high", "low", "close"], "func": f30_wtof_128_bb_minus_kc_width_ratio},
    "f30_wtof_129_bb_inside_kc_indicator": {"inputs": ["high", "low", "close"], "func": f30_wtof_129_bb_inside_kc_indicator},
    "f30_wtof_130_bb_outside_kc_indicator": {"inputs": ["high", "low", "close"], "func": f30_wtof_130_bb_outside_kc_indicator},
    "f30_wtof_131_bb_kc_crossover_count_63d": {"inputs": ["high", "low", "close"], "func": f30_wtof_131_bb_kc_crossover_count_63d},
    "f30_wtof_132_close_above_kc_upper_indicator": {"inputs": ["high", "low", "close"], "func": f30_wtof_132_close_above_kc_upper_indicator},
    "f30_wtof_133_close_above_kc_upper_dwell_21d": {"inputs": ["high", "low", "close"], "func": f30_wtof_133_close_above_kc_upper_dwell_21d},
    "f30_wtof_134_multi_band_alignment_above_upper": {"inputs": ["high", "low", "close"], "func": f30_wtof_134_multi_band_alignment_above_upper},
    "f30_wtof_135_bb_outside_kc_then_back_inside_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_135_bb_outside_kc_then_back_inside_event},
    "f30_wtof_136_bb_kc_overlap_ratio": {"inputs": ["high", "low", "close"], "func": f30_wtof_136_bb_kc_overlap_ratio},
    "f30_wtof_137_kc_width_short_horizon_10d": {"inputs": ["high", "low", "close"], "func": f30_wtof_137_kc_width_short_horizon_10d},
    "f30_wtof_138_kc_width_long_horizon_50d": {"inputs": ["high", "low", "close"], "func": f30_wtof_138_kc_width_long_horizon_50d},
    "f30_wtof_139_bb_kc_width_correlation_63d": {"inputs": ["high", "low", "close"], "func": f30_wtof_139_bb_kc_width_correlation_63d},
    "f30_wtof_140_bb_outside_kc_dwell_63d": {"inputs": ["high", "low", "close"], "func": f30_wtof_140_bb_outside_kc_dwell_63d},
    "f30_wtof_141_wto_bearish_cross_and_squeeze_release": {"inputs": ["high", "low", "close"], "func": f30_wtof_141_wto_bearish_cross_and_squeeze_release},
    "f30_wtof_142_wto_overbought_and_bb_walking_upper": {"inputs": ["high", "low", "close"], "func": f30_wtof_142_wto_overbought_and_bb_walking_upper},
    "f30_wtof_143_topping_alignment_count": {"inputs": ["high", "low", "close"], "func": f30_wtof_143_topping_alignment_count},
    "f30_wtof_144_exhaustion_signal_density_21d": {"inputs": ["high", "low", "close"], "func": f30_wtof_144_exhaustion_signal_density_21d},
    "f30_wtof_145_full_topping_complex_indicator": {"inputs": ["high", "low", "close"], "func": f30_wtof_145_full_topping_complex_indicator},
    "f30_wtof_146_wto_bearish_cross_at_252d_high_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_146_wto_bearish_cross_at_252d_high_event},
    "f30_wtof_147_squeeze_momentum_neg_after_bb_walk": {"inputs": ["high", "low", "close"], "func": f30_wtof_147_squeeze_momentum_neg_after_bb_walk},
    "f30_wtof_148_compound_overbought_release_signal_dwell_63d": {"inputs": ["high", "low", "close"], "func": f30_wtof_148_compound_overbought_release_signal_dwell_63d},
    "f30_wtof_149_full_topping_complex_dwell_21d": {"inputs": ["high", "low", "close"], "func": f30_wtof_149_full_topping_complex_dwell_21d},
    "f30_wtof_150_wto_long_horizon_and_squeeze_long_horizon_alignment": {"inputs": ["high", "low", "close"], "func": f30_wtof_150_wto_long_horizon_and_squeeze_long_horizon_alignment},
}
