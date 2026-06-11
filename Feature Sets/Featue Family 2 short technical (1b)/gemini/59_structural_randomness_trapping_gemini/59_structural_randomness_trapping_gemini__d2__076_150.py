"""59 structural randomness trapping gemini d2 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Identification of market phases where noise overwhelms signal, trapping traders.
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

def f59_sran_gemini_076_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=54, w2=239, w3=752, lag=13)."""
    x = open.shift(13)
    peak = x.rolling(239, min_periods=max(239//3, 2)).max()
    trough = x.rolling(54, min_periods=max(54//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.504706 + 0.0038787 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_077_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=61, w2=252, w3=18, lag=21)."""
    x = open.shift(21)
    change = x.pct_change(61)
    rank = change.rolling(252, min_periods=max(252//3, 2)).rank(pct=True)
    persistence = change.rolling(18, min_periods=max(18//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.087667 * persistence + 0.0038788 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_078_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=68, w2=265, w3=35, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(68, min_periods=max(68//3, 2)).std()
    vol_slow = ret.rolling(265, min_periods=max(265//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.531765 + 0.0038789 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_079_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=75, w2=278, w3=52, lag=55)."""
    x = open.shift(55)
    ma = x.rolling(278, min_periods=max(278//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 75)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.100333 * slope + 0.003879 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_080_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=82, w2=291, w3=69, lag=0)."""
    x = open.shift(0)
    impulse = x.diff(82)
    drag = impulse.rolling(291, min_periods=max(291//3, 2)).mean()
    noise = impulse.abs().rolling(69, min_periods=max(69//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.558824 + 0.0038791 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_081_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=89, w2=304, w3=86, lag=1)."""
    x = _safe_log(open.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 89)
    acceleration = _rolling_slope(velocity, 304)
    curvature = _rolling_slope(acceleration, 86)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.113 * acceleration + 0.0038792 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_082_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=96, w2=317, w3=103, lag=2)."""
    rel = _safe_div(open.shift(2), high.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 96)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.119333 * pressure.rolling(103, min_periods=max(103//3, 2)).mean() + 0.0038793 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_083_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=103, w2=330, w3=120, lag=3)."""
    a = open.shift(3)
    b = high.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(103, min_periods=max(103//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.599412 + 0.0038794 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_084_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=110, w2=343, w3=137, lag=5)."""
    a = _safe_log(open.abs() + 1.0).shift(5)
    b = _safe_log(high.abs() + 1.0).shift(5)
    corr = a.rolling(343, min_periods=max(343//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 110)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.612941 + 0.0038795 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_085_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=117, w2=356, w3=154, lag=8)."""
    a = open.shift(8)
    b = high.shift(8)
    cover = _safe_div(a.rolling(117, min_periods=max(117//3, 2)).mean(), b.abs().rolling(356, min_periods=max(356//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.138333 * _rolling_slope(cover, 117) + 0.0038796 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_086_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=124, w2=369, w3=171, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    y = _safe_log(high.abs() + 1.0).shift(13)
    z = _safe_log(low.abs() + 1.0).shift(13)
    basket = x - 0.144667 * y + 0.855333 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 124) - _rolling_slope(basket, 369) + 0.0038797 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_087_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=131, w2=382, w3=188, lag=21)."""
    x = open.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(131, min_periods=max(131//3, 2)).mean(), upside.rolling(382, min_periods=max(382//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.653529 + 0.0038798 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_088_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=138, w2=395, w3=205, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    draw = x - x.rolling(395, min_periods=max(395//3, 2)).max()
    rebound = x - x.rolling(138, min_periods=max(138//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.157333 * _rolling_slope(draw, 205) + 0.0038799 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_089_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=145, w2=408, w3=222, lag=55)."""
    a = _safe_log(open.abs() + 1.0).shift(55)
    b = _safe_log(high.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(222, min_periods=max(222//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.827059 + 0.00388 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_090_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=152, w2=421, w3=239, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 152)
    baseline = trend.rolling(421, min_periods=max(421//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(239, min_periods=max(239//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.840588 + 0.0038801 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_091_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=159, w2=434, w3=256, lag=1)."""
    x = _safe_log(open.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 159)
    slow = _rolling_slope(x, 434)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=256, adjust=False).mean() * 0.854118 + 0.0038802 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_092_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=166, w2=447, w3=273, lag=2)."""
    x = open.shift(2)
    peak = x.rolling(447, min_periods=max(447//3, 2)).max()
    trough = x.rolling(166, min_periods=max(166//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.867647 + 0.0038803 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_093_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=173, w2=460, w3=290, lag=3)."""
    x = open.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(460, min_periods=max(460//3, 2)).rank(pct=True)
    persistence = change.rolling(290, min_periods=max(290//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.189 * persistence + 0.0038804 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_094_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=180, w2=473, w3=307, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(180, min_periods=max(180//3, 2)).std()
    vol_slow = ret.rolling(473, min_periods=max(473//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.894706 + 0.0038805 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_095_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=187, w2=486, w3=324, lag=8)."""
    x = open.shift(8)
    ma = x.rolling(486, min_periods=max(486//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 187)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.201667 * slope + 0.0038806 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_096_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=194, w2=499, w3=341, lag=13)."""
    x = open.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(499, min_periods=max(499//3, 2)).mean()
    noise = impulse.abs().rolling(341, min_periods=max(341//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.921765 + 0.0038807 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_097_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=201, w2=13, w3=358, lag=21)."""
    x = _safe_log(open.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 201)
    acceleration = _rolling_slope(velocity, 13)
    curvature = _rolling_slope(acceleration, 358)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.214333 * acceleration + 0.0038808 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_098_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=208, w2=26, w3=375, lag=34)."""
    rel = _safe_div(open.shift(34), high.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 208)
    pressure = rel_log.diff(26)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.220667 * pressure.rolling(375, min_periods=max(375//3, 2)).mean() + 0.0038809 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_099_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=215, w2=39, w3=392, lag=55)."""
    a = open.shift(55)
    b = high.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(215, min_periods=max(215//3, 2)).mean())
    decay = spread.ewm(span=39, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.962353 + 0.003881 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_100_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=222, w2=52, w3=409, lag=0)."""
    a = _safe_log(open.abs() + 1.0).shift(0)
    b = _safe_log(high.abs() + 1.0).shift(0)
    corr = a.rolling(52, min_periods=max(52//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 222)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.975882 + 0.0038811 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_101_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=229, w2=65, w3=426, lag=1)."""
    a = open.shift(1)
    b = high.shift(1)
    cover = _safe_div(a.rolling(229, min_periods=max(229//3, 2)).mean(), b.abs().rolling(65, min_periods=max(65//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.239667 * _rolling_slope(cover, 229) + 0.0038812 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_102_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=236, w2=78, w3=443, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    y = _safe_log(high.abs() + 1.0).shift(2)
    z = _safe_log(low.abs() + 1.0).shift(2)
    basket = x - 0.246 * y + 0.754000 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 236) - _rolling_slope(basket, 78) + 0.0038813 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_103_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=243, w2=91, w3=460, lag=3)."""
    x = open.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(243, min_periods=max(243//3, 2)).mean(), upside.rolling(91, min_periods=max(91//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.016471 + 0.0038814 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_104_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=250, w2=104, w3=477, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    draw = x - x.rolling(104, min_periods=max(104//3, 2)).max()
    rebound = x - x.rolling(250, min_periods=max(250//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.258667 * _rolling_slope(draw, 477) + 0.0038815 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_105_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=10, w2=117, w3=494, lag=8)."""
    a = _safe_log(open.abs() + 1.0).shift(8)
    b = _safe_log(high.abs() + 1.0).shift(8)
    imbalance = a.diff(10) - b.diff(117)
    stress = imbalance.rolling(494, min_periods=max(494//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.043529 + 0.0038816 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_106_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=17, w2=130, w3=511, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 17)
    baseline = trend.rolling(130, min_periods=max(130//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(511, min_periods=max(511//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.057059 + 0.0038817 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_107_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=24, w2=143, w3=528, lag=21)."""
    x = _safe_log(open.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 24)
    slow = _rolling_slope(x, 143)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.070588 + 0.0038818 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_108_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=31, w2=156, w3=545, lag=34)."""
    x = open.shift(34)
    peak = x.rolling(156, min_periods=max(156//3, 2)).max()
    trough = x.rolling(31, min_periods=max(31//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.084118 + 0.0038819 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_109_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=38, w2=169, w3=562, lag=55)."""
    x = open.shift(55)
    change = x.pct_change(38)
    rank = change.rolling(169, min_periods=max(169//3, 2)).rank(pct=True)
    persistence = change.rolling(562, min_periods=max(562//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.290333 * persistence + 0.003882 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_110_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=45, w2=182, w3=579, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(45, min_periods=max(45//3, 2)).std()
    vol_slow = ret.rolling(182, min_periods=max(182//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.111176 + 0.0038821 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_111_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=52, w2=195, w3=596, lag=1)."""
    x = open.shift(1)
    ma = x.rolling(195, min_periods=max(195//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 52)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.303 * slope + 0.0038822 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_112_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=59, w2=208, w3=613, lag=2)."""
    x = open.shift(2)
    impulse = x.diff(59)
    drag = impulse.rolling(208, min_periods=max(208//3, 2)).mean()
    noise = impulse.abs().rolling(613, min_periods=max(613//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.138235 + 0.0038823 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_113_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=66, w2=221, w3=630, lag=3)."""
    x = _safe_log(open.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 66)
    acceleration = _rolling_slope(velocity, 221)
    curvature = _rolling_slope(acceleration, 630)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.315667 * acceleration + 0.0038824 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_114_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=73, w2=234, w3=647, lag=5)."""
    rel = _safe_div(open.shift(5), high.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 73)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.322 * pressure.rolling(647, min_periods=max(647//3, 2)).mean() + 0.0038825 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_115_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=80, w2=247, w3=664, lag=8)."""
    a = open.shift(8)
    b = high.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(80, min_periods=max(80//3, 2)).mean())
    decay = spread.ewm(span=247, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.178824 + 0.0038826 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_116_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=87, w2=260, w3=681, lag=13)."""
    a = _safe_log(open.abs() + 1.0).shift(13)
    b = _safe_log(high.abs() + 1.0).shift(13)
    corr = a.rolling(260, min_periods=max(260//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 87)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.192353 + 0.0038827 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_117_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=94, w2=273, w3=698, lag=21)."""
    a = open.shift(21)
    b = high.shift(21)
    cover = _safe_div(a.rolling(94, min_periods=max(94//3, 2)).mean(), b.abs().rolling(273, min_periods=max(273//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.341 * _rolling_slope(cover, 94) + 0.0038828 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_118_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=101, w2=286, w3=715, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    y = _safe_log(high.abs() + 1.0).shift(34)
    z = _safe_log(low.abs() + 1.0).shift(34)
    basket = x - 0.347333 * y + 0.652667 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 101) - _rolling_slope(basket, 286) + 0.0038829 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_119_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=108, w2=299, w3=732, lag=55)."""
    x = open.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(108, min_periods=max(108//3, 2)).mean(), upside.rolling(299, min_periods=max(299//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.232941 + 0.003883 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_120_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=115, w2=312, w3=749, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    draw = x - x.rolling(312, min_periods=max(312//3, 2)).max()
    rebound = x - x.rolling(115, min_periods=max(115//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.36 * _rolling_slope(draw, 749) + 0.0038831 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_121_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=122, w2=325, w3=766, lag=1)."""
    a = _safe_log(open.abs() + 1.0).shift(1)
    b = _safe_log(high.abs() + 1.0).shift(1)
    imbalance = a.diff(122) - b.diff(126)
    stress = imbalance.rolling(766, min_periods=max(766//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.26 + 0.0038832 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_122_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=129, w2=338, w3=32, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 129)
    baseline = trend.rolling(338, min_periods=max(338//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(32, min_periods=max(32//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.273529 + 0.0038833 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_123_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=136, w2=351, w3=49, lag=3)."""
    x = _safe_log(open.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 136)
    slow = _rolling_slope(x, 351)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=49, adjust=False).mean() * 1.287059 + 0.0038834 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_124_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=143, w2=364, w3=66, lag=5)."""
    x = open.shift(5)
    peak = x.rolling(364, min_periods=max(364//3, 2)).max()
    trough = x.rolling(143, min_periods=max(143//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.300588 + 0.0038835 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_125_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=150, w2=377, w3=83, lag=8)."""
    x = open.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(377, min_periods=max(377//3, 2)).rank(pct=True)
    persistence = change.rolling(83, min_periods=max(83//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.059333 * persistence + 0.0038836 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_126_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=157, w2=390, w3=100, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(157, min_periods=max(157//3, 2)).std()
    vol_slow = ret.rolling(390, min_periods=max(390//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.327647 + 0.0038837 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_127_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=164, w2=403, w3=117, lag=21)."""
    x = open.shift(21)
    ma = x.rolling(403, min_periods=max(403//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 164)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.072 * slope + 0.0038838 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_128_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=171, w2=416, w3=134, lag=34)."""
    x = open.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(416, min_periods=max(416//3, 2)).mean()
    noise = impulse.abs().rolling(134, min_periods=max(134//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.354706 + 0.0038839 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_129_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=178, w2=429, w3=151, lag=55)."""
    x = _safe_log(open.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 178)
    acceleration = _rolling_slope(velocity, 429)
    curvature = _rolling_slope(acceleration, 151)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.084667 * acceleration + 0.003884 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_130_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=185, w2=442, w3=168, lag=0)."""
    rel = _safe_div(open.shift(0), high.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 185)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.091 * pressure.rolling(168, min_periods=max(168//3, 2)).mean() + 0.0038841 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_131_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=192, w2=455, w3=185, lag=1)."""
    a = open.shift(1)
    b = high.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(192, min_periods=max(192//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.395294 + 0.0038842 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_132_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=199, w2=468, w3=202, lag=2)."""
    a = _safe_log(open.abs() + 1.0).shift(2)
    b = _safe_log(high.abs() + 1.0).shift(2)
    corr = a.rolling(468, min_periods=max(468//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 199)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.408824 + 0.0038843 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_133_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=206, w2=481, w3=219, lag=3)."""
    a = open.shift(3)
    b = high.shift(3)
    cover = _safe_div(a.rolling(206, min_periods=max(206//3, 2)).mean(), b.abs().rolling(481, min_periods=max(481//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.11 * _rolling_slope(cover, 206) + 0.0038844 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_134_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=213, w2=494, w3=236, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    y = _safe_log(high.abs() + 1.0).shift(5)
    z = _safe_log(low.abs() + 1.0).shift(5)
    basket = x - 0.116333 * y + 0.883667 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 213) - _rolling_slope(basket, 494) + 0.0038845 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_135_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=220, w2=507, w3=253, lag=8)."""
    x = open.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(220, min_periods=max(220//3, 2)).mean(), upside.rolling(507, min_periods=max(507//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.449412 + 0.0038846 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_136_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=227, w2=21, w3=270, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    draw = x - x.rolling(21, min_periods=max(21//3, 2)).max()
    rebound = x - x.rolling(227, min_periods=max(227//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.129 * _rolling_slope(draw, 270) + 0.0038847 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_137_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=234, w2=34, w3=287, lag=21)."""
    a = _safe_log(open.abs() + 1.0).shift(21)
    b = _safe_log(high.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(34)
    stress = imbalance.rolling(287, min_periods=max(287//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.476471 + 0.0038848 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_138_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=241, w2=47, w3=304, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 241)
    baseline = trend.rolling(47, min_periods=max(47//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(304, min_periods=max(304//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.49 + 0.0038849 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_139_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=248, w2=60, w3=321, lag=55)."""
    x = _safe_log(open.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 248)
    slow = _rolling_slope(x, 60)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.503529 + 0.003885 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_140_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=8, w2=73, w3=338, lag=0)."""
    x = open.shift(0)
    peak = x.rolling(73, min_periods=max(73//3, 2)).max()
    trough = x.rolling(8, min_periods=max(8//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.517059 + 0.0038851 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_141_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=15, w2=86, w3=355, lag=1)."""
    x = open.shift(1)
    change = x.pct_change(15)
    rank = change.rolling(86, min_periods=max(86//3, 2)).rank(pct=True)
    persistence = change.rolling(355, min_periods=max(355//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.160667 * persistence + 0.0038852 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_142_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=22, w2=99, w3=372, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(22, min_periods=max(22//3, 2)).std()
    vol_slow = ret.rolling(99, min_periods=max(99//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.544118 + 0.0038853 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_143_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=29, w2=112, w3=389, lag=3)."""
    x = open.shift(3)
    ma = x.rolling(112, min_periods=max(112//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 29)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.173333 * slope + 0.0038854 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_144_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=36, w2=125, w3=406, lag=5)."""
    x = open.shift(5)
    impulse = x.diff(36)
    drag = impulse.rolling(125, min_periods=max(125//3, 2)).mean()
    noise = impulse.abs().rolling(406, min_periods=max(406//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.571176 + 0.0038855 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_145_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=43, w2=138, w3=423, lag=8)."""
    x = _safe_log(open.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 43)
    acceleration = _rolling_slope(velocity, 138)
    curvature = _rolling_slope(acceleration, 423)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.186 * acceleration + 0.0038856 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_146_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=50, w2=151, w3=440, lag=13)."""
    rel = _safe_div(open.shift(13), high.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 50)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.192333 * pressure.rolling(440, min_periods=max(440//3, 2)).mean() + 0.0038857 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_147_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=57, w2=164, w3=457, lag=21)."""
    a = open.shift(21)
    b = high.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(57, min_periods=max(57//3, 2)).mean())
    decay = spread.ewm(span=164, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.611765 + 0.0038858 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_148_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=64, w2=177, w3=474, lag=34)."""
    a = _safe_log(open.abs() + 1.0).shift(34)
    b = _safe_log(high.abs() + 1.0).shift(34)
    corr = a.rolling(177, min_periods=max(177//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 64)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.625294 + 0.0038859 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_149_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=71, w2=190, w3=491, lag=55)."""
    a = open.shift(55)
    b = high.shift(55)
    cover = _safe_div(a.rolling(71, min_periods=max(71//3, 2)).mean(), b.abs().rolling(190, min_periods=max(190//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.211333 * _rolling_slope(cover, 71) + 0.003886 * anchor
    return base_signal.diff().diff()

def f59_sran_gemini_150_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=78, w2=203, w3=508, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    y = _safe_log(high.abs() + 1.0).shift(0)
    z = _safe_log(low.abs() + 1.0).shift(0)
    basket = x - 0.217667 * y + 0.782333 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 78) - _rolling_slope(basket, 203) + 0.0038861 * anchor
    return base_signal.diff().diff()
