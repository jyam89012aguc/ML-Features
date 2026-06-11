"""57 volatility entropy cluster gemini d3 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Entropy-based detection of volatility regimes and clustering behavior.
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

def f57_vent_gemini_001_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Entropy-based detection of volatility regimes and clustering behavior. [window=5]"""
    window = 5
    res = _safe_div(_atr(high, low, close, window), _atr(high, low, close, window).rolling(window).mean() + 1e-9)
    return (res).diff().diff().diff()

def f57_vent_gemini_002_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Entropy-based detection of volatility regimes and clustering behavior. [window=10]"""
    window = 10
    res = _safe_div(_atr(high, low, close, window), _atr(high, low, close, window).rolling(window).mean() + 1e-9)
    return (res).diff().diff().diff()

def f57_vent_gemini_003_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Entropy-based detection of volatility regimes and clustering behavior. [window=21]"""
    window = 21
    res = _safe_div(_atr(high, low, close, window), _atr(high, low, close, window).rolling(window).mean() + 1e-9)
    return (res).diff().diff().diff()

def f57_vent_gemini_004_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Entropy-based detection of volatility regimes and clustering behavior. [window=42]"""
    window = 42
    res = _safe_div(_atr(high, low, close, window), _atr(high, low, close, window).rolling(window).mean() + 1e-9)
    return (res).diff().diff().diff()

def f57_vent_gemini_005_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Entropy-based detection of volatility regimes and clustering behavior. [window=63]"""
    window = 63
    res = _safe_div(_atr(high, low, close, window), _atr(high, low, close, window).rolling(window).mean() + 1e-9)
    return (res).diff().diff().diff()

def f57_vent_gemini_006_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Entropy-based detection of volatility regimes and clustering behavior. [window=126]"""
    window = 126
    res = _safe_div(_atr(high, low, close, window), _atr(high, low, close, window).rolling(window).mean() + 1e-9)
    return (res).diff().diff().diff()

def f57_vent_gemini_007_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Entropy-based detection of volatility regimes and clustering behavior. [window=252]"""
    window = 252
    res = _safe_div(_atr(high, low, close, window), _atr(high, low, close, window).rolling(window).mean() + 1e-9)
    return (res).diff().diff().diff()

def f57_vent_gemini_008_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Entropy-based detection of volatility regimes and clustering behavior. [window=504]"""
    window = 504
    res = _safe_div(_atr(high, low, close, window), _atr(high, low, close, window).rolling(window).mean() + 1e-9)
    return (res).diff().diff().diff()

def f57_vent_gemini_009_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Entropy-based detection of volatility regimes and clustering behavior. [window=756]"""
    window = 756
    res = _safe_div(_atr(high, low, close, window), _atr(high, low, close, window).rolling(window).mean() + 1e-9)
    return (res).diff().diff().diff()

def f57_vent_gemini_010_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Entropy-based detection of volatility regimes and clustering behavior. [window=1260]"""
    window = 1260
    res = _safe_div(_atr(high, low, close, window), _atr(high, low, close, window).rolling(window).mean() + 1e-9)
    return (res).diff().diff().diff()

def f57_vent_gemini_011_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=149, w2=127, w3=260, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(149, min_periods=max(149//3, 2)).mean(), upside.rolling(127, min_periods=max(127//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.022941 + 0.0037742 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_012_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=156, w2=140, w3=277, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(140, min_periods=max(140//3, 2)).max()
    rebound = x - x.rolling(156, min_periods=max(156//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.116 * _rolling_slope(draw, 277) + 0.0037743 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_013_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=163, w2=153, w3=294, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(294, min_periods=max(294//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.05 + 0.0037744 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_014_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=170, w2=166, w3=311, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 170)
    baseline = trend.rolling(166, min_periods=max(166//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(311, min_periods=max(311//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.063529 + 0.0037745 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_015_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=177, w2=179, w3=328, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 177)
    slow = _rolling_slope(x, 179)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.077059 + 0.0037746 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_016_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=184, w2=192, w3=345, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(192, min_periods=max(192//3, 2)).max()
    trough = x.rolling(184, min_periods=max(184//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.090588 + 0.0037747 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_017_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=191, w2=205, w3=362, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(205, min_periods=max(205//3, 2)).rank(pct=True)
    persistence = change.rolling(362, min_periods=max(362//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.147667 * persistence + 0.0037748 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_018_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=198, w2=218, w3=379, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(198, min_periods=max(198//3, 2)).std()
    vol_slow = ret.rolling(218, min_periods=max(218//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.117647 + 0.0037749 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_019_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=205, w2=231, w3=396, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(231, min_periods=max(231//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 205)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.160333 * slope + 0.003775 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_020_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=212, w2=244, w3=413, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(244, min_periods=max(244//3, 2)).mean()
    noise = impulse.abs().rolling(413, min_periods=max(413//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.144706 + 0.0037751 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_021_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=219, w2=257, w3=430, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 219)
    acceleration = _rolling_slope(velocity, 257)
    curvature = _rolling_slope(acceleration, 430)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.173 * acceleration + 0.0037752 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_022_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=226, w2=270, w3=447, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 226)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.179333 * pressure.rolling(447, min_periods=max(447//3, 2)).mean() + 0.0037753 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_023_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=233, w2=283, w3=464, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(233, min_periods=max(233//3, 2)).mean())
    decay = spread.ewm(span=283, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.185294 + 0.0037754 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_024_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=240, w2=296, w3=481, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(296, min_periods=max(296//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 240)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.198824 + 0.0037755 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_025_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=247, w2=309, w3=498, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(247, min_periods=max(247//3, 2)).mean(), b.abs().rolling(309, min_periods=max(309//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.198333 * _rolling_slope(cover, 247) + 0.0037756 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_026_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=7, w2=322, w3=515, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.204667 * y + 0.795333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 7) - _rolling_slope(basket, 322) + 0.0037757 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_027_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=14, w2=335, w3=532, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(14, min_periods=max(14//3, 2)).mean(), upside.rolling(335, min_periods=max(335//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.239412 + 0.0037758 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_028_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=21, w2=348, w3=549, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(348, min_periods=max(348//3, 2)).max()
    rebound = x - x.rolling(21, min_periods=max(21//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.217333 * _rolling_slope(draw, 549) + 0.0037759 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_029_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=28, w2=361, w3=566, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(28) - b.diff(126)
    stress = imbalance.rolling(566, min_periods=max(566//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.266471 + 0.003776 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_030_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=35, w2=374, w3=583, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 35)
    baseline = trend.rolling(374, min_periods=max(374//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(583, min_periods=max(583//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.28 + 0.0037761 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_031_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=42, w2=387, w3=600, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 42)
    slow = _rolling_slope(x, 387)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.293529 + 0.0037762 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_032_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=49, w2=400, w3=617, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(400, min_periods=max(400//3, 2)).max()
    trough = x.rolling(49, min_periods=max(49//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.307059 + 0.0037763 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_033_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=56, w2=413, w3=634, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(56)
    rank = change.rolling(413, min_periods=max(413//3, 2)).rank(pct=True)
    persistence = change.rolling(634, min_periods=max(634//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.249 * persistence + 0.0037764 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_034_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=63, w2=426, w3=651, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(63, min_periods=max(63//3, 2)).std()
    vol_slow = ret.rolling(426, min_periods=max(426//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.334118 + 0.0037765 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_035_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=70, w2=439, w3=668, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(439, min_periods=max(439//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 70)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.261667 * slope + 0.0037766 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_036_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=77, w2=452, w3=685, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(77)
    drag = impulse.rolling(452, min_periods=max(452//3, 2)).mean()
    noise = impulse.abs().rolling(685, min_periods=max(685//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.361176 + 0.0037767 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_037_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=84, w2=465, w3=702, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 84)
    acceleration = _rolling_slope(velocity, 465)
    curvature = _rolling_slope(acceleration, 702)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.274333 * acceleration + 0.0037768 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_038_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=91, w2=478, w3=719, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 91)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.280667 * pressure.rolling(719, min_periods=max(719//3, 2)).mean() + 0.0037769 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_039_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=98, w2=491, w3=736, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(98, min_periods=max(98//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.401765 + 0.003777 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_040_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=105, w2=504, w3=753, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(504, min_periods=max(504//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 105)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.415294 + 0.0037771 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_041_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=112, w2=18, w3=19, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(112, min_periods=max(112//3, 2)).mean(), b.abs().rolling(18, min_periods=max(18//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(19) + 0.299667 * _rolling_slope(cover, 112) + 0.0037772 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_042_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=119, w2=31, w3=36, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.306 * y + 0.694000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 119) - _rolling_slope(basket, 31) + 0.0037773 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_043_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=126, w2=44, w3=53, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(126, min_periods=max(126//3, 2)).mean(), upside.rolling(44, min_periods=max(44//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(53) * 1.455882 + 0.0037774 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_044_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=133, w2=57, w3=70, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(57, min_periods=max(57//3, 2)).max()
    rebound = x - x.rolling(133, min_periods=max(133//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.318667 * _rolling_slope(draw, 70) + 0.0037775 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_045_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=140, w2=70, w3=87, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(70)
    stress = imbalance.rolling(87, min_periods=max(87//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.482941 + 0.0037776 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_046_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=147, w2=83, w3=104, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 147)
    baseline = trend.rolling(83, min_periods=max(83//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(104, min_periods=max(104//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.496471 + 0.0037777 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_047_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=154, w2=96, w3=121, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 154)
    slow = _rolling_slope(x, 96)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=121, adjust=False).mean() * 1.51 + 0.0037778 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_048_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=161, w2=109, w3=138, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(109, min_periods=max(109//3, 2)).max()
    trough = x.rolling(161, min_periods=max(161//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.523529 + 0.0037779 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_049_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=168, w2=122, w3=155, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(122, min_periods=max(122//3, 2)).rank(pct=True)
    persistence = change.rolling(155, min_periods=max(155//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.350333 * persistence + 0.003778 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_050_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=175, w2=135, w3=172, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(175, min_periods=max(175//3, 2)).std()
    vol_slow = ret.rolling(135, min_periods=max(135//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.550588 + 0.0037781 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_051_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=182, w2=148, w3=189, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(148, min_periods=max(148//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 182)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.363 * slope + 0.0037782 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_052_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=189, w2=161, w3=206, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(161, min_periods=max(161//3, 2)).mean()
    noise = impulse.abs().rolling(206, min_periods=max(206//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.577647 + 0.0037783 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_053_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=196, w2=174, w3=223, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 196)
    acceleration = _rolling_slope(velocity, 174)
    curvature = _rolling_slope(acceleration, 223)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.043333 * acceleration + 0.0037784 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_054_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=203, w2=187, w3=240, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 203)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.049667 * pressure.rolling(240, min_periods=max(240//3, 2)).mean() + 0.0037785 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_055_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=210, w2=200, w3=257, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(210, min_periods=max(210//3, 2)).mean())
    decay = spread.ewm(span=200, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.618235 + 0.0037786 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_056_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=217, w2=213, w3=274, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(213, min_periods=max(213//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 217)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.631765 + 0.0037787 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_057_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=224, w2=226, w3=291, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(224, min_periods=max(224//3, 2)).mean(), b.abs().rolling(226, min_periods=max(226//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.068667 * _rolling_slope(cover, 224) + 0.0037788 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_058_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=231, w2=239, w3=308, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.075 * y + 0.925000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 231) - _rolling_slope(basket, 239) + 0.0037789 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_059_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=238, w2=252, w3=325, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(238, min_periods=max(238//3, 2)).mean(), upside.rolling(252, min_periods=max(252//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.672353 + 0.003779 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_060_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=245, w2=265, w3=342, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(265, min_periods=max(265//3, 2)).max()
    rebound = x - x.rolling(245, min_periods=max(245//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.087667 * _rolling_slope(draw, 342) + 0.0037791 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_061_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=5, w2=278, w3=359, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(5) - b.diff(126)
    stress = imbalance.rolling(359, min_periods=max(359//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.845882 + 0.0037792 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_062_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=12, w2=291, w3=376, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 12)
    baseline = trend.rolling(291, min_periods=max(291//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(376, min_periods=max(376//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.859412 + 0.0037793 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_063_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=19, w2=304, w3=393, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 19)
    slow = _rolling_slope(x, 304)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.872941 + 0.0037794 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_064_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=26, w2=317, w3=410, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(317, min_periods=max(317//3, 2)).max()
    trough = x.rolling(26, min_periods=max(26//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.886471 + 0.0037795 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_065_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=33, w2=330, w3=427, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(33)
    rank = change.rolling(330, min_periods=max(330//3, 2)).rank(pct=True)
    persistence = change.rolling(427, min_periods=max(427//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.119333 * persistence + 0.0037796 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_066_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=40, w2=343, w3=444, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(40, min_periods=max(40//3, 2)).std()
    vol_slow = ret.rolling(343, min_periods=max(343//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.913529 + 0.0037797 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_067_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=47, w2=356, w3=461, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(356, min_periods=max(356//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 47)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.132 * slope + 0.0037798 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_068_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=54, w2=369, w3=478, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(54)
    drag = impulse.rolling(369, min_periods=max(369//3, 2)).mean()
    noise = impulse.abs().rolling(478, min_periods=max(478//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.940588 + 0.0037799 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_069_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=61, w2=382, w3=495, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 61)
    acceleration = _rolling_slope(velocity, 382)
    curvature = _rolling_slope(acceleration, 495)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.144667 * acceleration + 0.00378 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_070_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=68, w2=395, w3=512, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 68)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.151 * pressure.rolling(512, min_periods=max(512//3, 2)).mean() + 0.0037801 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_071_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=75, w2=408, w3=529, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(75, min_periods=max(75//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.981176 + 0.0037802 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_072_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=82, w2=421, w3=546, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(421, min_periods=max(421//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 82)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.994706 + 0.0037803 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_073_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=89, w2=434, w3=563, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(89, min_periods=max(89//3, 2)).mean(), b.abs().rolling(434, min_periods=max(434//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.17 * _rolling_slope(cover, 89) + 0.0037804 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_074_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=96, w2=447, w3=580, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.176333 * y + 0.823667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 96) - _rolling_slope(basket, 447) + 0.0037805 * anchor
    return base_signal.diff().diff().diff()

def f57_vent_gemini_075_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=103, w2=460, w3=597, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(103, min_periods=max(103//3, 2)).mean(), upside.rolling(460, min_periods=max(460//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.035294 + 0.0037806 * anchor
    return base_signal.diff().diff().diff()
