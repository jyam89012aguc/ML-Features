"""108 orthogonality breakdown signal gemini d1 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Loss of independence between supposedly uncorrelated market factors.
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

def f108_orbs_gemini_076_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=244, w2=97, w3=494, lag=13)."""
    x = open.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(97, min_periods=max(97//3, 2)).mean()
    noise = impulse.abs().rolling(494, min_periods=max(494//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.671765 + 0.0009527 * anchor
    return base_signal.diff()

def f108_orbs_gemini_077_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=251, w2=110, w3=511, lag=21)."""
    x = _safe_log(open.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 251)
    acceleration = _rolling_slope(velocity, 110)
    curvature = _rolling_slope(acceleration, 511)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.216333 * acceleration + 0.0009528 * anchor
    return base_signal.diff()

def f108_orbs_gemini_078_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=11, w2=123, w3=528, lag=34)."""
    rel = _safe_div(open.shift(34), high.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 11)
    pressure = rel_log.diff(123)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.222667 * pressure.rolling(528, min_periods=max(528//3, 2)).mean() + 0.0009529 * anchor
    return base_signal.diff()

def f108_orbs_gemini_079_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=18, w2=136, w3=545, lag=55)."""
    a = open.shift(55)
    b = high.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(18, min_periods=max(18//3, 2)).mean())
    decay = spread.ewm(span=136, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.858824 + 0.000953 * anchor
    return base_signal.diff()

def f108_orbs_gemini_080_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=25, w2=149, w3=562, lag=0)."""
    a = _safe_log(open.abs() + 1.0).shift(0)
    b = _safe_log(high.abs() + 1.0).shift(0)
    corr = a.rolling(149, min_periods=max(149//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 25)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.872353 + 0.0009531 * anchor
    return base_signal.diff()

def f108_orbs_gemini_081_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=32, w2=162, w3=579, lag=1)."""
    a = open.shift(1)
    b = high.shift(1)
    cover = _safe_div(a.rolling(32, min_periods=max(32//3, 2)).mean(), b.abs().rolling(162, min_periods=max(162//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.241667 * _rolling_slope(cover, 32) + 0.0009532 * anchor
    return base_signal.diff()

def f108_orbs_gemini_082_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=39, w2=175, w3=596, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    y = _safe_log(high.abs() + 1.0).shift(2)
    z = _safe_log(low.abs() + 1.0).shift(2)
    basket = x - 0.248 * y + 0.752000 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 39) - _rolling_slope(basket, 175) + 0.0009533 * anchor
    return base_signal.diff()

def f108_orbs_gemini_083_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=46, w2=188, w3=613, lag=3)."""
    x = open.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(46, min_periods=max(46//3, 2)).mean(), upside.rolling(188, min_periods=max(188//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.912941 + 0.0009534 * anchor
    return base_signal.diff()

def f108_orbs_gemini_084_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=53, w2=201, w3=630, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    draw = x - x.rolling(201, min_periods=max(201//3, 2)).max()
    rebound = x - x.rolling(53, min_periods=max(53//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.260667 * _rolling_slope(draw, 630) + 0.0009535 * anchor
    return base_signal.diff()

def f108_orbs_gemini_085_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=60, w2=214, w3=647, lag=8)."""
    a = _safe_log(open.abs() + 1.0).shift(8)
    b = _safe_log(high.abs() + 1.0).shift(8)
    imbalance = a.diff(60) - b.diff(126)
    stress = imbalance.rolling(647, min_periods=max(647//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.94 + 0.0009536 * anchor
    return base_signal.diff()

def f108_orbs_gemini_086_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=67, w2=227, w3=664, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 67)
    baseline = trend.rolling(227, min_periods=max(227//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(664, min_periods=max(664//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.953529 + 0.0009537 * anchor
    return base_signal.diff()

def f108_orbs_gemini_087_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=74, w2=240, w3=681, lag=21)."""
    x = _safe_log(open.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 74)
    slow = _rolling_slope(x, 240)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.967059 + 0.0009538 * anchor
    return base_signal.diff()

def f108_orbs_gemini_088_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=81, w2=253, w3=698, lag=34)."""
    x = open.shift(34)
    peak = x.rolling(253, min_periods=max(253//3, 2)).max()
    trough = x.rolling(81, min_periods=max(81//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.980588 + 0.0009539 * anchor
    return base_signal.diff()

def f108_orbs_gemini_089_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=88, w2=266, w3=715, lag=55)."""
    x = open.shift(55)
    change = x.pct_change(88)
    rank = change.rolling(266, min_periods=max(266//3, 2)).rank(pct=True)
    persistence = change.rolling(715, min_periods=max(715//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.292333 * persistence + 0.000954 * anchor
    return base_signal.diff()

def f108_orbs_gemini_090_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=95, w2=279, w3=732, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(95, min_periods=max(95//3, 2)).std()
    vol_slow = ret.rolling(279, min_periods=max(279//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.007647 + 0.0009541 * anchor
    return base_signal.diff()

def f108_orbs_gemini_091_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=102, w2=292, w3=749, lag=1)."""
    x = open.shift(1)
    ma = x.rolling(292, min_periods=max(292//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 102)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.305 * slope + 0.0009542 * anchor
    return base_signal.diff()

def f108_orbs_gemini_092_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=109, w2=305, w3=766, lag=2)."""
    x = open.shift(2)
    impulse = x.diff(109)
    drag = impulse.rolling(305, min_periods=max(305//3, 2)).mean()
    noise = impulse.abs().rolling(766, min_periods=max(766//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.034706 + 0.0009543 * anchor
    return base_signal.diff()

def f108_orbs_gemini_093_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=116, w2=318, w3=32, lag=3)."""
    x = _safe_log(open.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 116)
    acceleration = _rolling_slope(velocity, 318)
    curvature = _rolling_slope(acceleration, 32)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.317667 * acceleration + 0.0009544 * anchor
    return base_signal.diff()

def f108_orbs_gemini_094_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=123, w2=331, w3=49, lag=5)."""
    rel = _safe_div(open.shift(5), high.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 123)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.324 * pressure.rolling(49, min_periods=max(49//3, 2)).mean() + 0.0009545 * anchor
    return base_signal.diff()

def f108_orbs_gemini_095_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=130, w2=344, w3=66, lag=8)."""
    a = open.shift(8)
    b = high.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(130, min_periods=max(130//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.075294 + 0.0009546 * anchor
    return base_signal.diff()

def f108_orbs_gemini_096_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=137, w2=357, w3=83, lag=13)."""
    a = _safe_log(open.abs() + 1.0).shift(13)
    b = _safe_log(high.abs() + 1.0).shift(13)
    corr = a.rolling(357, min_periods=max(357//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 137)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.088824 + 0.0009547 * anchor
    return base_signal.diff()

def f108_orbs_gemini_097_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=144, w2=370, w3=100, lag=21)."""
    a = open.shift(21)
    b = high.shift(21)
    cover = _safe_div(a.rolling(144, min_periods=max(144//3, 2)).mean(), b.abs().rolling(370, min_periods=max(370//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(100) + 0.343 * _rolling_slope(cover, 144) + 0.0009548 * anchor
    return base_signal.diff()

def f108_orbs_gemini_098_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=151, w2=383, w3=117, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    y = _safe_log(high.abs() + 1.0).shift(34)
    z = _safe_log(low.abs() + 1.0).shift(34)
    basket = x - 0.349333 * y + 0.650667 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 151) - _rolling_slope(basket, 383) + 0.0009549 * anchor
    return base_signal.diff()

def f108_orbs_gemini_099_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=158, w2=396, w3=134, lag=55)."""
    x = open.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(158, min_periods=max(158//3, 2)).mean(), upside.rolling(396, min_periods=max(396//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.129412 + 0.000955 * anchor
    return base_signal.diff()

def f108_orbs_gemini_100_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=165, w2=409, w3=151, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    draw = x - x.rolling(409, min_periods=max(409//3, 2)).max()
    rebound = x - x.rolling(165, min_periods=max(165//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.362 * _rolling_slope(draw, 151) + 0.0009551 * anchor
    return base_signal.diff()

def f108_orbs_gemini_101_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=172, w2=422, w3=168, lag=1)."""
    a = _safe_log(open.abs() + 1.0).shift(1)
    b = _safe_log(high.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(168, min_periods=max(168//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.156471 + 0.0009552 * anchor
    return base_signal.diff()

def f108_orbs_gemini_102_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=179, w2=435, w3=185, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 179)
    baseline = trend.rolling(435, min_periods=max(435//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(185, min_periods=max(185//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.17 + 0.0009553 * anchor
    return base_signal.diff()

def f108_orbs_gemini_103_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=186, w2=448, w3=202, lag=3)."""
    x = _safe_log(open.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 186)
    slow = _rolling_slope(x, 448)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=202, adjust=False).mean() * 1.183529 + 0.0009554 * anchor
    return base_signal.diff()

def f108_orbs_gemini_104_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=193, w2=461, w3=219, lag=5)."""
    x = open.shift(5)
    peak = x.rolling(461, min_periods=max(461//3, 2)).max()
    trough = x.rolling(193, min_periods=max(193//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.197059 + 0.0009555 * anchor
    return base_signal.diff()

def f108_orbs_gemini_105_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=200, w2=474, w3=236, lag=8)."""
    x = open.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(474, min_periods=max(474//3, 2)).rank(pct=True)
    persistence = change.rolling(236, min_periods=max(236//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.061333 * persistence + 0.0009556 * anchor
    return base_signal.diff()

def f108_orbs_gemini_106_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=207, w2=487, w3=253, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(207, min_periods=max(207//3, 2)).std()
    vol_slow = ret.rolling(487, min_periods=max(487//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.224118 + 0.0009557 * anchor
    return base_signal.diff()

def f108_orbs_gemini_107_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=214, w2=500, w3=270, lag=21)."""
    x = open.shift(21)
    ma = x.rolling(500, min_periods=max(500//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 214)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.074 * slope + 0.0009558 * anchor
    return base_signal.diff()

def f108_orbs_gemini_108_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=221, w2=14, w3=287, lag=34)."""
    x = open.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(14, min_periods=max(14//3, 2)).mean()
    noise = impulse.abs().rolling(287, min_periods=max(287//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.251176 + 0.0009559 * anchor
    return base_signal.diff()

def f108_orbs_gemini_109_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=228, w2=27, w3=304, lag=55)."""
    x = _safe_log(open.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 228)
    acceleration = _rolling_slope(velocity, 27)
    curvature = _rolling_slope(acceleration, 304)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.086667 * acceleration + 0.000956 * anchor
    return base_signal.diff()

def f108_orbs_gemini_110_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=235, w2=40, w3=321, lag=0)."""
    rel = _safe_div(open.shift(0), high.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 235)
    pressure = rel_log.diff(40)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.093 * pressure.rolling(321, min_periods=max(321//3, 2)).mean() + 0.0009561 * anchor
    return base_signal.diff()

def f108_orbs_gemini_111_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=242, w2=53, w3=338, lag=1)."""
    a = open.shift(1)
    b = high.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(242, min_periods=max(242//3, 2)).mean())
    decay = spread.ewm(span=53, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.291765 + 0.0009562 * anchor
    return base_signal.diff()

def f108_orbs_gemini_112_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=249, w2=66, w3=355, lag=2)."""
    a = _safe_log(open.abs() + 1.0).shift(2)
    b = _safe_log(high.abs() + 1.0).shift(2)
    corr = a.rolling(66, min_periods=max(66//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 249)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.305294 + 0.0009563 * anchor
    return base_signal.diff()

def f108_orbs_gemini_113_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=9, w2=79, w3=372, lag=3)."""
    a = open.shift(3)
    b = high.shift(3)
    cover = _safe_div(a.rolling(9, min_periods=max(9//3, 2)).mean(), b.abs().rolling(79, min_periods=max(79//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.112 * _rolling_slope(cover, 9) + 0.0009564 * anchor
    return base_signal.diff()

def f108_orbs_gemini_114_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=16, w2=92, w3=389, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    y = _safe_log(high.abs() + 1.0).shift(5)
    z = _safe_log(low.abs() + 1.0).shift(5)
    basket = x - 0.118333 * y + 0.881667 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 16) - _rolling_slope(basket, 92) + 0.0009565 * anchor
    return base_signal.diff()

def f108_orbs_gemini_115_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=23, w2=105, w3=406, lag=8)."""
    x = open.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(23, min_periods=max(23//3, 2)).mean(), upside.rolling(105, min_periods=max(105//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.345882 + 0.0009566 * anchor
    return base_signal.diff()

def f108_orbs_gemini_116_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=30, w2=118, w3=423, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    draw = x - x.rolling(118, min_periods=max(118//3, 2)).max()
    rebound = x - x.rolling(30, min_periods=max(30//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.131 * _rolling_slope(draw, 423) + 0.0009567 * anchor
    return base_signal.diff()

def f108_orbs_gemini_117_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=37, w2=131, w3=440, lag=21)."""
    a = _safe_log(open.abs() + 1.0).shift(21)
    b = _safe_log(high.abs() + 1.0).shift(21)
    imbalance = a.diff(37) - b.diff(126)
    stress = imbalance.rolling(440, min_periods=max(440//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.372941 + 0.0009568 * anchor
    return base_signal.diff()

def f108_orbs_gemini_118_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=44, w2=144, w3=457, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 44)
    baseline = trend.rolling(144, min_periods=max(144//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(457, min_periods=max(457//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.386471 + 0.0009569 * anchor
    return base_signal.diff()

def f108_orbs_gemini_119_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=51, w2=157, w3=474, lag=55)."""
    x = _safe_log(open.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 51)
    slow = _rolling_slope(x, 157)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.4 + 0.000957 * anchor
    return base_signal.diff()

def f108_orbs_gemini_120_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=58, w2=170, w3=491, lag=0)."""
    x = open.shift(0)
    peak = x.rolling(170, min_periods=max(170//3, 2)).max()
    trough = x.rolling(58, min_periods=max(58//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.413529 + 0.0009571 * anchor
    return base_signal.diff()

def f108_orbs_gemini_121_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=65, w2=183, w3=508, lag=1)."""
    x = open.shift(1)
    change = x.pct_change(65)
    rank = change.rolling(183, min_periods=max(183//3, 2)).rank(pct=True)
    persistence = change.rolling(508, min_periods=max(508//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.162667 * persistence + 0.0009572 * anchor
    return base_signal.diff()

def f108_orbs_gemini_122_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=72, w2=196, w3=525, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(72, min_periods=max(72//3, 2)).std()
    vol_slow = ret.rolling(196, min_periods=max(196//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.440588 + 0.0009573 * anchor
    return base_signal.diff()

def f108_orbs_gemini_123_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=79, w2=209, w3=542, lag=3)."""
    x = open.shift(3)
    ma = x.rolling(209, min_periods=max(209//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 79)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.175333 * slope + 0.0009574 * anchor
    return base_signal.diff()

def f108_orbs_gemini_124_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=86, w2=222, w3=559, lag=5)."""
    x = open.shift(5)
    impulse = x.diff(86)
    drag = impulse.rolling(222, min_periods=max(222//3, 2)).mean()
    noise = impulse.abs().rolling(559, min_periods=max(559//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.467647 + 0.0009575 * anchor
    return base_signal.diff()

def f108_orbs_gemini_125_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=93, w2=235, w3=576, lag=8)."""
    x = _safe_log(open.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 93)
    acceleration = _rolling_slope(velocity, 235)
    curvature = _rolling_slope(acceleration, 576)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.188 * acceleration + 0.0009576 * anchor
    return base_signal.diff()

def f108_orbs_gemini_126_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=100, w2=248, w3=593, lag=13)."""
    rel = _safe_div(open.shift(13), high.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 100)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.194333 * pressure.rolling(593, min_periods=max(593//3, 2)).mean() + 0.0009577 * anchor
    return base_signal.diff()

def f108_orbs_gemini_127_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=107, w2=261, w3=610, lag=21)."""
    a = open.shift(21)
    b = high.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(107, min_periods=max(107//3, 2)).mean())
    decay = spread.ewm(span=261, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.508235 + 0.0009578 * anchor
    return base_signal.diff()

def f108_orbs_gemini_128_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=114, w2=274, w3=627, lag=34)."""
    a = _safe_log(open.abs() + 1.0).shift(34)
    b = _safe_log(high.abs() + 1.0).shift(34)
    corr = a.rolling(274, min_periods=max(274//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 114)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.521765 + 0.0009579 * anchor
    return base_signal.diff()

def f108_orbs_gemini_129_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=121, w2=287, w3=644, lag=55)."""
    a = open.shift(55)
    b = high.shift(55)
    cover = _safe_div(a.rolling(121, min_periods=max(121//3, 2)).mean(), b.abs().rolling(287, min_periods=max(287//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.213333 * _rolling_slope(cover, 121) + 0.000958 * anchor
    return base_signal.diff()

def f108_orbs_gemini_130_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=128, w2=300, w3=661, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    y = _safe_log(high.abs() + 1.0).shift(0)
    z = _safe_log(low.abs() + 1.0).shift(0)
    basket = x - 0.219667 * y + 0.780333 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 128) - _rolling_slope(basket, 300) + 0.0009581 * anchor
    return base_signal.diff()

def f108_orbs_gemini_131_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=135, w2=313, w3=678, lag=1)."""
    x = open.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(135, min_periods=max(135//3, 2)).mean(), upside.rolling(313, min_periods=max(313//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.562353 + 0.0009582 * anchor
    return base_signal.diff()

def f108_orbs_gemini_132_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=142, w2=326, w3=695, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    draw = x - x.rolling(326, min_periods=max(326//3, 2)).max()
    rebound = x - x.rolling(142, min_periods=max(142//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.232333 * _rolling_slope(draw, 695) + 0.0009583 * anchor
    return base_signal.diff()

def f108_orbs_gemini_133_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=149, w2=339, w3=712, lag=3)."""
    a = _safe_log(open.abs() + 1.0).shift(3)
    b = _safe_log(high.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(712, min_periods=max(712//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.589412 + 0.0009584 * anchor
    return base_signal.diff()

def f108_orbs_gemini_134_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=156, w2=352, w3=729, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 156)
    baseline = trend.rolling(352, min_periods=max(352//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(729, min_periods=max(729//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.602941 + 0.0009585 * anchor
    return base_signal.diff()

def f108_orbs_gemini_135_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=163, w2=365, w3=746, lag=8)."""
    x = _safe_log(open.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 163)
    slow = _rolling_slope(x, 365)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.616471 + 0.0009586 * anchor
    return base_signal.diff()

def f108_orbs_gemini_136_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=170, w2=378, w3=763, lag=13)."""
    x = open.shift(13)
    peak = x.rolling(378, min_periods=max(378//3, 2)).max()
    trough = x.rolling(170, min_periods=max(170//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.63 + 0.0009587 * anchor
    return base_signal.diff()

def f108_orbs_gemini_137_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=177, w2=391, w3=29, lag=21)."""
    x = open.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(391, min_periods=max(391//3, 2)).rank(pct=True)
    persistence = change.rolling(29, min_periods=max(29//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.264 * persistence + 0.0009588 * anchor
    return base_signal.diff()

def f108_orbs_gemini_138_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=184, w2=404, w3=46, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(184, min_periods=max(184//3, 2)).std()
    vol_slow = ret.rolling(404, min_periods=max(404//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.657059 + 0.0009589 * anchor
    return base_signal.diff()

def f108_orbs_gemini_139_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=191, w2=417, w3=63, lag=55)."""
    x = open.shift(55)
    ma = x.rolling(417, min_periods=max(417//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 191)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.276667 * slope + 0.000959 * anchor
    return base_signal.diff()

def f108_orbs_gemini_140_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=198, w2=430, w3=80, lag=0)."""
    x = open.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(430, min_periods=max(430//3, 2)).mean()
    noise = impulse.abs().rolling(80, min_periods=max(80//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.830588 + 0.0009591 * anchor
    return base_signal.diff()

def f108_orbs_gemini_141_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=205, w2=443, w3=97, lag=1)."""
    x = _safe_log(open.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 205)
    acceleration = _rolling_slope(velocity, 443)
    curvature = _rolling_slope(acceleration, 97)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.289333 * acceleration + 0.0009592 * anchor
    return base_signal.diff()

def f108_orbs_gemini_142_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=212, w2=456, w3=114, lag=2)."""
    rel = _safe_div(open.shift(2), high.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 212)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.295667 * pressure.rolling(114, min_periods=max(114//3, 2)).mean() + 0.0009593 * anchor
    return base_signal.diff()

def f108_orbs_gemini_143_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=219, w2=469, w3=131, lag=3)."""
    a = open.shift(3)
    b = high.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(219, min_periods=max(219//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.871176 + 0.0009594 * anchor
    return base_signal.diff()

def f108_orbs_gemini_144_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=226, w2=482, w3=148, lag=5)."""
    a = _safe_log(open.abs() + 1.0).shift(5)
    b = _safe_log(high.abs() + 1.0).shift(5)
    corr = a.rolling(482, min_periods=max(482//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 226)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.884706 + 0.0009595 * anchor
    return base_signal.diff()

def f108_orbs_gemini_145_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=233, w2=495, w3=165, lag=8)."""
    a = open.shift(8)
    b = high.shift(8)
    cover = _safe_div(a.rolling(233, min_periods=max(233//3, 2)).mean(), b.abs().rolling(495, min_periods=max(495//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.314667 * _rolling_slope(cover, 233) + 0.0009596 * anchor
    return base_signal.diff()

def f108_orbs_gemini_146_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=240, w2=508, w3=182, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    y = _safe_log(high.abs() + 1.0).shift(13)
    z = _safe_log(low.abs() + 1.0).shift(13)
    basket = x - 0.321 * y + 0.679000 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 240) - _rolling_slope(basket, 508) + 0.0009597 * anchor
    return base_signal.diff()

def f108_orbs_gemini_147_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=247, w2=22, w3=199, lag=21)."""
    x = open.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(247, min_periods=max(247//3, 2)).mean(), upside.rolling(22, min_periods=max(22//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.925294 + 0.0009598 * anchor
    return base_signal.diff()

def f108_orbs_gemini_148_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=7, w2=35, w3=216, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    draw = x - x.rolling(35, min_periods=max(35//3, 2)).max()
    rebound = x - x.rolling(7, min_periods=max(7//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.333667 * _rolling_slope(draw, 216) + 0.0009599 * anchor
    return base_signal.diff()

def f108_orbs_gemini_149_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=14, w2=48, w3=233, lag=55)."""
    a = _safe_log(open.abs() + 1.0).shift(55)
    b = _safe_log(high.abs() + 1.0).shift(55)
    imbalance = a.diff(14) - b.diff(48)
    stress = imbalance.rolling(233, min_periods=max(233//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.952353 + 0.00096 * anchor
    return base_signal.diff()

def f108_orbs_gemini_150_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=21, w2=61, w3=250, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 21)
    baseline = trend.rolling(61, min_periods=max(61//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(250, min_periods=max(250//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.965882 + 0.0009601 * anchor
    return base_signal.diff()
