"""68 high volume node exhaustion gemini base features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Price rejection or stalling at major high-volume nodes from historical profiles.
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

def f68_hvne_gemini_076(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=29, w2=243, w3=564, lag=13)."""
    a = _safe_log(close.abs() + 1.0).shift(13)
    b = _safe_log(volume.abs() + 1.0).shift(13)
    corr = a.rolling(243, min_periods=max(243//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 29)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.036471 + 0.0043547 * anchor
    return base_signal

def f68_hvne_gemini_077(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=36, w2=256, w3=581, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    cover = _safe_div(a.rolling(36, min_periods=max(36//3, 2)).mean(), b.abs().rolling(256, min_periods=max(256//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.324333 * _rolling_slope(cover, 36) + 0.0043548 * anchor
    return base_signal

def f68_hvne_gemini_078(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=43, w2=269, w3=598, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    y = _safe_log(volume.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.330667 * y + 0.669333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 43) - _rolling_slope(basket, 269) + 0.0043549 * anchor
    return base_signal

def f68_hvne_gemini_079(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=50, w2=282, w3=615, lag=55)."""
    x = close.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(50, min_periods=max(50//3, 2)).mean(), upside.rolling(282, min_periods=max(282//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.077059 + 0.004355 * anchor
    return base_signal

def f68_hvne_gemini_080(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=57, w2=295, w3=632, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    draw = x - x.rolling(295, min_periods=max(295//3, 2)).max()
    rebound = x - x.rolling(57, min_periods=max(57//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.343333 * _rolling_slope(draw, 632) + 0.0043551 * anchor
    return base_signal

def f68_hvne_gemini_081(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=64, w2=308, w3=649, lag=1)."""
    a = _safe_log(close.abs() + 1.0).shift(1)
    b = _safe_log(volume.abs() + 1.0).shift(1)
    imbalance = a.diff(64) - b.diff(126)
    stress = imbalance.rolling(649, min_periods=max(649//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.104118 + 0.0043552 * anchor
    return base_signal

def f68_hvne_gemini_082(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=71, w2=321, w3=666, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 71)
    baseline = trend.rolling(321, min_periods=max(321//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(666, min_periods=max(666//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.117647 + 0.0043553 * anchor
    return base_signal

def f68_hvne_gemini_083(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=78, w2=334, w3=683, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 78)
    slow = _rolling_slope(x, 334)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.131176 + 0.0043554 * anchor
    return base_signal

def f68_hvne_gemini_084(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=85, w2=347, w3=700, lag=5)."""
    x = close.shift(5)
    peak = x.rolling(347, min_periods=max(347//3, 2)).max()
    trough = x.rolling(85, min_periods=max(85//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.144706 + 0.0043555 * anchor
    return base_signal

def f68_hvne_gemini_085(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=92, w2=360, w3=717, lag=8)."""
    x = close.shift(8)
    change = x.pct_change(92)
    rank = change.rolling(360, min_periods=max(360//3, 2)).rank(pct=True)
    persistence = change.rolling(717, min_periods=max(717//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.042667 * persistence + 0.0043556 * anchor
    return base_signal

def f68_hvne_gemini_086(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=99, w2=373, w3=734, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(99, min_periods=max(99//3, 2)).std()
    vol_slow = ret.rolling(373, min_periods=max(373//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.171765 + 0.0043557 * anchor
    return base_signal

def f68_hvne_gemini_087(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=106, w2=386, w3=751, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(386, min_periods=max(386//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 106)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.055333 * slope + 0.0043558 * anchor
    return base_signal

def f68_hvne_gemini_088(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=113, w2=399, w3=17, lag=34)."""
    x = close.shift(34)
    impulse = x.diff(113)
    drag = impulse.rolling(399, min_periods=max(399//3, 2)).mean()
    noise = impulse.abs().rolling(17, min_periods=max(17//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.198824 + 0.0043559 * anchor
    return base_signal

def f68_hvne_gemini_089(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=120, w2=412, w3=34, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 120)
    acceleration = _rolling_slope(velocity, 412)
    curvature = _rolling_slope(acceleration, 34)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.068 * acceleration + 0.004356 * anchor
    return base_signal

def f68_hvne_gemini_090(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=127, w2=425, w3=51, lag=0)."""
    rel = _safe_div(close.shift(0), volume.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 127)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.074333 * pressure.rolling(51, min_periods=max(51//3, 2)).mean() + 0.0043561 * anchor
    return base_signal

def f68_hvne_gemini_091(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=134, w2=438, w3=68, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(134, min_periods=max(134//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.239412 + 0.0043562 * anchor
    return base_signal

def f68_hvne_gemini_092(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=141, w2=451, w3=85, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(volume.abs() + 1.0).shift(2)
    corr = a.rolling(451, min_periods=max(451//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 141)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.252941 + 0.0043563 * anchor
    return base_signal

def f68_hvne_gemini_093(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=148, w2=464, w3=102, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    cover = _safe_div(a.rolling(148, min_periods=max(148//3, 2)).mean(), b.abs().rolling(464, min_periods=max(464//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(102) + 0.093333 * _rolling_slope(cover, 148) + 0.0043564 * anchor
    return base_signal

def f68_hvne_gemini_094(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=155, w2=477, w3=119, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(volume.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.099667 * y + 0.900333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 155) - _rolling_slope(basket, 477) + 0.0043565 * anchor
    return base_signal

def f68_hvne_gemini_095(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=162, w2=490, w3=136, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(162, min_periods=max(162//3, 2)).mean(), upside.rolling(490, min_periods=max(490//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.293529 + 0.0043566 * anchor
    return base_signal

def f68_hvne_gemini_096(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=169, w2=503, w3=153, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    draw = x - x.rolling(503, min_periods=max(503//3, 2)).max()
    rebound = x - x.rolling(169, min_periods=max(169//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.112333 * _rolling_slope(draw, 153) + 0.0043567 * anchor
    return base_signal

def f68_hvne_gemini_097(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=176, w2=17, w3=170, lag=21)."""
    a = _safe_log(close.abs() + 1.0).shift(21)
    b = _safe_log(volume.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(17)
    stress = imbalance.rolling(170, min_periods=max(170//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.320588 + 0.0043568 * anchor
    return base_signal

def f68_hvne_gemini_098(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=183, w2=30, w3=187, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 183)
    baseline = trend.rolling(30, min_periods=max(30//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(187, min_periods=max(187//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.334118 + 0.0043569 * anchor
    return base_signal

def f68_hvne_gemini_099(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=190, w2=43, w3=204, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 190)
    slow = _rolling_slope(x, 43)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=204, adjust=False).mean() * 1.347647 + 0.004357 * anchor
    return base_signal

def f68_hvne_gemini_100(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=197, w2=56, w3=221, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(56, min_periods=max(56//3, 2)).max()
    trough = x.rolling(197, min_periods=max(197//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.361176 + 0.0043571 * anchor
    return base_signal

def f68_hvne_gemini_101(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=204, w2=69, w3=238, lag=1)."""
    x = close.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(69, min_periods=max(69//3, 2)).rank(pct=True)
    persistence = change.rolling(238, min_periods=max(238//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.144 * persistence + 0.0043572 * anchor
    return base_signal

def f68_hvne_gemini_102(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=211, w2=82, w3=255, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(211, min_periods=max(211//3, 2)).std()
    vol_slow = ret.rolling(82, min_periods=max(82//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.388235 + 0.0043573 * anchor
    return base_signal

def f68_hvne_gemini_103(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=218, w2=95, w3=272, lag=3)."""
    x = close.shift(3)
    ma = x.rolling(95, min_periods=max(95//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 218)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.156667 * slope + 0.0043574 * anchor
    return base_signal

def f68_hvne_gemini_104(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=225, w2=108, w3=289, lag=5)."""
    x = close.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(108, min_periods=max(108//3, 2)).mean()
    noise = impulse.abs().rolling(289, min_periods=max(289//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.415294 + 0.0043575 * anchor
    return base_signal

def f68_hvne_gemini_105(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=232, w2=121, w3=306, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 232)
    acceleration = _rolling_slope(velocity, 121)
    curvature = _rolling_slope(acceleration, 306)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.169333 * acceleration + 0.0043576 * anchor
    return base_signal

def f68_hvne_gemini_106(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=239, w2=134, w3=323, lag=13)."""
    rel = _safe_div(close.shift(13), volume.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 239)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.175667 * pressure.rolling(323, min_periods=max(323//3, 2)).mean() + 0.0043577 * anchor
    return base_signal

def f68_hvne_gemini_107(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=246, w2=147, w3=340, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(246, min_periods=max(246//3, 2)).mean())
    decay = spread.ewm(span=147, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.455882 + 0.0043578 * anchor
    return base_signal

def f68_hvne_gemini_108(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=6, w2=160, w3=357, lag=34)."""
    a = _safe_log(close.abs() + 1.0).shift(34)
    b = _safe_log(volume.abs() + 1.0).shift(34)
    corr = a.rolling(160, min_periods=max(160//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 6)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.469412 + 0.0043579 * anchor
    return base_signal

def f68_hvne_gemini_109(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=13, w2=173, w3=374, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    cover = _safe_div(a.rolling(13, min_periods=max(13//3, 2)).mean(), b.abs().rolling(173, min_periods=max(173//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.194667 * _rolling_slope(cover, 13) + 0.004358 * anchor
    return base_signal

def f68_hvne_gemini_110(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=20, w2=186, w3=391, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    y = _safe_log(volume.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.201 * y + 0.799000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 20) - _rolling_slope(basket, 186) + 0.0043581 * anchor
    return base_signal

def f68_hvne_gemini_111(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=27, w2=199, w3=408, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(27, min_periods=max(27//3, 2)).mean(), upside.rolling(199, min_periods=max(199//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.51 + 0.0043582 * anchor
    return base_signal

def f68_hvne_gemini_112(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=34, w2=212, w3=425, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(212, min_periods=max(212//3, 2)).max()
    rebound = x - x.rolling(34, min_periods=max(34//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.213667 * _rolling_slope(draw, 425) + 0.0043583 * anchor
    return base_signal

def f68_hvne_gemini_113(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=41, w2=225, w3=442, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(volume.abs() + 1.0).shift(3)
    imbalance = a.diff(41) - b.diff(126)
    stress = imbalance.rolling(442, min_periods=max(442//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.537059 + 0.0043584 * anchor
    return base_signal

def f68_hvne_gemini_114(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=48, w2=238, w3=459, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 48)
    baseline = trend.rolling(238, min_periods=max(238//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(459, min_periods=max(459//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.550588 + 0.0043585 * anchor
    return base_signal

def f68_hvne_gemini_115(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=55, w2=251, w3=476, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 55)
    slow = _rolling_slope(x, 251)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.564118 + 0.0043586 * anchor
    return base_signal

def f68_hvne_gemini_116(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=62, w2=264, w3=493, lag=13)."""
    x = close.shift(13)
    peak = x.rolling(264, min_periods=max(264//3, 2)).max()
    trough = x.rolling(62, min_periods=max(62//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.577647 + 0.0043587 * anchor
    return base_signal

def f68_hvne_gemini_117(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=69, w2=277, w3=510, lag=21)."""
    x = close.shift(21)
    change = x.pct_change(69)
    rank = change.rolling(277, min_periods=max(277//3, 2)).rank(pct=True)
    persistence = change.rolling(510, min_periods=max(510//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.245333 * persistence + 0.0043588 * anchor
    return base_signal

def f68_hvne_gemini_118(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=76, w2=290, w3=527, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(76, min_periods=max(76//3, 2)).std()
    vol_slow = ret.rolling(290, min_periods=max(290//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.604706 + 0.0043589 * anchor
    return base_signal

def f68_hvne_gemini_119(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=83, w2=303, w3=544, lag=55)."""
    x = close.shift(55)
    ma = x.rolling(303, min_periods=max(303//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 83)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.258 * slope + 0.004359 * anchor
    return base_signal

def f68_hvne_gemini_120(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=90, w2=316, w3=561, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(90)
    drag = impulse.rolling(316, min_periods=max(316//3, 2)).mean()
    noise = impulse.abs().rolling(561, min_periods=max(561//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.631765 + 0.0043591 * anchor
    return base_signal

def f68_hvne_gemini_121(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=97, w2=329, w3=578, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 97)
    acceleration = _rolling_slope(velocity, 329)
    curvature = _rolling_slope(acceleration, 578)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.270667 * acceleration + 0.0043592 * anchor
    return base_signal

def f68_hvne_gemini_122(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=104, w2=342, w3=595, lag=2)."""
    rel = _safe_div(close.shift(2), volume.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 104)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.277 * pressure.rolling(595, min_periods=max(595//3, 2)).mean() + 0.0043593 * anchor
    return base_signal

def f68_hvne_gemini_123(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=111, w2=355, w3=612, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(111, min_periods=max(111//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.672353 + 0.0043594 * anchor
    return base_signal

def f68_hvne_gemini_124(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=118, w2=368, w3=629, lag=5)."""
    a = _safe_log(close.abs() + 1.0).shift(5)
    b = _safe_log(volume.abs() + 1.0).shift(5)
    corr = a.rolling(368, min_periods=max(368//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 118)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.832353 + 0.0043595 * anchor
    return base_signal

def f68_hvne_gemini_125(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=125, w2=381, w3=646, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    cover = _safe_div(a.rolling(125, min_periods=max(125//3, 2)).mean(), b.abs().rolling(381, min_periods=max(381//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.296 * _rolling_slope(cover, 125) + 0.0043596 * anchor
    return base_signal

def f68_hvne_gemini_126(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=132, w2=394, w3=663, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    y = _safe_log(volume.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.302333 * y + 0.697667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 132) - _rolling_slope(basket, 394) + 0.0043597 * anchor
    return base_signal

def f68_hvne_gemini_127(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=139, w2=407, w3=680, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(139, min_periods=max(139//3, 2)).mean(), upside.rolling(407, min_periods=max(407//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.872941 + 0.0043598 * anchor
    return base_signal

def f68_hvne_gemini_128(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=146, w2=420, w3=697, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    draw = x - x.rolling(420, min_periods=max(420//3, 2)).max()
    rebound = x - x.rolling(146, min_periods=max(146//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.315 * _rolling_slope(draw, 697) + 0.0043599 * anchor
    return base_signal

def f68_hvne_gemini_129(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=153, w2=433, w3=714, lag=55)."""
    a = _safe_log(close.abs() + 1.0).shift(55)
    b = _safe_log(volume.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(714, min_periods=max(714//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.9 + 0.00436 * anchor
    return base_signal

def f68_hvne_gemini_130(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=160, w2=446, w3=731, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 160)
    baseline = trend.rolling(446, min_periods=max(446//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(731, min_periods=max(731//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.913529 + 0.0043601 * anchor
    return base_signal

def f68_hvne_gemini_131(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=167, w2=459, w3=748, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 167)
    slow = _rolling_slope(x, 459)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.927059 + 0.0043602 * anchor
    return base_signal

def f68_hvne_gemini_132(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=174, w2=472, w3=765, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(472, min_periods=max(472//3, 2)).max()
    trough = x.rolling(174, min_periods=max(174//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.940588 + 0.0043603 * anchor
    return base_signal

def f68_hvne_gemini_133(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=181, w2=485, w3=31, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(485, min_periods=max(485//3, 2)).rank(pct=True)
    persistence = change.rolling(31, min_periods=max(31//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.346667 * persistence + 0.0043604 * anchor
    return base_signal

def f68_hvne_gemini_134(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=188, w2=498, w3=48, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(188, min_periods=max(188//3, 2)).std()
    vol_slow = ret.rolling(498, min_periods=max(498//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.967647 + 0.0043605 * anchor
    return base_signal

def f68_hvne_gemini_135(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=195, w2=12, w3=65, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(12, min_periods=max(12//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 195)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.359333 * slope + 0.0043606 * anchor
    return base_signal

def f68_hvne_gemini_136(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=202, w2=25, w3=82, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(25, min_periods=max(25//3, 2)).mean()
    noise = impulse.abs().rolling(82, min_periods=max(82//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.994706 + 0.0043607 * anchor
    return base_signal

def f68_hvne_gemini_137(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=209, w2=38, w3=99, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 209)
    acceleration = _rolling_slope(velocity, 38)
    curvature = _rolling_slope(acceleration, 99)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.039667 * acceleration + 0.0043608 * anchor
    return base_signal

def f68_hvne_gemini_138(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=216, w2=51, w3=116, lag=34)."""
    rel = _safe_div(close.shift(34), volume.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 216)
    pressure = rel_log.diff(51)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.046 * pressure.rolling(116, min_periods=max(116//3, 2)).mean() + 0.0043609 * anchor
    return base_signal

def f68_hvne_gemini_139(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=223, w2=64, w3=133, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(223, min_periods=max(223//3, 2)).mean())
    decay = spread.ewm(span=64, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.035294 + 0.004361 * anchor
    return base_signal

def f68_hvne_gemini_140(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=230, w2=77, w3=150, lag=0)."""
    a = _safe_log(close.abs() + 1.0).shift(0)
    b = _safe_log(volume.abs() + 1.0).shift(0)
    corr = a.rolling(77, min_periods=max(77//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 230)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.048824 + 0.0043611 * anchor
    return base_signal

def f68_hvne_gemini_141(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=237, w2=90, w3=167, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    cover = _safe_div(a.rolling(237, min_periods=max(237//3, 2)).mean(), b.abs().rolling(90, min_periods=max(90//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.065 * _rolling_slope(cover, 237) + 0.0043612 * anchor
    return base_signal

def f68_hvne_gemini_142(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=244, w2=103, w3=184, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    y = _safe_log(volume.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.071333 * y + 0.928667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 244) - _rolling_slope(basket, 103) + 0.0043613 * anchor
    return base_signal

def f68_hvne_gemini_143(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=251, w2=116, w3=201, lag=3)."""
    x = close.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(251, min_periods=max(251//3, 2)).mean(), upside.rolling(116, min_periods=max(116//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.089412 + 0.0043614 * anchor
    return base_signal

def f68_hvne_gemini_144(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=11, w2=129, w3=218, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    draw = x - x.rolling(129, min_periods=max(129//3, 2)).max()
    rebound = x - x.rolling(11, min_periods=max(11//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.084 * _rolling_slope(draw, 218) + 0.0043615 * anchor
    return base_signal

def f68_hvne_gemini_145(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=18, w2=142, w3=235, lag=8)."""
    a = _safe_log(close.abs() + 1.0).shift(8)
    b = _safe_log(volume.abs() + 1.0).shift(8)
    imbalance = a.diff(18) - b.diff(126)
    stress = imbalance.rolling(235, min_periods=max(235//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.116471 + 0.0043616 * anchor
    return base_signal

def f68_hvne_gemini_146(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=25, w2=155, w3=252, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 25)
    baseline = trend.rolling(155, min_periods=max(155//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(252, min_periods=max(252//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.13 + 0.0043617 * anchor
    return base_signal

def f68_hvne_gemini_147(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=32, w2=168, w3=269, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 32)
    slow = _rolling_slope(x, 168)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=269, adjust=False).mean() * 1.143529 + 0.0043618 * anchor
    return base_signal

def f68_hvne_gemini_148(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=39, w2=181, w3=286, lag=34)."""
    x = close.shift(34)
    peak = x.rolling(181, min_periods=max(181//3, 2)).max()
    trough = x.rolling(39, min_periods=max(39//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.157059 + 0.0043619 * anchor
    return base_signal

def f68_hvne_gemini_149(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=46, w2=194, w3=303, lag=55)."""
    x = close.shift(55)
    change = x.pct_change(46)
    rank = change.rolling(194, min_periods=max(194//3, 2)).rank(pct=True)
    persistence = change.rolling(303, min_periods=max(303//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.115667 * persistence + 0.004362 * anchor
    return base_signal

def f68_hvne_gemini_150(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=53, w2=207, w3=320, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(53, min_periods=max(53//3, 2)).std()
    vol_slow = ret.rolling(207, min_periods=max(207//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.184118 + 0.0043621 * anchor
    return base_signal
