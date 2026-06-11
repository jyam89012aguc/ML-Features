"""
30_relative_strength — Extended Features 001-075
Domain: price vs its own moving averages — KAMA (Kaufman Adaptive MA),
        VWMA (volume-weighted MA), WMA (standalone), ZLEMA (zero-lag EMA),
        ALMA (Arnaud Legoux MA), T3 (Tillson Triple MA), FRAMA
        (Fractal Adaptive MA); MA envelope / percent-band position;
        days-below-MA streak and time-since-cross; multi-MA confluence /
        agreement scores; rate-of-change and ROC-acceleration variants
        applied to novel MA constructs.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_EPS     = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _sma(close: pd.Series, w: int) -> pd.Series:
    return _rolling_mean(close, w)


def _ema(close: pd.Series, span: int) -> pd.Series:
    return _ewm_mean(close, span)


# ── Novel MA Helpers (all vectorised, no apply on rolling) ────────────────────

def _wma(close: pd.Series, w: int) -> pd.Series:
    """Linearly-weighted moving average (vectorised convolution approach)."""
    weights = np.arange(1, w + 1, dtype=float)
    w_sum = weights.sum()
    arr = close.to_numpy(dtype=float)
    n = len(arr)
    out = np.full(n, np.nan)
    mp = max(1, w // 2)
    for i in range(n):
        start = max(0, i - w + 1)
        chunk = arr[start:i + 1]
        if len(chunk) < mp:
            continue
        wt = np.arange(1, len(chunk) + 1, dtype=float)
        out[i] = np.dot(chunk, wt) / wt.sum()
    return pd.Series(out, index=close.index)


def _kama(close: pd.Series, n: int = 10, fast: int = 2, slow: int = 30) -> pd.Series:
    """Kaufman Adaptive Moving Average (KAMA).
    Efficiency Ratio = abs(price_change_n) / sum(abs(daily_changes_n).
    Smoothing constant = (ER*(fc-sc) + sc)^2 where fc=2/(fast+1), sc=2/(slow+1).
    """
    arr = close.to_numpy(dtype=float)
    out = np.full(len(arr), np.nan)
    fc = 2.0 / (fast + 1)
    sc = 2.0 / (slow + 1)
    # seed first valid KAMA value
    seed_idx = n - 1
    if seed_idx >= len(arr):
        return pd.Series(out, index=close.index)
    out[seed_idx] = arr[seed_idx]
    for i in range(seed_idx + 1, len(arr)):
        direction = abs(arr[i] - arr[i - n])
        volatility = np.sum(np.abs(np.diff(arr[max(0, i - n + 1):i + 1])))
        if volatility < _EPS:
            er = 0.0
        else:
            er = direction / volatility
        sc_i = (er * (fc - sc) + sc) ** 2
        out[i] = out[i - 1] + sc_i * (arr[i] - out[i - 1])
    return pd.Series(out, index=close.index)


def _vwma(close: pd.Series, volume: pd.Series, w: int) -> pd.Series:
    """Volume-weighted moving average over w periods."""
    mp = max(1, w // 2)
    pv = close * volume
    sum_pv  = pv.rolling(w, min_periods=mp).sum()
    sum_vol = volume.rolling(w, min_periods=mp).sum()
    return _safe_div(sum_pv, sum_vol)


def _zlema(close: pd.Series, span: int) -> pd.Series:
    """Zero-Lag EMA: EMA applied to (close + (close - close.shift(lag)))
    where lag = (span - 1) // 2.
    """
    lag = (span - 1) // 2
    adjusted = close + (close - close.shift(lag))
    return adjusted.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _alma(close: pd.Series, w: int = 21, sigma: float = 6.0, offset: float = 0.85) -> pd.Series:
    """Arnaud Legoux Moving Average — Gaussian-weighted MA.
    Weights: w_i = exp(-((i - m)^2) / (2 * s^2)) where m = offset*(w-1), s = w/sigma.
    Pure convolution — no rolling.apply.
    """
    arr = close.to_numpy(dtype=float)
    n = len(arr)
    m = offset * (w - 1)
    s = w / sigma
    raw_weights = np.array([np.exp(-((i - m) ** 2) / (2.0 * s * s)) for i in range(w)], dtype=float)
    raw_weights /= raw_weights.sum()
    out = np.full(n, np.nan)
    mp = max(1, w // 2)
    for i in range(w - 1, n):
        chunk = arr[i - w + 1:i + 1]
        if np.sum(~np.isnan(chunk)) < mp:
            continue
        out[i] = np.nansum(chunk * raw_weights)
    return pd.Series(out, index=close.index)


def _t3(close: pd.Series, span: int = 21, v: float = 0.7) -> pd.Series:
    """Tillson T3 triple-smoothed MA.
    T3 = c1*e6 + c2*e5 + c3*e4 + c4*e3, where e1..e6 are cascaded EMAs
    and c1=-v^3, c2=3v^2+3v^3, c3=-6v^2-3v-3v^3, c4=1+3v+v^3+3v^2.
    """
    e1 = _ema(close, span)
    e2 = _ema(e1, span)
    e3 = _ema(e2, span)
    e4 = _ema(e3, span)
    e5 = _ema(e4, span)
    e6 = _ema(e5, span)
    c1 = -(v ** 3)
    c2 = 3.0 * v ** 2 + 3.0 * v ** 3
    c3 = -6.0 * v ** 2 - 3.0 * v - 3.0 * v ** 3
    c4 = 1.0 + 3.0 * v + v ** 3 + 3.0 * v ** 2
    return c1 * e6 + c2 * e5 + c3 * e4 + c4 * e3


def _frama(close: pd.Series, w: int = 16) -> pd.Series:
    """Fractal Adaptive Moving Average (simplified FRAMA).
    Fractal dimension D estimated from high/low of sub-windows.
    alpha = exp(-4.6 * (D - 1)).  Uses close only: high/low approximated from
    rolling max/min of the close within each half-window.
    """
    arr = close.to_numpy(dtype=float)
    n = len(arr)
    out = np.full(n, np.nan)
    half = w // 2
    if n <= w:
        return pd.Series(out, index=close.index)
    out[w - 1] = arr[w - 1]
    for i in range(w, n):
        full = arr[i - w:i]
        h1 = np.max(arr[i - w:i - half])
        l1 = np.min(arr[i - w:i - half])
        h2 = np.max(arr[i - half:i])
        l2 = np.min(arr[i - half:i])
        hf = np.max(full)
        lf = np.min(full)
        r1 = (h1 - l1) / half if half > 0 else 0.0
        r2 = (h2 - l2) / half if half > 0 else 0.0
        rf = (hf - lf) / w if w > 0 else 0.0
        if rf < _EPS or (r1 + r2) < _EPS:
            D = 1.0
        else:
            D = (np.log(r1 + r2) - np.log(rf)) / np.log(2.0)
            D = max(1.0, min(2.0, D))
        alpha = np.exp(-4.6 * (D - 1.0))
        alpha = max(0.01, min(1.0, alpha))
        out[i] = alpha * arr[i] + (1.0 - alpha) * out[i - 1]
    return pd.Series(out, index=close.index)


# ── Streak helper ─────────────────────────────────────────────────────────────

def _consecutive_true_streak(flag: pd.Series) -> pd.Series:
    """Rolling count of consecutive True values ending at each bar."""
    arr = flag.to_numpy(dtype=float)
    out = np.zeros(len(arr), dtype=float)
    streak = 0
    for i in range(len(arr)):
        if np.isnan(arr[i]):
            streak = 0
            out[i] = np.nan
        elif arr[i] > 0:
            streak += 1
            out[i] = float(streak)
        else:
            streak = 0
            out[i] = 0.0
    return pd.Series(out, index=flag.index)


def _bars_since_cross(above_flag: pd.Series) -> pd.Series:
    """Bars since the most recent transition in above_flag (0->1 or 1->0)."""
    arr = above_flag.to_numpy(dtype=float)
    out = np.full(len(arr), np.nan)
    last_cross = -1
    prev = np.nan
    for i in range(len(arr)):
        if np.isnan(arr[i]):
            prev = np.nan
            continue
        if not np.isnan(prev) and arr[i] != prev:
            last_cross = i
        if last_cross >= 0:
            out[i] = float(i - last_cross)
        prev = arr[i]
    return pd.Series(out, index=above_flag.index)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): KAMA — price distance, depth, slope ---

def rst_ext_001_close_to_kama10_ratio(close: pd.Series) -> pd.Series:
    """Ratio of close to KAMA(10) (Kaufman Adaptive MA, fast=2, slow=30)."""
    k = _kama(close, n=10, fast=2, slow=30)
    return _safe_div(close, k)


def rst_ext_002_pct_dist_kama10(close: pd.Series) -> pd.Series:
    """Percent distance of close from KAMA(10) ((close-KAMA)/KAMA)."""
    k = _kama(close, n=10, fast=2, slow=30)
    return _safe_div(close - k, k)


def rst_ext_003_depth_below_kama10(close: pd.Series) -> pd.Series:
    """Depth below KAMA(10) clipped at 0 (0 if above; negative = distress)."""
    k = _kama(close, n=10, fast=2, slow=30)
    return _safe_div(close - k, k).clip(upper=0.0)


def rst_ext_004_close_to_kama21_ratio(close: pd.Series) -> pd.Series:
    """Ratio of close to KAMA(21)."""
    k = _kama(close, n=_TD_MON, fast=2, slow=30)
    return _safe_div(close, k)


def rst_ext_005_pct_dist_kama21(close: pd.Series) -> pd.Series:
    """Percent distance of close from KAMA(21)."""
    k = _kama(close, n=_TD_MON, fast=2, slow=30)
    return _safe_div(close - k, k)


def rst_ext_006_depth_below_kama21(close: pd.Series) -> pd.Series:
    """Depth below KAMA(21) clipped at 0."""
    k = _kama(close, n=_TD_MON, fast=2, slow=30)
    return _safe_div(close - k, k).clip(upper=0.0)


def rst_ext_007_kama10_slope_5d(close: pd.Series) -> pd.Series:
    """5-day first difference of KAMA(10) (adaptive slope)."""
    return _kama(close, n=10).diff(_TD_WEEK)


def rst_ext_008_kama21_slope_21d(close: pd.Series) -> pd.Series:
    """21-day first difference of KAMA(21)."""
    return _kama(close, n=_TD_MON).diff(_TD_MON)


def rst_ext_009_kama10_below_kama21_flag(close: pd.Series) -> pd.Series:
    """Flag: KAMA(10) < KAMA(21) — adaptive bearish cross."""
    return (_kama(close, n=10) < _kama(close, n=_TD_MON)).astype(float)


def rst_ext_010_pct_dist_kama10_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of close-to-KAMA(10) pct-distance vs trailing 252-day window."""
    raw = _safe_div(close - _kama(close, n=10), _kama(close, n=10))
    m = _rolling_mean(raw, _TD_YEAR)
    s = _rolling_std(raw, _TD_YEAR)
    return _safe_div(raw - m, s)


# --- Group B (011-020): VWMA — volume-weighted MA constructs ---

def rst_ext_011_close_to_vwma21_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of close to 21-day VWMA (volume-weighted MA)."""
    return _safe_div(close, _vwma(close, volume, _TD_MON))


def rst_ext_012_pct_dist_vwma21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percent distance of close from 21-day VWMA."""
    v = _vwma(close, volume, _TD_MON)
    return _safe_div(close - v, v)


def rst_ext_013_depth_below_vwma21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Depth below 21-day VWMA clipped at 0 (negative = price distress vs volume-weighted level)."""
    v = _vwma(close, volume, _TD_MON)
    return _safe_div(close - v, v).clip(upper=0.0)


def rst_ext_014_close_to_vwma63_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of close to 63-day VWMA."""
    return _safe_div(close, _vwma(close, volume, _TD_QTR))


def rst_ext_015_pct_dist_vwma63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percent distance of close from 63-day VWMA."""
    v = _vwma(close, volume, _TD_QTR)
    return _safe_div(close - v, v)


def rst_ext_016_depth_below_vwma63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Depth below 63-day VWMA clipped at 0."""
    v = _vwma(close, volume, _TD_QTR)
    return _safe_div(close - v, v).clip(upper=0.0)


def rst_ext_017_vwma21_vs_sma21_spread(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Spread VWMA21 - SMA21 as pct of close (volume-weighted vs equal-weight divergence)."""
    return _safe_div(_vwma(close, volume, _TD_MON) - _sma(close, _TD_MON), close)


def rst_ext_018_vwma63_vs_sma63_spread(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Spread VWMA63 - SMA63 as pct of close."""
    return _safe_div(_vwma(close, volume, _TD_QTR) - _sma(close, _TD_QTR), close)


def rst_ext_019_pct_dist_vwma21_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of close-to-VWMA21 pct-distance vs trailing 252 days."""
    raw = _safe_div(close - _vwma(close, volume, _TD_MON), _vwma(close, volume, _TD_MON))
    m = _rolling_mean(raw, _TD_YEAR)
    s = _rolling_std(raw, _TD_YEAR)
    return _safe_div(raw - m, s)


def rst_ext_020_below_vwma21_and_sma21_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: close is below BOTH VWMA21 and SMA21 simultaneously (dual signal)."""
    return (
        (close < _vwma(close, volume, _TD_MON)).astype(float)
        * (close < _sma(close, _TD_MON)).astype(float)
    )


# --- Group C (021-026): WMA — standalone weighted MA constructs ---

def rst_ext_021_close_to_wma21_ratio(close: pd.Series) -> pd.Series:
    """Ratio of close to 21-day WMA (linear-weighted MA)."""
    return _safe_div(close, _wma(close, _TD_MON))


def rst_ext_022_pct_dist_wma21(close: pd.Series) -> pd.Series:
    """Percent distance of close from 21-day WMA."""
    w = _wma(close, _TD_MON)
    return _safe_div(close - w, w)


def rst_ext_023_depth_below_wma21(close: pd.Series) -> pd.Series:
    """Depth below 21-day WMA clipped at 0."""
    w = _wma(close, _TD_MON)
    return _safe_div(close - w, w).clip(upper=0.0)


def rst_ext_024_wma21_vs_ema21_spread(close: pd.Series) -> pd.Series:
    """Spread WMA21 - EMA21 as pct of close (weighting-method divergence)."""
    return _safe_div(_wma(close, _TD_MON) - _ema(close, _TD_MON), close)


def rst_ext_025_close_to_wma50_ratio(close: pd.Series) -> pd.Series:
    """Ratio of close to 50-day WMA."""
    return _safe_div(close, _wma(close, 50))


def rst_ext_026_depth_below_wma50(close: pd.Series) -> pd.Series:
    """Depth below 50-day WMA clipped at 0."""
    w = _wma(close, 50)
    return _safe_div(close - w, w).clip(upper=0.0)


# --- Group D (027-034): ZLEMA — zero-lag EMA constructs ---

def rst_ext_027_close_to_zlema21_ratio(close: pd.Series) -> pd.Series:
    """Ratio of close to 21-day ZLEMA (zero-lag EMA)."""
    return _safe_div(close, _zlema(close, _TD_MON))


def rst_ext_028_pct_dist_zlema21(close: pd.Series) -> pd.Series:
    """Percent distance of close from ZLEMA21."""
    z = _zlema(close, _TD_MON)
    return _safe_div(close - z, z)


def rst_ext_029_depth_below_zlema21(close: pd.Series) -> pd.Series:
    """Depth below ZLEMA21 clipped at 0."""
    z = _zlema(close, _TD_MON)
    return _safe_div(close - z, z).clip(upper=0.0)


def rst_ext_030_close_to_zlema50_ratio(close: pd.Series) -> pd.Series:
    """Ratio of close to ZLEMA50."""
    return _safe_div(close, _zlema(close, 50))


def rst_ext_031_pct_dist_zlema50(close: pd.Series) -> pd.Series:
    """Percent distance of close from ZLEMA50."""
    z = _zlema(close, 50)
    return _safe_div(close - z, z)


def rst_ext_032_zlema21_vs_ema21_spread(close: pd.Series) -> pd.Series:
    """Spread ZLEMA21 - EMA21 as pct of close (lag-reduction signal)."""
    return _safe_div(_zlema(close, _TD_MON) - _ema(close, _TD_MON), close)


def rst_ext_033_pct_dist_zlema21_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of close-to-ZLEMA21 pct-distance vs trailing 252 days."""
    raw = _safe_div(close - _zlema(close, _TD_MON), _zlema(close, _TD_MON))
    m = _rolling_mean(raw, _TD_YEAR)
    s = _rolling_std(raw, _TD_YEAR)
    return _safe_div(raw - m, s)


def rst_ext_034_zlema21_below_zlema50_flag(close: pd.Series) -> pd.Series:
    """Flag: ZLEMA21 < ZLEMA50 (zero-lag bearish cross)."""
    return (_zlema(close, _TD_MON) < _zlema(close, 50)).astype(float)


# --- Group E (035-040): ALMA — Arnaud Legoux MA constructs ---

def rst_ext_035_close_to_alma21_ratio(close: pd.Series) -> pd.Series:
    """Ratio of close to ALMA(21, sigma=6, offset=0.85)."""
    return _safe_div(close, _alma(close, w=_TD_MON, sigma=6.0, offset=0.85))


def rst_ext_036_pct_dist_alma21(close: pd.Series) -> pd.Series:
    """Percent distance of close from ALMA(21)."""
    a = _alma(close, w=_TD_MON, sigma=6.0, offset=0.85)
    return _safe_div(close - a, a)


def rst_ext_037_depth_below_alma21(close: pd.Series) -> pd.Series:
    """Depth below ALMA(21) clipped at 0."""
    a = _alma(close, w=_TD_MON, sigma=6.0, offset=0.85)
    return _safe_div(close - a, a).clip(upper=0.0)


def rst_ext_038_close_to_alma50_ratio(close: pd.Series) -> pd.Series:
    """Ratio of close to ALMA(50)."""
    return _safe_div(close, _alma(close, w=50, sigma=6.0, offset=0.85))


def rst_ext_039_pct_dist_alma50(close: pd.Series) -> pd.Series:
    """Percent distance of close from ALMA(50)."""
    a = _alma(close, w=50, sigma=6.0, offset=0.85)
    return _safe_div(close - a, a)


def rst_ext_040_alma21_vs_ema21_spread(close: pd.Series) -> pd.Series:
    """Spread ALMA21 - EMA21 as pct of close (Gaussian-vs-exponential weighting)."""
    return _safe_div(_alma(close, w=_TD_MON) - _ema(close, _TD_MON), close)


# --- Group F (041-046): T3 and FRAMA constructs ---

def rst_ext_041_close_to_t3_21_ratio(close: pd.Series) -> pd.Series:
    """Ratio of close to T3(21, v=0.7) Tillson triple MA."""
    return _safe_div(close, _t3(close, span=_TD_MON, v=0.7))


def rst_ext_042_pct_dist_t3_21(close: pd.Series) -> pd.Series:
    """Percent distance of close from T3(21)."""
    t = _t3(close, span=_TD_MON, v=0.7)
    return _safe_div(close - t, t)


def rst_ext_043_depth_below_t3_21(close: pd.Series) -> pd.Series:
    """Depth below T3(21) clipped at 0."""
    t = _t3(close, span=_TD_MON, v=0.7)
    return _safe_div(close - t, t).clip(upper=0.0)


def rst_ext_044_close_to_frama16_ratio(close: pd.Series) -> pd.Series:
    """Ratio of close to FRAMA(16) fractal adaptive MA."""
    return _safe_div(close, _frama(close, w=16))


def rst_ext_045_pct_dist_frama16(close: pd.Series) -> pd.Series:
    """Percent distance of close from FRAMA(16)."""
    f = _frama(close, w=16)
    return _safe_div(close - f, f)


def rst_ext_046_depth_below_frama16(close: pd.Series) -> pd.Series:
    """Depth below FRAMA(16) clipped at 0."""
    f = _frama(close, w=16)
    return _safe_div(close - f, f).clip(upper=0.0)


# --- Group G (047-054): MA envelope / percent-band position ---

def rst_ext_047_pos_in_sma21_pct_band_2(close: pd.Series) -> pd.Series:
    """Close position within SMA21 ± 2% envelope (0 = lower band, 1 = upper band)."""
    ma = _sma(close, _TD_MON)
    lo = ma * 0.98
    hi = ma * 1.02
    rng = (hi - lo).replace(0, np.nan)
    return _safe_div(close - lo, rng)


def rst_ext_048_pos_in_sma50_pct_band_5(close: pd.Series) -> pd.Series:
    """Close position within SMA50 ± 5% envelope."""
    ma = _sma(close, 50)
    lo = ma * 0.95
    hi = ma * 1.05
    rng = (hi - lo).replace(0, np.nan)
    return _safe_div(close - lo, rng)


def rst_ext_049_pos_in_sma200_pct_band_10(close: pd.Series) -> pd.Series:
    """Close position within SMA200 ± 10% envelope (deep bear when near 0)."""
    ma = _sma(close, 200)
    lo = ma * 0.90
    hi = ma * 1.10
    rng = (hi - lo).replace(0, np.nan)
    return _safe_div(close - lo, rng)


def rst_ext_050_below_sma21_lower_band_2pct_flag(close: pd.Series) -> pd.Series:
    """Flag: close is below the lower 2% envelope of SMA21 (extreme extension)."""
    ma = _sma(close, _TD_MON)
    return (close < ma * 0.98).astype(float)


def rst_ext_051_below_sma200_lower_band_10pct_flag(close: pd.Series) -> pd.Series:
    """Flag: close is below SMA200 lower 10% band (deep capitulation level)."""
    ma = _sma(close, 200)
    return (close < ma * 0.90).astype(float)


def rst_ext_052_pos_in_ema21_pct_band_2(close: pd.Series) -> pd.Series:
    """Close position within EMA21 ± 2% envelope."""
    ma = _ema(close, _TD_MON)
    lo = ma * 0.98
    hi = ma * 1.02
    rng = (hi - lo).replace(0, np.nan)
    return _safe_div(close - lo, rng)


def rst_ext_053_pos_in_ema200_pct_band_10(close: pd.Series) -> pd.Series:
    """Close position within EMA200 ± 10% envelope."""
    ma = _ema(close, 200)
    lo = ma * 0.90
    hi = ma * 1.10
    rng = (hi - lo).replace(0, np.nan)
    return _safe_div(close - lo, rng)


def rst_ext_054_sma200_band_breach_depth(close: pd.Series) -> pd.Series:
    """How far below SMA200 lower 10%-band close is (0 if above the band floor)."""
    ma = _sma(close, 200)
    floor = ma * 0.90
    return (close - floor).clip(upper=0.0)


# --- Group H (055-061): Days-below-MA streak and time-since-cross ---

def rst_ext_055_days_below_sma21_streak(close: pd.Series) -> pd.Series:
    """Consecutive days close has been below SMA21 (streak count; 0 when above)."""
    flag = (close < _sma(close, _TD_MON))
    return _consecutive_true_streak(flag)


def rst_ext_056_days_below_sma200_streak(close: pd.Series) -> pd.Series:
    """Consecutive days close has been below SMA200 (key capitulation persistence)."""
    flag = (close < _sma(close, 200))
    return _consecutive_true_streak(flag)


def rst_ext_057_days_below_ema200_streak(close: pd.Series) -> pd.Series:
    """Consecutive days close has been below EMA200."""
    flag = (close < _ema(close, 200))
    return _consecutive_true_streak(flag)


def rst_ext_058_bars_since_sma21_cross(close: pd.Series) -> pd.Series:
    """Bars since most recent cross of close vs SMA21 (up or down)."""
    above = (close >= _sma(close, _TD_MON))
    return _bars_since_cross(above)


def rst_ext_059_bars_since_sma200_cross(close: pd.Series) -> pd.Series:
    """Bars since most recent cross of close vs SMA200."""
    above = (close >= _sma(close, 200))
    return _bars_since_cross(above)


def rst_ext_060_days_below_all_3_key_mas_streak(close: pd.Series) -> pd.Series:
    """Consecutive days close is simultaneously below SMA21, SMA50, and SMA200."""
    flag = (
        (close < _sma(close, _TD_MON))
        & (close < _sma(close, 50))
        & (close < _sma(close, 200))
    )
    return _consecutive_true_streak(flag)


def rst_ext_061_bars_since_ema50_cross(close: pd.Series) -> pd.Series:
    """Bars since most recent cross of close vs EMA50."""
    above = (close >= _ema(close, 50))
    return _bars_since_cross(above)


# --- Group I (062-069): Multi-MA confluence / agreement scores ---

def rst_ext_062_ma_agreement_score_all_below(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of {SMA21, SMA50, SMA200, EMA21, EMA200, VWMA21} that close is below (0-6)."""
    return (
        (close < _sma(close, _TD_MON)).astype(float)
        + (close < _sma(close, 50)).astype(float)
        + (close < _sma(close, 200)).astype(float)
        + (close < _ema(close, _TD_MON)).astype(float)
        + (close < _ema(close, 200)).astype(float)
        + (close < _vwma(close, volume, _TD_MON)).astype(float)
    )


def rst_ext_063_novel_ma_agreement_score(close: pd.Series) -> pd.Series:
    """Count of {KAMA10, ZLEMA21, ALMA21, T3(21), FRAMA16, WMA21} that close is below (0-6)."""
    return (
        (close < _kama(close, n=10)).astype(float)
        + (close < _zlema(close, _TD_MON)).astype(float)
        + (close < _alma(close, w=_TD_MON)).astype(float)
        + (close < _t3(close, span=_TD_MON)).astype(float)
        + (close < _frama(close, w=16)).astype(float)
        + (close < _wma(close, _TD_MON)).astype(float)
    )


def rst_ext_064_novel_mas_all_below_flag(close: pd.Series) -> pd.Series:
    """Flag: close is below ALL of {KAMA10, ZLEMA21, ALMA21, T3(21), WMA21}."""
    return (
        (close < _kama(close, n=10)).astype(float)
        + (close < _zlema(close, _TD_MON)).astype(float)
        + (close < _alma(close, w=_TD_MON)).astype(float)
        + (close < _t3(close, span=_TD_MON)).astype(float)
        + (close < _wma(close, _TD_MON)).astype(float)
    ).ge(5.0).astype(float)


def rst_ext_065_novel_ma_mean_pct_dist(close: pd.Series) -> pd.Series:
    """Mean pct-distance of close from 5 novel MAs (KAMA10, ZLEMA21, ALMA21, T3-21, WMA21)."""
    k = _safe_div(close - _kama(close, n=10), _kama(close, n=10))
    z = _safe_div(close - _zlema(close, _TD_MON), _zlema(close, _TD_MON))
    a = _safe_div(close - _alma(close, w=_TD_MON), _alma(close, w=_TD_MON))
    t = _safe_div(close - _t3(close, span=_TD_MON), _t3(close, span=_TD_MON))
    w = _safe_div(close - _wma(close, _TD_MON), _wma(close, _TD_MON))
    return (k + z + a + t + w) / 5.0


def rst_ext_066_novel_ma_sum_depth_below(close: pd.Series) -> pd.Series:
    """Sum of depth-below (clipped at 0) for 5 novel MAs — composite distress signal."""
    k = _safe_div(close - _kama(close, n=10), _kama(close, n=10)).clip(upper=0.0)
    z = _safe_div(close - _zlema(close, _TD_MON), _zlema(close, _TD_MON)).clip(upper=0.0)
    a = _safe_div(close - _alma(close, w=_TD_MON), _alma(close, w=_TD_MON)).clip(upper=0.0)
    t = _safe_div(close - _t3(close, span=_TD_MON), _t3(close, span=_TD_MON)).clip(upper=0.0)
    w = _safe_div(close - _wma(close, _TD_MON), _wma(close, _TD_MON)).clip(upper=0.0)
    return k + z + a + t + w


def rst_ext_067_kama10_vs_sma21_spread(close: pd.Series) -> pd.Series:
    """KAMA10 - SMA21 as pct of close (adaptive-vs-simple divergence, trend strength proxy)."""
    return _safe_div(_kama(close, n=10) - _sma(close, _TD_MON), close)


def rst_ext_068_zlema21_vs_sma21_pctrank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of (ZLEMA21-SMA21)/close spread within trailing 252 days."""
    sp = _safe_div(_zlema(close, _TD_MON) - _sma(close, _TD_MON), close)
    return sp.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rst_ext_069_novel_ma_std_pct_of_mean(close: pd.Series) -> pd.Series:
    """Std of {KAMA10, ZLEMA21, ALMA21, T3-21, WMA21} values / their mean (novel ribbon compression)."""
    k = _kama(close, n=10)
    z = _zlema(close, _TD_MON)
    a = _alma(close, w=_TD_MON)
    t = _t3(close, span=_TD_MON)
    w = _wma(close, _TD_MON)
    df = pd.concat([k, z, a, t, w], axis=1)
    mn = df.mean(axis=1).replace(0, np.nan)
    sd = df.std(axis=1)
    return _safe_div(sd, mn)


# --- Group J (070-075): ROC and acceleration of novel MA distances ---

def rst_ext_070_kama10_dist_roc_5d(close: pd.Series) -> pd.Series:
    """5-day rate-of-change of close-to-KAMA10 pct-distance (velocity)."""
    raw = _safe_div(close - _kama(close, n=10), _kama(close, n=10))
    return raw.diff(_TD_WEEK)


def rst_ext_071_vwma21_dist_roc_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day rate-of-change of close-to-VWMA21 pct-distance."""
    raw = _safe_div(close - _vwma(close, volume, _TD_MON), _vwma(close, volume, _TD_MON))
    return raw.diff(_TD_WEEK)


def rst_ext_072_zlema21_dist_roc_21d(close: pd.Series) -> pd.Series:
    """21-day rate-of-change of close-to-ZLEMA21 pct-distance (monthly velocity)."""
    raw = _safe_div(close - _zlema(close, _TD_MON), _zlema(close, _TD_MON))
    return raw.diff(_TD_MON)


def rst_ext_073_novel_ma_mean_dist_roc_5d(close: pd.Series) -> pd.Series:
    """5-day ROC of mean pct-distance from 5 novel MAs (composite velocity)."""
    raw = rst_ext_065_novel_ma_mean_pct_dist(close)
    return raw.diff(_TD_WEEK)


def rst_ext_074_days_below_sma200_streak_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of below-SMA200 streak vs trailing 252-day distribution (how extreme the streak is)."""
    streak = rst_ext_056_days_below_sma200_streak(close)
    m = _rolling_mean(streak, _TD_YEAR)
    s = _rolling_std(streak, _TD_YEAR)
    return _safe_div(streak - m, s)


def rst_ext_075_novel_ma_sum_depth_roc_5d(close: pd.Series) -> pd.Series:
    """5-day ROC of the sum-of-depth-below-5-novel-MAs composite (acceleration of breakdown)."""
    raw = rst_ext_066_novel_ma_sum_depth_below(close)
    return raw.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

RELATIVE_STRENGTH_EXTENDED_REGISTRY_001_075 = {
    "rst_ext_001_close_to_kama10_ratio": {"inputs": ["close"], "func": rst_ext_001_close_to_kama10_ratio},
    "rst_ext_002_pct_dist_kama10": {"inputs": ["close"], "func": rst_ext_002_pct_dist_kama10},
    "rst_ext_003_depth_below_kama10": {"inputs": ["close"], "func": rst_ext_003_depth_below_kama10},
    "rst_ext_004_close_to_kama21_ratio": {"inputs": ["close"], "func": rst_ext_004_close_to_kama21_ratio},
    "rst_ext_005_pct_dist_kama21": {"inputs": ["close"], "func": rst_ext_005_pct_dist_kama21},
    "rst_ext_006_depth_below_kama21": {"inputs": ["close"], "func": rst_ext_006_depth_below_kama21},
    "rst_ext_007_kama10_slope_5d": {"inputs": ["close"], "func": rst_ext_007_kama10_slope_5d},
    "rst_ext_008_kama21_slope_21d": {"inputs": ["close"], "func": rst_ext_008_kama21_slope_21d},
    "rst_ext_009_kama10_below_kama21_flag": {"inputs": ["close"], "func": rst_ext_009_kama10_below_kama21_flag},
    "rst_ext_010_pct_dist_kama10_zscore_252d": {"inputs": ["close"], "func": rst_ext_010_pct_dist_kama10_zscore_252d},
    "rst_ext_011_close_to_vwma21_ratio": {"inputs": ["close", "volume"], "func": rst_ext_011_close_to_vwma21_ratio},
    "rst_ext_012_pct_dist_vwma21": {"inputs": ["close", "volume"], "func": rst_ext_012_pct_dist_vwma21},
    "rst_ext_013_depth_below_vwma21": {"inputs": ["close", "volume"], "func": rst_ext_013_depth_below_vwma21},
    "rst_ext_014_close_to_vwma63_ratio": {"inputs": ["close", "volume"], "func": rst_ext_014_close_to_vwma63_ratio},
    "rst_ext_015_pct_dist_vwma63": {"inputs": ["close", "volume"], "func": rst_ext_015_pct_dist_vwma63},
    "rst_ext_016_depth_below_vwma63": {"inputs": ["close", "volume"], "func": rst_ext_016_depth_below_vwma63},
    "rst_ext_017_vwma21_vs_sma21_spread": {"inputs": ["close", "volume"], "func": rst_ext_017_vwma21_vs_sma21_spread},
    "rst_ext_018_vwma63_vs_sma63_spread": {"inputs": ["close", "volume"], "func": rst_ext_018_vwma63_vs_sma63_spread},
    "rst_ext_019_pct_dist_vwma21_zscore_252d": {"inputs": ["close", "volume"], "func": rst_ext_019_pct_dist_vwma21_zscore_252d},
    "rst_ext_020_below_vwma21_and_sma21_flag": {"inputs": ["close", "volume"], "func": rst_ext_020_below_vwma21_and_sma21_flag},
    "rst_ext_021_close_to_wma21_ratio": {"inputs": ["close"], "func": rst_ext_021_close_to_wma21_ratio},
    "rst_ext_022_pct_dist_wma21": {"inputs": ["close"], "func": rst_ext_022_pct_dist_wma21},
    "rst_ext_023_depth_below_wma21": {"inputs": ["close"], "func": rst_ext_023_depth_below_wma21},
    "rst_ext_024_wma21_vs_ema21_spread": {"inputs": ["close"], "func": rst_ext_024_wma21_vs_ema21_spread},
    "rst_ext_025_close_to_wma50_ratio": {"inputs": ["close"], "func": rst_ext_025_close_to_wma50_ratio},
    "rst_ext_026_depth_below_wma50": {"inputs": ["close"], "func": rst_ext_026_depth_below_wma50},
    "rst_ext_027_close_to_zlema21_ratio": {"inputs": ["close"], "func": rst_ext_027_close_to_zlema21_ratio},
    "rst_ext_028_pct_dist_zlema21": {"inputs": ["close"], "func": rst_ext_028_pct_dist_zlema21},
    "rst_ext_029_depth_below_zlema21": {"inputs": ["close"], "func": rst_ext_029_depth_below_zlema21},
    "rst_ext_030_close_to_zlema50_ratio": {"inputs": ["close"], "func": rst_ext_030_close_to_zlema50_ratio},
    "rst_ext_031_pct_dist_zlema50": {"inputs": ["close"], "func": rst_ext_031_pct_dist_zlema50},
    "rst_ext_032_zlema21_vs_ema21_spread": {"inputs": ["close"], "func": rst_ext_032_zlema21_vs_ema21_spread},
    "rst_ext_033_pct_dist_zlema21_zscore_252d": {"inputs": ["close"], "func": rst_ext_033_pct_dist_zlema21_zscore_252d},
    "rst_ext_034_zlema21_below_zlema50_flag": {"inputs": ["close"], "func": rst_ext_034_zlema21_below_zlema50_flag},
    "rst_ext_035_close_to_alma21_ratio": {"inputs": ["close"], "func": rst_ext_035_close_to_alma21_ratio},
    "rst_ext_036_pct_dist_alma21": {"inputs": ["close"], "func": rst_ext_036_pct_dist_alma21},
    "rst_ext_037_depth_below_alma21": {"inputs": ["close"], "func": rst_ext_037_depth_below_alma21},
    "rst_ext_038_close_to_alma50_ratio": {"inputs": ["close"], "func": rst_ext_038_close_to_alma50_ratio},
    "rst_ext_039_pct_dist_alma50": {"inputs": ["close"], "func": rst_ext_039_pct_dist_alma50},
    "rst_ext_040_alma21_vs_ema21_spread": {"inputs": ["close"], "func": rst_ext_040_alma21_vs_ema21_spread},
    "rst_ext_041_close_to_t3_21_ratio": {"inputs": ["close"], "func": rst_ext_041_close_to_t3_21_ratio},
    "rst_ext_042_pct_dist_t3_21": {"inputs": ["close"], "func": rst_ext_042_pct_dist_t3_21},
    "rst_ext_043_depth_below_t3_21": {"inputs": ["close"], "func": rst_ext_043_depth_below_t3_21},
    "rst_ext_044_close_to_frama16_ratio": {"inputs": ["close"], "func": rst_ext_044_close_to_frama16_ratio},
    "rst_ext_045_pct_dist_frama16": {"inputs": ["close"], "func": rst_ext_045_pct_dist_frama16},
    "rst_ext_046_depth_below_frama16": {"inputs": ["close"], "func": rst_ext_046_depth_below_frama16},
    "rst_ext_047_pos_in_sma21_pct_band_2": {"inputs": ["close"], "func": rst_ext_047_pos_in_sma21_pct_band_2},
    "rst_ext_048_pos_in_sma50_pct_band_5": {"inputs": ["close"], "func": rst_ext_048_pos_in_sma50_pct_band_5},
    "rst_ext_049_pos_in_sma200_pct_band_10": {"inputs": ["close"], "func": rst_ext_049_pos_in_sma200_pct_band_10},
    "rst_ext_050_below_sma21_lower_band_2pct_flag": {"inputs": ["close"], "func": rst_ext_050_below_sma21_lower_band_2pct_flag},
    "rst_ext_051_below_sma200_lower_band_10pct_flag": {"inputs": ["close"], "func": rst_ext_051_below_sma200_lower_band_10pct_flag},
    "rst_ext_052_pos_in_ema21_pct_band_2": {"inputs": ["close"], "func": rst_ext_052_pos_in_ema21_pct_band_2},
    "rst_ext_053_pos_in_ema200_pct_band_10": {"inputs": ["close"], "func": rst_ext_053_pos_in_ema200_pct_band_10},
    "rst_ext_054_sma200_band_breach_depth": {"inputs": ["close"], "func": rst_ext_054_sma200_band_breach_depth},
    "rst_ext_055_days_below_sma21_streak": {"inputs": ["close"], "func": rst_ext_055_days_below_sma21_streak},
    "rst_ext_056_days_below_sma200_streak": {"inputs": ["close"], "func": rst_ext_056_days_below_sma200_streak},
    "rst_ext_057_days_below_ema200_streak": {"inputs": ["close"], "func": rst_ext_057_days_below_ema200_streak},
    "rst_ext_058_bars_since_sma21_cross": {"inputs": ["close"], "func": rst_ext_058_bars_since_sma21_cross},
    "rst_ext_059_bars_since_sma200_cross": {"inputs": ["close"], "func": rst_ext_059_bars_since_sma200_cross},
    "rst_ext_060_days_below_all_3_key_mas_streak": {"inputs": ["close"], "func": rst_ext_060_days_below_all_3_key_mas_streak},
    "rst_ext_061_bars_since_ema50_cross": {"inputs": ["close"], "func": rst_ext_061_bars_since_ema50_cross},
    "rst_ext_062_ma_agreement_score_all_below": {"inputs": ["close", "volume"], "func": rst_ext_062_ma_agreement_score_all_below},
    "rst_ext_063_novel_ma_agreement_score": {"inputs": ["close"], "func": rst_ext_063_novel_ma_agreement_score},
    "rst_ext_064_novel_mas_all_below_flag": {"inputs": ["close"], "func": rst_ext_064_novel_mas_all_below_flag},
    "rst_ext_065_novel_ma_mean_pct_dist": {"inputs": ["close"], "func": rst_ext_065_novel_ma_mean_pct_dist},
    "rst_ext_066_novel_ma_sum_depth_below": {"inputs": ["close"], "func": rst_ext_066_novel_ma_sum_depth_below},
    "rst_ext_067_kama10_vs_sma21_spread": {"inputs": ["close"], "func": rst_ext_067_kama10_vs_sma21_spread},
    "rst_ext_068_zlema21_vs_sma21_pctrank_252d": {"inputs": ["close"], "func": rst_ext_068_zlema21_vs_sma21_pctrank_252d},
    "rst_ext_069_novel_ma_std_pct_of_mean": {"inputs": ["close"], "func": rst_ext_069_novel_ma_std_pct_of_mean},
    "rst_ext_070_kama10_dist_roc_5d": {"inputs": ["close"], "func": rst_ext_070_kama10_dist_roc_5d},
    "rst_ext_071_vwma21_dist_roc_5d": {"inputs": ["close", "volume"], "func": rst_ext_071_vwma21_dist_roc_5d},
    "rst_ext_072_zlema21_dist_roc_21d": {"inputs": ["close"], "func": rst_ext_072_zlema21_dist_roc_21d},
    "rst_ext_073_novel_ma_mean_dist_roc_5d": {"inputs": ["close"], "func": rst_ext_073_novel_ma_mean_dist_roc_5d},
    "rst_ext_074_days_below_sma200_streak_zscore_252d": {"inputs": ["close"], "func": rst_ext_074_days_below_sma200_streak_zscore_252d},
    "rst_ext_075_novel_ma_sum_depth_roc_5d": {"inputs": ["close"], "func": rst_ext_075_novel_ma_sum_depth_roc_5d},
}
