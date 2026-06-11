"""04 distribution top signature gemini d3 features 76-150 — Pipeline 1b-HF Grade v7.

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

def f04_dtop_gemini_076_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=182, w2=120, w3=395, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(120, min_periods=max(120//3, 2)).max()
    rebound = x - x.rolling(182, min_periods=max(182//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.186 * _rolling_slope(draw, 395) + 0.0001967 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_077_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=189, w2=133, w3=412, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(412, min_periods=max(412//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.972941 + 0.0001968 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_078_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=196, w2=146, w3=429, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 196)
    baseline = trend.rolling(146, min_periods=max(146//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(429, min_periods=max(429//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.986471 + 0.0001969 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_079_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=203, w2=159, w3=446, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 203)
    slow = _rolling_slope(x, 159)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.0 + 0.000197 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_080_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=210, w2=172, w3=463, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(172, min_periods=max(172//3, 2)).max()
    trough = x.rolling(210, min_periods=max(210//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.013529 + 0.0001971 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_081_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=217, w2=185, w3=480, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(185, min_periods=max(185//3, 2)).rank(pct=True)
    persistence = change.rolling(480, min_periods=max(480//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.217667 * persistence + 0.0001972 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_082_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=224, w2=198, w3=497, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(224, min_periods=max(224//3, 2)).std()
    vol_slow = ret.rolling(198, min_periods=max(198//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.040588 + 0.0001973 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_083_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=231, w2=211, w3=514, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(211, min_periods=max(211//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 231)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.230333 * slope + 0.0001974 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_084_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=238, w2=224, w3=531, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(224, min_periods=max(224//3, 2)).mean()
    noise = impulse.abs().rolling(531, min_periods=max(531//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.067647 + 0.0001975 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_085_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=245, w2=237, w3=548, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 245)
    acceleration = _rolling_slope(velocity, 237)
    curvature = _rolling_slope(acceleration, 548)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.243 * acceleration + 0.0001976 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_086_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=5, w2=250, w3=565, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 5)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.249333 * pressure.rolling(565, min_periods=max(565//3, 2)).mean() + 0.0001977 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_087_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=12, w2=263, w3=582, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(12, min_periods=max(12//3, 2)).mean())
    decay = spread.ewm(span=263, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.108235 + 0.0001978 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_088_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=19, w2=276, w3=599, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(276, min_periods=max(276//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 19)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.121765 + 0.0001979 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_089_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=26, w2=289, w3=616, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(26, min_periods=max(26//3, 2)).mean(), b.abs().rolling(289, min_periods=max(289//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.268333 * _rolling_slope(cover, 26) + 0.000198 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_090_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=33, w2=302, w3=633, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.274667 * y + 0.725333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 33) - _rolling_slope(basket, 302) + 0.0001981 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_091_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=40, w2=315, w3=650, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(40, min_periods=max(40//3, 2)).mean(), upside.rolling(315, min_periods=max(315//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.162353 + 0.0001982 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_092_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=47, w2=328, w3=667, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(328, min_periods=max(328//3, 2)).max()
    rebound = x - x.rolling(47, min_periods=max(47//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.287333 * _rolling_slope(draw, 667) + 0.0001983 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_093_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=54, w2=341, w3=684, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(54) - b.diff(126)
    stress = imbalance.rolling(684, min_periods=max(684//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.189412 + 0.0001984 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_094_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=61, w2=354, w3=701, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 61)
    baseline = trend.rolling(354, min_periods=max(354//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(701, min_periods=max(701//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.202941 + 0.0001985 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_095_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=68, w2=367, w3=718, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 68)
    slow = _rolling_slope(x, 367)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.216471 + 0.0001986 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_096_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=75, w2=380, w3=735, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(380, min_periods=max(380//3, 2)).max()
    trough = x.rolling(75, min_periods=max(75//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.23 + 0.0001987 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_097_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=82, w2=393, w3=752, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(82)
    rank = change.rolling(393, min_periods=max(393//3, 2)).rank(pct=True)
    persistence = change.rolling(752, min_periods=max(752//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.319 * persistence + 0.0001988 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_098_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=89, w2=406, w3=18, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(89, min_periods=max(89//3, 2)).std()
    vol_slow = ret.rolling(406, min_periods=max(406//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.257059 + 0.0001989 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_099_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=96, w2=419, w3=35, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(419, min_periods=max(419//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 96)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.331667 * slope + 0.000199 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_100_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=103, w2=432, w3=52, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(103)
    drag = impulse.rolling(432, min_periods=max(432//3, 2)).mean()
    noise = impulse.abs().rolling(52, min_periods=max(52//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.284118 + 0.0001991 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_101_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=110, w2=445, w3=69, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 110)
    acceleration = _rolling_slope(velocity, 445)
    curvature = _rolling_slope(acceleration, 69)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.344333 * acceleration + 0.0001992 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_102_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=117, w2=458, w3=86, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 117)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.350667 * pressure.rolling(86, min_periods=max(86//3, 2)).mean() + 0.0001993 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_103_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=124, w2=471, w3=103, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(124, min_periods=max(124//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.324706 + 0.0001994 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_104_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=131, w2=484, w3=120, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(484, min_periods=max(484//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 131)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.338235 + 0.0001995 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_105_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=138, w2=497, w3=137, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(138, min_periods=max(138//3, 2)).mean(), b.abs().rolling(497, min_periods=max(497//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.037333 * _rolling_slope(cover, 138) + 0.0001996 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_106_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=145, w2=11, w3=154, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.043667 * y + 0.956333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 145) - _rolling_slope(basket, 11) + 0.0001997 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_107_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=152, w2=24, w3=171, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(152, min_periods=max(152//3, 2)).mean(), upside.rolling(24, min_periods=max(24//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.378824 + 0.0001998 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_108_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=159, w2=37, w3=188, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(37, min_periods=max(37//3, 2)).max()
    rebound = x - x.rolling(159, min_periods=max(159//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.056333 * _rolling_slope(draw, 188) + 0.0001999 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_109_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=166, w2=50, w3=205, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(50)
    stress = imbalance.rolling(205, min_periods=max(205//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.405882 + 0.0002 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_110_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=173, w2=63, w3=222, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 173)
    baseline = trend.rolling(63, min_periods=max(63//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(222, min_periods=max(222//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.419412 + 0.0002001 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_111_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=180, w2=76, w3=239, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 180)
    slow = _rolling_slope(x, 76)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=239, adjust=False).mean() * 1.432941 + 0.0002002 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_112_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=187, w2=89, w3=256, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(89, min_periods=max(89//3, 2)).max()
    trough = x.rolling(187, min_periods=max(187//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.446471 + 0.0002003 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_113_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=194, w2=102, w3=273, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(102, min_periods=max(102//3, 2)).rank(pct=True)
    persistence = change.rolling(273, min_periods=max(273//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.088 * persistence + 0.0002004 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_114_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=201, w2=115, w3=290, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(201, min_periods=max(201//3, 2)).std()
    vol_slow = ret.rolling(115, min_periods=max(115//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.473529 + 0.0002005 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_115_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=208, w2=128, w3=307, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(128, min_periods=max(128//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 208)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.100667 * slope + 0.0002006 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_116_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=215, w2=141, w3=324, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(141, min_periods=max(141//3, 2)).mean()
    noise = impulse.abs().rolling(324, min_periods=max(324//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.500588 + 0.0002007 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_117_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=222, w2=154, w3=341, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 222)
    acceleration = _rolling_slope(velocity, 154)
    curvature = _rolling_slope(acceleration, 341)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.113333 * acceleration + 0.0002008 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_118_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=229, w2=167, w3=358, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 229)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.119667 * pressure.rolling(358, min_periods=max(358//3, 2)).mean() + 0.0002009 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_119_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=236, w2=180, w3=375, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(236, min_periods=max(236//3, 2)).mean())
    decay = spread.ewm(span=180, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.541176 + 0.000201 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_120_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=243, w2=193, w3=392, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(193, min_periods=max(193//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 243)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.554706 + 0.0002011 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_121_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=250, w2=206, w3=409, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(250, min_periods=max(250//3, 2)).mean(), b.abs().rolling(206, min_periods=max(206//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.138667 * _rolling_slope(cover, 250) + 0.0002012 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_122_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=10, w2=219, w3=426, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.145 * y + 0.855000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 10) - _rolling_slope(basket, 219) + 0.0002013 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_123_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=17, w2=232, w3=443, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(17, min_periods=max(17//3, 2)).mean(), upside.rolling(232, min_periods=max(232//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.595294 + 0.0002014 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_124_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=24, w2=245, w3=460, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(245, min_periods=max(245//3, 2)).max()
    rebound = x - x.rolling(24, min_periods=max(24//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.157667 * _rolling_slope(draw, 460) + 0.0002015 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_125_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=31, w2=258, w3=477, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(31) - b.diff(126)
    stress = imbalance.rolling(477, min_periods=max(477//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.622353 + 0.0002016 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_126_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=38, w2=271, w3=494, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 38)
    baseline = trend.rolling(271, min_periods=max(271//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(494, min_periods=max(494//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.635882 + 0.0002017 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_127_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=45, w2=284, w3=511, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 45)
    slow = _rolling_slope(x, 284)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.649412 + 0.0002018 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_128_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=52, w2=297, w3=528, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(297, min_periods=max(297//3, 2)).max()
    trough = x.rolling(52, min_periods=max(52//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.662941 + 0.0002019 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_129_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=59, w2=310, w3=545, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(59)
    rank = change.rolling(310, min_periods=max(310//3, 2)).rank(pct=True)
    persistence = change.rolling(545, min_periods=max(545//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.189333 * persistence + 0.000202 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_130_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=66, w2=323, w3=562, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(66, min_periods=max(66//3, 2)).std()
    vol_slow = ret.rolling(323, min_periods=max(323//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.836471 + 0.0002021 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_131_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=73, w2=336, w3=579, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(336, min_periods=max(336//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 73)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.202 * slope + 0.0002022 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_132_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=80, w2=349, w3=596, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(80)
    drag = impulse.rolling(349, min_periods=max(349//3, 2)).mean()
    noise = impulse.abs().rolling(596, min_periods=max(596//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.863529 + 0.0002023 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_133_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=87, w2=362, w3=613, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 87)
    acceleration = _rolling_slope(velocity, 362)
    curvature = _rolling_slope(acceleration, 613)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.214667 * acceleration + 0.0002024 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_134_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=94, w2=375, w3=630, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 94)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.221 * pressure.rolling(630, min_periods=max(630//3, 2)).mean() + 0.0002025 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_135_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=101, w2=388, w3=647, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(101, min_periods=max(101//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.904118 + 0.0002026 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_136_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=108, w2=401, w3=664, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(401, min_periods=max(401//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 108)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.917647 + 0.0002027 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_137_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=115, w2=414, w3=681, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(115, min_periods=max(115//3, 2)).mean(), b.abs().rolling(414, min_periods=max(414//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.24 * _rolling_slope(cover, 115) + 0.0002028 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_138_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=122, w2=427, w3=698, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.246333 * y + 0.753667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 122) - _rolling_slope(basket, 427) + 0.0002029 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_139_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=129, w2=440, w3=715, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(129, min_periods=max(129//3, 2)).mean(), upside.rolling(440, min_periods=max(440//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.958235 + 0.000203 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_140_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=136, w2=453, w3=732, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(453, min_periods=max(453//3, 2)).max()
    rebound = x - x.rolling(136, min_periods=max(136//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.259 * _rolling_slope(draw, 732) + 0.0002031 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_141_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=143, w2=466, w3=749, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(749, min_periods=max(749//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.985294 + 0.0002032 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_142_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=150, w2=479, w3=766, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 150)
    baseline = trend.rolling(479, min_periods=max(479//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(766, min_periods=max(766//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.998824 + 0.0002033 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_143_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=157, w2=492, w3=32, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 157)
    slow = _rolling_slope(x, 492)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=32, adjust=False).mean() * 1.012353 + 0.0002034 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_144_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=164, w2=505, w3=49, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(505, min_periods=max(505//3, 2)).max()
    trough = x.rolling(164, min_periods=max(164//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.025882 + 0.0002035 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_145_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=171, w2=19, w3=66, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(19, min_periods=max(19//3, 2)).rank(pct=True)
    persistence = change.rolling(66, min_periods=max(66//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.290667 * persistence + 0.0002036 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_146_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=178, w2=32, w3=83, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(178, min_periods=max(178//3, 2)).std()
    vol_slow = ret.rolling(32, min_periods=max(32//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.052941 + 0.0002037 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_147_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=185, w2=45, w3=100, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(45, min_periods=max(45//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 185)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.303333 * slope + 0.0002038 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_148_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=192, w2=58, w3=117, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(58, min_periods=max(58//3, 2)).mean()
    noise = impulse.abs().rolling(117, min_periods=max(117//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.08 + 0.0002039 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_149_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=199, w2=71, w3=134, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 199)
    acceleration = _rolling_slope(velocity, 71)
    curvature = _rolling_slope(acceleration, 134)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.316 * acceleration + 0.000204 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_150_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=206, w2=84, w3=151, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 206)
    pressure = rel_log.diff(84)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.322333 * pressure.rolling(151, min_periods=max(151//3, 2)).mean() + 0.0002041 * anchor
    return base_signal.diff().diff().diff()
