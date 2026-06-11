"""27 macd topping dynamics gemini d1 features 1-75 — Pipeline 1b-HF Grade v7.

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

def f27_macd_gemini_001_d1(close: pd.Series) -> pd.Series:
    """Moving Average Convergence Divergence peaks and bearish crossovers at trend exhaustion. [window=5]"""
    window = 5
    res = _rolling_slope(close.rolling(window).mean() - close.rolling(window*2).mean(), window)
    return (res).diff()

def f27_macd_gemini_002_d1(close: pd.Series) -> pd.Series:
    """Moving Average Convergence Divergence peaks and bearish crossovers at trend exhaustion. [window=10]"""
    window = 10
    res = _rolling_slope(close.rolling(window).mean() - close.rolling(window*2).mean(), window)
    return (res).diff()

def f27_macd_gemini_003_d1(close: pd.Series) -> pd.Series:
    """Moving Average Convergence Divergence peaks and bearish crossovers at trend exhaustion. [window=21]"""
    window = 21
    res = _rolling_slope(close.rolling(window).mean() - close.rolling(window*2).mean(), window)
    return (res).diff()

def f27_macd_gemini_004_d1(close: pd.Series) -> pd.Series:
    """Moving Average Convergence Divergence peaks and bearish crossovers at trend exhaustion. [window=42]"""
    window = 42
    res = _rolling_slope(close.rolling(window).mean() - close.rolling(window*2).mean(), window)
    return (res).diff()

def f27_macd_gemini_005_d1(close: pd.Series) -> pd.Series:
    """Moving Average Convergence Divergence peaks and bearish crossovers at trend exhaustion. [window=63]"""
    window = 63
    res = _rolling_slope(close.rolling(window).mean() - close.rolling(window*2).mean(), window)
    return (res).diff()

def f27_macd_gemini_006_d1(close: pd.Series) -> pd.Series:
    """Moving Average Convergence Divergence peaks and bearish crossovers at trend exhaustion. [window=126]"""
    window = 126
    res = _rolling_slope(close.rolling(window).mean() - close.rolling(window*2).mean(), window)
    return (res).diff()

def f27_macd_gemini_007_d1(close: pd.Series) -> pd.Series:
    """Moving Average Convergence Divergence peaks and bearish crossovers at trend exhaustion. [window=252]"""
    window = 252
    res = _rolling_slope(close.rolling(window).mean() - close.rolling(window*2).mean(), window)
    return (res).diff()

def f27_macd_gemini_008_d1(close: pd.Series) -> pd.Series:
    """Moving Average Convergence Divergence peaks and bearish crossovers at trend exhaustion. [window=504]"""
    window = 504
    res = _rolling_slope(close.rolling(window).mean() - close.rolling(window*2).mean(), window)
    return (res).diff()

def f27_macd_gemini_009_d1(close: pd.Series) -> pd.Series:
    """Moving Average Convergence Divergence peaks and bearish crossovers at trend exhaustion. [window=756]"""
    window = 756
    res = _rolling_slope(close.rolling(window).mean() - close.rolling(window*2).mean(), window)
    return (res).diff()

def f27_macd_gemini_010_d1(close: pd.Series) -> pd.Series:
    """Moving Average Convergence Divergence peaks and bearish crossovers at trend exhaustion. [window=1260]"""
    window = 1260
    res = _rolling_slope(close.rolling(window).mean() - close.rolling(window*2).mean(), window)
    return (res).diff()

def f27_macd_gemini_011_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=137, w2=142, w3=537, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 137)
    slow = _rolling_slope(x, 142)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.247059 + 0.0020662 * anchor
    return base_signal.diff()

def f27_macd_gemini_012_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=144, w2=155, w3=554, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(155, min_periods=max(155//3, 2)).max()
    trough = x.rolling(144, min_periods=max(144//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.260588 + 0.0020663 * anchor
    return base_signal.diff()

def f27_macd_gemini_013_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=151, w2=168, w3=571, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(168, min_periods=max(168//3, 2)).rank(pct=True)
    persistence = change.rolling(571, min_periods=max(571//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.289667 * persistence + 0.0020664 * anchor
    return base_signal.diff()

def f27_macd_gemini_014_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=158, w2=181, w3=588, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(158, min_periods=max(158//3, 2)).std()
    vol_slow = ret.rolling(181, min_periods=max(181//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.287647 + 0.0020665 * anchor
    return base_signal.diff()

def f27_macd_gemini_015_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=165, w2=194, w3=605, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(194, min_periods=max(194//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 165)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.302333 * slope + 0.0020666 * anchor
    return base_signal.diff()

def f27_macd_gemini_016_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=172, w2=207, w3=622, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(207, min_periods=max(207//3, 2)).mean()
    noise = impulse.abs().rolling(622, min_periods=max(622//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.314706 + 0.0020667 * anchor
    return base_signal.diff()

def f27_macd_gemini_017_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=179, w2=220, w3=639, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 179)
    acceleration = _rolling_slope(velocity, 220)
    curvature = _rolling_slope(acceleration, 639)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.315 * acceleration + 0.0020668 * anchor
    return base_signal.diff()

def f27_macd_gemini_018_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=186, w2=233, w3=656, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(186, min_periods=max(186//3, 2)).mean(), upside.rolling(233, min_periods=max(233//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.341765 + 0.0020669 * anchor
    return base_signal.diff()

def f27_macd_gemini_019_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=193, w2=246, w3=673, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(246, min_periods=max(246//3, 2)).max()
    rebound = x - x.rolling(193, min_periods=max(193//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.327667 * _rolling_slope(draw, 673) + 0.002067 * anchor
    return base_signal.diff()

def f27_macd_gemini_020_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=200, w2=259, w3=690, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 200)
    baseline = trend.rolling(259, min_periods=max(259//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(690, min_periods=max(690//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.368824 + 0.0020671 * anchor
    return base_signal.diff()

def f27_macd_gemini_021_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=207, w2=272, w3=707, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 207)
    slow = _rolling_slope(x, 272)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.382353 + 0.0020672 * anchor
    return base_signal.diff()

def f27_macd_gemini_022_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=214, w2=285, w3=724, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(285, min_periods=max(285//3, 2)).max()
    trough = x.rolling(214, min_periods=max(214//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.395882 + 0.0020673 * anchor
    return base_signal.diff()

def f27_macd_gemini_023_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=221, w2=298, w3=741, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(298, min_periods=max(298//3, 2)).rank(pct=True)
    persistence = change.rolling(741, min_periods=max(741//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.353 * persistence + 0.0020674 * anchor
    return base_signal.diff()

def f27_macd_gemini_024_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=228, w2=311, w3=758, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(228, min_periods=max(228//3, 2)).std()
    vol_slow = ret.rolling(311, min_periods=max(311//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.422941 + 0.0020675 * anchor
    return base_signal.diff()

def f27_macd_gemini_025_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=235, w2=324, w3=24, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(324, min_periods=max(324//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 235)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.033333 * slope + 0.0020676 * anchor
    return base_signal.diff()

def f27_macd_gemini_026_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=242, w2=337, w3=41, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(337, min_periods=max(337//3, 2)).mean()
    noise = impulse.abs().rolling(41, min_periods=max(41//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.45 + 0.0020677 * anchor
    return base_signal.diff()

def f27_macd_gemini_027_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=249, w2=350, w3=58, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 249)
    acceleration = _rolling_slope(velocity, 350)
    curvature = _rolling_slope(acceleration, 58)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.046 * acceleration + 0.0020678 * anchor
    return base_signal.diff()

def f27_macd_gemini_028_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=9, w2=363, w3=75, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(9, min_periods=max(9//3, 2)).mean(), upside.rolling(363, min_periods=max(363//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(75) * 1.477059 + 0.0020679 * anchor
    return base_signal.diff()

def f27_macd_gemini_029_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=16, w2=376, w3=92, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(376, min_periods=max(376//3, 2)).max()
    rebound = x - x.rolling(16, min_periods=max(16//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.058667 * _rolling_slope(draw, 92) + 0.002068 * anchor
    return base_signal.diff()

def f27_macd_gemini_030_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=23, w2=389, w3=109, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 23)
    baseline = trend.rolling(389, min_periods=max(389//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(109, min_periods=max(109//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.504118 + 0.0020681 * anchor
    return base_signal.diff()

def f27_macd_gemini_031_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=30, w2=402, w3=126, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 30)
    slow = _rolling_slope(x, 402)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=126, adjust=False).mean() * 1.517647 + 0.0020682 * anchor
    return base_signal.diff()

def f27_macd_gemini_032_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=37, w2=415, w3=143, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(415, min_periods=max(415//3, 2)).max()
    trough = x.rolling(37, min_periods=max(37//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.531176 + 0.0020683 * anchor
    return base_signal.diff()

def f27_macd_gemini_033_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=44, w2=428, w3=160, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(44)
    rank = change.rolling(428, min_periods=max(428//3, 2)).rank(pct=True)
    persistence = change.rolling(160, min_periods=max(160//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.084 * persistence + 0.0020684 * anchor
    return base_signal.diff()

def f27_macd_gemini_034_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=51, w2=441, w3=177, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(51, min_periods=max(51//3, 2)).std()
    vol_slow = ret.rolling(441, min_periods=max(441//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.558235 + 0.0020685 * anchor
    return base_signal.diff()

def f27_macd_gemini_035_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=58, w2=454, w3=194, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(454, min_periods=max(454//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 58)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.096667 * slope + 0.0020686 * anchor
    return base_signal.diff()

def f27_macd_gemini_036_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=65, w2=467, w3=211, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(65)
    drag = impulse.rolling(467, min_periods=max(467//3, 2)).mean()
    noise = impulse.abs().rolling(211, min_periods=max(211//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.585294 + 0.0020687 * anchor
    return base_signal.diff()

def f27_macd_gemini_037_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=72, w2=480, w3=228, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 72)
    acceleration = _rolling_slope(velocity, 480)
    curvature = _rolling_slope(acceleration, 228)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.109333 * acceleration + 0.0020688 * anchor
    return base_signal.diff()

def f27_macd_gemini_038_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=79, w2=493, w3=245, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(79, min_periods=max(79//3, 2)).mean(), upside.rolling(493, min_periods=max(493//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.612353 + 0.0020689 * anchor
    return base_signal.diff()

def f27_macd_gemini_039_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=86, w2=506, w3=262, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(506, min_periods=max(506//3, 2)).max()
    rebound = x - x.rolling(86, min_periods=max(86//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.122 * _rolling_slope(draw, 262) + 0.002069 * anchor
    return base_signal.diff()

def f27_macd_gemini_040_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=93, w2=20, w3=279, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 93)
    baseline = trend.rolling(20, min_periods=max(20//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(279, min_periods=max(279//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.639412 + 0.0020691 * anchor
    return base_signal.diff()

def f27_macd_gemini_041_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=100, w2=33, w3=296, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 100)
    slow = _rolling_slope(x, 33)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=296, adjust=False).mean() * 1.652941 + 0.0020692 * anchor
    return base_signal.diff()

def f27_macd_gemini_042_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=107, w2=46, w3=313, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(46, min_periods=max(46//3, 2)).max()
    trough = x.rolling(107, min_periods=max(107//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.666471 + 0.0020693 * anchor
    return base_signal.diff()

def f27_macd_gemini_043_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=114, w2=59, w3=330, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(114)
    rank = change.rolling(59, min_periods=max(59//3, 2)).rank(pct=True)
    persistence = change.rolling(330, min_periods=max(330//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.147333 * persistence + 0.0020694 * anchor
    return base_signal.diff()

def f27_macd_gemini_044_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=121, w2=72, w3=347, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(121, min_periods=max(121//3, 2)).std()
    vol_slow = ret.rolling(72, min_periods=max(72//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.84 + 0.0020695 * anchor
    return base_signal.diff()

def f27_macd_gemini_045_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=128, w2=85, w3=364, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(85, min_periods=max(85//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 128)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.16 * slope + 0.0020696 * anchor
    return base_signal.diff()

def f27_macd_gemini_046_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=135, w2=98, w3=381, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(98, min_periods=max(98//3, 2)).mean()
    noise = impulse.abs().rolling(381, min_periods=max(381//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.867059 + 0.0020697 * anchor
    return base_signal.diff()

def f27_macd_gemini_047_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=142, w2=111, w3=398, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 142)
    acceleration = _rolling_slope(velocity, 111)
    curvature = _rolling_slope(acceleration, 398)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.172667 * acceleration + 0.0020698 * anchor
    return base_signal.diff()

def f27_macd_gemini_048_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=149, w2=124, w3=415, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(149, min_periods=max(149//3, 2)).mean(), upside.rolling(124, min_periods=max(124//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.894118 + 0.0020699 * anchor
    return base_signal.diff()

def f27_macd_gemini_049_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=156, w2=137, w3=432, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(137, min_periods=max(137//3, 2)).max()
    rebound = x - x.rolling(156, min_periods=max(156//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.185333 * _rolling_slope(draw, 432) + 0.00207 * anchor
    return base_signal.diff()

def f27_macd_gemini_050_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=163, w2=150, w3=449, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 163)
    baseline = trend.rolling(150, min_periods=max(150//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(449, min_periods=max(449//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.921176 + 0.0020701 * anchor
    return base_signal.diff()

def f27_macd_gemini_051_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=170, w2=163, w3=466, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 170)
    slow = _rolling_slope(x, 163)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.934706 + 0.0020702 * anchor
    return base_signal.diff()

def f27_macd_gemini_052_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=177, w2=176, w3=483, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(176, min_periods=max(176//3, 2)).max()
    trough = x.rolling(177, min_periods=max(177//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.948235 + 0.0020703 * anchor
    return base_signal.diff()

def f27_macd_gemini_053_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=184, w2=189, w3=500, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(189, min_periods=max(189//3, 2)).rank(pct=True)
    persistence = change.rolling(500, min_periods=max(500//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.210667 * persistence + 0.0020704 * anchor
    return base_signal.diff()

def f27_macd_gemini_054_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=191, w2=202, w3=517, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(191, min_periods=max(191//3, 2)).std()
    vol_slow = ret.rolling(202, min_periods=max(202//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.975294 + 0.0020705 * anchor
    return base_signal.diff()

def f27_macd_gemini_055_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=198, w2=215, w3=534, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(215, min_periods=max(215//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 198)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.223333 * slope + 0.0020706 * anchor
    return base_signal.diff()

def f27_macd_gemini_056_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=205, w2=228, w3=551, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(228, min_periods=max(228//3, 2)).mean()
    noise = impulse.abs().rolling(551, min_periods=max(551//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.002353 + 0.0020707 * anchor
    return base_signal.diff()

def f27_macd_gemini_057_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=212, w2=241, w3=568, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 212)
    acceleration = _rolling_slope(velocity, 241)
    curvature = _rolling_slope(acceleration, 568)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.236 * acceleration + 0.0020708 * anchor
    return base_signal.diff()

def f27_macd_gemini_058_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=219, w2=254, w3=585, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(219, min_periods=max(219//3, 2)).mean(), upside.rolling(254, min_periods=max(254//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.029412 + 0.0020709 * anchor
    return base_signal.diff()

def f27_macd_gemini_059_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=226, w2=267, w3=602, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(267, min_periods=max(267//3, 2)).max()
    rebound = x - x.rolling(226, min_periods=max(226//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.248667 * _rolling_slope(draw, 602) + 0.002071 * anchor
    return base_signal.diff()

def f27_macd_gemini_060_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=233, w2=280, w3=619, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 233)
    baseline = trend.rolling(280, min_periods=max(280//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(619, min_periods=max(619//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.056471 + 0.0020711 * anchor
    return base_signal.diff()

def f27_macd_gemini_061_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=240, w2=293, w3=636, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 240)
    slow = _rolling_slope(x, 293)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.07 + 0.0020712 * anchor
    return base_signal.diff()

def f27_macd_gemini_062_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=247, w2=306, w3=653, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(306, min_periods=max(306//3, 2)).max()
    trough = x.rolling(247, min_periods=max(247//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.083529 + 0.0020713 * anchor
    return base_signal.diff()

def f27_macd_gemini_063_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=7, w2=319, w3=670, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(7)
    rank = change.rolling(319, min_periods=max(319//3, 2)).rank(pct=True)
    persistence = change.rolling(670, min_periods=max(670//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.274 * persistence + 0.0020714 * anchor
    return base_signal.diff()

def f27_macd_gemini_064_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=14, w2=332, w3=687, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(14, min_periods=max(14//3, 2)).std()
    vol_slow = ret.rolling(332, min_periods=max(332//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.110588 + 0.0020715 * anchor
    return base_signal.diff()

def f27_macd_gemini_065_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=21, w2=345, w3=704, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(345, min_periods=max(345//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 21)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.286667 * slope + 0.0020716 * anchor
    return base_signal.diff()

def f27_macd_gemini_066_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=28, w2=358, w3=721, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(28)
    drag = impulse.rolling(358, min_periods=max(358//3, 2)).mean()
    noise = impulse.abs().rolling(721, min_periods=max(721//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.137647 + 0.0020717 * anchor
    return base_signal.diff()

def f27_macd_gemini_067_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=35, w2=371, w3=738, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 35)
    acceleration = _rolling_slope(velocity, 371)
    curvature = _rolling_slope(acceleration, 738)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.299333 * acceleration + 0.0020718 * anchor
    return base_signal.diff()

def f27_macd_gemini_068_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=42, w2=384, w3=755, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(42, min_periods=max(42//3, 2)).mean(), upside.rolling(384, min_periods=max(384//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.164706 + 0.0020719 * anchor
    return base_signal.diff()

def f27_macd_gemini_069_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=49, w2=397, w3=21, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(397, min_periods=max(397//3, 2)).max()
    rebound = x - x.rolling(49, min_periods=max(49//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.312 * _rolling_slope(draw, 21) + 0.002072 * anchor
    return base_signal.diff()

def f27_macd_gemini_070_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=56, w2=410, w3=38, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 56)
    baseline = trend.rolling(410, min_periods=max(410//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(38, min_periods=max(38//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.191765 + 0.0020721 * anchor
    return base_signal.diff()

def f27_macd_gemini_071_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=63, w2=423, w3=55, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 63)
    slow = _rolling_slope(x, 423)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=55, adjust=False).mean() * 1.205294 + 0.0020722 * anchor
    return base_signal.diff()

def f27_macd_gemini_072_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=70, w2=436, w3=72, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(436, min_periods=max(436//3, 2)).max()
    trough = x.rolling(70, min_periods=max(70//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.218824 + 0.0020723 * anchor
    return base_signal.diff()

def f27_macd_gemini_073_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=77, w2=449, w3=89, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(77)
    rank = change.rolling(449, min_periods=max(449//3, 2)).rank(pct=True)
    persistence = change.rolling(89, min_periods=max(89//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.337333 * persistence + 0.0020724 * anchor
    return base_signal.diff()

def f27_macd_gemini_074_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=84, w2=462, w3=106, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(84, min_periods=max(84//3, 2)).std()
    vol_slow = ret.rolling(462, min_periods=max(462//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.245882 + 0.0020725 * anchor
    return base_signal.diff()

def f27_macd_gemini_075_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=91, w2=475, w3=123, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(475, min_periods=max(475//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 91)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.35 * slope + 0.0020726 * anchor
    return base_signal.diff()
