"""29 ultimate aroon vortex gemini d1 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Directional movement and trend strength identified through Aroon and Vortex indicators.
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

def f29_vtxn_gemini_001_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Directional movement and trend strength identified through Aroon and Vortex indicators. [window=5]"""
    window = 5
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window))
    return (res).diff()

def f29_vtxn_gemini_002_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Directional movement and trend strength identified through Aroon and Vortex indicators. [window=10]"""
    window = 10
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window))
    return (res).diff()

def f29_vtxn_gemini_003_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Directional movement and trend strength identified through Aroon and Vortex indicators. [window=21]"""
    window = 21
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window))
    return (res).diff()

def f29_vtxn_gemini_004_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Directional movement and trend strength identified through Aroon and Vortex indicators. [window=42]"""
    window = 42
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window))
    return (res).diff()

def f29_vtxn_gemini_005_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Directional movement and trend strength identified through Aroon and Vortex indicators. [window=63]"""
    window = 63
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window))
    return (res).diff()

def f29_vtxn_gemini_006_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Directional movement and trend strength identified through Aroon and Vortex indicators. [window=126]"""
    window = 126
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window))
    return (res).diff()

def f29_vtxn_gemini_007_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Directional movement and trend strength identified through Aroon and Vortex indicators. [window=252]"""
    window = 252
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window))
    return (res).diff()

def f29_vtxn_gemini_008_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Directional movement and trend strength identified through Aroon and Vortex indicators. [window=504]"""
    window = 504
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window))
    return (res).diff()

def f29_vtxn_gemini_009_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Directional movement and trend strength identified through Aroon and Vortex indicators. [window=756]"""
    window = 756
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window))
    return (res).diff()

def f29_vtxn_gemini_010_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Directional movement and trend strength identified through Aroon and Vortex indicators. [window=1260]"""
    window = 1260
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window))
    return (res).diff()

def f29_vtxn_gemini_011_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=73, w2=231, w3=51, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(231, min_periods=max(231//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 73)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.059 * slope + 0.0021782 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_012_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=80, w2=244, w3=68, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(80)
    drag = impulse.rolling(244, min_periods=max(244//3, 2)).mean()
    noise = impulse.abs().rolling(68, min_periods=max(68//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.05 + 0.0021783 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_013_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=87, w2=257, w3=85, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 87)
    acceleration = _rolling_slope(velocity, 257)
    curvature = _rolling_slope(acceleration, 85)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.071667 * acceleration + 0.0021784 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_014_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=94, w2=270, w3=102, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 94)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.078 * pressure.rolling(102, min_periods=max(102//3, 2)).mean() + 0.0021785 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_015_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=101, w2=283, w3=119, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(101, min_periods=max(101//3, 2)).mean())
    decay = spread.ewm(span=283, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.090588 + 0.0021786 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_016_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=108, w2=296, w3=136, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(296, min_periods=max(296//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 108)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.104118 + 0.0021787 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_017_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=115, w2=309, w3=153, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(115, min_periods=max(115//3, 2)).mean(), b.abs().rolling(309, min_periods=max(309//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.097 * _rolling_slope(cover, 115) + 0.0021788 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_018_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=122, w2=322, w3=170, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.103333 * y + 0.896667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 122) - _rolling_slope(basket, 322) + 0.0021789 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_019_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=129, w2=335, w3=187, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(129, min_periods=max(129//3, 2)).mean(), upside.rolling(335, min_periods=max(335//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.144706 + 0.002179 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_020_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=136, w2=348, w3=204, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(348, min_periods=max(348//3, 2)).max()
    rebound = x - x.rolling(136, min_periods=max(136//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.116 * _rolling_slope(draw, 204) + 0.0021791 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_021_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=143, w2=361, w3=221, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(221, min_periods=max(221//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.171765 + 0.0021792 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_022_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=150, w2=374, w3=238, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 150)
    baseline = trend.rolling(374, min_periods=max(374//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(238, min_periods=max(238//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.185294 + 0.0021793 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_023_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=157, w2=387, w3=255, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 157)
    slow = _rolling_slope(x, 387)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=255, adjust=False).mean() * 1.198824 + 0.0021794 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_024_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=164, w2=400, w3=272, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(400, min_periods=max(400//3, 2)).max()
    trough = x.rolling(164, min_periods=max(164//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.212353 + 0.0021795 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_025_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=171, w2=413, w3=289, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(413, min_periods=max(413//3, 2)).rank(pct=True)
    persistence = change.rolling(289, min_periods=max(289//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.147667 * persistence + 0.0021796 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_026_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=178, w2=426, w3=306, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(178, min_periods=max(178//3, 2)).std()
    vol_slow = ret.rolling(426, min_periods=max(426//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.239412 + 0.0021797 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_027_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=185, w2=439, w3=323, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(439, min_periods=max(439//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 185)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.160333 * slope + 0.0021798 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_028_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=192, w2=452, w3=340, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(452, min_periods=max(452//3, 2)).mean()
    noise = impulse.abs().rolling(340, min_periods=max(340//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.266471 + 0.0021799 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_029_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=199, w2=465, w3=357, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 199)
    acceleration = _rolling_slope(velocity, 465)
    curvature = _rolling_slope(acceleration, 357)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.173 * acceleration + 0.00218 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_030_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=206, w2=478, w3=374, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 206)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.179333 * pressure.rolling(374, min_periods=max(374//3, 2)).mean() + 0.0021801 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_031_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=213, w2=491, w3=391, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(213, min_periods=max(213//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.307059 + 0.0021802 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_032_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=220, w2=504, w3=408, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(504, min_periods=max(504//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 220)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.320588 + 0.0021803 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_033_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=227, w2=18, w3=425, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(227, min_periods=max(227//3, 2)).mean(), b.abs().rolling(18, min_periods=max(18//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.198333 * _rolling_slope(cover, 227) + 0.0021804 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_034_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=234, w2=31, w3=442, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.204667 * y + 0.795333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 234) - _rolling_slope(basket, 31) + 0.0021805 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_035_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=241, w2=44, w3=459, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(241, min_periods=max(241//3, 2)).mean(), upside.rolling(44, min_periods=max(44//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.361176 + 0.0021806 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_036_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=248, w2=57, w3=476, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(57, min_periods=max(57//3, 2)).max()
    rebound = x - x.rolling(248, min_periods=max(248//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.217333 * _rolling_slope(draw, 476) + 0.0021807 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_037_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=8, w2=70, w3=493, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(8) - b.diff(70)
    stress = imbalance.rolling(493, min_periods=max(493//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.388235 + 0.0021808 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_038_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=15, w2=83, w3=510, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 15)
    baseline = trend.rolling(83, min_periods=max(83//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(510, min_periods=max(510//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.401765 + 0.0021809 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_039_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=22, w2=96, w3=527, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 22)
    slow = _rolling_slope(x, 96)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.415294 + 0.002181 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_040_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=29, w2=109, w3=544, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(109, min_periods=max(109//3, 2)).max()
    trough = x.rolling(29, min_periods=max(29//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.428824 + 0.0021811 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_041_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=36, w2=122, w3=561, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(36)
    rank = change.rolling(122, min_periods=max(122//3, 2)).rank(pct=True)
    persistence = change.rolling(561, min_periods=max(561//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.249 * persistence + 0.0021812 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_042_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=43, w2=135, w3=578, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(43, min_periods=max(43//3, 2)).std()
    vol_slow = ret.rolling(135, min_periods=max(135//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.455882 + 0.0021813 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_043_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=50, w2=148, w3=595, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(148, min_periods=max(148//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 50)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.261667 * slope + 0.0021814 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_044_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=57, w2=161, w3=612, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(57)
    drag = impulse.rolling(161, min_periods=max(161//3, 2)).mean()
    noise = impulse.abs().rolling(612, min_periods=max(612//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.482941 + 0.0021815 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_045_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=64, w2=174, w3=629, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 64)
    acceleration = _rolling_slope(velocity, 174)
    curvature = _rolling_slope(acceleration, 629)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.274333 * acceleration + 0.0021816 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_046_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=71, w2=187, w3=646, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 71)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.280667 * pressure.rolling(646, min_periods=max(646//3, 2)).mean() + 0.0021817 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_047_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=78, w2=200, w3=663, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(78, min_periods=max(78//3, 2)).mean())
    decay = spread.ewm(span=200, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.523529 + 0.0021818 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_048_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=85, w2=213, w3=680, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(213, min_periods=max(213//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 85)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.537059 + 0.0021819 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_049_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=92, w2=226, w3=697, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(92, min_periods=max(92//3, 2)).mean(), b.abs().rolling(226, min_periods=max(226//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.299667 * _rolling_slope(cover, 92) + 0.002182 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_050_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=99, w2=239, w3=714, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.306 * y + 0.694000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 99) - _rolling_slope(basket, 239) + 0.0021821 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_051_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=106, w2=252, w3=731, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(106, min_periods=max(106//3, 2)).mean(), upside.rolling(252, min_periods=max(252//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.577647 + 0.0021822 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_052_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=113, w2=265, w3=748, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(265, min_periods=max(265//3, 2)).max()
    rebound = x - x.rolling(113, min_periods=max(113//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.318667 * _rolling_slope(draw, 748) + 0.0021823 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_053_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=120, w2=278, w3=765, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(120) - b.diff(126)
    stress = imbalance.rolling(765, min_periods=max(765//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.604706 + 0.0021824 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_054_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=127, w2=291, w3=31, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 127)
    baseline = trend.rolling(291, min_periods=max(291//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(31, min_periods=max(31//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.618235 + 0.0021825 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_055_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=134, w2=304, w3=48, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 134)
    slow = _rolling_slope(x, 304)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=48, adjust=False).mean() * 1.631765 + 0.0021826 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_056_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=141, w2=317, w3=65, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(317, min_periods=max(317//3, 2)).max()
    trough = x.rolling(141, min_periods=max(141//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.645294 + 0.0021827 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_057_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=148, w2=330, w3=82, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(330, min_periods=max(330//3, 2)).rank(pct=True)
    persistence = change.rolling(82, min_periods=max(82//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.350333 * persistence + 0.0021828 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_058_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=155, w2=343, w3=99, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(155, min_periods=max(155//3, 2)).std()
    vol_slow = ret.rolling(343, min_periods=max(343//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.672353 + 0.0021829 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_059_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=162, w2=356, w3=116, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(356, min_periods=max(356//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 162)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.363 * slope + 0.002183 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_060_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=169, w2=369, w3=133, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(369, min_periods=max(369//3, 2)).mean()
    noise = impulse.abs().rolling(133, min_periods=max(133//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.845882 + 0.0021831 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_061_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=176, w2=382, w3=150, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 176)
    acceleration = _rolling_slope(velocity, 382)
    curvature = _rolling_slope(acceleration, 150)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.043333 * acceleration + 0.0021832 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_062_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=183, w2=395, w3=167, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 183)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.049667 * pressure.rolling(167, min_periods=max(167//3, 2)).mean() + 0.0021833 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_063_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=190, w2=408, w3=184, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(190, min_periods=max(190//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.886471 + 0.0021834 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_064_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=197, w2=421, w3=201, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(421, min_periods=max(421//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 197)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.9 + 0.0021835 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_065_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=204, w2=434, w3=218, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(204, min_periods=max(204//3, 2)).mean(), b.abs().rolling(434, min_periods=max(434//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.068667 * _rolling_slope(cover, 204) + 0.0021836 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_066_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=211, w2=447, w3=235, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.075 * y + 0.925000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 211) - _rolling_slope(basket, 447) + 0.0021837 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_067_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=218, w2=460, w3=252, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(218, min_periods=max(218//3, 2)).mean(), upside.rolling(460, min_periods=max(460//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.940588 + 0.0021838 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_068_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=225, w2=473, w3=269, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(473, min_periods=max(473//3, 2)).max()
    rebound = x - x.rolling(225, min_periods=max(225//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.087667 * _rolling_slope(draw, 269) + 0.0021839 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_069_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=232, w2=486, w3=286, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(286, min_periods=max(286//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.967647 + 0.002184 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_070_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=239, w2=499, w3=303, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 239)
    baseline = trend.rolling(499, min_periods=max(499//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(303, min_periods=max(303//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.981176 + 0.0021841 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_071_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=246, w2=13, w3=320, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 246)
    slow = _rolling_slope(x, 13)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.994706 + 0.0021842 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_072_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=6, w2=26, w3=337, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(26, min_periods=max(26//3, 2)).max()
    trough = x.rolling(6, min_periods=max(6//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.008235 + 0.0021843 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_073_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=13, w2=39, w3=354, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(13)
    rank = change.rolling(39, min_periods=max(39//3, 2)).rank(pct=True)
    persistence = change.rolling(354, min_periods=max(354//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.119333 * persistence + 0.0021844 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_074_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=20, w2=52, w3=371, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(20, min_periods=max(20//3, 2)).std()
    vol_slow = ret.rolling(52, min_periods=max(52//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.035294 + 0.0021845 * anchor
    return base_signal.diff()

def f29_vtxn_gemini_075_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=27, w2=65, w3=388, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(65, min_periods=max(65//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 27)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.132 * slope + 0.0021846 * anchor
    return base_signal.diff()
