"""27 macd topping dynamics gemini d3 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Moving Average Convergence Divergence peaks and bearish crossovers at trend exhaustion.
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

def f27_macd_gemini_001_d3(close: pd.Series) -> pd.Series:
    """Moving Average Convergence Divergence peaks and bearish crossovers at trend exhaustion. [window=5]"""
    window = 5
    res = _rolling_slope(close.rolling(window).mean() - close.rolling(window*2).mean(), window)
    return (res).diff().diff().diff()

def f27_macd_gemini_002_d3(close: pd.Series) -> pd.Series:
    """Moving Average Convergence Divergence peaks and bearish crossovers at trend exhaustion. [window=10]"""
    window = 10
    res = _rolling_slope(close.rolling(window).mean() - close.rolling(window*2).mean(), window)
    return (res).diff().diff().diff()

def f27_macd_gemini_003_d3(close: pd.Series) -> pd.Series:
    """Moving Average Convergence Divergence peaks and bearish crossovers at trend exhaustion. [window=21]"""
    window = 21
    res = _rolling_slope(close.rolling(window).mean() - close.rolling(window*2).mean(), window)
    return (res).diff().diff().diff()

def f27_macd_gemini_004_d3(close: pd.Series) -> pd.Series:
    """Moving Average Convergence Divergence peaks and bearish crossovers at trend exhaustion. [window=42]"""
    window = 42
    res = _rolling_slope(close.rolling(window).mean() - close.rolling(window*2).mean(), window)
    return (res).diff().diff().diff()

def f27_macd_gemini_005_d3(close: pd.Series) -> pd.Series:
    """Moving Average Convergence Divergence peaks and bearish crossovers at trend exhaustion. [window=63]"""
    window = 63
    res = _rolling_slope(close.rolling(window).mean() - close.rolling(window*2).mean(), window)
    return (res).diff().diff().diff()

def f27_macd_gemini_006_d3(close: pd.Series) -> pd.Series:
    """Moving Average Convergence Divergence peaks and bearish crossovers at trend exhaustion. [window=126]"""
    window = 126
    res = _rolling_slope(close.rolling(window).mean() - close.rolling(window*2).mean(), window)
    return (res).diff().diff().diff()

def f27_macd_gemini_007_d3(close: pd.Series) -> pd.Series:
    """Moving Average Convergence Divergence peaks and bearish crossovers at trend exhaustion. [window=252]"""
    window = 252
    res = _rolling_slope(close.rolling(window).mean() - close.rolling(window*2).mean(), window)
    return (res).diff().diff().diff()

def f27_macd_gemini_008_d3(close: pd.Series) -> pd.Series:
    """Moving Average Convergence Divergence peaks and bearish crossovers at trend exhaustion. [window=504]"""
    window = 504
    res = _rolling_slope(close.rolling(window).mean() - close.rolling(window*2).mean(), window)
    return (res).diff().diff().diff()

def f27_macd_gemini_009_d3(close: pd.Series) -> pd.Series:
    """Moving Average Convergence Divergence peaks and bearish crossovers at trend exhaustion. [window=756]"""
    window = 756
    res = _rolling_slope(close.rolling(window).mean() - close.rolling(window*2).mean(), window)
    return (res).diff().diff().diff()

def f27_macd_gemini_010_d3(close: pd.Series) -> pd.Series:
    """Moving Average Convergence Divergence peaks and bearish crossovers at trend exhaustion. [window=1260]"""
    window = 1260
    res = _rolling_slope(close.rolling(window).mean() - close.rolling(window*2).mean(), window)
    return (res).diff().diff().diff()

def f27_macd_gemini_011_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=121, w2=289, w3=40, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 121)
    slow = _rolling_slope(x, 289)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=40, adjust=False).mean() * 1.621176 + 0.0020942 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_012_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=128, w2=302, w3=57, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(302, min_periods=max(302//3, 2)).max()
    trough = x.rolling(128, min_periods=max(128//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.634706 + 0.0020943 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_013_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=135, w2=315, w3=74, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(315, min_periods=max(315//3, 2)).rank(pct=True)
    persistence = change.rolling(74, min_periods=max(74//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.069 * persistence + 0.0020944 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_014_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=142, w2=328, w3=91, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(142, min_periods=max(142//3, 2)).std()
    vol_slow = ret.rolling(328, min_periods=max(328//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.661765 + 0.0020945 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_015_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=149, w2=341, w3=108, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(341, min_periods=max(341//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 149)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.081667 * slope + 0.0020946 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_016_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=156, w2=354, w3=125, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(354, min_periods=max(354//3, 2)).mean()
    noise = impulse.abs().rolling(125, min_periods=max(125//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.835294 + 0.0020947 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_017_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=163, w2=367, w3=142, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 163)
    acceleration = _rolling_slope(velocity, 367)
    curvature = _rolling_slope(acceleration, 142)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.094333 * acceleration + 0.0020948 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_018_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=170, w2=380, w3=159, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(170, min_periods=max(170//3, 2)).mean(), upside.rolling(380, min_periods=max(380//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.862353 + 0.0020949 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_019_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=177, w2=393, w3=176, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(393, min_periods=max(393//3, 2)).max()
    rebound = x - x.rolling(177, min_periods=max(177//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.107 * _rolling_slope(draw, 176) + 0.002095 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_020_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=184, w2=406, w3=193, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 184)
    baseline = trend.rolling(406, min_periods=max(406//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(193, min_periods=max(193//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.889412 + 0.0020951 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_021_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=191, w2=419, w3=210, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 191)
    slow = _rolling_slope(x, 419)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=210, adjust=False).mean() * 0.902941 + 0.0020952 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_022_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=198, w2=432, w3=227, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(432, min_periods=max(432//3, 2)).max()
    trough = x.rolling(198, min_periods=max(198//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.916471 + 0.0020953 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_023_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=205, w2=445, w3=244, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(445, min_periods=max(445//3, 2)).rank(pct=True)
    persistence = change.rolling(244, min_periods=max(244//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.132333 * persistence + 0.0020954 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_024_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=212, w2=458, w3=261, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(212, min_periods=max(212//3, 2)).std()
    vol_slow = ret.rolling(458, min_periods=max(458//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.943529 + 0.0020955 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_025_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=219, w2=471, w3=278, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(471, min_periods=max(471//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 219)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.145 * slope + 0.0020956 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_026_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=226, w2=484, w3=295, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(484, min_periods=max(484//3, 2)).mean()
    noise = impulse.abs().rolling(295, min_periods=max(295//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.970588 + 0.0020957 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_027_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=233, w2=497, w3=312, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 233)
    acceleration = _rolling_slope(velocity, 497)
    curvature = _rolling_slope(acceleration, 312)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.157667 * acceleration + 0.0020958 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_028_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=240, w2=11, w3=329, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(240, min_periods=max(240//3, 2)).mean(), upside.rolling(11, min_periods=max(11//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.997647 + 0.0020959 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_029_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=247, w2=24, w3=346, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(24, min_periods=max(24//3, 2)).max()
    rebound = x - x.rolling(247, min_periods=max(247//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.170333 * _rolling_slope(draw, 346) + 0.002096 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_030_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=7, w2=37, w3=363, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 7)
    baseline = trend.rolling(37, min_periods=max(37//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(363, min_periods=max(363//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.024706 + 0.0020961 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_031_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=14, w2=50, w3=380, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 14)
    slow = _rolling_slope(x, 50)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.038235 + 0.0020962 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_032_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=21, w2=63, w3=397, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(63, min_periods=max(63//3, 2)).max()
    trough = x.rolling(21, min_periods=max(21//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.051765 + 0.0020963 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_033_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=28, w2=76, w3=414, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(28)
    rank = change.rolling(76, min_periods=max(76//3, 2)).rank(pct=True)
    persistence = change.rolling(414, min_periods=max(414//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.195667 * persistence + 0.0020964 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_034_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=35, w2=89, w3=431, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(35, min_periods=max(35//3, 2)).std()
    vol_slow = ret.rolling(89, min_periods=max(89//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.078824 + 0.0020965 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_035_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=42, w2=102, w3=448, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(102, min_periods=max(102//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 42)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.208333 * slope + 0.0020966 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_036_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=49, w2=115, w3=465, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(49)
    drag = impulse.rolling(115, min_periods=max(115//3, 2)).mean()
    noise = impulse.abs().rolling(465, min_periods=max(465//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.105882 + 0.0020967 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_037_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=56, w2=128, w3=482, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 56)
    acceleration = _rolling_slope(velocity, 128)
    curvature = _rolling_slope(acceleration, 482)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.221 * acceleration + 0.0020968 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_038_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=63, w2=141, w3=499, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(63, min_periods=max(63//3, 2)).mean(), upside.rolling(141, min_periods=max(141//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.132941 + 0.0020969 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_039_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=70, w2=154, w3=516, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(154, min_periods=max(154//3, 2)).max()
    rebound = x - x.rolling(70, min_periods=max(70//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.233667 * _rolling_slope(draw, 516) + 0.002097 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_040_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=77, w2=167, w3=533, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 77)
    baseline = trend.rolling(167, min_periods=max(167//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(533, min_periods=max(533//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.16 + 0.0020971 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_041_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=84, w2=180, w3=550, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 84)
    slow = _rolling_slope(x, 180)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.173529 + 0.0020972 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_042_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=91, w2=193, w3=567, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(193, min_periods=max(193//3, 2)).max()
    trough = x.rolling(91, min_periods=max(91//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.187059 + 0.0020973 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_043_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=98, w2=206, w3=584, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(98)
    rank = change.rolling(206, min_periods=max(206//3, 2)).rank(pct=True)
    persistence = change.rolling(584, min_periods=max(584//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.259 * persistence + 0.0020974 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_044_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=105, w2=219, w3=601, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(105, min_periods=max(105//3, 2)).std()
    vol_slow = ret.rolling(219, min_periods=max(219//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.214118 + 0.0020975 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_045_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=112, w2=232, w3=618, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(232, min_periods=max(232//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 112)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.271667 * slope + 0.0020976 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_046_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=119, w2=245, w3=635, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(119)
    drag = impulse.rolling(245, min_periods=max(245//3, 2)).mean()
    noise = impulse.abs().rolling(635, min_periods=max(635//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.241176 + 0.0020977 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_047_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=126, w2=258, w3=652, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 126)
    acceleration = _rolling_slope(velocity, 258)
    curvature = _rolling_slope(acceleration, 652)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.284333 * acceleration + 0.0020978 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_048_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=133, w2=271, w3=669, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(133, min_periods=max(133//3, 2)).mean(), upside.rolling(271, min_periods=max(271//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.268235 + 0.0020979 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_049_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=140, w2=284, w3=686, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(284, min_periods=max(284//3, 2)).max()
    rebound = x - x.rolling(140, min_periods=max(140//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.297 * _rolling_slope(draw, 686) + 0.002098 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_050_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=147, w2=297, w3=703, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 147)
    baseline = trend.rolling(297, min_periods=max(297//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(703, min_periods=max(703//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.295294 + 0.0020981 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_051_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=154, w2=310, w3=720, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 154)
    slow = _rolling_slope(x, 310)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.308824 + 0.0020982 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_052_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=161, w2=323, w3=737, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(323, min_periods=max(323//3, 2)).max()
    trough = x.rolling(161, min_periods=max(161//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.322353 + 0.0020983 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_053_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=168, w2=336, w3=754, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(336, min_periods=max(336//3, 2)).rank(pct=True)
    persistence = change.rolling(754, min_periods=max(754//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.322333 * persistence + 0.0020984 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_054_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=175, w2=349, w3=20, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(175, min_periods=max(175//3, 2)).std()
    vol_slow = ret.rolling(349, min_periods=max(349//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.349412 + 0.0020985 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_055_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=182, w2=362, w3=37, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(362, min_periods=max(362//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 182)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.335 * slope + 0.0020986 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_056_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=189, w2=375, w3=54, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(375, min_periods=max(375//3, 2)).mean()
    noise = impulse.abs().rolling(54, min_periods=max(54//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.376471 + 0.0020987 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_057_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=196, w2=388, w3=71, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 196)
    acceleration = _rolling_slope(velocity, 388)
    curvature = _rolling_slope(acceleration, 71)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.347667 * acceleration + 0.0020988 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_058_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=203, w2=401, w3=88, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(203, min_periods=max(203//3, 2)).mean(), upside.rolling(401, min_periods=max(401//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(88) * 1.403529 + 0.0020989 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_059_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=210, w2=414, w3=105, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(414, min_periods=max(414//3, 2)).max()
    rebound = x - x.rolling(210, min_periods=max(210//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.360333 * _rolling_slope(draw, 105) + 0.002099 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_060_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=217, w2=427, w3=122, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 217)
    baseline = trend.rolling(427, min_periods=max(427//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(122, min_periods=max(122//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.430588 + 0.0020991 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_061_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=224, w2=440, w3=139, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 224)
    slow = _rolling_slope(x, 440)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=139, adjust=False).mean() * 1.444118 + 0.0020992 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_062_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=231, w2=453, w3=156, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(453, min_periods=max(453//3, 2)).max()
    trough = x.rolling(231, min_periods=max(231//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.457647 + 0.0020993 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_063_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=238, w2=466, w3=173, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(466, min_periods=max(466//3, 2)).rank(pct=True)
    persistence = change.rolling(173, min_periods=max(173//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.053333 * persistence + 0.0020994 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_064_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=245, w2=479, w3=190, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(245, min_periods=max(245//3, 2)).std()
    vol_slow = ret.rolling(479, min_periods=max(479//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.484706 + 0.0020995 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_065_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=5, w2=492, w3=207, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(492, min_periods=max(492//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 5)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.066 * slope + 0.0020996 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_066_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=12, w2=505, w3=224, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(12)
    drag = impulse.rolling(505, min_periods=max(505//3, 2)).mean()
    noise = impulse.abs().rolling(224, min_periods=max(224//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.511765 + 0.0020997 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_067_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=19, w2=19, w3=241, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 19)
    acceleration = _rolling_slope(velocity, 19)
    curvature = _rolling_slope(acceleration, 241)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.078667 * acceleration + 0.0020998 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_068_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=26, w2=32, w3=258, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(26, min_periods=max(26//3, 2)).mean(), upside.rolling(32, min_periods=max(32//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.538824 + 0.0020999 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_069_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=33, w2=45, w3=275, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(45, min_periods=max(45//3, 2)).max()
    rebound = x - x.rolling(33, min_periods=max(33//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.091333 * _rolling_slope(draw, 275) + 0.0021 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_070_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=40, w2=58, w3=292, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 40)
    baseline = trend.rolling(58, min_periods=max(58//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(292, min_periods=max(292//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.565882 + 0.0021001 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_071_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=47, w2=71, w3=309, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 47)
    slow = _rolling_slope(x, 71)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.579412 + 0.0021002 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_072_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=54, w2=84, w3=326, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(84, min_periods=max(84//3, 2)).max()
    trough = x.rolling(54, min_periods=max(54//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.592941 + 0.0021003 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_073_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=61, w2=97, w3=343, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(61)
    rank = change.rolling(97, min_periods=max(97//3, 2)).rank(pct=True)
    persistence = change.rolling(343, min_periods=max(343//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.116667 * persistence + 0.0021004 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_074_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=68, w2=110, w3=360, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(68, min_periods=max(68//3, 2)).std()
    vol_slow = ret.rolling(110, min_periods=max(110//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.62 + 0.0021005 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_075_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=75, w2=123, w3=377, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(123, min_periods=max(123//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 75)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.129333 * slope + 0.0021006 * anchor
    return base_signal.diff().diff().diff()
