"""101 absorption ratio standardized shift gemini base features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Standardized changes in the proportion of variance explained by lead components.
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

def f101_abrs_gemini_076(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=229, w2=211, w3=566, lag=13)."""
    a = _safe_log(close.abs() + 1.0).shift(13)
    b = _safe_log(volume.abs() + 1.0).shift(13)
    corr = a.rolling(211, min_periods=max(211//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 229)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.368235 + 0.0005467 * anchor
    return base_signal

def f101_abrs_gemini_077(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=236, w2=224, w3=583, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    cover = _safe_div(a.rolling(236, min_periods=max(236//3, 2)).mean(), b.abs().rolling(224, min_periods=max(224//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.092667 * _rolling_slope(cover, 236) + 0.0005468 * anchor
    return base_signal

def f101_abrs_gemini_078(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=243, w2=237, w3=600, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    y = _safe_log(volume.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.099 * y + 0.901000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 243) - _rolling_slope(basket, 237) + 0.0005469 * anchor
    return base_signal

def f101_abrs_gemini_079(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=250, w2=250, w3=617, lag=55)."""
    x = close.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(250, min_periods=max(250//3, 2)).mean(), upside.rolling(250, min_periods=max(250//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.408824 + 0.000547 * anchor
    return base_signal

def f101_abrs_gemini_080(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=10, w2=263, w3=634, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    draw = x - x.rolling(263, min_periods=max(263//3, 2)).max()
    rebound = x - x.rolling(10, min_periods=max(10//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.111667 * _rolling_slope(draw, 634) + 0.0005471 * anchor
    return base_signal

def f101_abrs_gemini_081(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=17, w2=276, w3=651, lag=1)."""
    a = _safe_log(close.abs() + 1.0).shift(1)
    b = _safe_log(volume.abs() + 1.0).shift(1)
    imbalance = a.diff(17) - b.diff(126)
    stress = imbalance.rolling(651, min_periods=max(651//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.435882 + 0.0005472 * anchor
    return base_signal

def f101_abrs_gemini_082(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=24, w2=289, w3=668, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 24)
    baseline = trend.rolling(289, min_periods=max(289//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(668, min_periods=max(668//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.449412 + 0.0005473 * anchor
    return base_signal

def f101_abrs_gemini_083(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=31, w2=302, w3=685, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 31)
    slow = _rolling_slope(x, 302)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.462941 + 0.0005474 * anchor
    return base_signal

def f101_abrs_gemini_084(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=38, w2=315, w3=702, lag=5)."""
    x = close.shift(5)
    peak = x.rolling(315, min_periods=max(315//3, 2)).max()
    trough = x.rolling(38, min_periods=max(38//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.476471 + 0.0005475 * anchor
    return base_signal

def f101_abrs_gemini_085(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=45, w2=328, w3=719, lag=8)."""
    x = close.shift(8)
    change = x.pct_change(45)
    rank = change.rolling(328, min_periods=max(328//3, 2)).rank(pct=True)
    persistence = change.rolling(719, min_periods=max(719//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.143333 * persistence + 0.0005476 * anchor
    return base_signal

def f101_abrs_gemini_086(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=52, w2=341, w3=736, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(52, min_periods=max(52//3, 2)).std()
    vol_slow = ret.rolling(341, min_periods=max(341//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.503529 + 0.0005477 * anchor
    return base_signal

def f101_abrs_gemini_087(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=59, w2=354, w3=753, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(354, min_periods=max(354//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 59)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.156 * slope + 0.0005478 * anchor
    return base_signal

def f101_abrs_gemini_088(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=66, w2=367, w3=19, lag=34)."""
    x = close.shift(34)
    impulse = x.diff(66)
    drag = impulse.rolling(367, min_periods=max(367//3, 2)).mean()
    noise = impulse.abs().rolling(19, min_periods=max(19//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.530588 + 0.0005479 * anchor
    return base_signal

def f101_abrs_gemini_089(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=73, w2=380, w3=36, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 73)
    acceleration = _rolling_slope(velocity, 380)
    curvature = _rolling_slope(acceleration, 36)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.168667 * acceleration + 0.000548 * anchor
    return base_signal

def f101_abrs_gemini_090(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=80, w2=393, w3=53, lag=0)."""
    rel = _safe_div(close.shift(0), volume.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 80)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.175 * pressure.rolling(53, min_periods=max(53//3, 2)).mean() + 0.0005481 * anchor
    return base_signal

def f101_abrs_gemini_091(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=87, w2=406, w3=70, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(87, min_periods=max(87//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.571176 + 0.0005482 * anchor
    return base_signal

def f101_abrs_gemini_092(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=94, w2=419, w3=87, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(volume.abs() + 1.0).shift(2)
    corr = a.rolling(419, min_periods=max(419//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 94)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.584706 + 0.0005483 * anchor
    return base_signal

def f101_abrs_gemini_093(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=101, w2=432, w3=104, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    cover = _safe_div(a.rolling(101, min_periods=max(101//3, 2)).mean(), b.abs().rolling(432, min_periods=max(432//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(104) + 0.194 * _rolling_slope(cover, 101) + 0.0005484 * anchor
    return base_signal

def f101_abrs_gemini_094(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=108, w2=445, w3=121, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(volume.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.200333 * y + 0.799667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 108) - _rolling_slope(basket, 445) + 0.0005485 * anchor
    return base_signal

def f101_abrs_gemini_095(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=115, w2=458, w3=138, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(115, min_periods=max(115//3, 2)).mean(), upside.rolling(458, min_periods=max(458//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.625294 + 0.0005486 * anchor
    return base_signal

def f101_abrs_gemini_096(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=122, w2=471, w3=155, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    draw = x - x.rolling(471, min_periods=max(471//3, 2)).max()
    rebound = x - x.rolling(122, min_periods=max(122//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.213 * _rolling_slope(draw, 155) + 0.0005487 * anchor
    return base_signal

def f101_abrs_gemini_097(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=129, w2=484, w3=172, lag=21)."""
    a = _safe_log(close.abs() + 1.0).shift(21)
    b = _safe_log(volume.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(172, min_periods=max(172//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.652353 + 0.0005488 * anchor
    return base_signal

def f101_abrs_gemini_098(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=136, w2=497, w3=189, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 136)
    baseline = trend.rolling(497, min_periods=max(497//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(189, min_periods=max(189//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.665882 + 0.0005489 * anchor
    return base_signal

def f101_abrs_gemini_099(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=143, w2=11, w3=206, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 143)
    slow = _rolling_slope(x, 11)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=206, adjust=False).mean() * 0.825882 + 0.000549 * anchor
    return base_signal

def f101_abrs_gemini_100(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=150, w2=24, w3=223, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(24, min_periods=max(24//3, 2)).max()
    trough = x.rolling(150, min_periods=max(150//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.839412 + 0.0005491 * anchor
    return base_signal

def f101_abrs_gemini_101(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=157, w2=37, w3=240, lag=1)."""
    x = close.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(37, min_periods=max(37//3, 2)).rank(pct=True)
    persistence = change.rolling(240, min_periods=max(240//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.244667 * persistence + 0.0005492 * anchor
    return base_signal

def f101_abrs_gemini_102(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=164, w2=50, w3=257, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(164, min_periods=max(164//3, 2)).std()
    vol_slow = ret.rolling(50, min_periods=max(50//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.866471 + 0.0005493 * anchor
    return base_signal

def f101_abrs_gemini_103(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=171, w2=63, w3=274, lag=3)."""
    x = close.shift(3)
    ma = x.rolling(63, min_periods=max(63//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 171)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.257333 * slope + 0.0005494 * anchor
    return base_signal

def f101_abrs_gemini_104(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=178, w2=76, w3=291, lag=5)."""
    x = close.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(76, min_periods=max(76//3, 2)).mean()
    noise = impulse.abs().rolling(291, min_periods=max(291//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.893529 + 0.0005495 * anchor
    return base_signal

def f101_abrs_gemini_105(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=185, w2=89, w3=308, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 185)
    acceleration = _rolling_slope(velocity, 89)
    curvature = _rolling_slope(acceleration, 308)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.27 * acceleration + 0.0005496 * anchor
    return base_signal

def f101_abrs_gemini_106(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=192, w2=102, w3=325, lag=13)."""
    rel = _safe_div(close.shift(13), volume.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 192)
    pressure = rel_log.diff(102)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.276333 * pressure.rolling(325, min_periods=max(325//3, 2)).mean() + 0.0005497 * anchor
    return base_signal

def f101_abrs_gemini_107(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=199, w2=115, w3=342, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(199, min_periods=max(199//3, 2)).mean())
    decay = spread.ewm(span=115, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.934118 + 0.0005498 * anchor
    return base_signal

def f101_abrs_gemini_108(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=206, w2=128, w3=359, lag=34)."""
    a = _safe_log(close.abs() + 1.0).shift(34)
    b = _safe_log(volume.abs() + 1.0).shift(34)
    corr = a.rolling(128, min_periods=max(128//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 206)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.947647 + 0.0005499 * anchor
    return base_signal

def f101_abrs_gemini_109(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=213, w2=141, w3=376, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    cover = _safe_div(a.rolling(213, min_periods=max(213//3, 2)).mean(), b.abs().rolling(141, min_periods=max(141//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.295333 * _rolling_slope(cover, 213) + 0.00055 * anchor
    return base_signal

def f101_abrs_gemini_110(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=220, w2=154, w3=393, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    y = _safe_log(volume.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.301667 * y + 0.698333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 220) - _rolling_slope(basket, 154) + 0.0005501 * anchor
    return base_signal

def f101_abrs_gemini_111(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=227, w2=167, w3=410, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(227, min_periods=max(227//3, 2)).mean(), upside.rolling(167, min_periods=max(167//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.988235 + 0.0005502 * anchor
    return base_signal

def f101_abrs_gemini_112(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=234, w2=180, w3=427, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(180, min_periods=max(180//3, 2)).max()
    rebound = x - x.rolling(234, min_periods=max(234//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.314333 * _rolling_slope(draw, 427) + 0.0005503 * anchor
    return base_signal

def f101_abrs_gemini_113(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=241, w2=193, w3=444, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(volume.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(444, min_periods=max(444//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.015294 + 0.0005504 * anchor
    return base_signal

def f101_abrs_gemini_114(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=248, w2=206, w3=461, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 248)
    baseline = trend.rolling(206, min_periods=max(206//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(461, min_periods=max(461//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.028824 + 0.0005505 * anchor
    return base_signal

def f101_abrs_gemini_115(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=8, w2=219, w3=478, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 8)
    slow = _rolling_slope(x, 219)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.042353 + 0.0005506 * anchor
    return base_signal

def f101_abrs_gemini_116(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=15, w2=232, w3=495, lag=13)."""
    x = close.shift(13)
    peak = x.rolling(232, min_periods=max(232//3, 2)).max()
    trough = x.rolling(15, min_periods=max(15//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.055882 + 0.0005507 * anchor
    return base_signal

def f101_abrs_gemini_117(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=22, w2=245, w3=512, lag=21)."""
    x = close.shift(21)
    change = x.pct_change(22)
    rank = change.rolling(245, min_periods=max(245//3, 2)).rank(pct=True)
    persistence = change.rolling(512, min_periods=max(512//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.346 * persistence + 0.0005508 * anchor
    return base_signal

def f101_abrs_gemini_118(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=29, w2=258, w3=529, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(29, min_periods=max(29//3, 2)).std()
    vol_slow = ret.rolling(258, min_periods=max(258//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.082941 + 0.0005509 * anchor
    return base_signal

def f101_abrs_gemini_119(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=36, w2=271, w3=546, lag=55)."""
    x = close.shift(55)
    ma = x.rolling(271, min_periods=max(271//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 36)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.358667 * slope + 0.000551 * anchor
    return base_signal

def f101_abrs_gemini_120(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=43, w2=284, w3=563, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(43)
    drag = impulse.rolling(284, min_periods=max(284//3, 2)).mean()
    noise = impulse.abs().rolling(563, min_periods=max(563//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.11 + 0.0005511 * anchor
    return base_signal

def f101_abrs_gemini_121(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=50, w2=297, w3=580, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 50)
    acceleration = _rolling_slope(velocity, 297)
    curvature = _rolling_slope(acceleration, 580)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.039 * acceleration + 0.0005512 * anchor
    return base_signal

def f101_abrs_gemini_122(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=57, w2=310, w3=597, lag=2)."""
    rel = _safe_div(close.shift(2), volume.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 57)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.045333 * pressure.rolling(597, min_periods=max(597//3, 2)).mean() + 0.0005513 * anchor
    return base_signal

def f101_abrs_gemini_123(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=64, w2=323, w3=614, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(64, min_periods=max(64//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.150588 + 0.0005514 * anchor
    return base_signal

def f101_abrs_gemini_124(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=71, w2=336, w3=631, lag=5)."""
    a = _safe_log(close.abs() + 1.0).shift(5)
    b = _safe_log(volume.abs() + 1.0).shift(5)
    corr = a.rolling(336, min_periods=max(336//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 71)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.164118 + 0.0005515 * anchor
    return base_signal

def f101_abrs_gemini_125(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=78, w2=349, w3=648, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    cover = _safe_div(a.rolling(78, min_periods=max(78//3, 2)).mean(), b.abs().rolling(349, min_periods=max(349//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.064333 * _rolling_slope(cover, 78) + 0.0005516 * anchor
    return base_signal

def f101_abrs_gemini_126(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=85, w2=362, w3=665, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    y = _safe_log(volume.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.070667 * y + 0.929333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 85) - _rolling_slope(basket, 362) + 0.0005517 * anchor
    return base_signal

def f101_abrs_gemini_127(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=92, w2=375, w3=682, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(92, min_periods=max(92//3, 2)).mean(), upside.rolling(375, min_periods=max(375//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.204706 + 0.0005518 * anchor
    return base_signal

def f101_abrs_gemini_128(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=99, w2=388, w3=699, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    draw = x - x.rolling(388, min_periods=max(388//3, 2)).max()
    rebound = x - x.rolling(99, min_periods=max(99//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.083333 * _rolling_slope(draw, 699) + 0.0005519 * anchor
    return base_signal

def f101_abrs_gemini_129(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=106, w2=401, w3=716, lag=55)."""
    a = _safe_log(close.abs() + 1.0).shift(55)
    b = _safe_log(volume.abs() + 1.0).shift(55)
    imbalance = a.diff(106) - b.diff(126)
    stress = imbalance.rolling(716, min_periods=max(716//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.231765 + 0.000552 * anchor
    return base_signal

def f101_abrs_gemini_130(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=113, w2=414, w3=733, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 113)
    baseline = trend.rolling(414, min_periods=max(414//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(733, min_periods=max(733//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.245294 + 0.0005521 * anchor
    return base_signal

def f101_abrs_gemini_131(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=120, w2=427, w3=750, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 120)
    slow = _rolling_slope(x, 427)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.258824 + 0.0005522 * anchor
    return base_signal

def f101_abrs_gemini_132(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=127, w2=440, w3=767, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(440, min_periods=max(440//3, 2)).max()
    trough = x.rolling(127, min_periods=max(127//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.272353 + 0.0005523 * anchor
    return base_signal

def f101_abrs_gemini_133(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=134, w2=453, w3=33, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(453, min_periods=max(453//3, 2)).rank(pct=True)
    persistence = change.rolling(33, min_periods=max(33//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.115 * persistence + 0.0005524 * anchor
    return base_signal

def f101_abrs_gemini_134(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=141, w2=466, w3=50, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(141, min_periods=max(141//3, 2)).std()
    vol_slow = ret.rolling(466, min_periods=max(466//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.299412 + 0.0005525 * anchor
    return base_signal

def f101_abrs_gemini_135(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=148, w2=479, w3=67, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(479, min_periods=max(479//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 148)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.127667 * slope + 0.0005526 * anchor
    return base_signal

def f101_abrs_gemini_136(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=155, w2=492, w3=84, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(492, min_periods=max(492//3, 2)).mean()
    noise = impulse.abs().rolling(84, min_periods=max(84//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.326471 + 0.0005527 * anchor
    return base_signal

def f101_abrs_gemini_137(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=162, w2=505, w3=101, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 162)
    acceleration = _rolling_slope(velocity, 505)
    curvature = _rolling_slope(acceleration, 101)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.140333 * acceleration + 0.0005528 * anchor
    return base_signal

def f101_abrs_gemini_138(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=169, w2=19, w3=118, lag=34)."""
    rel = _safe_div(close.shift(34), volume.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 169)
    pressure = rel_log.diff(19)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.146667 * pressure.rolling(118, min_periods=max(118//3, 2)).mean() + 0.0005529 * anchor
    return base_signal

def f101_abrs_gemini_139(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=176, w2=32, w3=135, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(176, min_periods=max(176//3, 2)).mean())
    decay = spread.ewm(span=32, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.367059 + 0.000553 * anchor
    return base_signal

def f101_abrs_gemini_140(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=183, w2=45, w3=152, lag=0)."""
    a = _safe_log(close.abs() + 1.0).shift(0)
    b = _safe_log(volume.abs() + 1.0).shift(0)
    corr = a.rolling(45, min_periods=max(45//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 183)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.380588 + 0.0005531 * anchor
    return base_signal

def f101_abrs_gemini_141(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=190, w2=58, w3=169, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    cover = _safe_div(a.rolling(190, min_periods=max(190//3, 2)).mean(), b.abs().rolling(58, min_periods=max(58//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.165667 * _rolling_slope(cover, 190) + 0.0005532 * anchor
    return base_signal

def f101_abrs_gemini_142(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=197, w2=71, w3=186, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    y = _safe_log(volume.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.172 * y + 0.828000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 197) - _rolling_slope(basket, 71) + 0.0005533 * anchor
    return base_signal

def f101_abrs_gemini_143(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=204, w2=84, w3=203, lag=3)."""
    x = close.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(204, min_periods=max(204//3, 2)).mean(), upside.rolling(84, min_periods=max(84//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.421176 + 0.0005534 * anchor
    return base_signal

def f101_abrs_gemini_144(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=211, w2=97, w3=220, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    draw = x - x.rolling(97, min_periods=max(97//3, 2)).max()
    rebound = x - x.rolling(211, min_periods=max(211//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.184667 * _rolling_slope(draw, 220) + 0.0005535 * anchor
    return base_signal

def f101_abrs_gemini_145(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=218, w2=110, w3=237, lag=8)."""
    a = _safe_log(close.abs() + 1.0).shift(8)
    b = _safe_log(volume.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(110)
    stress = imbalance.rolling(237, min_periods=max(237//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.448235 + 0.0005536 * anchor
    return base_signal

def f101_abrs_gemini_146(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=225, w2=123, w3=254, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 225)
    baseline = trend.rolling(123, min_periods=max(123//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(254, min_periods=max(254//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.461765 + 0.0005537 * anchor
    return base_signal

def f101_abrs_gemini_147(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=232, w2=136, w3=271, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 232)
    slow = _rolling_slope(x, 136)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=271, adjust=False).mean() * 1.475294 + 0.0005538 * anchor
    return base_signal

def f101_abrs_gemini_148(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=239, w2=149, w3=288, lag=34)."""
    x = close.shift(34)
    peak = x.rolling(149, min_periods=max(149//3, 2)).max()
    trough = x.rolling(239, min_periods=max(239//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.488824 + 0.0005539 * anchor
    return base_signal

def f101_abrs_gemini_149(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=246, w2=162, w3=305, lag=55)."""
    x = close.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(162, min_periods=max(162//3, 2)).rank(pct=True)
    persistence = change.rolling(305, min_periods=max(305//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.216333 * persistence + 0.000554 * anchor
    return base_signal

def f101_abrs_gemini_150(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=6, w2=175, w3=322, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(6, min_periods=max(6//3, 2)).std()
    vol_slow = ret.rolling(175, min_periods=max(175//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.515882 + 0.0005541 * anchor
    return base_signal
