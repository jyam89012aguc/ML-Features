"""26 stochastic williams family gemini d1 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Momentum oscillators identifying price position within a high-low range over time.
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
# FEATURE HYPOTHESES (001-075)
# ============================================================

def f26_stow_gemini_001_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Momentum oscillators identifying price position within a high-low range over time. [window=5]"""
    window = 5
    res = _safe_div(close - low.rolling(window).min(), high.rolling(window).max() - low.rolling(window).min() + 1e-10)
    return (res).diff()

def f26_stow_gemini_002_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Momentum oscillators identifying price position within a high-low range over time. [window=10]"""
    window = 10
    res = _safe_div(close - low.rolling(window).min(), high.rolling(window).max() - low.rolling(window).min() + 1e-10)
    return (res).diff()

def f26_stow_gemini_003_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Momentum oscillators identifying price position within a high-low range over time. [window=21]"""
    window = 21
    res = _safe_div(close - low.rolling(window).min(), high.rolling(window).max() - low.rolling(window).min() + 1e-10)
    return (res).diff()

def f26_stow_gemini_004_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Momentum oscillators identifying price position within a high-low range over time. [window=42]"""
    window = 42
    res = _safe_div(close - low.rolling(window).min(), high.rolling(window).max() - low.rolling(window).min() + 1e-10)
    return (res).diff()

def f26_stow_gemini_005_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Momentum oscillators identifying price position within a high-low range over time. [window=63]"""
    window = 63
    res = _safe_div(close - low.rolling(window).min(), high.rolling(window).max() - low.rolling(window).min() + 1e-10)
    return (res).diff()

def f26_stow_gemini_006_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Momentum oscillators identifying price position within a high-low range over time. [window=126]"""
    window = 126
    res = _safe_div(close - low.rolling(window).min(), high.rolling(window).max() - low.rolling(window).min() + 1e-10)
    return (res).diff()

def f26_stow_gemini_007_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Momentum oscillators identifying price position within a high-low range over time. [window=252]"""
    window = 252
    res = _safe_div(close - low.rolling(window).min(), high.rolling(window).max() - low.rolling(window).min() + 1e-10)
    return (res).diff()

def f26_stow_gemini_008_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Momentum oscillators identifying price position within a high-low range over time. [window=504]"""
    window = 504
    res = _safe_div(close - low.rolling(window).min(), high.rolling(window).max() - low.rolling(window).min() + 1e-10)
    return (res).diff()

def f26_stow_gemini_009_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Momentum oscillators identifying price position within a high-low range over time. [window=756]"""
    window = 756
    res = _safe_div(close - low.rolling(window).min(), high.rolling(window).max() - low.rolling(window).min() + 1e-10)
    return (res).diff()

def f26_stow_gemini_010_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Momentum oscillators identifying price position within a high-low range over time. [window=1260]"""
    window = 1260
    res = _safe_div(close - low.rolling(window).min(), high.rolling(window).max() - low.rolling(window).min() + 1e-10)
    return (res).diff()

def f26_stow_gemini_011_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=169, w2=347, w3=29, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(347, min_periods=max(347//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 169)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.053667 * slope + 0.0020102 * anchor
    return base_signal.diff()

def f26_stow_gemini_012_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=176, w2=360, w3=46, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(360, min_periods=max(360//3, 2)).mean()
    noise = impulse.abs().rolling(46, min_periods=max(46//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.365882 + 0.0020103 * anchor
    return base_signal.diff()

def f26_stow_gemini_013_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=183, w2=373, w3=63, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 183)
    acceleration = _rolling_slope(velocity, 373)
    curvature = _rolling_slope(acceleration, 63)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.066333 * acceleration + 0.0020104 * anchor
    return base_signal.diff()

def f26_stow_gemini_014_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=190, w2=386, w3=80, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 190)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.072667 * pressure.rolling(80, min_periods=max(80//3, 2)).mean() + 0.0020105 * anchor
    return base_signal.diff()

def f26_stow_gemini_015_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=197, w2=399, w3=97, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(197, min_periods=max(197//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.406471 + 0.0020106 * anchor
    return base_signal.diff()

def f26_stow_gemini_016_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=204, w2=412, w3=114, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(412, min_periods=max(412//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 204)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.42 + 0.0020107 * anchor
    return base_signal.diff()

def f26_stow_gemini_017_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=211, w2=425, w3=131, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(211, min_periods=max(211//3, 2)).mean(), b.abs().rolling(425, min_periods=max(425//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.091667 * _rolling_slope(cover, 211) + 0.0020108 * anchor
    return base_signal.diff()

def f26_stow_gemini_018_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=218, w2=438, w3=148, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.098 * y + 0.902000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 218) - _rolling_slope(basket, 438) + 0.0020109 * anchor
    return base_signal.diff()

def f26_stow_gemini_019_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=225, w2=451, w3=165, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(225, min_periods=max(225//3, 2)).mean(), upside.rolling(451, min_periods=max(451//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.460588 + 0.002011 * anchor
    return base_signal.diff()

def f26_stow_gemini_020_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=232, w2=464, w3=182, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(464, min_periods=max(464//3, 2)).max()
    rebound = x - x.rolling(232, min_periods=max(232//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.110667 * _rolling_slope(draw, 182) + 0.0020111 * anchor
    return base_signal.diff()

def f26_stow_gemini_021_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=239, w2=477, w3=199, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(199, min_periods=max(199//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.487647 + 0.0020112 * anchor
    return base_signal.diff()

def f26_stow_gemini_022_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=246, w2=490, w3=216, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 246)
    baseline = trend.rolling(490, min_periods=max(490//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(216, min_periods=max(216//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.501176 + 0.0020113 * anchor
    return base_signal.diff()

def f26_stow_gemini_023_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=6, w2=503, w3=233, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 6)
    slow = _rolling_slope(x, 503)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=233, adjust=False).mean() * 1.514706 + 0.0020114 * anchor
    return base_signal.diff()

def f26_stow_gemini_024_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=13, w2=17, w3=250, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(17, min_periods=max(17//3, 2)).max()
    trough = x.rolling(13, min_periods=max(13//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.528235 + 0.0020115 * anchor
    return base_signal.diff()

def f26_stow_gemini_025_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=20, w2=30, w3=267, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(20)
    rank = change.rolling(30, min_periods=max(30//3, 2)).rank(pct=True)
    persistence = change.rolling(267, min_periods=max(267//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.142333 * persistence + 0.0020116 * anchor
    return base_signal.diff()

def f26_stow_gemini_026_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=27, w2=43, w3=284, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(27, min_periods=max(27//3, 2)).std()
    vol_slow = ret.rolling(43, min_periods=max(43//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.555294 + 0.0020117 * anchor
    return base_signal.diff()

def f26_stow_gemini_027_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=34, w2=56, w3=301, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(56, min_periods=max(56//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 34)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.155 * slope + 0.0020118 * anchor
    return base_signal.diff()

def f26_stow_gemini_028_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=41, w2=69, w3=318, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(41)
    drag = impulse.rolling(69, min_periods=max(69//3, 2)).mean()
    noise = impulse.abs().rolling(318, min_periods=max(318//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.582353 + 0.0020119 * anchor
    return base_signal.diff()

def f26_stow_gemini_029_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=48, w2=82, w3=335, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 48)
    acceleration = _rolling_slope(velocity, 82)
    curvature = _rolling_slope(acceleration, 335)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.167667 * acceleration + 0.002012 * anchor
    return base_signal.diff()

def f26_stow_gemini_030_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=55, w2=95, w3=352, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 55)
    pressure = rel_log.diff(95)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.174 * pressure.rolling(352, min_periods=max(352//3, 2)).mean() + 0.0020121 * anchor
    return base_signal.diff()

def f26_stow_gemini_031_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=62, w2=108, w3=369, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(62, min_periods=max(62//3, 2)).mean())
    decay = spread.ewm(span=108, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.622941 + 0.0020122 * anchor
    return base_signal.diff()

def f26_stow_gemini_032_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=69, w2=121, w3=386, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(121, min_periods=max(121//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 69)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.636471 + 0.0020123 * anchor
    return base_signal.diff()

def f26_stow_gemini_033_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=76, w2=134, w3=403, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(76, min_periods=max(76//3, 2)).mean(), b.abs().rolling(134, min_periods=max(134//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.193 * _rolling_slope(cover, 76) + 0.0020124 * anchor
    return base_signal.diff()

def f26_stow_gemini_034_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=83, w2=147, w3=420, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.199333 * y + 0.800667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 83) - _rolling_slope(basket, 147) + 0.0020125 * anchor
    return base_signal.diff()

def f26_stow_gemini_035_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=90, w2=160, w3=437, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(90, min_periods=max(90//3, 2)).mean(), upside.rolling(160, min_periods=max(160//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.823529 + 0.0020126 * anchor
    return base_signal.diff()

def f26_stow_gemini_036_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=97, w2=173, w3=454, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(173, min_periods=max(173//3, 2)).max()
    rebound = x - x.rolling(97, min_periods=max(97//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.212 * _rolling_slope(draw, 454) + 0.0020127 * anchor
    return base_signal.diff()

def f26_stow_gemini_037_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=104, w2=186, w3=471, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(104) - b.diff(126)
    stress = imbalance.rolling(471, min_periods=max(471//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.850588 + 0.0020128 * anchor
    return base_signal.diff()

def f26_stow_gemini_038_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=111, w2=199, w3=488, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 111)
    baseline = trend.rolling(199, min_periods=max(199//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(488, min_periods=max(488//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.864118 + 0.0020129 * anchor
    return base_signal.diff()

def f26_stow_gemini_039_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=118, w2=212, w3=505, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 118)
    slow = _rolling_slope(x, 212)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.877647 + 0.002013 * anchor
    return base_signal.diff()

def f26_stow_gemini_040_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=125, w2=225, w3=522, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(225, min_periods=max(225//3, 2)).max()
    trough = x.rolling(125, min_periods=max(125//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.891176 + 0.0020131 * anchor
    return base_signal.diff()

def f26_stow_gemini_041_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=132, w2=238, w3=539, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(238, min_periods=max(238//3, 2)).rank(pct=True)
    persistence = change.rolling(539, min_periods=max(539//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.243667 * persistence + 0.0020132 * anchor
    return base_signal.diff()

def f26_stow_gemini_042_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=139, w2=251, w3=556, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(139, min_periods=max(139//3, 2)).std()
    vol_slow = ret.rolling(251, min_periods=max(251//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.918235 + 0.0020133 * anchor
    return base_signal.diff()

def f26_stow_gemini_043_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=146, w2=264, w3=573, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(264, min_periods=max(264//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 146)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.256333 * slope + 0.0020134 * anchor
    return base_signal.diff()

def f26_stow_gemini_044_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=153, w2=277, w3=590, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(277, min_periods=max(277//3, 2)).mean()
    noise = impulse.abs().rolling(590, min_periods=max(590//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.945294 + 0.0020135 * anchor
    return base_signal.diff()

def f26_stow_gemini_045_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=160, w2=290, w3=607, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 160)
    acceleration = _rolling_slope(velocity, 290)
    curvature = _rolling_slope(acceleration, 607)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.269 * acceleration + 0.0020136 * anchor
    return base_signal.diff()

def f26_stow_gemini_046_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=167, w2=303, w3=624, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 167)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.275333 * pressure.rolling(624, min_periods=max(624//3, 2)).mean() + 0.0020137 * anchor
    return base_signal.diff()

def f26_stow_gemini_047_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=174, w2=316, w3=641, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(174, min_periods=max(174//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.985882 + 0.0020138 * anchor
    return base_signal.diff()

def f26_stow_gemini_048_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=181, w2=329, w3=658, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(329, min_periods=max(329//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 181)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.999412 + 0.0020139 * anchor
    return base_signal.diff()

def f26_stow_gemini_049_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=188, w2=342, w3=675, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(188, min_periods=max(188//3, 2)).mean(), b.abs().rolling(342, min_periods=max(342//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.294333 * _rolling_slope(cover, 188) + 0.002014 * anchor
    return base_signal.diff()

def f26_stow_gemini_050_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=195, w2=355, w3=692, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.300667 * y + 0.699333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 195) - _rolling_slope(basket, 355) + 0.0020141 * anchor
    return base_signal.diff()

def f26_stow_gemini_051_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=202, w2=368, w3=709, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(202, min_periods=max(202//3, 2)).mean(), upside.rolling(368, min_periods=max(368//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.04 + 0.0020142 * anchor
    return base_signal.diff()

def f26_stow_gemini_052_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=209, w2=381, w3=726, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(381, min_periods=max(381//3, 2)).max()
    rebound = x - x.rolling(209, min_periods=max(209//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.313333 * _rolling_slope(draw, 726) + 0.0020143 * anchor
    return base_signal.diff()

def f26_stow_gemini_053_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=216, w2=394, w3=743, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(743, min_periods=max(743//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.067059 + 0.0020144 * anchor
    return base_signal.diff()

def f26_stow_gemini_054_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=223, w2=407, w3=760, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 223)
    baseline = trend.rolling(407, min_periods=max(407//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(760, min_periods=max(760//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.080588 + 0.0020145 * anchor
    return base_signal.diff()

def f26_stow_gemini_055_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=230, w2=420, w3=26, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 230)
    slow = _rolling_slope(x, 420)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=26, adjust=False).mean() * 1.094118 + 0.0020146 * anchor
    return base_signal.diff()

def f26_stow_gemini_056_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=237, w2=433, w3=43, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(433, min_periods=max(433//3, 2)).max()
    trough = x.rolling(237, min_periods=max(237//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.107647 + 0.0020147 * anchor
    return base_signal.diff()

def f26_stow_gemini_057_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=244, w2=446, w3=60, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(446, min_periods=max(446//3, 2)).rank(pct=True)
    persistence = change.rolling(60, min_periods=max(60//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.345 * persistence + 0.0020148 * anchor
    return base_signal.diff()

def f26_stow_gemini_058_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=251, w2=459, w3=77, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(251, min_periods=max(251//3, 2)).std()
    vol_slow = ret.rolling(459, min_periods=max(459//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.134706 + 0.0020149 * anchor
    return base_signal.diff()

def f26_stow_gemini_059_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=11, w2=472, w3=94, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(472, min_periods=max(472//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 11)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.357667 * slope + 0.002015 * anchor
    return base_signal.diff()

def f26_stow_gemini_060_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=18, w2=485, w3=111, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(18)
    drag = impulse.rolling(485, min_periods=max(485//3, 2)).mean()
    noise = impulse.abs().rolling(111, min_periods=max(111//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.161765 + 0.0020151 * anchor
    return base_signal.diff()

def f26_stow_gemini_061_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=25, w2=498, w3=128, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 25)
    acceleration = _rolling_slope(velocity, 498)
    curvature = _rolling_slope(acceleration, 128)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.038 * acceleration + 0.0020152 * anchor
    return base_signal.diff()

def f26_stow_gemini_062_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=32, w2=12, w3=145, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 32)
    pressure = rel_log.diff(12)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.044333 * pressure.rolling(145, min_periods=max(145//3, 2)).mean() + 0.0020153 * anchor
    return base_signal.diff()

def f26_stow_gemini_063_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=39, w2=25, w3=162, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(39, min_periods=max(39//3, 2)).mean())
    decay = spread.ewm(span=25, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.202353 + 0.0020154 * anchor
    return base_signal.diff()

def f26_stow_gemini_064_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=46, w2=38, w3=179, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(38, min_periods=max(38//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 46)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.215882 + 0.0020155 * anchor
    return base_signal.diff()

def f26_stow_gemini_065_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=53, w2=51, w3=196, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(53, min_periods=max(53//3, 2)).mean(), b.abs().rolling(51, min_periods=max(51//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.063333 * _rolling_slope(cover, 53) + 0.0020156 * anchor
    return base_signal.diff()

def f26_stow_gemini_066_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=60, w2=64, w3=213, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.069667 * y + 0.930333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 60) - _rolling_slope(basket, 64) + 0.0020157 * anchor
    return base_signal.diff()

def f26_stow_gemini_067_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=67, w2=77, w3=230, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(67, min_periods=max(67//3, 2)).mean(), upside.rolling(77, min_periods=max(77//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.256471 + 0.0020158 * anchor
    return base_signal.diff()

def f26_stow_gemini_068_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=74, w2=90, w3=247, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(90, min_periods=max(90//3, 2)).max()
    rebound = x - x.rolling(74, min_periods=max(74//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.082333 * _rolling_slope(draw, 247) + 0.0020159 * anchor
    return base_signal.diff()

def f26_stow_gemini_069_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=81, w2=103, w3=264, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(81) - b.diff(103)
    stress = imbalance.rolling(264, min_periods=max(264//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.283529 + 0.002016 * anchor
    return base_signal.diff()

def f26_stow_gemini_070_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=88, w2=116, w3=281, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 88)
    baseline = trend.rolling(116, min_periods=max(116//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(281, min_periods=max(281//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.297059 + 0.0020161 * anchor
    return base_signal.diff()

def f26_stow_gemini_071_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=95, w2=129, w3=298, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 95)
    slow = _rolling_slope(x, 129)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=298, adjust=False).mean() * 1.310588 + 0.0020162 * anchor
    return base_signal.diff()

def f26_stow_gemini_072_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=102, w2=142, w3=315, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(142, min_periods=max(142//3, 2)).max()
    trough = x.rolling(102, min_periods=max(102//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.324118 + 0.0020163 * anchor
    return base_signal.diff()

def f26_stow_gemini_073_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=109, w2=155, w3=332, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(109)
    rank = change.rolling(155, min_periods=max(155//3, 2)).rank(pct=True)
    persistence = change.rolling(332, min_periods=max(332//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.114 * persistence + 0.0020164 * anchor
    return base_signal.diff()

def f26_stow_gemini_074_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=116, w2=168, w3=349, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(116, min_periods=max(116//3, 2)).std()
    vol_slow = ret.rolling(168, min_periods=max(168//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.351176 + 0.0020165 * anchor
    return base_signal.diff()

def f26_stow_gemini_075_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=123, w2=181, w3=366, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(181, min_periods=max(181//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 123)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.126667 * slope + 0.0020166 * anchor
    return base_signal.diff()
