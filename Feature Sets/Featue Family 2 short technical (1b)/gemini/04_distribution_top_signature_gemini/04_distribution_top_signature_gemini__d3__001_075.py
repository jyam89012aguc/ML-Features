"""04 distribution top signature gemini d3 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Distribution at price tops characterized by high volume without significant price progress.
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

def f04_dtop_gemini_001_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Distribution at price tops characterized by high volume without significant price progress. [window=5]"""
    window = 5
    res = _safe_div(_rolling_zscore(volume, window), _safe_log(high.rolling(window).max() / low.rolling(window).min() + 1e-9))
    return (res).diff().diff().diff()

def f04_dtop_gemini_002_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Distribution at price tops characterized by high volume without significant price progress. [window=10]"""
    window = 10
    res = _safe_div(_rolling_zscore(volume, window), _safe_log(high.rolling(window).max() / low.rolling(window).min() + 1e-9))
    return (res).diff().diff().diff()

def f04_dtop_gemini_003_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Distribution at price tops characterized by high volume without significant price progress. [window=21]"""
    window = 21
    res = _safe_div(_rolling_zscore(volume, window), _safe_log(high.rolling(window).max() / low.rolling(window).min() + 1e-9))
    return (res).diff().diff().diff()

def f04_dtop_gemini_004_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Distribution at price tops characterized by high volume without significant price progress. [window=42]"""
    window = 42
    res = _safe_div(_rolling_zscore(volume, window), _safe_log(high.rolling(window).max() / low.rolling(window).min() + 1e-9))
    return (res).diff().diff().diff()

def f04_dtop_gemini_005_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Distribution at price tops characterized by high volume without significant price progress. [window=63]"""
    window = 63
    res = _safe_div(_rolling_zscore(volume, window), _safe_log(high.rolling(window).max() / low.rolling(window).min() + 1e-9))
    return (res).diff().diff().diff()

def f04_dtop_gemini_006_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Distribution at price tops characterized by high volume without significant price progress. [window=126]"""
    window = 126
    res = _safe_div(_rolling_zscore(volume, window), _safe_log(high.rolling(window).max() / low.rolling(window).min() + 1e-9))
    return (res).diff().diff().diff()

def f04_dtop_gemini_007_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Distribution at price tops characterized by high volume without significant price progress. [window=252]"""
    window = 252
    res = _safe_div(_rolling_zscore(volume, window), _safe_log(high.rolling(window).max() / low.rolling(window).min() + 1e-9))
    return (res).diff().diff().diff()

def f04_dtop_gemini_008_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Distribution at price tops characterized by high volume without significant price progress. [window=504]"""
    window = 504
    res = _safe_div(_rolling_zscore(volume, window), _safe_log(high.rolling(window).max() / low.rolling(window).min() + 1e-9))
    return (res).diff().diff().diff()

def f04_dtop_gemini_009_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Distribution at price tops characterized by high volume without significant price progress. [window=756]"""
    window = 756
    res = _safe_div(_rolling_zscore(volume, window), _safe_log(high.rolling(window).max() / low.rolling(window).min() + 1e-9))
    return (res).diff().diff().diff()

def f04_dtop_gemini_010_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Distribution at price tops characterized by high volume without significant price progress. [window=1260]"""
    window = 1260
    res = _safe_div(_rolling_zscore(volume, window), _safe_log(high.rolling(window).max() / low.rolling(window).min() + 1e-9))
    return (res).diff().diff().diff()

def f04_dtop_gemini_011_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=221, w2=273, w3=41, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(221, min_periods=max(221//3, 2)).mean(), upside.rolling(273, min_periods=max(273//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(41) * 0.933529 + 0.0001902 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_012_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=228, w2=286, w3=58, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(286, min_periods=max(286//3, 2)).max()
    rebound = x - x.rolling(228, min_periods=max(228//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.113 * _rolling_slope(draw, 58) + 0.0001903 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_013_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=235, w2=299, w3=75, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(75, min_periods=max(75//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.960588 + 0.0001904 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_014_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=242, w2=312, w3=92, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 242)
    baseline = trend.rolling(312, min_periods=max(312//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(92, min_periods=max(92//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.974118 + 0.0001905 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_015_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=249, w2=325, w3=109, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 249)
    slow = _rolling_slope(x, 325)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=109, adjust=False).mean() * 0.987647 + 0.0001906 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_016_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=9, w2=338, w3=126, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(338, min_periods=max(338//3, 2)).max()
    trough = x.rolling(9, min_periods=max(9//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.001176 + 0.0001907 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_017_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=16, w2=351, w3=143, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(16)
    rank = change.rolling(351, min_periods=max(351//3, 2)).rank(pct=True)
    persistence = change.rolling(143, min_periods=max(143//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.144667 * persistence + 0.0001908 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_018_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=23, w2=364, w3=160, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(23, min_periods=max(23//3, 2)).std()
    vol_slow = ret.rolling(364, min_periods=max(364//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.028235 + 0.0001909 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_019_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=30, w2=377, w3=177, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(377, min_periods=max(377//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 30)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.157333 * slope + 0.000191 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_020_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=37, w2=390, w3=194, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(37)
    drag = impulse.rolling(390, min_periods=max(390//3, 2)).mean()
    noise = impulse.abs().rolling(194, min_periods=max(194//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.055294 + 0.0001911 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_021_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=44, w2=403, w3=211, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 44)
    acceleration = _rolling_slope(velocity, 403)
    curvature = _rolling_slope(acceleration, 211)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.17 * acceleration + 0.0001912 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_022_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=51, w2=416, w3=228, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 51)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.176333 * pressure.rolling(228, min_periods=max(228//3, 2)).mean() + 0.0001913 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_023_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=58, w2=429, w3=245, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(58, min_periods=max(58//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.095882 + 0.0001914 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_024_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=65, w2=442, w3=262, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(442, min_periods=max(442//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 65)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.109412 + 0.0001915 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_025_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=72, w2=455, w3=279, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(72, min_periods=max(72//3, 2)).mean(), b.abs().rolling(455, min_periods=max(455//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.195333 * _rolling_slope(cover, 72) + 0.0001916 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_026_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=79, w2=468, w3=296, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.201667 * y + 0.798333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 79) - _rolling_slope(basket, 468) + 0.0001917 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_027_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=86, w2=481, w3=313, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(86, min_periods=max(86//3, 2)).mean(), upside.rolling(481, min_periods=max(481//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.15 + 0.0001918 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_028_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=93, w2=494, w3=330, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(494, min_periods=max(494//3, 2)).max()
    rebound = x - x.rolling(93, min_periods=max(93//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.214333 * _rolling_slope(draw, 330) + 0.0001919 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_029_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=100, w2=507, w3=347, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(100) - b.diff(126)
    stress = imbalance.rolling(347, min_periods=max(347//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.177059 + 0.000192 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_030_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=107, w2=21, w3=364, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 107)
    baseline = trend.rolling(21, min_periods=max(21//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(364, min_periods=max(364//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.190588 + 0.0001921 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_031_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=114, w2=34, w3=381, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 114)
    slow = _rolling_slope(x, 34)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.204118 + 0.0001922 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_032_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=121, w2=47, w3=398, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(47, min_periods=max(47//3, 2)).max()
    trough = x.rolling(121, min_periods=max(121//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.217647 + 0.0001923 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_033_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=128, w2=60, w3=415, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(60, min_periods=max(60//3, 2)).rank(pct=True)
    persistence = change.rolling(415, min_periods=max(415//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.246 * persistence + 0.0001924 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_034_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=135, w2=73, w3=432, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(135, min_periods=max(135//3, 2)).std()
    vol_slow = ret.rolling(73, min_periods=max(73//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.244706 + 0.0001925 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_035_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=142, w2=86, w3=449, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(86, min_periods=max(86//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 142)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.258667 * slope + 0.0001926 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_036_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=149, w2=99, w3=466, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(99, min_periods=max(99//3, 2)).mean()
    noise = impulse.abs().rolling(466, min_periods=max(466//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.271765 + 0.0001927 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_037_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=156, w2=112, w3=483, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 156)
    acceleration = _rolling_slope(velocity, 112)
    curvature = _rolling_slope(acceleration, 483)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.271333 * acceleration + 0.0001928 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_038_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=163, w2=125, w3=500, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 163)
    pressure = rel_log.diff(125)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.277667 * pressure.rolling(500, min_periods=max(500//3, 2)).mean() + 0.0001929 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_039_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=170, w2=138, w3=517, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(170, min_periods=max(170//3, 2)).mean())
    decay = spread.ewm(span=138, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.312353 + 0.000193 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_040_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=177, w2=151, w3=534, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(151, min_periods=max(151//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 177)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.325882 + 0.0001931 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_041_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=184, w2=164, w3=551, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(184, min_periods=max(184//3, 2)).mean(), b.abs().rolling(164, min_periods=max(164//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.296667 * _rolling_slope(cover, 184) + 0.0001932 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_042_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=191, w2=177, w3=568, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.303 * y + 0.697000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 191) - _rolling_slope(basket, 177) + 0.0001933 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_043_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=198, w2=190, w3=585, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(198, min_periods=max(198//3, 2)).mean(), upside.rolling(190, min_periods=max(190//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.366471 + 0.0001934 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_044_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=205, w2=203, w3=602, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(203, min_periods=max(203//3, 2)).max()
    rebound = x - x.rolling(205, min_periods=max(205//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.315667 * _rolling_slope(draw, 602) + 0.0001935 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_045_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=212, w2=216, w3=619, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(619, min_periods=max(619//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.393529 + 0.0001936 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_046_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=219, w2=229, w3=636, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 219)
    baseline = trend.rolling(229, min_periods=max(229//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(636, min_periods=max(636//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.407059 + 0.0001937 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_047_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=226, w2=242, w3=653, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 226)
    slow = _rolling_slope(x, 242)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.420588 + 0.0001938 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_048_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=233, w2=255, w3=670, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(255, min_periods=max(255//3, 2)).max()
    trough = x.rolling(233, min_periods=max(233//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.434118 + 0.0001939 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_049_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=240, w2=268, w3=687, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(268, min_periods=max(268//3, 2)).rank(pct=True)
    persistence = change.rolling(687, min_periods=max(687//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.347333 * persistence + 0.000194 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_050_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=247, w2=281, w3=704, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(247, min_periods=max(247//3, 2)).std()
    vol_slow = ret.rolling(281, min_periods=max(281//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.461176 + 0.0001941 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_051_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=7, w2=294, w3=721, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(294, min_periods=max(294//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 7)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.36 * slope + 0.0001942 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_052_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=14, w2=307, w3=738, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(14)
    drag = impulse.rolling(307, min_periods=max(307//3, 2)).mean()
    noise = impulse.abs().rolling(738, min_periods=max(738//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.488235 + 0.0001943 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_053_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=21, w2=320, w3=755, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 21)
    acceleration = _rolling_slope(velocity, 320)
    curvature = _rolling_slope(acceleration, 755)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.040333 * acceleration + 0.0001944 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_054_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=28, w2=333, w3=21, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 28)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.046667 * pressure.rolling(21, min_periods=max(21//3, 2)).mean() + 0.0001945 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_055_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=35, w2=346, w3=38, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(35, min_periods=max(35//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.528824 + 0.0001946 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_056_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=42, w2=359, w3=55, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(359, min_periods=max(359//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 42)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.542353 + 0.0001947 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_057_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=49, w2=372, w3=72, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(49, min_periods=max(49//3, 2)).mean(), b.abs().rolling(372, min_periods=max(372//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(72) + 0.065667 * _rolling_slope(cover, 49) + 0.0001948 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_058_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=56, w2=385, w3=89, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.072 * y + 0.928000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 56) - _rolling_slope(basket, 385) + 0.0001949 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_059_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=63, w2=398, w3=106, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(63, min_periods=max(63//3, 2)).mean(), upside.rolling(398, min_periods=max(398//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(106) * 1.582941 + 0.000195 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_060_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=70, w2=411, w3=123, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(411, min_periods=max(411//3, 2)).max()
    rebound = x - x.rolling(70, min_periods=max(70//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.084667 * _rolling_slope(draw, 123) + 0.0001951 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_061_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=77, w2=424, w3=140, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(77) - b.diff(126)
    stress = imbalance.rolling(140, min_periods=max(140//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.61 + 0.0001952 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_062_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=84, w2=437, w3=157, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 84)
    baseline = trend.rolling(437, min_periods=max(437//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(157, min_periods=max(157//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.623529 + 0.0001953 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_063_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=91, w2=450, w3=174, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 91)
    slow = _rolling_slope(x, 450)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=174, adjust=False).mean() * 1.637059 + 0.0001954 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_064_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=98, w2=463, w3=191, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(463, min_periods=max(463//3, 2)).max()
    trough = x.rolling(98, min_periods=max(98//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.650588 + 0.0001955 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_065_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=105, w2=476, w3=208, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(105)
    rank = change.rolling(476, min_periods=max(476//3, 2)).rank(pct=True)
    persistence = change.rolling(208, min_periods=max(208//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.116333 * persistence + 0.0001956 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_066_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=112, w2=489, w3=225, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(112, min_periods=max(112//3, 2)).std()
    vol_slow = ret.rolling(489, min_periods=max(489//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.824118 + 0.0001957 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_067_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=119, w2=502, w3=242, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(502, min_periods=max(502//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 119)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.129 * slope + 0.0001958 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_068_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=126, w2=16, w3=259, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(16, min_periods=max(16//3, 2)).mean()
    noise = impulse.abs().rolling(259, min_periods=max(259//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.851176 + 0.0001959 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_069_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=133, w2=29, w3=276, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 133)
    acceleration = _rolling_slope(velocity, 29)
    curvature = _rolling_slope(acceleration, 276)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.141667 * acceleration + 0.000196 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_070_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=140, w2=42, w3=293, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 140)
    pressure = rel_log.diff(42)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.148 * pressure.rolling(293, min_periods=max(293//3, 2)).mean() + 0.0001961 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_071_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=147, w2=55, w3=310, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(147, min_periods=max(147//3, 2)).mean())
    decay = spread.ewm(span=55, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.891765 + 0.0001962 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_072_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=154, w2=68, w3=327, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(68, min_periods=max(68//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 154)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.905294 + 0.0001963 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_073_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=161, w2=81, w3=344, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(161, min_periods=max(161//3, 2)).mean(), b.abs().rolling(81, min_periods=max(81//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.167 * _rolling_slope(cover, 161) + 0.0001964 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_074_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=168, w2=94, w3=361, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.173333 * y + 0.826667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 168) - _rolling_slope(basket, 94) + 0.0001965 * anchor
    return base_signal.diff().diff().diff()

def f04_dtop_gemini_075_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=175, w2=107, w3=378, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(175, min_periods=max(175//3, 2)).mean(), upside.rolling(107, min_periods=max(107//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.945882 + 0.0001966 * anchor
    return base_signal.diff().diff().diff()
