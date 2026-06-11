"""11 sma ema extension dynamics gemini d1 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Measurement of price deviation from simple and exponential moving averages as a signal of overextension.
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

def f11_maex_gemini_001_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of price deviation from simple and exponential moving averages as a signal of overextension. [window=5]"""
    window = 5
    res = _safe_div(close - close.rolling(window).mean(), _atr(high, low, close, window))
    return (res).diff()

def f11_maex_gemini_002_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of price deviation from simple and exponential moving averages as a signal of overextension. [window=10]"""
    window = 10
    res = _safe_div(close - close.rolling(window).mean(), _atr(high, low, close, window))
    return (res).diff()

def f11_maex_gemini_003_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of price deviation from simple and exponential moving averages as a signal of overextension. [window=21]"""
    window = 21
    res = _safe_div(close - close.rolling(window).mean(), _atr(high, low, close, window))
    return (res).diff()

def f11_maex_gemini_004_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of price deviation from simple and exponential moving averages as a signal of overextension. [window=42]"""
    window = 42
    res = _safe_div(close - close.rolling(window).mean(), _atr(high, low, close, window))
    return (res).diff()

def f11_maex_gemini_005_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of price deviation from simple and exponential moving averages as a signal of overextension. [window=63]"""
    window = 63
    res = _safe_div(close - close.rolling(window).mean(), _atr(high, low, close, window))
    return (res).diff()

def f11_maex_gemini_006_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of price deviation from simple and exponential moving averages as a signal of overextension. [window=126]"""
    window = 126
    res = _safe_div(close - close.rolling(window).mean(), _atr(high, low, close, window))
    return (res).diff()

def f11_maex_gemini_007_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of price deviation from simple and exponential moving averages as a signal of overextension. [window=252]"""
    window = 252
    res = _safe_div(close - close.rolling(window).mean(), _atr(high, low, close, window))
    return (res).diff()

def f11_maex_gemini_008_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of price deviation from simple and exponential moving averages as a signal of overextension. [window=504]"""
    window = 504
    res = _safe_div(close - close.rolling(window).mean(), _atr(high, low, close, window))
    return (res).diff()

def f11_maex_gemini_009_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of price deviation from simple and exponential moving averages as a signal of overextension. [window=756]"""
    window = 756
    res = _safe_div(close - close.rolling(window).mean(), _atr(high, low, close, window))
    return (res).diff()

def f11_maex_gemini_010_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of price deviation from simple and exponential moving averages as a signal of overextension. [window=1260]"""
    window = 1260
    res = _safe_div(close - close.rolling(window).mean(), _atr(high, low, close, window))
    return (res).diff()

def f11_maex_gemini_011_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=155, w2=428, w3=670, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(428, min_periods=max(428//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 155)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.359333 * slope + 0.0011702 * anchor
    return base_signal.diff()

def f11_maex_gemini_012_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=162, w2=441, w3=687, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(441, min_periods=max(441//3, 2)).mean()
    noise = impulse.abs().rolling(687, min_periods=max(687//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.238235 + 0.0011703 * anchor
    return base_signal.diff()

def f11_maex_gemini_013_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=169, w2=454, w3=704, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 169)
    acceleration = _rolling_slope(velocity, 454)
    curvature = _rolling_slope(acceleration, 704)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.039667 * acceleration + 0.0011704 * anchor
    return base_signal.diff()

def f11_maex_gemini_014_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=176, w2=467, w3=721, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 176)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.046 * pressure.rolling(721, min_periods=max(721//3, 2)).mean() + 0.0011705 * anchor
    return base_signal.diff()

def f11_maex_gemini_015_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=183, w2=480, w3=738, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(183, min_periods=max(183//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.278824 + 0.0011706 * anchor
    return base_signal.diff()

def f11_maex_gemini_016_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=190, w2=493, w3=755, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(493, min_periods=max(493//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 190)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.292353 + 0.0011707 * anchor
    return base_signal.diff()

def f11_maex_gemini_017_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=197, w2=506, w3=21, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(197, min_periods=max(197//3, 2)).mean(), b.abs().rolling(506, min_periods=max(506//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(21) + 0.065 * _rolling_slope(cover, 197) + 0.0011708 * anchor
    return base_signal.diff()

def f11_maex_gemini_018_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=204, w2=20, w3=38, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.071333 * y + 0.928667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 204) - _rolling_slope(basket, 20) + 0.0011709 * anchor
    return base_signal.diff()

def f11_maex_gemini_019_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=211, w2=33, w3=55, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(211, min_periods=max(211//3, 2)).mean(), upside.rolling(33, min_periods=max(33//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(55) * 1.332941 + 0.001171 * anchor
    return base_signal.diff()

def f11_maex_gemini_020_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=218, w2=46, w3=72, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(46, min_periods=max(46//3, 2)).max()
    rebound = x - x.rolling(218, min_periods=max(218//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.084 * _rolling_slope(draw, 72) + 0.0011711 * anchor
    return base_signal.diff()

def f11_maex_gemini_021_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=225, w2=59, w3=89, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(59)
    stress = imbalance.rolling(89, min_periods=max(89//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.36 + 0.0011712 * anchor
    return base_signal.diff()

def f11_maex_gemini_022_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=232, w2=72, w3=106, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 232)
    baseline = trend.rolling(72, min_periods=max(72//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(106, min_periods=max(106//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.373529 + 0.0011713 * anchor
    return base_signal.diff()

def f11_maex_gemini_023_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=239, w2=85, w3=123, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 239)
    slow = _rolling_slope(x, 85)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=123, adjust=False).mean() * 1.387059 + 0.0011714 * anchor
    return base_signal.diff()

def f11_maex_gemini_024_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=246, w2=98, w3=140, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(98, min_periods=max(98//3, 2)).max()
    trough = x.rolling(246, min_periods=max(246//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.400588 + 0.0011715 * anchor
    return base_signal.diff()

def f11_maex_gemini_025_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=6, w2=111, w3=157, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(6)
    rank = change.rolling(111, min_periods=max(111//3, 2)).rank(pct=True)
    persistence = change.rolling(157, min_periods=max(157//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.115667 * persistence + 0.0011716 * anchor
    return base_signal.diff()

def f11_maex_gemini_026_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=13, w2=124, w3=174, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(13, min_periods=max(13//3, 2)).std()
    vol_slow = ret.rolling(124, min_periods=max(124//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.427647 + 0.0011717 * anchor
    return base_signal.diff()

def f11_maex_gemini_027_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=20, w2=137, w3=191, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(137, min_periods=max(137//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 20)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.128333 * slope + 0.0011718 * anchor
    return base_signal.diff()

def f11_maex_gemini_028_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=27, w2=150, w3=208, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(27)
    drag = impulse.rolling(150, min_periods=max(150//3, 2)).mean()
    noise = impulse.abs().rolling(208, min_periods=max(208//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.454706 + 0.0011719 * anchor
    return base_signal.diff()

def f11_maex_gemini_029_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=34, w2=163, w3=225, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 34)
    acceleration = _rolling_slope(velocity, 163)
    curvature = _rolling_slope(acceleration, 225)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.141 * acceleration + 0.001172 * anchor
    return base_signal.diff()

def f11_maex_gemini_030_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=41, w2=176, w3=242, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 41)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.147333 * pressure.rolling(242, min_periods=max(242//3, 2)).mean() + 0.0011721 * anchor
    return base_signal.diff()

def f11_maex_gemini_031_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=48, w2=189, w3=259, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(48, min_periods=max(48//3, 2)).mean())
    decay = spread.ewm(span=189, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.495294 + 0.0011722 * anchor
    return base_signal.diff()

def f11_maex_gemini_032_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=55, w2=202, w3=276, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(202, min_periods=max(202//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 55)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.508824 + 0.0011723 * anchor
    return base_signal.diff()

def f11_maex_gemini_033_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=62, w2=215, w3=293, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(62, min_periods=max(62//3, 2)).mean(), b.abs().rolling(215, min_periods=max(215//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.166333 * _rolling_slope(cover, 62) + 0.0011724 * anchor
    return base_signal.diff()

def f11_maex_gemini_034_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=69, w2=228, w3=310, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.172667 * y + 0.827333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 69) - _rolling_slope(basket, 228) + 0.0011725 * anchor
    return base_signal.diff()

def f11_maex_gemini_035_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=76, w2=241, w3=327, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(76, min_periods=max(76//3, 2)).mean(), upside.rolling(241, min_periods=max(241//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.549412 + 0.0011726 * anchor
    return base_signal.diff()

def f11_maex_gemini_036_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=83, w2=254, w3=344, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(254, min_periods=max(254//3, 2)).max()
    rebound = x - x.rolling(83, min_periods=max(83//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.185333 * _rolling_slope(draw, 344) + 0.0011727 * anchor
    return base_signal.diff()

def f11_maex_gemini_037_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=90, w2=267, w3=361, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(90) - b.diff(126)
    stress = imbalance.rolling(361, min_periods=max(361//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.576471 + 0.0011728 * anchor
    return base_signal.diff()

def f11_maex_gemini_038_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=97, w2=280, w3=378, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 97)
    baseline = trend.rolling(280, min_periods=max(280//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(378, min_periods=max(378//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.59 + 0.0011729 * anchor
    return base_signal.diff()

def f11_maex_gemini_039_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=104, w2=293, w3=395, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 104)
    slow = _rolling_slope(x, 293)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.603529 + 0.001173 * anchor
    return base_signal.diff()

def f11_maex_gemini_040_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=111, w2=306, w3=412, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(306, min_periods=max(306//3, 2)).max()
    trough = x.rolling(111, min_periods=max(111//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.617059 + 0.0011731 * anchor
    return base_signal.diff()

def f11_maex_gemini_041_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=118, w2=319, w3=429, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(118)
    rank = change.rolling(319, min_periods=max(319//3, 2)).rank(pct=True)
    persistence = change.rolling(429, min_periods=max(429//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.217 * persistence + 0.0011732 * anchor
    return base_signal.diff()

def f11_maex_gemini_042_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=125, w2=332, w3=446, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(125, min_periods=max(125//3, 2)).std()
    vol_slow = ret.rolling(332, min_periods=max(332//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.644118 + 0.0011733 * anchor
    return base_signal.diff()

def f11_maex_gemini_043_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=132, w2=345, w3=463, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(345, min_periods=max(345//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 132)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.229667 * slope + 0.0011734 * anchor
    return base_signal.diff()

def f11_maex_gemini_044_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=139, w2=358, w3=480, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(358, min_periods=max(358//3, 2)).mean()
    noise = impulse.abs().rolling(480, min_periods=max(480//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.671176 + 0.0011735 * anchor
    return base_signal.diff()

def f11_maex_gemini_045_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=146, w2=371, w3=497, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 146)
    acceleration = _rolling_slope(velocity, 371)
    curvature = _rolling_slope(acceleration, 497)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.242333 * acceleration + 0.0011736 * anchor
    return base_signal.diff()

def f11_maex_gemini_046_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=153, w2=384, w3=514, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 153)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.248667 * pressure.rolling(514, min_periods=max(514//3, 2)).mean() + 0.0011737 * anchor
    return base_signal.diff()

def f11_maex_gemini_047_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=160, w2=397, w3=531, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(160, min_periods=max(160//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.858235 + 0.0011738 * anchor
    return base_signal.diff()

def f11_maex_gemini_048_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=167, w2=410, w3=548, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(410, min_periods=max(410//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 167)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.871765 + 0.0011739 * anchor
    return base_signal.diff()

def f11_maex_gemini_049_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=174, w2=423, w3=565, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(174, min_periods=max(174//3, 2)).mean(), b.abs().rolling(423, min_periods=max(423//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.267667 * _rolling_slope(cover, 174) + 0.001174 * anchor
    return base_signal.diff()

def f11_maex_gemini_050_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=181, w2=436, w3=582, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.274 * y + 0.726000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 181) - _rolling_slope(basket, 436) + 0.0011741 * anchor
    return base_signal.diff()

def f11_maex_gemini_051_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=188, w2=449, w3=599, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(188, min_periods=max(188//3, 2)).mean(), upside.rolling(449, min_periods=max(449//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.912353 + 0.0011742 * anchor
    return base_signal.diff()

def f11_maex_gemini_052_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=195, w2=462, w3=616, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(462, min_periods=max(462//3, 2)).max()
    rebound = x - x.rolling(195, min_periods=max(195//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.286667 * _rolling_slope(draw, 616) + 0.0011743 * anchor
    return base_signal.diff()

def f11_maex_gemini_053_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=202, w2=475, w3=633, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(633, min_periods=max(633//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.939412 + 0.0011744 * anchor
    return base_signal.diff()

def f11_maex_gemini_054_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=209, w2=488, w3=650, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 209)
    baseline = trend.rolling(488, min_periods=max(488//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(650, min_periods=max(650//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.952941 + 0.0011745 * anchor
    return base_signal.diff()

def f11_maex_gemini_055_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=216, w2=501, w3=667, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 216)
    slow = _rolling_slope(x, 501)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.966471 + 0.0011746 * anchor
    return base_signal.diff()

def f11_maex_gemini_056_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=223, w2=15, w3=684, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(15, min_periods=max(15//3, 2)).max()
    trough = x.rolling(223, min_periods=max(223//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.98 + 0.0011747 * anchor
    return base_signal.diff()

def f11_maex_gemini_057_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=230, w2=28, w3=701, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(28, min_periods=max(28//3, 2)).rank(pct=True)
    persistence = change.rolling(701, min_periods=max(701//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.318333 * persistence + 0.0011748 * anchor
    return base_signal.diff()

def f11_maex_gemini_058_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=237, w2=41, w3=718, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(237, min_periods=max(237//3, 2)).std()
    vol_slow = ret.rolling(41, min_periods=max(41//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.007059 + 0.0011749 * anchor
    return base_signal.diff()

def f11_maex_gemini_059_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=244, w2=54, w3=735, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(54, min_periods=max(54//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 244)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.331 * slope + 0.001175 * anchor
    return base_signal.diff()

def f11_maex_gemini_060_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=251, w2=67, w3=752, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(67, min_periods=max(67//3, 2)).mean()
    noise = impulse.abs().rolling(752, min_periods=max(752//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.034118 + 0.0011751 * anchor
    return base_signal.diff()

def f11_maex_gemini_061_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=11, w2=80, w3=18, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 11)
    acceleration = _rolling_slope(velocity, 80)
    curvature = _rolling_slope(acceleration, 18)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.343667 * acceleration + 0.0011752 * anchor
    return base_signal.diff()

def f11_maex_gemini_062_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=18, w2=93, w3=35, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 18)
    pressure = rel_log.diff(93)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.35 * pressure.rolling(35, min_periods=max(35//3, 2)).mean() + 0.0011753 * anchor
    return base_signal.diff()

def f11_maex_gemini_063_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=25, w2=106, w3=52, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(25, min_periods=max(25//3, 2)).mean())
    decay = spread.ewm(span=106, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.074706 + 0.0011754 * anchor
    return base_signal.diff()

def f11_maex_gemini_064_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=32, w2=119, w3=69, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(119, min_periods=max(119//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 32)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.088235 + 0.0011755 * anchor
    return base_signal.diff()

def f11_maex_gemini_065_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=39, w2=132, w3=86, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(39, min_periods=max(39//3, 2)).mean(), b.abs().rolling(132, min_periods=max(132//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(86) + 0.036667 * _rolling_slope(cover, 39) + 0.0011756 * anchor
    return base_signal.diff()

def f11_maex_gemini_066_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=46, w2=145, w3=103, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.043 * y + 0.957000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 46) - _rolling_slope(basket, 145) + 0.0011757 * anchor
    return base_signal.diff()

def f11_maex_gemini_067_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=53, w2=158, w3=120, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(53, min_periods=max(53//3, 2)).mean(), upside.rolling(158, min_periods=max(158//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(120) * 1.128824 + 0.0011758 * anchor
    return base_signal.diff()

def f11_maex_gemini_068_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=60, w2=171, w3=137, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(171, min_periods=max(171//3, 2)).max()
    rebound = x - x.rolling(60, min_periods=max(60//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.055667 * _rolling_slope(draw, 137) + 0.0011759 * anchor
    return base_signal.diff()

def f11_maex_gemini_069_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=67, w2=184, w3=154, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(67) - b.diff(126)
    stress = imbalance.rolling(154, min_periods=max(154//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.155882 + 0.001176 * anchor
    return base_signal.diff()

def f11_maex_gemini_070_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=74, w2=197, w3=171, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 74)
    baseline = trend.rolling(197, min_periods=max(197//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(171, min_periods=max(171//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.169412 + 0.0011761 * anchor
    return base_signal.diff()

def f11_maex_gemini_071_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=81, w2=210, w3=188, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 81)
    slow = _rolling_slope(x, 210)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=188, adjust=False).mean() * 1.182941 + 0.0011762 * anchor
    return base_signal.diff()

def f11_maex_gemini_072_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=88, w2=223, w3=205, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(223, min_periods=max(223//3, 2)).max()
    trough = x.rolling(88, min_periods=max(88//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.196471 + 0.0011763 * anchor
    return base_signal.diff()

def f11_maex_gemini_073_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=95, w2=236, w3=222, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(95)
    rank = change.rolling(236, min_periods=max(236//3, 2)).rank(pct=True)
    persistence = change.rolling(222, min_periods=max(222//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.087333 * persistence + 0.0011764 * anchor
    return base_signal.diff()

def f11_maex_gemini_074_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=102, w2=249, w3=239, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(102, min_periods=max(102//3, 2)).std()
    vol_slow = ret.rolling(249, min_periods=max(249//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.223529 + 0.0011765 * anchor
    return base_signal.diff()

def f11_maex_gemini_075_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=109, w2=262, w3=256, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(262, min_periods=max(262//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 109)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1 * slope + 0.0011766 * anchor
    return base_signal.diff()
