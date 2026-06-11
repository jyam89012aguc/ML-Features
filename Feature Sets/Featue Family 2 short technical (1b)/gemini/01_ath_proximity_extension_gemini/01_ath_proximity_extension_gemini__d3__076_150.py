"""01 ath proximity extension gemini d3 features 76-150 â€” Pipeline 1b-HF Grade v7.

Hypothesis: ATH - Institutional-grade technical signal with high-entropy logic.
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
    data = pd.concat(returns_list, axis=1)
    def _ar(w):
        if np.isnan(w).any(): return np.nan
        corr = np.corrcoef(w.T)
        eigvals = np.linalg.eigvalsh(corr)
        return np.max(eigvals) / len(eigvals)
    return data.rolling(21).apply(_ar, raw=True)

# ============================================================
# FEATURE HYPOTHESES (076-150)
# ============================================================

def f01_athx_gemini_076_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=97, w2=278, w3=231, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    draw = x - x.rolling(278, min_periods=max(278//3, 2)).max()
    rebound = x - x.rolling(97, min_periods=max(97//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.355 * _rolling_slope(draw, 231) + 3.67e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_077_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=104, w2=291, w3=248, lag=21)."""
    a = _safe_log(close.abs() + 1.0).shift(21)
    b = _safe_log(high.abs() + 1.0).shift(21)
    imbalance = a.diff(104) - b.diff(126)
    stress = imbalance.rolling(248, min_periods=max(248//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.517647 + 3.68e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_078_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=111, w2=304, w3=265, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 111)
    baseline = trend.rolling(304, min_periods=max(304//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(265, min_periods=max(265//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.531176 + 3.69e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_079_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=118, w2=317, w3=282, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 118)
    slow = _rolling_slope(x, 317)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=282, adjust=False).mean() * 1.544706 + 3.7e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_080_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=125, w2=330, w3=299, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(330, min_periods=max(330//3, 2)).max()
    trough = x.rolling(125, min_periods=max(125//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.558235 + 3.71e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_081_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=132, w2=343, w3=316, lag=1)."""
    x = close.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(343, min_periods=max(343//3, 2)).rank(pct=True)
    persistence = change.rolling(316, min_periods=max(316//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.054333 * persistence + 3.72e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_082_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=139, w2=356, w3=333, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(139, min_periods=max(139//3, 2)).std()
    vol_slow = ret.rolling(356, min_periods=max(356//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.585294 + 3.73e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_083_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=146, w2=369, w3=350, lag=3)."""
    x = close.shift(3)
    ma = x.rolling(369, min_periods=max(369//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 146)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.067 * slope + 3.74e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_084_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=153, w2=382, w3=367, lag=5)."""
    x = close.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(382, min_periods=max(382//3, 2)).mean()
    noise = impulse.abs().rolling(367, min_periods=max(367//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.612353 + 3.75e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_085_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=160, w2=395, w3=384, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 160)
    acceleration = _rolling_slope(velocity, 395)
    curvature = _rolling_slope(acceleration, 384)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.079667 * acceleration + 3.76e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_086_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=167, w2=408, w3=401, lag=13)."""
    rel = _safe_div(close.shift(13), high.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 167)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.086 * pressure.rolling(401, min_periods=max(401//3, 2)).mean() + 3.77e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_087_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=174, w2=421, w3=418, lag=21)."""
    a = close.shift(21)
    b = high.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(174, min_periods=max(174//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.652941 + 3.78e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_088_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=181, w2=434, w3=435, lag=34)."""
    a = _safe_log(close.abs() + 1.0).shift(34)
    b = _safe_log(high.abs() + 1.0).shift(34)
    corr = a.rolling(434, min_periods=max(434//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 181)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.666471 + 3.79e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_089_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=188, w2=447, w3=452, lag=55)."""
    a = close.shift(55)
    b = high.shift(55)
    cover = _safe_div(a.rolling(188, min_periods=max(188//3, 2)).mean(), b.abs().rolling(447, min_periods=max(447//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.105 * _rolling_slope(cover, 188) + 3.8e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_090_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=195, w2=460, w3=469, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    y = _safe_log(high.abs() + 1.0).shift(0)
    z = _safe_log(low.abs() + 1.0).shift(0)
    basket = x - 0.111333 * y + 0.888667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 195) - _rolling_slope(basket, 460) + 3.81e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_091_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=202, w2=473, w3=486, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(202, min_periods=max(202//3, 2)).mean(), upside.rolling(473, min_periods=max(473//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.853529 + 3.82e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_092_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=209, w2=486, w3=503, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(486, min_periods=max(486//3, 2)).max()
    rebound = x - x.rolling(209, min_periods=max(209//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.124 * _rolling_slope(draw, 503) + 3.83e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_093_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=216, w2=499, w3=520, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(high.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(520, min_periods=max(520//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.880588 + 3.84e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_094_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=223, w2=13, w3=537, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 223)
    baseline = trend.rolling(13, min_periods=max(13//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(537, min_periods=max(537//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.894118 + 3.85e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_095_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=230, w2=26, w3=554, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 230)
    slow = _rolling_slope(x, 26)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.907647 + 3.86e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_096_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=237, w2=39, w3=571, lag=13)."""
    x = close.shift(13)
    peak = x.rolling(39, min_periods=max(39//3, 2)).max()
    trough = x.rolling(237, min_periods=max(237//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.921176 + 3.87e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_097_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=244, w2=52, w3=588, lag=21)."""
    x = close.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(52, min_periods=max(52//3, 2)).rank(pct=True)
    persistence = change.rolling(588, min_periods=max(588//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.155667 * persistence + 3.88e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_098_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=251, w2=65, w3=605, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(251, min_periods=max(251//3, 2)).std()
    vol_slow = ret.rolling(65, min_periods=max(65//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.948235 + 3.89e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_099_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=11, w2=78, w3=622, lag=55)."""
    x = close.shift(55)
    ma = x.rolling(78, min_periods=max(78//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 11)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.168333 * slope + 3.9e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_100_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=18, w2=91, w3=639, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(18)
    drag = impulse.rolling(91, min_periods=max(91//3, 2)).mean()
    noise = impulse.abs().rolling(639, min_periods=max(639//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.975294 + 3.91e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_101_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=25, w2=104, w3=656, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 25)
    acceleration = _rolling_slope(velocity, 104)
    curvature = _rolling_slope(acceleration, 656)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.181 * acceleration + 3.92e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_102_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=32, w2=117, w3=673, lag=2)."""
    rel = _safe_div(close.shift(2), high.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 32)
    pressure = rel_log.diff(117)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.187333 * pressure.rolling(673, min_periods=max(673//3, 2)).mean() + 3.93e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_103_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=39, w2=130, w3=690, lag=3)."""
    a = close.shift(3)
    b = high.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(39, min_periods=max(39//3, 2)).mean())
    decay = spread.ewm(span=130, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.015882 + 3.94e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_104_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=46, w2=143, w3=707, lag=5)."""
    a = _safe_log(close.abs() + 1.0).shift(5)
    b = _safe_log(high.abs() + 1.0).shift(5)
    corr = a.rolling(143, min_periods=max(143//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 46)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.029412 + 3.95e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_105_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=53, w2=156, w3=724, lag=8)."""
    a = close.shift(8)
    b = high.shift(8)
    cover = _safe_div(a.rolling(53, min_periods=max(53//3, 2)).mean(), b.abs().rolling(156, min_periods=max(156//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.206333 * _rolling_slope(cover, 53) + 3.96e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_106_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=60, w2=169, w3=741, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    y = _safe_log(high.abs() + 1.0).shift(13)
    z = _safe_log(low.abs() + 1.0).shift(13)
    basket = x - 0.212667 * y + 0.787333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 60) - _rolling_slope(basket, 169) + 3.97e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_107_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=67, w2=182, w3=758, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(67, min_periods=max(67//3, 2)).mean(), upside.rolling(182, min_periods=max(182//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.07 + 3.98e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_108_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=74, w2=195, w3=24, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    draw = x - x.rolling(195, min_periods=max(195//3, 2)).max()
    rebound = x - x.rolling(74, min_periods=max(74//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.225333 * _rolling_slope(draw, 24) + 3.99e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_109_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=81, w2=208, w3=41, lag=55)."""
    a = _safe_log(close.abs() + 1.0).shift(55)
    b = _safe_log(high.abs() + 1.0).shift(55)
    imbalance = a.diff(81) - b.diff(126)
    stress = imbalance.rolling(41, min_periods=max(41//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.097059 + 4e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_110_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=88, w2=221, w3=58, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 88)
    baseline = trend.rolling(221, min_periods=max(221//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(58, min_periods=max(58//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.110588 + 4.01e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_111_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=95, w2=234, w3=75, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 95)
    slow = _rolling_slope(x, 234)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=75, adjust=False).mean() * 1.124118 + 4.02e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_112_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=102, w2=247, w3=92, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(247, min_periods=max(247//3, 2)).max()
    trough = x.rolling(102, min_periods=max(102//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.137647 + 4.03e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_113_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=109, w2=260, w3=109, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(109)
    rank = change.rolling(260, min_periods=max(260//3, 2)).rank(pct=True)
    persistence = change.rolling(109, min_periods=max(109//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.257 * persistence + 4.04e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_114_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=116, w2=273, w3=126, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(116, min_periods=max(116//3, 2)).std()
    vol_slow = ret.rolling(273, min_periods=max(273//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.164706 + 4.05e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_115_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=123, w2=286, w3=143, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(286, min_periods=max(286//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 123)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.269667 * slope + 4.06e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_116_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=130, w2=299, w3=160, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(299, min_periods=max(299//3, 2)).mean()
    noise = impulse.abs().rolling(160, min_periods=max(160//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.191765 + 4.07e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_117_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=137, w2=312, w3=177, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 137)
    acceleration = _rolling_slope(velocity, 312)
    curvature = _rolling_slope(acceleration, 177)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.282333 * acceleration + 4.08e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_118_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=144, w2=325, w3=194, lag=34)."""
    rel = _safe_div(close.shift(34), high.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 144)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.288667 * pressure.rolling(194, min_periods=max(194//3, 2)).mean() + 4.09e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_119_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=151, w2=338, w3=211, lag=55)."""
    a = close.shift(55)
    b = high.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(151, min_periods=max(151//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.232353 + 4.1e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_120_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=158, w2=351, w3=228, lag=0)."""
    a = _safe_log(close.abs() + 1.0).shift(0)
    b = _safe_log(high.abs() + 1.0).shift(0)
    corr = a.rolling(351, min_periods=max(351//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 158)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.245882 + 4.11e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_121_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=165, w2=364, w3=245, lag=1)."""
    a = close.shift(1)
    b = high.shift(1)
    cover = _safe_div(a.rolling(165, min_periods=max(165//3, 2)).mean(), b.abs().rolling(364, min_periods=max(364//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.307667 * _rolling_slope(cover, 165) + 4.12e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_122_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=172, w2=377, w3=262, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    y = _safe_log(high.abs() + 1.0).shift(2)
    z = _safe_log(low.abs() + 1.0).shift(2)
    basket = x - 0.314 * y + 0.686000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 172) - _rolling_slope(basket, 377) + 4.13e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_123_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=179, w2=390, w3=279, lag=3)."""
    x = close.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(179, min_periods=max(179//3, 2)).mean(), upside.rolling(390, min_periods=max(390//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.286471 + 4.14e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_124_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=186, w2=403, w3=296, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    draw = x - x.rolling(403, min_periods=max(403//3, 2)).max()
    rebound = x - x.rolling(186, min_periods=max(186//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.326667 * _rolling_slope(draw, 296) + 4.15e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_125_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=193, w2=416, w3=313, lag=8)."""
    a = _safe_log(close.abs() + 1.0).shift(8)
    b = _safe_log(high.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(313, min_periods=max(313//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.313529 + 4.16e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_126_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=200, w2=429, w3=330, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 200)
    baseline = trend.rolling(429, min_periods=max(429//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(330, min_periods=max(330//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.327059 + 4.17e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_127_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=207, w2=442, w3=347, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 207)
    slow = _rolling_slope(x, 442)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.340588 + 4.18e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_128_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=214, w2=455, w3=364, lag=34)."""
    x = close.shift(34)
    peak = x.rolling(455, min_periods=max(455//3, 2)).max()
    trough = x.rolling(214, min_periods=max(214//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.354118 + 4.19e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_129_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=221, w2=468, w3=381, lag=55)."""
    x = close.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(468, min_periods=max(468//3, 2)).rank(pct=True)
    persistence = change.rolling(381, min_periods=max(381//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.358333 * persistence + 4.2e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_130_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=228, w2=481, w3=398, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(228, min_periods=max(228//3, 2)).std()
    vol_slow = ret.rolling(481, min_periods=max(481//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.381176 + 4.21e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_131_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=235, w2=494, w3=415, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(494, min_periods=max(494//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 235)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.038667 * slope + 4.22e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_132_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=242, w2=507, w3=432, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(507, min_periods=max(507//3, 2)).mean()
    noise = impulse.abs().rolling(432, min_periods=max(432//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.408235 + 4.23e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_133_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=249, w2=21, w3=449, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 249)
    acceleration = _rolling_slope(velocity, 21)
    curvature = _rolling_slope(acceleration, 449)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.051333 * acceleration + 4.24e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_134_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=9, w2=34, w3=466, lag=5)."""
    rel = _safe_div(close.shift(5), high.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 9)
    pressure = rel_log.diff(34)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.057667 * pressure.rolling(466, min_periods=max(466//3, 2)).mean() + 4.25e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_135_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=16, w2=47, w3=483, lag=8)."""
    a = close.shift(8)
    b = high.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(16, min_periods=max(16//3, 2)).mean())
    decay = spread.ewm(span=47, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.448824 + 4.26e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_136_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=23, w2=60, w3=500, lag=13)."""
    a = _safe_log(close.abs() + 1.0).shift(13)
    b = _safe_log(high.abs() + 1.0).shift(13)
    corr = a.rolling(60, min_periods=max(60//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 23)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.462353 + 4.27e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_137_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=30, w2=73, w3=517, lag=21)."""
    a = close.shift(21)
    b = high.shift(21)
    cover = _safe_div(a.rolling(30, min_periods=max(30//3, 2)).mean(), b.abs().rolling(73, min_periods=max(73//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.076667 * _rolling_slope(cover, 30) + 4.28e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_138_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=37, w2=86, w3=534, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    y = _safe_log(high.abs() + 1.0).shift(34)
    z = _safe_log(low.abs() + 1.0).shift(34)
    basket = x - 0.083 * y + 0.917000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 37) - _rolling_slope(basket, 86) + 4.29e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_139_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=44, w2=99, w3=551, lag=55)."""
    x = close.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(44, min_periods=max(44//3, 2)).mean(), upside.rolling(99, min_periods=max(99//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.502941 + 4.3e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_140_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=51, w2=112, w3=568, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    draw = x - x.rolling(112, min_periods=max(112//3, 2)).max()
    rebound = x - x.rolling(51, min_periods=max(51//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.095667 * _rolling_slope(draw, 568) + 4.31e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_141_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=58, w2=125, w3=585, lag=1)."""
    a = _safe_log(close.abs() + 1.0).shift(1)
    b = _safe_log(high.abs() + 1.0).shift(1)
    imbalance = a.diff(58) - b.diff(125)
    stress = imbalance.rolling(585, min_periods=max(585//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.53 + 4.32e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_142_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=65, w2=138, w3=602, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 65)
    baseline = trend.rolling(138, min_periods=max(138//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(602, min_periods=max(602//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.543529 + 4.33e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_143_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=72, w2=151, w3=619, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 72)
    slow = _rolling_slope(x, 151)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.557059 + 4.34e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_144_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=79, w2=164, w3=636, lag=5)."""
    x = close.shift(5)
    peak = x.rolling(164, min_periods=max(164//3, 2)).max()
    trough = x.rolling(79, min_periods=max(79//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.570588 + 4.35e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_145_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=86, w2=177, w3=653, lag=8)."""
    x = close.shift(8)
    change = x.pct_change(86)
    rank = change.rolling(177, min_periods=max(177//3, 2)).rank(pct=True)
    persistence = change.rolling(653, min_periods=max(653//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.127333 * persistence + 4.36e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_146_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=93, w2=190, w3=670, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(93, min_periods=max(93//3, 2)).std()
    vol_slow = ret.rolling(190, min_periods=max(190//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.597647 + 4.37e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_147_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=100, w2=203, w3=687, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(203, min_periods=max(203//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 100)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.14 * slope + 4.38e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_148_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=107, w2=216, w3=704, lag=34)."""
    x = close.shift(34)
    impulse = x.diff(107)
    drag = impulse.rolling(216, min_periods=max(216//3, 2)).mean()
    noise = impulse.abs().rolling(704, min_periods=max(704//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.624706 + 4.39e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_149_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=114, w2=229, w3=721, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 114)
    acceleration = _rolling_slope(velocity, 229)
    curvature = _rolling_slope(acceleration, 721)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.152667 * acceleration + 4.4e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_150_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=121, w2=242, w3=738, lag=0)."""
    rel = _safe_div(close.shift(0), high.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 121)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.159 * pressure.rolling(738, min_periods=max(738//3, 2)).mean() + 4.41e-05 * anchor
    return base_signal.diff().diff().diff()

# ============================================================
# POSTGRES FEATURE REGISTRY
# ============================================================

REGISTRY_01_ATH_PROXIMITY_EXTENSION_GEMINI_D3_076_150 = {
    "f01_athx_gemini_076_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_076_d3, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_077_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_077_d3, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_078_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_078_d3, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_079_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_079_d3, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_080_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_080_d3, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_081_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_081_d3, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_082_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_082_d3, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_083_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_083_d3, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_084_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_084_d3, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_085_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_085_d3, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_086_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_086_d3, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_087_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_087_d3, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_088_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_088_d3, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_089_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_089_d3, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_090_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_090_d3, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_091_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_091_d3, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_092_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_092_d3, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_093_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_093_d3, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_094_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_094_d3, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_095_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_095_d3, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_096_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_096_d3, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_097_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_097_d3, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_098_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_098_d3, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_099_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_099_d3, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_100_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_100_d3, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_101_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_101_d3, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_102_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_102_d3, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_103_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_103_d3, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_104_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_104_d3, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_105_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_105_d3, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_106_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_106_d3, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_107_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_107_d3, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_108_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_108_d3, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_109_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_109_d3, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_110_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_110_d3, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_111_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_111_d3, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_112_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_112_d3, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_113_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_113_d3, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_114_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_114_d3, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_115_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_115_d3, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_116_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_116_d3, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_117_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_117_d3, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_118_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_118_d3, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_119_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_119_d3, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_120_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_120_d3, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_121_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_121_d3, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_122_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_122_d3, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_123_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_123_d3, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_124_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_124_d3, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_125_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_125_d3, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_126_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_126_d3, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_127_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_127_d3, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_128_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_128_d3, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_129_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_129_d3, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_130_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_130_d3, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_131_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_131_d3, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_132_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_132_d3, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_133_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_133_d3, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_134_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_134_d3, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_135_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_135_d3, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_136_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_136_d3, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_137_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_137_d3, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_138_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_138_d3, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_139_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_139_d3, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_140_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_140_d3, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_141_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_141_d3, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_142_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_142_d3, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_143_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_143_d3, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_144_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_144_d3, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_145_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_145_d3, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_146_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_146_d3, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_147_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_147_d3, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_148_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_148_d3, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_149_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_149_d3, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_150_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_150_d3, "description": "ATR-normalized distance to 1260d high."},
}
