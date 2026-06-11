"""05 failed breakout dynamics gemini d3 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Price action failing to maintain levels above prior resistance, indicating bull traps.
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

def f05_fbrk_gemini_076_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=150, w2=414, w3=152, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(414, min_periods=max(414//3, 2)).max()
    rebound = x - x.rolling(150, min_periods=max(150//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.077 * _rolling_slope(draw, 152) + 0.0002527 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_077_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=157, w2=427, w3=169, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(169, min_periods=max(169//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.867647 + 0.0002528 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_078_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=164, w2=440, w3=186, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 164)
    baseline = trend.rolling(440, min_periods=max(440//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(186, min_periods=max(186//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.881176 + 0.0002529 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_079_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=171, w2=453, w3=203, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 171)
    slow = _rolling_slope(x, 453)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=203, adjust=False).mean() * 0.894706 + 0.000253 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_080_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=178, w2=466, w3=220, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(466, min_periods=max(466//3, 2)).max()
    trough = x.rolling(178, min_periods=max(178//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.908235 + 0.0002531 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_081_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=185, w2=479, w3=237, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(479, min_periods=max(479//3, 2)).rank(pct=True)
    persistence = change.rolling(237, min_periods=max(237//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.108667 * persistence + 0.0002532 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_082_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=192, w2=492, w3=254, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(192, min_periods=max(192//3, 2)).std()
    vol_slow = ret.rolling(492, min_periods=max(492//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.935294 + 0.0002533 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_083_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=199, w2=505, w3=271, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(505, min_periods=max(505//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 199)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.121333 * slope + 0.0002534 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_084_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=206, w2=19, w3=288, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(19, min_periods=max(19//3, 2)).mean()
    noise = impulse.abs().rolling(288, min_periods=max(288//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.962353 + 0.0002535 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_085_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=213, w2=32, w3=305, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 213)
    acceleration = _rolling_slope(velocity, 32)
    curvature = _rolling_slope(acceleration, 305)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.134 * acceleration + 0.0002536 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_086_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=220, w2=45, w3=322, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 220)
    pressure = rel_log.diff(45)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.140333 * pressure.rolling(322, min_periods=max(322//3, 2)).mean() + 0.0002537 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_087_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=227, w2=58, w3=339, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(227, min_periods=max(227//3, 2)).mean())
    decay = spread.ewm(span=58, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.002941 + 0.0002538 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_088_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=234, w2=71, w3=356, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(71, min_periods=max(71//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 234)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.016471 + 0.0002539 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_089_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=241, w2=84, w3=373, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(241, min_periods=max(241//3, 2)).mean(), b.abs().rolling(84, min_periods=max(84//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.159333 * _rolling_slope(cover, 241) + 0.000254 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_090_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=248, w2=97, w3=390, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.165667 * y + 0.834333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 248) - _rolling_slope(basket, 97) + 0.0002541 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_091_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=8, w2=110, w3=407, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(8, min_periods=max(8//3, 2)).mean(), upside.rolling(110, min_periods=max(110//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.057059 + 0.0002542 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_092_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=15, w2=123, w3=424, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(123, min_periods=max(123//3, 2)).max()
    rebound = x - x.rolling(15, min_periods=max(15//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.178333 * _rolling_slope(draw, 424) + 0.0002543 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_093_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=22, w2=136, w3=441, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(22) - b.diff(126)
    stress = imbalance.rolling(441, min_periods=max(441//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.084118 + 0.0002544 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_094_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=29, w2=149, w3=458, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 29)
    baseline = trend.rolling(149, min_periods=max(149//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(458, min_periods=max(458//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.097647 + 0.0002545 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_095_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=36, w2=162, w3=475, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 36)
    slow = _rolling_slope(x, 162)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.111176 + 0.0002546 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_096_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=43, w2=175, w3=492, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(175, min_periods=max(175//3, 2)).max()
    trough = x.rolling(43, min_periods=max(43//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.124706 + 0.0002547 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_097_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=50, w2=188, w3=509, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(50)
    rank = change.rolling(188, min_periods=max(188//3, 2)).rank(pct=True)
    persistence = change.rolling(509, min_periods=max(509//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.21 * persistence + 0.0002548 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_098_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=57, w2=201, w3=526, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(57, min_periods=max(57//3, 2)).std()
    vol_slow = ret.rolling(201, min_periods=max(201//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.151765 + 0.0002549 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_099_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=64, w2=214, w3=543, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(214, min_periods=max(214//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 64)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.222667 * slope + 0.000255 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_100_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=71, w2=227, w3=560, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(71)
    drag = impulse.rolling(227, min_periods=max(227//3, 2)).mean()
    noise = impulse.abs().rolling(560, min_periods=max(560//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.178824 + 0.0002551 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_101_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=78, w2=240, w3=577, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 78)
    acceleration = _rolling_slope(velocity, 240)
    curvature = _rolling_slope(acceleration, 577)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.235333 * acceleration + 0.0002552 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_102_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=85, w2=253, w3=594, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 85)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.241667 * pressure.rolling(594, min_periods=max(594//3, 2)).mean() + 0.0002553 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_103_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=92, w2=266, w3=611, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(92, min_periods=max(92//3, 2)).mean())
    decay = spread.ewm(span=266, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.219412 + 0.0002554 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_104_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=99, w2=279, w3=628, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(279, min_periods=max(279//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 99)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.232941 + 0.0002555 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_105_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=106, w2=292, w3=645, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(106, min_periods=max(106//3, 2)).mean(), b.abs().rolling(292, min_periods=max(292//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.260667 * _rolling_slope(cover, 106) + 0.0002556 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_106_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=113, w2=305, w3=662, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.267 * y + 0.733000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 113) - _rolling_slope(basket, 305) + 0.0002557 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_107_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=120, w2=318, w3=679, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(120, min_periods=max(120//3, 2)).mean(), upside.rolling(318, min_periods=max(318//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.273529 + 0.0002558 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_108_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=127, w2=331, w3=696, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(331, min_periods=max(331//3, 2)).max()
    rebound = x - x.rolling(127, min_periods=max(127//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.279667 * _rolling_slope(draw, 696) + 0.0002559 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_109_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=134, w2=344, w3=713, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(713, min_periods=max(713//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.300588 + 0.000256 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_110_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=141, w2=357, w3=730, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 141)
    baseline = trend.rolling(357, min_periods=max(357//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(730, min_periods=max(730//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.314118 + 0.0002561 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_111_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=148, w2=370, w3=747, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 148)
    slow = _rolling_slope(x, 370)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.327647 + 0.0002562 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_112_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=155, w2=383, w3=764, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(383, min_periods=max(383//3, 2)).max()
    trough = x.rolling(155, min_periods=max(155//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.341176 + 0.0002563 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_113_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=162, w2=396, w3=30, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(396, min_periods=max(396//3, 2)).rank(pct=True)
    persistence = change.rolling(30, min_periods=max(30//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.311333 * persistence + 0.0002564 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_114_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=169, w2=409, w3=47, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(169, min_periods=max(169//3, 2)).std()
    vol_slow = ret.rolling(409, min_periods=max(409//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.368235 + 0.0002565 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_115_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=176, w2=422, w3=64, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(422, min_periods=max(422//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 176)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.324 * slope + 0.0002566 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_116_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=183, w2=435, w3=81, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(435, min_periods=max(435//3, 2)).mean()
    noise = impulse.abs().rolling(81, min_periods=max(81//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.395294 + 0.0002567 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_117_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=190, w2=448, w3=98, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 190)
    acceleration = _rolling_slope(velocity, 448)
    curvature = _rolling_slope(acceleration, 98)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.336667 * acceleration + 0.0002568 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_118_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=197, w2=461, w3=115, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 197)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.343 * pressure.rolling(115, min_periods=max(115//3, 2)).mean() + 0.0002569 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_119_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=204, w2=474, w3=132, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(204, min_periods=max(204//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.435882 + 0.000257 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_120_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=211, w2=487, w3=149, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(487, min_periods=max(487//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 211)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.449412 + 0.0002571 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_121_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=218, w2=500, w3=166, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(218, min_periods=max(218//3, 2)).mean(), b.abs().rolling(500, min_periods=max(500//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.362 * _rolling_slope(cover, 218) + 0.0002572 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_122_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=225, w2=14, w3=183, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.036 * y + 0.964000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 225) - _rolling_slope(basket, 14) + 0.0002573 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_123_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=232, w2=27, w3=200, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(232, min_periods=max(232//3, 2)).mean(), upside.rolling(27, min_periods=max(27//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.49 + 0.0002574 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_124_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=239, w2=40, w3=217, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(40, min_periods=max(40//3, 2)).max()
    rebound = x - x.rolling(239, min_periods=max(239//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.048667 * _rolling_slope(draw, 217) + 0.0002575 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_125_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=246, w2=53, w3=234, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(53)
    stress = imbalance.rolling(234, min_periods=max(234//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.517059 + 0.0002576 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_126_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=6, w2=66, w3=251, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 6)
    baseline = trend.rolling(66, min_periods=max(66//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(251, min_periods=max(251//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.530588 + 0.0002577 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_127_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=13, w2=79, w3=268, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 13)
    slow = _rolling_slope(x, 79)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=268, adjust=False).mean() * 1.544118 + 0.0002578 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_128_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=20, w2=92, w3=285, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(92, min_periods=max(92//3, 2)).max()
    trough = x.rolling(20, min_periods=max(20//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.557647 + 0.0002579 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_129_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=27, w2=105, w3=302, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(27)
    rank = change.rolling(105, min_periods=max(105//3, 2)).rank(pct=True)
    persistence = change.rolling(302, min_periods=max(302//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.080333 * persistence + 0.000258 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_130_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=34, w2=118, w3=319, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(34, min_periods=max(34//3, 2)).std()
    vol_slow = ret.rolling(118, min_periods=max(118//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.584706 + 0.0002581 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_131_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=41, w2=131, w3=336, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(131, min_periods=max(131//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 41)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.093 * slope + 0.0002582 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_132_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=48, w2=144, w3=353, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(48)
    drag = impulse.rolling(144, min_periods=max(144//3, 2)).mean()
    noise = impulse.abs().rolling(353, min_periods=max(353//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.611765 + 0.0002583 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_133_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=55, w2=157, w3=370, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 55)
    acceleration = _rolling_slope(velocity, 157)
    curvature = _rolling_slope(acceleration, 370)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.105667 * acceleration + 0.0002584 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_134_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=62, w2=170, w3=387, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 62)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.112 * pressure.rolling(387, min_periods=max(387//3, 2)).mean() + 0.0002585 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_135_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=69, w2=183, w3=404, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(69, min_periods=max(69//3, 2)).mean())
    decay = spread.ewm(span=183, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.652353 + 0.0002586 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_136_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=76, w2=196, w3=421, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(196, min_periods=max(196//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 76)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.665882 + 0.0002587 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_137_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=83, w2=209, w3=438, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(83, min_periods=max(83//3, 2)).mean(), b.abs().rolling(209, min_periods=max(209//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.131 * _rolling_slope(cover, 83) + 0.0002588 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_138_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=90, w2=222, w3=455, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.137333 * y + 0.862667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 90) - _rolling_slope(basket, 222) + 0.0002589 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_139_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=97, w2=235, w3=472, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(97, min_periods=max(97//3, 2)).mean(), upside.rolling(235, min_periods=max(235//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.852941 + 0.000259 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_140_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=104, w2=248, w3=489, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(248, min_periods=max(248//3, 2)).max()
    rebound = x - x.rolling(104, min_periods=max(104//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.15 * _rolling_slope(draw, 489) + 0.0002591 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_141_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=111, w2=261, w3=506, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(111) - b.diff(126)
    stress = imbalance.rolling(506, min_periods=max(506//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.88 + 0.0002592 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_142_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=118, w2=274, w3=523, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 118)
    baseline = trend.rolling(274, min_periods=max(274//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(523, min_periods=max(523//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.893529 + 0.0002593 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_143_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=125, w2=287, w3=540, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 125)
    slow = _rolling_slope(x, 287)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.907059 + 0.0002594 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_144_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=132, w2=300, w3=557, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(300, min_periods=max(300//3, 2)).max()
    trough = x.rolling(132, min_periods=max(132//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.920588 + 0.0002595 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_145_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=139, w2=313, w3=574, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(313, min_periods=max(313//3, 2)).rank(pct=True)
    persistence = change.rolling(574, min_periods=max(574//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.181667 * persistence + 0.0002596 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_146_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=146, w2=326, w3=591, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(146, min_periods=max(146//3, 2)).std()
    vol_slow = ret.rolling(326, min_periods=max(326//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.947647 + 0.0002597 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_147_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=153, w2=339, w3=608, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(339, min_periods=max(339//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 153)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.194333 * slope + 0.0002598 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_148_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=160, w2=352, w3=625, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(352, min_periods=max(352//3, 2)).mean()
    noise = impulse.abs().rolling(625, min_periods=max(625//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.974706 + 0.0002599 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_149_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=167, w2=365, w3=642, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 167)
    acceleration = _rolling_slope(velocity, 365)
    curvature = _rolling_slope(acceleration, 642)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.207 * acceleration + 0.00026 * anchor
    return base_signal.diff().diff().diff()

def f05_fbrk_gemini_150_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=174, w2=378, w3=659, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 174)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.213333 * pressure.rolling(659, min_periods=max(659//3, 2)).mean() + 0.0002601 * anchor
    return base_signal.diff().diff().diff()
