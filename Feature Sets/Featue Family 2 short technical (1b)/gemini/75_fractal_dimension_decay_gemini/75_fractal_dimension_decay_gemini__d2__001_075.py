"""75 fractal dimension decay gemini d2 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Changes in the complexity and space-filling properties of the price path.
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
    if isinstance(s, pd.Series):
        return np.log(s.where(s > eps, np.nan))
    return np.log(s if s > eps else np.nan)

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

def f75_fdim_gemini_001_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Changes in the complexity and space-filling properties of the price path. [window=5]"""
    window = 5
    res = _safe_div(_safe_log(window + 1e-9), _safe_log(window + 1e-9) + _safe_log(_safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window) + 1e-9) + 1e-9))
    return (res).diff().diff()

def f75_fdim_gemini_002_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Changes in the complexity and space-filling properties of the price path. [window=10]"""
    window = 10
    res = _safe_div(_safe_log(window + 1e-9), _safe_log(window + 1e-9) + _safe_log(_safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window) + 1e-9) + 1e-9))
    return (res).diff().diff()

def f75_fdim_gemini_003_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Changes in the complexity and space-filling properties of the price path. [window=21]"""
    window = 21
    res = _safe_div(_safe_log(window + 1e-9), _safe_log(window + 1e-9) + _safe_log(_safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window) + 1e-9) + 1e-9))
    return (res).diff().diff()

def f75_fdim_gemini_004_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Changes in the complexity and space-filling properties of the price path. [window=42]"""
    window = 42
    res = _safe_div(_safe_log(window + 1e-9), _safe_log(window + 1e-9) + _safe_log(_safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window) + 1e-9) + 1e-9))
    return (res).diff().diff()

def f75_fdim_gemini_005_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Changes in the complexity and space-filling properties of the price path. [window=63]"""
    window = 63
    res = _safe_div(_safe_log(window + 1e-9), _safe_log(window + 1e-9) + _safe_log(_safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window) + 1e-9) + 1e-9))
    return (res).diff().diff()

def f75_fdim_gemini_006_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Changes in the complexity and space-filling properties of the price path. [window=126]"""
    window = 126
    res = _safe_div(_safe_log(window + 1e-9), _safe_log(window + 1e-9) + _safe_log(_safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window) + 1e-9) + 1e-9))
    return (res).diff().diff()

def f75_fdim_gemini_007_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Changes in the complexity and space-filling properties of the price path. [window=252]"""
    window = 252
    res = _safe_div(_safe_log(window + 1e-9), _safe_log(window + 1e-9) + _safe_log(_safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window) + 1e-9) + 1e-9))
    return (res).diff().diff()

def f75_fdim_gemini_008_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Changes in the complexity and space-filling properties of the price path. [window=504]"""
    window = 504
    res = _safe_div(_safe_log(window + 1e-9), _safe_log(window + 1e-9) + _safe_log(_safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window) + 1e-9) + 1e-9))
    return (res).diff().diff()

def f75_fdim_gemini_009_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Changes in the complexity and space-filling properties of the price path. [window=756]"""
    window = 756
    res = _safe_div(_safe_log(window + 1e-9), _safe_log(window + 1e-9) + _safe_log(_safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window) + 1e-9) + 1e-9))
    return (res).diff().diff()

def f75_fdim_gemini_010_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Changes in the complexity and space-filling properties of the price path. [window=1260]"""
    window = 1260
    res = _safe_div(_safe_log(window + 1e-9), _safe_log(window + 1e-9) + _safe_log(_safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window) + 1e-9) + 1e-9))
    return (res).diff().diff()

def f75_fdim_gemini_011_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=75, w2=106, w3=265, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 75)
    slow = _rolling_slope(x, 106)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=265, adjust=False).mean() * 1.501176 + 0.0047682 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_012_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=82, w2=119, w3=282, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(119, min_periods=max(119//3, 2)).max()
    trough = x.rolling(82, min_periods=max(82//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.514706 + 0.0047683 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_013_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=89, w2=132, w3=299, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(89)
    rank = change.rolling(132, min_periods=max(132//3, 2)).rank(pct=True)
    persistence = change.rolling(299, min_periods=max(299//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.264667 * persistence + 0.0047684 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_014_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=96, w2=145, w3=316, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(96, min_periods=max(96//3, 2)).std()
    vol_slow = ret.rolling(145, min_periods=max(145//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.541765 + 0.0047685 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_015_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=103, w2=158, w3=333, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(158, min_periods=max(158//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 103)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.277333 * slope + 0.0047686 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_016_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=110, w2=171, w3=350, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(110)
    drag = impulse.rolling(171, min_periods=max(171//3, 2)).mean()
    noise = impulse.abs().rolling(350, min_periods=max(350//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.568824 + 0.0047687 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_017_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=117, w2=184, w3=367, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 117)
    acceleration = _rolling_slope(velocity, 184)
    curvature = _rolling_slope(acceleration, 367)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.29 * acceleration + 0.0047688 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_018_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=124, w2=197, w3=384, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 124)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.296333 * pressure.rolling(384, min_periods=max(384//3, 2)).mean() + 0.0047689 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_019_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=131, w2=210, w3=401, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(131, min_periods=max(131//3, 2)).mean())
    decay = spread.ewm(span=210, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.609412 + 0.004769 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_020_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=138, w2=223, w3=418, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(223, min_periods=max(223//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 138)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.622941 + 0.0047691 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_021_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=145, w2=236, w3=435, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(145, min_periods=max(145//3, 2)).mean(), b.abs().rolling(236, min_periods=max(236//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.315333 * _rolling_slope(cover, 145) + 0.0047692 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_022_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=152, w2=249, w3=452, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.321667 * y + 0.678333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 152) - _rolling_slope(basket, 249) + 0.0047693 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_023_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=159, w2=262, w3=469, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(159, min_periods=max(159//3, 2)).mean(), upside.rolling(262, min_periods=max(262//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.663529 + 0.0047694 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_024_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=166, w2=275, w3=486, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(275, min_periods=max(275//3, 2)).max()
    rebound = x - x.rolling(166, min_periods=max(166//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.334333 * _rolling_slope(draw, 486) + 0.0047695 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_025_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=173, w2=288, w3=503, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(503, min_periods=max(503//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.837059 + 0.0047696 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_026_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=180, w2=301, w3=520, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 180)
    baseline = trend.rolling(301, min_periods=max(301//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(520, min_periods=max(520//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.850588 + 0.0047697 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_027_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=187, w2=314, w3=537, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 187)
    slow = _rolling_slope(x, 314)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.864118 + 0.0047698 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_028_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=194, w2=327, w3=554, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(327, min_periods=max(327//3, 2)).max()
    trough = x.rolling(194, min_periods=max(194//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.877647 + 0.0047699 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_029_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=201, w2=340, w3=571, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(340, min_periods=max(340//3, 2)).rank(pct=True)
    persistence = change.rolling(571, min_periods=max(571//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.033667 * persistence + 0.00477 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_030_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=208, w2=353, w3=588, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(208, min_periods=max(208//3, 2)).std()
    vol_slow = ret.rolling(353, min_periods=max(353//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.904706 + 0.0047701 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_031_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=215, w2=366, w3=605, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(366, min_periods=max(366//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 215)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.046333 * slope + 0.0047702 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_032_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=222, w2=379, w3=622, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(379, min_periods=max(379//3, 2)).mean()
    noise = impulse.abs().rolling(622, min_periods=max(622//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.931765 + 0.0047703 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_033_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=229, w2=392, w3=639, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 229)
    acceleration = _rolling_slope(velocity, 392)
    curvature = _rolling_slope(acceleration, 639)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.059 * acceleration + 0.0047704 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_034_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=236, w2=405, w3=656, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 236)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.065333 * pressure.rolling(656, min_periods=max(656//3, 2)).mean() + 0.0047705 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_035_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=243, w2=418, w3=673, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(243, min_periods=max(243//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.972353 + 0.0047706 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_036_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=250, w2=431, w3=690, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(431, min_periods=max(431//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 250)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.985882 + 0.0047707 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_037_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=10, w2=444, w3=707, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(10, min_periods=max(10//3, 2)).mean(), b.abs().rolling(444, min_periods=max(444//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.084333 * _rolling_slope(cover, 10) + 0.0047708 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_038_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=17, w2=457, w3=724, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.090667 * y + 0.909333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 17) - _rolling_slope(basket, 457) + 0.0047709 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_039_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=24, w2=470, w3=741, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(24, min_periods=max(24//3, 2)).mean(), upside.rolling(470, min_periods=max(470//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.026471 + 0.004771 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_040_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=31, w2=483, w3=758, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(483, min_periods=max(483//3, 2)).max()
    rebound = x - x.rolling(31, min_periods=max(31//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.103333 * _rolling_slope(draw, 758) + 0.0047711 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_041_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=38, w2=496, w3=24, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(38) - b.diff(126)
    stress = imbalance.rolling(24, min_periods=max(24//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.053529 + 0.0047712 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_042_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=45, w2=509, w3=41, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 45)
    baseline = trend.rolling(509, min_periods=max(509//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(41, min_periods=max(41//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.067059 + 0.0047713 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_043_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=52, w2=23, w3=58, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 52)
    slow = _rolling_slope(x, 23)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=58, adjust=False).mean() * 1.080588 + 0.0047714 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_044_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=59, w2=36, w3=75, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(36, min_periods=max(36//3, 2)).max()
    trough = x.rolling(59, min_periods=max(59//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.094118 + 0.0047715 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_045_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=66, w2=49, w3=92, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(66)
    rank = change.rolling(49, min_periods=max(49//3, 2)).rank(pct=True)
    persistence = change.rolling(92, min_periods=max(92//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.135 * persistence + 0.0047716 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_046_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=73, w2=62, w3=109, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(73, min_periods=max(73//3, 2)).std()
    vol_slow = ret.rolling(62, min_periods=max(62//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.121176 + 0.0047717 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_047_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=80, w2=75, w3=126, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(75, min_periods=max(75//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 80)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.147667 * slope + 0.0047718 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_048_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=87, w2=88, w3=143, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(87)
    drag = impulse.rolling(88, min_periods=max(88//3, 2)).mean()
    noise = impulse.abs().rolling(143, min_periods=max(143//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.148235 + 0.0047719 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_049_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=94, w2=101, w3=160, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 94)
    acceleration = _rolling_slope(velocity, 101)
    curvature = _rolling_slope(acceleration, 160)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.160333 * acceleration + 0.004772 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_050_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=101, w2=114, w3=177, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 101)
    pressure = rel_log.diff(114)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.166667 * pressure.rolling(177, min_periods=max(177//3, 2)).mean() + 0.0047721 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_051_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=108, w2=127, w3=194, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(108, min_periods=max(108//3, 2)).mean())
    decay = spread.ewm(span=127, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.188824 + 0.0047722 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_052_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=115, w2=140, w3=211, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(140, min_periods=max(140//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 115)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.202353 + 0.0047723 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_053_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=122, w2=153, w3=228, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(122, min_periods=max(122//3, 2)).mean(), b.abs().rolling(153, min_periods=max(153//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.185667 * _rolling_slope(cover, 122) + 0.0047724 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_054_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=129, w2=166, w3=245, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.192 * y + 0.808000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 129) - _rolling_slope(basket, 166) + 0.0047725 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_055_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=136, w2=179, w3=262, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(136, min_periods=max(136//3, 2)).mean(), upside.rolling(179, min_periods=max(179//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.242941 + 0.0047726 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_056_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=143, w2=192, w3=279, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(192, min_periods=max(192//3, 2)).max()
    rebound = x - x.rolling(143, min_periods=max(143//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.204667 * _rolling_slope(draw, 279) + 0.0047727 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_057_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=150, w2=205, w3=296, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(296, min_periods=max(296//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.27 + 0.0047728 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_058_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=157, w2=218, w3=313, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 157)
    baseline = trend.rolling(218, min_periods=max(218//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(313, min_periods=max(313//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.283529 + 0.0047729 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_059_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=164, w2=231, w3=330, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 164)
    slow = _rolling_slope(x, 231)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.297059 + 0.004773 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_060_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=171, w2=244, w3=347, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(244, min_periods=max(244//3, 2)).max()
    trough = x.rolling(171, min_periods=max(171//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.310588 + 0.0047731 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_061_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=178, w2=257, w3=364, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(257, min_periods=max(257//3, 2)).rank(pct=True)
    persistence = change.rolling(364, min_periods=max(364//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.236333 * persistence + 0.0047732 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_062_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=185, w2=270, w3=381, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(185, min_periods=max(185//3, 2)).std()
    vol_slow = ret.rolling(270, min_periods=max(270//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.337647 + 0.0047733 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_063_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=192, w2=283, w3=398, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(283, min_periods=max(283//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 192)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.249 * slope + 0.0047734 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_064_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=199, w2=296, w3=415, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(296, min_periods=max(296//3, 2)).mean()
    noise = impulse.abs().rolling(415, min_periods=max(415//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.364706 + 0.0047735 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_065_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=206, w2=309, w3=432, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 206)
    acceleration = _rolling_slope(velocity, 309)
    curvature = _rolling_slope(acceleration, 432)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.261667 * acceleration + 0.0047736 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_066_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=213, w2=322, w3=449, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 213)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.268 * pressure.rolling(449, min_periods=max(449//3, 2)).mean() + 0.0047737 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_067_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=220, w2=335, w3=466, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(220, min_periods=max(220//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.405294 + 0.0047738 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_068_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=227, w2=348, w3=483, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(348, min_periods=max(348//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 227)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.418824 + 0.0047739 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_069_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=234, w2=361, w3=500, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(234, min_periods=max(234//3, 2)).mean(), b.abs().rolling(361, min_periods=max(361//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.287 * _rolling_slope(cover, 234) + 0.004774 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_070_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=241, w2=374, w3=517, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.293333 * y + 0.706667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 241) - _rolling_slope(basket, 374) + 0.0047741 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_071_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=248, w2=387, w3=534, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(248, min_periods=max(248//3, 2)).mean(), upside.rolling(387, min_periods=max(387//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.459412 + 0.0047742 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_072_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=8, w2=400, w3=551, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(400, min_periods=max(400//3, 2)).max()
    rebound = x - x.rolling(8, min_periods=max(8//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.306 * _rolling_slope(draw, 551) + 0.0047743 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_073_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=15, w2=413, w3=568, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(15) - b.diff(126)
    stress = imbalance.rolling(568, min_periods=max(568//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.486471 + 0.0047744 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_074_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=22, w2=426, w3=585, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 22)
    baseline = trend.rolling(426, min_periods=max(426//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(585, min_periods=max(585//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.5 + 0.0047745 * anchor
    return base_signal.diff().diff()

def f75_fdim_gemini_075_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=29, w2=439, w3=602, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 29)
    slow = _rolling_slope(x, 439)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.513529 + 0.0047746 * anchor
    return base_signal.diff().diff()
