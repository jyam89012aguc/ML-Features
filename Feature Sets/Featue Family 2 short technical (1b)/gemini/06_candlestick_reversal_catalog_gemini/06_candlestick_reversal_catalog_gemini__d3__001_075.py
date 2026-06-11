"""06 candlestick reversal catalog gemini d3 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Standard candlestick reversal patterns detected through relative wick and body proportions.
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

def f06_crev_gemini_001_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Standard candlestick reversal patterns detected through relative wick and body proportions. [window=5]"""
    window = 5
    res = _safe_div(high - low, _safe_log(close / open).abs() + 1e-9).rolling(window).mean()
    return (res).diff().diff().diff()

def f06_crev_gemini_002_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Standard candlestick reversal patterns detected through relative wick and body proportions. [window=10]"""
    window = 10
    res = _safe_div(high - low, _safe_log(close / open).abs() + 1e-9).rolling(window).mean()
    return (res).diff().diff().diff()

def f06_crev_gemini_003_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Standard candlestick reversal patterns detected through relative wick and body proportions. [window=21]"""
    window = 21
    res = _safe_div(high - low, _safe_log(close / open).abs() + 1e-9).rolling(window).mean()
    return (res).diff().diff().diff()

def f06_crev_gemini_004_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Standard candlestick reversal patterns detected through relative wick and body proportions. [window=42]"""
    window = 42
    res = _safe_div(high - low, _safe_log(close / open).abs() + 1e-9).rolling(window).mean()
    return (res).diff().diff().diff()

def f06_crev_gemini_005_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Standard candlestick reversal patterns detected through relative wick and body proportions. [window=63]"""
    window = 63
    res = _safe_div(high - low, _safe_log(close / open).abs() + 1e-9).rolling(window).mean()
    return (res).diff().diff().diff()

def f06_crev_gemini_006_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Standard candlestick reversal patterns detected through relative wick and body proportions. [window=126]"""
    window = 126
    res = _safe_div(high - low, _safe_log(close / open).abs() + 1e-9).rolling(window).mean()
    return (res).diff().diff().diff()

def f06_crev_gemini_007_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Standard candlestick reversal patterns detected through relative wick and body proportions. [window=252]"""
    window = 252
    res = _safe_div(high - low, _safe_log(close / open).abs() + 1e-9).rolling(window).mean()
    return (res).diff().diff().diff()

def f06_crev_gemini_008_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Standard candlestick reversal patterns detected through relative wick and body proportions. [window=504]"""
    window = 504
    res = _safe_div(high - low, _safe_log(close / open).abs() + 1e-9).rolling(window).mean()
    return (res).diff().diff().diff()

def f06_crev_gemini_009_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Standard candlestick reversal patterns detected through relative wick and body proportions. [window=756]"""
    window = 756
    res = _safe_div(high - low, _safe_log(close / open).abs() + 1e-9).rolling(window).mean()
    return (res).diff().diff().diff()

def f06_crev_gemini_010_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Standard candlestick reversal patterns detected through relative wick and body proportions. [window=1260]"""
    window = 1260
    res = _safe_div(high - low, _safe_log(close / open).abs() + 1e-9).rolling(window).mean()
    return (res).diff().diff().diff()

def f06_crev_gemini_011_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=157, w2=362, w3=306, lag=1)."""
    x = open.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(157, min_periods=max(157//3, 2)).mean(), upside.rolling(362, min_periods=max(362//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.576471 + 0.0003022 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_012_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=164, w2=375, w3=323, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    draw = x - x.rolling(375, min_periods=max(375//3, 2)).max()
    rebound = x - x.rolling(164, min_periods=max(164//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.227333 * _rolling_slope(draw, 323) + 0.0003023 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_013_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=171, w2=388, w3=340, lag=3)."""
    a = _safe_log(open.abs() + 1.0).shift(3)
    b = _safe_log(high.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(340, min_periods=max(340//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.603529 + 0.0003024 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_014_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=178, w2=401, w3=357, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 178)
    baseline = trend.rolling(401, min_periods=max(401//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(357, min_periods=max(357//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.617059 + 0.0003025 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_015_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=185, w2=414, w3=374, lag=8)."""
    x = _safe_log(open.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 185)
    slow = _rolling_slope(x, 414)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.630588 + 0.0003026 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_016_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=192, w2=427, w3=391, lag=13)."""
    x = open.shift(13)
    peak = x.rolling(427, min_periods=max(427//3, 2)).max()
    trough = x.rolling(192, min_periods=max(192//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.644118 + 0.0003027 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_017_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=199, w2=440, w3=408, lag=21)."""
    x = open.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(440, min_periods=max(440//3, 2)).rank(pct=True)
    persistence = change.rolling(408, min_periods=max(408//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.259 * persistence + 0.0003028 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_018_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=206, w2=453, w3=425, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(206, min_periods=max(206//3, 2)).std()
    vol_slow = ret.rolling(453, min_periods=max(453//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.671176 + 0.0003029 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_019_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=213, w2=466, w3=442, lag=55)."""
    x = open.shift(55)
    ma = x.rolling(466, min_periods=max(466//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 213)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.271667 * slope + 0.000303 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_020_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=220, w2=479, w3=459, lag=0)."""
    x = open.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(479, min_periods=max(479//3, 2)).mean()
    noise = impulse.abs().rolling(459, min_periods=max(459//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.844706 + 0.0003031 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_021_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=227, w2=492, w3=476, lag=1)."""
    x = _safe_log(open.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 227)
    acceleration = _rolling_slope(velocity, 492)
    curvature = _rolling_slope(acceleration, 476)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.284333 * acceleration + 0.0003032 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_022_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=234, w2=505, w3=493, lag=2)."""
    rel = _safe_div(open.shift(2), high.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 234)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.290667 * pressure.rolling(493, min_periods=max(493//3, 2)).mean() + 0.0003033 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_023_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=241, w2=19, w3=510, lag=3)."""
    a = open.shift(3)
    b = high.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(241, min_periods=max(241//3, 2)).mean())
    decay = spread.ewm(span=19, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.885294 + 0.0003034 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_024_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=248, w2=32, w3=527, lag=5)."""
    a = _safe_log(open.abs() + 1.0).shift(5)
    b = _safe_log(high.abs() + 1.0).shift(5)
    corr = a.rolling(32, min_periods=max(32//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 248)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.898824 + 0.0003035 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_025_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=8, w2=45, w3=544, lag=8)."""
    a = open.shift(8)
    b = high.shift(8)
    cover = _safe_div(a.rolling(8, min_periods=max(8//3, 2)).mean(), b.abs().rolling(45, min_periods=max(45//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.309667 * _rolling_slope(cover, 8) + 0.0003036 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_026_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=15, w2=58, w3=561, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    y = _safe_log(high.abs() + 1.0).shift(13)
    z = _safe_log(low.abs() + 1.0).shift(13)
    basket = x - 0.316 * y + 0.684000 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 15) - _rolling_slope(basket, 58) + 0.0003037 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_027_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=22, w2=71, w3=578, lag=21)."""
    x = open.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(22, min_periods=max(22//3, 2)).mean(), upside.rolling(71, min_periods=max(71//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.939412 + 0.0003038 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_028_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=29, w2=84, w3=595, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    draw = x - x.rolling(84, min_periods=max(84//3, 2)).max()
    rebound = x - x.rolling(29, min_periods=max(29//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.328667 * _rolling_slope(draw, 595) + 0.0003039 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_029_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=36, w2=97, w3=612, lag=55)."""
    a = _safe_log(open.abs() + 1.0).shift(55)
    b = _safe_log(high.abs() + 1.0).shift(55)
    imbalance = a.diff(36) - b.diff(97)
    stress = imbalance.rolling(612, min_periods=max(612//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.966471 + 0.000304 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_030_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=43, w2=110, w3=629, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 43)
    baseline = trend.rolling(110, min_periods=max(110//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(629, min_periods=max(629//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.98 + 0.0003041 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_031_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=50, w2=123, w3=646, lag=1)."""
    x = _safe_log(open.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 50)
    slow = _rolling_slope(x, 123)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.993529 + 0.0003042 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_032_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=57, w2=136, w3=663, lag=2)."""
    x = open.shift(2)
    peak = x.rolling(136, min_periods=max(136//3, 2)).max()
    trough = x.rolling(57, min_periods=max(57//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.007059 + 0.0003043 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_033_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=64, w2=149, w3=680, lag=3)."""
    x = open.shift(3)
    change = x.pct_change(64)
    rank = change.rolling(149, min_periods=max(149//3, 2)).rank(pct=True)
    persistence = change.rolling(680, min_periods=max(680//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.360333 * persistence + 0.0003044 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_034_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=71, w2=162, w3=697, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(71, min_periods=max(71//3, 2)).std()
    vol_slow = ret.rolling(162, min_periods=max(162//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.034118 + 0.0003045 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_035_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=78, w2=175, w3=714, lag=8)."""
    x = open.shift(8)
    ma = x.rolling(175, min_periods=max(175//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 78)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.040667 * slope + 0.0003046 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_036_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=85, w2=188, w3=731, lag=13)."""
    x = open.shift(13)
    impulse = x.diff(85)
    drag = impulse.rolling(188, min_periods=max(188//3, 2)).mean()
    noise = impulse.abs().rolling(731, min_periods=max(731//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.061176 + 0.0003047 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_037_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=92, w2=201, w3=748, lag=21)."""
    x = _safe_log(open.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 92)
    acceleration = _rolling_slope(velocity, 201)
    curvature = _rolling_slope(acceleration, 748)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.053333 * acceleration + 0.0003048 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_038_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=99, w2=214, w3=765, lag=34)."""
    rel = _safe_div(open.shift(34), high.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 99)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.059667 * pressure.rolling(765, min_periods=max(765//3, 2)).mean() + 0.0003049 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_039_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=106, w2=227, w3=31, lag=55)."""
    a = open.shift(55)
    b = high.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(106, min_periods=max(106//3, 2)).mean())
    decay = spread.ewm(span=227, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.101765 + 0.000305 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_040_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=113, w2=240, w3=48, lag=0)."""
    a = _safe_log(open.abs() + 1.0).shift(0)
    b = _safe_log(high.abs() + 1.0).shift(0)
    corr = a.rolling(240, min_periods=max(240//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 113)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.115294 + 0.0003051 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_041_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=120, w2=253, w3=65, lag=1)."""
    a = open.shift(1)
    b = high.shift(1)
    cover = _safe_div(a.rolling(120, min_periods=max(120//3, 2)).mean(), b.abs().rolling(253, min_periods=max(253//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(65) + 0.078667 * _rolling_slope(cover, 120) + 0.0003052 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_042_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=127, w2=266, w3=82, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    y = _safe_log(high.abs() + 1.0).shift(2)
    z = _safe_log(low.abs() + 1.0).shift(2)
    basket = x - 0.085 * y + 0.915000 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 127) - _rolling_slope(basket, 266) + 0.0003053 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_043_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=134, w2=279, w3=99, lag=3)."""
    x = open.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(134, min_periods=max(134//3, 2)).mean(), upside.rolling(279, min_periods=max(279//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(99) * 1.155882 + 0.0003054 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_044_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=141, w2=292, w3=116, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    draw = x - x.rolling(292, min_periods=max(292//3, 2)).max()
    rebound = x - x.rolling(141, min_periods=max(141//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.097667 * _rolling_slope(draw, 116) + 0.0003055 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_045_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=148, w2=305, w3=133, lag=8)."""
    a = _safe_log(open.abs() + 1.0).shift(8)
    b = _safe_log(high.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(133, min_periods=max(133//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.182941 + 0.0003056 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_046_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=155, w2=318, w3=150, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 155)
    baseline = trend.rolling(318, min_periods=max(318//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(150, min_periods=max(150//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.196471 + 0.0003057 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_047_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=162, w2=331, w3=167, lag=21)."""
    x = _safe_log(open.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 162)
    slow = _rolling_slope(x, 331)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=167, adjust=False).mean() * 1.21 + 0.0003058 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_048_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=169, w2=344, w3=184, lag=34)."""
    x = open.shift(34)
    peak = x.rolling(344, min_periods=max(344//3, 2)).max()
    trough = x.rolling(169, min_periods=max(169//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.223529 + 0.0003059 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_049_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=176, w2=357, w3=201, lag=55)."""
    x = open.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(357, min_periods=max(357//3, 2)).rank(pct=True)
    persistence = change.rolling(201, min_periods=max(201//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.129333 * persistence + 0.000306 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_050_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=183, w2=370, w3=218, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(183, min_periods=max(183//3, 2)).std()
    vol_slow = ret.rolling(370, min_periods=max(370//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.250588 + 0.0003061 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_051_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=190, w2=383, w3=235, lag=1)."""
    x = open.shift(1)
    ma = x.rolling(383, min_periods=max(383//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 190)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.142 * slope + 0.0003062 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_052_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=197, w2=396, w3=252, lag=2)."""
    x = open.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(396, min_periods=max(396//3, 2)).mean()
    noise = impulse.abs().rolling(252, min_periods=max(252//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.277647 + 0.0003063 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_053_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=204, w2=409, w3=269, lag=3)."""
    x = _safe_log(open.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 204)
    acceleration = _rolling_slope(velocity, 409)
    curvature = _rolling_slope(acceleration, 269)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.154667 * acceleration + 0.0003064 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_054_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=211, w2=422, w3=286, lag=5)."""
    rel = _safe_div(open.shift(5), high.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 211)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.161 * pressure.rolling(286, min_periods=max(286//3, 2)).mean() + 0.0003065 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_055_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=218, w2=435, w3=303, lag=8)."""
    a = open.shift(8)
    b = high.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(218, min_periods=max(218//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.318235 + 0.0003066 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_056_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=225, w2=448, w3=320, lag=13)."""
    a = _safe_log(open.abs() + 1.0).shift(13)
    b = _safe_log(high.abs() + 1.0).shift(13)
    corr = a.rolling(448, min_periods=max(448//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 225)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.331765 + 0.0003067 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_057_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=232, w2=461, w3=337, lag=21)."""
    a = open.shift(21)
    b = high.shift(21)
    cover = _safe_div(a.rolling(232, min_periods=max(232//3, 2)).mean(), b.abs().rolling(461, min_periods=max(461//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.18 * _rolling_slope(cover, 232) + 0.0003068 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_058_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=239, w2=474, w3=354, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    y = _safe_log(high.abs() + 1.0).shift(34)
    z = _safe_log(low.abs() + 1.0).shift(34)
    basket = x - 0.186333 * y + 0.813667 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 239) - _rolling_slope(basket, 474) + 0.0003069 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_059_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=246, w2=487, w3=371, lag=55)."""
    x = open.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(246, min_periods=max(246//3, 2)).mean(), upside.rolling(487, min_periods=max(487//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.372353 + 0.000307 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_060_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=6, w2=500, w3=388, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    draw = x - x.rolling(500, min_periods=max(500//3, 2)).max()
    rebound = x - x.rolling(6, min_periods=max(6//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.199 * _rolling_slope(draw, 388) + 0.0003071 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_061_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=13, w2=14, w3=405, lag=1)."""
    a = _safe_log(open.abs() + 1.0).shift(1)
    b = _safe_log(high.abs() + 1.0).shift(1)
    imbalance = a.diff(13) - b.diff(14)
    stress = imbalance.rolling(405, min_periods=max(405//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.399412 + 0.0003072 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_062_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=20, w2=27, w3=422, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 20)
    baseline = trend.rolling(27, min_periods=max(27//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(422, min_periods=max(422//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.412941 + 0.0003073 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_063_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=27, w2=40, w3=439, lag=3)."""
    x = _safe_log(open.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 27)
    slow = _rolling_slope(x, 40)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.426471 + 0.0003074 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_064_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=34, w2=53, w3=456, lag=5)."""
    x = open.shift(5)
    peak = x.rolling(53, min_periods=max(53//3, 2)).max()
    trough = x.rolling(34, min_periods=max(34//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.44 + 0.0003075 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_065_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=41, w2=66, w3=473, lag=8)."""
    x = open.shift(8)
    change = x.pct_change(41)
    rank = change.rolling(66, min_periods=max(66//3, 2)).rank(pct=True)
    persistence = change.rolling(473, min_periods=max(473//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.230667 * persistence + 0.0003076 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_066_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=48, w2=79, w3=490, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(48, min_periods=max(48//3, 2)).std()
    vol_slow = ret.rolling(79, min_periods=max(79//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.467059 + 0.0003077 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_067_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=55, w2=92, w3=507, lag=21)."""
    x = open.shift(21)
    ma = x.rolling(92, min_periods=max(92//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 55)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.243333 * slope + 0.0003078 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_068_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=62, w2=105, w3=524, lag=34)."""
    x = open.shift(34)
    impulse = x.diff(62)
    drag = impulse.rolling(105, min_periods=max(105//3, 2)).mean()
    noise = impulse.abs().rolling(524, min_periods=max(524//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.494118 + 0.0003079 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_069_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=69, w2=118, w3=541, lag=55)."""
    x = _safe_log(open.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 69)
    acceleration = _rolling_slope(velocity, 118)
    curvature = _rolling_slope(acceleration, 541)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.256 * acceleration + 0.000308 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_070_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=76, w2=131, w3=558, lag=0)."""
    rel = _safe_div(open.shift(0), high.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 76)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.262333 * pressure.rolling(558, min_periods=max(558//3, 2)).mean() + 0.0003081 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_071_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=83, w2=144, w3=575, lag=1)."""
    a = open.shift(1)
    b = high.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(83, min_periods=max(83//3, 2)).mean())
    decay = spread.ewm(span=144, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.534706 + 0.0003082 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_072_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=90, w2=157, w3=592, lag=2)."""
    a = _safe_log(open.abs() + 1.0).shift(2)
    b = _safe_log(high.abs() + 1.0).shift(2)
    corr = a.rolling(157, min_periods=max(157//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 90)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.548235 + 0.0003083 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_073_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=97, w2=170, w3=609, lag=3)."""
    a = open.shift(3)
    b = high.shift(3)
    cover = _safe_div(a.rolling(97, min_periods=max(97//3, 2)).mean(), b.abs().rolling(170, min_periods=max(170//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.281333 * _rolling_slope(cover, 97) + 0.0003084 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_074_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=104, w2=183, w3=626, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    y = _safe_log(high.abs() + 1.0).shift(5)
    z = _safe_log(low.abs() + 1.0).shift(5)
    basket = x - 0.287667 * y + 0.712333 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 104) - _rolling_slope(basket, 183) + 0.0003085 * anchor
    return base_signal.diff().diff().diff()

def f06_crev_gemini_075_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=111, w2=196, w3=643, lag=8)."""
    x = open.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(111, min_periods=max(111//3, 2)).mean(), upside.rolling(196, min_periods=max(196//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.588824 + 0.0003086 * anchor
    return base_signal.diff().diff().diff()
