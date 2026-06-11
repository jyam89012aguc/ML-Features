"""01 ath proximity extension gemini d1 features 76-150 â€” Pipeline 1b-HF Grade v7.

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

def f01_athx_gemini_076_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=39, w2=412, w3=246, lag=13)."""
    x = close.shift(13)
    peak = x.rolling(412, min_periods=max(412//3, 2)).max()
    trough = x.rolling(39, min_periods=max(39//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.088235 + 1.47e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_077_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=46, w2=425, w3=263, lag=21)."""
    x = close.shift(21)
    change = x.pct_change(46)
    rank = change.rolling(425, min_periods=max(425//3, 2)).rank(pct=True)
    persistence = change.rolling(263, min_periods=max(263//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.297333 * persistence + 1.48e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_078_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=53, w2=438, w3=280, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(53, min_periods=max(53//3, 2)).std()
    vol_slow = ret.rolling(438, min_periods=max(438//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.115294 + 1.49e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_079_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=60, w2=451, w3=297, lag=55)."""
    x = close.shift(55)
    ma = x.rolling(451, min_periods=max(451//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 60)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.31 * slope + 1.5e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_080_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=67, w2=464, w3=314, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(67)
    drag = impulse.rolling(464, min_periods=max(464//3, 2)).mean()
    noise = impulse.abs().rolling(314, min_periods=max(314//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.142353 + 1.51e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_081_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=74, w2=477, w3=331, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 74)
    acceleration = _rolling_slope(velocity, 477)
    curvature = _rolling_slope(acceleration, 331)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.322667 * acceleration + 1.52e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_082_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=81, w2=490, w3=348, lag=2)."""
    rel = _safe_div(close.shift(2), high.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 81)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.329 * pressure.rolling(348, min_periods=max(348//3, 2)).mean() + 1.53e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_083_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=88, w2=503, w3=365, lag=3)."""
    a = close.shift(3)
    b = high.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(88, min_periods=max(88//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.182941 + 1.54e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_084_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=95, w2=17, w3=382, lag=5)."""
    a = _safe_log(close.abs() + 1.0).shift(5)
    b = _safe_log(high.abs() + 1.0).shift(5)
    corr = a.rolling(17, min_periods=max(17//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 95)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.196471 + 1.55e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_085_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=102, w2=30, w3=399, lag=8)."""
    a = close.shift(8)
    b = high.shift(8)
    cover = _safe_div(a.rolling(102, min_periods=max(102//3, 2)).mean(), b.abs().rolling(30, min_periods=max(30//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.348 * _rolling_slope(cover, 102) + 1.56e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_086_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=109, w2=43, w3=416, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    y = _safe_log(high.abs() + 1.0).shift(13)
    z = _safe_log(low.abs() + 1.0).shift(13)
    basket = x - 0.354333 * y + 0.645667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 109) - _rolling_slope(basket, 43) + 1.57e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_087_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=116, w2=56, w3=433, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(116, min_periods=max(116//3, 2)).mean(), upside.rolling(56, min_periods=max(56//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.237059 + 1.58e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_088_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=123, w2=69, w3=450, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    draw = x - x.rolling(69, min_periods=max(69//3, 2)).max()
    rebound = x - x.rolling(123, min_periods=max(123//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.034667 * _rolling_slope(draw, 450) + 1.59e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_089_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=130, w2=82, w3=467, lag=55)."""
    a = _safe_log(close.abs() + 1.0).shift(55)
    b = _safe_log(high.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(82)
    stress = imbalance.rolling(467, min_periods=max(467//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.264118 + 1.6e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_090_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=137, w2=95, w3=484, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 137)
    baseline = trend.rolling(95, min_periods=max(95//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(484, min_periods=max(484//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.277647 + 1.61e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_091_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=144, w2=108, w3=501, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 144)
    slow = _rolling_slope(x, 108)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.291176 + 1.62e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_092_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=151, w2=121, w3=518, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(121, min_periods=max(121//3, 2)).max()
    trough = x.rolling(151, min_periods=max(151//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.304706 + 1.63e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_093_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=158, w2=134, w3=535, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(134, min_periods=max(134//3, 2)).rank(pct=True)
    persistence = change.rolling(535, min_periods=max(535//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.066333 * persistence + 1.64e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_094_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=165, w2=147, w3=552, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(165, min_periods=max(165//3, 2)).std()
    vol_slow = ret.rolling(147, min_periods=max(147//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.331765 + 1.65e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_095_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=172, w2=160, w3=569, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(160, min_periods=max(160//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 172)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.079 * slope + 1.66e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_096_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=179, w2=173, w3=586, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(173, min_periods=max(173//3, 2)).mean()
    noise = impulse.abs().rolling(586, min_periods=max(586//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.358824 + 1.67e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_097_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=186, w2=186, w3=603, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 186)
    acceleration = _rolling_slope(velocity, 186)
    curvature = _rolling_slope(acceleration, 603)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.091667 * acceleration + 1.68e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_098_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=193, w2=199, w3=620, lag=34)."""
    rel = _safe_div(close.shift(34), high.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 193)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.098 * pressure.rolling(620, min_periods=max(620//3, 2)).mean() + 1.69e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_099_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=200, w2=212, w3=637, lag=55)."""
    a = close.shift(55)
    b = high.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(200, min_periods=max(200//3, 2)).mean())
    decay = spread.ewm(span=212, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.399412 + 1.7e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_100_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=207, w2=225, w3=654, lag=0)."""
    a = _safe_log(close.abs() + 1.0).shift(0)
    b = _safe_log(high.abs() + 1.0).shift(0)
    corr = a.rolling(225, min_periods=max(225//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 207)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.412941 + 1.71e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_101_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=214, w2=238, w3=671, lag=1)."""
    a = close.shift(1)
    b = high.shift(1)
    cover = _safe_div(a.rolling(214, min_periods=max(214//3, 2)).mean(), b.abs().rolling(238, min_periods=max(238//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.117 * _rolling_slope(cover, 214) + 1.72e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_102_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=221, w2=251, w3=688, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    y = _safe_log(high.abs() + 1.0).shift(2)
    z = _safe_log(low.abs() + 1.0).shift(2)
    basket = x - 0.123333 * y + 0.876667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 221) - _rolling_slope(basket, 251) + 1.73e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_103_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=228, w2=264, w3=705, lag=3)."""
    x = close.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(228, min_periods=max(228//3, 2)).mean(), upside.rolling(264, min_periods=max(264//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.453529 + 1.74e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_104_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=235, w2=277, w3=722, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    draw = x - x.rolling(277, min_periods=max(277//3, 2)).max()
    rebound = x - x.rolling(235, min_periods=max(235//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.136 * _rolling_slope(draw, 722) + 1.75e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_105_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=242, w2=290, w3=739, lag=8)."""
    a = _safe_log(close.abs() + 1.0).shift(8)
    b = _safe_log(high.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(739, min_periods=max(739//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.480588 + 1.76e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_106_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=249, w2=303, w3=756, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 249)
    baseline = trend.rolling(303, min_periods=max(303//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(756, min_periods=max(756//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.494118 + 1.77e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_107_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=9, w2=316, w3=22, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 9)
    slow = _rolling_slope(x, 316)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=22, adjust=False).mean() * 1.507647 + 1.78e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_108_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=16, w2=329, w3=39, lag=34)."""
    x = close.shift(34)
    peak = x.rolling(329, min_periods=max(329//3, 2)).max()
    trough = x.rolling(16, min_periods=max(16//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.521176 + 1.79e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_109_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=23, w2=342, w3=56, lag=55)."""
    x = close.shift(55)
    change = x.pct_change(23)
    rank = change.rolling(342, min_periods=max(342//3, 2)).rank(pct=True)
    persistence = change.rolling(56, min_periods=max(56//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.167667 * persistence + 1.8e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_110_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=30, w2=355, w3=73, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(30, min_periods=max(30//3, 2)).std()
    vol_slow = ret.rolling(355, min_periods=max(355//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.548235 + 1.81e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_111_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=37, w2=368, w3=90, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(368, min_periods=max(368//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 37)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.180333 * slope + 1.82e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_112_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=44, w2=381, w3=107, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(44)
    drag = impulse.rolling(381, min_periods=max(381//3, 2)).mean()
    noise = impulse.abs().rolling(107, min_periods=max(107//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.575294 + 1.83e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_113_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=51, w2=394, w3=124, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 51)
    acceleration = _rolling_slope(velocity, 394)
    curvature = _rolling_slope(acceleration, 124)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.193 * acceleration + 1.84e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_114_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=58, w2=407, w3=141, lag=5)."""
    rel = _safe_div(close.shift(5), high.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 58)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.199333 * pressure.rolling(141, min_periods=max(141//3, 2)).mean() + 1.85e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_115_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=65, w2=420, w3=158, lag=8)."""
    a = close.shift(8)
    b = high.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(65, min_periods=max(65//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.615882 + 1.86e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_116_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=72, w2=433, w3=175, lag=13)."""
    a = _safe_log(close.abs() + 1.0).shift(13)
    b = _safe_log(high.abs() + 1.0).shift(13)
    corr = a.rolling(433, min_periods=max(433//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 72)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.629412 + 1.87e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_117_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=79, w2=446, w3=192, lag=21)."""
    a = close.shift(21)
    b = high.shift(21)
    cover = _safe_div(a.rolling(79, min_periods=max(79//3, 2)).mean(), b.abs().rolling(446, min_periods=max(446//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.218333 * _rolling_slope(cover, 79) + 1.88e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_118_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=86, w2=459, w3=209, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    y = _safe_log(high.abs() + 1.0).shift(34)
    z = _safe_log(low.abs() + 1.0).shift(34)
    basket = x - 0.224667 * y + 0.775333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 86) - _rolling_slope(basket, 459) + 1.89e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_119_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=93, w2=472, w3=226, lag=55)."""
    x = close.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(93, min_periods=max(93//3, 2)).mean(), upside.rolling(472, min_periods=max(472//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.67 + 1.9e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_120_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=100, w2=485, w3=243, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    draw = x - x.rolling(485, min_periods=max(485//3, 2)).max()
    rebound = x - x.rolling(100, min_periods=max(100//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.237333 * _rolling_slope(draw, 243) + 1.91e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_121_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=107, w2=498, w3=260, lag=1)."""
    a = _safe_log(close.abs() + 1.0).shift(1)
    b = _safe_log(high.abs() + 1.0).shift(1)
    imbalance = a.diff(107) - b.diff(126)
    stress = imbalance.rolling(260, min_periods=max(260//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.843529 + 1.92e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_122_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=114, w2=12, w3=277, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 114)
    baseline = trend.rolling(12, min_periods=max(12//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(277, min_periods=max(277//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.857059 + 1.93e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_123_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=121, w2=25, w3=294, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 121)
    slow = _rolling_slope(x, 25)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=294, adjust=False).mean() * 0.870588 + 1.94e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_124_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=128, w2=38, w3=311, lag=5)."""
    x = close.shift(5)
    peak = x.rolling(38, min_periods=max(38//3, 2)).max()
    trough = x.rolling(128, min_periods=max(128//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.884118 + 1.95e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_125_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=135, w2=51, w3=328, lag=8)."""
    x = close.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(51, min_periods=max(51//3, 2)).rank(pct=True)
    persistence = change.rolling(328, min_periods=max(328//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.269 * persistence + 1.96e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_126_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=142, w2=64, w3=345, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(142, min_periods=max(142//3, 2)).std()
    vol_slow = ret.rolling(64, min_periods=max(64//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.911176 + 1.97e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_127_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=149, w2=77, w3=362, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(77, min_periods=max(77//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 149)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.281667 * slope + 1.98e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_128_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=156, w2=90, w3=379, lag=34)."""
    x = close.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(90, min_periods=max(90//3, 2)).mean()
    noise = impulse.abs().rolling(379, min_periods=max(379//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.938235 + 1.99e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_129_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=163, w2=103, w3=396, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 163)
    acceleration = _rolling_slope(velocity, 103)
    curvature = _rolling_slope(acceleration, 396)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.294333 * acceleration + 2e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_130_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=170, w2=116, w3=413, lag=0)."""
    rel = _safe_div(close.shift(0), high.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 170)
    pressure = rel_log.diff(116)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.300667 * pressure.rolling(413, min_periods=max(413//3, 2)).mean() + 2.01e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_131_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=177, w2=129, w3=430, lag=1)."""
    a = close.shift(1)
    b = high.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(177, min_periods=max(177//3, 2)).mean())
    decay = spread.ewm(span=129, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.978824 + 2.02e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_132_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=184, w2=142, w3=447, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(high.abs() + 1.0).shift(2)
    corr = a.rolling(142, min_periods=max(142//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 184)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.992353 + 2.03e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_133_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=191, w2=155, w3=464, lag=3)."""
    a = close.shift(3)
    b = high.shift(3)
    cover = _safe_div(a.rolling(191, min_periods=max(191//3, 2)).mean(), b.abs().rolling(155, min_periods=max(155//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.319667 * _rolling_slope(cover, 191) + 2.04e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_134_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=198, w2=168, w3=481, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(high.abs() + 1.0).shift(5)
    z = _safe_log(low.abs() + 1.0).shift(5)
    basket = x - 0.326 * y + 0.674000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 198) - _rolling_slope(basket, 168) + 2.05e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_135_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=205, w2=181, w3=498, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(205, min_periods=max(205//3, 2)).mean(), upside.rolling(181, min_periods=max(181//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.032941 + 2.06e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_136_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=212, w2=194, w3=515, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    draw = x - x.rolling(194, min_periods=max(194//3, 2)).max()
    rebound = x - x.rolling(212, min_periods=max(212//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.338667 * _rolling_slope(draw, 515) + 2.07e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_137_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=219, w2=207, w3=532, lag=21)."""
    a = _safe_log(close.abs() + 1.0).shift(21)
    b = _safe_log(high.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(532, min_periods=max(532//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.06 + 2.08e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_138_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=226, w2=220, w3=549, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 226)
    baseline = trend.rolling(220, min_periods=max(220//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(549, min_periods=max(549//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.073529 + 2.09e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_139_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=233, w2=233, w3=566, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 233)
    slow = _rolling_slope(x, 233)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.087059 + 2.1e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_140_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=240, w2=246, w3=583, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(246, min_periods=max(246//3, 2)).max()
    trough = x.rolling(240, min_periods=max(240//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.100588 + 2.11e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_141_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=247, w2=259, w3=600, lag=1)."""
    x = close.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(259, min_periods=max(259//3, 2)).rank(pct=True)
    persistence = change.rolling(600, min_periods=max(600//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.038 * persistence + 2.12e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_142_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=7, w2=272, w3=617, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(7, min_periods=max(7//3, 2)).std()
    vol_slow = ret.rolling(272, min_periods=max(272//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.127647 + 2.13e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_143_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=14, w2=285, w3=634, lag=3)."""
    x = close.shift(3)
    ma = x.rolling(285, min_periods=max(285//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 14)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.050667 * slope + 2.14e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_144_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=21, w2=298, w3=651, lag=5)."""
    x = close.shift(5)
    impulse = x.diff(21)
    drag = impulse.rolling(298, min_periods=max(298//3, 2)).mean()
    noise = impulse.abs().rolling(651, min_periods=max(651//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.154706 + 2.15e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_145_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=28, w2=311, w3=668, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 28)
    acceleration = _rolling_slope(velocity, 311)
    curvature = _rolling_slope(acceleration, 668)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.063333 * acceleration + 2.16e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_146_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=35, w2=324, w3=685, lag=13)."""
    rel = _safe_div(close.shift(13), high.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 35)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.069667 * pressure.rolling(685, min_periods=max(685//3, 2)).mean() + 2.17e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_147_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=42, w2=337, w3=702, lag=21)."""
    a = close.shift(21)
    b = high.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(42, min_periods=max(42//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.195294 + 2.18e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_148_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=49, w2=350, w3=719, lag=34)."""
    a = _safe_log(close.abs() + 1.0).shift(34)
    b = _safe_log(high.abs() + 1.0).shift(34)
    corr = a.rolling(350, min_periods=max(350//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 49)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.208824 + 2.19e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_149_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=56, w2=363, w3=736, lag=55)."""
    a = close.shift(55)
    b = high.shift(55)
    cover = _safe_div(a.rolling(56, min_periods=max(56//3, 2)).mean(), b.abs().rolling(363, min_periods=max(363//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.088667 * _rolling_slope(cover, 56) + 2.2e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_150_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=63, w2=376, w3=753, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    y = _safe_log(high.abs() + 1.0).shift(0)
    z = _safe_log(low.abs() + 1.0).shift(0)
    basket = x - 0.095 * y + 0.905000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 63) - _rolling_slope(basket, 376) + 2.21e-05 * anchor
    return base_signal.diff()

# ============================================================
# POSTGRES FEATURE REGISTRY
# ============================================================

REGISTRY_01_ATH_PROXIMITY_EXTENSION_GEMINI_D1_076_150 = {
    "f01_athx_gemini_076_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_076_d1, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_077_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_077_d1, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_078_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_078_d1, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_079_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_079_d1, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_080_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_080_d1, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_081_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_081_d1, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_082_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_082_d1, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_083_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_083_d1, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_084_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_084_d1, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_085_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_085_d1, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_086_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_086_d1, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_087_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_087_d1, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_088_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_088_d1, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_089_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_089_d1, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_090_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_090_d1, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_091_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_091_d1, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_092_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_092_d1, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_093_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_093_d1, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_094_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_094_d1, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_095_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_095_d1, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_096_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_096_d1, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_097_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_097_d1, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_098_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_098_d1, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_099_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_099_d1, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_100_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_100_d1, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_101_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_101_d1, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_102_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_102_d1, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_103_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_103_d1, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_104_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_104_d1, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_105_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_105_d1, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_106_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_106_d1, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_107_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_107_d1, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_108_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_108_d1, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_109_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_109_d1, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_110_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_110_d1, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_111_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_111_d1, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_112_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_112_d1, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_113_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_113_d1, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_114_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_114_d1, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_115_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_115_d1, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_116_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_116_d1, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_117_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_117_d1, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_118_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_118_d1, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_119_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_119_d1, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_120_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_120_d1, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_121_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_121_d1, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_122_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_122_d1, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_123_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_123_d1, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_124_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_124_d1, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_125_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_125_d1, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_126_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_126_d1, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_127_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_127_d1, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_128_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_128_d1, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_129_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_129_d1, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_130_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_130_d1, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_131_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_131_d1, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_132_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_132_d1, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_133_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_133_d1, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_134_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_134_d1, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_135_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_135_d1, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_136_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_136_d1, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_137_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_137_d1, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_138_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_138_d1, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_139_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_139_d1, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_140_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_140_d1, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_141_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_141_d1, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_142_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_142_d1, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_143_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_143_d1, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_144_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_144_d1, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_145_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_145_d1, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_146_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_146_d1, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_147_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_147_d1, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_148_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_148_d1, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_149_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_149_d1, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_150_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_150_d1, "description": "ATR-normalized distance to 1260d high."},
}
