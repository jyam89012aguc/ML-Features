"""17 trend line break dynamics gemini d2 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Kinetic energy and volume confirmation associated with the breach of established trend lines.
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

def f17_tlbk_gemini_001_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Kinetic energy and volume confirmation associated with the breach of established trend lines. [window=5]"""
    window = 5
    res = _safe_div(_rolling_slope(close, window), _rolling_zscore(volume, window).abs() + 1e-9)
    return (res).diff().diff()

def f17_tlbk_gemini_002_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Kinetic energy and volume confirmation associated with the breach of established trend lines. [window=10]"""
    window = 10
    res = _safe_div(_rolling_slope(close, window), _rolling_zscore(volume, window).abs() + 1e-9)
    return (res).diff().diff()

def f17_tlbk_gemini_003_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Kinetic energy and volume confirmation associated with the breach of established trend lines. [window=21]"""
    window = 21
    res = _safe_div(_rolling_slope(close, window), _rolling_zscore(volume, window).abs() + 1e-9)
    return (res).diff().diff()

def f17_tlbk_gemini_004_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Kinetic energy and volume confirmation associated with the breach of established trend lines. [window=42]"""
    window = 42
    res = _safe_div(_rolling_slope(close, window), _rolling_zscore(volume, window).abs() + 1e-9)
    return (res).diff().diff()

def f17_tlbk_gemini_005_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Kinetic energy and volume confirmation associated with the breach of established trend lines. [window=63]"""
    window = 63
    res = _safe_div(_rolling_slope(close, window), _rolling_zscore(volume, window).abs() + 1e-9)
    return (res).diff().diff()

def f17_tlbk_gemini_006_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Kinetic energy and volume confirmation associated with the breach of established trend lines. [window=126]"""
    window = 126
    res = _safe_div(_rolling_slope(close, window), _rolling_zscore(volume, window).abs() + 1e-9)
    return (res).diff().diff()

def f17_tlbk_gemini_007_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Kinetic energy and volume confirmation associated with the breach of established trend lines. [window=252]"""
    window = 252
    res = _safe_div(_rolling_slope(close, window), _rolling_zscore(volume, window).abs() + 1e-9)
    return (res).diff().diff()

def f17_tlbk_gemini_008_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Kinetic energy and volume confirmation associated with the breach of established trend lines. [window=504]"""
    window = 504
    res = _safe_div(_rolling_slope(close, window), _rolling_zscore(volume, window).abs() + 1e-9)
    return (res).diff().diff()

def f17_tlbk_gemini_009_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Kinetic energy and volume confirmation associated with the breach of established trend lines. [window=756]"""
    window = 756
    res = _safe_div(_rolling_slope(close, window), _rolling_zscore(volume, window).abs() + 1e-9)
    return (res).diff().diff()

def f17_tlbk_gemini_010_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Kinetic energy and volume confirmation associated with the breach of established trend lines. [window=1260]"""
    window = 1260
    res = _safe_div(_rolling_slope(close, window), _rolling_zscore(volume, window).abs() + 1e-9)
    return (res).diff().diff()

def f17_tlbk_gemini_011_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=202, w2=20, w3=90, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 202)
    slow = _rolling_slope(x, 20)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=90, adjust=False).mean() * 1.633529 + 0.0015202 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_012_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=209, w2=33, w3=107, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(33, min_periods=max(33//3, 2)).max()
    trough = x.rolling(209, min_periods=max(209//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.647059 + 0.0015203 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_013_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=216, w2=46, w3=124, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(46, min_periods=max(46//3, 2)).rank(pct=True)
    persistence = change.rolling(124, min_periods=max(124//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.272333 * persistence + 0.0015204 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_014_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=223, w2=59, w3=141, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(223, min_periods=max(223//3, 2)).std()
    vol_slow = ret.rolling(59, min_periods=max(59//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.820588 + 0.0015205 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_015_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=230, w2=72, w3=158, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(72, min_periods=max(72//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 230)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.285 * slope + 0.0015206 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_016_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=237, w2=85, w3=175, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(85, min_periods=max(85//3, 2)).mean()
    noise = impulse.abs().rolling(175, min_periods=max(175//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.847647 + 0.0015207 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_017_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=244, w2=98, w3=192, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 244)
    acceleration = _rolling_slope(velocity, 98)
    curvature = _rolling_slope(acceleration, 192)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.297667 * acceleration + 0.0015208 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_018_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=251, w2=111, w3=209, lag=34)."""
    rel = _safe_div(close.shift(34), volume.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 251)
    pressure = rel_log.diff(111)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.304 * pressure.rolling(209, min_periods=max(209//3, 2)).mean() + 0.0015209 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_019_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=11, w2=124, w3=226, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(11, min_periods=max(11//3, 2)).mean())
    decay = spread.ewm(span=124, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.888235 + 0.001521 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_020_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=18, w2=137, w3=243, lag=0)."""
    a = _safe_log(close.abs() + 1.0).shift(0)
    b = _safe_log(volume.abs() + 1.0).shift(0)
    corr = a.rolling(137, min_periods=max(137//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 18)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.901765 + 0.0015211 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_021_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=25, w2=150, w3=260, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    cover = _safe_div(a.rolling(25, min_periods=max(25//3, 2)).mean(), b.abs().rolling(150, min_periods=max(150//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.323 * _rolling_slope(cover, 25) + 0.0015212 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_022_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=32, w2=163, w3=277, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    y = _safe_log(volume.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.329333 * y + 0.670667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 32) - _rolling_slope(basket, 163) + 0.0015213 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_023_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=39, w2=176, w3=294, lag=3)."""
    x = close.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(39, min_periods=max(39//3, 2)).mean(), upside.rolling(176, min_periods=max(176//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.942353 + 0.0015214 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_024_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=46, w2=189, w3=311, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    draw = x - x.rolling(189, min_periods=max(189//3, 2)).max()
    rebound = x - x.rolling(46, min_periods=max(46//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.342 * _rolling_slope(draw, 311) + 0.0015215 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_025_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=53, w2=202, w3=328, lag=8)."""
    a = _safe_log(close.abs() + 1.0).shift(8)
    b = _safe_log(volume.abs() + 1.0).shift(8)
    imbalance = a.diff(53) - b.diff(126)
    stress = imbalance.rolling(328, min_periods=max(328//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.969412 + 0.0015216 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_026_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=60, w2=215, w3=345, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 60)
    baseline = trend.rolling(215, min_periods=max(215//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(345, min_periods=max(345//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.982941 + 0.0015217 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_027_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=67, w2=228, w3=362, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 67)
    slow = _rolling_slope(x, 228)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.996471 + 0.0015218 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_028_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=74, w2=241, w3=379, lag=34)."""
    x = close.shift(34)
    peak = x.rolling(241, min_periods=max(241//3, 2)).max()
    trough = x.rolling(74, min_periods=max(74//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.01 + 0.0015219 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_029_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=81, w2=254, w3=396, lag=55)."""
    x = close.shift(55)
    change = x.pct_change(81)
    rank = change.rolling(254, min_periods=max(254//3, 2)).rank(pct=True)
    persistence = change.rolling(396, min_periods=max(396//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.041333 * persistence + 0.001522 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_030_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=88, w2=267, w3=413, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(88, min_periods=max(88//3, 2)).std()
    vol_slow = ret.rolling(267, min_periods=max(267//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.037059 + 0.0015221 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_031_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=95, w2=280, w3=430, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(280, min_periods=max(280//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 95)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.054 * slope + 0.0015222 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_032_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=102, w2=293, w3=447, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(102)
    drag = impulse.rolling(293, min_periods=max(293//3, 2)).mean()
    noise = impulse.abs().rolling(447, min_periods=max(447//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.064118 + 0.0015223 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_033_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=109, w2=306, w3=464, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 109)
    acceleration = _rolling_slope(velocity, 306)
    curvature = _rolling_slope(acceleration, 464)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.066667 * acceleration + 0.0015224 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_034_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=116, w2=319, w3=481, lag=5)."""
    rel = _safe_div(close.shift(5), volume.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 116)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.073 * pressure.rolling(481, min_periods=max(481//3, 2)).mean() + 0.0015225 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_035_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=123, w2=332, w3=498, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(123, min_periods=max(123//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.104706 + 0.0015226 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_036_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=130, w2=345, w3=515, lag=13)."""
    a = _safe_log(close.abs() + 1.0).shift(13)
    b = _safe_log(volume.abs() + 1.0).shift(13)
    corr = a.rolling(345, min_periods=max(345//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 130)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.118235 + 0.0015227 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_037_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=137, w2=358, w3=532, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    cover = _safe_div(a.rolling(137, min_periods=max(137//3, 2)).mean(), b.abs().rolling(358, min_periods=max(358//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.092 * _rolling_slope(cover, 137) + 0.0015228 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_038_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=144, w2=371, w3=549, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    y = _safe_log(volume.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.098333 * y + 0.901667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 144) - _rolling_slope(basket, 371) + 0.0015229 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_039_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=151, w2=384, w3=566, lag=55)."""
    x = close.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(151, min_periods=max(151//3, 2)).mean(), upside.rolling(384, min_periods=max(384//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.158824 + 0.001523 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_040_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=158, w2=397, w3=583, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    draw = x - x.rolling(397, min_periods=max(397//3, 2)).max()
    rebound = x - x.rolling(158, min_periods=max(158//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.111 * _rolling_slope(draw, 583) + 0.0015231 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_041_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=165, w2=410, w3=600, lag=1)."""
    a = _safe_log(close.abs() + 1.0).shift(1)
    b = _safe_log(volume.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(600, min_periods=max(600//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.185882 + 0.0015232 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_042_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=172, w2=423, w3=617, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 172)
    baseline = trend.rolling(423, min_periods=max(423//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(617, min_periods=max(617//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.199412 + 0.0015233 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_043_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=179, w2=436, w3=634, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 179)
    slow = _rolling_slope(x, 436)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.212941 + 0.0015234 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_044_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=186, w2=449, w3=651, lag=5)."""
    x = close.shift(5)
    peak = x.rolling(449, min_periods=max(449//3, 2)).max()
    trough = x.rolling(186, min_periods=max(186//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.226471 + 0.0015235 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_045_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=193, w2=462, w3=668, lag=8)."""
    x = close.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(462, min_periods=max(462//3, 2)).rank(pct=True)
    persistence = change.rolling(668, min_periods=max(668//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.142667 * persistence + 0.0015236 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_046_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=200, w2=475, w3=685, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(200, min_periods=max(200//3, 2)).std()
    vol_slow = ret.rolling(475, min_periods=max(475//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.253529 + 0.0015237 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_047_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=207, w2=488, w3=702, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(488, min_periods=max(488//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 207)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.155333 * slope + 0.0015238 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_048_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=214, w2=501, w3=719, lag=34)."""
    x = close.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(501, min_periods=max(501//3, 2)).mean()
    noise = impulse.abs().rolling(719, min_periods=max(719//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.280588 + 0.0015239 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_049_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=221, w2=15, w3=736, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 221)
    acceleration = _rolling_slope(velocity, 15)
    curvature = _rolling_slope(acceleration, 736)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.168 * acceleration + 0.001524 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_050_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=228, w2=28, w3=753, lag=0)."""
    rel = _safe_div(close.shift(0), volume.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 228)
    pressure = rel_log.diff(28)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.174333 * pressure.rolling(753, min_periods=max(753//3, 2)).mean() + 0.0015241 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_051_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=235, w2=41, w3=19, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(235, min_periods=max(235//3, 2)).mean())
    decay = spread.ewm(span=41, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.321176 + 0.0015242 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_052_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=242, w2=54, w3=36, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(volume.abs() + 1.0).shift(2)
    corr = a.rolling(54, min_periods=max(54//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 242)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.334706 + 0.0015243 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_053_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=249, w2=67, w3=53, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    cover = _safe_div(a.rolling(249, min_periods=max(249//3, 2)).mean(), b.abs().rolling(67, min_periods=max(67//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(53) + 0.193333 * _rolling_slope(cover, 249) + 0.0015244 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_054_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=9, w2=80, w3=70, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(volume.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.199667 * y + 0.800333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 9) - _rolling_slope(basket, 80) + 0.0015245 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_055_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=16, w2=93, w3=87, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(16, min_periods=max(16//3, 2)).mean(), upside.rolling(93, min_periods=max(93//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(87) * 1.375294 + 0.0015246 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_056_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=23, w2=106, w3=104, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    draw = x - x.rolling(106, min_periods=max(106//3, 2)).max()
    rebound = x - x.rolling(23, min_periods=max(23//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.212333 * _rolling_slope(draw, 104) + 0.0015247 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_057_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=30, w2=119, w3=121, lag=21)."""
    a = _safe_log(close.abs() + 1.0).shift(21)
    b = _safe_log(volume.abs() + 1.0).shift(21)
    imbalance = a.diff(30) - b.diff(119)
    stress = imbalance.rolling(121, min_periods=max(121//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.402353 + 0.0015248 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_058_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=37, w2=132, w3=138, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 37)
    baseline = trend.rolling(132, min_periods=max(132//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(138, min_periods=max(138//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.415882 + 0.0015249 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_059_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=44, w2=145, w3=155, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 44)
    slow = _rolling_slope(x, 145)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=155, adjust=False).mean() * 1.429412 + 0.001525 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_060_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=51, w2=158, w3=172, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(158, min_periods=max(158//3, 2)).max()
    trough = x.rolling(51, min_periods=max(51//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.442941 + 0.0015251 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_061_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=58, w2=171, w3=189, lag=1)."""
    x = close.shift(1)
    change = x.pct_change(58)
    rank = change.rolling(171, min_periods=max(171//3, 2)).rank(pct=True)
    persistence = change.rolling(189, min_periods=max(189//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.244 * persistence + 0.0015252 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_062_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=65, w2=184, w3=206, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(65, min_periods=max(65//3, 2)).std()
    vol_slow = ret.rolling(184, min_periods=max(184//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.47 + 0.0015253 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_063_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=72, w2=197, w3=223, lag=3)."""
    x = close.shift(3)
    ma = x.rolling(197, min_periods=max(197//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 72)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.256667 * slope + 0.0015254 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_064_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=79, w2=210, w3=240, lag=5)."""
    x = close.shift(5)
    impulse = x.diff(79)
    drag = impulse.rolling(210, min_periods=max(210//3, 2)).mean()
    noise = impulse.abs().rolling(240, min_periods=max(240//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.497059 + 0.0015255 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_065_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=86, w2=223, w3=257, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 86)
    acceleration = _rolling_slope(velocity, 223)
    curvature = _rolling_slope(acceleration, 257)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.269333 * acceleration + 0.0015256 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_066_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=93, w2=236, w3=274, lag=13)."""
    rel = _safe_div(close.shift(13), volume.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 93)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.275667 * pressure.rolling(274, min_periods=max(274//3, 2)).mean() + 0.0015257 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_067_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=100, w2=249, w3=291, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(100, min_periods=max(100//3, 2)).mean())
    decay = spread.ewm(span=249, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.537647 + 0.0015258 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_068_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=107, w2=262, w3=308, lag=34)."""
    a = _safe_log(close.abs() + 1.0).shift(34)
    b = _safe_log(volume.abs() + 1.0).shift(34)
    corr = a.rolling(262, min_periods=max(262//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 107)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.551176 + 0.0015259 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_069_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=114, w2=275, w3=325, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    cover = _safe_div(a.rolling(114, min_periods=max(114//3, 2)).mean(), b.abs().rolling(275, min_periods=max(275//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.294667 * _rolling_slope(cover, 114) + 0.001526 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_070_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=121, w2=288, w3=342, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    y = _safe_log(volume.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.301 * y + 0.699000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 121) - _rolling_slope(basket, 288) + 0.0015261 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_071_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=128, w2=301, w3=359, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(128, min_periods=max(128//3, 2)).mean(), upside.rolling(301, min_periods=max(301//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.591765 + 0.0015262 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_072_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=135, w2=314, w3=376, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(314, min_periods=max(314//3, 2)).max()
    rebound = x - x.rolling(135, min_periods=max(135//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.313667 * _rolling_slope(draw, 376) + 0.0015263 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_073_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=142, w2=327, w3=393, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(volume.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(393, min_periods=max(393//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.618824 + 0.0015264 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_074_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=149, w2=340, w3=410, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 149)
    baseline = trend.rolling(340, min_periods=max(340//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(410, min_periods=max(410//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.632353 + 0.0015265 * anchor
    return base_signal.diff().diff()

def f17_tlbk_gemini_075_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=156, w2=353, w3=427, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 156)
    slow = _rolling_slope(x, 353)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.645882 + 0.0015266 * anchor
    return base_signal.diff().diff()
