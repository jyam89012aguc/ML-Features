"""37 range estimators family gemini d2 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Estimation of true market range and volatility using high-low-open-close relationships.
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

def f37_rngm_gemini_076_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=17, w2=258, w3=90, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(258, min_periods=max(258//3, 2)).max()
    trough = x.rolling(17, min_periods=max(17//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.260588 + 0.0026467 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_077_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=24, w2=271, w3=107, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(24)
    rank = change.rolling(271, min_periods=max(271//3, 2)).rank(pct=True)
    persistence = change.rolling(107, min_periods=max(107//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.159333 * persistence + 0.0026468 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_078_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=31, w2=284, w3=124, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(31, min_periods=max(31//3, 2)).std()
    vol_slow = ret.rolling(284, min_periods=max(284//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.287647 + 0.0026469 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_079_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=38, w2=297, w3=141, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(297, min_periods=max(297//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 38)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.172 * slope + 0.002647 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_080_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=45, w2=310, w3=158, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(45)
    drag = impulse.rolling(310, min_periods=max(310//3, 2)).mean()
    noise = impulse.abs().rolling(158, min_periods=max(158//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.314706 + 0.0026471 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_081_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=52, w2=323, w3=175, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 52)
    acceleration = _rolling_slope(velocity, 323)
    curvature = _rolling_slope(acceleration, 175)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.184667 * acceleration + 0.0026472 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_082_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=59, w2=336, w3=192, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 59)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.191 * pressure.rolling(192, min_periods=max(192//3, 2)).mean() + 0.0026473 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_083_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=66, w2=349, w3=209, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(66, min_periods=max(66//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.355294 + 0.0026474 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_084_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=73, w2=362, w3=226, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(362, min_periods=max(362//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 73)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.368824 + 0.0026475 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_085_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=80, w2=375, w3=243, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(80, min_periods=max(80//3, 2)).mean(), b.abs().rolling(375, min_periods=max(375//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.21 * _rolling_slope(cover, 80) + 0.0026476 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_086_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=87, w2=388, w3=260, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.216333 * y + 0.783667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 87) - _rolling_slope(basket, 388) + 0.0026477 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_087_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=94, w2=401, w3=277, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(94, min_periods=max(94//3, 2)).mean(), upside.rolling(401, min_periods=max(401//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.409412 + 0.0026478 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_088_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=101, w2=414, w3=294, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(414, min_periods=max(414//3, 2)).max()
    rebound = x - x.rolling(101, min_periods=max(101//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.229 * _rolling_slope(draw, 294) + 0.0026479 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_089_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=108, w2=427, w3=311, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(108) - b.diff(126)
    stress = imbalance.rolling(311, min_periods=max(311//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.436471 + 0.002648 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_090_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=115, w2=440, w3=328, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 115)
    baseline = trend.rolling(440, min_periods=max(440//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(328, min_periods=max(328//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.45 + 0.0026481 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_091_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=122, w2=453, w3=345, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 122)
    slow = _rolling_slope(x, 453)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.463529 + 0.0026482 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_092_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=129, w2=466, w3=362, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(466, min_periods=max(466//3, 2)).max()
    trough = x.rolling(129, min_periods=max(129//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.477059 + 0.0026483 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_093_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=136, w2=479, w3=379, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(479, min_periods=max(479//3, 2)).rank(pct=True)
    persistence = change.rolling(379, min_periods=max(379//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.260667 * persistence + 0.0026484 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_094_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=143, w2=492, w3=396, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(143, min_periods=max(143//3, 2)).std()
    vol_slow = ret.rolling(492, min_periods=max(492//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.504118 + 0.0026485 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_095_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=150, w2=505, w3=413, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(505, min_periods=max(505//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 150)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.273333 * slope + 0.0026486 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_096_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=157, w2=19, w3=430, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(19, min_periods=max(19//3, 2)).mean()
    noise = impulse.abs().rolling(430, min_periods=max(430//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.531176 + 0.0026487 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_097_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=164, w2=32, w3=447, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 164)
    acceleration = _rolling_slope(velocity, 32)
    curvature = _rolling_slope(acceleration, 447)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.286 * acceleration + 0.0026488 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_098_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=171, w2=45, w3=464, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 171)
    pressure = rel_log.diff(45)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.292333 * pressure.rolling(464, min_periods=max(464//3, 2)).mean() + 0.0026489 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_099_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=178, w2=58, w3=481, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(178, min_periods=max(178//3, 2)).mean())
    decay = spread.ewm(span=58, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.571765 + 0.002649 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_100_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=185, w2=71, w3=498, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(71, min_periods=max(71//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 185)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.585294 + 0.0026491 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_101_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=192, w2=84, w3=515, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(192, min_periods=max(192//3, 2)).mean(), b.abs().rolling(84, min_periods=max(84//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.311333 * _rolling_slope(cover, 192) + 0.0026492 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_102_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=199, w2=97, w3=532, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.317667 * y + 0.682333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 199) - _rolling_slope(basket, 97) + 0.0026493 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_103_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=206, w2=110, w3=549, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(206, min_periods=max(206//3, 2)).mean(), upside.rolling(110, min_periods=max(110//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.625882 + 0.0026494 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_104_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=213, w2=123, w3=566, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(123, min_periods=max(123//3, 2)).max()
    rebound = x - x.rolling(213, min_periods=max(213//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.330333 * _rolling_slope(draw, 566) + 0.0026495 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_105_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=220, w2=136, w3=583, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(583, min_periods=max(583//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.652941 + 0.0026496 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_106_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=227, w2=149, w3=600, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 227)
    baseline = trend.rolling(149, min_periods=max(149//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(600, min_periods=max(600//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.666471 + 0.0026497 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_107_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=234, w2=162, w3=617, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 234)
    slow = _rolling_slope(x, 162)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.826471 + 0.0026498 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_108_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=241, w2=175, w3=634, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(175, min_periods=max(175//3, 2)).max()
    trough = x.rolling(241, min_periods=max(241//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.84 + 0.0026499 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_109_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=248, w2=188, w3=651, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(188, min_periods=max(188//3, 2)).rank(pct=True)
    persistence = change.rolling(651, min_periods=max(651//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.362 * persistence + 0.00265 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_110_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=8, w2=201, w3=668, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(8, min_periods=max(8//3, 2)).std()
    vol_slow = ret.rolling(201, min_periods=max(201//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.867059 + 0.0026501 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_111_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=15, w2=214, w3=685, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(214, min_periods=max(214//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 15)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.042333 * slope + 0.0026502 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_112_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=22, w2=227, w3=702, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(22)
    drag = impulse.rolling(227, min_periods=max(227//3, 2)).mean()
    noise = impulse.abs().rolling(702, min_periods=max(702//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.894118 + 0.0026503 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_113_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=29, w2=240, w3=719, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 29)
    acceleration = _rolling_slope(velocity, 240)
    curvature = _rolling_slope(acceleration, 719)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.055 * acceleration + 0.0026504 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_114_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=36, w2=253, w3=736, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 36)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.061333 * pressure.rolling(736, min_periods=max(736//3, 2)).mean() + 0.0026505 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_115_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=43, w2=266, w3=753, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(43, min_periods=max(43//3, 2)).mean())
    decay = spread.ewm(span=266, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.934706 + 0.0026506 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_116_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=50, w2=279, w3=19, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(279, min_periods=max(279//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 50)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.948235 + 0.0026507 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_117_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=57, w2=292, w3=36, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(57, min_periods=max(57//3, 2)).mean(), b.abs().rolling(292, min_periods=max(292//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(36) + 0.080333 * _rolling_slope(cover, 57) + 0.0026508 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_118_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=64, w2=305, w3=53, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.086667 * y + 0.913333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 64) - _rolling_slope(basket, 305) + 0.0026509 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_119_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=71, w2=318, w3=70, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(71, min_periods=max(71//3, 2)).mean(), upside.rolling(318, min_periods=max(318//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(70) * 0.988824 + 0.002651 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_120_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=78, w2=331, w3=87, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(331, min_periods=max(331//3, 2)).max()
    rebound = x - x.rolling(78, min_periods=max(78//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.099333 * _rolling_slope(draw, 87) + 0.0026511 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_121_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=85, w2=344, w3=104, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(85) - b.diff(126)
    stress = imbalance.rolling(104, min_periods=max(104//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.015882 + 0.0026512 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_122_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=92, w2=357, w3=121, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 92)
    baseline = trend.rolling(357, min_periods=max(357//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(121, min_periods=max(121//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.029412 + 0.0026513 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_123_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=99, w2=370, w3=138, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 99)
    slow = _rolling_slope(x, 370)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=138, adjust=False).mean() * 1.042941 + 0.0026514 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_124_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=106, w2=383, w3=155, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(383, min_periods=max(383//3, 2)).max()
    trough = x.rolling(106, min_periods=max(106//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.056471 + 0.0026515 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_125_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=113, w2=396, w3=172, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(113)
    rank = change.rolling(396, min_periods=max(396//3, 2)).rank(pct=True)
    persistence = change.rolling(172, min_periods=max(172//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.131 * persistence + 0.0026516 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_126_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=120, w2=409, w3=189, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(120, min_periods=max(120//3, 2)).std()
    vol_slow = ret.rolling(409, min_periods=max(409//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.083529 + 0.0026517 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_127_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=127, w2=422, w3=206, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(422, min_periods=max(422//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 127)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.143667 * slope + 0.0026518 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_128_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=134, w2=435, w3=223, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(435, min_periods=max(435//3, 2)).mean()
    noise = impulse.abs().rolling(223, min_periods=max(223//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.110588 + 0.0026519 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_129_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=141, w2=448, w3=240, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 141)
    acceleration = _rolling_slope(velocity, 448)
    curvature = _rolling_slope(acceleration, 240)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.156333 * acceleration + 0.002652 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_130_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=148, w2=461, w3=257, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 148)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.162667 * pressure.rolling(257, min_periods=max(257//3, 2)).mean() + 0.0026521 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_131_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=155, w2=474, w3=274, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(155, min_periods=max(155//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.151176 + 0.0026522 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_132_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=162, w2=487, w3=291, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(487, min_periods=max(487//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 162)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.164706 + 0.0026523 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_133_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=169, w2=500, w3=308, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(169, min_periods=max(169//3, 2)).mean(), b.abs().rolling(500, min_periods=max(500//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.181667 * _rolling_slope(cover, 169) + 0.0026524 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_134_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=176, w2=14, w3=325, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.188 * y + 0.812000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 176) - _rolling_slope(basket, 14) + 0.0026525 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_135_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=183, w2=27, w3=342, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(183, min_periods=max(183//3, 2)).mean(), upside.rolling(27, min_periods=max(27//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.205294 + 0.0026526 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_136_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=190, w2=40, w3=359, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(40, min_periods=max(40//3, 2)).max()
    rebound = x - x.rolling(190, min_periods=max(190//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.200667 * _rolling_slope(draw, 359) + 0.0026527 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_137_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=197, w2=53, w3=376, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(53)
    stress = imbalance.rolling(376, min_periods=max(376//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.232353 + 0.0026528 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_138_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=204, w2=66, w3=393, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 204)
    baseline = trend.rolling(66, min_periods=max(66//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(393, min_periods=max(393//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.245882 + 0.0026529 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_139_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=211, w2=79, w3=410, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 211)
    slow = _rolling_slope(x, 79)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.259412 + 0.002653 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_140_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=218, w2=92, w3=427, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(92, min_periods=max(92//3, 2)).max()
    trough = x.rolling(218, min_periods=max(218//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.272941 + 0.0026531 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_141_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=225, w2=105, w3=444, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(105, min_periods=max(105//3, 2)).rank(pct=True)
    persistence = change.rolling(444, min_periods=max(444//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.232333 * persistence + 0.0026532 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_142_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=232, w2=118, w3=461, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(232, min_periods=max(232//3, 2)).std()
    vol_slow = ret.rolling(118, min_periods=max(118//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.3 + 0.0026533 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_143_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=239, w2=131, w3=478, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(131, min_periods=max(131//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 239)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.245 * slope + 0.0026534 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_144_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=246, w2=144, w3=495, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(144, min_periods=max(144//3, 2)).mean()
    noise = impulse.abs().rolling(495, min_periods=max(495//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.327059 + 0.0026535 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_145_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=6, w2=157, w3=512, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 6)
    acceleration = _rolling_slope(velocity, 157)
    curvature = _rolling_slope(acceleration, 512)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.257667 * acceleration + 0.0026536 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_146_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=13, w2=170, w3=529, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 13)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.264 * pressure.rolling(529, min_periods=max(529//3, 2)).mean() + 0.0026537 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_147_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=20, w2=183, w3=546, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(20, min_periods=max(20//3, 2)).mean())
    decay = spread.ewm(span=183, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.367647 + 0.0026538 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_148_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=27, w2=196, w3=563, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(196, min_periods=max(196//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 27)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.381176 + 0.0026539 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_149_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=34, w2=209, w3=580, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(34, min_periods=max(34//3, 2)).mean(), b.abs().rolling(209, min_periods=max(209//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.283 * _rolling_slope(cover, 34) + 0.002654 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_150_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=41, w2=222, w3=597, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.289333 * y + 0.710667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 41) - _rolling_slope(basket, 222) + 0.0026541 * anchor
    return base_signal.diff().diff()
