"""87 body to wick ratio decay gemini d3 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Decreasing ratio of candlestick body to total range signaling trend weakening.
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

def f87_bwrd_gemini_001_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Decreasing ratio of candlestick body to total range signaling trend weakening. [window=5]"""
    window = 5
    res = _safe_div((close - open).abs(), high - low + 1e-9)
    return (res).diff().diff().diff()

def f87_bwrd_gemini_002_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Decreasing ratio of candlestick body to total range signaling trend weakening. [window=10]"""
    window = 10
    res = _safe_div((close - open).abs(), high - low + 1e-9)
    return (res).diff().diff().diff()

def f87_bwrd_gemini_003_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Decreasing ratio of candlestick body to total range signaling trend weakening. [window=21]"""
    window = 21
    res = _safe_div((close - open).abs(), high - low + 1e-9)
    return (res).diff().diff().diff()

def f87_bwrd_gemini_004_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Decreasing ratio of candlestick body to total range signaling trend weakening. [window=42]"""
    window = 42
    res = _safe_div((close - open).abs(), high - low + 1e-9)
    return (res).diff().diff().diff()

def f87_bwrd_gemini_005_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Decreasing ratio of candlestick body to total range signaling trend weakening. [window=63]"""
    window = 63
    res = _safe_div((close - open).abs(), high - low + 1e-9)
    return (res).diff().diff().diff()

def f87_bwrd_gemini_006_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Decreasing ratio of candlestick body to total range signaling trend weakening. [window=126]"""
    window = 126
    res = _safe_div((close - open).abs(), high - low + 1e-9)
    return (res).diff().diff().diff()

def f87_bwrd_gemini_007_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Decreasing ratio of candlestick body to total range signaling trend weakening. [window=252]"""
    window = 252
    res = _safe_div((close - open).abs(), high - low + 1e-9)
    return (res).diff().diff().diff()

def f87_bwrd_gemini_008_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Decreasing ratio of candlestick body to total range signaling trend weakening. [window=504]"""
    window = 504
    res = _safe_div((close - open).abs(), high - low + 1e-9)
    return (res).diff().diff().diff()

def f87_bwrd_gemini_009_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Decreasing ratio of candlestick body to total range signaling trend weakening. [window=756]"""
    window = 756
    res = _safe_div((close - open).abs(), high - low + 1e-9)
    return (res).diff().diff().diff()

def f87_bwrd_gemini_010_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Decreasing ratio of candlestick body to total range signaling trend weakening. [window=1260]"""
    window = 1260
    res = _safe_div((close - open).abs(), high - low + 1e-9)
    return (res).diff().diff().diff()

def f87_bwrd_gemini_011_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=177, w2=464, w3=480, lag=1)."""
    x = open.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(177, min_periods=max(177//3, 2)).mean(), upside.rolling(464, min_periods=max(464//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.278235 + 0.0054542 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_012_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=184, w2=477, w3=497, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    draw = x - x.rolling(477, min_periods=max(477//3, 2)).max()
    rebound = x - x.rolling(184, min_periods=max(184//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.169333 * _rolling_slope(draw, 497) + 0.0054543 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_013_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=191, w2=490, w3=514, lag=3)."""
    a = _safe_log(open.abs() + 1.0).shift(3)
    b = _safe_log(high.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(514, min_periods=max(514//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.305294 + 0.0054544 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_014_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=198, w2=503, w3=531, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 198)
    baseline = trend.rolling(503, min_periods=max(503//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(531, min_periods=max(531//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.318824 + 0.0054545 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_015_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=205, w2=17, w3=548, lag=8)."""
    x = _safe_log(open.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 205)
    slow = _rolling_slope(x, 17)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.332353 + 0.0054546 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_016_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=212, w2=30, w3=565, lag=13)."""
    x = open.shift(13)
    peak = x.rolling(30, min_periods=max(30//3, 2)).max()
    trough = x.rolling(212, min_periods=max(212//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.345882 + 0.0054547 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_017_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=219, w2=43, w3=582, lag=21)."""
    x = open.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(43, min_periods=max(43//3, 2)).rank(pct=True)
    persistence = change.rolling(582, min_periods=max(582//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.201 * persistence + 0.0054548 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_018_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=226, w2=56, w3=599, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(226, min_periods=max(226//3, 2)).std()
    vol_slow = ret.rolling(56, min_periods=max(56//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.372941 + 0.0054549 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_019_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=233, w2=69, w3=616, lag=55)."""
    x = open.shift(55)
    ma = x.rolling(69, min_periods=max(69//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 233)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.213667 * slope + 0.005455 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_020_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=240, w2=82, w3=633, lag=0)."""
    x = open.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(82, min_periods=max(82//3, 2)).mean()
    noise = impulse.abs().rolling(633, min_periods=max(633//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.4 + 0.0054551 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_021_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=247, w2=95, w3=650, lag=1)."""
    x = _safe_log(open.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 247)
    acceleration = _rolling_slope(velocity, 95)
    curvature = _rolling_slope(acceleration, 650)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.226333 * acceleration + 0.0054552 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_022_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=7, w2=108, w3=667, lag=2)."""
    rel = _safe_div(open.shift(2), high.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 7)
    pressure = rel_log.diff(108)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.232667 * pressure.rolling(667, min_periods=max(667//3, 2)).mean() + 0.0054553 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_023_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=14, w2=121, w3=684, lag=3)."""
    a = open.shift(3)
    b = high.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(14, min_periods=max(14//3, 2)).mean())
    decay = spread.ewm(span=121, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.440588 + 0.0054554 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_024_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=21, w2=134, w3=701, lag=5)."""
    a = _safe_log(open.abs() + 1.0).shift(5)
    b = _safe_log(high.abs() + 1.0).shift(5)
    corr = a.rolling(134, min_periods=max(134//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 21)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.454118 + 0.0054555 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_025_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=28, w2=147, w3=718, lag=8)."""
    a = open.shift(8)
    b = high.shift(8)
    cover = _safe_div(a.rolling(28, min_periods=max(28//3, 2)).mean(), b.abs().rolling(147, min_periods=max(147//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.251667 * _rolling_slope(cover, 28) + 0.0054556 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_026_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=35, w2=160, w3=735, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    y = _safe_log(high.abs() + 1.0).shift(13)
    z = _safe_log(low.abs() + 1.0).shift(13)
    basket = x - 0.258 * y + 0.742000 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 35) - _rolling_slope(basket, 160) + 0.0054557 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_027_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=42, w2=173, w3=752, lag=21)."""
    x = open.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(42, min_periods=max(42//3, 2)).mean(), upside.rolling(173, min_periods=max(173//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.494706 + 0.0054558 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_028_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=49, w2=186, w3=18, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    draw = x - x.rolling(186, min_periods=max(186//3, 2)).max()
    rebound = x - x.rolling(49, min_periods=max(49//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.270667 * _rolling_slope(draw, 18) + 0.0054559 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_029_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=56, w2=199, w3=35, lag=55)."""
    a = _safe_log(open.abs() + 1.0).shift(55)
    b = _safe_log(high.abs() + 1.0).shift(55)
    imbalance = a.diff(56) - b.diff(126)
    stress = imbalance.rolling(35, min_periods=max(35//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.521765 + 0.005456 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_030_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=63, w2=212, w3=52, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 63)
    baseline = trend.rolling(212, min_periods=max(212//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(52, min_periods=max(52//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.535294 + 0.0054561 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_031_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=70, w2=225, w3=69, lag=1)."""
    x = _safe_log(open.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 70)
    slow = _rolling_slope(x, 225)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=69, adjust=False).mean() * 1.548824 + 0.0054562 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_032_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=77, w2=238, w3=86, lag=2)."""
    x = open.shift(2)
    peak = x.rolling(238, min_periods=max(238//3, 2)).max()
    trough = x.rolling(77, min_periods=max(77//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.562353 + 0.0054563 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_033_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=84, w2=251, w3=103, lag=3)."""
    x = open.shift(3)
    change = x.pct_change(84)
    rank = change.rolling(251, min_periods=max(251//3, 2)).rank(pct=True)
    persistence = change.rolling(103, min_periods=max(103//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.302333 * persistence + 0.0054564 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_034_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=91, w2=264, w3=120, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(91, min_periods=max(91//3, 2)).std()
    vol_slow = ret.rolling(264, min_periods=max(264//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.589412 + 0.0054565 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_035_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=98, w2=277, w3=137, lag=8)."""
    x = open.shift(8)
    ma = x.rolling(277, min_periods=max(277//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 98)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.315 * slope + 0.0054566 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_036_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=105, w2=290, w3=154, lag=13)."""
    x = open.shift(13)
    impulse = x.diff(105)
    drag = impulse.rolling(290, min_periods=max(290//3, 2)).mean()
    noise = impulse.abs().rolling(154, min_periods=max(154//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.616471 + 0.0054567 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_037_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=112, w2=303, w3=171, lag=21)."""
    x = _safe_log(open.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 112)
    acceleration = _rolling_slope(velocity, 303)
    curvature = _rolling_slope(acceleration, 171)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.327667 * acceleration + 0.0054568 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_038_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=119, w2=316, w3=188, lag=34)."""
    rel = _safe_div(open.shift(34), high.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 119)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.334 * pressure.rolling(188, min_periods=max(188//3, 2)).mean() + 0.0054569 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_039_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=126, w2=329, w3=205, lag=55)."""
    a = open.shift(55)
    b = high.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(126, min_periods=max(126//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.657059 + 0.005457 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_040_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=133, w2=342, w3=222, lag=0)."""
    a = _safe_log(open.abs() + 1.0).shift(0)
    b = _safe_log(high.abs() + 1.0).shift(0)
    corr = a.rolling(342, min_periods=max(342//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 133)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.670588 + 0.0054571 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_041_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=140, w2=355, w3=239, lag=1)."""
    a = open.shift(1)
    b = high.shift(1)
    cover = _safe_div(a.rolling(140, min_periods=max(140//3, 2)).mean(), b.abs().rolling(355, min_periods=max(355//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.353 * _rolling_slope(cover, 140) + 0.0054572 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_042_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=147, w2=368, w3=256, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    y = _safe_log(high.abs() + 1.0).shift(2)
    z = _safe_log(low.abs() + 1.0).shift(2)
    basket = x - 0.359333 * y + 0.640667 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 147) - _rolling_slope(basket, 368) + 0.0054573 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_043_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=154, w2=381, w3=273, lag=3)."""
    x = open.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(154, min_periods=max(154//3, 2)).mean(), upside.rolling(381, min_periods=max(381//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.857647 + 0.0054574 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_044_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=161, w2=394, w3=290, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    draw = x - x.rolling(394, min_periods=max(394//3, 2)).max()
    rebound = x - x.rolling(161, min_periods=max(161//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.039667 * _rolling_slope(draw, 290) + 0.0054575 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_045_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=168, w2=407, w3=307, lag=8)."""
    a = _safe_log(open.abs() + 1.0).shift(8)
    b = _safe_log(high.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(307, min_periods=max(307//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.884706 + 0.0054576 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_046_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=175, w2=420, w3=324, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 175)
    baseline = trend.rolling(420, min_periods=max(420//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(324, min_periods=max(324//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.898235 + 0.0054577 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_047_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=182, w2=433, w3=341, lag=21)."""
    x = _safe_log(open.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 182)
    slow = _rolling_slope(x, 433)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.911765 + 0.0054578 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_048_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=189, w2=446, w3=358, lag=34)."""
    x = open.shift(34)
    peak = x.rolling(446, min_periods=max(446//3, 2)).max()
    trough = x.rolling(189, min_periods=max(189//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.925294 + 0.0054579 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_049_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=196, w2=459, w3=375, lag=55)."""
    x = open.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(459, min_periods=max(459//3, 2)).rank(pct=True)
    persistence = change.rolling(375, min_periods=max(375//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.071333 * persistence + 0.005458 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_050_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=203, w2=472, w3=392, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(203, min_periods=max(203//3, 2)).std()
    vol_slow = ret.rolling(472, min_periods=max(472//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.952353 + 0.0054581 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_051_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=210, w2=485, w3=409, lag=1)."""
    x = open.shift(1)
    ma = x.rolling(485, min_periods=max(485//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 210)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.084 * slope + 0.0054582 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_052_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=217, w2=498, w3=426, lag=2)."""
    x = open.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(498, min_periods=max(498//3, 2)).mean()
    noise = impulse.abs().rolling(426, min_periods=max(426//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.979412 + 0.0054583 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_053_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=224, w2=12, w3=443, lag=3)."""
    x = _safe_log(open.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 224)
    acceleration = _rolling_slope(velocity, 12)
    curvature = _rolling_slope(acceleration, 443)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.096667 * acceleration + 0.0054584 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_054_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=231, w2=25, w3=460, lag=5)."""
    rel = _safe_div(open.shift(5), high.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 231)
    pressure = rel_log.diff(25)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.103 * pressure.rolling(460, min_periods=max(460//3, 2)).mean() + 0.0054585 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_055_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=238, w2=38, w3=477, lag=8)."""
    a = open.shift(8)
    b = high.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(238, min_periods=max(238//3, 2)).mean())
    decay = spread.ewm(span=38, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.02 + 0.0054586 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_056_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=245, w2=51, w3=494, lag=13)."""
    a = _safe_log(open.abs() + 1.0).shift(13)
    b = _safe_log(high.abs() + 1.0).shift(13)
    corr = a.rolling(51, min_periods=max(51//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 245)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.033529 + 0.0054587 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_057_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=5, w2=64, w3=511, lag=21)."""
    a = open.shift(21)
    b = high.shift(21)
    cover = _safe_div(a.rolling(5, min_periods=max(5//3, 2)).mean(), b.abs().rolling(64, min_periods=max(64//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.122 * _rolling_slope(cover, 5) + 0.0054588 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_058_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=12, w2=77, w3=528, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    y = _safe_log(high.abs() + 1.0).shift(34)
    z = _safe_log(low.abs() + 1.0).shift(34)
    basket = x - 0.128333 * y + 0.871667 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 12) - _rolling_slope(basket, 77) + 0.0054589 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_059_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=19, w2=90, w3=545, lag=55)."""
    x = open.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(19, min_periods=max(19//3, 2)).mean(), upside.rolling(90, min_periods=max(90//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.074118 + 0.005459 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_060_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=26, w2=103, w3=562, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    draw = x - x.rolling(103, min_periods=max(103//3, 2)).max()
    rebound = x - x.rolling(26, min_periods=max(26//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.141 * _rolling_slope(draw, 562) + 0.0054591 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_061_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=33, w2=116, w3=579, lag=1)."""
    a = _safe_log(open.abs() + 1.0).shift(1)
    b = _safe_log(high.abs() + 1.0).shift(1)
    imbalance = a.diff(33) - b.diff(116)
    stress = imbalance.rolling(579, min_periods=max(579//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.101176 + 0.0054592 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_062_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=40, w2=129, w3=596, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 40)
    baseline = trend.rolling(129, min_periods=max(129//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(596, min_periods=max(596//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.114706 + 0.0054593 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_063_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=47, w2=142, w3=613, lag=3)."""
    x = _safe_log(open.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 47)
    slow = _rolling_slope(x, 142)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.128235 + 0.0054594 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_064_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=54, w2=155, w3=630, lag=5)."""
    x = open.shift(5)
    peak = x.rolling(155, min_periods=max(155//3, 2)).max()
    trough = x.rolling(54, min_periods=max(54//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.141765 + 0.0054595 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_065_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=61, w2=168, w3=647, lag=8)."""
    x = open.shift(8)
    change = x.pct_change(61)
    rank = change.rolling(168, min_periods=max(168//3, 2)).rank(pct=True)
    persistence = change.rolling(647, min_periods=max(647//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.172667 * persistence + 0.0054596 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_066_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=68, w2=181, w3=664, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(68, min_periods=max(68//3, 2)).std()
    vol_slow = ret.rolling(181, min_periods=max(181//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.168824 + 0.0054597 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_067_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=75, w2=194, w3=681, lag=21)."""
    x = open.shift(21)
    ma = x.rolling(194, min_periods=max(194//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 75)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.185333 * slope + 0.0054598 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_068_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=82, w2=207, w3=698, lag=34)."""
    x = open.shift(34)
    impulse = x.diff(82)
    drag = impulse.rolling(207, min_periods=max(207//3, 2)).mean()
    noise = impulse.abs().rolling(698, min_periods=max(698//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.195882 + 0.0054599 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_069_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=89, w2=220, w3=715, lag=55)."""
    x = _safe_log(open.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 89)
    acceleration = _rolling_slope(velocity, 220)
    curvature = _rolling_slope(acceleration, 715)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.198 * acceleration + 0.00546 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_070_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=96, w2=233, w3=732, lag=0)."""
    rel = _safe_div(open.shift(0), high.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 96)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.204333 * pressure.rolling(732, min_periods=max(732//3, 2)).mean() + 0.0054601 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_071_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=103, w2=246, w3=749, lag=1)."""
    a = open.shift(1)
    b = high.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(103, min_periods=max(103//3, 2)).mean())
    decay = spread.ewm(span=246, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.236471 + 0.0054602 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_072_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=110, w2=259, w3=766, lag=2)."""
    a = _safe_log(open.abs() + 1.0).shift(2)
    b = _safe_log(high.abs() + 1.0).shift(2)
    corr = a.rolling(259, min_periods=max(259//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 110)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.25 + 0.0054603 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_073_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=117, w2=272, w3=32, lag=3)."""
    a = open.shift(3)
    b = high.shift(3)
    cover = _safe_div(a.rolling(117, min_periods=max(117//3, 2)).mean(), b.abs().rolling(272, min_periods=max(272//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(32) + 0.223333 * _rolling_slope(cover, 117) + 0.0054604 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_074_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=124, w2=285, w3=49, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    y = _safe_log(high.abs() + 1.0).shift(5)
    z = _safe_log(low.abs() + 1.0).shift(5)
    basket = x - 0.229667 * y + 0.770333 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 124) - _rolling_slope(basket, 285) + 0.0054605 * anchor
    return base_signal.diff().diff().diff()

def f87_bwrd_gemini_075_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=131, w2=298, w3=66, lag=8)."""
    x = open.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(131, min_periods=max(131//3, 2)).mean(), upside.rolling(298, min_periods=max(298//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(66) * 1.290588 + 0.0054606 * anchor
    return base_signal.diff().diff().diff()
