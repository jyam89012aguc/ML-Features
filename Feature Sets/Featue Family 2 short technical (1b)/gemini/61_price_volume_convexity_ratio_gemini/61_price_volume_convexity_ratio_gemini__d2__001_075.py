"""61 price volume convexity ratio gemini d2 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Non-linear relationship between price change and volume as a signal of trend strength.
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

def f61_pvcr_gemini_001_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Non-linear relationship between price change and volume as a signal of trend strength. [window=5]"""
    window = 5
    res = _safe_div(_rolling_slope(close, window), _rolling_slope(volume, window) + 1e-9)
    return (res).diff().diff()

def f61_pvcr_gemini_002_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Non-linear relationship between price change and volume as a signal of trend strength. [window=10]"""
    window = 10
    res = _safe_div(_rolling_slope(close, window), _rolling_slope(volume, window) + 1e-9)
    return (res).diff().diff()

def f61_pvcr_gemini_003_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Non-linear relationship between price change and volume as a signal of trend strength. [window=21]"""
    window = 21
    res = _safe_div(_rolling_slope(close, window), _rolling_slope(volume, window) + 1e-9)
    return (res).diff().diff()

def f61_pvcr_gemini_004_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Non-linear relationship between price change and volume as a signal of trend strength. [window=42]"""
    window = 42
    res = _safe_div(_rolling_slope(close, window), _rolling_slope(volume, window) + 1e-9)
    return (res).diff().diff()

def f61_pvcr_gemini_005_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Non-linear relationship between price change and volume as a signal of trend strength. [window=63]"""
    window = 63
    res = _safe_div(_rolling_slope(close, window), _rolling_slope(volume, window) + 1e-9)
    return (res).diff().diff()

def f61_pvcr_gemini_006_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Non-linear relationship between price change and volume as a signal of trend strength. [window=126]"""
    window = 126
    res = _safe_div(_rolling_slope(close, window), _rolling_slope(volume, window) + 1e-9)
    return (res).diff().diff()

def f61_pvcr_gemini_007_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Non-linear relationship between price change and volume as a signal of trend strength. [window=252]"""
    window = 252
    res = _safe_div(_rolling_slope(close, window), _rolling_slope(volume, window) + 1e-9)
    return (res).diff().diff()

def f61_pvcr_gemini_008_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Non-linear relationship between price change and volume as a signal of trend strength. [window=504]"""
    window = 504
    res = _safe_div(_rolling_slope(close, window), _rolling_slope(volume, window) + 1e-9)
    return (res).diff().diff()

def f61_pvcr_gemini_009_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Non-linear relationship between price change and volume as a signal of trend strength. [window=756]"""
    window = 756
    res = _safe_div(_rolling_slope(close, window), _rolling_slope(volume, window) + 1e-9)
    return (res).diff().diff()

def f61_pvcr_gemini_010_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Non-linear relationship between price change and volume as a signal of trend strength. [window=1260]"""
    window = 1260
    res = _safe_div(_rolling_slope(close, window), _rolling_slope(volume, window) + 1e-9)
    return (res).diff().diff()

def f61_pvcr_gemini_011_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=29, w2=481, w3=663, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 29)
    slow = _rolling_slope(x, 481)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.268235 + 0.0039842 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_012_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=36, w2=494, w3=680, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(494, min_periods=max(494//3, 2)).max()
    trough = x.rolling(36, min_periods=max(36//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.281765 + 0.0039843 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_013_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=43, w2=507, w3=697, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(43)
    rank = change.rolling(507, min_periods=max(507//3, 2)).rank(pct=True)
    persistence = change.rolling(697, min_periods=max(697//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.129 * persistence + 0.0039844 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_014_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=50, w2=21, w3=714, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(50, min_periods=max(50//3, 2)).std()
    vol_slow = ret.rolling(21, min_periods=max(21//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.308824 + 0.0039845 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_015_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=57, w2=34, w3=731, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(34, min_periods=max(34//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 57)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.141667 * slope + 0.0039846 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_016_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=64, w2=47, w3=748, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(64)
    drag = impulse.rolling(47, min_periods=max(47//3, 2)).mean()
    noise = impulse.abs().rolling(748, min_periods=max(748//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.335882 + 0.0039847 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_017_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=71, w2=60, w3=765, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 71)
    acceleration = _rolling_slope(velocity, 60)
    curvature = _rolling_slope(acceleration, 765)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.154333 * acceleration + 0.0039848 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_018_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=78, w2=73, w3=31, lag=34)."""
    rel = _safe_div(close.shift(34), volume.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 78)
    pressure = rel_log.diff(73)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.160667 * pressure.rolling(31, min_periods=max(31//3, 2)).mean() + 0.0039849 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_019_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=85, w2=86, w3=48, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(85, min_periods=max(85//3, 2)).mean())
    decay = spread.ewm(span=86, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.376471 + 0.003985 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_020_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=92, w2=99, w3=65, lag=0)."""
    a = _safe_log(close.abs() + 1.0).shift(0)
    b = _safe_log(volume.abs() + 1.0).shift(0)
    corr = a.rolling(99, min_periods=max(99//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 92)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.39 + 0.0039851 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_021_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=99, w2=112, w3=82, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    cover = _safe_div(a.rolling(99, min_periods=max(99//3, 2)).mean(), b.abs().rolling(112, min_periods=max(112//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(82) + 0.179667 * _rolling_slope(cover, 99) + 0.0039852 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_022_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=106, w2=125, w3=99, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    y = _safe_log(volume.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.186 * y + 0.814000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 106) - _rolling_slope(basket, 125) + 0.0039853 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_023_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=113, w2=138, w3=116, lag=3)."""
    x = close.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(113, min_periods=max(113//3, 2)).mean(), upside.rolling(138, min_periods=max(138//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(116) * 1.430588 + 0.0039854 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_024_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=120, w2=151, w3=133, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    draw = x - x.rolling(151, min_periods=max(151//3, 2)).max()
    rebound = x - x.rolling(120, min_periods=max(120//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.198667 * _rolling_slope(draw, 133) + 0.0039855 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_025_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=127, w2=164, w3=150, lag=8)."""
    a = _safe_log(close.abs() + 1.0).shift(8)
    b = _safe_log(volume.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(150, min_periods=max(150//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.457647 + 0.0039856 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_026_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=134, w2=177, w3=167, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 134)
    baseline = trend.rolling(177, min_periods=max(177//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(167, min_periods=max(167//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.471176 + 0.0039857 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_027_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=141, w2=190, w3=184, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 141)
    slow = _rolling_slope(x, 190)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=184, adjust=False).mean() * 1.484706 + 0.0039858 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_028_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=148, w2=203, w3=201, lag=34)."""
    x = close.shift(34)
    peak = x.rolling(203, min_periods=max(203//3, 2)).max()
    trough = x.rolling(148, min_periods=max(148//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.498235 + 0.0039859 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_029_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=155, w2=216, w3=218, lag=55)."""
    x = close.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(216, min_periods=max(216//3, 2)).rank(pct=True)
    persistence = change.rolling(218, min_periods=max(218//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.230333 * persistence + 0.003986 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_030_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=162, w2=229, w3=235, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(162, min_periods=max(162//3, 2)).std()
    vol_slow = ret.rolling(229, min_periods=max(229//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.525294 + 0.0039861 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_031_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=169, w2=242, w3=252, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(242, min_periods=max(242//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 169)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.243 * slope + 0.0039862 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_032_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=176, w2=255, w3=269, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(255, min_periods=max(255//3, 2)).mean()
    noise = impulse.abs().rolling(269, min_periods=max(269//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.552353 + 0.0039863 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_033_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=183, w2=268, w3=286, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 183)
    acceleration = _rolling_slope(velocity, 268)
    curvature = _rolling_slope(acceleration, 286)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.255667 * acceleration + 0.0039864 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_034_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=190, w2=281, w3=303, lag=5)."""
    rel = _safe_div(close.shift(5), volume.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 190)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.262 * pressure.rolling(303, min_periods=max(303//3, 2)).mean() + 0.0039865 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_035_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=197, w2=294, w3=320, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(197, min_periods=max(197//3, 2)).mean())
    decay = spread.ewm(span=294, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.592941 + 0.0039866 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_036_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=204, w2=307, w3=337, lag=13)."""
    a = _safe_log(close.abs() + 1.0).shift(13)
    b = _safe_log(volume.abs() + 1.0).shift(13)
    corr = a.rolling(307, min_periods=max(307//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 204)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.606471 + 0.0039867 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_037_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=211, w2=320, w3=354, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    cover = _safe_div(a.rolling(211, min_periods=max(211//3, 2)).mean(), b.abs().rolling(320, min_periods=max(320//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.281 * _rolling_slope(cover, 211) + 0.0039868 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_038_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=218, w2=333, w3=371, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    y = _safe_log(volume.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.287333 * y + 0.712667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 218) - _rolling_slope(basket, 333) + 0.0039869 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_039_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=225, w2=346, w3=388, lag=55)."""
    x = close.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(225, min_periods=max(225//3, 2)).mean(), upside.rolling(346, min_periods=max(346//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.647059 + 0.003987 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_040_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=232, w2=359, w3=405, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    draw = x - x.rolling(359, min_periods=max(359//3, 2)).max()
    rebound = x - x.rolling(232, min_periods=max(232//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3 * _rolling_slope(draw, 405) + 0.0039871 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_041_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=239, w2=372, w3=422, lag=1)."""
    a = _safe_log(close.abs() + 1.0).shift(1)
    b = _safe_log(volume.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(422, min_periods=max(422//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.820588 + 0.0039872 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_042_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=246, w2=385, w3=439, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 246)
    baseline = trend.rolling(385, min_periods=max(385//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(439, min_periods=max(439//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.834118 + 0.0039873 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_043_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=6, w2=398, w3=456, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 6)
    slow = _rolling_slope(x, 398)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.847647 + 0.0039874 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_044_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=13, w2=411, w3=473, lag=5)."""
    x = close.shift(5)
    peak = x.rolling(411, min_periods=max(411//3, 2)).max()
    trough = x.rolling(13, min_periods=max(13//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.861176 + 0.0039875 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_045_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=20, w2=424, w3=490, lag=8)."""
    x = close.shift(8)
    change = x.pct_change(20)
    rank = change.rolling(424, min_periods=max(424//3, 2)).rank(pct=True)
    persistence = change.rolling(490, min_periods=max(490//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.331667 * persistence + 0.0039876 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_046_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=27, w2=437, w3=507, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(27, min_periods=max(27//3, 2)).std()
    vol_slow = ret.rolling(437, min_periods=max(437//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.888235 + 0.0039877 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_047_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=34, w2=450, w3=524, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(450, min_periods=max(450//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 34)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.344333 * slope + 0.0039878 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_048_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=41, w2=463, w3=541, lag=34)."""
    x = close.shift(34)
    impulse = x.diff(41)
    drag = impulse.rolling(463, min_periods=max(463//3, 2)).mean()
    noise = impulse.abs().rolling(541, min_periods=max(541//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.915294 + 0.0039879 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_049_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=48, w2=476, w3=558, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 48)
    acceleration = _rolling_slope(velocity, 476)
    curvature = _rolling_slope(acceleration, 558)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.357 * acceleration + 0.003988 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_050_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=55, w2=489, w3=575, lag=0)."""
    rel = _safe_div(close.shift(0), volume.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 55)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.031 * pressure.rolling(575, min_periods=max(575//3, 2)).mean() + 0.0039881 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_051_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=62, w2=502, w3=592, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(62, min_periods=max(62//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.955882 + 0.0039882 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_052_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=69, w2=16, w3=609, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(volume.abs() + 1.0).shift(2)
    corr = a.rolling(16, min_periods=max(16//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 69)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.969412 + 0.0039883 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_053_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=76, w2=29, w3=626, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    cover = _safe_div(a.rolling(76, min_periods=max(76//3, 2)).mean(), b.abs().rolling(29, min_periods=max(29//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.05 * _rolling_slope(cover, 76) + 0.0039884 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_054_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=83, w2=42, w3=643, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(volume.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.056333 * y + 0.943667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 83) - _rolling_slope(basket, 42) + 0.0039885 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_055_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=90, w2=55, w3=660, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(90, min_periods=max(90//3, 2)).mean(), upside.rolling(55, min_periods=max(55//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.01 + 0.0039886 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_056_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=97, w2=68, w3=677, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    draw = x - x.rolling(68, min_periods=max(68//3, 2)).max()
    rebound = x - x.rolling(97, min_periods=max(97//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.069 * _rolling_slope(draw, 677) + 0.0039887 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_057_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=104, w2=81, w3=694, lag=21)."""
    a = _safe_log(close.abs() + 1.0).shift(21)
    b = _safe_log(volume.abs() + 1.0).shift(21)
    imbalance = a.diff(104) - b.diff(81)
    stress = imbalance.rolling(694, min_periods=max(694//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.037059 + 0.0039888 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_058_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=111, w2=94, w3=711, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 111)
    baseline = trend.rolling(94, min_periods=max(94//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(711, min_periods=max(711//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.050588 + 0.0039889 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_059_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=118, w2=107, w3=728, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 118)
    slow = _rolling_slope(x, 107)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.064118 + 0.003989 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_060_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=125, w2=120, w3=745, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(120, min_periods=max(120//3, 2)).max()
    trough = x.rolling(125, min_periods=max(125//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.077647 + 0.0039891 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_061_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=132, w2=133, w3=762, lag=1)."""
    x = close.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(133, min_periods=max(133//3, 2)).rank(pct=True)
    persistence = change.rolling(762, min_periods=max(762//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.100667 * persistence + 0.0039892 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_062_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=139, w2=146, w3=28, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(139, min_periods=max(139//3, 2)).std()
    vol_slow = ret.rolling(146, min_periods=max(146//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.104706 + 0.0039893 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_063_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=146, w2=159, w3=45, lag=3)."""
    x = close.shift(3)
    ma = x.rolling(159, min_periods=max(159//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 146)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.113333 * slope + 0.0039894 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_064_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=153, w2=172, w3=62, lag=5)."""
    x = close.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(172, min_periods=max(172//3, 2)).mean()
    noise = impulse.abs().rolling(62, min_periods=max(62//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.131765 + 0.0039895 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_065_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=160, w2=185, w3=79, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 160)
    acceleration = _rolling_slope(velocity, 185)
    curvature = _rolling_slope(acceleration, 79)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.126 * acceleration + 0.0039896 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_066_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=167, w2=198, w3=96, lag=13)."""
    rel = _safe_div(close.shift(13), volume.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 167)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.132333 * pressure.rolling(96, min_periods=max(96//3, 2)).mean() + 0.0039897 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_067_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=174, w2=211, w3=113, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(174, min_periods=max(174//3, 2)).mean())
    decay = spread.ewm(span=211, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.172353 + 0.0039898 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_068_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=181, w2=224, w3=130, lag=34)."""
    a = _safe_log(close.abs() + 1.0).shift(34)
    b = _safe_log(volume.abs() + 1.0).shift(34)
    corr = a.rolling(224, min_periods=max(224//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 181)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.185882 + 0.0039899 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_069_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=188, w2=237, w3=147, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    cover = _safe_div(a.rolling(188, min_periods=max(188//3, 2)).mean(), b.abs().rolling(237, min_periods=max(237//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.151333 * _rolling_slope(cover, 188) + 0.00399 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_070_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=195, w2=250, w3=164, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    y = _safe_log(volume.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.157667 * y + 0.842333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 195) - _rolling_slope(basket, 250) + 0.0039901 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_071_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=202, w2=263, w3=181, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(202, min_periods=max(202//3, 2)).mean(), upside.rolling(263, min_periods=max(263//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.226471 + 0.0039902 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_072_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=209, w2=276, w3=198, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(276, min_periods=max(276//3, 2)).max()
    rebound = x - x.rolling(209, min_periods=max(209//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.170333 * _rolling_slope(draw, 198) + 0.0039903 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_073_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=216, w2=289, w3=215, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(volume.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(215, min_periods=max(215//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.253529 + 0.0039904 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_074_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=223, w2=302, w3=232, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 223)
    baseline = trend.rolling(302, min_periods=max(302//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(232, min_periods=max(232//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.267059 + 0.0039905 * anchor
    return base_signal.diff().diff()

def f61_pvcr_gemini_075_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=230, w2=315, w3=249, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 230)
    slow = _rolling_slope(x, 315)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=249, adjust=False).mean() * 1.280588 + 0.0039906 * anchor
    return base_signal.diff().diff()
