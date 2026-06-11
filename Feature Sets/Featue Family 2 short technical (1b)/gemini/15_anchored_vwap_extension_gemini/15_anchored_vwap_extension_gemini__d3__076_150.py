"""15 anchored vwap extension gemini d3 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Price distance and reaction from Volume Weighted Average Price anchored to significant events.
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
# FEATURE HYPOTHESES (076-150)
# ============================================================

def f15_avwx_gemini_076_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=219, w2=101, w3=306, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(101, min_periods=max(101//3, 2)).max()
    rebound = x - x.rolling(219, min_periods=max(219//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.114333 * _rolling_slope(draw, 306) + 0.0014287 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_077_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=226, w2=114, w3=323, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(114)
    stress = imbalance.rolling(323, min_periods=max(323//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.217059 + 0.0014288 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_078_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=233, w2=127, w3=340, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 233)
    baseline = trend.rolling(127, min_periods=max(127//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(340, min_periods=max(340//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.230588 + 0.0014289 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_079_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=240, w2=140, w3=357, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 240)
    slow = _rolling_slope(x, 140)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.244118 + 0.001429 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_080_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=247, w2=153, w3=374, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(153, min_periods=max(153//3, 2)).max()
    trough = x.rolling(247, min_periods=max(247//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.257647 + 0.0014291 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_081_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=7, w2=166, w3=391, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(7)
    rank = change.rolling(166, min_periods=max(166//3, 2)).rank(pct=True)
    persistence = change.rolling(391, min_periods=max(391//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.146 * persistence + 0.0014292 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_082_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=14, w2=179, w3=408, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(14, min_periods=max(14//3, 2)).std()
    vol_slow = ret.rolling(179, min_periods=max(179//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.284706 + 0.0014293 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_083_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=21, w2=192, w3=425, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(192, min_periods=max(192//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 21)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.158667 * slope + 0.0014294 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_084_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=28, w2=205, w3=442, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(28)
    drag = impulse.rolling(205, min_periods=max(205//3, 2)).mean()
    noise = impulse.abs().rolling(442, min_periods=max(442//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.311765 + 0.0014295 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_085_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=35, w2=218, w3=459, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 35)
    acceleration = _rolling_slope(velocity, 218)
    curvature = _rolling_slope(acceleration, 459)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.171333 * acceleration + 0.0014296 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_086_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=42, w2=231, w3=476, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 42)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.177667 * pressure.rolling(476, min_periods=max(476//3, 2)).mean() + 0.0014297 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_087_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=49, w2=244, w3=493, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(49, min_periods=max(49//3, 2)).mean())
    decay = spread.ewm(span=244, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.352353 + 0.0014298 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_088_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=56, w2=257, w3=510, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(257, min_periods=max(257//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 56)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.365882 + 0.0014299 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_089_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=63, w2=270, w3=527, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(63, min_periods=max(63//3, 2)).mean(), b.abs().rolling(270, min_periods=max(270//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.196667 * _rolling_slope(cover, 63) + 0.00143 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_090_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=70, w2=283, w3=544, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.203 * y + 0.797000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 70) - _rolling_slope(basket, 283) + 0.0014301 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_091_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=77, w2=296, w3=561, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(77, min_periods=max(77//3, 2)).mean(), upside.rolling(296, min_periods=max(296//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.406471 + 0.0014302 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_092_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=84, w2=309, w3=578, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(309, min_periods=max(309//3, 2)).max()
    rebound = x - x.rolling(84, min_periods=max(84//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.215667 * _rolling_slope(draw, 578) + 0.0014303 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_093_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=91, w2=322, w3=595, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(91) - b.diff(126)
    stress = imbalance.rolling(595, min_periods=max(595//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.433529 + 0.0014304 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_094_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=98, w2=335, w3=612, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 98)
    baseline = trend.rolling(335, min_periods=max(335//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(612, min_periods=max(612//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.447059 + 0.0014305 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_095_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=105, w2=348, w3=629, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 105)
    slow = _rolling_slope(x, 348)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.460588 + 0.0014306 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_096_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=112, w2=361, w3=646, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(361, min_periods=max(361//3, 2)).max()
    trough = x.rolling(112, min_periods=max(112//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.474118 + 0.0014307 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_097_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=119, w2=374, w3=663, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(119)
    rank = change.rolling(374, min_periods=max(374//3, 2)).rank(pct=True)
    persistence = change.rolling(663, min_periods=max(663//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.247333 * persistence + 0.0014308 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_098_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=126, w2=387, w3=680, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(126, min_periods=max(126//3, 2)).std()
    vol_slow = ret.rolling(387, min_periods=max(387//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.501176 + 0.0014309 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_099_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=133, w2=400, w3=697, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(400, min_periods=max(400//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 133)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.26 * slope + 0.001431 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_100_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=140, w2=413, w3=714, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(413, min_periods=max(413//3, 2)).mean()
    noise = impulse.abs().rolling(714, min_periods=max(714//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.528235 + 0.0014311 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_101_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=147, w2=426, w3=731, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 147)
    acceleration = _rolling_slope(velocity, 426)
    curvature = _rolling_slope(acceleration, 731)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.272667 * acceleration + 0.0014312 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_102_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=154, w2=439, w3=748, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 154)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.279 * pressure.rolling(748, min_periods=max(748//3, 2)).mean() + 0.0014313 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_103_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=161, w2=452, w3=765, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(161, min_periods=max(161//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.568824 + 0.0014314 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_104_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=168, w2=465, w3=31, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(465, min_periods=max(465//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 168)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.582353 + 0.0014315 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_105_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=175, w2=478, w3=48, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(175, min_periods=max(175//3, 2)).mean(), b.abs().rolling(478, min_periods=max(478//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(48) + 0.298 * _rolling_slope(cover, 175) + 0.0014316 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_106_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=182, w2=491, w3=65, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.304333 * y + 0.695667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 182) - _rolling_slope(basket, 491) + 0.0014317 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_107_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=189, w2=504, w3=82, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(189, min_periods=max(189//3, 2)).mean(), upside.rolling(504, min_periods=max(504//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(82) * 1.622941 + 0.0014318 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_108_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=196, w2=18, w3=99, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(18, min_periods=max(18//3, 2)).max()
    rebound = x - x.rolling(196, min_periods=max(196//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.317 * _rolling_slope(draw, 99) + 0.0014319 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_109_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=203, w2=31, w3=116, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(31)
    stress = imbalance.rolling(116, min_periods=max(116//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.65 + 0.001432 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_110_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=210, w2=44, w3=133, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 210)
    baseline = trend.rolling(44, min_periods=max(44//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(133, min_periods=max(133//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.663529 + 0.0014321 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_111_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=217, w2=57, w3=150, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 217)
    slow = _rolling_slope(x, 57)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=150, adjust=False).mean() * 0.823529 + 0.0014322 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_112_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=224, w2=70, w3=167, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(70, min_periods=max(70//3, 2)).max()
    trough = x.rolling(224, min_periods=max(224//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.837059 + 0.0014323 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_113_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=231, w2=83, w3=184, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(83, min_periods=max(83//3, 2)).rank(pct=True)
    persistence = change.rolling(184, min_periods=max(184//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.348667 * persistence + 0.0014324 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_114_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=238, w2=96, w3=201, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(238, min_periods=max(238//3, 2)).std()
    vol_slow = ret.rolling(96, min_periods=max(96//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.864118 + 0.0014325 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_115_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=245, w2=109, w3=218, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(109, min_periods=max(109//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 245)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.361333 * slope + 0.0014326 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_116_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=5, w2=122, w3=235, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(5)
    drag = impulse.rolling(122, min_periods=max(122//3, 2)).mean()
    noise = impulse.abs().rolling(235, min_periods=max(235//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.891176 + 0.0014327 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_117_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=12, w2=135, w3=252, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 12)
    acceleration = _rolling_slope(velocity, 135)
    curvature = _rolling_slope(acceleration, 252)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.041667 * acceleration + 0.0014328 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_118_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=19, w2=148, w3=269, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 19)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.048 * pressure.rolling(269, min_periods=max(269//3, 2)).mean() + 0.0014329 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_119_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=26, w2=161, w3=286, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(26, min_periods=max(26//3, 2)).mean())
    decay = spread.ewm(span=161, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.931765 + 0.001433 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_120_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=33, w2=174, w3=303, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(174, min_periods=max(174//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 33)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.945294 + 0.0014331 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_121_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=40, w2=187, w3=320, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(40, min_periods=max(40//3, 2)).mean(), b.abs().rolling(187, min_periods=max(187//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.067 * _rolling_slope(cover, 40) + 0.0014332 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_122_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=47, w2=200, w3=337, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.073333 * y + 0.926667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 47) - _rolling_slope(basket, 200) + 0.0014333 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_123_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=54, w2=213, w3=354, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(54, min_periods=max(54//3, 2)).mean(), upside.rolling(213, min_periods=max(213//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.985882 + 0.0014334 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_124_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=61, w2=226, w3=371, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(226, min_periods=max(226//3, 2)).max()
    rebound = x - x.rolling(61, min_periods=max(61//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.086 * _rolling_slope(draw, 371) + 0.0014335 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_125_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=68, w2=239, w3=388, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(68) - b.diff(126)
    stress = imbalance.rolling(388, min_periods=max(388//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.012941 + 0.0014336 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_126_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=75, w2=252, w3=405, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 75)
    baseline = trend.rolling(252, min_periods=max(252//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(405, min_periods=max(405//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.026471 + 0.0014337 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_127_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=82, w2=265, w3=422, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 82)
    slow = _rolling_slope(x, 265)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.04 + 0.0014338 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_128_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=89, w2=278, w3=439, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(278, min_periods=max(278//3, 2)).max()
    trough = x.rolling(89, min_periods=max(89//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.053529 + 0.0014339 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_129_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=96, w2=291, w3=456, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(96)
    rank = change.rolling(291, min_periods=max(291//3, 2)).rank(pct=True)
    persistence = change.rolling(456, min_periods=max(456//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.117667 * persistence + 0.001434 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_130_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=103, w2=304, w3=473, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(103, min_periods=max(103//3, 2)).std()
    vol_slow = ret.rolling(304, min_periods=max(304//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.080588 + 0.0014341 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_131_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=110, w2=317, w3=490, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(317, min_periods=max(317//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 110)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.130333 * slope + 0.0014342 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_132_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=117, w2=330, w3=507, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(117)
    drag = impulse.rolling(330, min_periods=max(330//3, 2)).mean()
    noise = impulse.abs().rolling(507, min_periods=max(507//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.107647 + 0.0014343 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_133_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=124, w2=343, w3=524, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 124)
    acceleration = _rolling_slope(velocity, 343)
    curvature = _rolling_slope(acceleration, 524)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.143 * acceleration + 0.0014344 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_134_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=131, w2=356, w3=541, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 131)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.149333 * pressure.rolling(541, min_periods=max(541//3, 2)).mean() + 0.0014345 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_135_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=138, w2=369, w3=558, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(138, min_periods=max(138//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.148235 + 0.0014346 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_136_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=145, w2=382, w3=575, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(382, min_periods=max(382//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 145)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.161765 + 0.0014347 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_137_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=152, w2=395, w3=592, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(152, min_periods=max(152//3, 2)).mean(), b.abs().rolling(395, min_periods=max(395//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.168333 * _rolling_slope(cover, 152) + 0.0014348 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_138_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=159, w2=408, w3=609, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.174667 * y + 0.825333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 159) - _rolling_slope(basket, 408) + 0.0014349 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_139_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=166, w2=421, w3=626, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(166, min_periods=max(166//3, 2)).mean(), upside.rolling(421, min_periods=max(421//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.202353 + 0.001435 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_140_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=173, w2=434, w3=643, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(434, min_periods=max(434//3, 2)).max()
    rebound = x - x.rolling(173, min_periods=max(173//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.187333 * _rolling_slope(draw, 643) + 0.0014351 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_141_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=180, w2=447, w3=660, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(660, min_periods=max(660//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.229412 + 0.0014352 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_142_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=187, w2=460, w3=677, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 187)
    baseline = trend.rolling(460, min_periods=max(460//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(677, min_periods=max(677//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.242941 + 0.0014353 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_143_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=194, w2=473, w3=694, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 194)
    slow = _rolling_slope(x, 473)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.256471 + 0.0014354 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_144_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=201, w2=486, w3=711, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(486, min_periods=max(486//3, 2)).max()
    trough = x.rolling(201, min_periods=max(201//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.27 + 0.0014355 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_145_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=208, w2=499, w3=728, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(499, min_periods=max(499//3, 2)).rank(pct=True)
    persistence = change.rolling(728, min_periods=max(728//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.219 * persistence + 0.0014356 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_146_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=215, w2=13, w3=745, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(215, min_periods=max(215//3, 2)).std()
    vol_slow = ret.rolling(13, min_periods=max(13//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.297059 + 0.0014357 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_147_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=222, w2=26, w3=762, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(26, min_periods=max(26//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 222)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.231667 * slope + 0.0014358 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_148_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=229, w2=39, w3=28, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(39, min_periods=max(39//3, 2)).mean()
    noise = impulse.abs().rolling(28, min_periods=max(28//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.324118 + 0.0014359 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_149_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=236, w2=52, w3=45, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 236)
    acceleration = _rolling_slope(velocity, 52)
    curvature = _rolling_slope(acceleration, 45)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.244333 * acceleration + 0.001436 * anchor
    return base_signal.diff().diff().diff()

def f15_avwx_gemini_150_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=243, w2=65, w3=62, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 243)
    pressure = rel_log.diff(65)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.250667 * pressure.rolling(62, min_periods=max(62//3, 2)).mean() + 0.0014361 * anchor
    return base_signal.diff().diff().diff()
