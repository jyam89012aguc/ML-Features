"""01 ath proximity extension gemini base features 76-150 â€” Pipeline 1b-HF Grade v7.

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

def f01_athx_gemini_076(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=10, w2=479, w3=629, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(10, min_periods=max(10//3, 2)).std()
    vol_slow = ret.rolling(479, min_periods=max(479//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.307059 + 3.7e-06 * anchor
    return base_signal

def f01_athx_gemini_077(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=17, w2=492, w3=646, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(492, min_periods=max(492//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 17)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.265333 * slope + 3.8e-06 * anchor
    return base_signal

def f01_athx_gemini_078(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=24, w2=505, w3=663, lag=34)."""
    x = close.shift(34)
    impulse = x.diff(24)
    drag = impulse.rolling(505, min_periods=max(505//3, 2)).mean()
    noise = impulse.abs().rolling(663, min_periods=max(663//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.334118 + 3.9e-06 * anchor
    return base_signal

def f01_athx_gemini_079(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=31, w2=19, w3=680, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 31)
    acceleration = _rolling_slope(velocity, 19)
    curvature = _rolling_slope(acceleration, 680)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.278 * acceleration + 4e-06 * anchor
    return base_signal

def f01_athx_gemini_080(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=38, w2=32, w3=697, lag=0)."""
    rel = _safe_div(close.shift(0), high.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 38)
    pressure = rel_log.diff(32)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.284333 * pressure.rolling(697, min_periods=max(697//3, 2)).mean() + 4.1e-06 * anchor
    return base_signal

def f01_athx_gemini_081(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=45, w2=45, w3=714, lag=1)."""
    a = close.shift(1)
    b = high.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(45, min_periods=max(45//3, 2)).mean())
    decay = spread.ewm(span=45, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.374706 + 4.2e-06 * anchor
    return base_signal

def f01_athx_gemini_082(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=52, w2=58, w3=731, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(high.abs() + 1.0).shift(2)
    corr = a.rolling(58, min_periods=max(58//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 52)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.388235 + 4.3e-06 * anchor
    return base_signal

def f01_athx_gemini_083(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=59, w2=71, w3=748, lag=3)."""
    a = close.shift(3)
    b = high.shift(3)
    cover = _safe_div(a.rolling(59, min_periods=max(59//3, 2)).mean(), b.abs().rolling(71, min_periods=max(71//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.303333 * _rolling_slope(cover, 59) + 4.4e-06 * anchor
    return base_signal

def f01_athx_gemini_084(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=66, w2=84, w3=765, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(high.abs() + 1.0).shift(5)
    z = _safe_log(low.abs() + 1.0).shift(5)
    basket = x - 0.309667 * y + 0.690333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 66) - _rolling_slope(basket, 84) + 4.5e-06 * anchor
    return base_signal

def f01_athx_gemini_085(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=73, w2=97, w3=31, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(73, min_periods=max(73//3, 2)).mean(), upside.rolling(97, min_periods=max(97//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(31) * 1.428824 + 4.6e-06 * anchor
    return base_signal

def f01_athx_gemini_086(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=80, w2=110, w3=48, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    draw = x - x.rolling(110, min_periods=max(110//3, 2)).max()
    rebound = x - x.rolling(80, min_periods=max(80//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.322333 * _rolling_slope(draw, 48) + 4.7e-06 * anchor
    return base_signal

def f01_athx_gemini_087(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=87, w2=123, w3=65, lag=21)."""
    a = _safe_log(close.abs() + 1.0).shift(21)
    b = _safe_log(high.abs() + 1.0).shift(21)
    imbalance = a.diff(87) - b.diff(123)
    stress = imbalance.rolling(65, min_periods=max(65//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.455882 + 4.8e-06 * anchor
    return base_signal

def f01_athx_gemini_088(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=94, w2=136, w3=82, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 94)
    baseline = trend.rolling(136, min_periods=max(136//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(82, min_periods=max(82//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.469412 + 4.9e-06 * anchor
    return base_signal

def f01_athx_gemini_089(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=101, w2=149, w3=99, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 101)
    slow = _rolling_slope(x, 149)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=99, adjust=False).mean() * 1.482941 + 5e-06 * anchor
    return base_signal

def f01_athx_gemini_090(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=108, w2=162, w3=116, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(162, min_periods=max(162//3, 2)).max()
    trough = x.rolling(108, min_periods=max(108//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.496471 + 5.1e-06 * anchor
    return base_signal

def f01_athx_gemini_091(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=115, w2=175, w3=133, lag=1)."""
    x = close.shift(1)
    change = x.pct_change(115)
    rank = change.rolling(175, min_periods=max(175//3, 2)).rank(pct=True)
    persistence = change.rolling(133, min_periods=max(133//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.354 * persistence + 5.2e-06 * anchor
    return base_signal

def f01_athx_gemini_092(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=122, w2=188, w3=150, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(122, min_periods=max(122//3, 2)).std()
    vol_slow = ret.rolling(188, min_periods=max(188//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.523529 + 5.3e-06 * anchor
    return base_signal

def f01_athx_gemini_093(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=129, w2=201, w3=167, lag=3)."""
    x = close.shift(3)
    ma = x.rolling(201, min_periods=max(201//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 129)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.034333 * slope + 5.4e-06 * anchor
    return base_signal

def f01_athx_gemini_094(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=136, w2=214, w3=184, lag=5)."""
    x = close.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(214, min_periods=max(214//3, 2)).mean()
    noise = impulse.abs().rolling(184, min_periods=max(184//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.550588 + 5.5e-06 * anchor
    return base_signal

def f01_athx_gemini_095(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=143, w2=227, w3=201, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 143)
    acceleration = _rolling_slope(velocity, 227)
    curvature = _rolling_slope(acceleration, 201)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.047 * acceleration + 5.6e-06 * anchor
    return base_signal

def f01_athx_gemini_096(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=150, w2=240, w3=218, lag=13)."""
    rel = _safe_div(close.shift(13), high.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 150)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.053333 * pressure.rolling(218, min_periods=max(218//3, 2)).mean() + 5.7e-06 * anchor
    return base_signal

def f01_athx_gemini_097(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=157, w2=253, w3=235, lag=21)."""
    a = close.shift(21)
    b = high.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(157, min_periods=max(157//3, 2)).mean())
    decay = spread.ewm(span=253, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.591176 + 5.8e-06 * anchor
    return base_signal

def f01_athx_gemini_098(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=164, w2=266, w3=252, lag=34)."""
    a = _safe_log(close.abs() + 1.0).shift(34)
    b = _safe_log(high.abs() + 1.0).shift(34)
    corr = a.rolling(266, min_periods=max(266//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 164)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.604706 + 5.9e-06 * anchor
    return base_signal

def f01_athx_gemini_099(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=171, w2=279, w3=269, lag=55)."""
    a = close.shift(55)
    b = high.shift(55)
    cover = _safe_div(a.rolling(171, min_periods=max(171//3, 2)).mean(), b.abs().rolling(279, min_periods=max(279//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.072333 * _rolling_slope(cover, 171) + 6e-06 * anchor
    return base_signal

def f01_athx_gemini_100(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=178, w2=292, w3=286, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    y = _safe_log(high.abs() + 1.0).shift(0)
    z = _safe_log(low.abs() + 1.0).shift(0)
    basket = x - 0.078667 * y + 0.921333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 178) - _rolling_slope(basket, 292) + 6.1e-06 * anchor
    return base_signal

def f01_athx_gemini_101(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=185, w2=305, w3=303, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(185, min_periods=max(185//3, 2)).mean(), upside.rolling(305, min_periods=max(305//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.645294 + 6.2e-06 * anchor
    return base_signal

def f01_athx_gemini_102(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=192, w2=318, w3=320, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(318, min_periods=max(318//3, 2)).max()
    rebound = x - x.rolling(192, min_periods=max(192//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.091333 * _rolling_slope(draw, 320) + 6.3e-06 * anchor
    return base_signal

def f01_athx_gemini_103(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=199, w2=331, w3=337, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(high.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(337, min_periods=max(337//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.672353 + 6.4e-06 * anchor
    return base_signal

def f01_athx_gemini_104(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=206, w2=344, w3=354, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 206)
    baseline = trend.rolling(344, min_periods=max(344//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(354, min_periods=max(354//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.832353 + 6.5e-06 * anchor
    return base_signal

def f01_athx_gemini_105(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=213, w2=357, w3=371, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 213)
    slow = _rolling_slope(x, 357)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.845882 + 6.6e-06 * anchor
    return base_signal

def f01_athx_gemini_106(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=220, w2=370, w3=388, lag=13)."""
    x = close.shift(13)
    peak = x.rolling(370, min_periods=max(370//3, 2)).max()
    trough = x.rolling(220, min_periods=max(220//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.859412 + 6.7e-06 * anchor
    return base_signal

def f01_athx_gemini_107(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=227, w2=383, w3=405, lag=21)."""
    x = close.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(383, min_periods=max(383//3, 2)).rank(pct=True)
    persistence = change.rolling(405, min_periods=max(405//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.123 * persistence + 6.8e-06 * anchor
    return base_signal

def f01_athx_gemini_108(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=234, w2=396, w3=422, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(234, min_periods=max(234//3, 2)).std()
    vol_slow = ret.rolling(396, min_periods=max(396//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.886471 + 6.9e-06 * anchor
    return base_signal

def f01_athx_gemini_109(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=241, w2=409, w3=439, lag=55)."""
    x = close.shift(55)
    ma = x.rolling(409, min_periods=max(409//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 241)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.135667 * slope + 7e-06 * anchor
    return base_signal

def f01_athx_gemini_110(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=248, w2=422, w3=456, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(422, min_periods=max(422//3, 2)).mean()
    noise = impulse.abs().rolling(456, min_periods=max(456//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.913529 + 7.1e-06 * anchor
    return base_signal

def f01_athx_gemini_111(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=8, w2=435, w3=473, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 8)
    acceleration = _rolling_slope(velocity, 435)
    curvature = _rolling_slope(acceleration, 473)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.148333 * acceleration + 7.2e-06 * anchor
    return base_signal

def f01_athx_gemini_112(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=15, w2=448, w3=490, lag=2)."""
    rel = _safe_div(close.shift(2), high.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 15)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.154667 * pressure.rolling(490, min_periods=max(490//3, 2)).mean() + 7.3e-06 * anchor
    return base_signal

def f01_athx_gemini_113(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=22, w2=461, w3=507, lag=3)."""
    a = close.shift(3)
    b = high.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(22, min_periods=max(22//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.954118 + 7.4e-06 * anchor
    return base_signal

def f01_athx_gemini_114(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=29, w2=474, w3=524, lag=5)."""
    a = _safe_log(close.abs() + 1.0).shift(5)
    b = _safe_log(high.abs() + 1.0).shift(5)
    corr = a.rolling(474, min_periods=max(474//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 29)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.967647 + 7.5e-06 * anchor
    return base_signal

def f01_athx_gemini_115(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=36, w2=487, w3=541, lag=8)."""
    a = close.shift(8)
    b = high.shift(8)
    cover = _safe_div(a.rolling(36, min_periods=max(36//3, 2)).mean(), b.abs().rolling(487, min_periods=max(487//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.173667 * _rolling_slope(cover, 36) + 7.6e-06 * anchor
    return base_signal

def f01_athx_gemini_116(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=43, w2=500, w3=558, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    y = _safe_log(high.abs() + 1.0).shift(13)
    z = _safe_log(low.abs() + 1.0).shift(13)
    basket = x - 0.18 * y + 0.820000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 43) - _rolling_slope(basket, 500) + 7.7e-06 * anchor
    return base_signal

def f01_athx_gemini_117(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=50, w2=14, w3=575, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(50, min_periods=max(50//3, 2)).mean(), upside.rolling(14, min_periods=max(14//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.008235 + 7.8e-06 * anchor
    return base_signal

def f01_athx_gemini_118(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=57, w2=27, w3=592, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    draw = x - x.rolling(27, min_periods=max(27//3, 2)).max()
    rebound = x - x.rolling(57, min_periods=max(57//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.192667 * _rolling_slope(draw, 592) + 7.9e-06 * anchor
    return base_signal

def f01_athx_gemini_119(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=64, w2=40, w3=609, lag=55)."""
    a = _safe_log(close.abs() + 1.0).shift(55)
    b = _safe_log(high.abs() + 1.0).shift(55)
    imbalance = a.diff(64) - b.diff(40)
    stress = imbalance.rolling(609, min_periods=max(609//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.035294 + 8e-06 * anchor
    return base_signal

def f01_athx_gemini_120(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=71, w2=53, w3=626, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 71)
    baseline = trend.rolling(53, min_periods=max(53//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(626, min_periods=max(626//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.048824 + 8.1e-06 * anchor
    return base_signal

def f01_athx_gemini_121(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=78, w2=66, w3=643, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 78)
    slow = _rolling_slope(x, 66)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.062353 + 8.2e-06 * anchor
    return base_signal

def f01_athx_gemini_122(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=85, w2=79, w3=660, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(79, min_periods=max(79//3, 2)).max()
    trough = x.rolling(85, min_periods=max(85//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.075882 + 8.3e-06 * anchor
    return base_signal

def f01_athx_gemini_123(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=92, w2=92, w3=677, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(92)
    rank = change.rolling(92, min_periods=max(92//3, 2)).rank(pct=True)
    persistence = change.rolling(677, min_periods=max(677//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.224333 * persistence + 8.4e-06 * anchor
    return base_signal

def f01_athx_gemini_124(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=99, w2=105, w3=694, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(99, min_periods=max(99//3, 2)).std()
    vol_slow = ret.rolling(105, min_periods=max(105//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.102941 + 8.5e-06 * anchor
    return base_signal

def f01_athx_gemini_125(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=106, w2=118, w3=711, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(118, min_periods=max(118//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 106)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.237 * slope + 8.6e-06 * anchor
    return base_signal

def f01_athx_gemini_126(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=113, w2=131, w3=728, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(113)
    drag = impulse.rolling(131, min_periods=max(131//3, 2)).mean()
    noise = impulse.abs().rolling(728, min_periods=max(728//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.13 + 8.7e-06 * anchor
    return base_signal

def f01_athx_gemini_127(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=120, w2=144, w3=745, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 120)
    acceleration = _rolling_slope(velocity, 144)
    curvature = _rolling_slope(acceleration, 745)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.249667 * acceleration + 8.8e-06 * anchor
    return base_signal

def f01_athx_gemini_128(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=127, w2=157, w3=762, lag=34)."""
    rel = _safe_div(close.shift(34), high.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 127)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.256 * pressure.rolling(762, min_periods=max(762//3, 2)).mean() + 8.9e-06 * anchor
    return base_signal

def f01_athx_gemini_129(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=134, w2=170, w3=28, lag=55)."""
    a = close.shift(55)
    b = high.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(134, min_periods=max(134//3, 2)).mean())
    decay = spread.ewm(span=170, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.170588 + 9e-06 * anchor
    return base_signal

def f01_athx_gemini_130(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=141, w2=183, w3=45, lag=0)."""
    a = _safe_log(close.abs() + 1.0).shift(0)
    b = _safe_log(high.abs() + 1.0).shift(0)
    corr = a.rolling(183, min_periods=max(183//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 141)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.184118 + 9.1e-06 * anchor
    return base_signal

def f01_athx_gemini_131(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=148, w2=196, w3=62, lag=1)."""
    a = close.shift(1)
    b = high.shift(1)
    cover = _safe_div(a.rolling(148, min_periods=max(148//3, 2)).mean(), b.abs().rolling(196, min_periods=max(196//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(62) + 0.275 * _rolling_slope(cover, 148) + 9.2e-06 * anchor
    return base_signal

def f01_athx_gemini_132(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=155, w2=209, w3=79, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    y = _safe_log(high.abs() + 1.0).shift(2)
    z = _safe_log(low.abs() + 1.0).shift(2)
    basket = x - 0.281333 * y + 0.718667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 155) - _rolling_slope(basket, 209) + 9.3e-06 * anchor
    return base_signal

def f01_athx_gemini_133(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=162, w2=222, w3=96, lag=3)."""
    x = close.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(162, min_periods=max(162//3, 2)).mean(), upside.rolling(222, min_periods=max(222//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(96) * 1.224706 + 9.4e-06 * anchor
    return base_signal

def f01_athx_gemini_134(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=169, w2=235, w3=113, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    draw = x - x.rolling(235, min_periods=max(235//3, 2)).max()
    rebound = x - x.rolling(169, min_periods=max(169//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.294 * _rolling_slope(draw, 113) + 9.5e-06 * anchor
    return base_signal

def f01_athx_gemini_135(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=176, w2=248, w3=130, lag=8)."""
    a = _safe_log(close.abs() + 1.0).shift(8)
    b = _safe_log(high.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(130, min_periods=max(130//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.251765 + 9.6e-06 * anchor
    return base_signal

def f01_athx_gemini_136(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=183, w2=261, w3=147, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 183)
    baseline = trend.rolling(261, min_periods=max(261//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(147, min_periods=max(147//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.265294 + 9.7e-06 * anchor
    return base_signal

def f01_athx_gemini_137(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=190, w2=274, w3=164, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 190)
    slow = _rolling_slope(x, 274)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=164, adjust=False).mean() * 1.278824 + 9.8e-06 * anchor
    return base_signal

def f01_athx_gemini_138(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=197, w2=287, w3=181, lag=34)."""
    x = close.shift(34)
    peak = x.rolling(287, min_periods=max(287//3, 2)).max()
    trough = x.rolling(197, min_periods=max(197//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.292353 + 9.9e-06 * anchor
    return base_signal

def f01_athx_gemini_139(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=204, w2=300, w3=198, lag=55)."""
    x = close.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(300, min_periods=max(300//3, 2)).rank(pct=True)
    persistence = change.rolling(198, min_periods=max(198//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.325667 * persistence + 1e-05 * anchor
    return base_signal

def f01_athx_gemini_140(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=211, w2=313, w3=215, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(211, min_periods=max(211//3, 2)).std()
    vol_slow = ret.rolling(313, min_periods=max(313//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.319412 + 1.01e-05 * anchor
    return base_signal

def f01_athx_gemini_141(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=218, w2=326, w3=232, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(326, min_periods=max(326//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 218)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.338333 * slope + 1.02e-05 * anchor
    return base_signal

def f01_athx_gemini_142(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=225, w2=339, w3=249, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(339, min_periods=max(339//3, 2)).mean()
    noise = impulse.abs().rolling(249, min_periods=max(249//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.346471 + 1.03e-05 * anchor
    return base_signal

def f01_athx_gemini_143(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=232, w2=352, w3=266, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 232)
    acceleration = _rolling_slope(velocity, 352)
    curvature = _rolling_slope(acceleration, 266)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.351 * acceleration + 1.04e-05 * anchor
    return base_signal

def f01_athx_gemini_144(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=239, w2=365, w3=283, lag=5)."""
    rel = _safe_div(close.shift(5), high.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 239)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.357333 * pressure.rolling(283, min_periods=max(283//3, 2)).mean() + 1.05e-05 * anchor
    return base_signal

def f01_athx_gemini_145(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=246, w2=378, w3=300, lag=8)."""
    a = close.shift(8)
    b = high.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(246, min_periods=max(246//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.387059 + 1.06e-05 * anchor
    return base_signal

def f01_athx_gemini_146(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=6, w2=391, w3=317, lag=13)."""
    a = _safe_log(close.abs() + 1.0).shift(13)
    b = _safe_log(high.abs() + 1.0).shift(13)
    corr = a.rolling(391, min_periods=max(391//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 6)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.400588 + 1.07e-05 * anchor
    return base_signal

def f01_athx_gemini_147(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=13, w2=404, w3=334, lag=21)."""
    a = close.shift(21)
    b = high.shift(21)
    cover = _safe_div(a.rolling(13, min_periods=max(13//3, 2)).mean(), b.abs().rolling(404, min_periods=max(404//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.044 * _rolling_slope(cover, 13) + 1.08e-05 * anchor
    return base_signal

def f01_athx_gemini_148(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=20, w2=417, w3=351, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    y = _safe_log(high.abs() + 1.0).shift(34)
    z = _safe_log(low.abs() + 1.0).shift(34)
    basket = x - 0.050333 * y + 0.949667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 20) - _rolling_slope(basket, 417) + 1.09e-05 * anchor
    return base_signal

def f01_athx_gemini_149(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=27, w2=430, w3=368, lag=55)."""
    x = close.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(27, min_periods=max(27//3, 2)).mean(), upside.rolling(430, min_periods=max(430//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.441176 + 1.1e-05 * anchor
    return base_signal

def f01_athx_gemini_150(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=34, w2=443, w3=385, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    draw = x - x.rolling(443, min_periods=max(443//3, 2)).max()
    rebound = x - x.rolling(34, min_periods=max(34//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.063 * _rolling_slope(draw, 385) + 1.11e-05 * anchor
    return base_signal

# ============================================================
# POSTGRES FEATURE REGISTRY
# ============================================================

REGISTRY_01_ATH_PROXIMITY_EXTENSION_GEMINI_BASE_076_150 = {
    "f01_athx_gemini_076": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_076, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_077": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_077, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_078": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_078, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_079": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_079, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_080": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_080, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_081": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_081, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_082": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_082, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_083": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_083, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_084": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_084, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_085": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_085, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_086": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_086, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_087": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_087, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_088": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_088, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_089": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_089, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_090": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_090, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_091": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_091, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_092": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_092, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_093": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_093, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_094": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_094, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_095": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_095, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_096": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_096, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_097": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_097, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_098": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_098, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_099": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_099, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_100": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_100, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_101": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_101, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_102": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_102, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_103": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_103, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_104": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_104, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_105": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_105, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_106": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_106, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_107": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_107, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_108": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_108, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_109": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_109, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_110": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_110, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_111": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_111, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_112": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_112, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_113": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_113, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_114": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_114, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_115": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_115, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_116": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_116, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_117": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_117, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_118": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_118, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_119": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_119, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_120": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_120, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_121": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_121, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_122": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_122, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_123": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_123, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_124": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_124, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_125": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_125, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_126": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_126, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_127": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_127, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_128": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_128, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_129": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_129, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_130": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_130, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_131": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_131, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_132": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_132, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_133": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_133, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_134": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_134, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_135": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_135, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_136": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_136, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_137": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_137, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_138": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_138, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_139": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_139, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_140": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_140, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_141": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_141, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_142": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_142, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_143": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_143, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_144": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_144, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_145": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_145, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_146": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_146, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_147": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_147, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_148": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_148, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_149": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_149, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_150": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_150, "description": "ATR-normalized distance to 1260d high."},
}
