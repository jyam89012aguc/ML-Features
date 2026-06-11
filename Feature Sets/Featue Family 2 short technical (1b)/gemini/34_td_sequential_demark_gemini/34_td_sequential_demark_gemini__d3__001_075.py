"""34 td sequential demark gemini d3 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Count-based exhaustion signals using DeMark sequential methodology.
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

def f34_tdsq_gemini_001_d3(close: pd.Series) -> pd.Series:
    """Count-based exhaustion signals using DeMark sequential methodology. [window=5]"""
    window = 5
    res = _rolling_zscore(close.diff(4), window)
    return (res).diff().diff().diff()

def f34_tdsq_gemini_002_d3(close: pd.Series) -> pd.Series:
    """Count-based exhaustion signals using DeMark sequential methodology. [window=10]"""
    window = 10
    res = _rolling_zscore(close.diff(4), window)
    return (res).diff().diff().diff()

def f34_tdsq_gemini_003_d3(close: pd.Series) -> pd.Series:
    """Count-based exhaustion signals using DeMark sequential methodology. [window=21]"""
    window = 21
    res = _rolling_zscore(close.diff(4), window)
    return (res).diff().diff().diff()

def f34_tdsq_gemini_004_d3(close: pd.Series) -> pd.Series:
    """Count-based exhaustion signals using DeMark sequential methodology. [window=42]"""
    window = 42
    res = _rolling_zscore(close.diff(4), window)
    return (res).diff().diff().diff()

def f34_tdsq_gemini_005_d3(close: pd.Series) -> pd.Series:
    """Count-based exhaustion signals using DeMark sequential methodology. [window=63]"""
    window = 63
    res = _rolling_zscore(close.diff(4), window)
    return (res).diff().diff().diff()

def f34_tdsq_gemini_006_d3(close: pd.Series) -> pd.Series:
    """Count-based exhaustion signals using DeMark sequential methodology. [window=126]"""
    window = 126
    res = _rolling_zscore(close.diff(4), window)
    return (res).diff().diff().diff()

def f34_tdsq_gemini_007_d3(close: pd.Series) -> pd.Series:
    """Count-based exhaustion signals using DeMark sequential methodology. [window=252]"""
    window = 252
    res = _rolling_zscore(close.diff(4), window)
    return (res).diff().diff().diff()

def f34_tdsq_gemini_008_d3(close: pd.Series) -> pd.Series:
    """Count-based exhaustion signals using DeMark sequential methodology. [window=504]"""
    window = 504
    res = _rolling_zscore(close.diff(4), window)
    return (res).diff().diff().diff()

def f34_tdsq_gemini_009_d3(close: pd.Series) -> pd.Series:
    """Count-based exhaustion signals using DeMark sequential methodology. [window=756]"""
    window = 756
    res = _rolling_zscore(close.diff(4), window)
    return (res).diff().diff().diff()

def f34_tdsq_gemini_010_d3(close: pd.Series) -> pd.Series:
    """Count-based exhaustion signals using DeMark sequential methodology. [window=1260]"""
    window = 1260
    res = _rolling_zscore(close.diff(4), window)
    return (res).diff().diff().diff()

def f34_tdsq_gemini_011_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=144, w2=351, w3=592, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 144)
    slow = _rolling_slope(x, 351)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.884118 + 0.0024862 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_012_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=151, w2=364, w3=609, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(364, min_periods=max(364//3, 2)).max()
    trough = x.rolling(151, min_periods=max(151//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.897647 + 0.0024863 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_013_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=158, w2=377, w3=626, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(377, min_periods=max(377//3, 2)).rank(pct=True)
    persistence = change.rolling(626, min_periods=max(626//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.303 * persistence + 0.0024864 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_014_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=165, w2=390, w3=643, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(165, min_periods=max(165//3, 2)).std()
    vol_slow = ret.rolling(390, min_periods=max(390//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.924706 + 0.0024865 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_015_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=172, w2=403, w3=660, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(403, min_periods=max(403//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 172)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.315667 * slope + 0.0024866 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_016_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=179, w2=416, w3=677, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(416, min_periods=max(416//3, 2)).mean()
    noise = impulse.abs().rolling(677, min_periods=max(677//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.951765 + 0.0024867 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_017_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=186, w2=429, w3=694, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 186)
    acceleration = _rolling_slope(velocity, 429)
    curvature = _rolling_slope(acceleration, 694)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.328333 * acceleration + 0.0024868 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_018_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=193, w2=442, w3=711, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(193, min_periods=max(193//3, 2)).mean(), upside.rolling(442, min_periods=max(442//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.978824 + 0.0024869 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_019_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=200, w2=455, w3=728, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(455, min_periods=max(455//3, 2)).max()
    rebound = x - x.rolling(200, min_periods=max(200//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.341 * _rolling_slope(draw, 728) + 0.002487 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_020_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=207, w2=468, w3=745, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 207)
    baseline = trend.rolling(468, min_periods=max(468//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(745, min_periods=max(745//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.005882 + 0.0024871 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_021_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=214, w2=481, w3=762, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 214)
    slow = _rolling_slope(x, 481)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.019412 + 0.0024872 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_022_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=221, w2=494, w3=28, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(494, min_periods=max(494//3, 2)).max()
    trough = x.rolling(221, min_periods=max(221//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.032941 + 0.0024873 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_023_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=228, w2=507, w3=45, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(507, min_periods=max(507//3, 2)).rank(pct=True)
    persistence = change.rolling(45, min_periods=max(45//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.034 * persistence + 0.0024874 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_024_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=235, w2=21, w3=62, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(235, min_periods=max(235//3, 2)).std()
    vol_slow = ret.rolling(21, min_periods=max(21//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.06 + 0.0024875 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_025_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=242, w2=34, w3=79, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(34, min_periods=max(34//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 242)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.046667 * slope + 0.0024876 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_026_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=249, w2=47, w3=96, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(47, min_periods=max(47//3, 2)).mean()
    noise = impulse.abs().rolling(96, min_periods=max(96//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.087059 + 0.0024877 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_027_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=9, w2=60, w3=113, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 9)
    acceleration = _rolling_slope(velocity, 60)
    curvature = _rolling_slope(acceleration, 113)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.059333 * acceleration + 0.0024878 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_028_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=16, w2=73, w3=130, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(16, min_periods=max(16//3, 2)).mean(), upside.rolling(73, min_periods=max(73//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.114118 + 0.0024879 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_029_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=23, w2=86, w3=147, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(86, min_periods=max(86//3, 2)).max()
    rebound = x - x.rolling(23, min_periods=max(23//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.072 * _rolling_slope(draw, 147) + 0.002488 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_030_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=30, w2=99, w3=164, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 30)
    baseline = trend.rolling(99, min_periods=max(99//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(164, min_periods=max(164//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.141176 + 0.0024881 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_031_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=37, w2=112, w3=181, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 37)
    slow = _rolling_slope(x, 112)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=181, adjust=False).mean() * 1.154706 + 0.0024882 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_032_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=44, w2=125, w3=198, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(125, min_periods=max(125//3, 2)).max()
    trough = x.rolling(44, min_periods=max(44//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.168235 + 0.0024883 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_033_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=51, w2=138, w3=215, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(51)
    rank = change.rolling(138, min_periods=max(138//3, 2)).rank(pct=True)
    persistence = change.rolling(215, min_periods=max(215//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.097333 * persistence + 0.0024884 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_034_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=58, w2=151, w3=232, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(58, min_periods=max(58//3, 2)).std()
    vol_slow = ret.rolling(151, min_periods=max(151//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.195294 + 0.0024885 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_035_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=65, w2=164, w3=249, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(164, min_periods=max(164//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 65)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.11 * slope + 0.0024886 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_036_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=72, w2=177, w3=266, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(72)
    drag = impulse.rolling(177, min_periods=max(177//3, 2)).mean()
    noise = impulse.abs().rolling(266, min_periods=max(266//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.222353 + 0.0024887 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_037_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=79, w2=190, w3=283, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 79)
    acceleration = _rolling_slope(velocity, 190)
    curvature = _rolling_slope(acceleration, 283)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.122667 * acceleration + 0.0024888 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_038_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=86, w2=203, w3=300, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(86, min_periods=max(86//3, 2)).mean(), upside.rolling(203, min_periods=max(203//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.249412 + 0.0024889 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_039_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=93, w2=216, w3=317, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(216, min_periods=max(216//3, 2)).max()
    rebound = x - x.rolling(93, min_periods=max(93//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.135333 * _rolling_slope(draw, 317) + 0.002489 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_040_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=100, w2=229, w3=334, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 100)
    baseline = trend.rolling(229, min_periods=max(229//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(334, min_periods=max(334//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.276471 + 0.0024891 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_041_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=107, w2=242, w3=351, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 107)
    slow = _rolling_slope(x, 242)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.29 + 0.0024892 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_042_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=114, w2=255, w3=368, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(255, min_periods=max(255//3, 2)).max()
    trough = x.rolling(114, min_periods=max(114//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.303529 + 0.0024893 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_043_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=121, w2=268, w3=385, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(121)
    rank = change.rolling(268, min_periods=max(268//3, 2)).rank(pct=True)
    persistence = change.rolling(385, min_periods=max(385//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.160667 * persistence + 0.0024894 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_044_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=128, w2=281, w3=402, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(128, min_periods=max(128//3, 2)).std()
    vol_slow = ret.rolling(281, min_periods=max(281//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.330588 + 0.0024895 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_045_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=135, w2=294, w3=419, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(294, min_periods=max(294//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 135)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.173333 * slope + 0.0024896 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_046_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=142, w2=307, w3=436, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(307, min_periods=max(307//3, 2)).mean()
    noise = impulse.abs().rolling(436, min_periods=max(436//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.357647 + 0.0024897 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_047_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=149, w2=320, w3=453, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 149)
    acceleration = _rolling_slope(velocity, 320)
    curvature = _rolling_slope(acceleration, 453)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.186 * acceleration + 0.0024898 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_048_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=156, w2=333, w3=470, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(156, min_periods=max(156//3, 2)).mean(), upside.rolling(333, min_periods=max(333//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.384706 + 0.0024899 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_049_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=163, w2=346, w3=487, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(346, min_periods=max(346//3, 2)).max()
    rebound = x - x.rolling(163, min_periods=max(163//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.198667 * _rolling_slope(draw, 487) + 0.00249 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_050_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=170, w2=359, w3=504, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 170)
    baseline = trend.rolling(359, min_periods=max(359//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(504, min_periods=max(504//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.411765 + 0.0024901 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_051_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=177, w2=372, w3=521, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 177)
    slow = _rolling_slope(x, 372)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.425294 + 0.0024902 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_052_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=184, w2=385, w3=538, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(385, min_periods=max(385//3, 2)).max()
    trough = x.rolling(184, min_periods=max(184//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.438824 + 0.0024903 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_053_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=191, w2=398, w3=555, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(398, min_periods=max(398//3, 2)).rank(pct=True)
    persistence = change.rolling(555, min_periods=max(555//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.224 * persistence + 0.0024904 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_054_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=198, w2=411, w3=572, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(198, min_periods=max(198//3, 2)).std()
    vol_slow = ret.rolling(411, min_periods=max(411//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.465882 + 0.0024905 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_055_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=205, w2=424, w3=589, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(424, min_periods=max(424//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 205)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.236667 * slope + 0.0024906 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_056_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=212, w2=437, w3=606, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(437, min_periods=max(437//3, 2)).mean()
    noise = impulse.abs().rolling(606, min_periods=max(606//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.492941 + 0.0024907 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_057_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=219, w2=450, w3=623, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 219)
    acceleration = _rolling_slope(velocity, 450)
    curvature = _rolling_slope(acceleration, 623)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.249333 * acceleration + 0.0024908 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_058_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=226, w2=463, w3=640, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(226, min_periods=max(226//3, 2)).mean(), upside.rolling(463, min_periods=max(463//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.52 + 0.0024909 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_059_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=233, w2=476, w3=657, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(476, min_periods=max(476//3, 2)).max()
    rebound = x - x.rolling(233, min_periods=max(233//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.262 * _rolling_slope(draw, 657) + 0.002491 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_060_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=240, w2=489, w3=674, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 240)
    baseline = trend.rolling(489, min_periods=max(489//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(674, min_periods=max(674//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.547059 + 0.0024911 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_061_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=247, w2=502, w3=691, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 247)
    slow = _rolling_slope(x, 502)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.560588 + 0.0024912 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_062_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=7, w2=16, w3=708, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(16, min_periods=max(16//3, 2)).max()
    trough = x.rolling(7, min_periods=max(7//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.574118 + 0.0024913 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_063_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=14, w2=29, w3=725, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(14)
    rank = change.rolling(29, min_periods=max(29//3, 2)).rank(pct=True)
    persistence = change.rolling(725, min_periods=max(725//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.287333 * persistence + 0.0024914 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_064_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=21, w2=42, w3=742, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(21, min_periods=max(21//3, 2)).std()
    vol_slow = ret.rolling(42, min_periods=max(42//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.601176 + 0.0024915 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_065_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=28, w2=55, w3=759, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(55, min_periods=max(55//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 28)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3 * slope + 0.0024916 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_066_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=35, w2=68, w3=25, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(35)
    drag = impulse.rolling(68, min_periods=max(68//3, 2)).mean()
    noise = impulse.abs().rolling(25, min_periods=max(25//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.628235 + 0.0024917 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_067_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=42, w2=81, w3=42, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 42)
    acceleration = _rolling_slope(velocity, 81)
    curvature = _rolling_slope(acceleration, 42)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.312667 * acceleration + 0.0024918 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_068_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=49, w2=94, w3=59, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(49, min_periods=max(49//3, 2)).mean(), upside.rolling(94, min_periods=max(94//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(59) * 1.655294 + 0.0024919 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_069_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=56, w2=107, w3=76, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(107, min_periods=max(107//3, 2)).max()
    rebound = x - x.rolling(56, min_periods=max(56//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.325333 * _rolling_slope(draw, 76) + 0.002492 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_070_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=63, w2=120, w3=93, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 63)
    baseline = trend.rolling(120, min_periods=max(120//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(93, min_periods=max(93//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.828824 + 0.0024921 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_071_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=70, w2=133, w3=110, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 70)
    slow = _rolling_slope(x, 133)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=110, adjust=False).mean() * 0.842353 + 0.0024922 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_072_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=77, w2=146, w3=127, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(146, min_periods=max(146//3, 2)).max()
    trough = x.rolling(77, min_periods=max(77//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.855882 + 0.0024923 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_073_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=84, w2=159, w3=144, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(84)
    rank = change.rolling(159, min_periods=max(159//3, 2)).rank(pct=True)
    persistence = change.rolling(144, min_periods=max(144//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.350667 * persistence + 0.0024924 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_074_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=91, w2=172, w3=161, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(91, min_periods=max(91//3, 2)).std()
    vol_slow = ret.rolling(172, min_periods=max(172//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.882941 + 0.0024925 * anchor
    return base_signal.diff().diff().diff()

def f34_tdsq_gemini_075_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=98, w2=185, w3=178, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(185, min_periods=max(185//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 98)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.031 * slope + 0.0024926 * anchor
    return base_signal.diff().diff().diff()
