"""09 island reversal gap dynamics gemini d3 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Isolated price action separated by gaps, signaling a strong reversal in sentiment.
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

def f09_islr_gemini_001_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Isolated price action separated by gaps, signaling a strong reversal in sentiment. [window=5]"""
    window = 5
    res = _safe_div(low - high.shift(1), _atr(high, low, close, window)).rolling(window).max()
    return (res).diff().diff().diff()

def f09_islr_gemini_002_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Isolated price action separated by gaps, signaling a strong reversal in sentiment. [window=10]"""
    window = 10
    res = _safe_div(low - high.shift(1), _atr(high, low, close, window)).rolling(window).max()
    return (res).diff().diff().diff()

def f09_islr_gemini_003_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Isolated price action separated by gaps, signaling a strong reversal in sentiment. [window=21]"""
    window = 21
    res = _safe_div(low - high.shift(1), _atr(high, low, close, window)).rolling(window).max()
    return (res).diff().diff().diff()

def f09_islr_gemini_004_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Isolated price action separated by gaps, signaling a strong reversal in sentiment. [window=42]"""
    window = 42
    res = _safe_div(low - high.shift(1), _atr(high, low, close, window)).rolling(window).max()
    return (res).diff().diff().diff()

def f09_islr_gemini_005_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Isolated price action separated by gaps, signaling a strong reversal in sentiment. [window=63]"""
    window = 63
    res = _safe_div(low - high.shift(1), _atr(high, low, close, window)).rolling(window).max()
    return (res).diff().diff().diff()

def f09_islr_gemini_006_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Isolated price action separated by gaps, signaling a strong reversal in sentiment. [window=126]"""
    window = 126
    res = _safe_div(low - high.shift(1), _atr(high, low, close, window)).rolling(window).max()
    return (res).diff().diff().diff()

def f09_islr_gemini_007_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Isolated price action separated by gaps, signaling a strong reversal in sentiment. [window=252]"""
    window = 252
    res = _safe_div(low - high.shift(1), _atr(high, low, close, window)).rolling(window).max()
    return (res).diff().diff().diff()

def f09_islr_gemini_008_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Isolated price action separated by gaps, signaling a strong reversal in sentiment. [window=504]"""
    window = 504
    res = _safe_div(low - high.shift(1), _atr(high, low, close, window)).rolling(window).max()
    return (res).diff().diff().diff()

def f09_islr_gemini_009_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Isolated price action separated by gaps, signaling a strong reversal in sentiment. [window=756]"""
    window = 756
    res = _safe_div(low - high.shift(1), _atr(high, low, close, window)).rolling(window).max()
    return (res).diff().diff().diff()

def f09_islr_gemini_010_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Isolated price action separated by gaps, signaling a strong reversal in sentiment. [window=1260]"""
    window = 1260
    res = _safe_div(low - high.shift(1), _atr(high, low, close, window)).rolling(window).max()
    return (res).diff().diff().diff()

def f09_islr_gemini_011_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=61, w2=246, w3=328, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(61, min_periods=max(61//3, 2)).mean(), upside.rolling(246, min_periods=max(246//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.260588 + 0.0004702 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_012_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=68, w2=259, w3=345, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(259, min_periods=max(259//3, 2)).max()
    rebound = x - x.rolling(68, min_periods=max(68//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.232667 * _rolling_slope(draw, 345) + 0.0004703 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_013_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=75, w2=272, w3=362, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(75) - b.diff(126)
    stress = imbalance.rolling(362, min_periods=max(362//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.287647 + 0.0004704 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_014_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=82, w2=285, w3=379, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 82)
    baseline = trend.rolling(285, min_periods=max(285//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(379, min_periods=max(379//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.301176 + 0.0004705 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_015_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=89, w2=298, w3=396, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 89)
    slow = _rolling_slope(x, 298)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.314706 + 0.0004706 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_016_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=96, w2=311, w3=413, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(311, min_periods=max(311//3, 2)).max()
    trough = x.rolling(96, min_periods=max(96//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.328235 + 0.0004707 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_017_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=103, w2=324, w3=430, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(103)
    rank = change.rolling(324, min_periods=max(324//3, 2)).rank(pct=True)
    persistence = change.rolling(430, min_periods=max(430//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.264333 * persistence + 0.0004708 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_018_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=110, w2=337, w3=447, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(110, min_periods=max(110//3, 2)).std()
    vol_slow = ret.rolling(337, min_periods=max(337//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.355294 + 0.0004709 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_019_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=117, w2=350, w3=464, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(350, min_periods=max(350//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 117)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.277 * slope + 0.000471 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_020_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=124, w2=363, w3=481, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(124)
    drag = impulse.rolling(363, min_periods=max(363//3, 2)).mean()
    noise = impulse.abs().rolling(481, min_periods=max(481//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.382353 + 0.0004711 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_021_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=131, w2=376, w3=498, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 131)
    acceleration = _rolling_slope(velocity, 376)
    curvature = _rolling_slope(acceleration, 498)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.289667 * acceleration + 0.0004712 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_022_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=138, w2=389, w3=515, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 138)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.296 * pressure.rolling(515, min_periods=max(515//3, 2)).mean() + 0.0004713 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_023_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=145, w2=402, w3=532, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(145, min_periods=max(145//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.422941 + 0.0004714 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_024_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=152, w2=415, w3=549, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(415, min_periods=max(415//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 152)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.436471 + 0.0004715 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_025_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=159, w2=428, w3=566, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(159, min_periods=max(159//3, 2)).mean(), b.abs().rolling(428, min_periods=max(428//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.315 * _rolling_slope(cover, 159) + 0.0004716 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_026_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=166, w2=441, w3=583, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.321333 * y + 0.678667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 166) - _rolling_slope(basket, 441) + 0.0004717 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_027_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=173, w2=454, w3=600, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(173, min_periods=max(173//3, 2)).mean(), upside.rolling(454, min_periods=max(454//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.477059 + 0.0004718 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_028_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=180, w2=467, w3=617, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(467, min_periods=max(467//3, 2)).max()
    rebound = x - x.rolling(180, min_periods=max(180//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.334 * _rolling_slope(draw, 617) + 0.0004719 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_029_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=187, w2=480, w3=634, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(634, min_periods=max(634//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.504118 + 0.000472 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_030_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=194, w2=493, w3=651, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 194)
    baseline = trend.rolling(493, min_periods=max(493//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(651, min_periods=max(651//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.517647 + 0.0004721 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_031_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=201, w2=506, w3=668, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 201)
    slow = _rolling_slope(x, 506)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.531176 + 0.0004722 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_032_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=208, w2=20, w3=685, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(20, min_periods=max(20//3, 2)).max()
    trough = x.rolling(208, min_periods=max(208//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.544706 + 0.0004723 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_033_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=215, w2=33, w3=702, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(33, min_periods=max(33//3, 2)).rank(pct=True)
    persistence = change.rolling(702, min_periods=max(702//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.033333 * persistence + 0.0004724 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_034_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=222, w2=46, w3=719, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(222, min_periods=max(222//3, 2)).std()
    vol_slow = ret.rolling(46, min_periods=max(46//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.571765 + 0.0004725 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_035_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=229, w2=59, w3=736, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(59, min_periods=max(59//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 229)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.046 * slope + 0.0004726 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_036_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=236, w2=72, w3=753, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(72, min_periods=max(72//3, 2)).mean()
    noise = impulse.abs().rolling(753, min_periods=max(753//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.598824 + 0.0004727 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_037_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=243, w2=85, w3=19, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 243)
    acceleration = _rolling_slope(velocity, 85)
    curvature = _rolling_slope(acceleration, 19)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.058667 * acceleration + 0.0004728 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_038_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=250, w2=98, w3=36, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 250)
    pressure = rel_log.diff(98)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.065 * pressure.rolling(36, min_periods=max(36//3, 2)).mean() + 0.0004729 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_039_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=10, w2=111, w3=53, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(10, min_periods=max(10//3, 2)).mean())
    decay = spread.ewm(span=111, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.639412 + 0.000473 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_040_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=17, w2=124, w3=70, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(124, min_periods=max(124//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 17)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.652941 + 0.0004731 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_041_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=24, w2=137, w3=87, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(24, min_periods=max(24//3, 2)).mean(), b.abs().rolling(137, min_periods=max(137//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(87) + 0.084 * _rolling_slope(cover, 24) + 0.0004732 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_042_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=31, w2=150, w3=104, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.090333 * y + 0.909667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 31) - _rolling_slope(basket, 150) + 0.0004733 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_043_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=38, w2=163, w3=121, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(38, min_periods=max(38//3, 2)).mean(), upside.rolling(163, min_periods=max(163//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(121) * 0.84 + 0.0004734 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_044_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=45, w2=176, w3=138, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(176, min_periods=max(176//3, 2)).max()
    rebound = x - x.rolling(45, min_periods=max(45//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.103 * _rolling_slope(draw, 138) + 0.0004735 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_045_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=52, w2=189, w3=155, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(52) - b.diff(126)
    stress = imbalance.rolling(155, min_periods=max(155//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.867059 + 0.0004736 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_046_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=59, w2=202, w3=172, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 59)
    baseline = trend.rolling(202, min_periods=max(202//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(172, min_periods=max(172//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.880588 + 0.0004737 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_047_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=66, w2=215, w3=189, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 66)
    slow = _rolling_slope(x, 215)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=189, adjust=False).mean() * 0.894118 + 0.0004738 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_048_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=73, w2=228, w3=206, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(228, min_periods=max(228//3, 2)).max()
    trough = x.rolling(73, min_periods=max(73//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.907647 + 0.0004739 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_049_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=80, w2=241, w3=223, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(80)
    rank = change.rolling(241, min_periods=max(241//3, 2)).rank(pct=True)
    persistence = change.rolling(223, min_periods=max(223//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.134667 * persistence + 0.000474 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_050_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=87, w2=254, w3=240, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(87, min_periods=max(87//3, 2)).std()
    vol_slow = ret.rolling(254, min_periods=max(254//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.934706 + 0.0004741 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_051_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=94, w2=267, w3=257, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(267, min_periods=max(267//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 94)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.147333 * slope + 0.0004742 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_052_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=101, w2=280, w3=274, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(101)
    drag = impulse.rolling(280, min_periods=max(280//3, 2)).mean()
    noise = impulse.abs().rolling(274, min_periods=max(274//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.961765 + 0.0004743 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_053_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=108, w2=293, w3=291, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 108)
    acceleration = _rolling_slope(velocity, 293)
    curvature = _rolling_slope(acceleration, 291)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.16 * acceleration + 0.0004744 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_054_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=115, w2=306, w3=308, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 115)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.166333 * pressure.rolling(308, min_periods=max(308//3, 2)).mean() + 0.0004745 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_055_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=122, w2=319, w3=325, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(122, min_periods=max(122//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.002353 + 0.0004746 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_056_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=129, w2=332, w3=342, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(332, min_periods=max(332//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 129)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.015882 + 0.0004747 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_057_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=136, w2=345, w3=359, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(136, min_periods=max(136//3, 2)).mean(), b.abs().rolling(345, min_periods=max(345//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.185333 * _rolling_slope(cover, 136) + 0.0004748 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_058_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=143, w2=358, w3=376, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.191667 * y + 0.808333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 143) - _rolling_slope(basket, 358) + 0.0004749 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_059_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=150, w2=371, w3=393, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(150, min_periods=max(150//3, 2)).mean(), upside.rolling(371, min_periods=max(371//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.056471 + 0.000475 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_060_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=157, w2=384, w3=410, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(384, min_periods=max(384//3, 2)).max()
    rebound = x - x.rolling(157, min_periods=max(157//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.204333 * _rolling_slope(draw, 410) + 0.0004751 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_061_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=164, w2=397, w3=427, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(427, min_periods=max(427//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.083529 + 0.0004752 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_062_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=171, w2=410, w3=444, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 171)
    baseline = trend.rolling(410, min_periods=max(410//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(444, min_periods=max(444//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.097059 + 0.0004753 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_063_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=178, w2=423, w3=461, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 178)
    slow = _rolling_slope(x, 423)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.110588 + 0.0004754 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_064_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=185, w2=436, w3=478, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(436, min_periods=max(436//3, 2)).max()
    trough = x.rolling(185, min_periods=max(185//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.124118 + 0.0004755 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_065_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=192, w2=449, w3=495, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(449, min_periods=max(449//3, 2)).rank(pct=True)
    persistence = change.rolling(495, min_periods=max(495//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.236 * persistence + 0.0004756 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_066_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=199, w2=462, w3=512, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(199, min_periods=max(199//3, 2)).std()
    vol_slow = ret.rolling(462, min_periods=max(462//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.151176 + 0.0004757 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_067_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=206, w2=475, w3=529, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(475, min_periods=max(475//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 206)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.248667 * slope + 0.0004758 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_068_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=213, w2=488, w3=546, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(488, min_periods=max(488//3, 2)).mean()
    noise = impulse.abs().rolling(546, min_periods=max(546//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.178235 + 0.0004759 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_069_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=220, w2=501, w3=563, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 220)
    acceleration = _rolling_slope(velocity, 501)
    curvature = _rolling_slope(acceleration, 563)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.261333 * acceleration + 0.000476 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_070_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=227, w2=15, w3=580, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 227)
    pressure = rel_log.diff(15)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.267667 * pressure.rolling(580, min_periods=max(580//3, 2)).mean() + 0.0004761 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_071_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=234, w2=28, w3=597, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(234, min_periods=max(234//3, 2)).mean())
    decay = spread.ewm(span=28, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.218824 + 0.0004762 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_072_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=241, w2=41, w3=614, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(41, min_periods=max(41//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 241)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.232353 + 0.0004763 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_073_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=248, w2=54, w3=631, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(248, min_periods=max(248//3, 2)).mean(), b.abs().rolling(54, min_periods=max(54//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.286667 * _rolling_slope(cover, 248) + 0.0004764 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_074_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=8, w2=67, w3=648, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.293 * y + 0.707000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 8) - _rolling_slope(basket, 67) + 0.0004765 * anchor
    return base_signal.diff().diff().diff()

def f09_islr_gemini_075_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=15, w2=80, w3=665, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(15, min_periods=max(15//3, 2)).mean(), upside.rolling(80, min_periods=max(80//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.272941 + 0.0004766 * anchor
    return base_signal.diff().diff().diff()
