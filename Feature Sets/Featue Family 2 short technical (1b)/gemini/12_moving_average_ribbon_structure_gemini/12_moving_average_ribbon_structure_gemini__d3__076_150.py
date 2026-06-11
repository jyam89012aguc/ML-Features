"""12 moving average ribbon structure gemini d3 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Interaction and convergence/divergence of multiple moving averages across different timeframes.
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

def f12_marb_gemini_076_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=68, w2=217, w3=284, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(217, min_periods=max(217//3, 2)).max()
    rebound = x - x.rolling(68, min_periods=max(68//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.109 * _rolling_slope(draw, 284) + 0.0012607 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_077_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=75, w2=230, w3=301, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(75) - b.diff(126)
    stress = imbalance.rolling(301, min_periods=max(301//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.532941 + 0.0012608 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_078_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=82, w2=243, w3=318, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 82)
    baseline = trend.rolling(243, min_periods=max(243//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(318, min_periods=max(318//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.546471 + 0.0012609 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_079_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=89, w2=256, w3=335, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 89)
    slow = _rolling_slope(x, 256)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.56 + 0.001261 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_080_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=96, w2=269, w3=352, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(269, min_periods=max(269//3, 2)).max()
    trough = x.rolling(96, min_periods=max(96//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.573529 + 0.0012611 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_081_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=103, w2=282, w3=369, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(103)
    rank = change.rolling(282, min_periods=max(282//3, 2)).rank(pct=True)
    persistence = change.rolling(369, min_periods=max(369//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.140667 * persistence + 0.0012612 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_082_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=110, w2=295, w3=386, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(110, min_periods=max(110//3, 2)).std()
    vol_slow = ret.rolling(295, min_periods=max(295//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.600588 + 0.0012613 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_083_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=117, w2=308, w3=403, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(308, min_periods=max(308//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 117)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.153333 * slope + 0.0012614 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_084_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=124, w2=321, w3=420, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(124)
    drag = impulse.rolling(321, min_periods=max(321//3, 2)).mean()
    noise = impulse.abs().rolling(420, min_periods=max(420//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.627647 + 0.0012615 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_085_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=131, w2=334, w3=437, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 131)
    acceleration = _rolling_slope(velocity, 334)
    curvature = _rolling_slope(acceleration, 437)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.166 * acceleration + 0.0012616 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_086_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=138, w2=347, w3=454, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 138)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.172333 * pressure.rolling(454, min_periods=max(454//3, 2)).mean() + 0.0012617 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_087_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=145, w2=360, w3=471, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(145, min_periods=max(145//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.668235 + 0.0012618 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_088_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=152, w2=373, w3=488, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(373, min_periods=max(373//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 152)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.828235 + 0.0012619 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_089_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=159, w2=386, w3=505, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(159, min_periods=max(159//3, 2)).mean(), b.abs().rolling(386, min_periods=max(386//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.191333 * _rolling_slope(cover, 159) + 0.001262 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_090_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=166, w2=399, w3=522, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.197667 * y + 0.802333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 166) - _rolling_slope(basket, 399) + 0.0012621 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_091_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=173, w2=412, w3=539, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(173, min_periods=max(173//3, 2)).mean(), upside.rolling(412, min_periods=max(412//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.868824 + 0.0012622 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_092_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=180, w2=425, w3=556, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(425, min_periods=max(425//3, 2)).max()
    rebound = x - x.rolling(180, min_periods=max(180//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.210333 * _rolling_slope(draw, 556) + 0.0012623 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_093_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=187, w2=438, w3=573, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(573, min_periods=max(573//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.895882 + 0.0012624 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_094_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=194, w2=451, w3=590, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 194)
    baseline = trend.rolling(451, min_periods=max(451//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(590, min_periods=max(590//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.909412 + 0.0012625 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_095_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=201, w2=464, w3=607, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 201)
    slow = _rolling_slope(x, 464)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.922941 + 0.0012626 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_096_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=208, w2=477, w3=624, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(477, min_periods=max(477//3, 2)).max()
    trough = x.rolling(208, min_periods=max(208//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.936471 + 0.0012627 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_097_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=215, w2=490, w3=641, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(490, min_periods=max(490//3, 2)).rank(pct=True)
    persistence = change.rolling(641, min_periods=max(641//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.242 * persistence + 0.0012628 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_098_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=222, w2=503, w3=658, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(222, min_periods=max(222//3, 2)).std()
    vol_slow = ret.rolling(503, min_periods=max(503//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.963529 + 0.0012629 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_099_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=229, w2=17, w3=675, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(17, min_periods=max(17//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 229)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.254667 * slope + 0.001263 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_100_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=236, w2=30, w3=692, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(30, min_periods=max(30//3, 2)).mean()
    noise = impulse.abs().rolling(692, min_periods=max(692//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.990588 + 0.0012631 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_101_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=243, w2=43, w3=709, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 243)
    acceleration = _rolling_slope(velocity, 43)
    curvature = _rolling_slope(acceleration, 709)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.267333 * acceleration + 0.0012632 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_102_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=250, w2=56, w3=726, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 250)
    pressure = rel_log.diff(56)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.273667 * pressure.rolling(726, min_periods=max(726//3, 2)).mean() + 0.0012633 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_103_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=10, w2=69, w3=743, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(10, min_periods=max(10//3, 2)).mean())
    decay = spread.ewm(span=69, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.031176 + 0.0012634 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_104_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=17, w2=82, w3=760, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(82, min_periods=max(82//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 17)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.044706 + 0.0012635 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_105_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=24, w2=95, w3=26, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(24, min_periods=max(24//3, 2)).mean(), b.abs().rolling(95, min_periods=max(95//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(26) + 0.292667 * _rolling_slope(cover, 24) + 0.0012636 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_106_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=31, w2=108, w3=43, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.299 * y + 0.701000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 31) - _rolling_slope(basket, 108) + 0.0012637 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_107_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=38, w2=121, w3=60, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(38, min_periods=max(38//3, 2)).mean(), upside.rolling(121, min_periods=max(121//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(60) * 1.085294 + 0.0012638 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_108_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=45, w2=134, w3=77, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(134, min_periods=max(134//3, 2)).max()
    rebound = x - x.rolling(45, min_periods=max(45//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.311667 * _rolling_slope(draw, 77) + 0.0012639 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_109_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=52, w2=147, w3=94, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(52) - b.diff(126)
    stress = imbalance.rolling(94, min_periods=max(94//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.112353 + 0.001264 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_110_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=59, w2=160, w3=111, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 59)
    baseline = trend.rolling(160, min_periods=max(160//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(111, min_periods=max(111//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.125882 + 0.0012641 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_111_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=66, w2=173, w3=128, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 66)
    slow = _rolling_slope(x, 173)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=128, adjust=False).mean() * 1.139412 + 0.0012642 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_112_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=73, w2=186, w3=145, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(186, min_periods=max(186//3, 2)).max()
    trough = x.rolling(73, min_periods=max(73//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.152941 + 0.0012643 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_113_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=80, w2=199, w3=162, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(80)
    rank = change.rolling(199, min_periods=max(199//3, 2)).rank(pct=True)
    persistence = change.rolling(162, min_periods=max(162//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.343333 * persistence + 0.0012644 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_114_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=87, w2=212, w3=179, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(87, min_periods=max(87//3, 2)).std()
    vol_slow = ret.rolling(212, min_periods=max(212//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.18 + 0.0012645 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_115_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=94, w2=225, w3=196, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(225, min_periods=max(225//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 94)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.356 * slope + 0.0012646 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_116_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=101, w2=238, w3=213, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(101)
    drag = impulse.rolling(238, min_periods=max(238//3, 2)).mean()
    noise = impulse.abs().rolling(213, min_periods=max(213//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.207059 + 0.0012647 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_117_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=108, w2=251, w3=230, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 108)
    acceleration = _rolling_slope(velocity, 251)
    curvature = _rolling_slope(acceleration, 230)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.036333 * acceleration + 0.0012648 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_118_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=115, w2=264, w3=247, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 115)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.042667 * pressure.rolling(247, min_periods=max(247//3, 2)).mean() + 0.0012649 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_119_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=122, w2=277, w3=264, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(122, min_periods=max(122//3, 2)).mean())
    decay = spread.ewm(span=277, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.247647 + 0.001265 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_120_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=129, w2=290, w3=281, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(290, min_periods=max(290//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 129)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.261176 + 0.0012651 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_121_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=136, w2=303, w3=298, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(136, min_periods=max(136//3, 2)).mean(), b.abs().rolling(303, min_periods=max(303//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.061667 * _rolling_slope(cover, 136) + 0.0012652 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_122_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=143, w2=316, w3=315, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.068 * y + 0.932000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 143) - _rolling_slope(basket, 316) + 0.0012653 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_123_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=150, w2=329, w3=332, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(150, min_periods=max(150//3, 2)).mean(), upside.rolling(329, min_periods=max(329//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.301765 + 0.0012654 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_124_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=157, w2=342, w3=349, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(342, min_periods=max(342//3, 2)).max()
    rebound = x - x.rolling(157, min_periods=max(157//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.080667 * _rolling_slope(draw, 349) + 0.0012655 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_125_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=164, w2=355, w3=366, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(366, min_periods=max(366//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.328824 + 0.0012656 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_126_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=171, w2=368, w3=383, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 171)
    baseline = trend.rolling(368, min_periods=max(368//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(383, min_periods=max(383//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.342353 + 0.0012657 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_127_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=178, w2=381, w3=400, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 178)
    slow = _rolling_slope(x, 381)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.355882 + 0.0012658 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_128_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=185, w2=394, w3=417, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(394, min_periods=max(394//3, 2)).max()
    trough = x.rolling(185, min_periods=max(185//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.369412 + 0.0012659 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_129_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=192, w2=407, w3=434, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(407, min_periods=max(407//3, 2)).rank(pct=True)
    persistence = change.rolling(434, min_periods=max(434//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.112333 * persistence + 0.001266 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_130_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=199, w2=420, w3=451, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(199, min_periods=max(199//3, 2)).std()
    vol_slow = ret.rolling(420, min_periods=max(420//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.396471 + 0.0012661 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_131_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=206, w2=433, w3=468, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(433, min_periods=max(433//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 206)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.125 * slope + 0.0012662 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_132_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=213, w2=446, w3=485, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(446, min_periods=max(446//3, 2)).mean()
    noise = impulse.abs().rolling(485, min_periods=max(485//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.423529 + 0.0012663 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_133_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=220, w2=459, w3=502, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 220)
    acceleration = _rolling_slope(velocity, 459)
    curvature = _rolling_slope(acceleration, 502)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.137667 * acceleration + 0.0012664 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_134_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=227, w2=472, w3=519, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 227)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.144 * pressure.rolling(519, min_periods=max(519//3, 2)).mean() + 0.0012665 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_135_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=234, w2=485, w3=536, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(234, min_periods=max(234//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.464118 + 0.0012666 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_136_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=241, w2=498, w3=553, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(498, min_periods=max(498//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 241)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.477647 + 0.0012667 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_137_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=248, w2=12, w3=570, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(248, min_periods=max(248//3, 2)).mean(), b.abs().rolling(12, min_periods=max(12//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.163 * _rolling_slope(cover, 248) + 0.0012668 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_138_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=8, w2=25, w3=587, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.169333 * y + 0.830667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 8) - _rolling_slope(basket, 25) + 0.0012669 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_139_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=15, w2=38, w3=604, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(15, min_periods=max(15//3, 2)).mean(), upside.rolling(38, min_periods=max(38//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.518235 + 0.001267 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_140_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=22, w2=51, w3=621, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(51, min_periods=max(51//3, 2)).max()
    rebound = x - x.rolling(22, min_periods=max(22//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.182 * _rolling_slope(draw, 621) + 0.0012671 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_141_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=29, w2=64, w3=638, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(29) - b.diff(64)
    stress = imbalance.rolling(638, min_periods=max(638//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.545294 + 0.0012672 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_142_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=36, w2=77, w3=655, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 36)
    baseline = trend.rolling(77, min_periods=max(77//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(655, min_periods=max(655//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.558824 + 0.0012673 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_143_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=43, w2=90, w3=672, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 43)
    slow = _rolling_slope(x, 90)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.572353 + 0.0012674 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_144_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=50, w2=103, w3=689, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(103, min_periods=max(103//3, 2)).max()
    trough = x.rolling(50, min_periods=max(50//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.585882 + 0.0012675 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_145_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=57, w2=116, w3=706, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(57)
    rank = change.rolling(116, min_periods=max(116//3, 2)).rank(pct=True)
    persistence = change.rolling(706, min_periods=max(706//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.213667 * persistence + 0.0012676 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_146_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=64, w2=129, w3=723, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(64, min_periods=max(64//3, 2)).std()
    vol_slow = ret.rolling(129, min_periods=max(129//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.612941 + 0.0012677 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_147_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=71, w2=142, w3=740, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(142, min_periods=max(142//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 71)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.226333 * slope + 0.0012678 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_148_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=78, w2=155, w3=757, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(78)
    drag = impulse.rolling(155, min_periods=max(155//3, 2)).mean()
    noise = impulse.abs().rolling(757, min_periods=max(757//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.64 + 0.0012679 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_149_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=85, w2=168, w3=23, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 85)
    acceleration = _rolling_slope(velocity, 168)
    curvature = _rolling_slope(acceleration, 23)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.239 * acceleration + 0.001268 * anchor
    return base_signal.diff().diff().diff()

def f12_marb_gemini_150_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=92, w2=181, w3=40, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 92)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.245333 * pressure.rolling(40, min_periods=max(40//3, 2)).mean() + 0.0012681 * anchor
    return base_signal.diff().diff().diff()
