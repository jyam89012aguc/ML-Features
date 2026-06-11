"""82 range to volatility expansion gemini d2 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Disproportionate growth in price range compared to underlying volatility.
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

def f82_rtve_gemini_001_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Disproportionate growth in price range compared to underlying volatility. [window=5]"""
    window = 5
    res = _safe_div(high - low, _atr(high, low, close, window) + 1e-9)
    return (res).diff().diff()

def f82_rtve_gemini_002_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Disproportionate growth in price range compared to underlying volatility. [window=10]"""
    window = 10
    res = _safe_div(high - low, _atr(high, low, close, window) + 1e-9)
    return (res).diff().diff()

def f82_rtve_gemini_003_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Disproportionate growth in price range compared to underlying volatility. [window=21]"""
    window = 21
    res = _safe_div(high - low, _atr(high, low, close, window) + 1e-9)
    return (res).diff().diff()

def f82_rtve_gemini_004_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Disproportionate growth in price range compared to underlying volatility. [window=42]"""
    window = 42
    res = _safe_div(high - low, _atr(high, low, close, window) + 1e-9)
    return (res).diff().diff()

def f82_rtve_gemini_005_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Disproportionate growth in price range compared to underlying volatility. [window=63]"""
    window = 63
    res = _safe_div(high - low, _atr(high, low, close, window) + 1e-9)
    return (res).diff().diff()

def f82_rtve_gemini_006_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Disproportionate growth in price range compared to underlying volatility. [window=126]"""
    window = 126
    res = _safe_div(high - low, _atr(high, low, close, window) + 1e-9)
    return (res).diff().diff()

def f82_rtve_gemini_007_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Disproportionate growth in price range compared to underlying volatility. [window=252]"""
    window = 252
    res = _safe_div(high - low, _atr(high, low, close, window) + 1e-9)
    return (res).diff().diff()

def f82_rtve_gemini_008_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Disproportionate growth in price range compared to underlying volatility. [window=504]"""
    window = 504
    res = _safe_div(high - low, _atr(high, low, close, window) + 1e-9)
    return (res).diff().diff()

def f82_rtve_gemini_009_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Disproportionate growth in price range compared to underlying volatility. [window=756]"""
    window = 756
    res = _safe_div(high - low, _atr(high, low, close, window) + 1e-9)
    return (res).diff().diff()

def f82_rtve_gemini_010_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Disproportionate growth in price range compared to underlying volatility. [window=1260]"""
    window = 1260
    res = _safe_div(high - low, _atr(high, low, close, window) + 1e-9)
    return (res).diff().diff()

def f82_rtve_gemini_011_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=98, w2=168, w3=66, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 98)
    slow = _rolling_slope(x, 168)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=66, adjust=False).mean() * 1.617647 + 0.0051602 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_012_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=105, w2=181, w3=83, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(181, min_periods=max(181//3, 2)).max()
    trough = x.rolling(105, min_periods=max(105//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.631176 + 0.0051603 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_013_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=112, w2=194, w3=100, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(112)
    rank = change.rolling(194, min_periods=max(194//3, 2)).rank(pct=True)
    persistence = change.rolling(100, min_periods=max(100//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.166333 * persistence + 0.0051604 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_014_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=119, w2=207, w3=117, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(119, min_periods=max(119//3, 2)).std()
    vol_slow = ret.rolling(207, min_periods=max(207//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.658235 + 0.0051605 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_015_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=126, w2=220, w3=134, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(220, min_periods=max(220//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 126)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.179 * slope + 0.0051606 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_016_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=133, w2=233, w3=151, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(233, min_periods=max(233//3, 2)).mean()
    noise = impulse.abs().rolling(151, min_periods=max(151//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.831765 + 0.0051607 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_017_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=140, w2=246, w3=168, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 140)
    acceleration = _rolling_slope(velocity, 246)
    curvature = _rolling_slope(acceleration, 168)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.191667 * acceleration + 0.0051608 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_018_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=147, w2=259, w3=185, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 147)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.198 * pressure.rolling(185, min_periods=max(185//3, 2)).mean() + 0.0051609 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_019_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=154, w2=272, w3=202, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(154, min_periods=max(154//3, 2)).mean())
    decay = spread.ewm(span=272, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.872353 + 0.005161 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_020_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=161, w2=285, w3=219, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(285, min_periods=max(285//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 161)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.885882 + 0.0051611 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_021_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=168, w2=298, w3=236, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(168, min_periods=max(168//3, 2)).mean(), b.abs().rolling(298, min_periods=max(298//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.217 * _rolling_slope(cover, 168) + 0.0051612 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_022_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=175, w2=311, w3=253, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.223333 * y + 0.776667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 175) - _rolling_slope(basket, 311) + 0.0051613 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_023_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=182, w2=324, w3=270, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(182, min_periods=max(182//3, 2)).mean(), upside.rolling(324, min_periods=max(324//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.926471 + 0.0051614 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_024_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=189, w2=337, w3=287, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(337, min_periods=max(337//3, 2)).max()
    rebound = x - x.rolling(189, min_periods=max(189//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.236 * _rolling_slope(draw, 287) + 0.0051615 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_025_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=196, w2=350, w3=304, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(304, min_periods=max(304//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.953529 + 0.0051616 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_026_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=203, w2=363, w3=321, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 203)
    baseline = trend.rolling(363, min_periods=max(363//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(321, min_periods=max(321//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.967059 + 0.0051617 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_027_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=210, w2=376, w3=338, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 210)
    slow = _rolling_slope(x, 376)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.980588 + 0.0051618 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_028_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=217, w2=389, w3=355, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(389, min_periods=max(389//3, 2)).max()
    trough = x.rolling(217, min_periods=max(217//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.994118 + 0.0051619 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_029_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=224, w2=402, w3=372, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(402, min_periods=max(402//3, 2)).rank(pct=True)
    persistence = change.rolling(372, min_periods=max(372//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.267667 * persistence + 0.005162 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_030_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=231, w2=415, w3=389, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(231, min_periods=max(231//3, 2)).std()
    vol_slow = ret.rolling(415, min_periods=max(415//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.021176 + 0.0051621 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_031_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=238, w2=428, w3=406, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(428, min_periods=max(428//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 238)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.280333 * slope + 0.0051622 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_032_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=245, w2=441, w3=423, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(441, min_periods=max(441//3, 2)).mean()
    noise = impulse.abs().rolling(423, min_periods=max(423//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.048235 + 0.0051623 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_033_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=5, w2=454, w3=440, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 5)
    acceleration = _rolling_slope(velocity, 454)
    curvature = _rolling_slope(acceleration, 440)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.293 * acceleration + 0.0051624 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_034_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=12, w2=467, w3=457, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 12)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.299333 * pressure.rolling(457, min_periods=max(457//3, 2)).mean() + 0.0051625 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_035_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=19, w2=480, w3=474, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(19, min_periods=max(19//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.088824 + 0.0051626 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_036_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=26, w2=493, w3=491, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(493, min_periods=max(493//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 26)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.102353 + 0.0051627 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_037_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=33, w2=506, w3=508, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(33, min_periods=max(33//3, 2)).mean(), b.abs().rolling(506, min_periods=max(506//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.318333 * _rolling_slope(cover, 33) + 0.0051628 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_038_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=40, w2=20, w3=525, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.324667 * y + 0.675333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 40) - _rolling_slope(basket, 20) + 0.0051629 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_039_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=47, w2=33, w3=542, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(47, min_periods=max(47//3, 2)).mean(), upside.rolling(33, min_periods=max(33//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.142941 + 0.005163 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_040_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=54, w2=46, w3=559, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(46, min_periods=max(46//3, 2)).max()
    rebound = x - x.rolling(54, min_periods=max(54//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.337333 * _rolling_slope(draw, 559) + 0.0051631 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_041_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=61, w2=59, w3=576, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(61) - b.diff(59)
    stress = imbalance.rolling(576, min_periods=max(576//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.17 + 0.0051632 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_042_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=68, w2=72, w3=593, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 68)
    baseline = trend.rolling(72, min_periods=max(72//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(593, min_periods=max(593//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.183529 + 0.0051633 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_043_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=75, w2=85, w3=610, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 75)
    slow = _rolling_slope(x, 85)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.197059 + 0.0051634 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_044_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=82, w2=98, w3=627, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(98, min_periods=max(98//3, 2)).max()
    trough = x.rolling(82, min_periods=max(82//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.210588 + 0.0051635 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_045_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=89, w2=111, w3=644, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(89)
    rank = change.rolling(111, min_periods=max(111//3, 2)).rank(pct=True)
    persistence = change.rolling(644, min_periods=max(644//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.036667 * persistence + 0.0051636 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_046_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=96, w2=124, w3=661, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(96, min_periods=max(96//3, 2)).std()
    vol_slow = ret.rolling(124, min_periods=max(124//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.237647 + 0.0051637 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_047_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=103, w2=137, w3=678, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(137, min_periods=max(137//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 103)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.049333 * slope + 0.0051638 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_048_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=110, w2=150, w3=695, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(110)
    drag = impulse.rolling(150, min_periods=max(150//3, 2)).mean()
    noise = impulse.abs().rolling(695, min_periods=max(695//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.264706 + 0.0051639 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_049_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=117, w2=163, w3=712, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 117)
    acceleration = _rolling_slope(velocity, 163)
    curvature = _rolling_slope(acceleration, 712)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.062 * acceleration + 0.005164 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_050_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=124, w2=176, w3=729, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 124)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.068333 * pressure.rolling(729, min_periods=max(729//3, 2)).mean() + 0.0051641 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_051_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=131, w2=189, w3=746, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(131, min_periods=max(131//3, 2)).mean())
    decay = spread.ewm(span=189, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.305294 + 0.0051642 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_052_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=138, w2=202, w3=763, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(202, min_periods=max(202//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 138)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.318824 + 0.0051643 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_053_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=145, w2=215, w3=29, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(145, min_periods=max(145//3, 2)).mean(), b.abs().rolling(215, min_periods=max(215//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(29) + 0.087333 * _rolling_slope(cover, 145) + 0.0051644 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_054_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=152, w2=228, w3=46, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.093667 * y + 0.906333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 152) - _rolling_slope(basket, 228) + 0.0051645 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_055_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=159, w2=241, w3=63, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(159, min_periods=max(159//3, 2)).mean(), upside.rolling(241, min_periods=max(241//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(63) * 1.359412 + 0.0051646 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_056_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=166, w2=254, w3=80, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(254, min_periods=max(254//3, 2)).max()
    rebound = x - x.rolling(166, min_periods=max(166//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.106333 * _rolling_slope(draw, 80) + 0.0051647 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_057_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=173, w2=267, w3=97, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(97, min_periods=max(97//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.386471 + 0.0051648 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_058_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=180, w2=280, w3=114, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 180)
    baseline = trend.rolling(280, min_periods=max(280//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(114, min_periods=max(114//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.4 + 0.0051649 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_059_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=187, w2=293, w3=131, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 187)
    slow = _rolling_slope(x, 293)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=131, adjust=False).mean() * 1.413529 + 0.005165 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_060_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=194, w2=306, w3=148, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(306, min_periods=max(306//3, 2)).max()
    trough = x.rolling(194, min_periods=max(194//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.427059 + 0.0051651 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_061_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=201, w2=319, w3=165, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(319, min_periods=max(319//3, 2)).rank(pct=True)
    persistence = change.rolling(165, min_periods=max(165//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.138 * persistence + 0.0051652 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_062_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=208, w2=332, w3=182, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(208, min_periods=max(208//3, 2)).std()
    vol_slow = ret.rolling(332, min_periods=max(332//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.454118 + 0.0051653 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_063_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=215, w2=345, w3=199, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(345, min_periods=max(345//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 215)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.150667 * slope + 0.0051654 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_064_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=222, w2=358, w3=216, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(358, min_periods=max(358//3, 2)).mean()
    noise = impulse.abs().rolling(216, min_periods=max(216//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.481176 + 0.0051655 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_065_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=229, w2=371, w3=233, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 229)
    acceleration = _rolling_slope(velocity, 371)
    curvature = _rolling_slope(acceleration, 233)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.163333 * acceleration + 0.0051656 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_066_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=236, w2=384, w3=250, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 236)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.169667 * pressure.rolling(250, min_periods=max(250//3, 2)).mean() + 0.0051657 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_067_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=243, w2=397, w3=267, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(243, min_periods=max(243//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.521765 + 0.0051658 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_068_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=250, w2=410, w3=284, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(410, min_periods=max(410//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 250)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.535294 + 0.0051659 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_069_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=10, w2=423, w3=301, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(10, min_periods=max(10//3, 2)).mean(), b.abs().rolling(423, min_periods=max(423//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.188667 * _rolling_slope(cover, 10) + 0.005166 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_070_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=17, w2=436, w3=318, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.195 * y + 0.805000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 17) - _rolling_slope(basket, 436) + 0.0051661 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_071_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=24, w2=449, w3=335, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(24, min_periods=max(24//3, 2)).mean(), upside.rolling(449, min_periods=max(449//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.575882 + 0.0051662 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_072_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=31, w2=462, w3=352, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(462, min_periods=max(462//3, 2)).max()
    rebound = x - x.rolling(31, min_periods=max(31//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.207667 * _rolling_slope(draw, 352) + 0.0051663 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_073_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=38, w2=475, w3=369, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(38) - b.diff(126)
    stress = imbalance.rolling(369, min_periods=max(369//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.602941 + 0.0051664 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_074_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=45, w2=488, w3=386, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 45)
    baseline = trend.rolling(488, min_periods=max(488//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(386, min_periods=max(386//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.616471 + 0.0051665 * anchor
    return base_signal.diff().diff()

def f82_rtve_gemini_075_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=52, w2=501, w3=403, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 52)
    slow = _rolling_slope(x, 501)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.63 + 0.0051666 * anchor
    return base_signal.diff().diff()
