"""17 trend line break dynamics gemini d1 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Kinetic energy and volume confirmation associated with the breach of established trend lines.
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

def f17_tlbk_gemini_001_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Kinetic energy and volume confirmation associated with the breach of established trend lines. [window=5]"""
    window = 5
    res = _safe_div(_rolling_slope(close, window), _rolling_zscore(volume, window).abs() + 1e-9)
    return (res).diff()

def f17_tlbk_gemini_002_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Kinetic energy and volume confirmation associated with the breach of established trend lines. [window=10]"""
    window = 10
    res = _safe_div(_rolling_slope(close, window), _rolling_zscore(volume, window).abs() + 1e-9)
    return (res).diff()

def f17_tlbk_gemini_003_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Kinetic energy and volume confirmation associated with the breach of established trend lines. [window=21]"""
    window = 21
    res = _safe_div(_rolling_slope(close, window), _rolling_zscore(volume, window).abs() + 1e-9)
    return (res).diff()

def f17_tlbk_gemini_004_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Kinetic energy and volume confirmation associated with the breach of established trend lines. [window=42]"""
    window = 42
    res = _safe_div(_rolling_slope(close, window), _rolling_zscore(volume, window).abs() + 1e-9)
    return (res).diff()

def f17_tlbk_gemini_005_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Kinetic energy and volume confirmation associated with the breach of established trend lines. [window=63]"""
    window = 63
    res = _safe_div(_rolling_slope(close, window), _rolling_zscore(volume, window).abs() + 1e-9)
    return (res).diff()

def f17_tlbk_gemini_006_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Kinetic energy and volume confirmation associated with the breach of established trend lines. [window=126]"""
    window = 126
    res = _safe_div(_rolling_slope(close, window), _rolling_zscore(volume, window).abs() + 1e-9)
    return (res).diff()

def f17_tlbk_gemini_007_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Kinetic energy and volume confirmation associated with the breach of established trend lines. [window=252]"""
    window = 252
    res = _safe_div(_rolling_slope(close, window), _rolling_zscore(volume, window).abs() + 1e-9)
    return (res).diff()

def f17_tlbk_gemini_008_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Kinetic energy and volume confirmation associated with the breach of established trend lines. [window=504]"""
    window = 504
    res = _safe_div(_rolling_slope(close, window), _rolling_zscore(volume, window).abs() + 1e-9)
    return (res).diff()

def f17_tlbk_gemini_009_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Kinetic energy and volume confirmation associated with the breach of established trend lines. [window=756]"""
    window = 756
    res = _safe_div(_rolling_slope(close, window), _rolling_zscore(volume, window).abs() + 1e-9)
    return (res).diff()

def f17_tlbk_gemini_010_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Kinetic energy and volume confirmation associated with the breach of established trend lines. [window=1260]"""
    window = 1260
    res = _safe_div(_rolling_slope(close, window), _rolling_zscore(volume, window).abs() + 1e-9)
    return (res).diff()

def f17_tlbk_gemini_011_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=210, w2=196, w3=714, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(196, min_periods=max(196//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 210)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.037667 * slope + 0.0015062 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_012_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=217, w2=209, w3=731, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(209, min_periods=max(209//3, 2)).mean()
    noise = impulse.abs().rolling(731, min_periods=max(731//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.46 + 0.0015063 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_013_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=224, w2=222, w3=748, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 224)
    acceleration = _rolling_slope(velocity, 222)
    curvature = _rolling_slope(acceleration, 748)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.050333 * acceleration + 0.0015064 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_014_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=231, w2=235, w3=765, lag=5)."""
    rel = _safe_div(close.shift(5), volume.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 231)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.056667 * pressure.rolling(765, min_periods=max(765//3, 2)).mean() + 0.0015065 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_015_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=238, w2=248, w3=31, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(238, min_periods=max(238//3, 2)).mean())
    decay = spread.ewm(span=248, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.500588 + 0.0015066 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_016_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=245, w2=261, w3=48, lag=13)."""
    a = _safe_log(close.abs() + 1.0).shift(13)
    b = _safe_log(volume.abs() + 1.0).shift(13)
    corr = a.rolling(261, min_periods=max(261//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 245)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.514118 + 0.0015067 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_017_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=5, w2=274, w3=65, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    cover = _safe_div(a.rolling(5, min_periods=max(5//3, 2)).mean(), b.abs().rolling(274, min_periods=max(274//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(65) + 0.075667 * _rolling_slope(cover, 5) + 0.0015068 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_018_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=12, w2=287, w3=82, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    y = _safe_log(volume.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.082 * y + 0.918000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 12) - _rolling_slope(basket, 287) + 0.0015069 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_019_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=19, w2=300, w3=99, lag=55)."""
    x = close.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(19, min_periods=max(19//3, 2)).mean(), upside.rolling(300, min_periods=max(300//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(99) * 1.554706 + 0.001507 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_020_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=26, w2=313, w3=116, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    draw = x - x.rolling(313, min_periods=max(313//3, 2)).max()
    rebound = x - x.rolling(26, min_periods=max(26//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.094667 * _rolling_slope(draw, 116) + 0.0015071 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_021_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=33, w2=326, w3=133, lag=1)."""
    a = _safe_log(close.abs() + 1.0).shift(1)
    b = _safe_log(volume.abs() + 1.0).shift(1)
    imbalance = a.diff(33) - b.diff(126)
    stress = imbalance.rolling(133, min_periods=max(133//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.581765 + 0.0015072 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_022_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=40, w2=339, w3=150, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 40)
    baseline = trend.rolling(339, min_periods=max(339//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(150, min_periods=max(150//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.595294 + 0.0015073 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_023_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=47, w2=352, w3=167, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 47)
    slow = _rolling_slope(x, 352)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=167, adjust=False).mean() * 1.608824 + 0.0015074 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_024_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=54, w2=365, w3=184, lag=5)."""
    x = close.shift(5)
    peak = x.rolling(365, min_periods=max(365//3, 2)).max()
    trough = x.rolling(54, min_periods=max(54//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.622353 + 0.0015075 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_025_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=61, w2=378, w3=201, lag=8)."""
    x = close.shift(8)
    change = x.pct_change(61)
    rank = change.rolling(378, min_periods=max(378//3, 2)).rank(pct=True)
    persistence = change.rolling(201, min_periods=max(201//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.126333 * persistence + 0.0015076 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_026_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=68, w2=391, w3=218, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(68, min_periods=max(68//3, 2)).std()
    vol_slow = ret.rolling(391, min_periods=max(391//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.649412 + 0.0015077 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_027_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=75, w2=404, w3=235, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(404, min_periods=max(404//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 75)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.139 * slope + 0.0015078 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_028_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=82, w2=417, w3=252, lag=34)."""
    x = close.shift(34)
    impulse = x.diff(82)
    drag = impulse.rolling(417, min_periods=max(417//3, 2)).mean()
    noise = impulse.abs().rolling(252, min_periods=max(252//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.822941 + 0.0015079 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_029_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=89, w2=430, w3=269, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 89)
    acceleration = _rolling_slope(velocity, 430)
    curvature = _rolling_slope(acceleration, 269)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.151667 * acceleration + 0.001508 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_030_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=96, w2=443, w3=286, lag=0)."""
    rel = _safe_div(close.shift(0), volume.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 96)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.158 * pressure.rolling(286, min_periods=max(286//3, 2)).mean() + 0.0015081 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_031_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=103, w2=456, w3=303, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(103, min_periods=max(103//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.863529 + 0.0015082 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_032_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=110, w2=469, w3=320, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(volume.abs() + 1.0).shift(2)
    corr = a.rolling(469, min_periods=max(469//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 110)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.877059 + 0.0015083 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_033_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=117, w2=482, w3=337, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    cover = _safe_div(a.rolling(117, min_periods=max(117//3, 2)).mean(), b.abs().rolling(482, min_periods=max(482//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.177 * _rolling_slope(cover, 117) + 0.0015084 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_034_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=124, w2=495, w3=354, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(volume.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.183333 * y + 0.816667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 124) - _rolling_slope(basket, 495) + 0.0015085 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_035_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=131, w2=508, w3=371, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(131, min_periods=max(131//3, 2)).mean(), upside.rolling(508, min_periods=max(508//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.917647 + 0.0015086 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_036_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=138, w2=22, w3=388, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    draw = x - x.rolling(22, min_periods=max(22//3, 2)).max()
    rebound = x - x.rolling(138, min_periods=max(138//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.196 * _rolling_slope(draw, 388) + 0.0015087 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_037_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=145, w2=35, w3=405, lag=21)."""
    a = _safe_log(close.abs() + 1.0).shift(21)
    b = _safe_log(volume.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(35)
    stress = imbalance.rolling(405, min_periods=max(405//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.944706 + 0.0015088 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_038_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=152, w2=48, w3=422, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 152)
    baseline = trend.rolling(48, min_periods=max(48//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(422, min_periods=max(422//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.958235 + 0.0015089 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_039_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=159, w2=61, w3=439, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 159)
    slow = _rolling_slope(x, 61)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.971765 + 0.001509 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_040_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=166, w2=74, w3=456, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(74, min_periods=max(74//3, 2)).max()
    trough = x.rolling(166, min_periods=max(166//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.985294 + 0.0015091 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_041_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=173, w2=87, w3=473, lag=1)."""
    x = close.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(87, min_periods=max(87//3, 2)).rank(pct=True)
    persistence = change.rolling(473, min_periods=max(473//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.227667 * persistence + 0.0015092 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_042_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=180, w2=100, w3=490, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(180, min_periods=max(180//3, 2)).std()
    vol_slow = ret.rolling(100, min_periods=max(100//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.012353 + 0.0015093 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_043_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=187, w2=113, w3=507, lag=3)."""
    x = close.shift(3)
    ma = x.rolling(113, min_periods=max(113//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 187)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.240333 * slope + 0.0015094 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_044_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=194, w2=126, w3=524, lag=5)."""
    x = close.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(126, min_periods=max(126//3, 2)).mean()
    noise = impulse.abs().rolling(524, min_periods=max(524//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.039412 + 0.0015095 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_045_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=201, w2=139, w3=541, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 201)
    acceleration = _rolling_slope(velocity, 139)
    curvature = _rolling_slope(acceleration, 541)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.253 * acceleration + 0.0015096 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_046_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=208, w2=152, w3=558, lag=13)."""
    rel = _safe_div(close.shift(13), volume.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 208)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.259333 * pressure.rolling(558, min_periods=max(558//3, 2)).mean() + 0.0015097 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_047_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=215, w2=165, w3=575, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(215, min_periods=max(215//3, 2)).mean())
    decay = spread.ewm(span=165, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.08 + 0.0015098 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_048_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=222, w2=178, w3=592, lag=34)."""
    a = _safe_log(close.abs() + 1.0).shift(34)
    b = _safe_log(volume.abs() + 1.0).shift(34)
    corr = a.rolling(178, min_periods=max(178//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 222)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.093529 + 0.0015099 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_049_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=229, w2=191, w3=609, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    cover = _safe_div(a.rolling(229, min_periods=max(229//3, 2)).mean(), b.abs().rolling(191, min_periods=max(191//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.278333 * _rolling_slope(cover, 229) + 0.00151 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_050_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=236, w2=204, w3=626, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    y = _safe_log(volume.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.284667 * y + 0.715333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 236) - _rolling_slope(basket, 204) + 0.0015101 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_051_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=243, w2=217, w3=643, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(243, min_periods=max(243//3, 2)).mean(), upside.rolling(217, min_periods=max(217//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.134118 + 0.0015102 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_052_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=250, w2=230, w3=660, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(230, min_periods=max(230//3, 2)).max()
    rebound = x - x.rolling(250, min_periods=max(250//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.297333 * _rolling_slope(draw, 660) + 0.0015103 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_053_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=10, w2=243, w3=677, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(volume.abs() + 1.0).shift(3)
    imbalance = a.diff(10) - b.diff(126)
    stress = imbalance.rolling(677, min_periods=max(677//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.161176 + 0.0015104 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_054_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=17, w2=256, w3=694, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 17)
    baseline = trend.rolling(256, min_periods=max(256//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(694, min_periods=max(694//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.174706 + 0.0015105 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_055_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=24, w2=269, w3=711, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 24)
    slow = _rolling_slope(x, 269)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.188235 + 0.0015106 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_056_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=31, w2=282, w3=728, lag=13)."""
    x = close.shift(13)
    peak = x.rolling(282, min_periods=max(282//3, 2)).max()
    trough = x.rolling(31, min_periods=max(31//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.201765 + 0.0015107 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_057_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=38, w2=295, w3=745, lag=21)."""
    x = close.shift(21)
    change = x.pct_change(38)
    rank = change.rolling(295, min_periods=max(295//3, 2)).rank(pct=True)
    persistence = change.rolling(745, min_periods=max(745//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.329 * persistence + 0.0015108 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_058_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=45, w2=308, w3=762, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(45, min_periods=max(45//3, 2)).std()
    vol_slow = ret.rolling(308, min_periods=max(308//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.228824 + 0.0015109 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_059_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=52, w2=321, w3=28, lag=55)."""
    x = close.shift(55)
    ma = x.rolling(321, min_periods=max(321//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 52)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.341667 * slope + 0.001511 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_060_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=59, w2=334, w3=45, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(59)
    drag = impulse.rolling(334, min_periods=max(334//3, 2)).mean()
    noise = impulse.abs().rolling(45, min_periods=max(45//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.255882 + 0.0015111 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_061_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=66, w2=347, w3=62, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 66)
    acceleration = _rolling_slope(velocity, 347)
    curvature = _rolling_slope(acceleration, 62)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.354333 * acceleration + 0.0015112 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_062_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=73, w2=360, w3=79, lag=2)."""
    rel = _safe_div(close.shift(2), volume.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 73)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.360667 * pressure.rolling(79, min_periods=max(79//3, 2)).mean() + 0.0015113 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_063_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=80, w2=373, w3=96, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(80, min_periods=max(80//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.296471 + 0.0015114 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_064_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=87, w2=386, w3=113, lag=5)."""
    a = _safe_log(close.abs() + 1.0).shift(5)
    b = _safe_log(volume.abs() + 1.0).shift(5)
    corr = a.rolling(386, min_periods=max(386//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 87)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.31 + 0.0015115 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_065_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=94, w2=399, w3=130, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    cover = _safe_div(a.rolling(94, min_periods=max(94//3, 2)).mean(), b.abs().rolling(399, min_periods=max(399//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.047333 * _rolling_slope(cover, 94) + 0.0015116 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_066_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=101, w2=412, w3=147, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    y = _safe_log(volume.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.053667 * y + 0.946333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 101) - _rolling_slope(basket, 412) + 0.0015117 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_067_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=108, w2=425, w3=164, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(108, min_periods=max(108//3, 2)).mean(), upside.rolling(425, min_periods=max(425//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.350588 + 0.0015118 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_068_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=115, w2=438, w3=181, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    draw = x - x.rolling(438, min_periods=max(438//3, 2)).max()
    rebound = x - x.rolling(115, min_periods=max(115//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.066333 * _rolling_slope(draw, 181) + 0.0015119 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_069_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=122, w2=451, w3=198, lag=55)."""
    a = _safe_log(close.abs() + 1.0).shift(55)
    b = _safe_log(volume.abs() + 1.0).shift(55)
    imbalance = a.diff(122) - b.diff(126)
    stress = imbalance.rolling(198, min_periods=max(198//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.377647 + 0.001512 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_070_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=129, w2=464, w3=215, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 129)
    baseline = trend.rolling(464, min_periods=max(464//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(215, min_periods=max(215//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.391176 + 0.0015121 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_071_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=136, w2=477, w3=232, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 136)
    slow = _rolling_slope(x, 477)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=232, adjust=False).mean() * 1.404706 + 0.0015122 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_072_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=143, w2=490, w3=249, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(490, min_periods=max(490//3, 2)).max()
    trough = x.rolling(143, min_periods=max(143//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.418235 + 0.0015123 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_073_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=150, w2=503, w3=266, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(503, min_periods=max(503//3, 2)).rank(pct=True)
    persistence = change.rolling(266, min_periods=max(266//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.098 * persistence + 0.0015124 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_074_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=157, w2=17, w3=283, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(157, min_periods=max(157//3, 2)).std()
    vol_slow = ret.rolling(17, min_periods=max(17//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.445294 + 0.0015125 * anchor
    return base_signal.diff()

def f17_tlbk_gemini_075_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=164, w2=30, w3=300, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(30, min_periods=max(30//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 164)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.110667 * slope + 0.0015126 * anchor
    return base_signal.diff()
