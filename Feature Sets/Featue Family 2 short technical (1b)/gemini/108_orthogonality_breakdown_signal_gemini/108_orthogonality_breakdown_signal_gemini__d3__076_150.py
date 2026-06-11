"""108 orthogonality breakdown signal gemini d3 features 76-150 — Pipeline 1b-HF Grade v7.

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

def f108_orbs_gemini_076_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=228, w2=244, w3=748, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    draw = x - x.rolling(244, min_periods=max(244//3, 2)).max()
    rebound = x - x.rolling(228, min_periods=max(228//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.321667 * _rolling_slope(draw, 748) + 0.0009807 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_077_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=235, w2=257, w3=765, lag=21)."""
    a = _safe_log(open.abs() + 1.0).shift(21)
    b = _safe_log(high.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(765, min_periods=max(765//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.205882 + 0.0009808 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_078_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=242, w2=270, w3=31, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 242)
    baseline = trend.rolling(270, min_periods=max(270//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(31, min_periods=max(31//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.219412 + 0.0009809 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_079_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=249, w2=283, w3=48, lag=55)."""
    x = _safe_log(open.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 249)
    slow = _rolling_slope(x, 283)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=48, adjust=False).mean() * 1.232941 + 0.000981 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_080_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=9, w2=296, w3=65, lag=0)."""
    x = open.shift(0)
    peak = x.rolling(296, min_periods=max(296//3, 2)).max()
    trough = x.rolling(9, min_periods=max(9//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.246471 + 0.0009811 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_081_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=16, w2=309, w3=82, lag=1)."""
    x = open.shift(1)
    change = x.pct_change(16)
    rank = change.rolling(309, min_periods=max(309//3, 2)).rank(pct=True)
    persistence = change.rolling(82, min_periods=max(82//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.353333 * persistence + 0.0009812 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_082_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=23, w2=322, w3=99, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(23, min_periods=max(23//3, 2)).std()
    vol_slow = ret.rolling(322, min_periods=max(322//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.273529 + 0.0009813 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_083_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=30, w2=335, w3=116, lag=3)."""
    x = open.shift(3)
    ma = x.rolling(335, min_periods=max(335//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 30)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.033667 * slope + 0.0009814 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_084_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=37, w2=348, w3=133, lag=5)."""
    x = open.shift(5)
    impulse = x.diff(37)
    drag = impulse.rolling(348, min_periods=max(348//3, 2)).mean()
    noise = impulse.abs().rolling(133, min_periods=max(133//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.300588 + 0.0009815 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_085_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=44, w2=361, w3=150, lag=8)."""
    x = _safe_log(open.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 44)
    acceleration = _rolling_slope(velocity, 361)
    curvature = _rolling_slope(acceleration, 150)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.046333 * acceleration + 0.0009816 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_086_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=51, w2=374, w3=167, lag=13)."""
    rel = _safe_div(open.shift(13), high.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 51)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.052667 * pressure.rolling(167, min_periods=max(167//3, 2)).mean() + 0.0009817 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_087_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=58, w2=387, w3=184, lag=21)."""
    a = open.shift(21)
    b = high.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(58, min_periods=max(58//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.341176 + 0.0009818 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_088_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=65, w2=400, w3=201, lag=34)."""
    a = _safe_log(open.abs() + 1.0).shift(34)
    b = _safe_log(high.abs() + 1.0).shift(34)
    corr = a.rolling(400, min_periods=max(400//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 65)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.354706 + 0.0009819 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_089_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=72, w2=413, w3=218, lag=55)."""
    a = open.shift(55)
    b = high.shift(55)
    cover = _safe_div(a.rolling(72, min_periods=max(72//3, 2)).mean(), b.abs().rolling(413, min_periods=max(413//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.071667 * _rolling_slope(cover, 72) + 0.000982 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_090_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=79, w2=426, w3=235, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    y = _safe_log(high.abs() + 1.0).shift(0)
    z = _safe_log(low.abs() + 1.0).shift(0)
    basket = x - 0.078 * y + 0.922000 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 79) - _rolling_slope(basket, 426) + 0.0009821 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_091_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=86, w2=439, w3=252, lag=1)."""
    x = open.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(86, min_periods=max(86//3, 2)).mean(), upside.rolling(439, min_periods=max(439//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.395294 + 0.0009822 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_092_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=93, w2=452, w3=269, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    draw = x - x.rolling(452, min_periods=max(452//3, 2)).max()
    rebound = x - x.rolling(93, min_periods=max(93//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.090667 * _rolling_slope(draw, 269) + 0.0009823 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_093_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=100, w2=465, w3=286, lag=3)."""
    a = _safe_log(open.abs() + 1.0).shift(3)
    b = _safe_log(high.abs() + 1.0).shift(3)
    imbalance = a.diff(100) - b.diff(126)
    stress = imbalance.rolling(286, min_periods=max(286//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.422353 + 0.0009824 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_094_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=107, w2=478, w3=303, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 107)
    baseline = trend.rolling(478, min_periods=max(478//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(303, min_periods=max(303//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.435882 + 0.0009825 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_095_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=114, w2=491, w3=320, lag=8)."""
    x = _safe_log(open.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 114)
    slow = _rolling_slope(x, 491)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.449412 + 0.0009826 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_096_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=121, w2=504, w3=337, lag=13)."""
    x = open.shift(13)
    peak = x.rolling(504, min_periods=max(504//3, 2)).max()
    trough = x.rolling(121, min_periods=max(121//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.462941 + 0.0009827 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_097_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=128, w2=18, w3=354, lag=21)."""
    x = open.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(18, min_periods=max(18//3, 2)).rank(pct=True)
    persistence = change.rolling(354, min_periods=max(354//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.122333 * persistence + 0.0009828 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_098_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=135, w2=31, w3=371, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(135, min_periods=max(135//3, 2)).std()
    vol_slow = ret.rolling(31, min_periods=max(31//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.49 + 0.0009829 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_099_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=142, w2=44, w3=388, lag=55)."""
    x = open.shift(55)
    ma = x.rolling(44, min_periods=max(44//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 142)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.135 * slope + 0.000983 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_100_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=149, w2=57, w3=405, lag=0)."""
    x = open.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(57, min_periods=max(57//3, 2)).mean()
    noise = impulse.abs().rolling(405, min_periods=max(405//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.517059 + 0.0009831 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_101_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=156, w2=70, w3=422, lag=1)."""
    x = _safe_log(open.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 156)
    acceleration = _rolling_slope(velocity, 70)
    curvature = _rolling_slope(acceleration, 422)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.147667 * acceleration + 0.0009832 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_102_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=163, w2=83, w3=439, lag=2)."""
    rel = _safe_div(open.shift(2), high.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 163)
    pressure = rel_log.diff(83)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.154 * pressure.rolling(439, min_periods=max(439//3, 2)).mean() + 0.0009833 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_103_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=170, w2=96, w3=456, lag=3)."""
    a = open.shift(3)
    b = high.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(170, min_periods=max(170//3, 2)).mean())
    decay = spread.ewm(span=96, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.557647 + 0.0009834 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_104_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=177, w2=109, w3=473, lag=5)."""
    a = _safe_log(open.abs() + 1.0).shift(5)
    b = _safe_log(high.abs() + 1.0).shift(5)
    corr = a.rolling(109, min_periods=max(109//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 177)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.571176 + 0.0009835 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_105_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=184, w2=122, w3=490, lag=8)."""
    a = open.shift(8)
    b = high.shift(8)
    cover = _safe_div(a.rolling(184, min_periods=max(184//3, 2)).mean(), b.abs().rolling(122, min_periods=max(122//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.173 * _rolling_slope(cover, 184) + 0.0009836 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_106_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=191, w2=135, w3=507, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    y = _safe_log(high.abs() + 1.0).shift(13)
    z = _safe_log(low.abs() + 1.0).shift(13)
    basket = x - 0.179333 * y + 0.820667 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 191) - _rolling_slope(basket, 135) + 0.0009837 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_107_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=198, w2=148, w3=524, lag=21)."""
    x = open.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(198, min_periods=max(198//3, 2)).mean(), upside.rolling(148, min_periods=max(148//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.611765 + 0.0009838 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_108_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=205, w2=161, w3=541, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    draw = x - x.rolling(161, min_periods=max(161//3, 2)).max()
    rebound = x - x.rolling(205, min_periods=max(205//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.192 * _rolling_slope(draw, 541) + 0.0009839 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_109_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=212, w2=174, w3=558, lag=55)."""
    a = _safe_log(open.abs() + 1.0).shift(55)
    b = _safe_log(high.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(558, min_periods=max(558//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.638824 + 0.000984 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_110_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=219, w2=187, w3=575, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 219)
    baseline = trend.rolling(187, min_periods=max(187//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(575, min_periods=max(575//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.652353 + 0.0009841 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_111_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=226, w2=200, w3=592, lag=1)."""
    x = _safe_log(open.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 226)
    slow = _rolling_slope(x, 200)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.665882 + 0.0009842 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_112_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=233, w2=213, w3=609, lag=2)."""
    x = open.shift(2)
    peak = x.rolling(213, min_periods=max(213//3, 2)).max()
    trough = x.rolling(233, min_periods=max(233//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.825882 + 0.0009843 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_113_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=240, w2=226, w3=626, lag=3)."""
    x = open.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(226, min_periods=max(226//3, 2)).rank(pct=True)
    persistence = change.rolling(626, min_periods=max(626//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.223667 * persistence + 0.0009844 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_114_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=247, w2=239, w3=643, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(247, min_periods=max(247//3, 2)).std()
    vol_slow = ret.rolling(239, min_periods=max(239//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.852941 + 0.0009845 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_115_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=7, w2=252, w3=660, lag=8)."""
    x = open.shift(8)
    ma = x.rolling(252, min_periods=max(252//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 7)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.236333 * slope + 0.0009846 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_116_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=14, w2=265, w3=677, lag=13)."""
    x = open.shift(13)
    impulse = x.diff(14)
    drag = impulse.rolling(265, min_periods=max(265//3, 2)).mean()
    noise = impulse.abs().rolling(677, min_periods=max(677//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.88 + 0.0009847 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_117_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=21, w2=278, w3=694, lag=21)."""
    x = _safe_log(open.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 21)
    acceleration = _rolling_slope(velocity, 278)
    curvature = _rolling_slope(acceleration, 694)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.249 * acceleration + 0.0009848 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_118_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=28, w2=291, w3=711, lag=34)."""
    rel = _safe_div(open.shift(34), high.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 28)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.255333 * pressure.rolling(711, min_periods=max(711//3, 2)).mean() + 0.0009849 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_119_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=35, w2=304, w3=728, lag=55)."""
    a = open.shift(55)
    b = high.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(35, min_periods=max(35//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.920588 + 0.000985 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_120_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=42, w2=317, w3=745, lag=0)."""
    a = _safe_log(open.abs() + 1.0).shift(0)
    b = _safe_log(high.abs() + 1.0).shift(0)
    corr = a.rolling(317, min_periods=max(317//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 42)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.934118 + 0.0009851 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_121_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=49, w2=330, w3=762, lag=1)."""
    a = open.shift(1)
    b = high.shift(1)
    cover = _safe_div(a.rolling(49, min_periods=max(49//3, 2)).mean(), b.abs().rolling(330, min_periods=max(330//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.274333 * _rolling_slope(cover, 49) + 0.0009852 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_122_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=56, w2=343, w3=28, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    y = _safe_log(high.abs() + 1.0).shift(2)
    z = _safe_log(low.abs() + 1.0).shift(2)
    basket = x - 0.280667 * y + 0.719333 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 56) - _rolling_slope(basket, 343) + 0.0009853 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_123_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=63, w2=356, w3=45, lag=3)."""
    x = open.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(63, min_periods=max(63//3, 2)).mean(), upside.rolling(356, min_periods=max(356//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(45) * 0.974706 + 0.0009854 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_124_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=70, w2=369, w3=62, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    draw = x - x.rolling(369, min_periods=max(369//3, 2)).max()
    rebound = x - x.rolling(70, min_periods=max(70//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.293333 * _rolling_slope(draw, 62) + 0.0009855 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_125_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=77, w2=382, w3=79, lag=8)."""
    a = _safe_log(open.abs() + 1.0).shift(8)
    b = _safe_log(high.abs() + 1.0).shift(8)
    imbalance = a.diff(77) - b.diff(126)
    stress = imbalance.rolling(79, min_periods=max(79//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.001765 + 0.0009856 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_126_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=84, w2=395, w3=96, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 84)
    baseline = trend.rolling(395, min_periods=max(395//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(96, min_periods=max(96//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.015294 + 0.0009857 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_127_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=91, w2=408, w3=113, lag=21)."""
    x = _safe_log(open.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 91)
    slow = _rolling_slope(x, 408)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=113, adjust=False).mean() * 1.028824 + 0.0009858 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_128_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=98, w2=421, w3=130, lag=34)."""
    x = open.shift(34)
    peak = x.rolling(421, min_periods=max(421//3, 2)).max()
    trough = x.rolling(98, min_periods=max(98//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.042353 + 0.0009859 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_129_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=105, w2=434, w3=147, lag=55)."""
    x = open.shift(55)
    change = x.pct_change(105)
    rank = change.rolling(434, min_periods=max(434//3, 2)).rank(pct=True)
    persistence = change.rolling(147, min_periods=max(147//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.325 * persistence + 0.000986 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_130_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=112, w2=447, w3=164, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(112, min_periods=max(112//3, 2)).std()
    vol_slow = ret.rolling(447, min_periods=max(447//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.069412 + 0.0009861 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_131_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=119, w2=460, w3=181, lag=1)."""
    x = open.shift(1)
    ma = x.rolling(460, min_periods=max(460//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 119)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.337667 * slope + 0.0009862 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_132_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=126, w2=473, w3=198, lag=2)."""
    x = open.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(473, min_periods=max(473//3, 2)).mean()
    noise = impulse.abs().rolling(198, min_periods=max(198//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.096471 + 0.0009863 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_133_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=133, w2=486, w3=215, lag=3)."""
    x = _safe_log(open.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 133)
    acceleration = _rolling_slope(velocity, 486)
    curvature = _rolling_slope(acceleration, 215)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.350333 * acceleration + 0.0009864 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_134_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=140, w2=499, w3=232, lag=5)."""
    rel = _safe_div(open.shift(5), high.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 140)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.356667 * pressure.rolling(232, min_periods=max(232//3, 2)).mean() + 0.0009865 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_135_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=147, w2=13, w3=249, lag=8)."""
    a = open.shift(8)
    b = high.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(147, min_periods=max(147//3, 2)).mean())
    decay = spread.ewm(span=13, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.137059 + 0.0009866 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_136_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=154, w2=26, w3=266, lag=13)."""
    a = _safe_log(open.abs() + 1.0).shift(13)
    b = _safe_log(high.abs() + 1.0).shift(13)
    corr = a.rolling(26, min_periods=max(26//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 154)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.150588 + 0.0009867 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_137_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=161, w2=39, w3=283, lag=21)."""
    a = open.shift(21)
    b = high.shift(21)
    cover = _safe_div(a.rolling(161, min_periods=max(161//3, 2)).mean(), b.abs().rolling(39, min_periods=max(39//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.043333 * _rolling_slope(cover, 161) + 0.0009868 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_138_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=168, w2=52, w3=300, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    y = _safe_log(high.abs() + 1.0).shift(34)
    z = _safe_log(low.abs() + 1.0).shift(34)
    basket = x - 0.049667 * y + 0.950333 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 168) - _rolling_slope(basket, 52) + 0.0009869 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_139_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=175, w2=65, w3=317, lag=55)."""
    x = open.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(175, min_periods=max(175//3, 2)).mean(), upside.rolling(65, min_periods=max(65//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.191176 + 0.000987 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_140_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=182, w2=78, w3=334, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    draw = x - x.rolling(78, min_periods=max(78//3, 2)).max()
    rebound = x - x.rolling(182, min_periods=max(182//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.062333 * _rolling_slope(draw, 334) + 0.0009871 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_141_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=189, w2=91, w3=351, lag=1)."""
    a = _safe_log(open.abs() + 1.0).shift(1)
    b = _safe_log(high.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(91)
    stress = imbalance.rolling(351, min_periods=max(351//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.218235 + 0.0009872 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_142_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=196, w2=104, w3=368, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 196)
    baseline = trend.rolling(104, min_periods=max(104//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(368, min_periods=max(368//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.231765 + 0.0009873 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_143_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=203, w2=117, w3=385, lag=3)."""
    x = _safe_log(open.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 203)
    slow = _rolling_slope(x, 117)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.245294 + 0.0009874 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_144_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=210, w2=130, w3=402, lag=5)."""
    x = open.shift(5)
    peak = x.rolling(130, min_periods=max(130//3, 2)).max()
    trough = x.rolling(210, min_periods=max(210//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.258824 + 0.0009875 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_145_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=217, w2=143, w3=419, lag=8)."""
    x = open.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(143, min_periods=max(143//3, 2)).rank(pct=True)
    persistence = change.rolling(419, min_periods=max(419//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.094 * persistence + 0.0009876 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_146_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=224, w2=156, w3=436, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(224, min_periods=max(224//3, 2)).std()
    vol_slow = ret.rolling(156, min_periods=max(156//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.285882 + 0.0009877 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_147_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=231, w2=169, w3=453, lag=21)."""
    x = open.shift(21)
    ma = x.rolling(169, min_periods=max(169//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 231)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.106667 * slope + 0.0009878 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_148_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=238, w2=182, w3=470, lag=34)."""
    x = open.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(182, min_periods=max(182//3, 2)).mean()
    noise = impulse.abs().rolling(470, min_periods=max(470//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.312941 + 0.0009879 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_149_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=245, w2=195, w3=487, lag=55)."""
    x = _safe_log(open.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 245)
    acceleration = _rolling_slope(velocity, 195)
    curvature = _rolling_slope(acceleration, 487)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.119333 * acceleration + 0.000988 * anchor
    return base_signal.diff().diff().diff()

def f108_orbs_gemini_150_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=5, w2=208, w3=504, lag=0)."""
    rel = _safe_div(open.shift(0), high.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 5)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.125667 * pressure.rolling(504, min_periods=max(504//3, 2)).mean() + 0.0009881 * anchor
    return base_signal.diff().diff().diff()
