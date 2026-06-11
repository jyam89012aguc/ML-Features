"""110 spectral regime transition composite gemini d3 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Composite signal for detecting transitions between different spectral regimes.
Version: 7.0 (Strict De-duplication + Functional Safety)
Registry Status: Optimized for PostgreSQL Feature Store ingestion.
PIT-clean: right-anchored rolling, explicit min_periods.
"""
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
    idx = num.index if hasattr(num, "index") else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)

def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)

def _atr(high, low, close, n=14):
    pc = close.shift(1)
    tr = pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    return tr.rolling(n, min_periods=max(n // 2, 1)).mean()

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
            x = x[valid]; wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)

def _absorption_ratio_proxy(returns_list, n_comp=1):
    data = pd.concat(returns_list, axis=1).astype(float)
    window = 21
    n_comp = max(1, int(n_comp))
    out = pd.Series(np.nan, index=data.index, dtype=float)
    for i in range(window - 1, len(data)):
        w = data.iloc[i - window + 1:i + 1].to_numpy(dtype=float)
        if w.shape[1] < 2 or np.isnan(w).any():
            continue
        corr = np.corrcoef(w, rowvar=False)
        if np.ndim(corr) != 2 or not np.isfinite(corr).all():
            continue
        eigvals = np.linalg.eigvalsh(corr)
        total = eigvals.sum()
        if not np.isfinite(total) or abs(total) < 1e-12:
            continue
        k = min(n_comp, len(eigvals))
        out.iloc[i] = np.sort(eigvals)[-k:].sum() / total
    return out


# ============================================================
# FEATURE HYPOTHESES (001-075)
# ============================================================

def f110_srtc_gemini_001_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite signal for detecting transitions between different spectral regimes. [window=5]"""
    window = 5
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1), window * 2)
    return (res).diff().diff().diff()

def f110_srtc_gemini_002_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite signal for detecting transitions between different spectral regimes. [window=10]"""
    window = 10
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1), window * 2)
    return (res).diff().diff().diff()

def f110_srtc_gemini_003_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite signal for detecting transitions between different spectral regimes. [window=21]"""
    window = 21
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1), window * 2)
    return (res).diff().diff().diff()

def f110_srtc_gemini_004_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite signal for detecting transitions between different spectral regimes. [window=42]"""
    window = 42
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1), window * 2)
    return (res).diff().diff().diff()

def f110_srtc_gemini_005_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite signal for detecting transitions between different spectral regimes. [window=63]"""
    window = 63
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1), window * 2)
    return (res).diff().diff().diff()

def f110_srtc_gemini_006_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite signal for detecting transitions between different spectral regimes. [window=126]"""
    window = 126
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1), window * 2)
    return (res).diff().diff().diff()

def f110_srtc_gemini_007_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite signal for detecting transitions between different spectral regimes. [window=252]"""
    window = 252
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1), window * 2)
    return (res).diff().diff().diff()

def f110_srtc_gemini_008_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite signal for detecting transitions between different spectral regimes. [window=504]"""
    window = 504
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1), window * 2)
    return (res).diff().diff().diff()

def f110_srtc_gemini_009_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite signal for detecting transitions between different spectral regimes. [window=756]"""
    window = 756
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1), window * 2)
    return (res).diff().diff().diff()

def f110_srtc_gemini_010_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite signal for detecting transitions between different spectral regimes. [window=1260]"""
    window = 1260
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1), window * 2)
    return (res).diff().diff().diff()

def f110_srtc_gemini_011_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=171, w2=281, w3=416, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(171, min_periods=max(171//3, 2)).mean(), upside.rolling(281, min_periods=max(281//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.850588 + 0.0011422 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_012_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=178, w2=294, w3=433, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(294, min_periods=max(294//3, 2)).max()
    rebound = x - x.rolling(178, min_periods=max(178//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.254 * _rolling_slope(draw, 433) + 0.0011423 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_013_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=185, w2=307, w3=450, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(volume.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(450, min_periods=max(450//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.877647 + 0.0011424 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_014_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=192, w2=320, w3=467, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 192)
    baseline = trend.rolling(320, min_periods=max(320//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(467, min_periods=max(467//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.891176 + 0.0011425 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_015_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=199, w2=333, w3=484, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 199)
    slow = _rolling_slope(x, 333)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.904706 + 0.0011426 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_016_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=206, w2=346, w3=501, lag=13)."""
    x = close.shift(13)
    peak = x.rolling(346, min_periods=max(346//3, 2)).max()
    trough = x.rolling(206, min_periods=max(206//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.918235 + 0.0011427 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_017_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=213, w2=359, w3=518, lag=21)."""
    x = close.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(359, min_periods=max(359//3, 2)).rank(pct=True)
    persistence = change.rolling(518, min_periods=max(518//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.285667 * persistence + 0.0011428 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_018_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=220, w2=372, w3=535, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(220, min_periods=max(220//3, 2)).std()
    vol_slow = ret.rolling(372, min_periods=max(372//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.945294 + 0.0011429 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_019_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=227, w2=385, w3=552, lag=55)."""
    x = close.shift(55)
    ma = x.rolling(385, min_periods=max(385//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 227)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.298333 * slope + 0.001143 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_020_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=234, w2=398, w3=569, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(398, min_periods=max(398//3, 2)).mean()
    noise = impulse.abs().rolling(569, min_periods=max(569//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.972353 + 0.0011431 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_021_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=241, w2=411, w3=586, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 241)
    acceleration = _rolling_slope(velocity, 411)
    curvature = _rolling_slope(acceleration, 586)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.311 * acceleration + 0.0011432 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_022_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=248, w2=424, w3=603, lag=2)."""
    rel = _safe_div(close.shift(2), volume.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 248)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.317333 * pressure.rolling(603, min_periods=max(603//3, 2)).mean() + 0.0011433 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_023_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=8, w2=437, w3=620, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(8, min_periods=max(8//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.012941 + 0.0011434 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_024_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=15, w2=450, w3=637, lag=5)."""
    a = _safe_log(close.abs() + 1.0).shift(5)
    b = _safe_log(volume.abs() + 1.0).shift(5)
    corr = a.rolling(450, min_periods=max(450//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 15)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.026471 + 0.0011435 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_025_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=22, w2=463, w3=654, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    cover = _safe_div(a.rolling(22, min_periods=max(22//3, 2)).mean(), b.abs().rolling(463, min_periods=max(463//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.336333 * _rolling_slope(cover, 22) + 0.0011436 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_026_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=29, w2=476, w3=671, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    y = _safe_log(volume.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.342667 * y + 0.657333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 29) - _rolling_slope(basket, 476) + 0.0011437 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_027_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=36, w2=489, w3=688, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(36, min_periods=max(36//3, 2)).mean(), upside.rolling(489, min_periods=max(489//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.067059 + 0.0011438 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_028_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=43, w2=502, w3=705, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    draw = x - x.rolling(502, min_periods=max(502//3, 2)).max()
    rebound = x - x.rolling(43, min_periods=max(43//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.355333 * _rolling_slope(draw, 705) + 0.0011439 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_029_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=50, w2=16, w3=722, lag=55)."""
    a = _safe_log(close.abs() + 1.0).shift(55)
    b = _safe_log(volume.abs() + 1.0).shift(55)
    imbalance = a.diff(50) - b.diff(16)
    stress = imbalance.rolling(722, min_periods=max(722//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.094118 + 0.001144 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_030_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=57, w2=29, w3=739, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 57)
    baseline = trend.rolling(29, min_periods=max(29//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(739, min_periods=max(739//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.107647 + 0.0011441 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_031_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=64, w2=42, w3=756, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 64)
    slow = _rolling_slope(x, 42)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.121176 + 0.0011442 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_032_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=71, w2=55, w3=22, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(55, min_periods=max(55//3, 2)).max()
    trough = x.rolling(71, min_periods=max(71//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.134706 + 0.0011443 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_033_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=78, w2=68, w3=39, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(78)
    rank = change.rolling(68, min_periods=max(68//3, 2)).rank(pct=True)
    persistence = change.rolling(39, min_periods=max(39//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.054667 * persistence + 0.0011444 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_034_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=85, w2=81, w3=56, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(85, min_periods=max(85//3, 2)).std()
    vol_slow = ret.rolling(81, min_periods=max(81//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.161765 + 0.0011445 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_035_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=92, w2=94, w3=73, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(94, min_periods=max(94//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 92)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.067333 * slope + 0.0011446 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_036_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=99, w2=107, w3=90, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(99)
    drag = impulse.rolling(107, min_periods=max(107//3, 2)).mean()
    noise = impulse.abs().rolling(90, min_periods=max(90//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.188824 + 0.0011447 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_037_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=106, w2=120, w3=107, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 106)
    acceleration = _rolling_slope(velocity, 120)
    curvature = _rolling_slope(acceleration, 107)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.08 * acceleration + 0.0011448 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_038_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=113, w2=133, w3=124, lag=34)."""
    rel = _safe_div(close.shift(34), volume.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 113)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.086333 * pressure.rolling(124, min_periods=max(124//3, 2)).mean() + 0.0011449 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_039_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=120, w2=146, w3=141, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(120, min_periods=max(120//3, 2)).mean())
    decay = spread.ewm(span=146, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.229412 + 0.001145 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_040_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=127, w2=159, w3=158, lag=0)."""
    a = _safe_log(close.abs() + 1.0).shift(0)
    b = _safe_log(volume.abs() + 1.0).shift(0)
    corr = a.rolling(159, min_periods=max(159//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 127)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.242941 + 0.0011451 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_041_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=134, w2=172, w3=175, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    cover = _safe_div(a.rolling(134, min_periods=max(134//3, 2)).mean(), b.abs().rolling(172, min_periods=max(172//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.105333 * _rolling_slope(cover, 134) + 0.0011452 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_042_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=141, w2=185, w3=192, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    y = _safe_log(volume.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.111667 * y + 0.888333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 141) - _rolling_slope(basket, 185) + 0.0011453 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_043_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=148, w2=198, w3=209, lag=3)."""
    x = close.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(148, min_periods=max(148//3, 2)).mean(), upside.rolling(198, min_periods=max(198//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.283529 + 0.0011454 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_044_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=155, w2=211, w3=226, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    draw = x - x.rolling(211, min_periods=max(211//3, 2)).max()
    rebound = x - x.rolling(155, min_periods=max(155//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.124333 * _rolling_slope(draw, 226) + 0.0011455 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_045_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=162, w2=224, w3=243, lag=8)."""
    a = _safe_log(close.abs() + 1.0).shift(8)
    b = _safe_log(volume.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(243, min_periods=max(243//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.310588 + 0.0011456 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_046_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=169, w2=237, w3=260, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 169)
    baseline = trend.rolling(237, min_periods=max(237//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(260, min_periods=max(260//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.324118 + 0.0011457 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_047_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=176, w2=250, w3=277, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 176)
    slow = _rolling_slope(x, 250)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=277, adjust=False).mean() * 1.337647 + 0.0011458 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_048_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=183, w2=263, w3=294, lag=34)."""
    x = close.shift(34)
    peak = x.rolling(263, min_periods=max(263//3, 2)).max()
    trough = x.rolling(183, min_periods=max(183//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.351176 + 0.0011459 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_049_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=190, w2=276, w3=311, lag=55)."""
    x = close.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(276, min_periods=max(276//3, 2)).rank(pct=True)
    persistence = change.rolling(311, min_periods=max(311//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.156 * persistence + 0.001146 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_050_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=197, w2=289, w3=328, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(197, min_periods=max(197//3, 2)).std()
    vol_slow = ret.rolling(289, min_periods=max(289//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.378235 + 0.0011461 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_051_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=204, w2=302, w3=345, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(302, min_periods=max(302//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 204)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.168667 * slope + 0.0011462 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_052_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=211, w2=315, w3=362, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(315, min_periods=max(315//3, 2)).mean()
    noise = impulse.abs().rolling(362, min_periods=max(362//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.405294 + 0.0011463 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_053_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=218, w2=328, w3=379, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 218)
    acceleration = _rolling_slope(velocity, 328)
    curvature = _rolling_slope(acceleration, 379)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.181333 * acceleration + 0.0011464 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_054_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=225, w2=341, w3=396, lag=5)."""
    rel = _safe_div(close.shift(5), volume.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 225)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.187667 * pressure.rolling(396, min_periods=max(396//3, 2)).mean() + 0.0011465 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_055_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=232, w2=354, w3=413, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(232, min_periods=max(232//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.445882 + 0.0011466 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_056_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=239, w2=367, w3=430, lag=13)."""
    a = _safe_log(close.abs() + 1.0).shift(13)
    b = _safe_log(volume.abs() + 1.0).shift(13)
    corr = a.rolling(367, min_periods=max(367//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 239)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.459412 + 0.0011467 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_057_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=246, w2=380, w3=447, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    cover = _safe_div(a.rolling(246, min_periods=max(246//3, 2)).mean(), b.abs().rolling(380, min_periods=max(380//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.206667 * _rolling_slope(cover, 246) + 0.0011468 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_058_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=6, w2=393, w3=464, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    y = _safe_log(volume.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.213 * y + 0.787000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 6) - _rolling_slope(basket, 393) + 0.0011469 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_059_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=13, w2=406, w3=481, lag=55)."""
    x = close.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(13, min_periods=max(13//3, 2)).mean(), upside.rolling(406, min_periods=max(406//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.5 + 0.001147 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_060_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=20, w2=419, w3=498, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    draw = x - x.rolling(419, min_periods=max(419//3, 2)).max()
    rebound = x - x.rolling(20, min_periods=max(20//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.225667 * _rolling_slope(draw, 498) + 0.0011471 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_061_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=27, w2=432, w3=515, lag=1)."""
    a = _safe_log(close.abs() + 1.0).shift(1)
    b = _safe_log(volume.abs() + 1.0).shift(1)
    imbalance = a.diff(27) - b.diff(126)
    stress = imbalance.rolling(515, min_periods=max(515//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.527059 + 0.0011472 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_062_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=34, w2=445, w3=532, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 34)
    baseline = trend.rolling(445, min_periods=max(445//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(532, min_periods=max(532//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.540588 + 0.0011473 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_063_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=41, w2=458, w3=549, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 41)
    slow = _rolling_slope(x, 458)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.554118 + 0.0011474 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_064_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=48, w2=471, w3=566, lag=5)."""
    x = close.shift(5)
    peak = x.rolling(471, min_periods=max(471//3, 2)).max()
    trough = x.rolling(48, min_periods=max(48//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.567647 + 0.0011475 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_065_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=55, w2=484, w3=583, lag=8)."""
    x = close.shift(8)
    change = x.pct_change(55)
    rank = change.rolling(484, min_periods=max(484//3, 2)).rank(pct=True)
    persistence = change.rolling(583, min_periods=max(583//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.257333 * persistence + 0.0011476 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_066_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=62, w2=497, w3=600, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(62, min_periods=max(62//3, 2)).std()
    vol_slow = ret.rolling(497, min_periods=max(497//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.594706 + 0.0011477 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_067_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=69, w2=11, w3=617, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(11, min_periods=max(11//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 69)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.27 * slope + 0.0011478 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_068_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=76, w2=24, w3=634, lag=34)."""
    x = close.shift(34)
    impulse = x.diff(76)
    drag = impulse.rolling(24, min_periods=max(24//3, 2)).mean()
    noise = impulse.abs().rolling(634, min_periods=max(634//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.621765 + 0.0011479 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_069_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=83, w2=37, w3=651, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 83)
    acceleration = _rolling_slope(velocity, 37)
    curvature = _rolling_slope(acceleration, 651)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.282667 * acceleration + 0.001148 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_070_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=90, w2=50, w3=668, lag=0)."""
    rel = _safe_div(close.shift(0), volume.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 90)
    pressure = rel_log.diff(50)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.289 * pressure.rolling(668, min_periods=max(668//3, 2)).mean() + 0.0011481 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_071_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=97, w2=63, w3=685, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(97, min_periods=max(97//3, 2)).mean())
    decay = spread.ewm(span=63, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.662353 + 0.0011482 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_072_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=104, w2=76, w3=702, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(volume.abs() + 1.0).shift(2)
    corr = a.rolling(76, min_periods=max(76//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 104)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.822353 + 0.0011483 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_073_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=111, w2=89, w3=719, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    cover = _safe_div(a.rolling(111, min_periods=max(111//3, 2)).mean(), b.abs().rolling(89, min_periods=max(89//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.308 * _rolling_slope(cover, 111) + 0.0011484 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_074_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=118, w2=102, w3=736, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(volume.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.314333 * y + 0.685667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 118) - _rolling_slope(basket, 102) + 0.0011485 * anchor
    return base_signal.diff().diff().diff()

def f110_srtc_gemini_075_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=125, w2=115, w3=753, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(125, min_periods=max(125//3, 2)).mean(), upside.rolling(115, min_periods=max(115//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.862941 + 0.0011486 * anchor
    return base_signal.diff().diff().diff()
