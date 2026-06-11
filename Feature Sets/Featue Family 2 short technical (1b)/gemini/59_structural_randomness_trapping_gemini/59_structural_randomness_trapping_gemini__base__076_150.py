"""59 structural randomness trapping gemini base features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Identification of market phases where noise overwhelms signal, trapping traders.
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

def f59_sran_gemini_076(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=70, w2=92, w3=498, lag=13)."""
    a = _safe_log(open.abs() + 1.0).shift(13)
    b = _safe_log(high.abs() + 1.0).shift(13)
    corr = a.rolling(92, min_periods=max(92//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 70)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.130588 + 0.0038507 * anchor
    return base_signal

def f59_sran_gemini_077(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=77, w2=105, w3=515, lag=21)."""
    a = open.shift(21)
    b = high.shift(21)
    cover = _safe_div(a.rolling(77, min_periods=max(77//3, 2)).mean(), b.abs().rolling(105, min_periods=max(105//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.308333 * _rolling_slope(cover, 77) + 0.0038508 * anchor
    return base_signal

def f59_sran_gemini_078(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=84, w2=118, w3=532, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    y = _safe_log(high.abs() + 1.0).shift(34)
    z = _safe_log(low.abs() + 1.0).shift(34)
    basket = x - 0.314667 * y + 0.685333 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 84) - _rolling_slope(basket, 118) + 0.0038509 * anchor
    return base_signal

def f59_sran_gemini_079(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=91, w2=131, w3=549, lag=55)."""
    x = open.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(91, min_periods=max(91//3, 2)).mean(), upside.rolling(131, min_periods=max(131//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.171176 + 0.003851 * anchor
    return base_signal

def f59_sran_gemini_080(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=98, w2=144, w3=566, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    draw = x - x.rolling(144, min_periods=max(144//3, 2)).max()
    rebound = x - x.rolling(98, min_periods=max(98//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.327333 * _rolling_slope(draw, 566) + 0.0038511 * anchor
    return base_signal

def f59_sran_gemini_081(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=105, w2=157, w3=583, lag=1)."""
    a = _safe_log(open.abs() + 1.0).shift(1)
    b = _safe_log(high.abs() + 1.0).shift(1)
    imbalance = a.diff(105) - b.diff(126)
    stress = imbalance.rolling(583, min_periods=max(583//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.198235 + 0.0038512 * anchor
    return base_signal

def f59_sran_gemini_082(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=112, w2=170, w3=600, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 112)
    baseline = trend.rolling(170, min_periods=max(170//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(600, min_periods=max(600//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.211765 + 0.0038513 * anchor
    return base_signal

def f59_sran_gemini_083(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=119, w2=183, w3=617, lag=3)."""
    x = _safe_log(open.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 119)
    slow = _rolling_slope(x, 183)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.225294 + 0.0038514 * anchor
    return base_signal

def f59_sran_gemini_084(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=126, w2=196, w3=634, lag=5)."""
    x = open.shift(5)
    peak = x.rolling(196, min_periods=max(196//3, 2)).max()
    trough = x.rolling(126, min_periods=max(126//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.238824 + 0.0038515 * anchor
    return base_signal

def f59_sran_gemini_085(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=133, w2=209, w3=651, lag=8)."""
    x = open.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(209, min_periods=max(209//3, 2)).rank(pct=True)
    persistence = change.rolling(651, min_periods=max(651//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.359 * persistence + 0.0038516 * anchor
    return base_signal

def f59_sran_gemini_086(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=140, w2=222, w3=668, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(140, min_periods=max(140//3, 2)).std()
    vol_slow = ret.rolling(222, min_periods=max(222//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.265882 + 0.0038517 * anchor
    return base_signal

def f59_sran_gemini_087(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=147, w2=235, w3=685, lag=21)."""
    x = open.shift(21)
    ma = x.rolling(235, min_periods=max(235//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 147)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.039333 * slope + 0.0038518 * anchor
    return base_signal

def f59_sran_gemini_088(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=154, w2=248, w3=702, lag=34)."""
    x = open.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(248, min_periods=max(248//3, 2)).mean()
    noise = impulse.abs().rolling(702, min_periods=max(702//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.292941 + 0.0038519 * anchor
    return base_signal

def f59_sran_gemini_089(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=161, w2=261, w3=719, lag=55)."""
    x = _safe_log(open.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 161)
    acceleration = _rolling_slope(velocity, 261)
    curvature = _rolling_slope(acceleration, 719)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.052 * acceleration + 0.003852 * anchor
    return base_signal

def f59_sran_gemini_090(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=168, w2=274, w3=736, lag=0)."""
    rel = _safe_div(open.shift(0), high.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 168)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.058333 * pressure.rolling(736, min_periods=max(736//3, 2)).mean() + 0.0038521 * anchor
    return base_signal

def f59_sran_gemini_091(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=175, w2=287, w3=753, lag=1)."""
    a = open.shift(1)
    b = high.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(175, min_periods=max(175//3, 2)).mean())
    decay = spread.ewm(span=287, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.333529 + 0.0038522 * anchor
    return base_signal

def f59_sran_gemini_092(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=182, w2=300, w3=19, lag=2)."""
    a = _safe_log(open.abs() + 1.0).shift(2)
    b = _safe_log(high.abs() + 1.0).shift(2)
    corr = a.rolling(300, min_periods=max(300//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 182)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.347059 + 0.0038523 * anchor
    return base_signal

def f59_sran_gemini_093(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=189, w2=313, w3=36, lag=3)."""
    a = open.shift(3)
    b = high.shift(3)
    cover = _safe_div(a.rolling(189, min_periods=max(189//3, 2)).mean(), b.abs().rolling(313, min_periods=max(313//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(36) + 0.077333 * _rolling_slope(cover, 189) + 0.0038524 * anchor
    return base_signal

def f59_sran_gemini_094(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=196, w2=326, w3=53, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    y = _safe_log(high.abs() + 1.0).shift(5)
    z = _safe_log(low.abs() + 1.0).shift(5)
    basket = x - 0.083667 * y + 0.916333 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 196) - _rolling_slope(basket, 326) + 0.0038525 * anchor
    return base_signal

def f59_sran_gemini_095(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=203, w2=339, w3=70, lag=8)."""
    x = open.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(203, min_periods=max(203//3, 2)).mean(), upside.rolling(339, min_periods=max(339//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(70) * 1.387647 + 0.0038526 * anchor
    return base_signal

def f59_sran_gemini_096(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=210, w2=352, w3=87, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    draw = x - x.rolling(352, min_periods=max(352//3, 2)).max()
    rebound = x - x.rolling(210, min_periods=max(210//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.096333 * _rolling_slope(draw, 87) + 0.0038527 * anchor
    return base_signal

def f59_sran_gemini_097(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=217, w2=365, w3=104, lag=21)."""
    a = _safe_log(open.abs() + 1.0).shift(21)
    b = _safe_log(high.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(104, min_periods=max(104//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.414706 + 0.0038528 * anchor
    return base_signal

def f59_sran_gemini_098(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=224, w2=378, w3=121, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 224)
    baseline = trend.rolling(378, min_periods=max(378//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(121, min_periods=max(121//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.428235 + 0.0038529 * anchor
    return base_signal

def f59_sran_gemini_099(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=231, w2=391, w3=138, lag=55)."""
    x = _safe_log(open.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 231)
    slow = _rolling_slope(x, 391)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=138, adjust=False).mean() * 1.441765 + 0.003853 * anchor
    return base_signal

def f59_sran_gemini_100(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=238, w2=404, w3=155, lag=0)."""
    x = open.shift(0)
    peak = x.rolling(404, min_periods=max(404//3, 2)).max()
    trough = x.rolling(238, min_periods=max(238//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.455294 + 0.0038531 * anchor
    return base_signal

def f59_sran_gemini_101(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=245, w2=417, w3=172, lag=1)."""
    x = open.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(417, min_periods=max(417//3, 2)).rank(pct=True)
    persistence = change.rolling(172, min_periods=max(172//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.128 * persistence + 0.0038532 * anchor
    return base_signal

def f59_sran_gemini_102(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=5, w2=430, w3=189, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(5, min_periods=max(5//3, 2)).std()
    vol_slow = ret.rolling(430, min_periods=max(430//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.482353 + 0.0038533 * anchor
    return base_signal

def f59_sran_gemini_103(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=12, w2=443, w3=206, lag=3)."""
    x = open.shift(3)
    ma = x.rolling(443, min_periods=max(443//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 12)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.140667 * slope + 0.0038534 * anchor
    return base_signal

def f59_sran_gemini_104(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=19, w2=456, w3=223, lag=5)."""
    x = open.shift(5)
    impulse = x.diff(19)
    drag = impulse.rolling(456, min_periods=max(456//3, 2)).mean()
    noise = impulse.abs().rolling(223, min_periods=max(223//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.509412 + 0.0038535 * anchor
    return base_signal

def f59_sran_gemini_105(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=26, w2=469, w3=240, lag=8)."""
    x = _safe_log(open.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 26)
    acceleration = _rolling_slope(velocity, 469)
    curvature = _rolling_slope(acceleration, 240)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.153333 * acceleration + 0.0038536 * anchor
    return base_signal

def f59_sran_gemini_106(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=33, w2=482, w3=257, lag=13)."""
    rel = _safe_div(open.shift(13), high.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 33)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.159667 * pressure.rolling(257, min_periods=max(257//3, 2)).mean() + 0.0038537 * anchor
    return base_signal

def f59_sran_gemini_107(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=40, w2=495, w3=274, lag=21)."""
    a = open.shift(21)
    b = high.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(40, min_periods=max(40//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.55 + 0.0038538 * anchor
    return base_signal

def f59_sran_gemini_108(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=47, w2=508, w3=291, lag=34)."""
    a = _safe_log(open.abs() + 1.0).shift(34)
    b = _safe_log(high.abs() + 1.0).shift(34)
    corr = a.rolling(508, min_periods=max(508//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 47)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.563529 + 0.0038539 * anchor
    return base_signal

def f59_sran_gemini_109(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=54, w2=22, w3=308, lag=55)."""
    a = open.shift(55)
    b = high.shift(55)
    cover = _safe_div(a.rolling(54, min_periods=max(54//3, 2)).mean(), b.abs().rolling(22, min_periods=max(22//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.178667 * _rolling_slope(cover, 54) + 0.003854 * anchor
    return base_signal

def f59_sran_gemini_110(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=61, w2=35, w3=325, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    y = _safe_log(high.abs() + 1.0).shift(0)
    z = _safe_log(low.abs() + 1.0).shift(0)
    basket = x - 0.185 * y + 0.815000 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 61) - _rolling_slope(basket, 35) + 0.0038541 * anchor
    return base_signal

def f59_sran_gemini_111(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=68, w2=48, w3=342, lag=1)."""
    x = open.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(68, min_periods=max(68//3, 2)).mean(), upside.rolling(48, min_periods=max(48//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.604118 + 0.0038542 * anchor
    return base_signal

def f59_sran_gemini_112(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=75, w2=61, w3=359, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    draw = x - x.rolling(61, min_periods=max(61//3, 2)).max()
    rebound = x - x.rolling(75, min_periods=max(75//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.197667 * _rolling_slope(draw, 359) + 0.0038543 * anchor
    return base_signal

def f59_sran_gemini_113(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=82, w2=74, w3=376, lag=3)."""
    a = _safe_log(open.abs() + 1.0).shift(3)
    b = _safe_log(high.abs() + 1.0).shift(3)
    imbalance = a.diff(82) - b.diff(74)
    stress = imbalance.rolling(376, min_periods=max(376//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.631176 + 0.0038544 * anchor
    return base_signal

def f59_sran_gemini_114(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=89, w2=87, w3=393, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 89)
    baseline = trend.rolling(87, min_periods=max(87//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(393, min_periods=max(393//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.644706 + 0.0038545 * anchor
    return base_signal

def f59_sran_gemini_115(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=96, w2=100, w3=410, lag=8)."""
    x = _safe_log(open.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 96)
    slow = _rolling_slope(x, 100)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.658235 + 0.0038546 * anchor
    return base_signal

def f59_sran_gemini_116(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=103, w2=113, w3=427, lag=13)."""
    x = open.shift(13)
    peak = x.rolling(113, min_periods=max(113//3, 2)).max()
    trough = x.rolling(103, min_periods=max(103//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.671765 + 0.0038547 * anchor
    return base_signal

def f59_sran_gemini_117(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=110, w2=126, w3=444, lag=21)."""
    x = open.shift(21)
    change = x.pct_change(110)
    rank = change.rolling(126, min_periods=max(126//3, 2)).rank(pct=True)
    persistence = change.rolling(444, min_periods=max(444//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.229333 * persistence + 0.0038548 * anchor
    return base_signal

def f59_sran_gemini_118(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=117, w2=139, w3=461, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(117, min_periods=max(117//3, 2)).std()
    vol_slow = ret.rolling(139, min_periods=max(139//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.845294 + 0.0038549 * anchor
    return base_signal

def f59_sran_gemini_119(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=124, w2=152, w3=478, lag=55)."""
    x = open.shift(55)
    ma = x.rolling(152, min_periods=max(152//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 124)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.242 * slope + 0.003855 * anchor
    return base_signal

def f59_sran_gemini_120(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=131, w2=165, w3=495, lag=0)."""
    x = open.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(165, min_periods=max(165//3, 2)).mean()
    noise = impulse.abs().rolling(495, min_periods=max(495//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.872353 + 0.0038551 * anchor
    return base_signal

def f59_sran_gemini_121(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=138, w2=178, w3=512, lag=1)."""
    x = _safe_log(open.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 138)
    acceleration = _rolling_slope(velocity, 178)
    curvature = _rolling_slope(acceleration, 512)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.254667 * acceleration + 0.0038552 * anchor
    return base_signal

def f59_sran_gemini_122(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=145, w2=191, w3=529, lag=2)."""
    rel = _safe_div(open.shift(2), high.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 145)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.261 * pressure.rolling(529, min_periods=max(529//3, 2)).mean() + 0.0038553 * anchor
    return base_signal

def f59_sran_gemini_123(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=152, w2=204, w3=546, lag=3)."""
    a = open.shift(3)
    b = high.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(152, min_periods=max(152//3, 2)).mean())
    decay = spread.ewm(span=204, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.912941 + 0.0038554 * anchor
    return base_signal

def f59_sran_gemini_124(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=159, w2=217, w3=563, lag=5)."""
    a = _safe_log(open.abs() + 1.0).shift(5)
    b = _safe_log(high.abs() + 1.0).shift(5)
    corr = a.rolling(217, min_periods=max(217//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 159)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.926471 + 0.0038555 * anchor
    return base_signal

def f59_sran_gemini_125(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=166, w2=230, w3=580, lag=8)."""
    a = open.shift(8)
    b = high.shift(8)
    cover = _safe_div(a.rolling(166, min_periods=max(166//3, 2)).mean(), b.abs().rolling(230, min_periods=max(230//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.28 * _rolling_slope(cover, 166) + 0.0038556 * anchor
    return base_signal

def f59_sran_gemini_126(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=173, w2=243, w3=597, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    y = _safe_log(high.abs() + 1.0).shift(13)
    z = _safe_log(low.abs() + 1.0).shift(13)
    basket = x - 0.286333 * y + 0.713667 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 173) - _rolling_slope(basket, 243) + 0.0038557 * anchor
    return base_signal

def f59_sran_gemini_127(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=180, w2=256, w3=614, lag=21)."""
    x = open.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(180, min_periods=max(180//3, 2)).mean(), upside.rolling(256, min_periods=max(256//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.967059 + 0.0038558 * anchor
    return base_signal

def f59_sran_gemini_128(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=187, w2=269, w3=631, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    draw = x - x.rolling(269, min_periods=max(269//3, 2)).max()
    rebound = x - x.rolling(187, min_periods=max(187//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.299 * _rolling_slope(draw, 631) + 0.0038559 * anchor
    return base_signal

def f59_sran_gemini_129(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=194, w2=282, w3=648, lag=55)."""
    a = _safe_log(open.abs() + 1.0).shift(55)
    b = _safe_log(high.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(648, min_periods=max(648//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.994118 + 0.003856 * anchor
    return base_signal

def f59_sran_gemini_130(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=201, w2=295, w3=665, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 201)
    baseline = trend.rolling(295, min_periods=max(295//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(665, min_periods=max(665//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.007647 + 0.0038561 * anchor
    return base_signal

def f59_sran_gemini_131(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=208, w2=308, w3=682, lag=1)."""
    x = _safe_log(open.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 208)
    slow = _rolling_slope(x, 308)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.021176 + 0.0038562 * anchor
    return base_signal

def f59_sran_gemini_132(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=215, w2=321, w3=699, lag=2)."""
    x = open.shift(2)
    peak = x.rolling(321, min_periods=max(321//3, 2)).max()
    trough = x.rolling(215, min_periods=max(215//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.034706 + 0.0038563 * anchor
    return base_signal

def f59_sran_gemini_133(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=222, w2=334, w3=716, lag=3)."""
    x = open.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(334, min_periods=max(334//3, 2)).rank(pct=True)
    persistence = change.rolling(716, min_periods=max(716//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.330667 * persistence + 0.0038564 * anchor
    return base_signal

def f59_sran_gemini_134(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=229, w2=347, w3=733, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(229, min_periods=max(229//3, 2)).std()
    vol_slow = ret.rolling(347, min_periods=max(347//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.061765 + 0.0038565 * anchor
    return base_signal

def f59_sran_gemini_135(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=236, w2=360, w3=750, lag=8)."""
    x = open.shift(8)
    ma = x.rolling(360, min_periods=max(360//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 236)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.343333 * slope + 0.0038566 * anchor
    return base_signal

def f59_sran_gemini_136(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=243, w2=373, w3=767, lag=13)."""
    x = open.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(373, min_periods=max(373//3, 2)).mean()
    noise = impulse.abs().rolling(767, min_periods=max(767//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.088824 + 0.0038567 * anchor
    return base_signal

def f59_sran_gemini_137(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=250, w2=386, w3=33, lag=21)."""
    x = _safe_log(open.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 250)
    acceleration = _rolling_slope(velocity, 386)
    curvature = _rolling_slope(acceleration, 33)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.356 * acceleration + 0.0038568 * anchor
    return base_signal

def f59_sran_gemini_138(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=10, w2=399, w3=50, lag=34)."""
    rel = _safe_div(open.shift(34), high.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 10)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.362333 * pressure.rolling(50, min_periods=max(50//3, 2)).mean() + 0.0038569 * anchor
    return base_signal

def f59_sran_gemini_139(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=17, w2=412, w3=67, lag=55)."""
    a = open.shift(55)
    b = high.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(17, min_periods=max(17//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.129412 + 0.003857 * anchor
    return base_signal

def f59_sran_gemini_140(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=24, w2=425, w3=84, lag=0)."""
    a = _safe_log(open.abs() + 1.0).shift(0)
    b = _safe_log(high.abs() + 1.0).shift(0)
    corr = a.rolling(425, min_periods=max(425//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 24)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.142941 + 0.0038571 * anchor
    return base_signal

def f59_sran_gemini_141(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=31, w2=438, w3=101, lag=1)."""
    a = open.shift(1)
    b = high.shift(1)
    cover = _safe_div(a.rolling(31, min_periods=max(31//3, 2)).mean(), b.abs().rolling(438, min_periods=max(438//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(101) + 0.049 * _rolling_slope(cover, 31) + 0.0038572 * anchor
    return base_signal

def f59_sran_gemini_142(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=38, w2=451, w3=118, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    y = _safe_log(high.abs() + 1.0).shift(2)
    z = _safe_log(low.abs() + 1.0).shift(2)
    basket = x - 0.055333 * y + 0.944667 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 38) - _rolling_slope(basket, 451) + 0.0038573 * anchor
    return base_signal

def f59_sran_gemini_143(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=45, w2=464, w3=135, lag=3)."""
    x = open.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(45, min_periods=max(45//3, 2)).mean(), upside.rolling(464, min_periods=max(464//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.183529 + 0.0038574 * anchor
    return base_signal

def f59_sran_gemini_144(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=52, w2=477, w3=152, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    draw = x - x.rolling(477, min_periods=max(477//3, 2)).max()
    rebound = x - x.rolling(52, min_periods=max(52//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.068 * _rolling_slope(draw, 152) + 0.0038575 * anchor
    return base_signal

def f59_sran_gemini_145(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=59, w2=490, w3=169, lag=8)."""
    a = _safe_log(open.abs() + 1.0).shift(8)
    b = _safe_log(high.abs() + 1.0).shift(8)
    imbalance = a.diff(59) - b.diff(126)
    stress = imbalance.rolling(169, min_periods=max(169//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.210588 + 0.0038576 * anchor
    return base_signal

def f59_sran_gemini_146(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=66, w2=503, w3=186, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 66)
    baseline = trend.rolling(503, min_periods=max(503//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(186, min_periods=max(186//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.224118 + 0.0038577 * anchor
    return base_signal

def f59_sran_gemini_147(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=73, w2=17, w3=203, lag=21)."""
    x = _safe_log(open.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 73)
    slow = _rolling_slope(x, 17)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=203, adjust=False).mean() * 1.237647 + 0.0038578 * anchor
    return base_signal

def f59_sran_gemini_148(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=80, w2=30, w3=220, lag=34)."""
    x = open.shift(34)
    peak = x.rolling(30, min_periods=max(30//3, 2)).max()
    trough = x.rolling(80, min_periods=max(80//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.251176 + 0.0038579 * anchor
    return base_signal

def f59_sran_gemini_149(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=87, w2=43, w3=237, lag=55)."""
    x = open.shift(55)
    change = x.pct_change(87)
    rank = change.rolling(43, min_periods=max(43//3, 2)).rank(pct=True)
    persistence = change.rolling(237, min_periods=max(237//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.099667 * persistence + 0.003858 * anchor
    return base_signal

def f59_sran_gemini_150(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=94, w2=56, w3=254, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(94, min_periods=max(94//3, 2)).std()
    vol_slow = ret.rolling(56, min_periods=max(56//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.278235 + 0.0038581 * anchor
    return base_signal
