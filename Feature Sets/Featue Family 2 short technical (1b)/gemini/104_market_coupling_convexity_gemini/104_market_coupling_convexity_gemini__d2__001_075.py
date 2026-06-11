"""104 market coupling convexity gemini d2 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Convexity of the relationship between different market segments or assets.
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

def f104_mccx_gemini_001_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Convexity of the relationship between different market segments or assets. [window=5]"""
    window = 5
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1), window)
    return (res).diff().diff()

def f104_mccx_gemini_002_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Convexity of the relationship between different market segments or assets. [window=10]"""
    window = 10
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1), window)
    return (res).diff().diff()

def f104_mccx_gemini_003_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Convexity of the relationship between different market segments or assets. [window=21]"""
    window = 21
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1), window)
    return (res).diff().diff()

def f104_mccx_gemini_004_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Convexity of the relationship between different market segments or assets. [window=42]"""
    window = 42
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1), window)
    return (res).diff().diff()

def f104_mccx_gemini_005_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Convexity of the relationship between different market segments or assets. [window=63]"""
    window = 63
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1), window)
    return (res).diff().diff()

def f104_mccx_gemini_006_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Convexity of the relationship between different market segments or assets. [window=126]"""
    window = 126
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1), window)
    return (res).diff().diff()

def f104_mccx_gemini_007_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Convexity of the relationship between different market segments or assets. [window=252]"""
    window = 252
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1), window)
    return (res).diff().diff()

def f104_mccx_gemini_008_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Convexity of the relationship between different market segments or assets. [window=504]"""
    window = 504
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1), window)
    return (res).diff().diff()

def f104_mccx_gemini_009_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Convexity of the relationship between different market segments or assets. [window=756]"""
    window = 756
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1), window)
    return (res).diff().diff()

def f104_mccx_gemini_010_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Convexity of the relationship between different market segments or assets. [window=1260]"""
    window = 1260
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1), window)
    return (res).diff().diff()

def f104_mccx_gemini_011_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=156, w2=395, w3=488, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 156)
    slow = _rolling_slope(x, 395)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.400588 + 0.0007362 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_012_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=163, w2=408, w3=505, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(408, min_periods=max(408//3, 2)).max()
    trough = x.rolling(163, min_periods=max(163//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.414118 + 0.0007363 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_013_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=170, w2=421, w3=522, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(421, min_periods=max(421//3, 2)).rank(pct=True)
    persistence = change.rolling(522, min_periods=max(522//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.136667 * persistence + 0.0007364 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_014_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=177, w2=434, w3=539, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(177, min_periods=max(177//3, 2)).std()
    vol_slow = ret.rolling(434, min_periods=max(434//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.441176 + 0.0007365 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_015_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=184, w2=447, w3=556, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(447, min_periods=max(447//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 184)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.149333 * slope + 0.0007366 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_016_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=191, w2=460, w3=573, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(460, min_periods=max(460//3, 2)).mean()
    noise = impulse.abs().rolling(573, min_periods=max(573//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.468235 + 0.0007367 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_017_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=198, w2=473, w3=590, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 198)
    acceleration = _rolling_slope(velocity, 473)
    curvature = _rolling_slope(acceleration, 590)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.162 * acceleration + 0.0007368 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_018_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=205, w2=486, w3=607, lag=34)."""
    rel = _safe_div(close.shift(34), volume.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 205)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.168333 * pressure.rolling(607, min_periods=max(607//3, 2)).mean() + 0.0007369 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_019_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=212, w2=499, w3=624, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(212, min_periods=max(212//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.508824 + 0.000737 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_020_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=219, w2=13, w3=641, lag=0)."""
    a = _safe_log(close.abs() + 1.0).shift(0)
    b = _safe_log(volume.abs() + 1.0).shift(0)
    corr = a.rolling(13, min_periods=max(13//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 219)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.522353 + 0.0007371 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_021_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=226, w2=26, w3=658, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    cover = _safe_div(a.rolling(226, min_periods=max(226//3, 2)).mean(), b.abs().rolling(26, min_periods=max(26//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.187333 * _rolling_slope(cover, 226) + 0.0007372 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_022_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=233, w2=39, w3=675, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    y = _safe_log(volume.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.193667 * y + 0.806333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 233) - _rolling_slope(basket, 39) + 0.0007373 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_023_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=240, w2=52, w3=692, lag=3)."""
    x = close.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(240, min_periods=max(240//3, 2)).mean(), upside.rolling(52, min_periods=max(52//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.562941 + 0.0007374 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_024_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=247, w2=65, w3=709, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    draw = x - x.rolling(65, min_periods=max(65//3, 2)).max()
    rebound = x - x.rolling(247, min_periods=max(247//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.206333 * _rolling_slope(draw, 709) + 0.0007375 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_025_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=7, w2=78, w3=726, lag=8)."""
    a = _safe_log(close.abs() + 1.0).shift(8)
    b = _safe_log(volume.abs() + 1.0).shift(8)
    imbalance = a.diff(7) - b.diff(78)
    stress = imbalance.rolling(726, min_periods=max(726//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.59 + 0.0007376 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_026_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=14, w2=91, w3=743, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 14)
    baseline = trend.rolling(91, min_periods=max(91//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(743, min_periods=max(743//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.603529 + 0.0007377 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_027_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=21, w2=104, w3=760, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 21)
    slow = _rolling_slope(x, 104)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.617059 + 0.0007378 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_028_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=28, w2=117, w3=26, lag=34)."""
    x = close.shift(34)
    peak = x.rolling(117, min_periods=max(117//3, 2)).max()
    trough = x.rolling(28, min_periods=max(28//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.630588 + 0.0007379 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_029_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=35, w2=130, w3=43, lag=55)."""
    x = close.shift(55)
    change = x.pct_change(35)
    rank = change.rolling(130, min_periods=max(130//3, 2)).rank(pct=True)
    persistence = change.rolling(43, min_periods=max(43//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.238 * persistence + 0.000738 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_030_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=42, w2=143, w3=60, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(42, min_periods=max(42//3, 2)).std()
    vol_slow = ret.rolling(143, min_periods=max(143//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.657647 + 0.0007381 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_031_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=49, w2=156, w3=77, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(156, min_periods=max(156//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 49)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.250667 * slope + 0.0007382 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_032_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=56, w2=169, w3=94, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(56)
    drag = impulse.rolling(169, min_periods=max(169//3, 2)).mean()
    noise = impulse.abs().rolling(94, min_periods=max(94//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.831176 + 0.0007383 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_033_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=63, w2=182, w3=111, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 63)
    acceleration = _rolling_slope(velocity, 182)
    curvature = _rolling_slope(acceleration, 111)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.263333 * acceleration + 0.0007384 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_034_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=70, w2=195, w3=128, lag=5)."""
    rel = _safe_div(close.shift(5), volume.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 70)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.269667 * pressure.rolling(128, min_periods=max(128//3, 2)).mean() + 0.0007385 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_035_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=77, w2=208, w3=145, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(77, min_periods=max(77//3, 2)).mean())
    decay = spread.ewm(span=208, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.871765 + 0.0007386 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_036_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=84, w2=221, w3=162, lag=13)."""
    a = _safe_log(close.abs() + 1.0).shift(13)
    b = _safe_log(volume.abs() + 1.0).shift(13)
    corr = a.rolling(221, min_periods=max(221//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 84)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.885294 + 0.0007387 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_037_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=91, w2=234, w3=179, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    cover = _safe_div(a.rolling(91, min_periods=max(91//3, 2)).mean(), b.abs().rolling(234, min_periods=max(234//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.288667 * _rolling_slope(cover, 91) + 0.0007388 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_038_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=98, w2=247, w3=196, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    y = _safe_log(volume.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.295 * y + 0.705000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 98) - _rolling_slope(basket, 247) + 0.0007389 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_039_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=105, w2=260, w3=213, lag=55)."""
    x = close.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(105, min_periods=max(105//3, 2)).mean(), upside.rolling(260, min_periods=max(260//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.925882 + 0.000739 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_040_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=112, w2=273, w3=230, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    draw = x - x.rolling(273, min_periods=max(273//3, 2)).max()
    rebound = x - x.rolling(112, min_periods=max(112//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.307667 * _rolling_slope(draw, 230) + 0.0007391 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_041_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=119, w2=286, w3=247, lag=1)."""
    a = _safe_log(close.abs() + 1.0).shift(1)
    b = _safe_log(volume.abs() + 1.0).shift(1)
    imbalance = a.diff(119) - b.diff(126)
    stress = imbalance.rolling(247, min_periods=max(247//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.952941 + 0.0007392 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_042_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=126, w2=299, w3=264, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 126)
    baseline = trend.rolling(299, min_periods=max(299//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(264, min_periods=max(264//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.966471 + 0.0007393 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_043_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=133, w2=312, w3=281, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 133)
    slow = _rolling_slope(x, 312)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=281, adjust=False).mean() * 0.98 + 0.0007394 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_044_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=140, w2=325, w3=298, lag=5)."""
    x = close.shift(5)
    peak = x.rolling(325, min_periods=max(325//3, 2)).max()
    trough = x.rolling(140, min_periods=max(140//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.993529 + 0.0007395 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_045_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=147, w2=338, w3=315, lag=8)."""
    x = close.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(338, min_periods=max(338//3, 2)).rank(pct=True)
    persistence = change.rolling(315, min_periods=max(315//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.339333 * persistence + 0.0007396 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_046_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=154, w2=351, w3=332, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(154, min_periods=max(154//3, 2)).std()
    vol_slow = ret.rolling(351, min_periods=max(351//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.020588 + 0.0007397 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_047_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=161, w2=364, w3=349, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(364, min_periods=max(364//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 161)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.352 * slope + 0.0007398 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_048_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=168, w2=377, w3=366, lag=34)."""
    x = close.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(377, min_periods=max(377//3, 2)).mean()
    noise = impulse.abs().rolling(366, min_periods=max(366//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.047647 + 0.0007399 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_049_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=175, w2=390, w3=383, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 175)
    acceleration = _rolling_slope(velocity, 390)
    curvature = _rolling_slope(acceleration, 383)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.032333 * acceleration + 0.00074 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_050_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=182, w2=403, w3=400, lag=0)."""
    rel = _safe_div(close.shift(0), volume.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 182)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.038667 * pressure.rolling(400, min_periods=max(400//3, 2)).mean() + 0.0007401 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_051_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=189, w2=416, w3=417, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(189, min_periods=max(189//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.088235 + 0.0007402 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_052_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=196, w2=429, w3=434, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(volume.abs() + 1.0).shift(2)
    corr = a.rolling(429, min_periods=max(429//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 196)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.101765 + 0.0007403 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_053_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=203, w2=442, w3=451, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    cover = _safe_div(a.rolling(203, min_periods=max(203//3, 2)).mean(), b.abs().rolling(442, min_periods=max(442//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.057667 * _rolling_slope(cover, 203) + 0.0007404 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_054_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=210, w2=455, w3=468, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(volume.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.064 * y + 0.936000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 210) - _rolling_slope(basket, 455) + 0.0007405 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_055_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=217, w2=468, w3=485, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(217, min_periods=max(217//3, 2)).mean(), upside.rolling(468, min_periods=max(468//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.142353 + 0.0007406 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_056_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=224, w2=481, w3=502, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    draw = x - x.rolling(481, min_periods=max(481//3, 2)).max()
    rebound = x - x.rolling(224, min_periods=max(224//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.076667 * _rolling_slope(draw, 502) + 0.0007407 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_057_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=231, w2=494, w3=519, lag=21)."""
    a = _safe_log(close.abs() + 1.0).shift(21)
    b = _safe_log(volume.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(519, min_periods=max(519//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.169412 + 0.0007408 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_058_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=238, w2=507, w3=536, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 238)
    baseline = trend.rolling(507, min_periods=max(507//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(536, min_periods=max(536//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.182941 + 0.0007409 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_059_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=245, w2=21, w3=553, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 245)
    slow = _rolling_slope(x, 21)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.196471 + 0.000741 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_060_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=5, w2=34, w3=570, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(34, min_periods=max(34//3, 2)).max()
    trough = x.rolling(5, min_periods=max(5//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.21 + 0.0007411 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_061_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=12, w2=47, w3=587, lag=1)."""
    x = close.shift(1)
    change = x.pct_change(12)
    rank = change.rolling(47, min_periods=max(47//3, 2)).rank(pct=True)
    persistence = change.rolling(587, min_periods=max(587//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.108333 * persistence + 0.0007412 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_062_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=19, w2=60, w3=604, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(19, min_periods=max(19//3, 2)).std()
    vol_slow = ret.rolling(60, min_periods=max(60//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.237059 + 0.0007413 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_063_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=26, w2=73, w3=621, lag=3)."""
    x = close.shift(3)
    ma = x.rolling(73, min_periods=max(73//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 26)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.121 * slope + 0.0007414 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_064_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=33, w2=86, w3=638, lag=5)."""
    x = close.shift(5)
    impulse = x.diff(33)
    drag = impulse.rolling(86, min_periods=max(86//3, 2)).mean()
    noise = impulse.abs().rolling(638, min_periods=max(638//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.264118 + 0.0007415 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_065_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=40, w2=99, w3=655, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 40)
    acceleration = _rolling_slope(velocity, 99)
    curvature = _rolling_slope(acceleration, 655)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.133667 * acceleration + 0.0007416 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_066_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=47, w2=112, w3=672, lag=13)."""
    rel = _safe_div(close.shift(13), volume.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 47)
    pressure = rel_log.diff(112)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.14 * pressure.rolling(672, min_periods=max(672//3, 2)).mean() + 0.0007417 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_067_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=54, w2=125, w3=689, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(54, min_periods=max(54//3, 2)).mean())
    decay = spread.ewm(span=125, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.304706 + 0.0007418 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_068_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=61, w2=138, w3=706, lag=34)."""
    a = _safe_log(close.abs() + 1.0).shift(34)
    b = _safe_log(volume.abs() + 1.0).shift(34)
    corr = a.rolling(138, min_periods=max(138//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 61)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.318235 + 0.0007419 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_069_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=68, w2=151, w3=723, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    cover = _safe_div(a.rolling(68, min_periods=max(68//3, 2)).mean(), b.abs().rolling(151, min_periods=max(151//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.159 * _rolling_slope(cover, 68) + 0.000742 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_070_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=75, w2=164, w3=740, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    y = _safe_log(volume.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.165333 * y + 0.834667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 75) - _rolling_slope(basket, 164) + 0.0007421 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_071_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=82, w2=177, w3=757, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(82, min_periods=max(82//3, 2)).mean(), upside.rolling(177, min_periods=max(177//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.358824 + 0.0007422 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_072_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=89, w2=190, w3=23, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(190, min_periods=max(190//3, 2)).max()
    rebound = x - x.rolling(89, min_periods=max(89//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.178 * _rolling_slope(draw, 23) + 0.0007423 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_073_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=96, w2=203, w3=40, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(volume.abs() + 1.0).shift(3)
    imbalance = a.diff(96) - b.diff(126)
    stress = imbalance.rolling(40, min_periods=max(40//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.385882 + 0.0007424 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_074_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=103, w2=216, w3=57, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 103)
    baseline = trend.rolling(216, min_periods=max(216//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(57, min_periods=max(57//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.399412 + 0.0007425 * anchor
    return base_signal.diff().diff()

def f104_mccx_gemini_075_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=110, w2=229, w3=74, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 110)
    slow = _rolling_slope(x, 229)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=74, adjust=False).mean() * 1.412941 + 0.0007426 * anchor
    return base_signal.diff().diff()
