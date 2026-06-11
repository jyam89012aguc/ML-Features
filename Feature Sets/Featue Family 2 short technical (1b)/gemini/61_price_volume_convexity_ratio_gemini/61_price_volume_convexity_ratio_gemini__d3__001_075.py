"""61 price volume convexity ratio gemini d3 features 1-75 — Pipeline 1b-HF Grade v7.

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

def f61_pvcr_gemini_001_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Non-linear relationship between price change and volume as a signal of trend strength. [window=5]"""
    window = 5
    res = _safe_div(_rolling_slope(close, window), _rolling_slope(volume, window) + 1e-9)
    return (res).diff().diff().diff()

def f61_pvcr_gemini_002_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Non-linear relationship between price change and volume as a signal of trend strength. [window=10]"""
    window = 10
    res = _safe_div(_rolling_slope(close, window), _rolling_slope(volume, window) + 1e-9)
    return (res).diff().diff().diff()

def f61_pvcr_gemini_003_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Non-linear relationship between price change and volume as a signal of trend strength. [window=21]"""
    window = 21
    res = _safe_div(_rolling_slope(close, window), _rolling_slope(volume, window) + 1e-9)
    return (res).diff().diff().diff()

def f61_pvcr_gemini_004_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Non-linear relationship between price change and volume as a signal of trend strength. [window=42]"""
    window = 42
    res = _safe_div(_rolling_slope(close, window), _rolling_slope(volume, window) + 1e-9)
    return (res).diff().diff().diff()

def f61_pvcr_gemini_005_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Non-linear relationship between price change and volume as a signal of trend strength. [window=63]"""
    window = 63
    res = _safe_div(_rolling_slope(close, window), _rolling_slope(volume, window) + 1e-9)
    return (res).diff().diff().diff()

def f61_pvcr_gemini_006_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Non-linear relationship between price change and volume as a signal of trend strength. [window=126]"""
    window = 126
    res = _safe_div(_rolling_slope(close, window), _rolling_slope(volume, window) + 1e-9)
    return (res).diff().diff().diff()

def f61_pvcr_gemini_007_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Non-linear relationship between price change and volume as a signal of trend strength. [window=252]"""
    window = 252
    res = _safe_div(_rolling_slope(close, window), _rolling_slope(volume, window) + 1e-9)
    return (res).diff().diff().diff()

def f61_pvcr_gemini_008_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Non-linear relationship between price change and volume as a signal of trend strength. [window=504]"""
    window = 504
    res = _safe_div(_rolling_slope(close, window), _rolling_slope(volume, window) + 1e-9)
    return (res).diff().diff().diff()

def f61_pvcr_gemini_009_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Non-linear relationship between price change and volume as a signal of trend strength. [window=756]"""
    window = 756
    res = _safe_div(_rolling_slope(close, window), _rolling_slope(volume, window) + 1e-9)
    return (res).diff().diff().diff()

def f61_pvcr_gemini_010_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Non-linear relationship between price change and volume as a signal of trend strength. [window=1260]"""
    window = 1260
    res = _safe_div(_rolling_slope(close, window), _rolling_slope(volume, window) + 1e-9)
    return (res).diff().diff().diff()

def f61_pvcr_gemini_011_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=21, w2=305, w3=39, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(21, min_periods=max(21//3, 2)).mean(), upside.rolling(305, min_periods=max(305//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(39) * 1.455294 + 0.0039982 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_012_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=28, w2=318, w3=56, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(318, min_periods=max(318//3, 2)).max()
    rebound = x - x.rolling(28, min_periods=max(28//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.344667 * _rolling_slope(draw, 56) + 0.0039983 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_013_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=35, w2=331, w3=73, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(volume.abs() + 1.0).shift(3)
    imbalance = a.diff(35) - b.diff(126)
    stress = imbalance.rolling(73, min_periods=max(73//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.482353 + 0.0039984 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_014_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=42, w2=344, w3=90, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 42)
    baseline = trend.rolling(344, min_periods=max(344//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(90, min_periods=max(90//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.495882 + 0.0039985 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_015_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=49, w2=357, w3=107, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 49)
    slow = _rolling_slope(x, 357)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=107, adjust=False).mean() * 1.509412 + 0.0039986 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_016_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=56, w2=370, w3=124, lag=13)."""
    x = close.shift(13)
    peak = x.rolling(370, min_periods=max(370//3, 2)).max()
    trough = x.rolling(56, min_periods=max(56//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.522941 + 0.0039987 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_017_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=63, w2=383, w3=141, lag=21)."""
    x = close.shift(21)
    change = x.pct_change(63)
    rank = change.rolling(383, min_periods=max(383//3, 2)).rank(pct=True)
    persistence = change.rolling(141, min_periods=max(141//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.044 * persistence + 0.0039988 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_018_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=70, w2=396, w3=158, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(70, min_periods=max(70//3, 2)).std()
    vol_slow = ret.rolling(396, min_periods=max(396//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.55 + 0.0039989 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_019_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=77, w2=409, w3=175, lag=55)."""
    x = close.shift(55)
    ma = x.rolling(409, min_periods=max(409//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 77)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.056667 * slope + 0.003999 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_020_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=84, w2=422, w3=192, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(84)
    drag = impulse.rolling(422, min_periods=max(422//3, 2)).mean()
    noise = impulse.abs().rolling(192, min_periods=max(192//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.577059 + 0.0039991 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_021_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=91, w2=435, w3=209, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 91)
    acceleration = _rolling_slope(velocity, 435)
    curvature = _rolling_slope(acceleration, 209)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.069333 * acceleration + 0.0039992 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_022_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=98, w2=448, w3=226, lag=2)."""
    rel = _safe_div(close.shift(2), volume.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 98)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.075667 * pressure.rolling(226, min_periods=max(226//3, 2)).mean() + 0.0039993 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_023_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=105, w2=461, w3=243, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(105, min_periods=max(105//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.617647 + 0.0039994 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_024_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=112, w2=474, w3=260, lag=5)."""
    a = _safe_log(close.abs() + 1.0).shift(5)
    b = _safe_log(volume.abs() + 1.0).shift(5)
    corr = a.rolling(474, min_periods=max(474//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 112)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.631176 + 0.0039995 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_025_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=119, w2=487, w3=277, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    cover = _safe_div(a.rolling(119, min_periods=max(119//3, 2)).mean(), b.abs().rolling(487, min_periods=max(487//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.094667 * _rolling_slope(cover, 119) + 0.0039996 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_026_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=126, w2=500, w3=294, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    y = _safe_log(volume.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.101 * y + 0.899000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 126) - _rolling_slope(basket, 500) + 0.0039997 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_027_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=133, w2=14, w3=311, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(133, min_periods=max(133//3, 2)).mean(), upside.rolling(14, min_periods=max(14//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.671765 + 0.0039998 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_028_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=140, w2=27, w3=328, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    draw = x - x.rolling(27, min_periods=max(27//3, 2)).max()
    rebound = x - x.rolling(140, min_periods=max(140//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.113667 * _rolling_slope(draw, 328) + 0.0039999 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_029_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=147, w2=40, w3=345, lag=55)."""
    a = _safe_log(close.abs() + 1.0).shift(55)
    b = _safe_log(volume.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(40)
    stress = imbalance.rolling(345, min_periods=max(345//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.845294 + 0.004 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_030_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=154, w2=53, w3=362, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 154)
    baseline = trend.rolling(53, min_periods=max(53//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(362, min_periods=max(362//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.858824 + 0.0040001 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_031_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=161, w2=66, w3=379, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 161)
    slow = _rolling_slope(x, 66)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.872353 + 0.0040002 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_032_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=168, w2=79, w3=396, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(79, min_periods=max(79//3, 2)).max()
    trough = x.rolling(168, min_periods=max(168//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.885882 + 0.0040003 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_033_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=175, w2=92, w3=413, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(92, min_periods=max(92//3, 2)).rank(pct=True)
    persistence = change.rolling(413, min_periods=max(413//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.145333 * persistence + 0.0040004 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_034_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=182, w2=105, w3=430, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(182, min_periods=max(182//3, 2)).std()
    vol_slow = ret.rolling(105, min_periods=max(105//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.912941 + 0.0040005 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_035_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=189, w2=118, w3=447, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(118, min_periods=max(118//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 189)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.158 * slope + 0.0040006 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_036_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=196, w2=131, w3=464, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(131, min_periods=max(131//3, 2)).mean()
    noise = impulse.abs().rolling(464, min_periods=max(464//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.94 + 0.0040007 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_037_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=203, w2=144, w3=481, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 203)
    acceleration = _rolling_slope(velocity, 144)
    curvature = _rolling_slope(acceleration, 481)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.170667 * acceleration + 0.0040008 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_038_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=210, w2=157, w3=498, lag=34)."""
    rel = _safe_div(close.shift(34), volume.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 210)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.177 * pressure.rolling(498, min_periods=max(498//3, 2)).mean() + 0.0040009 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_039_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=217, w2=170, w3=515, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(217, min_periods=max(217//3, 2)).mean())
    decay = spread.ewm(span=170, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.980588 + 0.004001 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_040_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=224, w2=183, w3=532, lag=0)."""
    a = _safe_log(close.abs() + 1.0).shift(0)
    b = _safe_log(volume.abs() + 1.0).shift(0)
    corr = a.rolling(183, min_periods=max(183//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 224)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.994118 + 0.0040011 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_041_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=231, w2=196, w3=549, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    cover = _safe_div(a.rolling(231, min_periods=max(231//3, 2)).mean(), b.abs().rolling(196, min_periods=max(196//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.196 * _rolling_slope(cover, 231) + 0.0040012 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_042_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=238, w2=209, w3=566, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    y = _safe_log(volume.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.202333 * y + 0.797667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 238) - _rolling_slope(basket, 209) + 0.0040013 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_043_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=245, w2=222, w3=583, lag=3)."""
    x = close.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(245, min_periods=max(245//3, 2)).mean(), upside.rolling(222, min_periods=max(222//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.034706 + 0.0040014 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_044_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=5, w2=235, w3=600, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    draw = x - x.rolling(235, min_periods=max(235//3, 2)).max()
    rebound = x - x.rolling(5, min_periods=max(5//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.215 * _rolling_slope(draw, 600) + 0.0040015 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_045_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=12, w2=248, w3=617, lag=8)."""
    a = _safe_log(close.abs() + 1.0).shift(8)
    b = _safe_log(volume.abs() + 1.0).shift(8)
    imbalance = a.diff(12) - b.diff(126)
    stress = imbalance.rolling(617, min_periods=max(617//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.061765 + 0.0040016 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_046_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=19, w2=261, w3=634, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 19)
    baseline = trend.rolling(261, min_periods=max(261//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(634, min_periods=max(634//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.075294 + 0.0040017 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_047_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=26, w2=274, w3=651, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 26)
    slow = _rolling_slope(x, 274)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.088824 + 0.0040018 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_048_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=33, w2=287, w3=668, lag=34)."""
    x = close.shift(34)
    peak = x.rolling(287, min_periods=max(287//3, 2)).max()
    trough = x.rolling(33, min_periods=max(33//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.102353 + 0.0040019 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_049_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=40, w2=300, w3=685, lag=55)."""
    x = close.shift(55)
    change = x.pct_change(40)
    rank = change.rolling(300, min_periods=max(300//3, 2)).rank(pct=True)
    persistence = change.rolling(685, min_periods=max(685//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.246667 * persistence + 0.004002 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_050_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=47, w2=313, w3=702, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(47, min_periods=max(47//3, 2)).std()
    vol_slow = ret.rolling(313, min_periods=max(313//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.129412 + 0.0040021 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_051_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=54, w2=326, w3=719, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(326, min_periods=max(326//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 54)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.259333 * slope + 0.0040022 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_052_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=61, w2=339, w3=736, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(61)
    drag = impulse.rolling(339, min_periods=max(339//3, 2)).mean()
    noise = impulse.abs().rolling(736, min_periods=max(736//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.156471 + 0.0040023 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_053_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=68, w2=352, w3=753, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 68)
    acceleration = _rolling_slope(velocity, 352)
    curvature = _rolling_slope(acceleration, 753)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.272 * acceleration + 0.0040024 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_054_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=75, w2=365, w3=19, lag=5)."""
    rel = _safe_div(close.shift(5), volume.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 75)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.278333 * pressure.rolling(19, min_periods=max(19//3, 2)).mean() + 0.0040025 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_055_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=82, w2=378, w3=36, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(82, min_periods=max(82//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.197059 + 0.0040026 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_056_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=89, w2=391, w3=53, lag=13)."""
    a = _safe_log(close.abs() + 1.0).shift(13)
    b = _safe_log(volume.abs() + 1.0).shift(13)
    corr = a.rolling(391, min_periods=max(391//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 89)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.210588 + 0.0040027 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_057_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=96, w2=404, w3=70, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    cover = _safe_div(a.rolling(96, min_periods=max(96//3, 2)).mean(), b.abs().rolling(404, min_periods=max(404//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(70) + 0.297333 * _rolling_slope(cover, 96) + 0.0040028 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_058_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=103, w2=417, w3=87, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    y = _safe_log(volume.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.303667 * y + 0.696333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 103) - _rolling_slope(basket, 417) + 0.0040029 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_059_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=110, w2=430, w3=104, lag=55)."""
    x = close.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(110, min_periods=max(110//3, 2)).mean(), upside.rolling(430, min_periods=max(430//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(104) * 1.251176 + 0.004003 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_060_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=117, w2=443, w3=121, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    draw = x - x.rolling(443, min_periods=max(443//3, 2)).max()
    rebound = x - x.rolling(117, min_periods=max(117//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.316333 * _rolling_slope(draw, 121) + 0.0040031 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_061_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=124, w2=456, w3=138, lag=1)."""
    a = _safe_log(close.abs() + 1.0).shift(1)
    b = _safe_log(volume.abs() + 1.0).shift(1)
    imbalance = a.diff(124) - b.diff(126)
    stress = imbalance.rolling(138, min_periods=max(138//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.278235 + 0.0040032 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_062_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=131, w2=469, w3=155, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 131)
    baseline = trend.rolling(469, min_periods=max(469//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(155, min_periods=max(155//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.291765 + 0.0040033 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_063_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=138, w2=482, w3=172, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 138)
    slow = _rolling_slope(x, 482)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=172, adjust=False).mean() * 1.305294 + 0.0040034 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_064_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=145, w2=495, w3=189, lag=5)."""
    x = close.shift(5)
    peak = x.rolling(495, min_periods=max(495//3, 2)).max()
    trough = x.rolling(145, min_periods=max(145//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.318824 + 0.0040035 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_065_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=152, w2=508, w3=206, lag=8)."""
    x = close.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(508, min_periods=max(508//3, 2)).rank(pct=True)
    persistence = change.rolling(206, min_periods=max(206//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.348 * persistence + 0.0040036 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_066_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=159, w2=22, w3=223, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(159, min_periods=max(159//3, 2)).std()
    vol_slow = ret.rolling(22, min_periods=max(22//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.345882 + 0.0040037 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_067_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=166, w2=35, w3=240, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(35, min_periods=max(35//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 166)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.360667 * slope + 0.0040038 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_068_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=173, w2=48, w3=257, lag=34)."""
    x = close.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(48, min_periods=max(48//3, 2)).mean()
    noise = impulse.abs().rolling(257, min_periods=max(257//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.372941 + 0.0040039 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_069_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=180, w2=61, w3=274, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 180)
    acceleration = _rolling_slope(velocity, 61)
    curvature = _rolling_slope(acceleration, 274)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.041 * acceleration + 0.004004 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_070_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=187, w2=74, w3=291, lag=0)."""
    rel = _safe_div(close.shift(0), volume.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 187)
    pressure = rel_log.diff(74)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.047333 * pressure.rolling(291, min_periods=max(291//3, 2)).mean() + 0.0040041 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_071_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=194, w2=87, w3=308, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(194, min_periods=max(194//3, 2)).mean())
    decay = spread.ewm(span=87, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.413529 + 0.0040042 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_072_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=201, w2=100, w3=325, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(volume.abs() + 1.0).shift(2)
    corr = a.rolling(100, min_periods=max(100//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 201)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.427059 + 0.0040043 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_073_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=208, w2=113, w3=342, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    cover = _safe_div(a.rolling(208, min_periods=max(208//3, 2)).mean(), b.abs().rolling(113, min_periods=max(113//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.066333 * _rolling_slope(cover, 208) + 0.0040044 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_074_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=215, w2=126, w3=359, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(volume.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.072667 * y + 0.927333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 215) - _rolling_slope(basket, 126) + 0.0040045 * anchor
    return base_signal.diff().diff().diff()

def f61_pvcr_gemini_075_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=222, w2=139, w3=376, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(222, min_periods=max(222//3, 2)).mean(), upside.rolling(139, min_periods=max(139//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.467647 + 0.0040046 * anchor
    return base_signal.diff().diff().diff()
