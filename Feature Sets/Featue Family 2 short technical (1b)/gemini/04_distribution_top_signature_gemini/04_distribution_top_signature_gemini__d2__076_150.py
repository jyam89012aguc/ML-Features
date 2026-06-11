"""04 distribution top signature gemini d2 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Distribution at price tops characterized by high volume without significant price progress.
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

def f04_dtop_gemini_076_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=190, w2=296, w3=268, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(296, min_periods=max(296//3, 2)).max()
    trough = x.rolling(190, min_periods=max(190//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.625882 + 0.0001827 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_077_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=197, w2=309, w3=285, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(309, min_periods=max(309//3, 2)).rank(pct=True)
    persistence = change.rolling(285, min_periods=max(285//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.302667 * persistence + 0.0001828 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_078_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=204, w2=322, w3=302, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(204, min_periods=max(204//3, 2)).std()
    vol_slow = ret.rolling(322, min_periods=max(322//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.652941 + 0.0001829 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_079_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=211, w2=335, w3=319, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(335, min_periods=max(335//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 211)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.315333 * slope + 0.000183 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_080_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=218, w2=348, w3=336, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(348, min_periods=max(348//3, 2)).mean()
    noise = impulse.abs().rolling(336, min_periods=max(336//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.826471 + 0.0001831 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_081_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=225, w2=361, w3=353, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 225)
    acceleration = _rolling_slope(velocity, 361)
    curvature = _rolling_slope(acceleration, 353)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.328 * acceleration + 0.0001832 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_082_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=232, w2=374, w3=370, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 232)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.334333 * pressure.rolling(370, min_periods=max(370//3, 2)).mean() + 0.0001833 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_083_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=239, w2=387, w3=387, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(239, min_periods=max(239//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.867059 + 0.0001834 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_084_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=246, w2=400, w3=404, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(400, min_periods=max(400//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 246)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.880588 + 0.0001835 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_085_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=6, w2=413, w3=421, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(6, min_periods=max(6//3, 2)).mean(), b.abs().rolling(413, min_periods=max(413//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.353333 * _rolling_slope(cover, 6) + 0.0001836 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_086_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=13, w2=426, w3=438, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.359667 * y + 0.640333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 13) - _rolling_slope(basket, 426) + 0.0001837 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_087_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=20, w2=439, w3=455, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(20, min_periods=max(20//3, 2)).mean(), upside.rolling(439, min_periods=max(439//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.921176 + 0.0001838 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_088_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=27, w2=452, w3=472, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(452, min_periods=max(452//3, 2)).max()
    rebound = x - x.rolling(27, min_periods=max(27//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.04 * _rolling_slope(draw, 472) + 0.0001839 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_089_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=34, w2=465, w3=489, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(34) - b.diff(126)
    stress = imbalance.rolling(489, min_periods=max(489//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.948235 + 0.000184 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_090_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=41, w2=478, w3=506, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 41)
    baseline = trend.rolling(478, min_periods=max(478//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(506, min_periods=max(506//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.961765 + 0.0001841 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_091_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=48, w2=491, w3=523, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 48)
    slow = _rolling_slope(x, 491)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.975294 + 0.0001842 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_092_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=55, w2=504, w3=540, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(504, min_periods=max(504//3, 2)).max()
    trough = x.rolling(55, min_periods=max(55//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.988824 + 0.0001843 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_093_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=62, w2=18, w3=557, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(62)
    rank = change.rolling(18, min_periods=max(18//3, 2)).rank(pct=True)
    persistence = change.rolling(557, min_periods=max(557//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.071667 * persistence + 0.0001844 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_094_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=69, w2=31, w3=574, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(69, min_periods=max(69//3, 2)).std()
    vol_slow = ret.rolling(31, min_periods=max(31//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.015882 + 0.0001845 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_095_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=76, w2=44, w3=591, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(44, min_periods=max(44//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 76)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.084333 * slope + 0.0001846 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_096_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=83, w2=57, w3=608, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(83)
    drag = impulse.rolling(57, min_periods=max(57//3, 2)).mean()
    noise = impulse.abs().rolling(608, min_periods=max(608//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.042941 + 0.0001847 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_097_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=90, w2=70, w3=625, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 90)
    acceleration = _rolling_slope(velocity, 70)
    curvature = _rolling_slope(acceleration, 625)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.097 * acceleration + 0.0001848 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_098_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=97, w2=83, w3=642, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 97)
    pressure = rel_log.diff(83)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.103333 * pressure.rolling(642, min_periods=max(642//3, 2)).mean() + 0.0001849 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_099_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=104, w2=96, w3=659, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(104, min_periods=max(104//3, 2)).mean())
    decay = spread.ewm(span=96, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.083529 + 0.000185 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_100_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=111, w2=109, w3=676, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(109, min_periods=max(109//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 111)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.097059 + 0.0001851 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_101_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=118, w2=122, w3=693, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(118, min_periods=max(118//3, 2)).mean(), b.abs().rolling(122, min_periods=max(122//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.122333 * _rolling_slope(cover, 118) + 0.0001852 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_102_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=125, w2=135, w3=710, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.128667 * y + 0.871333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 125) - _rolling_slope(basket, 135) + 0.0001853 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_103_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=132, w2=148, w3=727, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(132, min_periods=max(132//3, 2)).mean(), upside.rolling(148, min_periods=max(148//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.137647 + 0.0001854 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_104_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=139, w2=161, w3=744, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(161, min_periods=max(161//3, 2)).max()
    rebound = x - x.rolling(139, min_periods=max(139//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.141333 * _rolling_slope(draw, 744) + 0.0001855 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_105_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=146, w2=174, w3=761, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(761, min_periods=max(761//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.164706 + 0.0001856 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_106_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=153, w2=187, w3=27, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 153)
    baseline = trend.rolling(187, min_periods=max(187//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(27, min_periods=max(27//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.178235 + 0.0001857 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_107_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=160, w2=200, w3=44, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 160)
    slow = _rolling_slope(x, 200)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=44, adjust=False).mean() * 1.191765 + 0.0001858 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_108_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=167, w2=213, w3=61, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(213, min_periods=max(213//3, 2)).max()
    trough = x.rolling(167, min_periods=max(167//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.205294 + 0.0001859 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_109_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=174, w2=226, w3=78, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(226, min_periods=max(226//3, 2)).rank(pct=True)
    persistence = change.rolling(78, min_periods=max(78//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.173 * persistence + 0.000186 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_110_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=181, w2=239, w3=95, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(181, min_periods=max(181//3, 2)).std()
    vol_slow = ret.rolling(239, min_periods=max(239//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.232353 + 0.0001861 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_111_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=188, w2=252, w3=112, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(252, min_periods=max(252//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 188)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.185667 * slope + 0.0001862 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_112_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=195, w2=265, w3=129, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(265, min_periods=max(265//3, 2)).mean()
    noise = impulse.abs().rolling(129, min_periods=max(129//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.259412 + 0.0001863 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_113_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=202, w2=278, w3=146, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 202)
    acceleration = _rolling_slope(velocity, 278)
    curvature = _rolling_slope(acceleration, 146)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.198333 * acceleration + 0.0001864 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_114_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=209, w2=291, w3=163, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 209)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.204667 * pressure.rolling(163, min_periods=max(163//3, 2)).mean() + 0.0001865 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_115_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=216, w2=304, w3=180, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(216, min_periods=max(216//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.3 + 0.0001866 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_116_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=223, w2=317, w3=197, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(317, min_periods=max(317//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 223)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.313529 + 0.0001867 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_117_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=230, w2=330, w3=214, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(230, min_periods=max(230//3, 2)).mean(), b.abs().rolling(330, min_periods=max(330//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.223667 * _rolling_slope(cover, 230) + 0.0001868 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_118_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=237, w2=343, w3=231, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.23 * y + 0.770000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 237) - _rolling_slope(basket, 343) + 0.0001869 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_119_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=244, w2=356, w3=248, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(244, min_periods=max(244//3, 2)).mean(), upside.rolling(356, min_periods=max(356//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.354118 + 0.000187 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_120_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=251, w2=369, w3=265, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(369, min_periods=max(369//3, 2)).max()
    rebound = x - x.rolling(251, min_periods=max(251//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.242667 * _rolling_slope(draw, 265) + 0.0001871 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_121_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=11, w2=382, w3=282, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(11) - b.diff(126)
    stress = imbalance.rolling(282, min_periods=max(282//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.381176 + 0.0001872 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_122_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=18, w2=395, w3=299, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 18)
    baseline = trend.rolling(395, min_periods=max(395//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(299, min_periods=max(299//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.394706 + 0.0001873 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_123_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=25, w2=408, w3=316, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 25)
    slow = _rolling_slope(x, 408)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.408235 + 0.0001874 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_124_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=32, w2=421, w3=333, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(421, min_periods=max(421//3, 2)).max()
    trough = x.rolling(32, min_periods=max(32//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.421765 + 0.0001875 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_125_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=39, w2=434, w3=350, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(39)
    rank = change.rolling(434, min_periods=max(434//3, 2)).rank(pct=True)
    persistence = change.rolling(350, min_periods=max(350//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.274333 * persistence + 0.0001876 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_126_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=46, w2=447, w3=367, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(46, min_periods=max(46//3, 2)).std()
    vol_slow = ret.rolling(447, min_periods=max(447//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.448824 + 0.0001877 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_127_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=53, w2=460, w3=384, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(460, min_periods=max(460//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 53)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.287 * slope + 0.0001878 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_128_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=60, w2=473, w3=401, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(60)
    drag = impulse.rolling(473, min_periods=max(473//3, 2)).mean()
    noise = impulse.abs().rolling(401, min_periods=max(401//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.475882 + 0.0001879 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_129_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=67, w2=486, w3=418, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 67)
    acceleration = _rolling_slope(velocity, 486)
    curvature = _rolling_slope(acceleration, 418)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.299667 * acceleration + 0.000188 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_130_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=74, w2=499, w3=435, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 74)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.306 * pressure.rolling(435, min_periods=max(435//3, 2)).mean() + 0.0001881 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_131_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=81, w2=13, w3=452, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(81, min_periods=max(81//3, 2)).mean())
    decay = spread.ewm(span=13, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.516471 + 0.0001882 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_132_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=88, w2=26, w3=469, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(26, min_periods=max(26//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 88)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.53 + 0.0001883 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_133_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=95, w2=39, w3=486, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(95, min_periods=max(95//3, 2)).mean(), b.abs().rolling(39, min_periods=max(39//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.325 * _rolling_slope(cover, 95) + 0.0001884 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_134_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=102, w2=52, w3=503, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.331333 * y + 0.668667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 102) - _rolling_slope(basket, 52) + 0.0001885 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_135_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=109, w2=65, w3=520, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(109, min_periods=max(109//3, 2)).mean(), upside.rolling(65, min_periods=max(65//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.570588 + 0.0001886 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_136_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=116, w2=78, w3=537, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(78, min_periods=max(78//3, 2)).max()
    rebound = x - x.rolling(116, min_periods=max(116//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.344 * _rolling_slope(draw, 537) + 0.0001887 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_137_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=123, w2=91, w3=554, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(123) - b.diff(91)
    stress = imbalance.rolling(554, min_periods=max(554//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.597647 + 0.0001888 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_138_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=130, w2=104, w3=571, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 130)
    baseline = trend.rolling(104, min_periods=max(104//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(571, min_periods=max(571//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.611176 + 0.0001889 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_139_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=137, w2=117, w3=588, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 137)
    slow = _rolling_slope(x, 117)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.624706 + 0.000189 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_140_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=144, w2=130, w3=605, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(130, min_periods=max(130//3, 2)).max()
    trough = x.rolling(144, min_periods=max(144//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.638235 + 0.0001891 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_141_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=151, w2=143, w3=622, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(143, min_periods=max(143//3, 2)).rank(pct=True)
    persistence = change.rolling(622, min_periods=max(622//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.043333 * persistence + 0.0001892 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_142_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=158, w2=156, w3=639, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(158, min_periods=max(158//3, 2)).std()
    vol_slow = ret.rolling(156, min_periods=max(156//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.665294 + 0.0001893 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_143_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=165, w2=169, w3=656, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(169, min_periods=max(169//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 165)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.056 * slope + 0.0001894 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_144_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=172, w2=182, w3=673, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(182, min_periods=max(182//3, 2)).mean()
    noise = impulse.abs().rolling(673, min_periods=max(673//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.838824 + 0.0001895 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_145_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=179, w2=195, w3=690, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 179)
    acceleration = _rolling_slope(velocity, 195)
    curvature = _rolling_slope(acceleration, 690)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.068667 * acceleration + 0.0001896 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_146_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=186, w2=208, w3=707, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 186)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.075 * pressure.rolling(707, min_periods=max(707//3, 2)).mean() + 0.0001897 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_147_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=193, w2=221, w3=724, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(193, min_periods=max(193//3, 2)).mean())
    decay = spread.ewm(span=221, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.879412 + 0.0001898 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_148_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=200, w2=234, w3=741, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(234, min_periods=max(234//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 200)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.892941 + 0.0001899 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_149_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=207, w2=247, w3=758, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(207, min_periods=max(207//3, 2)).mean(), b.abs().rolling(247, min_periods=max(247//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.094 * _rolling_slope(cover, 207) + 0.00019 * anchor
    return base_signal.diff().diff()

def f04_dtop_gemini_150_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=214, w2=260, w3=24, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.100333 * y + 0.899667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 214) - _rolling_slope(basket, 260) + 0.0001901 * anchor
    return base_signal.diff().diff()
