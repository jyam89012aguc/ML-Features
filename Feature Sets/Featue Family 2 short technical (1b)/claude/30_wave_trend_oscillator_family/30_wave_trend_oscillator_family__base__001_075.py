"""wave_trend_oscillator_family base features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__076_150.py. Family theme:
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

def _wto(high, low, close, n1=10, n2=21):
    """LazyBear Wave Trend Oscillator. Returns (WT1, WT2)."""
    ap = (high + low + close) / 3.0
    esa = _ema(ap, n1)
    d = _ema((ap - esa).abs(), n1)
    ci = _safe_div(ap - esa, 0.015 * d)
    tci = _ema(ci, n2)
    wt1 = tci
    wt2 = wt1.rolling(4, min_periods=2).mean()
    return wt1, wt2


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
    """LazyBear squeeze-ON indicator: BB inside KC."""
    _, bbu, bbl = _bb(close, n=n, mult=mult_bb)
    _, kcu, kcl = _kc(high, low, close, n=n, mult=mult_kc)
    on = (bbl > kcl) & (bbu < kcu)
    return on.astype(float).where(bbu.notna() & kcu.notna(), np.nan)


def _squeeze_momentum(high, low, close, n=20):
    """LazyBear squeeze momentum value: LinReg slope of (close - mid-of-channels) over n."""
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    sma_c = close.rolling(n, min_periods=max(n // 3, 2)).mean()
    val = close - ((hh + ll) / 2.0 + sma_c) / 2.0
    # LazyBear uses LinReg as the smoother; we use the rolling regression value-at-endpoint:
    # val_lr[t] = a + b*(n-1) where (a,b) = LR(val[t-n+1..t], x=0..n-1).
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
# Bucket A — WTO levels & smoothings (001-025)
# ============================================================

def f30_wtof_001_wto_wt1_default(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """LazyBear WT1 (n1=10, n2=21) — classic Wave Trend fast line."""
    wt1, _ = _wto(high, low, close, 10, 21)
    return wt1


def f30_wtof_002_wto_wt2_default(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """LazyBear WT2 (4-bar SMA of WT1) — classic Wave Trend signal line."""
    _, wt2 = _wto(high, low, close, 10, 21)
    return wt2


def f30_wtof_003_wto_wt1_minus_wt2_default(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """WT1 − WT2: signed Wave-Trend histogram (positive when fast above signal)."""
    wt1, wt2 = _wto(high, low, close, 10, 21)
    return wt1 - wt2


def f30_wtof_004_wto_wt1_short_horizon_5_10(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Short-horizon WT1 (n1=5, n2=10) — weekly-cycle Wave-Trend reading."""
    wt1, _ = _wto(high, low, close, 5, 10)
    return wt1


def f30_wtof_005_wto_wt1_long_horizon_20_50(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Long-horizon WT1 (n1=20, n2=50) — multi-month Wave-Trend reading."""
    wt1, _ = _wto(high, low, close, 20, 50)
    return wt1


def f30_wtof_006_wto_wt1_distance_from_zero(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Absolute distance of WT1 from neutral zero — magnitude of directional bias."""
    wt1, _ = _wto(high, low, close, 10, 21)
    return wt1.abs()


def f30_wtof_007_wto_wt1_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of WT1(10,21) in trailing 252d distribution — anomalous WT level."""
    wt1, _ = _wto(high, low, close, 10, 21)
    return _rolling_zscore(wt1, YDAYS, min_periods=QDAYS)


def f30_wtof_008_wto_wt1_percentile_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of WT1 in trailing 252d — where current reading sits in distribution."""
    wt1, _ = _wto(high, low, close, 10, 21)
    return wt1.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f30_wtof_009_wto_wt1_amplitude_swing_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63d max − min of WT1 — oscillator amplitude over the quarter."""
    wt1, _ = _wto(high, low, close, 10, 21)
    return wt1.rolling(QDAYS, min_periods=MDAYS).max() - wt1.rolling(QDAYS, min_periods=MDAYS).min()


def f30_wtof_010_wto_wt1_distance_from_63d_max(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """WT1 minus its 63d max — exhaustion distance from quarterly oscillator peak."""
    wt1, _ = _wto(high, low, close, 10, 21)
    return wt1 - wt1.rolling(QDAYS, min_periods=MDAYS).max()


def f30_wtof_011_wto_wt1_distance_from_63d_min(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """WT1 minus its 63d min — recovery distance from quarterly oscillator trough."""
    wt1, _ = _wto(high, low, close, 10, 21)
    return wt1 - wt1.rolling(QDAYS, min_periods=MDAYS).min()


def f30_wtof_012_wto_wt1_local_max_above_60_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: WT1 prints a 5d local max while above the +60 overbought line."""
    wt1, _ = _wto(high, low, close, 10, 21)
    rmax = wt1.rolling(WDAYS, min_periods=2).max()
    cond = (wt1 >= rmax) & (wt1 >= 60.0)
    return cond.astype(float).where(wt1.notna(), np.nan)


def f30_wtof_013_wto_wt1_above_wt2_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: WT1 above signal WT2 — bullish-oscillator regime."""
    wt1, wt2 = _wto(high, low, close, 10, 21)
    return (wt1 > wt2).astype(float).where(wt1.notna() & wt2.notna(), np.nan)


def f30_wtof_014_wto_wt1_smoothed_5d_median(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5d-median-smoothed WT1 — denoised Wave-Trend reading."""
    wt1, _ = _wto(high, low, close, 10, 21)
    return wt1.rolling(WDAYS, min_periods=2).median()


def f30_wtof_015_wto_wt1_long_minus_short_spread(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Long-horizon WT1(20,50) minus short-horizon WT1(5,10) — slow-fast disagreement."""
    wt1_long, _ = _wto(high, low, close, 20, 50)
    wt1_short, _ = _wto(high, low, close, 5, 10)
    return wt1_long - wt1_short


def f30_wtof_016_wto_wt2_zscore_504d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of WT2 over 504d — anomalous signal-line level."""
    _, wt2 = _wto(high, low, close, 10, 21)
    return _rolling_zscore(wt2, DDAYS_2Y, min_periods=YDAYS)


def f30_wtof_017_wto_wt1_minus_wt2_percentile_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of (WT1 − WT2) in 252d — extremity of oscillator histogram."""
    wt1, wt2 = _wto(high, low, close, 10, 21)
    return (wt1 - wt2).rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f30_wtof_018_wto_wt1_short_horizon_distance_from_zero(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Short-horizon WT1(5,10) absolute deviation from zero — weekly directional magnitude."""
    wt1, _ = _wto(high, low, close, 5, 10)
    return wt1.abs()


def f30_wtof_019_wto_wt1_long_horizon_distance_from_zero(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Long-horizon WT1(20,50) absolute deviation from zero — multi-month directional magnitude."""
    wt1, _ = _wto(high, low, close, 20, 50)
    return wt1.abs()


def f30_wtof_020_wto_wt1_5d_slope(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5d linear-regression slope of WT1 — short-horizon Wave-Trend velocity."""
    wt1, _ = _wto(high, low, close, 10, 21)
    return _rolling_slope(wt1, WDAYS, min_periods=3)


def f30_wtof_021_wto_wt1_21d_slope(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21d linear-regression slope of WT1 — monthly Wave-Trend trend velocity."""
    wt1, _ = _wto(high, low, close, 10, 21)
    return _rolling_slope(wt1, MDAYS, min_periods=5)


def f30_wtof_022_wto_wt1_amplitude_252d_log(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log of 252d WT1 amplitude — annual oscillator amplitude on log scale."""
    wt1, _ = _wto(high, low, close, 10, 21)
    amp = wt1.rolling(YDAYS, min_periods=QDAYS).max() - wt1.rolling(YDAYS, min_periods=QDAYS).min()
    return _safe_log(amp + 1e-6)


def f30_wtof_023_wto_wt1_above_zero_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: WT1 above zero — bullish oscillator regime (above midline)."""
    wt1, _ = _wto(high, low, close, 10, 21)
    return (wt1 > 0.0).astype(float).where(wt1.notna(), np.nan)


def f30_wtof_024_wto_wt1_smoothed_long_horizon_21d_mean(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21d-mean-smoothed WT1 — monthly Wave-Trend trend level."""
    wt1, _ = _wto(high, low, close, 10, 21)
    return wt1.rolling(MDAYS, min_periods=WDAYS).mean()


def f30_wtof_025_wto_wt1_distance_from_252d_max(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """WT1 minus its 252d max — annual oscillator-peak exhaustion distance."""
    wt1, _ = _wto(high, low, close, 10, 21)
    return wt1 - wt1.rolling(YDAYS, min_periods=QDAYS).max()


# ============================================================
# Bucket B — WTO crosses & overbought zones (026-050)
# ============================================================

def f30_wtof_026_wto_bullish_cross_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: WT1 crosses above WT2 today — bullish Wave-Trend cross."""
    wt1, wt2 = _wto(high, low, close, 10, 21)
    cond = (wt1 > wt2) & (wt1.shift(1) <= wt2.shift(1))
    return cond.astype(float).where(wt1.notna() & wt2.shift(1).notna(), np.nan)


def f30_wtof_027_wto_bearish_cross_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: WT1 crosses below WT2 today — bearish Wave-Trend cross."""
    wt1, wt2 = _wto(high, low, close, 10, 21)
    cond = (wt1 < wt2) & (wt1.shift(1) >= wt2.shift(1))
    return cond.astype(float).where(wt1.notna() & wt2.shift(1).notna(), np.nan)


def f30_wtof_028_wto_overbought_above_60_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: WT1 above the +60 overbought line."""
    wt1, _ = _wto(high, low, close, 10, 21)
    return (wt1 >= 60.0).astype(float).where(wt1.notna(), np.nan)


def f30_wtof_029_wto_extreme_overbought_above_80_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: WT1 above the +80 extreme-overbought line."""
    wt1, _ = _wto(high, low, close, 10, 21)
    return (wt1 >= 80.0).astype(float).where(wt1.notna(), np.nan)


def f30_wtof_030_wto_oversold_below_minus60_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: WT1 below the −60 oversold line (rare during topping)."""
    wt1, _ = _wto(high, low, close, 10, 21)
    return (wt1 <= -60.0).astype(float).where(wt1.notna(), np.nan)


def f30_wtof_031_wto_dwell_above_60_in_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars in trailing 21d with WT1 ≥ 60 — sustained overbought dwell."""
    wt1, _ = _wto(high, low, close, 10, 21)
    above = (wt1 >= 60.0).astype(float)
    return above.rolling(MDAYS, min_periods=WDAYS).sum()


def f30_wtof_032_wto_dwell_above_60_in_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars in trailing 63d with WT1 ≥ 60 — quarterly sustained-overbought dwell."""
    wt1, _ = _wto(high, low, close, 10, 21)
    above = (wt1 >= 60.0).astype(float)
    return above.rolling(QDAYS, min_periods=MDAYS).sum()


def f30_wtof_033_wto_dwell_above_80_in_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars in trailing 21d with WT1 ≥ 80 — extreme-overbought monthly dwell."""
    wt1, _ = _wto(high, low, close, 10, 21)
    above = (wt1 >= 80.0).astype(float)
    return above.rolling(MDAYS, min_periods=WDAYS).sum()


def f30_wtof_034_wto_first_decline_from_above_60_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: WT1 was ≥ 60 yesterday and is falling today (first-decline-from-overbought)."""
    wt1, _ = _wto(high, low, close, 10, 21)
    cond = (wt1.shift(1) >= 60.0) & (wt1 < wt1.shift(1))
    return cond.astype(float).where(wt1.notna() & wt1.shift(1).notna(), np.nan)


def f30_wtof_035_wto_bearish_cross_above_60_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: bearish WT1/WT2 cross occurring while WT1 ≥ 60 — classic LazyBear top."""
    wt1, wt2 = _wto(high, low, close, 10, 21)
    cross = (wt1 < wt2) & (wt1.shift(1) >= wt2.shift(1))
    cond = cross & (wt1 >= 60.0)
    return cond.astype(float).where(wt1.notna() & wt2.shift(1).notna(), np.nan)


def f30_wtof_036_wto_bearish_cross_above_80_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: bearish WT1/WT2 cross while WT1 ≥ 80 — extreme-overbought topping."""
    wt1, wt2 = _wto(high, low, close, 10, 21)
    cross = (wt1 < wt2) & (wt1.shift(1) >= wt2.shift(1))
    cond = cross & (wt1 >= 80.0)
    return cond.astype(float).where(wt1.notna() & wt2.shift(1).notna(), np.nan)


def f30_wtof_037_wto_signal_curvature_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Discrete 2nd-difference of WT2 — signal-line curvature (negative = topping)."""
    _, wt2 = _wto(high, low, close, 10, 21)
    return wt2.diff().diff().rolling(WDAYS, min_periods=2).mean()


def f30_wtof_038_wto_double_top_above_60_in_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: WT1 prints two distinct peaks both ≥ 60 inside trailing 21d (double-top in OB)."""
    wt1, _ = _wto(high, low, close, 10, 21)
    is_local_max = (wt1.shift(1) > wt1) & (wt1.shift(1) > wt1.shift(2)) & (wt1.shift(1) >= 60.0)
    peaks = is_local_max.astype(float)
    cnt = peaks.rolling(MDAYS, min_periods=WDAYS).sum()
    return (cnt >= 2).astype(float).where(wt1.notna(), np.nan)


def f30_wtof_039_wto_post_bearish_cross_5d_decline(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Magnitude: WT1(t) − WT1(t−5) given bearish-cross was triggered within the prior 5 bars."""
    wt1, wt2 = _wto(high, low, close, 10, 21)
    bear = ((wt1 < wt2) & (wt1.shift(1) >= wt2.shift(1))).astype(float)
    trig = bear.rolling(WDAYS, min_periods=2).max()
    diff = wt1 - wt1.shift(WDAYS)
    return diff.where(trig > 0, np.nan)


def f30_wtof_040_wto_bars_since_last_above_60(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since WT1 was last ≥ 60 — staleness of last overbought reading."""
    wt1, _ = _wto(high, low, close, 10, 21)
    above = (wt1 >= 60.0)
    arr = above.values
    n = len(arr)
    out = np.full(n, np.nan, dtype=float)
    last = -1
    for i in range(n):
        v = wt1.iat[i]
        if pd.isna(v):
            out[i] = np.nan
            continue
        if arr[i]:
            last = i
        out[i] = float(i - last) if last >= 0 else np.nan
    return pd.Series(out, index=wt1.index)


def f30_wtof_041_wto_bullish_cross_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bullish WT1/WT2 crosses in trailing 63d — oscillator-cycle frequency."""
    wt1, wt2 = _wto(high, low, close, 10, 21)
    cross = ((wt1 > wt2) & (wt1.shift(1) <= wt2.shift(1))).astype(float)
    return cross.rolling(QDAYS, min_periods=MDAYS).sum()


def f30_wtof_042_wto_bearish_cross_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bearish WT1/WT2 crosses in trailing 63d — oscillator-cycle frequency."""
    wt1, wt2 = _wto(high, low, close, 10, 21)
    cross = ((wt1 < wt2) & (wt1.shift(1) >= wt2.shift(1))).astype(float)
    return cross.rolling(QDAYS, min_periods=MDAYS).sum()


def f30_wtof_043_wto_consecutive_decline_streak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Consecutive-bar streak of WT1 falling — relentless oscillator-down momentum."""
    wt1, _ = _wto(high, low, close, 10, 21)
    fall = (wt1.diff() < 0).astype(float).values
    n = len(fall)
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    for i in range(n):
        if pd.isna(wt1.iat[i]):
            streak = 0
            out[i] = np.nan
        else:
            streak = streak + 1 if fall[i] > 0 else 0
            out[i] = float(streak)
    return pd.Series(out, index=wt1.index)


def f30_wtof_044_wto_wt1_falling_from_above_80_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: WT1 was ≥ 80 within last 5 bars and now falling — extreme topping."""
    wt1, _ = _wto(high, low, close, 10, 21)
    hot = (wt1.rolling(WDAYS, min_periods=2).max() >= 80.0)
    cond = hot.shift(1).fillna(False) & (wt1.diff() < 0)
    return cond.astype(float).where(wt1.notna(), np.nan)


def f30_wtof_045_wto_wt1_minus_wt2_distance_from_max(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(WT1−WT2) minus its 63d max — histogram exhaustion from quarterly high."""
    wt1, wt2 = _wto(high, low, close, 10, 21)
    h = wt1 - wt2
    return h - h.rolling(QDAYS, min_periods=MDAYS).max()


def f30_wtof_046_wto_overbought_exit_event_below_60(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: WT1 crosses down through +60 (overbought exit)."""
    wt1, _ = _wto(high, low, close, 10, 21)
    cond = (wt1 < 60.0) & (wt1.shift(1) >= 60.0)
    return cond.astype(float).where(wt1.notna() & wt1.shift(1).notna(), np.nan)


def f30_wtof_047_wto_extreme_exit_event_below_80(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: WT1 crosses down through +80 (extreme-overbought exit)."""
    wt1, _ = _wto(high, low, close, 10, 21)
    cond = (wt1 < 80.0) & (wt1.shift(1) >= 80.0)
    return cond.astype(float).where(wt1.notna() & wt1.shift(1).notna(), np.nan)


def f30_wtof_048_wto_bearish_cross_short_horizon_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: bearish WT1/WT2 cross on short-horizon WTO(5,10) — fast top signal."""
    wt1, wt2 = _wto(high, low, close, 5, 10)
    cond = (wt1 < wt2) & (wt1.shift(1) >= wt2.shift(1))
    return cond.astype(float).where(wt1.notna() & wt2.shift(1).notna(), np.nan)


def f30_wtof_049_wto_bearish_cross_long_horizon_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: bearish WT1/WT2 cross on long-horizon WTO(20,50) — slow-cycle top signal."""
    wt1, wt2 = _wto(high, low, close, 20, 50)
    cond = (wt1 < wt2) & (wt1.shift(1) >= wt2.shift(1))
    return cond.astype(float).where(wt1.notna() & wt2.shift(1).notna(), np.nan)


def f30_wtof_050_wto_wt1_at_252d_high_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """At bars where high == 252d max, value of WT1 — WT level right at the annual peak."""
    wt1, _ = _wto(high, low, close, 10, 21)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = (high >= rmax)
    return wt1.where(at_peak, np.nan)


# ============================================================
# Bucket C — Squeeze Momentum (051-075)
# ============================================================

def f30_wtof_051_squeeze_momentum_classic_20d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """LazyBear squeeze-momentum value (n=20) — classic momentum oscillator."""
    return _squeeze_momentum(high, low, close, n=20)


def f30_wtof_052_squeeze_momentum_sign(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sign of squeeze-momentum (20) — green/red histogram color in {−1,0,+1}."""
    mom = _squeeze_momentum(high, low, close, n=20)
    return np.sign(mom).where(mom.notna(), np.nan)


def f30_wtof_053_squeeze_momentum_velocity_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5d linear-regression slope of squeeze-momentum — bar-color rate of change."""
    mom = _squeeze_momentum(high, low, close, n=20)
    return _rolling_slope(mom, WDAYS, min_periods=3)


def f30_wtof_054_squeeze_momentum_color_change_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: momentum sign flipped today — color change in LazyBear histogram."""
    mom = _squeeze_momentum(high, low, close, n=20)
    s = np.sign(mom)
    cond = (s != s.shift(1)) & mom.notna() & mom.shift(1).notna()
    return cond.astype(float).where(mom.notna(), np.nan)


def f30_wtof_055_squeeze_momentum_above_zero_dwell_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars in trailing 21d with momentum > 0 — positive-momentum dwell."""
    mom = _squeeze_momentum(high, low, close, n=20)
    return (mom > 0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f30_wtof_056_squeeze_momentum_below_zero_dwell_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars in trailing 21d with momentum < 0 — negative-momentum dwell."""
    mom = _squeeze_momentum(high, low, close, n=20)
    return (mom < 0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f30_wtof_057_squeeze_momentum_local_max_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Momentum value relative to 63d trailing max (momentum − max ≤ 0)."""
    mom = _squeeze_momentum(high, low, close, n=20)
    return mom - mom.rolling(QDAYS, min_periods=MDAYS).max()


def f30_wtof_058_squeeze_momentum_falling_from_positive_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: momentum > 0 yesterday and falling today — first-decline-from-positive event."""
    mom = _squeeze_momentum(high, low, close, n=20)
    cond = (mom.shift(1) > 0) & (mom < mom.shift(1))
    return cond.astype(float).where(mom.notna() & mom.shift(1).notna(), np.nan)


def f30_wtof_059_squeeze_momentum_amplitude_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63d max − min of momentum — oscillator amplitude over the quarter."""
    mom = _squeeze_momentum(high, low, close, n=20)
    return mom.rolling(QDAYS, min_periods=MDAYS).max() - mom.rolling(QDAYS, min_periods=MDAYS).min()


def f30_wtof_060_squeeze_momentum_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of squeeze-momentum in trailing 252d — anomalous-momentum reading."""
    mom = _squeeze_momentum(high, low, close, n=20)
    return _rolling_zscore(mom, YDAYS, min_periods=QDAYS)


def f30_wtof_061_squeeze_momentum_smoothed_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5d-mean-smoothed squeeze-momentum — denoised momentum oscillator."""
    mom = _squeeze_momentum(high, low, close, n=20)
    return mom.rolling(WDAYS, min_periods=2).mean()


def f30_wtof_062_squeeze_momentum_percentile_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of squeeze-momentum in trailing 252d — where current reading sits."""
    mom = _squeeze_momentum(high, low, close, n=20)
    return mom.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f30_wtof_063_squeeze_momentum_distance_from_252d_max(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Momentum minus its 252d max — annual momentum-peak exhaustion distance."""
    mom = _squeeze_momentum(high, low, close, n=20)
    return mom - mom.rolling(YDAYS, min_periods=QDAYS).max()


def f30_wtof_064_squeeze_momentum_zero_crossings_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of momentum sign flips in trailing 63d — oscillator-chop frequency."""
    mom = _squeeze_momentum(high, low, close, n=20)
    s = np.sign(mom)
    flip = (s != s.shift(1)) & mom.notna() & mom.shift(1).notna()
    return flip.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f30_wtof_065_squeeze_momentum_short_horizon_10d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Short-horizon squeeze-momentum (n=10) — fast cycle reading."""
    return _squeeze_momentum(high, low, close, n=10)


def f30_wtof_066_squeeze_momentum_long_horizon_50d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Long-horizon squeeze-momentum (n=50) — slow cycle reading."""
    return _squeeze_momentum(high, low, close, n=50)


def f30_wtof_067_squeeze_momentum_short_minus_long_spread(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Short(10) − Long(50) momentum spread — fast-cycle vs slow-cycle disagreement."""
    return _squeeze_momentum(high, low, close, n=10) - _squeeze_momentum(high, low, close, n=50)


def f30_wtof_068_squeeze_momentum_consecutive_decline_streak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Consecutive-bar streak of momentum falling — momentum-decay run."""
    mom = _squeeze_momentum(high, low, close, n=20)
    fall = (mom.diff() < 0).astype(float).values
    n = len(fall)
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    for i in range(n):
        if pd.isna(mom.iat[i]):
            streak = 0
            out[i] = np.nan
        else:
            streak = streak + 1 if fall[i] > 0 else 0
            out[i] = float(streak)
    return pd.Series(out, index=mom.index)


def f30_wtof_069_squeeze_momentum_persistence_negative_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: momentum has been < 0 every bar in trailing 5d — fresh negative regime."""
    mom = _squeeze_momentum(high, low, close, n=20)
    neg = (mom < 0).astype(float)
    s = neg.rolling(WDAYS, min_periods=WDAYS).sum()
    return (s >= WDAYS).astype(float).where(mom.notna(), np.nan)


def f30_wtof_070_squeeze_momentum_long_horizon_color_change_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: long-horizon (n=50) squeeze-momentum flipped sign — slow-cycle regime change."""
    mom = _squeeze_momentum(high, low, close, n=50)
    s = np.sign(mom)
    cond = (s != s.shift(1)) & mom.notna() & mom.shift(1).notna()
    return cond.astype(float).where(mom.notna(), np.nan)


def f30_wtof_071_squeeze_momentum_at_252d_high_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """At bars where high == 252d max, value of squeeze-momentum — momentum at the peak."""
    mom = _squeeze_momentum(high, low, close, n=20)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = (high >= rmax)
    return mom.where(at_peak, np.nan)


def f30_wtof_072_squeeze_momentum_negative_after_positive_streak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Event: momentum > 0 for ≥ 10 of trailing 21d AND today < 0 — fresh down-regime."""
    mom = _squeeze_momentum(high, low, close, n=20)
    pos = (mom > 0).astype(float)
    prior_pos = pos.rolling(MDAYS, min_periods=WDAYS).sum().shift(1)
    cond = (prior_pos >= 10) & (mom < 0)
    return cond.astype(float).where(mom.notna() & prior_pos.notna(), np.nan)


def f30_wtof_073_squeeze_momentum_5d_change(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5d change in squeeze-momentum — weekly momentum delta."""
    mom = _squeeze_momentum(high, low, close, n=20)
    return mom - mom.shift(WDAYS)


def f30_wtof_074_squeeze_momentum_abs_value(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Absolute value of squeeze-momentum — magnitude regardless of direction."""
    mom = _squeeze_momentum(high, low, close, n=20)
    return mom.abs()


def f30_wtof_075_squeeze_momentum_short_horizon_sign(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sign of short-horizon (n=10) squeeze-momentum — fast-cycle direction in {−1,0,+1}."""
    mom = _squeeze_momentum(high, low, close, n=10)
    return np.sign(mom).where(mom.notna(), np.nan)


# ============================================================
#                         REGISTRY 001-075
# ============================================================

WAVE_TREND_OSCILLATOR_FAMILY_BASE_REGISTRY_001_075 = {
    "f30_wtof_001_wto_wt1_default": {"inputs": ["high", "low", "close"], "func": f30_wtof_001_wto_wt1_default},
    "f30_wtof_002_wto_wt2_default": {"inputs": ["high", "low", "close"], "func": f30_wtof_002_wto_wt2_default},
    "f30_wtof_003_wto_wt1_minus_wt2_default": {"inputs": ["high", "low", "close"], "func": f30_wtof_003_wto_wt1_minus_wt2_default},
    "f30_wtof_004_wto_wt1_short_horizon_5_10": {"inputs": ["high", "low", "close"], "func": f30_wtof_004_wto_wt1_short_horizon_5_10},
    "f30_wtof_005_wto_wt1_long_horizon_20_50": {"inputs": ["high", "low", "close"], "func": f30_wtof_005_wto_wt1_long_horizon_20_50},
    "f30_wtof_006_wto_wt1_distance_from_zero": {"inputs": ["high", "low", "close"], "func": f30_wtof_006_wto_wt1_distance_from_zero},
    "f30_wtof_007_wto_wt1_zscore_252d": {"inputs": ["high", "low", "close"], "func": f30_wtof_007_wto_wt1_zscore_252d},
    "f30_wtof_008_wto_wt1_percentile_rank_252d": {"inputs": ["high", "low", "close"], "func": f30_wtof_008_wto_wt1_percentile_rank_252d},
    "f30_wtof_009_wto_wt1_amplitude_swing_63d": {"inputs": ["high", "low", "close"], "func": f30_wtof_009_wto_wt1_amplitude_swing_63d},
    "f30_wtof_010_wto_wt1_distance_from_63d_max": {"inputs": ["high", "low", "close"], "func": f30_wtof_010_wto_wt1_distance_from_63d_max},
    "f30_wtof_011_wto_wt1_distance_from_63d_min": {"inputs": ["high", "low", "close"], "func": f30_wtof_011_wto_wt1_distance_from_63d_min},
    "f30_wtof_012_wto_wt1_local_max_above_60_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_012_wto_wt1_local_max_above_60_event},
    "f30_wtof_013_wto_wt1_above_wt2_indicator": {"inputs": ["high", "low", "close"], "func": f30_wtof_013_wto_wt1_above_wt2_indicator},
    "f30_wtof_014_wto_wt1_smoothed_5d_median": {"inputs": ["high", "low", "close"], "func": f30_wtof_014_wto_wt1_smoothed_5d_median},
    "f30_wtof_015_wto_wt1_long_minus_short_spread": {"inputs": ["high", "low", "close"], "func": f30_wtof_015_wto_wt1_long_minus_short_spread},
    "f30_wtof_016_wto_wt2_zscore_504d": {"inputs": ["high", "low", "close"], "func": f30_wtof_016_wto_wt2_zscore_504d},
    "f30_wtof_017_wto_wt1_minus_wt2_percentile_252d": {"inputs": ["high", "low", "close"], "func": f30_wtof_017_wto_wt1_minus_wt2_percentile_252d},
    "f30_wtof_018_wto_wt1_short_horizon_distance_from_zero": {"inputs": ["high", "low", "close"], "func": f30_wtof_018_wto_wt1_short_horizon_distance_from_zero},
    "f30_wtof_019_wto_wt1_long_horizon_distance_from_zero": {"inputs": ["high", "low", "close"], "func": f30_wtof_019_wto_wt1_long_horizon_distance_from_zero},
    "f30_wtof_020_wto_wt1_5d_slope": {"inputs": ["high", "low", "close"], "func": f30_wtof_020_wto_wt1_5d_slope},
    "f30_wtof_021_wto_wt1_21d_slope": {"inputs": ["high", "low", "close"], "func": f30_wtof_021_wto_wt1_21d_slope},
    "f30_wtof_022_wto_wt1_amplitude_252d_log": {"inputs": ["high", "low", "close"], "func": f30_wtof_022_wto_wt1_amplitude_252d_log},
    "f30_wtof_023_wto_wt1_above_zero_indicator": {"inputs": ["high", "low", "close"], "func": f30_wtof_023_wto_wt1_above_zero_indicator},
    "f30_wtof_024_wto_wt1_smoothed_long_horizon_21d_mean": {"inputs": ["high", "low", "close"], "func": f30_wtof_024_wto_wt1_smoothed_long_horizon_21d_mean},
    "f30_wtof_025_wto_wt1_distance_from_252d_max": {"inputs": ["high", "low", "close"], "func": f30_wtof_025_wto_wt1_distance_from_252d_max},
    "f30_wtof_026_wto_bullish_cross_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_026_wto_bullish_cross_event},
    "f30_wtof_027_wto_bearish_cross_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_027_wto_bearish_cross_event},
    "f30_wtof_028_wto_overbought_above_60_indicator": {"inputs": ["high", "low", "close"], "func": f30_wtof_028_wto_overbought_above_60_indicator},
    "f30_wtof_029_wto_extreme_overbought_above_80_indicator": {"inputs": ["high", "low", "close"], "func": f30_wtof_029_wto_extreme_overbought_above_80_indicator},
    "f30_wtof_030_wto_oversold_below_minus60_indicator": {"inputs": ["high", "low", "close"], "func": f30_wtof_030_wto_oversold_below_minus60_indicator},
    "f30_wtof_031_wto_dwell_above_60_in_21d": {"inputs": ["high", "low", "close"], "func": f30_wtof_031_wto_dwell_above_60_in_21d},
    "f30_wtof_032_wto_dwell_above_60_in_63d": {"inputs": ["high", "low", "close"], "func": f30_wtof_032_wto_dwell_above_60_in_63d},
    "f30_wtof_033_wto_dwell_above_80_in_21d": {"inputs": ["high", "low", "close"], "func": f30_wtof_033_wto_dwell_above_80_in_21d},
    "f30_wtof_034_wto_first_decline_from_above_60_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_034_wto_first_decline_from_above_60_event},
    "f30_wtof_035_wto_bearish_cross_above_60_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_035_wto_bearish_cross_above_60_event},
    "f30_wtof_036_wto_bearish_cross_above_80_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_036_wto_bearish_cross_above_80_event},
    "f30_wtof_037_wto_signal_curvature_5d": {"inputs": ["high", "low", "close"], "func": f30_wtof_037_wto_signal_curvature_5d},
    "f30_wtof_038_wto_double_top_above_60_in_21d": {"inputs": ["high", "low", "close"], "func": f30_wtof_038_wto_double_top_above_60_in_21d},
    "f30_wtof_039_wto_post_bearish_cross_5d_decline": {"inputs": ["high", "low", "close"], "func": f30_wtof_039_wto_post_bearish_cross_5d_decline},
    "f30_wtof_040_wto_bars_since_last_above_60": {"inputs": ["high", "low", "close"], "func": f30_wtof_040_wto_bars_since_last_above_60},
    "f30_wtof_041_wto_bullish_cross_count_63d": {"inputs": ["high", "low", "close"], "func": f30_wtof_041_wto_bullish_cross_count_63d},
    "f30_wtof_042_wto_bearish_cross_count_63d": {"inputs": ["high", "low", "close"], "func": f30_wtof_042_wto_bearish_cross_count_63d},
    "f30_wtof_043_wto_consecutive_decline_streak": {"inputs": ["high", "low", "close"], "func": f30_wtof_043_wto_consecutive_decline_streak},
    "f30_wtof_044_wto_wt1_falling_from_above_80_indicator": {"inputs": ["high", "low", "close"], "func": f30_wtof_044_wto_wt1_falling_from_above_80_indicator},
    "f30_wtof_045_wto_wt1_minus_wt2_distance_from_max": {"inputs": ["high", "low", "close"], "func": f30_wtof_045_wto_wt1_minus_wt2_distance_from_max},
    "f30_wtof_046_wto_overbought_exit_event_below_60": {"inputs": ["high", "low", "close"], "func": f30_wtof_046_wto_overbought_exit_event_below_60},
    "f30_wtof_047_wto_extreme_exit_event_below_80": {"inputs": ["high", "low", "close"], "func": f30_wtof_047_wto_extreme_exit_event_below_80},
    "f30_wtof_048_wto_bearish_cross_short_horizon_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_048_wto_bearish_cross_short_horizon_event},
    "f30_wtof_049_wto_bearish_cross_long_horizon_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_049_wto_bearish_cross_long_horizon_event},
    "f30_wtof_050_wto_wt1_at_252d_high_indicator": {"inputs": ["high", "low", "close"], "func": f30_wtof_050_wto_wt1_at_252d_high_indicator},
    "f30_wtof_051_squeeze_momentum_classic_20d": {"inputs": ["high", "low", "close"], "func": f30_wtof_051_squeeze_momentum_classic_20d},
    "f30_wtof_052_squeeze_momentum_sign": {"inputs": ["high", "low", "close"], "func": f30_wtof_052_squeeze_momentum_sign},
    "f30_wtof_053_squeeze_momentum_velocity_5d": {"inputs": ["high", "low", "close"], "func": f30_wtof_053_squeeze_momentum_velocity_5d},
    "f30_wtof_054_squeeze_momentum_color_change_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_054_squeeze_momentum_color_change_event},
    "f30_wtof_055_squeeze_momentum_above_zero_dwell_21d": {"inputs": ["high", "low", "close"], "func": f30_wtof_055_squeeze_momentum_above_zero_dwell_21d},
    "f30_wtof_056_squeeze_momentum_below_zero_dwell_21d": {"inputs": ["high", "low", "close"], "func": f30_wtof_056_squeeze_momentum_below_zero_dwell_21d},
    "f30_wtof_057_squeeze_momentum_local_max_63d": {"inputs": ["high", "low", "close"], "func": f30_wtof_057_squeeze_momentum_local_max_63d},
    "f30_wtof_058_squeeze_momentum_falling_from_positive_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_058_squeeze_momentum_falling_from_positive_event},
    "f30_wtof_059_squeeze_momentum_amplitude_63d": {"inputs": ["high", "low", "close"], "func": f30_wtof_059_squeeze_momentum_amplitude_63d},
    "f30_wtof_060_squeeze_momentum_zscore_252d": {"inputs": ["high", "low", "close"], "func": f30_wtof_060_squeeze_momentum_zscore_252d},
    "f30_wtof_061_squeeze_momentum_smoothed_5d": {"inputs": ["high", "low", "close"], "func": f30_wtof_061_squeeze_momentum_smoothed_5d},
    "f30_wtof_062_squeeze_momentum_percentile_252d": {"inputs": ["high", "low", "close"], "func": f30_wtof_062_squeeze_momentum_percentile_252d},
    "f30_wtof_063_squeeze_momentum_distance_from_252d_max": {"inputs": ["high", "low", "close"], "func": f30_wtof_063_squeeze_momentum_distance_from_252d_max},
    "f30_wtof_064_squeeze_momentum_zero_crossings_63d": {"inputs": ["high", "low", "close"], "func": f30_wtof_064_squeeze_momentum_zero_crossings_63d},
    "f30_wtof_065_squeeze_momentum_short_horizon_10d": {"inputs": ["high", "low", "close"], "func": f30_wtof_065_squeeze_momentum_short_horizon_10d},
    "f30_wtof_066_squeeze_momentum_long_horizon_50d": {"inputs": ["high", "low", "close"], "func": f30_wtof_066_squeeze_momentum_long_horizon_50d},
    "f30_wtof_067_squeeze_momentum_short_minus_long_spread": {"inputs": ["high", "low", "close"], "func": f30_wtof_067_squeeze_momentum_short_minus_long_spread},
    "f30_wtof_068_squeeze_momentum_consecutive_decline_streak": {"inputs": ["high", "low", "close"], "func": f30_wtof_068_squeeze_momentum_consecutive_decline_streak},
    "f30_wtof_069_squeeze_momentum_persistence_negative_5d": {"inputs": ["high", "low", "close"], "func": f30_wtof_069_squeeze_momentum_persistence_negative_5d},
    "f30_wtof_070_squeeze_momentum_long_horizon_color_change_event": {"inputs": ["high", "low", "close"], "func": f30_wtof_070_squeeze_momentum_long_horizon_color_change_event},
    "f30_wtof_071_squeeze_momentum_at_252d_high_indicator": {"inputs": ["high", "low", "close"], "func": f30_wtof_071_squeeze_momentum_at_252d_high_indicator},
    "f30_wtof_072_squeeze_momentum_negative_after_positive_streak": {"inputs": ["high", "low", "close"], "func": f30_wtof_072_squeeze_momentum_negative_after_positive_streak},
    "f30_wtof_073_squeeze_momentum_5d_change": {"inputs": ["high", "low", "close"], "func": f30_wtof_073_squeeze_momentum_5d_change},
    "f30_wtof_074_squeeze_momentum_abs_value": {"inputs": ["high", "low", "close"], "func": f30_wtof_074_squeeze_momentum_abs_value},
    "f30_wtof_075_squeeze_momentum_short_horizon_sign": {"inputs": ["high", "low", "close"], "func": f30_wtof_075_squeeze_momentum_short_horizon_sign},
}
