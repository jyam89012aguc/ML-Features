"""
30_relative_strength — Extended 2nd Derivatives (Features extdrv2_001-025)
Domain: rate of change / velocity of extended-base relative-strength concepts —
        KAMA distance velocity, VWMA distance velocity, WMA distance changes,
        ZLEMA distance changes, ALMA distance velocity, T3/FRAMA distance changes,
        MA envelope position velocity, MA agreement score velocity,
        novel-MA composite ROC, and novel-MA ribbon compression dynamics.
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


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi   = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m  = x.mean()
        num  = ((xi - xi_m) * (x - x_m)).sum()
        den  = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


# ── Novel MA Helpers (self-contained) ────────────────────────────────────────

def _wma(close: pd.Series, w: int) -> pd.Series:
    """Linearly-weighted moving average."""
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
    """Kaufman Adaptive Moving Average (KAMA)."""
    arr = close.to_numpy(dtype=float)
    out = np.full(len(arr), np.nan)
    fc = 2.0 / (fast + 1)
    sc = 2.0 / (slow + 1)
    seed_idx = n - 1
    if seed_idx >= len(arr):
        return pd.Series(out, index=close.index)
    out[seed_idx] = arr[seed_idx]
    for i in range(seed_idx + 1, len(arr)):
        direction = abs(arr[i] - arr[i - n])
        volatility = np.sum(np.abs(np.diff(arr[max(0, i - n + 1):i + 1])))
        er = 0.0 if volatility < _EPS else direction / volatility
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
    """Zero-Lag EMA."""
    lag = (span - 1) // 2
    adjusted = close + (close - close.shift(lag))
    return adjusted.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _alma(close: pd.Series, w: int = 21, sigma: float = 6.0, offset: float = 0.85) -> pd.Series:
    """Arnaud Legoux Moving Average — Gaussian-weighted MA."""
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
    """Tillson T3 triple-smoothed MA."""
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
    """Fractal Adaptive Moving Average (FRAMA)."""
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


# ── Extended 2nd-Derivative Feature Functions ─────────────────────────────────

# --- Group A (001-005): KAMA distance velocity ---

def rst_extdrv2_001_pct_dist_kama10_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of close-to-KAMA(10) pct-distance (KAMA velocity, weekly)."""
    k = _kama(close, n=10, fast=2, slow=30)
    raw = _safe_div(close - k, k)
    return raw.diff(_TD_WEEK)


def rst_extdrv2_002_pct_dist_kama10_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of close-to-KAMA(10) pct-distance (monthly KAMA velocity)."""
    k = _kama(close, n=10, fast=2, slow=30)
    raw = _safe_div(close - k, k)
    return raw.diff(_TD_MON)


def rst_extdrv2_003_pct_dist_kama21_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of close-to-KAMA(21) pct-distance."""
    k = _kama(close, n=_TD_MON, fast=2, slow=30)
    raw = _safe_div(close - k, k)
    return raw.diff(_TD_WEEK)


def rst_extdrv2_004_kama10_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of KAMA(10) slope (acceleration of adaptive MA direction)."""
    slope = _kama(close, n=10).diff(_TD_WEEK)
    return slope.diff(_TD_WEEK)


def rst_extdrv2_005_pct_dist_kama10_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of close-to-KAMA(10) pct-distance over trailing 21 days."""
    k = _kama(close, n=10, fast=2, slow=30)
    raw = _safe_div(close - k, k)
    return _linslope(raw, _TD_MON)


# --- Group B (006-010): VWMA distance velocity ---

def rst_extdrv2_006_pct_dist_vwma21_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of close-to-VWMA21 pct-distance (monthly VWMA velocity)."""
    v = _vwma(close, volume, _TD_MON)
    raw = _safe_div(close - v, v)
    return raw.diff(_TD_MON)


def rst_extdrv2_007_pct_dist_vwma63_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of close-to-VWMA63 pct-distance."""
    v = _vwma(close, volume, _TD_QTR)
    raw = _safe_div(close - v, v)
    return raw.diff(_TD_WEEK)


def rst_extdrv2_008_vwma21_vs_sma21_spread_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of VWMA21-SMA21 spread as pct of close (volume-weighting divergence velocity)."""
    sp = _safe_div(_vwma(close, volume, _TD_MON) - _sma(close, _TD_MON), close)
    return sp.diff(_TD_WEEK)


def rst_extdrv2_009_pct_dist_vwma21_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of close-to-VWMA21 pct-distance over trailing 21 days."""
    v = _vwma(close, volume, _TD_MON)
    raw = _safe_div(close - v, v)
    return _linslope(raw, _TD_MON)


def rst_extdrv2_010_vwma63_vs_sma63_spread_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of VWMA63-SMA63 spread as pct of close."""
    sp = _safe_div(_vwma(close, volume, _TD_QTR) - _sma(close, _TD_QTR), close)
    return sp.diff(_TD_MON)


# --- Group C (011-013): WMA and ZLEMA distance velocity ---

def rst_extdrv2_011_pct_dist_wma21_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of close-to-WMA21 pct-distance."""
    w = _wma(close, _TD_MON)
    raw = _safe_div(close - w, w)
    return raw.diff(_TD_WEEK)


def rst_extdrv2_012_pct_dist_wma50_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of close-to-WMA50 pct-distance."""
    w = _wma(close, 50)
    raw = _safe_div(close - w, w)
    return raw.diff(_TD_WEEK)


def rst_extdrv2_013_pct_dist_zlema21_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of close-to-ZLEMA21 pct-distance (zero-lag velocity)."""
    z = _zlema(close, _TD_MON)
    raw = _safe_div(close - z, z)
    return raw.diff(_TD_WEEK)


# --- Group D (014-016): ALMA and T3/FRAMA distance velocity ---

def rst_extdrv2_014_pct_dist_alma21_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of close-to-ALMA21 pct-distance."""
    a = _alma(close, w=_TD_MON, sigma=6.0, offset=0.85)
    raw = _safe_div(close - a, a)
    return raw.diff(_TD_WEEK)


def rst_extdrv2_015_pct_dist_alma50_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of close-to-ALMA50 pct-distance."""
    a = _alma(close, w=50, sigma=6.0, offset=0.85)
    raw = _safe_div(close - a, a)
    return raw.diff(_TD_MON)


def rst_extdrv2_016_pct_dist_t3_21_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of close-to-T3(21) pct-distance (Tillson velocity)."""
    t = _t3(close, span=_TD_MON, v=0.7)
    raw = _safe_div(close - t, t)
    return raw.diff(_TD_WEEK)


# --- Group E (017-018): FRAMA distance velocity ---

def rst_extdrv2_017_pct_dist_frama16_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of close-to-FRAMA(16) pct-distance (fractal-adaptive velocity)."""
    f = _frama(close, w=16)
    raw = _safe_div(close - f, f)
    return raw.diff(_TD_WEEK)


def rst_extdrv2_018_pct_dist_frama16_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of close-to-FRAMA(16) pct-distance."""
    f = _frama(close, w=16)
    raw = _safe_div(close - f, f)
    return raw.diff(_TD_MON)


# --- Group F (019-021): MA envelope position velocity ---

def rst_extdrv2_019_pos_in_sma21_band_2_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of position within SMA21±2% envelope (band position velocity)."""
    ma = _sma(close, _TD_MON)
    lo = ma * 0.98
    hi = ma * 1.02
    rng = (hi - lo).replace(0, np.nan)
    pos = _safe_div(close - lo, rng)
    return pos.diff(_TD_WEEK)


def rst_extdrv2_020_pos_in_sma200_band_10_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of position within SMA200±10% envelope."""
    ma = _sma(close, 200)
    lo = ma * 0.90
    hi = ma * 1.10
    rng = (hi - lo).replace(0, np.nan)
    pos = _safe_div(close - lo, rng)
    return pos.diff(_TD_WEEK)


def rst_extdrv2_021_pos_in_ema21_band_2_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of position within EMA21±2% envelope."""
    ma = _ema(close, _TD_MON)
    lo = ma * 0.98
    hi = ma * 1.02
    rng = (hi - lo).replace(0, np.nan)
    pos = _safe_div(close - lo, rng)
    return pos.diff(_TD_MON)


# --- Group G (022-025): Novel MA composite / confluence velocity ---

def rst_extdrv2_022_novel_ma_agreement_score_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of novel-MA agreement score (KAMA10,ZLEMA21,ALMA21,T3-21,FRAMA16,WMA21 below-count velocity)."""
    score = (
        (close < _kama(close, n=10)).astype(float)
        + (close < _zlema(close, _TD_MON)).astype(float)
        + (close < _alma(close, w=_TD_MON)).astype(float)
        + (close < _t3(close, span=_TD_MON)).astype(float)
        + (close < _frama(close, w=16)).astype(float)
        + (close < _wma(close, _TD_MON)).astype(float)
    )
    return score.diff(_TD_WEEK)


def rst_extdrv2_023_novel_ma_mean_pct_dist_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of mean pct-distance from 5 novel MAs (composite monthly velocity)."""
    k = _safe_div(close - _kama(close, n=10), _kama(close, n=10))
    z = _safe_div(close - _zlema(close, _TD_MON), _zlema(close, _TD_MON))
    a = _safe_div(close - _alma(close, w=_TD_MON), _alma(close, w=_TD_MON))
    t = _safe_div(close - _t3(close, span=_TD_MON), _t3(close, span=_TD_MON))
    w = _safe_div(close - _wma(close, _TD_MON), _wma(close, _TD_MON))
    mean_dist = (k + z + a + t + w) / 5.0
    return mean_dist.diff(_TD_MON)


def rst_extdrv2_024_novel_ma_sum_depth_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of sum-of-depth-below-5-novel-MAs composite (monthly distress velocity)."""
    k = _safe_div(close - _kama(close, n=10), _kama(close, n=10)).clip(upper=0.0)
    z = _safe_div(close - _zlema(close, _TD_MON), _zlema(close, _TD_MON)).clip(upper=0.0)
    a = _safe_div(close - _alma(close, w=_TD_MON), _alma(close, w=_TD_MON)).clip(upper=0.0)
    t = _safe_div(close - _t3(close, span=_TD_MON), _t3(close, span=_TD_MON)).clip(upper=0.0)
    w = _safe_div(close - _wma(close, _TD_MON), _wma(close, _TD_MON)).clip(upper=0.0)
    depth = k + z + a + t + w
    return depth.diff(_TD_MON)


def rst_extdrv2_025_novel_ma_std_pct_mean_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of novel-MA ribbon compression (std/mean of 5 novel MAs)."""
    k = _kama(close, n=10)
    z = _zlema(close, _TD_MON)
    a = _alma(close, w=_TD_MON)
    t = _t3(close, span=_TD_MON)
    w = _wma(close, _TD_MON)
    df = pd.concat([k, z, a, t, w], axis=1)
    mn = df.mean(axis=1).replace(0, np.nan)
    sd = df.std(axis=1)
    compression = _safe_div(sd, mn)
    return compression.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

RELATIVE_STRENGTH_EXTENDED_REGISTRY_2ND_DERIVATIVES = {
    "rst_extdrv2_001_pct_dist_kama10_5d_diff": {"inputs": ["close"], "func": rst_extdrv2_001_pct_dist_kama10_5d_diff},
    "rst_extdrv2_002_pct_dist_kama10_21d_diff": {"inputs": ["close"], "func": rst_extdrv2_002_pct_dist_kama10_21d_diff},
    "rst_extdrv2_003_pct_dist_kama21_5d_diff": {"inputs": ["close"], "func": rst_extdrv2_003_pct_dist_kama21_5d_diff},
    "rst_extdrv2_004_kama10_slope_5d_diff": {"inputs": ["close"], "func": rst_extdrv2_004_kama10_slope_5d_diff},
    "rst_extdrv2_005_pct_dist_kama10_slope_21d": {"inputs": ["close"], "func": rst_extdrv2_005_pct_dist_kama10_slope_21d},
    "rst_extdrv2_006_pct_dist_vwma21_21d_diff": {"inputs": ["close", "volume"], "func": rst_extdrv2_006_pct_dist_vwma21_21d_diff},
    "rst_extdrv2_007_pct_dist_vwma63_5d_diff": {"inputs": ["close", "volume"], "func": rst_extdrv2_007_pct_dist_vwma63_5d_diff},
    "rst_extdrv2_008_vwma21_vs_sma21_spread_5d_diff": {"inputs": ["close", "volume"], "func": rst_extdrv2_008_vwma21_vs_sma21_spread_5d_diff},
    "rst_extdrv2_009_pct_dist_vwma21_slope_21d": {"inputs": ["close", "volume"], "func": rst_extdrv2_009_pct_dist_vwma21_slope_21d},
    "rst_extdrv2_010_vwma63_vs_sma63_spread_21d_diff": {"inputs": ["close", "volume"], "func": rst_extdrv2_010_vwma63_vs_sma63_spread_21d_diff},
    "rst_extdrv2_011_pct_dist_wma21_5d_diff": {"inputs": ["close"], "func": rst_extdrv2_011_pct_dist_wma21_5d_diff},
    "rst_extdrv2_012_pct_dist_wma50_5d_diff": {"inputs": ["close"], "func": rst_extdrv2_012_pct_dist_wma50_5d_diff},
    "rst_extdrv2_013_pct_dist_zlema21_5d_diff": {"inputs": ["close"], "func": rst_extdrv2_013_pct_dist_zlema21_5d_diff},
    "rst_extdrv2_014_pct_dist_alma21_5d_diff": {"inputs": ["close"], "func": rst_extdrv2_014_pct_dist_alma21_5d_diff},
    "rst_extdrv2_015_pct_dist_alma50_21d_diff": {"inputs": ["close"], "func": rst_extdrv2_015_pct_dist_alma50_21d_diff},
    "rst_extdrv2_016_pct_dist_t3_21_5d_diff": {"inputs": ["close"], "func": rst_extdrv2_016_pct_dist_t3_21_5d_diff},
    "rst_extdrv2_017_pct_dist_frama16_5d_diff": {"inputs": ["close"], "func": rst_extdrv2_017_pct_dist_frama16_5d_diff},
    "rst_extdrv2_018_pct_dist_frama16_21d_diff": {"inputs": ["close"], "func": rst_extdrv2_018_pct_dist_frama16_21d_diff},
    "rst_extdrv2_019_pos_in_sma21_band_2_5d_diff": {"inputs": ["close"], "func": rst_extdrv2_019_pos_in_sma21_band_2_5d_diff},
    "rst_extdrv2_020_pos_in_sma200_band_10_5d_diff": {"inputs": ["close"], "func": rst_extdrv2_020_pos_in_sma200_band_10_5d_diff},
    "rst_extdrv2_021_pos_in_ema21_band_2_21d_diff": {"inputs": ["close"], "func": rst_extdrv2_021_pos_in_ema21_band_2_21d_diff},
    "rst_extdrv2_022_novel_ma_agreement_score_5d_diff": {"inputs": ["close"], "func": rst_extdrv2_022_novel_ma_agreement_score_5d_diff},
    "rst_extdrv2_023_novel_ma_mean_pct_dist_21d_diff": {"inputs": ["close"], "func": rst_extdrv2_023_novel_ma_mean_pct_dist_21d_diff},
    "rst_extdrv2_024_novel_ma_sum_depth_21d_diff": {"inputs": ["close"], "func": rst_extdrv2_024_novel_ma_sum_depth_21d_diff},
    "rst_extdrv2_025_novel_ma_std_pct_mean_5d_diff": {"inputs": ["close"], "func": rst_extdrv2_025_novel_ma_std_pct_mean_5d_diff},
}
