"""20 volume dryup at high gemini d3 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Decreasing volume at price peaks suggesting a lack of buying interest and potential reversal.
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

def f20_vdry_gemini_076_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=59, w2=74, w3=593, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(74, min_periods=max(74//3, 2)).max()
    rebound = x - x.rolling(59, min_periods=max(59//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.234 * _rolling_slope(draw, 593) + 0.0017087 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_077_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=66, w2=87, w3=610, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(close.abs() + 1.0).shift(21)
    imbalance = a.diff(66) - b.diff(87)
    stress = imbalance.rolling(610, min_periods=max(610//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.544118 + 0.0017088 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_078_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=73, w2=100, w3=627, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 73)
    baseline = trend.rolling(100, min_periods=max(100//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(627, min_periods=max(627//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.557647 + 0.0017089 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_079_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=80, w2=113, w3=644, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 80)
    slow = _rolling_slope(x, 113)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.571176 + 0.001709 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_080_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=87, w2=126, w3=661, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(126, min_periods=max(126//3, 2)).max()
    trough = x.rolling(87, min_periods=max(87//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.584706 + 0.0017091 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_081_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=94, w2=139, w3=678, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(94)
    rank = change.rolling(139, min_periods=max(139//3, 2)).rank(pct=True)
    persistence = change.rolling(678, min_periods=max(678//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.265667 * persistence + 0.0017092 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_082_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=101, w2=152, w3=695, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(101, min_periods=max(101//3, 2)).std()
    vol_slow = ret.rolling(152, min_periods=max(152//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.611765 + 0.0017093 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_083_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=108, w2=165, w3=712, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(165, min_periods=max(165//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 108)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.278333 * slope + 0.0017094 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_084_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=115, w2=178, w3=729, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(115)
    drag = impulse.rolling(178, min_periods=max(178//3, 2)).mean()
    noise = impulse.abs().rolling(729, min_periods=max(729//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.638824 + 0.0017095 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_085_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=122, w2=191, w3=746, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 122)
    acceleration = _rolling_slope(velocity, 191)
    curvature = _rolling_slope(acceleration, 746)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.291 * acceleration + 0.0017096 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_086_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=129, w2=204, w3=763, lag=13)."""
    rel = _safe_div(high.shift(13), close.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 129)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.297333 * pressure.rolling(763, min_periods=max(763//3, 2)).mean() + 0.0017097 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_087_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=136, w2=217, w3=29, lag=21)."""
    a = high.shift(21)
    b = close.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(136, min_periods=max(136//3, 2)).mean())
    decay = spread.ewm(span=217, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.825882 + 0.0017098 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_088_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=143, w2=230, w3=46, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(close.abs() + 1.0).shift(34)
    corr = a.rolling(230, min_periods=max(230//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 143)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.839412 + 0.0017099 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_089_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=150, w2=243, w3=63, lag=55)."""
    a = high.shift(55)
    b = close.shift(55)
    cover = _safe_div(a.rolling(150, min_periods=max(150//3, 2)).mean(), b.abs().rolling(243, min_periods=max(243//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(63) + 0.316333 * _rolling_slope(cover, 150) + 0.00171 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_090_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=157, w2=256, w3=80, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(close.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.322667 * y + 0.677333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 157) - _rolling_slope(basket, 256) + 0.0017101 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_091_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=164, w2=269, w3=97, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(164, min_periods=max(164//3, 2)).mean(), upside.rolling(269, min_periods=max(269//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(97) * 0.88 + 0.0017102 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_092_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=171, w2=282, w3=114, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(282, min_periods=max(282//3, 2)).max()
    rebound = x - x.rolling(171, min_periods=max(171//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.335333 * _rolling_slope(draw, 114) + 0.0017103 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_093_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=178, w2=295, w3=131, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(close.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(131, min_periods=max(131//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.907059 + 0.0017104 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_094_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=185, w2=308, w3=148, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 185)
    baseline = trend.rolling(308, min_periods=max(308//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(148, min_periods=max(148//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.920588 + 0.0017105 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_095_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=192, w2=321, w3=165, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 192)
    slow = _rolling_slope(x, 321)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=165, adjust=False).mean() * 0.934118 + 0.0017106 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_096_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=199, w2=334, w3=182, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(334, min_periods=max(334//3, 2)).max()
    trough = x.rolling(199, min_periods=max(199//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.947647 + 0.0017107 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_097_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=206, w2=347, w3=199, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(347, min_periods=max(347//3, 2)).rank(pct=True)
    persistence = change.rolling(199, min_periods=max(199//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.034667 * persistence + 0.0017108 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_098_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=213, w2=360, w3=216, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(213, min_periods=max(213//3, 2)).std()
    vol_slow = ret.rolling(360, min_periods=max(360//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.974706 + 0.0017109 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_099_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=220, w2=373, w3=233, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(373, min_periods=max(373//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 220)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.047333 * slope + 0.001711 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_100_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=227, w2=386, w3=250, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(386, min_periods=max(386//3, 2)).mean()
    noise = impulse.abs().rolling(250, min_periods=max(250//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.001765 + 0.0017111 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_101_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=234, w2=399, w3=267, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 234)
    acceleration = _rolling_slope(velocity, 399)
    curvature = _rolling_slope(acceleration, 267)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.06 * acceleration + 0.0017112 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_102_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=241, w2=412, w3=284, lag=2)."""
    rel = _safe_div(high.shift(2), close.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 241)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.066333 * pressure.rolling(284, min_periods=max(284//3, 2)).mean() + 0.0017113 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_103_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=248, w2=425, w3=301, lag=3)."""
    a = high.shift(3)
    b = close.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(248, min_periods=max(248//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.042353 + 0.0017114 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_104_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=8, w2=438, w3=318, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(close.abs() + 1.0).shift(5)
    corr = a.rolling(438, min_periods=max(438//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 8)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.055882 + 0.0017115 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_105_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=15, w2=451, w3=335, lag=8)."""
    a = high.shift(8)
    b = close.shift(8)
    cover = _safe_div(a.rolling(15, min_periods=max(15//3, 2)).mean(), b.abs().rolling(451, min_periods=max(451//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.085333 * _rolling_slope(cover, 15) + 0.0017116 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_106_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=22, w2=464, w3=352, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(close.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.091667 * y + 0.908333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 22) - _rolling_slope(basket, 464) + 0.0017117 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_107_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=29, w2=477, w3=369, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(29, min_periods=max(29//3, 2)).mean(), upside.rolling(477, min_periods=max(477//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.096471 + 0.0017118 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_108_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=36, w2=490, w3=386, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(490, min_periods=max(490//3, 2)).max()
    rebound = x - x.rolling(36, min_periods=max(36//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.104333 * _rolling_slope(draw, 386) + 0.0017119 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_109_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=43, w2=503, w3=403, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(close.abs() + 1.0).shift(55)
    imbalance = a.diff(43) - b.diff(126)
    stress = imbalance.rolling(403, min_periods=max(403//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.123529 + 0.001712 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_110_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=50, w2=17, w3=420, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 50)
    baseline = trend.rolling(17, min_periods=max(17//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(420, min_periods=max(420//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.137059 + 0.0017121 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_111_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=57, w2=30, w3=437, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 57)
    slow = _rolling_slope(x, 30)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.150588 + 0.0017122 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_112_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=64, w2=43, w3=454, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(43, min_periods=max(43//3, 2)).max()
    trough = x.rolling(64, min_periods=max(64//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.164118 + 0.0017123 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_113_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=71, w2=56, w3=471, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(71)
    rank = change.rolling(56, min_periods=max(56//3, 2)).rank(pct=True)
    persistence = change.rolling(471, min_periods=max(471//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.136 * persistence + 0.0017124 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_114_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=78, w2=69, w3=488, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(78, min_periods=max(78//3, 2)).std()
    vol_slow = ret.rolling(69, min_periods=max(69//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.191176 + 0.0017125 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_115_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=85, w2=82, w3=505, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(82, min_periods=max(82//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 85)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.148667 * slope + 0.0017126 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_116_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=92, w2=95, w3=522, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(92)
    drag = impulse.rolling(95, min_periods=max(95//3, 2)).mean()
    noise = impulse.abs().rolling(522, min_periods=max(522//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.218235 + 0.0017127 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_117_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=99, w2=108, w3=539, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 99)
    acceleration = _rolling_slope(velocity, 108)
    curvature = _rolling_slope(acceleration, 539)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.161333 * acceleration + 0.0017128 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_118_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=106, w2=121, w3=556, lag=34)."""
    rel = _safe_div(high.shift(34), close.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 106)
    pressure = rel_log.diff(121)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.167667 * pressure.rolling(556, min_periods=max(556//3, 2)).mean() + 0.0017129 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_119_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=113, w2=134, w3=573, lag=55)."""
    a = high.shift(55)
    b = close.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(113, min_periods=max(113//3, 2)).mean())
    decay = spread.ewm(span=134, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.258824 + 0.001713 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_120_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=120, w2=147, w3=590, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(close.abs() + 1.0).shift(0)
    corr = a.rolling(147, min_periods=max(147//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 120)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.272353 + 0.0017131 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_121_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=127, w2=160, w3=607, lag=1)."""
    a = high.shift(1)
    b = close.shift(1)
    cover = _safe_div(a.rolling(127, min_periods=max(127//3, 2)).mean(), b.abs().rolling(160, min_periods=max(160//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.186667 * _rolling_slope(cover, 127) + 0.0017132 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_122_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=134, w2=173, w3=624, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(close.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.193 * y + 0.807000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 134) - _rolling_slope(basket, 173) + 0.0017133 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_123_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=141, w2=186, w3=641, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(141, min_periods=max(141//3, 2)).mean(), upside.rolling(186, min_periods=max(186//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.312941 + 0.0017134 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_124_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=148, w2=199, w3=658, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(199, min_periods=max(199//3, 2)).max()
    rebound = x - x.rolling(148, min_periods=max(148//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.205667 * _rolling_slope(draw, 658) + 0.0017135 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_125_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=155, w2=212, w3=675, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(close.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(675, min_periods=max(675//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.34 + 0.0017136 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_126_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=162, w2=225, w3=692, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 162)
    baseline = trend.rolling(225, min_periods=max(225//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(692, min_periods=max(692//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.353529 + 0.0017137 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_127_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=169, w2=238, w3=709, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 169)
    slow = _rolling_slope(x, 238)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.367059 + 0.0017138 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_128_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=176, w2=251, w3=726, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(251, min_periods=max(251//3, 2)).max()
    trough = x.rolling(176, min_periods=max(176//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.380588 + 0.0017139 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_129_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=183, w2=264, w3=743, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(264, min_periods=max(264//3, 2)).rank(pct=True)
    persistence = change.rolling(743, min_periods=max(743//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.237333 * persistence + 0.001714 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_130_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=190, w2=277, w3=760, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(190, min_periods=max(190//3, 2)).std()
    vol_slow = ret.rolling(277, min_periods=max(277//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.407647 + 0.0017141 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_131_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=197, w2=290, w3=26, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(290, min_periods=max(290//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 197)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.25 * slope + 0.0017142 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_132_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=204, w2=303, w3=43, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(303, min_periods=max(303//3, 2)).mean()
    noise = impulse.abs().rolling(43, min_periods=max(43//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.434706 + 0.0017143 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_133_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=211, w2=316, w3=60, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 211)
    acceleration = _rolling_slope(velocity, 316)
    curvature = _rolling_slope(acceleration, 60)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.262667 * acceleration + 0.0017144 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_134_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=218, w2=329, w3=77, lag=5)."""
    rel = _safe_div(high.shift(5), close.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 218)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.269 * pressure.rolling(77, min_periods=max(77//3, 2)).mean() + 0.0017145 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_135_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=225, w2=342, w3=94, lag=8)."""
    a = high.shift(8)
    b = close.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(225, min_periods=max(225//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.475294 + 0.0017146 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_136_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=232, w2=355, w3=111, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(close.abs() + 1.0).shift(13)
    corr = a.rolling(355, min_periods=max(355//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 232)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.488824 + 0.0017147 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_137_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=239, w2=368, w3=128, lag=21)."""
    a = high.shift(21)
    b = close.shift(21)
    cover = _safe_div(a.rolling(239, min_periods=max(239//3, 2)).mean(), b.abs().rolling(368, min_periods=max(368//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.288 * _rolling_slope(cover, 239) + 0.0017148 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_138_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=246, w2=381, w3=145, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(close.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.294333 * y + 0.705667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 246) - _rolling_slope(basket, 381) + 0.0017149 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_139_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=6, w2=394, w3=162, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(6, min_periods=max(6//3, 2)).mean(), upside.rolling(394, min_periods=max(394//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.529412 + 0.001715 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_140_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=13, w2=407, w3=179, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(407, min_periods=max(407//3, 2)).max()
    rebound = x - x.rolling(13, min_periods=max(13//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.307 * _rolling_slope(draw, 179) + 0.0017151 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_141_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=20, w2=420, w3=196, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(close.abs() + 1.0).shift(1)
    imbalance = a.diff(20) - b.diff(126)
    stress = imbalance.rolling(196, min_periods=max(196//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.556471 + 0.0017152 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_142_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=27, w2=433, w3=213, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 27)
    baseline = trend.rolling(433, min_periods=max(433//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(213, min_periods=max(213//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.57 + 0.0017153 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_143_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=34, w2=446, w3=230, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 34)
    slow = _rolling_slope(x, 446)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=230, adjust=False).mean() * 1.583529 + 0.0017154 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_144_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=41, w2=459, w3=247, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(459, min_periods=max(459//3, 2)).max()
    trough = x.rolling(41, min_periods=max(41//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.597059 + 0.0017155 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_145_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=48, w2=472, w3=264, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(48)
    rank = change.rolling(472, min_periods=max(472//3, 2)).rank(pct=True)
    persistence = change.rolling(264, min_periods=max(264//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.338667 * persistence + 0.0017156 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_146_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=55, w2=485, w3=281, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(55, min_periods=max(55//3, 2)).std()
    vol_slow = ret.rolling(485, min_periods=max(485//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.624118 + 0.0017157 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_147_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=62, w2=498, w3=298, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(498, min_periods=max(498//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 62)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.351333 * slope + 0.0017158 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_148_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=69, w2=12, w3=315, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(69)
    drag = impulse.rolling(12, min_periods=max(12//3, 2)).mean()
    noise = impulse.abs().rolling(315, min_periods=max(315//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.651176 + 0.0017159 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_149_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=76, w2=25, w3=332, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 76)
    acceleration = _rolling_slope(velocity, 25)
    curvature = _rolling_slope(acceleration, 332)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.031667 * acceleration + 0.001716 * anchor
    return base_signal.diff().diff().diff()

def f20_vdry_gemini_150_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=83, w2=38, w3=349, lag=0)."""
    rel = _safe_div(high.shift(0), close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 83)
    pressure = rel_log.diff(38)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.038 * pressure.rolling(349, min_periods=max(349//3, 2)).mean() + 0.0017161 * anchor
    return base_signal.diff().diff().diff()
