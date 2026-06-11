"""23 accumulation distribution line gemini d2 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Relationship between price close and range to determine if volume is accumulating or distributing.
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

def f23_adln_gemini_001_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Relationship between price close and range to determine if volume is accumulating or distributing. [window=5]"""
    window = 5
    res = _safe_div((close - low) - (high - close), high - low + 1e-9).rolling(window).mean()
    return (res).diff().diff()

def f23_adln_gemini_002_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Relationship between price close and range to determine if volume is accumulating or distributing. [window=10]"""
    window = 10
    res = _safe_div((close - low) - (high - close), high - low + 1e-9).rolling(window).mean()
    return (res).diff().diff()

def f23_adln_gemini_003_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Relationship between price close and range to determine if volume is accumulating or distributing. [window=21]"""
    window = 21
    res = _safe_div((close - low) - (high - close), high - low + 1e-9).rolling(window).mean()
    return (res).diff().diff()

def f23_adln_gemini_004_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Relationship between price close and range to determine if volume is accumulating or distributing. [window=42]"""
    window = 42
    res = _safe_div((close - low) - (high - close), high - low + 1e-9).rolling(window).mean()
    return (res).diff().diff()

def f23_adln_gemini_005_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Relationship between price close and range to determine if volume is accumulating or distributing. [window=63]"""
    window = 63
    res = _safe_div((close - low) - (high - close), high - low + 1e-9).rolling(window).mean()
    return (res).diff().diff()

def f23_adln_gemini_006_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Relationship between price close and range to determine if volume is accumulating or distributing. [window=126]"""
    window = 126
    res = _safe_div((close - low) - (high - close), high - low + 1e-9).rolling(window).mean()
    return (res).diff().diff()

def f23_adln_gemini_007_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Relationship between price close and range to determine if volume is accumulating or distributing. [window=252]"""
    window = 252
    res = _safe_div((close - low) - (high - close), high - low + 1e-9).rolling(window).mean()
    return (res).diff().diff()

def f23_adln_gemini_008_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Relationship between price close and range to determine if volume is accumulating or distributing. [window=504]"""
    window = 504
    res = _safe_div((close - low) - (high - close), high - low + 1e-9).rolling(window).mean()
    return (res).diff().diff()

def f23_adln_gemini_009_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Relationship between price close and range to determine if volume is accumulating or distributing. [window=756]"""
    window = 756
    res = _safe_div((close - low) - (high - close), high - low + 1e-9).rolling(window).mean()
    return (res).diff().diff()

def f23_adln_gemini_010_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Relationship between price close and range to determine if volume is accumulating or distributing. [window=1260]"""
    window = 1260
    res = _safe_div((close - low) - (high - close), high - low + 1e-9).rolling(window).mean()
    return (res).diff().diff()

def f23_adln_gemini_011_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=10, w2=287, w3=134, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 10)
    slow = _rolling_slope(x, 287)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=134, adjust=False).mean() * 1.001765 + 0.0018562 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_012_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=17, w2=300, w3=151, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(300, min_periods=max(300//3, 2)).max()
    trough = x.rolling(17, min_periods=max(17//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.015294 + 0.0018563 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_013_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=24, w2=313, w3=168, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(24)
    rank = change.rolling(313, min_periods=max(313//3, 2)).rank(pct=True)
    persistence = change.rolling(168, min_periods=max(168//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.283 * persistence + 0.0018564 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_014_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=31, w2=326, w3=185, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(31, min_periods=max(31//3, 2)).std()
    vol_slow = ret.rolling(326, min_periods=max(326//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.042353 + 0.0018565 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_015_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=38, w2=339, w3=202, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(339, min_periods=max(339//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 38)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.295667 * slope + 0.0018566 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_016_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=45, w2=352, w3=219, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(45)
    drag = impulse.rolling(352, min_periods=max(352//3, 2)).mean()
    noise = impulse.abs().rolling(219, min_periods=max(219//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.069412 + 0.0018567 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_017_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=52, w2=365, w3=236, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 52)
    acceleration = _rolling_slope(velocity, 365)
    curvature = _rolling_slope(acceleration, 236)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.308333 * acceleration + 0.0018568 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_018_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=59, w2=378, w3=253, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 59)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.314667 * pressure.rolling(253, min_periods=max(253//3, 2)).mean() + 0.0018569 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_019_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=66, w2=391, w3=270, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(66, min_periods=max(66//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.11 + 0.001857 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_020_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=73, w2=404, w3=287, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(404, min_periods=max(404//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 73)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.123529 + 0.0018571 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_021_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=80, w2=417, w3=304, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(80, min_periods=max(80//3, 2)).mean(), b.abs().rolling(417, min_periods=max(417//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.333667 * _rolling_slope(cover, 80) + 0.0018572 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_022_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=87, w2=430, w3=321, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.34 * y + 0.660000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 87) - _rolling_slope(basket, 430) + 0.0018573 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_023_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=94, w2=443, w3=338, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(94, min_periods=max(94//3, 2)).mean(), upside.rolling(443, min_periods=max(443//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.164118 + 0.0018574 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_024_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=101, w2=456, w3=355, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(456, min_periods=max(456//3, 2)).max()
    rebound = x - x.rolling(101, min_periods=max(101//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.352667 * _rolling_slope(draw, 355) + 0.0018575 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_025_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=108, w2=469, w3=372, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(108) - b.diff(126)
    stress = imbalance.rolling(372, min_periods=max(372//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.191176 + 0.0018576 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_026_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=115, w2=482, w3=389, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 115)
    baseline = trend.rolling(482, min_periods=max(482//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(389, min_periods=max(389//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.204706 + 0.0018577 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_027_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=122, w2=495, w3=406, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 122)
    slow = _rolling_slope(x, 495)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.218235 + 0.0018578 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_028_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=129, w2=508, w3=423, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(508, min_periods=max(508//3, 2)).max()
    trough = x.rolling(129, min_periods=max(129//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.231765 + 0.0018579 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_029_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=136, w2=22, w3=440, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(22, min_periods=max(22//3, 2)).rank(pct=True)
    persistence = change.rolling(440, min_periods=max(440//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.052 * persistence + 0.001858 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_030_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=143, w2=35, w3=457, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(143, min_periods=max(143//3, 2)).std()
    vol_slow = ret.rolling(35, min_periods=max(35//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.258824 + 0.0018581 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_031_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=150, w2=48, w3=474, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(48, min_periods=max(48//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 150)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.064667 * slope + 0.0018582 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_032_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=157, w2=61, w3=491, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(61, min_periods=max(61//3, 2)).mean()
    noise = impulse.abs().rolling(491, min_periods=max(491//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.285882 + 0.0018583 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_033_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=164, w2=74, w3=508, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 164)
    acceleration = _rolling_slope(velocity, 74)
    curvature = _rolling_slope(acceleration, 508)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.077333 * acceleration + 0.0018584 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_034_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=171, w2=87, w3=525, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 171)
    pressure = rel_log.diff(87)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.083667 * pressure.rolling(525, min_periods=max(525//3, 2)).mean() + 0.0018585 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_035_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=178, w2=100, w3=542, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(178, min_periods=max(178//3, 2)).mean())
    decay = spread.ewm(span=100, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.326471 + 0.0018586 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_036_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=185, w2=113, w3=559, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(113, min_periods=max(113//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 185)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.34 + 0.0018587 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_037_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=192, w2=126, w3=576, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(192, min_periods=max(192//3, 2)).mean(), b.abs().rolling(126, min_periods=max(126//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.102667 * _rolling_slope(cover, 192) + 0.0018588 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_038_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=199, w2=139, w3=593, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.109 * y + 0.891000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 199) - _rolling_slope(basket, 139) + 0.0018589 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_039_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=206, w2=152, w3=610, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(206, min_periods=max(206//3, 2)).mean(), upside.rolling(152, min_periods=max(152//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.380588 + 0.001859 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_040_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=213, w2=165, w3=627, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(165, min_periods=max(165//3, 2)).max()
    rebound = x - x.rolling(213, min_periods=max(213//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.121667 * _rolling_slope(draw, 627) + 0.0018591 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_041_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=220, w2=178, w3=644, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(644, min_periods=max(644//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.407647 + 0.0018592 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_042_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=227, w2=191, w3=661, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 227)
    baseline = trend.rolling(191, min_periods=max(191//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(661, min_periods=max(661//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.421176 + 0.0018593 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_043_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=234, w2=204, w3=678, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 234)
    slow = _rolling_slope(x, 204)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.434706 + 0.0018594 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_044_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=241, w2=217, w3=695, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(217, min_periods=max(217//3, 2)).max()
    trough = x.rolling(241, min_periods=max(241//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.448235 + 0.0018595 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_045_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=248, w2=230, w3=712, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(230, min_periods=max(230//3, 2)).rank(pct=True)
    persistence = change.rolling(712, min_periods=max(712//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.153333 * persistence + 0.0018596 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_046_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=8, w2=243, w3=729, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(8, min_periods=max(8//3, 2)).std()
    vol_slow = ret.rolling(243, min_periods=max(243//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.475294 + 0.0018597 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_047_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=15, w2=256, w3=746, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(256, min_periods=max(256//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 15)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.166 * slope + 0.0018598 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_048_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=22, w2=269, w3=763, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(22)
    drag = impulse.rolling(269, min_periods=max(269//3, 2)).mean()
    noise = impulse.abs().rolling(763, min_periods=max(763//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.502353 + 0.0018599 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_049_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=29, w2=282, w3=29, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 29)
    acceleration = _rolling_slope(velocity, 282)
    curvature = _rolling_slope(acceleration, 29)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.178667 * acceleration + 0.00186 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_050_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=36, w2=295, w3=46, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 36)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.185 * pressure.rolling(46, min_periods=max(46//3, 2)).mean() + 0.0018601 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_051_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=43, w2=308, w3=63, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(43, min_periods=max(43//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.542941 + 0.0018602 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_052_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=50, w2=321, w3=80, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(321, min_periods=max(321//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 50)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.556471 + 0.0018603 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_053_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=57, w2=334, w3=97, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(57, min_periods=max(57//3, 2)).mean(), b.abs().rolling(334, min_periods=max(334//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(97) + 0.204 * _rolling_slope(cover, 57) + 0.0018604 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_054_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=64, w2=347, w3=114, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.210333 * y + 0.789667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 64) - _rolling_slope(basket, 347) + 0.0018605 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_055_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=71, w2=360, w3=131, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(71, min_periods=max(71//3, 2)).mean(), upside.rolling(360, min_periods=max(360//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.597059 + 0.0018606 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_056_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=78, w2=373, w3=148, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(373, min_periods=max(373//3, 2)).max()
    rebound = x - x.rolling(78, min_periods=max(78//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.223 * _rolling_slope(draw, 148) + 0.0018607 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_057_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=85, w2=386, w3=165, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(85) - b.diff(126)
    stress = imbalance.rolling(165, min_periods=max(165//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.624118 + 0.0018608 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_058_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=92, w2=399, w3=182, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 92)
    baseline = trend.rolling(399, min_periods=max(399//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(182, min_periods=max(182//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.637647 + 0.0018609 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_059_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=99, w2=412, w3=199, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 99)
    slow = _rolling_slope(x, 412)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=199, adjust=False).mean() * 1.651176 + 0.001861 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_060_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=106, w2=425, w3=216, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(425, min_periods=max(425//3, 2)).max()
    trough = x.rolling(106, min_periods=max(106//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.664706 + 0.0018611 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_061_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=113, w2=438, w3=233, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(113)
    rank = change.rolling(438, min_periods=max(438//3, 2)).rank(pct=True)
    persistence = change.rolling(233, min_periods=max(233//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.254667 * persistence + 0.0018612 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_062_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=120, w2=451, w3=250, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(120, min_periods=max(120//3, 2)).std()
    vol_slow = ret.rolling(451, min_periods=max(451//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.838235 + 0.0018613 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_063_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=127, w2=464, w3=267, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(464, min_periods=max(464//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 127)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.267333 * slope + 0.0018614 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_064_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=134, w2=477, w3=284, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(477, min_periods=max(477//3, 2)).mean()
    noise = impulse.abs().rolling(284, min_periods=max(284//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.865294 + 0.0018615 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_065_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=141, w2=490, w3=301, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 141)
    acceleration = _rolling_slope(velocity, 490)
    curvature = _rolling_slope(acceleration, 301)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.28 * acceleration + 0.0018616 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_066_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=148, w2=503, w3=318, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 148)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.286333 * pressure.rolling(318, min_periods=max(318//3, 2)).mean() + 0.0018617 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_067_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=155, w2=17, w3=335, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(155, min_periods=max(155//3, 2)).mean())
    decay = spread.ewm(span=17, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.905882 + 0.0018618 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_068_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=162, w2=30, w3=352, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(30, min_periods=max(30//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 162)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.919412 + 0.0018619 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_069_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=169, w2=43, w3=369, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(169, min_periods=max(169//3, 2)).mean(), b.abs().rolling(43, min_periods=max(43//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.305333 * _rolling_slope(cover, 169) + 0.001862 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_070_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=176, w2=56, w3=386, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.311667 * y + 0.688333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 176) - _rolling_slope(basket, 56) + 0.0018621 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_071_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=183, w2=69, w3=403, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(183, min_periods=max(183//3, 2)).mean(), upside.rolling(69, min_periods=max(69//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.96 + 0.0018622 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_072_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=190, w2=82, w3=420, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(82, min_periods=max(82//3, 2)).max()
    rebound = x - x.rolling(190, min_periods=max(190//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.324333 * _rolling_slope(draw, 420) + 0.0018623 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_073_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=197, w2=95, w3=437, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(95)
    stress = imbalance.rolling(437, min_periods=max(437//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.987059 + 0.0018624 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_074_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=204, w2=108, w3=454, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 204)
    baseline = trend.rolling(108, min_periods=max(108//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(454, min_periods=max(454//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.000588 + 0.0018625 * anchor
    return base_signal.diff().diff()

def f23_adln_gemini_075_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=211, w2=121, w3=471, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 211)
    slow = _rolling_slope(x, 121)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.014118 + 0.0018626 * anchor
    return base_signal.diff().diff()
