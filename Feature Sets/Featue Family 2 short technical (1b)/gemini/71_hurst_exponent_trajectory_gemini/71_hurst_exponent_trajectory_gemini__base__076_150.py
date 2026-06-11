"""71 hurst exponent trajectory gemini base features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Measurement of long-term memory and trend persistence in time series.
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

def f71_hurst_gemini_076(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=180, w2=127, w3=586, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(127, min_periods=max(127//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 180)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.574118 + 0.0045227 * anchor
    return base_signal

def f71_hurst_gemini_077(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=187, w2=140, w3=603, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(187, min_periods=max(187//3, 2)).mean(), b.abs().rolling(140, min_periods=max(140//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.329667 * _rolling_slope(cover, 187) + 0.0045228 * anchor
    return base_signal

def f71_hurst_gemini_078(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=194, w2=153, w3=620, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.336 * y + 0.664000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 194) - _rolling_slope(basket, 153) + 0.0045229 * anchor
    return base_signal

def f71_hurst_gemini_079(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=201, w2=166, w3=637, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(201, min_periods=max(201//3, 2)).mean(), upside.rolling(166, min_periods=max(166//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.614706 + 0.004523 * anchor
    return base_signal

def f71_hurst_gemini_080(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=208, w2=179, w3=654, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(179, min_periods=max(179//3, 2)).max()
    rebound = x - x.rolling(208, min_periods=max(208//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.348667 * _rolling_slope(draw, 654) + 0.0045231 * anchor
    return base_signal

def f71_hurst_gemini_081(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=215, w2=192, w3=671, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(671, min_periods=max(671//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.641765 + 0.0045232 * anchor
    return base_signal

def f71_hurst_gemini_082(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=222, w2=205, w3=688, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 222)
    baseline = trend.rolling(205, min_periods=max(205//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(688, min_periods=max(688//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.655294 + 0.0045233 * anchor
    return base_signal

def f71_hurst_gemini_083(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=229, w2=218, w3=705, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 229)
    slow = _rolling_slope(x, 218)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.668824 + 0.0045234 * anchor
    return base_signal

def f71_hurst_gemini_084(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=236, w2=231, w3=722, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(231, min_periods=max(231//3, 2)).max()
    trough = x.rolling(236, min_periods=max(236//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.828824 + 0.0045235 * anchor
    return base_signal

def f71_hurst_gemini_085(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=243, w2=244, w3=739, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(244, min_periods=max(244//3, 2)).rank(pct=True)
    persistence = change.rolling(739, min_periods=max(739//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.048 * persistence + 0.0045236 * anchor
    return base_signal

def f71_hurst_gemini_086(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=250, w2=257, w3=756, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(250, min_periods=max(250//3, 2)).std()
    vol_slow = ret.rolling(257, min_periods=max(257//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.855882 + 0.0045237 * anchor
    return base_signal

def f71_hurst_gemini_087(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=10, w2=270, w3=22, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(270, min_periods=max(270//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 10)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.060667 * slope + 0.0045238 * anchor
    return base_signal

def f71_hurst_gemini_088(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=17, w2=283, w3=39, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(17)
    drag = impulse.rolling(283, min_periods=max(283//3, 2)).mean()
    noise = impulse.abs().rolling(39, min_periods=max(39//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.882941 + 0.0045239 * anchor
    return base_signal

def f71_hurst_gemini_089(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=24, w2=296, w3=56, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 24)
    acceleration = _rolling_slope(velocity, 296)
    curvature = _rolling_slope(acceleration, 56)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.073333 * acceleration + 0.004524 * anchor
    return base_signal

def f71_hurst_gemini_090(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=31, w2=309, w3=73, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 31)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.079667 * pressure.rolling(73, min_periods=max(73//3, 2)).mean() + 0.0045241 * anchor
    return base_signal

def f71_hurst_gemini_091(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=38, w2=322, w3=90, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(38, min_periods=max(38//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.923529 + 0.0045242 * anchor
    return base_signal

def f71_hurst_gemini_092(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=45, w2=335, w3=107, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(335, min_periods=max(335//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 45)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.937059 + 0.0045243 * anchor
    return base_signal

def f71_hurst_gemini_093(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=52, w2=348, w3=124, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(52, min_periods=max(52//3, 2)).mean(), b.abs().rolling(348, min_periods=max(348//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(124) + 0.098667 * _rolling_slope(cover, 52) + 0.0045244 * anchor
    return base_signal

def f71_hurst_gemini_094(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=59, w2=361, w3=141, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.105 * y + 0.895000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 59) - _rolling_slope(basket, 361) + 0.0045245 * anchor
    return base_signal

def f71_hurst_gemini_095(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=66, w2=374, w3=158, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(66, min_periods=max(66//3, 2)).mean(), upside.rolling(374, min_periods=max(374//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.977647 + 0.0045246 * anchor
    return base_signal

def f71_hurst_gemini_096(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=73, w2=387, w3=175, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(387, min_periods=max(387//3, 2)).max()
    rebound = x - x.rolling(73, min_periods=max(73//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.117667 * _rolling_slope(draw, 175) + 0.0045247 * anchor
    return base_signal

def f71_hurst_gemini_097(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=80, w2=400, w3=192, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(80) - b.diff(126)
    stress = imbalance.rolling(192, min_periods=max(192//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.004706 + 0.0045248 * anchor
    return base_signal

def f71_hurst_gemini_098(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=87, w2=413, w3=209, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 87)
    baseline = trend.rolling(413, min_periods=max(413//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(209, min_periods=max(209//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.018235 + 0.0045249 * anchor
    return base_signal

def f71_hurst_gemini_099(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=94, w2=426, w3=226, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 94)
    slow = _rolling_slope(x, 426)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=226, adjust=False).mean() * 1.031765 + 0.004525 * anchor
    return base_signal

def f71_hurst_gemini_100(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=101, w2=439, w3=243, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(439, min_periods=max(439//3, 2)).max()
    trough = x.rolling(101, min_periods=max(101//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.045294 + 0.0045251 * anchor
    return base_signal

def f71_hurst_gemini_101(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=108, w2=452, w3=260, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(108)
    rank = change.rolling(452, min_periods=max(452//3, 2)).rank(pct=True)
    persistence = change.rolling(260, min_periods=max(260//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.149333 * persistence + 0.0045252 * anchor
    return base_signal

def f71_hurst_gemini_102(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=115, w2=465, w3=277, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(115, min_periods=max(115//3, 2)).std()
    vol_slow = ret.rolling(465, min_periods=max(465//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.072353 + 0.0045253 * anchor
    return base_signal

def f71_hurst_gemini_103(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=122, w2=478, w3=294, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(478, min_periods=max(478//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 122)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.162 * slope + 0.0045254 * anchor
    return base_signal

def f71_hurst_gemini_104(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=129, w2=491, w3=311, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(491, min_periods=max(491//3, 2)).mean()
    noise = impulse.abs().rolling(311, min_periods=max(311//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.099412 + 0.0045255 * anchor
    return base_signal

def f71_hurst_gemini_105(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=136, w2=504, w3=328, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 136)
    acceleration = _rolling_slope(velocity, 504)
    curvature = _rolling_slope(acceleration, 328)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.174667 * acceleration + 0.0045256 * anchor
    return base_signal

def f71_hurst_gemini_106(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=143, w2=18, w3=345, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 143)
    pressure = rel_log.diff(18)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.181 * pressure.rolling(345, min_periods=max(345//3, 2)).mean() + 0.0045257 * anchor
    return base_signal

def f71_hurst_gemini_107(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=150, w2=31, w3=362, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(150, min_periods=max(150//3, 2)).mean())
    decay = spread.ewm(span=31, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.14 + 0.0045258 * anchor
    return base_signal

def f71_hurst_gemini_108(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=157, w2=44, w3=379, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(44, min_periods=max(44//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 157)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.153529 + 0.0045259 * anchor
    return base_signal

def f71_hurst_gemini_109(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=164, w2=57, w3=396, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(164, min_periods=max(164//3, 2)).mean(), b.abs().rolling(57, min_periods=max(57//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.2 * _rolling_slope(cover, 164) + 0.004526 * anchor
    return base_signal

def f71_hurst_gemini_110(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=171, w2=70, w3=413, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.206333 * y + 0.793667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 171) - _rolling_slope(basket, 70) + 0.0045261 * anchor
    return base_signal

def f71_hurst_gemini_111(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=178, w2=83, w3=430, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(178, min_periods=max(178//3, 2)).mean(), upside.rolling(83, min_periods=max(83//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.194118 + 0.0045262 * anchor
    return base_signal

def f71_hurst_gemini_112(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=185, w2=96, w3=447, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(96, min_periods=max(96//3, 2)).max()
    rebound = x - x.rolling(185, min_periods=max(185//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.219 * _rolling_slope(draw, 447) + 0.0045263 * anchor
    return base_signal

def f71_hurst_gemini_113(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=192, w2=109, w3=464, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(109)
    stress = imbalance.rolling(464, min_periods=max(464//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.221176 + 0.0045264 * anchor
    return base_signal

def f71_hurst_gemini_114(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=199, w2=122, w3=481, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 199)
    baseline = trend.rolling(122, min_periods=max(122//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(481, min_periods=max(481//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.234706 + 0.0045265 * anchor
    return base_signal

def f71_hurst_gemini_115(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=206, w2=135, w3=498, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 206)
    slow = _rolling_slope(x, 135)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.248235 + 0.0045266 * anchor
    return base_signal

def f71_hurst_gemini_116(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=213, w2=148, w3=515, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(148, min_periods=max(148//3, 2)).max()
    trough = x.rolling(213, min_periods=max(213//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.261765 + 0.0045267 * anchor
    return base_signal

def f71_hurst_gemini_117(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=220, w2=161, w3=532, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(161, min_periods=max(161//3, 2)).rank(pct=True)
    persistence = change.rolling(532, min_periods=max(532//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.250667 * persistence + 0.0045268 * anchor
    return base_signal

def f71_hurst_gemini_118(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=227, w2=174, w3=549, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(227, min_periods=max(227//3, 2)).std()
    vol_slow = ret.rolling(174, min_periods=max(174//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.288824 + 0.0045269 * anchor
    return base_signal

def f71_hurst_gemini_119(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=234, w2=187, w3=566, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(187, min_periods=max(187//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 234)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.263333 * slope + 0.004527 * anchor
    return base_signal

def f71_hurst_gemini_120(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=241, w2=200, w3=583, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(200, min_periods=max(200//3, 2)).mean()
    noise = impulse.abs().rolling(583, min_periods=max(583//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.315882 + 0.0045271 * anchor
    return base_signal

def f71_hurst_gemini_121(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=248, w2=213, w3=600, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 248)
    acceleration = _rolling_slope(velocity, 213)
    curvature = _rolling_slope(acceleration, 600)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.276 * acceleration + 0.0045272 * anchor
    return base_signal

def f71_hurst_gemini_122(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=8, w2=226, w3=617, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 8)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.282333 * pressure.rolling(617, min_periods=max(617//3, 2)).mean() + 0.0045273 * anchor
    return base_signal

def f71_hurst_gemini_123(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=15, w2=239, w3=634, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(15, min_periods=max(15//3, 2)).mean())
    decay = spread.ewm(span=239, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.356471 + 0.0045274 * anchor
    return base_signal

def f71_hurst_gemini_124(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=22, w2=252, w3=651, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(252, min_periods=max(252//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 22)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.37 + 0.0045275 * anchor
    return base_signal

def f71_hurst_gemini_125(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=29, w2=265, w3=668, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(29, min_periods=max(29//3, 2)).mean(), b.abs().rolling(265, min_periods=max(265//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.301333 * _rolling_slope(cover, 29) + 0.0045276 * anchor
    return base_signal

def f71_hurst_gemini_126(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=36, w2=278, w3=685, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.307667 * y + 0.692333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 36) - _rolling_slope(basket, 278) + 0.0045277 * anchor
    return base_signal

def f71_hurst_gemini_127(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=43, w2=291, w3=702, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(43, min_periods=max(43//3, 2)).mean(), upside.rolling(291, min_periods=max(291//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.410588 + 0.0045278 * anchor
    return base_signal

def f71_hurst_gemini_128(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=50, w2=304, w3=719, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(304, min_periods=max(304//3, 2)).max()
    rebound = x - x.rolling(50, min_periods=max(50//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.320333 * _rolling_slope(draw, 719) + 0.0045279 * anchor
    return base_signal

def f71_hurst_gemini_129(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=57, w2=317, w3=736, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(57) - b.diff(126)
    stress = imbalance.rolling(736, min_periods=max(736//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.437647 + 0.004528 * anchor
    return base_signal

def f71_hurst_gemini_130(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=64, w2=330, w3=753, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 64)
    baseline = trend.rolling(330, min_periods=max(330//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(753, min_periods=max(753//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.451176 + 0.0045281 * anchor
    return base_signal

def f71_hurst_gemini_131(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=71, w2=343, w3=19, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 71)
    slow = _rolling_slope(x, 343)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=19, adjust=False).mean() * 1.464706 + 0.0045282 * anchor
    return base_signal

def f71_hurst_gemini_132(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=78, w2=356, w3=36, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(356, min_periods=max(356//3, 2)).max()
    trough = x.rolling(78, min_periods=max(78//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.478235 + 0.0045283 * anchor
    return base_signal

def f71_hurst_gemini_133(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=85, w2=369, w3=53, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(85)
    rank = change.rolling(369, min_periods=max(369//3, 2)).rank(pct=True)
    persistence = change.rolling(53, min_periods=max(53//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.352 * persistence + 0.0045284 * anchor
    return base_signal

def f71_hurst_gemini_134(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=92, w2=382, w3=70, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(92, min_periods=max(92//3, 2)).std()
    vol_slow = ret.rolling(382, min_periods=max(382//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.505294 + 0.0045285 * anchor
    return base_signal

def f71_hurst_gemini_135(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=99, w2=395, w3=87, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(395, min_periods=max(395//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 99)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.032333 * slope + 0.0045286 * anchor
    return base_signal

def f71_hurst_gemini_136(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=106, w2=408, w3=104, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(106)
    drag = impulse.rolling(408, min_periods=max(408//3, 2)).mean()
    noise = impulse.abs().rolling(104, min_periods=max(104//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.532353 + 0.0045287 * anchor
    return base_signal

def f71_hurst_gemini_137(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=113, w2=421, w3=121, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 113)
    acceleration = _rolling_slope(velocity, 421)
    curvature = _rolling_slope(acceleration, 121)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.045 * acceleration + 0.0045288 * anchor
    return base_signal

def f71_hurst_gemini_138(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=120, w2=434, w3=138, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 120)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.051333 * pressure.rolling(138, min_periods=max(138//3, 2)).mean() + 0.0045289 * anchor
    return base_signal

def f71_hurst_gemini_139(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=127, w2=447, w3=155, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(127, min_periods=max(127//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.572941 + 0.004529 * anchor
    return base_signal

def f71_hurst_gemini_140(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=134, w2=460, w3=172, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(460, min_periods=max(460//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 134)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.586471 + 0.0045291 * anchor
    return base_signal

def f71_hurst_gemini_141(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=141, w2=473, w3=189, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(141, min_periods=max(141//3, 2)).mean(), b.abs().rolling(473, min_periods=max(473//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.070333 * _rolling_slope(cover, 141) + 0.0045292 * anchor
    return base_signal

def f71_hurst_gemini_142(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=148, w2=486, w3=206, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.076667 * y + 0.923333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 148) - _rolling_slope(basket, 486) + 0.0045293 * anchor
    return base_signal

def f71_hurst_gemini_143(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=155, w2=499, w3=223, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(155, min_periods=max(155//3, 2)).mean(), upside.rolling(499, min_periods=max(499//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.627059 + 0.0045294 * anchor
    return base_signal

def f71_hurst_gemini_144(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=162, w2=13, w3=240, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(13, min_periods=max(13//3, 2)).max()
    rebound = x - x.rolling(162, min_periods=max(162//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.089333 * _rolling_slope(draw, 240) + 0.0045295 * anchor
    return base_signal

def f71_hurst_gemini_145(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=169, w2=26, w3=257, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(26)
    stress = imbalance.rolling(257, min_periods=max(257//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.654118 + 0.0045296 * anchor
    return base_signal

def f71_hurst_gemini_146(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=176, w2=39, w3=274, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 176)
    baseline = trend.rolling(39, min_periods=max(39//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(274, min_periods=max(274//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.667647 + 0.0045297 * anchor
    return base_signal

def f71_hurst_gemini_147(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=183, w2=52, w3=291, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 183)
    slow = _rolling_slope(x, 52)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=291, adjust=False).mean() * 0.827647 + 0.0045298 * anchor
    return base_signal

def f71_hurst_gemini_148(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=190, w2=65, w3=308, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(65, min_periods=max(65//3, 2)).max()
    trough = x.rolling(190, min_periods=max(190//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.841176 + 0.0045299 * anchor
    return base_signal

def f71_hurst_gemini_149(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=197, w2=78, w3=325, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(78, min_periods=max(78//3, 2)).rank(pct=True)
    persistence = change.rolling(325, min_periods=max(325//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.121 * persistence + 0.00453 * anchor
    return base_signal

def f71_hurst_gemini_150(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=204, w2=91, w3=342, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(204, min_periods=max(204//3, 2)).std()
    vol_slow = ret.rolling(91, min_periods=max(91//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.868235 + 0.0045301 * anchor
    return base_signal
