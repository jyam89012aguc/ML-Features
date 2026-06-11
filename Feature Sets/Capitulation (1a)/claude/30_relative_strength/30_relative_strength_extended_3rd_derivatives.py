"""
30_relative_strength — Extended 3rd Derivatives (Features extdrv3_001-025)
Domain: acceleration / curvature of extended 2nd-derivative relative-strength
        concepts — KAMA distance acceleration, VWMA distance acceleration,
        WMA/ZLEMA distance second diffs, ALMA/T3/FRAMA distance curvature,
        MA envelope position acceleration, novel-MA composite acceleration,
        novel-MA ribbon compression curvature, and OLS slope-of-slope constructs.
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


# ── Extended 3rd-Derivative Feature Functions ─────────────────────────────────

# --- Group A (001-005): KAMA distance acceleration ---

def rst_extdrv3_001_pct_dist_kama10_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of close-to-KAMA(10) pct-distance (KAMA acceleration)."""
    k = _kama(close, n=10, fast=2, slow=30)
    raw = _safe_div(close - k, k)
    vel = raw.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rst_extdrv3_002_pct_dist_kama10_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of monthly KAMA(10) velocity (KAMA jerk)."""
    k = _kama(close, n=10, fast=2, slow=30)
    raw = _safe_div(close - k, k)
    vel = raw.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def rst_extdrv3_003_pct_dist_kama21_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of close-to-KAMA(21) pct-distance."""
    k = _kama(close, n=_TD_MON, fast=2, slow=30)
    raw = _safe_div(close - k, k)
    vel = raw.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rst_extdrv3_004_kama10_slope_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of KAMA(10) slope (KAMA jerk of adaptive direction)."""
    slope = _kama(close, n=10).diff(_TD_WEEK)
    vel = slope.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rst_extdrv3_005_pct_dist_kama10_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of KAMA(10)-distance over 21 days (slope-of-slope)."""
    k = _kama(close, n=10, fast=2, slow=30)
    raw = _safe_div(close - k, k)
    slp = _linslope(raw, _TD_MON)
    return slp.diff(_TD_WEEK)


# --- Group B (006-010): VWMA distance acceleration ---

def rst_extdrv3_006_pct_dist_vwma21_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of monthly VWMA21 velocity (VWMA distance jerk)."""
    v = _vwma(close, volume, _TD_MON)
    raw = _safe_div(close - v, v)
    vel = raw.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def rst_extdrv3_007_pct_dist_vwma63_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of close-to-VWMA63 pct-distance (acceleration)."""
    v = _vwma(close, volume, _TD_QTR)
    raw = _safe_div(close - v, v)
    vel = raw.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rst_extdrv3_008_vwma21_vs_sma21_spread_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of VWMA21-SMA21 spread (volume-weighting divergence acceleration)."""
    sp = _safe_div(_vwma(close, volume, _TD_MON) - _sma(close, _TD_MON), close)
    vel = sp.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rst_extdrv3_009_pct_dist_vwma21_slope_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of VWMA21-distance over 21 days (slope-of-slope)."""
    v = _vwma(close, volume, _TD_MON)
    raw = _safe_div(close - v, v)
    slp = _linslope(raw, _TD_MON)
    return slp.diff(_TD_WEEK)


def rst_extdrv3_010_vwma63_vs_sma63_spread_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of monthly VWMA63-SMA63 spread velocity."""
    sp = _safe_div(_vwma(close, volume, _TD_QTR) - _sma(close, _TD_QTR), close)
    vel = sp.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


# --- Group C (011-013): WMA and ZLEMA distance acceleration ---

def rst_extdrv3_011_pct_dist_wma21_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of close-to-WMA21 pct-distance (WMA acceleration)."""
    w = _wma(close, _TD_MON)
    raw = _safe_div(close - w, w)
    vel = raw.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rst_extdrv3_012_pct_dist_wma50_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of close-to-WMA50 pct-distance."""
    w = _wma(close, 50)
    raw = _safe_div(close - w, w)
    vel = raw.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rst_extdrv3_013_pct_dist_zlema21_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of close-to-ZLEMA21 pct-distance (zero-lag acceleration)."""
    z = _zlema(close, _TD_MON)
    raw = _safe_div(close - z, z)
    vel = raw.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# --- Group D (014-016): ALMA / T3 / FRAMA distance acceleration ---

def rst_extdrv3_014_pct_dist_alma21_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of close-to-ALMA21 pct-distance (Gaussian-MA acceleration)."""
    a = _alma(close, w=_TD_MON, sigma=6.0, offset=0.85)
    raw = _safe_div(close - a, a)
    vel = raw.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rst_extdrv3_015_pct_dist_t3_21_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of close-to-T3(21) pct-distance (Tillson acceleration)."""
    t = _t3(close, span=_TD_MON, v=0.7)
    raw = _safe_div(close - t, t)
    vel = raw.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rst_extdrv3_016_pct_dist_frama16_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of close-to-FRAMA(16) pct-distance (fractal-adaptive acceleration)."""
    f = _frama(close, w=16)
    raw = _safe_div(close - f, f)
    vel = raw.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# --- Group E (017-019): MA envelope position acceleration ---

def rst_extdrv3_017_pos_in_sma21_band_2_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of position within SMA21±2% band (envelope position acceleration)."""
    ma = _sma(close, _TD_MON)
    lo = ma * 0.98
    hi = ma * 1.02
    rng = (hi - lo).replace(0, np.nan)
    pos = _safe_div(close - lo, rng)
    vel = pos.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rst_extdrv3_018_pos_in_sma200_band_10_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of position within SMA200±10% band."""
    ma = _sma(close, 200)
    lo = ma * 0.90
    hi = ma * 1.10
    rng = (hi - lo).replace(0, np.nan)
    pos = _safe_div(close - lo, rng)
    vel = pos.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rst_extdrv3_019_pos_in_ema21_band_2_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of EMA21±2% envelope position (slope-of-slope)."""
    ma = _ema(close, _TD_MON)
    lo = ma * 0.98
    hi = ma * 1.02
    rng = (hi - lo).replace(0, np.nan)
    pos = _safe_div(close - lo, rng)
    slp = _linslope(pos, _TD_MON)
    return slp.diff(_TD_WEEK)


# --- Group F (020-022): Novel MA composite / confluence acceleration ---

def rst_extdrv3_020_novel_ma_agreement_score_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of novel-MA agreement score (below-count acceleration)."""
    score = (
        (close < _kama(close, n=10)).astype(float)
        + (close < _zlema(close, _TD_MON)).astype(float)
        + (close < _alma(close, w=_TD_MON)).astype(float)
        + (close < _t3(close, span=_TD_MON)).astype(float)
        + (close < _frama(close, w=16)).astype(float)
        + (close < _wma(close, _TD_MON)).astype(float)
    )
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rst_extdrv3_021_novel_ma_mean_pct_dist_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of mean pct-distance from 5 novel MAs."""
    k = _safe_div(close - _kama(close, n=10), _kama(close, n=10))
    z = _safe_div(close - _zlema(close, _TD_MON), _zlema(close, _TD_MON))
    a = _safe_div(close - _alma(close, w=_TD_MON), _alma(close, w=_TD_MON))
    t = _safe_div(close - _t3(close, span=_TD_MON), _t3(close, span=_TD_MON))
    w = _safe_div(close - _wma(close, _TD_MON), _wma(close, _TD_MON))
    mean_dist = (k + z + a + t + w) / 5.0
    vel = mean_dist.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def rst_extdrv3_022_novel_ma_sum_depth_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of sum-of-depth-below-5-novel-MAs."""
    k = _safe_div(close - _kama(close, n=10), _kama(close, n=10)).clip(upper=0.0)
    z = _safe_div(close - _zlema(close, _TD_MON), _zlema(close, _TD_MON)).clip(upper=0.0)
    a = _safe_div(close - _alma(close, w=_TD_MON), _alma(close, w=_TD_MON)).clip(upper=0.0)
    t = _safe_div(close - _t3(close, span=_TD_MON), _t3(close, span=_TD_MON)).clip(upper=0.0)
    w = _safe_div(close - _wma(close, _TD_MON), _wma(close, _TD_MON)).clip(upper=0.0)
    depth = k + z + a + t + w
    vel = depth.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


# --- Group G (023-025): Novel MA ribbon compression curvature ---

def rst_extdrv3_023_novel_ma_std_pct_mean_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of novel-MA ribbon compression std/mean (compression acceleration)."""
    k = _kama(close, n=10)
    z = _zlema(close, _TD_MON)
    a = _alma(close, w=_TD_MON)
    t = _t3(close, span=_TD_MON)
    w = _wma(close, _TD_MON)
    df = pd.concat([k, z, a, t, w], axis=1)
    mn = df.mean(axis=1).replace(0, np.nan)
    sd = df.std(axis=1)
    compression = _safe_div(sd, mn)
    vel = compression.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rst_extdrv3_024_novel_ma_mean_pct_dist_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of mean-pct-dist-from-5-novel-MAs over 21 days (slope-of-slope)."""
    k = _safe_div(close - _kama(close, n=10), _kama(close, n=10))
    z = _safe_div(close - _zlema(close, _TD_MON), _zlema(close, _TD_MON))
    a = _safe_div(close - _alma(close, w=_TD_MON), _alma(close, w=_TD_MON))
    t = _safe_div(close - _t3(close, span=_TD_MON), _t3(close, span=_TD_MON))
    w = _safe_div(close - _wma(close, _TD_MON), _wma(close, _TD_MON))
    mean_dist = (k + z + a + t + w) / 5.0
    slp = _linslope(mean_dist, _TD_MON)
    return slp.diff(_TD_WEEK)


def rst_extdrv3_025_pct_dist_kama10_slope_21d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21d of the OLS slope of KAMA(10)-distance (curvature of adaptive MA gap)."""
    k = _kama(close, n=10, fast=2, slow=30)
    raw = _safe_div(close - k, k)
    slp1 = _linslope(raw, _TD_MON)
    return _linslope(slp1, _TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

RELATIVE_STRENGTH_EXTENDED_REGISTRY_3RD_DERIVATIVES = {
    "rst_extdrv3_001_pct_dist_kama10_5d_diff_5d_diff": {"inputs": ["close"], "func": rst_extdrv3_001_pct_dist_kama10_5d_diff_5d_diff},
    "rst_extdrv3_002_pct_dist_kama10_21d_diff_5d_diff": {"inputs": ["close"], "func": rst_extdrv3_002_pct_dist_kama10_21d_diff_5d_diff},
    "rst_extdrv3_003_pct_dist_kama21_5d_diff_5d_diff": {"inputs": ["close"], "func": rst_extdrv3_003_pct_dist_kama21_5d_diff_5d_diff},
    "rst_extdrv3_004_kama10_slope_5d_diff_5d_diff": {"inputs": ["close"], "func": rst_extdrv3_004_kama10_slope_5d_diff_5d_diff},
    "rst_extdrv3_005_pct_dist_kama10_slope_21d_5d_diff": {"inputs": ["close"], "func": rst_extdrv3_005_pct_dist_kama10_slope_21d_5d_diff},
    "rst_extdrv3_006_pct_dist_vwma21_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": rst_extdrv3_006_pct_dist_vwma21_21d_diff_5d_diff},
    "rst_extdrv3_007_pct_dist_vwma63_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": rst_extdrv3_007_pct_dist_vwma63_5d_diff_5d_diff},
    "rst_extdrv3_008_vwma21_vs_sma21_spread_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": rst_extdrv3_008_vwma21_vs_sma21_spread_5d_diff_5d_diff},
    "rst_extdrv3_009_pct_dist_vwma21_slope_21d_5d_diff": {"inputs": ["close", "volume"], "func": rst_extdrv3_009_pct_dist_vwma21_slope_21d_5d_diff},
    "rst_extdrv3_010_vwma63_vs_sma63_spread_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": rst_extdrv3_010_vwma63_vs_sma63_spread_21d_diff_5d_diff},
    "rst_extdrv3_011_pct_dist_wma21_5d_diff_5d_diff": {"inputs": ["close"], "func": rst_extdrv3_011_pct_dist_wma21_5d_diff_5d_diff},
    "rst_extdrv3_012_pct_dist_wma50_5d_diff_5d_diff": {"inputs": ["close"], "func": rst_extdrv3_012_pct_dist_wma50_5d_diff_5d_diff},
    "rst_extdrv3_013_pct_dist_zlema21_5d_diff_5d_diff": {"inputs": ["close"], "func": rst_extdrv3_013_pct_dist_zlema21_5d_diff_5d_diff},
    "rst_extdrv3_014_pct_dist_alma21_5d_diff_5d_diff": {"inputs": ["close"], "func": rst_extdrv3_014_pct_dist_alma21_5d_diff_5d_diff},
    "rst_extdrv3_015_pct_dist_t3_21_5d_diff_5d_diff": {"inputs": ["close"], "func": rst_extdrv3_015_pct_dist_t3_21_5d_diff_5d_diff},
    "rst_extdrv3_016_pct_dist_frama16_5d_diff_5d_diff": {"inputs": ["close"], "func": rst_extdrv3_016_pct_dist_frama16_5d_diff_5d_diff},
    "rst_extdrv3_017_pos_in_sma21_band_2_5d_diff_5d_diff": {"inputs": ["close"], "func": rst_extdrv3_017_pos_in_sma21_band_2_5d_diff_5d_diff},
    "rst_extdrv3_018_pos_in_sma200_band_10_5d_diff_5d_diff": {"inputs": ["close"], "func": rst_extdrv3_018_pos_in_sma200_band_10_5d_diff_5d_diff},
    "rst_extdrv3_019_pos_in_ema21_band_2_slope_21d_5d_diff": {"inputs": ["close"], "func": rst_extdrv3_019_pos_in_ema21_band_2_slope_21d_5d_diff},
    "rst_extdrv3_020_novel_ma_agreement_score_5d_diff_5d_diff": {"inputs": ["close"], "func": rst_extdrv3_020_novel_ma_agreement_score_5d_diff_5d_diff},
    "rst_extdrv3_021_novel_ma_mean_pct_dist_21d_diff_5d_diff": {"inputs": ["close"], "func": rst_extdrv3_021_novel_ma_mean_pct_dist_21d_diff_5d_diff},
    "rst_extdrv3_022_novel_ma_sum_depth_21d_diff_5d_diff": {"inputs": ["close"], "func": rst_extdrv3_022_novel_ma_sum_depth_21d_diff_5d_diff},
    "rst_extdrv3_023_novel_ma_std_pct_mean_5d_diff_5d_diff": {"inputs": ["close"], "func": rst_extdrv3_023_novel_ma_std_pct_mean_5d_diff_5d_diff},
    "rst_extdrv3_024_novel_ma_mean_pct_dist_slope_21d_5d_diff": {"inputs": ["close"], "func": rst_extdrv3_024_novel_ma_mean_pct_dist_slope_21d_5d_diff},
    "rst_extdrv3_025_pct_dist_kama10_slope_21d_slope_21d": {"inputs": ["close"], "func": rst_extdrv3_025_pct_dist_kama10_slope_21d_slope_21d},
}
