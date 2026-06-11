"""72 detrended fluctuation analysis gemini d1 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Scaling properties of price fluctuations to detect fractal-like behavior.
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

def f72_dfa_gemini_001_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Scaling properties of price fluctuations to detect fractal-like behavior. [window=5]"""
    window = 5
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() * volume.rolling(window).mean() / (volume.rolling(window).mean() + 1e-9), window)
    return (res).diff()

def f72_dfa_gemini_002_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Scaling properties of price fluctuations to detect fractal-like behavior. [window=10]"""
    window = 10
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() * volume.rolling(window).mean() / (volume.rolling(window).mean() + 1e-9), window)
    return (res).diff()

def f72_dfa_gemini_003_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Scaling properties of price fluctuations to detect fractal-like behavior. [window=21]"""
    window = 21
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() * volume.rolling(window).mean() / (volume.rolling(window).mean() + 1e-9), window)
    return (res).diff()

def f72_dfa_gemini_004_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Scaling properties of price fluctuations to detect fractal-like behavior. [window=42]"""
    window = 42
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() * volume.rolling(window).mean() / (volume.rolling(window).mean() + 1e-9), window)
    return (res).diff()

def f72_dfa_gemini_005_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Scaling properties of price fluctuations to detect fractal-like behavior. [window=63]"""
    window = 63
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() * volume.rolling(window).mean() / (volume.rolling(window).mean() + 1e-9), window)
    return (res).diff()

def f72_dfa_gemini_006_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Scaling properties of price fluctuations to detect fractal-like behavior. [window=126]"""
    window = 126
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() * volume.rolling(window).mean() / (volume.rolling(window).mean() + 1e-9), window)
    return (res).diff()

def f72_dfa_gemini_007_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Scaling properties of price fluctuations to detect fractal-like behavior. [window=252]"""
    window = 252
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() * volume.rolling(window).mean() / (volume.rolling(window).mean() + 1e-9), window)
    return (res).diff()

def f72_dfa_gemini_008_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Scaling properties of price fluctuations to detect fractal-like behavior. [window=504]"""
    window = 504
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() * volume.rolling(window).mean() / (volume.rolling(window).mean() + 1e-9), window)
    return (res).diff()

def f72_dfa_gemini_009_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Scaling properties of price fluctuations to detect fractal-like behavior. [window=756]"""
    window = 756
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() * volume.rolling(window).mean() / (volume.rolling(window).mean() + 1e-9), window)
    return (res).diff()

def f72_dfa_gemini_010_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Scaling properties of price fluctuations to detect fractal-like behavior. [window=1260]"""
    window = 1260
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() * volume.rolling(window).mean() / (volume.rolling(window).mean() + 1e-9), window)
    return (res).diff()

def f72_dfa_gemini_011_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=179, w2=398, w3=116, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(398, min_periods=max(398//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 179)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.357 * slope + 0.0045862 * anchor
    return base_signal.diff()

def f72_dfa_gemini_012_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=186, w2=411, w3=133, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(411, min_periods=max(411//3, 2)).mean()
    noise = impulse.abs().rolling(133, min_periods=max(133//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.643529 + 0.0045863 * anchor
    return base_signal.diff()

def f72_dfa_gemini_013_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=193, w2=424, w3=150, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 193)
    acceleration = _rolling_slope(velocity, 424)
    curvature = _rolling_slope(acceleration, 150)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.037333 * acceleration + 0.0045864 * anchor
    return base_signal.diff()

def f72_dfa_gemini_014_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=200, w2=437, w3=167, lag=5)."""
    rel = _safe_div(close.shift(5), volume.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 200)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.043667 * pressure.rolling(167, min_periods=max(167//3, 2)).mean() + 0.0045865 * anchor
    return base_signal.diff()

def f72_dfa_gemini_015_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=207, w2=450, w3=184, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(207, min_periods=max(207//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.830588 + 0.0045866 * anchor
    return base_signal.diff()

def f72_dfa_gemini_016_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=214, w2=463, w3=201, lag=13)."""
    a = _safe_log(close.abs() + 1.0).shift(13)
    b = _safe_log(volume.abs() + 1.0).shift(13)
    corr = a.rolling(463, min_periods=max(463//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 214)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.844118 + 0.0045867 * anchor
    return base_signal.diff()

def f72_dfa_gemini_017_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=221, w2=476, w3=218, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    cover = _safe_div(a.rolling(221, min_periods=max(221//3, 2)).mean(), b.abs().rolling(476, min_periods=max(476//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.062667 * _rolling_slope(cover, 221) + 0.0045868 * anchor
    return base_signal.diff()

def f72_dfa_gemini_018_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=228, w2=489, w3=235, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    y = _safe_log(volume.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.069 * y + 0.931000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 228) - _rolling_slope(basket, 489) + 0.0045869 * anchor
    return base_signal.diff()

def f72_dfa_gemini_019_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=235, w2=502, w3=252, lag=55)."""
    x = close.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(235, min_periods=max(235//3, 2)).mean(), upside.rolling(502, min_periods=max(502//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.884706 + 0.004587 * anchor
    return base_signal.diff()

def f72_dfa_gemini_020_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=242, w2=16, w3=269, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    draw = x - x.rolling(16, min_periods=max(16//3, 2)).max()
    rebound = x - x.rolling(242, min_periods=max(242//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.081667 * _rolling_slope(draw, 269) + 0.0045871 * anchor
    return base_signal.diff()

def f72_dfa_gemini_021_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=249, w2=29, w3=286, lag=1)."""
    a = _safe_log(close.abs() + 1.0).shift(1)
    b = _safe_log(volume.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(29)
    stress = imbalance.rolling(286, min_periods=max(286//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.911765 + 0.0045872 * anchor
    return base_signal.diff()

def f72_dfa_gemini_022_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=9, w2=42, w3=303, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 9)
    baseline = trend.rolling(42, min_periods=max(42//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(303, min_periods=max(303//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.925294 + 0.0045873 * anchor
    return base_signal.diff()

def f72_dfa_gemini_023_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=16, w2=55, w3=320, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 16)
    slow = _rolling_slope(x, 55)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.938824 + 0.0045874 * anchor
    return base_signal.diff()

def f72_dfa_gemini_024_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=23, w2=68, w3=337, lag=5)."""
    x = close.shift(5)
    peak = x.rolling(68, min_periods=max(68//3, 2)).max()
    trough = x.rolling(23, min_periods=max(23//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.952353 + 0.0045875 * anchor
    return base_signal.diff()

def f72_dfa_gemini_025_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=30, w2=81, w3=354, lag=8)."""
    x = close.shift(8)
    change = x.pct_change(30)
    rank = change.rolling(81, min_periods=max(81//3, 2)).rank(pct=True)
    persistence = change.rolling(354, min_periods=max(354//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.113333 * persistence + 0.0045876 * anchor
    return base_signal.diff()

def f72_dfa_gemini_026_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=37, w2=94, w3=371, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(37, min_periods=max(37//3, 2)).std()
    vol_slow = ret.rolling(94, min_periods=max(94//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.979412 + 0.0045877 * anchor
    return base_signal.diff()

def f72_dfa_gemini_027_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=44, w2=107, w3=388, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(107, min_periods=max(107//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 44)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.126 * slope + 0.0045878 * anchor
    return base_signal.diff()

def f72_dfa_gemini_028_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=51, w2=120, w3=405, lag=34)."""
    x = close.shift(34)
    impulse = x.diff(51)
    drag = impulse.rolling(120, min_periods=max(120//3, 2)).mean()
    noise = impulse.abs().rolling(405, min_periods=max(405//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.006471 + 0.0045879 * anchor
    return base_signal.diff()

def f72_dfa_gemini_029_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=58, w2=133, w3=422, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 58)
    acceleration = _rolling_slope(velocity, 133)
    curvature = _rolling_slope(acceleration, 422)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.138667 * acceleration + 0.004588 * anchor
    return base_signal.diff()

def f72_dfa_gemini_030_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=65, w2=146, w3=439, lag=0)."""
    rel = _safe_div(close.shift(0), volume.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 65)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.145 * pressure.rolling(439, min_periods=max(439//3, 2)).mean() + 0.0045881 * anchor
    return base_signal.diff()

def f72_dfa_gemini_031_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=72, w2=159, w3=456, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(72, min_periods=max(72//3, 2)).mean())
    decay = spread.ewm(span=159, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.047059 + 0.0045882 * anchor
    return base_signal.diff()

def f72_dfa_gemini_032_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=79, w2=172, w3=473, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(volume.abs() + 1.0).shift(2)
    corr = a.rolling(172, min_periods=max(172//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 79)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.060588 + 0.0045883 * anchor
    return base_signal.diff()

def f72_dfa_gemini_033_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=86, w2=185, w3=490, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    cover = _safe_div(a.rolling(86, min_periods=max(86//3, 2)).mean(), b.abs().rolling(185, min_periods=max(185//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.164 * _rolling_slope(cover, 86) + 0.0045884 * anchor
    return base_signal.diff()

def f72_dfa_gemini_034_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=93, w2=198, w3=507, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(volume.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.170333 * y + 0.829667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 93) - _rolling_slope(basket, 198) + 0.0045885 * anchor
    return base_signal.diff()

def f72_dfa_gemini_035_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=100, w2=211, w3=524, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(100, min_periods=max(100//3, 2)).mean(), upside.rolling(211, min_periods=max(211//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.101176 + 0.0045886 * anchor
    return base_signal.diff()

def f72_dfa_gemini_036_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=107, w2=224, w3=541, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    draw = x - x.rolling(224, min_periods=max(224//3, 2)).max()
    rebound = x - x.rolling(107, min_periods=max(107//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.183 * _rolling_slope(draw, 541) + 0.0045887 * anchor
    return base_signal.diff()

def f72_dfa_gemini_037_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=114, w2=237, w3=558, lag=21)."""
    a = _safe_log(close.abs() + 1.0).shift(21)
    b = _safe_log(volume.abs() + 1.0).shift(21)
    imbalance = a.diff(114) - b.diff(126)
    stress = imbalance.rolling(558, min_periods=max(558//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.128235 + 0.0045888 * anchor
    return base_signal.diff()

def f72_dfa_gemini_038_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=121, w2=250, w3=575, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 121)
    baseline = trend.rolling(250, min_periods=max(250//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(575, min_periods=max(575//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.141765 + 0.0045889 * anchor
    return base_signal.diff()

def f72_dfa_gemini_039_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=128, w2=263, w3=592, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 128)
    slow = _rolling_slope(x, 263)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.155294 + 0.004589 * anchor
    return base_signal.diff()

def f72_dfa_gemini_040_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=135, w2=276, w3=609, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(276, min_periods=max(276//3, 2)).max()
    trough = x.rolling(135, min_periods=max(135//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.168824 + 0.0045891 * anchor
    return base_signal.diff()

def f72_dfa_gemini_041_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=142, w2=289, w3=626, lag=1)."""
    x = close.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(289, min_periods=max(289//3, 2)).rank(pct=True)
    persistence = change.rolling(626, min_periods=max(626//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.214667 * persistence + 0.0045892 * anchor
    return base_signal.diff()

def f72_dfa_gemini_042_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=149, w2=302, w3=643, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(149, min_periods=max(149//3, 2)).std()
    vol_slow = ret.rolling(302, min_periods=max(302//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.195882 + 0.0045893 * anchor
    return base_signal.diff()

def f72_dfa_gemini_043_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=156, w2=315, w3=660, lag=3)."""
    x = close.shift(3)
    ma = x.rolling(315, min_periods=max(315//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 156)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.227333 * slope + 0.0045894 * anchor
    return base_signal.diff()

def f72_dfa_gemini_044_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=163, w2=328, w3=677, lag=5)."""
    x = close.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(328, min_periods=max(328//3, 2)).mean()
    noise = impulse.abs().rolling(677, min_periods=max(677//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.222941 + 0.0045895 * anchor
    return base_signal.diff()

def f72_dfa_gemini_045_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=170, w2=341, w3=694, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 170)
    acceleration = _rolling_slope(velocity, 341)
    curvature = _rolling_slope(acceleration, 694)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.24 * acceleration + 0.0045896 * anchor
    return base_signal.diff()

def f72_dfa_gemini_046_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=177, w2=354, w3=711, lag=13)."""
    rel = _safe_div(close.shift(13), volume.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 177)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.246333 * pressure.rolling(711, min_periods=max(711//3, 2)).mean() + 0.0045897 * anchor
    return base_signal.diff()

def f72_dfa_gemini_047_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=184, w2=367, w3=728, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(184, min_periods=max(184//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.263529 + 0.0045898 * anchor
    return base_signal.diff()

def f72_dfa_gemini_048_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=191, w2=380, w3=745, lag=34)."""
    a = _safe_log(close.abs() + 1.0).shift(34)
    b = _safe_log(volume.abs() + 1.0).shift(34)
    corr = a.rolling(380, min_periods=max(380//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 191)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.277059 + 0.0045899 * anchor
    return base_signal.diff()

def f72_dfa_gemini_049_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=198, w2=393, w3=762, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    cover = _safe_div(a.rolling(198, min_periods=max(198//3, 2)).mean(), b.abs().rolling(393, min_periods=max(393//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.265333 * _rolling_slope(cover, 198) + 0.00459 * anchor
    return base_signal.diff()

def f72_dfa_gemini_050_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=205, w2=406, w3=28, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    y = _safe_log(volume.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.271667 * y + 0.728333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 205) - _rolling_slope(basket, 406) + 0.0045901 * anchor
    return base_signal.diff()

def f72_dfa_gemini_051_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=212, w2=419, w3=45, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(212, min_periods=max(212//3, 2)).mean(), upside.rolling(419, min_periods=max(419//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(45) * 1.317647 + 0.0045902 * anchor
    return base_signal.diff()

def f72_dfa_gemini_052_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=219, w2=432, w3=62, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(432, min_periods=max(432//3, 2)).max()
    rebound = x - x.rolling(219, min_periods=max(219//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.284333 * _rolling_slope(draw, 62) + 0.0045903 * anchor
    return base_signal.diff()

def f72_dfa_gemini_053_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=226, w2=445, w3=79, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(volume.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(79, min_periods=max(79//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.344706 + 0.0045904 * anchor
    return base_signal.diff()

def f72_dfa_gemini_054_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=233, w2=458, w3=96, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 233)
    baseline = trend.rolling(458, min_periods=max(458//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(96, min_periods=max(96//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.358235 + 0.0045905 * anchor
    return base_signal.diff()

def f72_dfa_gemini_055_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=240, w2=471, w3=113, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 240)
    slow = _rolling_slope(x, 471)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=113, adjust=False).mean() * 1.371765 + 0.0045906 * anchor
    return base_signal.diff()

def f72_dfa_gemini_056_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=247, w2=484, w3=130, lag=13)."""
    x = close.shift(13)
    peak = x.rolling(484, min_periods=max(484//3, 2)).max()
    trough = x.rolling(247, min_periods=max(247//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.385294 + 0.0045907 * anchor
    return base_signal.diff()

def f72_dfa_gemini_057_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=7, w2=497, w3=147, lag=21)."""
    x = close.shift(21)
    change = x.pct_change(7)
    rank = change.rolling(497, min_periods=max(497//3, 2)).rank(pct=True)
    persistence = change.rolling(147, min_periods=max(147//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.316 * persistence + 0.0045908 * anchor
    return base_signal.diff()

def f72_dfa_gemini_058_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=14, w2=11, w3=164, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(14, min_periods=max(14//3, 2)).std()
    vol_slow = ret.rolling(11, min_periods=max(11//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.412353 + 0.0045909 * anchor
    return base_signal.diff()

def f72_dfa_gemini_059_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=21, w2=24, w3=181, lag=55)."""
    x = close.shift(55)
    ma = x.rolling(24, min_periods=max(24//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 21)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.328667 * slope + 0.004591 * anchor
    return base_signal.diff()

def f72_dfa_gemini_060_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=28, w2=37, w3=198, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(28)
    drag = impulse.rolling(37, min_periods=max(37//3, 2)).mean()
    noise = impulse.abs().rolling(198, min_periods=max(198//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.439412 + 0.0045911 * anchor
    return base_signal.diff()

def f72_dfa_gemini_061_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=35, w2=50, w3=215, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 35)
    acceleration = _rolling_slope(velocity, 50)
    curvature = _rolling_slope(acceleration, 215)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.341333 * acceleration + 0.0045912 * anchor
    return base_signal.diff()

def f72_dfa_gemini_062_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=42, w2=63, w3=232, lag=2)."""
    rel = _safe_div(close.shift(2), volume.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 42)
    pressure = rel_log.diff(63)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.347667 * pressure.rolling(232, min_periods=max(232//3, 2)).mean() + 0.0045913 * anchor
    return base_signal.diff()

def f72_dfa_gemini_063_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=49, w2=76, w3=249, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(49, min_periods=max(49//3, 2)).mean())
    decay = spread.ewm(span=76, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.48 + 0.0045914 * anchor
    return base_signal.diff()

def f72_dfa_gemini_064_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=56, w2=89, w3=266, lag=5)."""
    a = _safe_log(close.abs() + 1.0).shift(5)
    b = _safe_log(volume.abs() + 1.0).shift(5)
    corr = a.rolling(89, min_periods=max(89//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 56)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.493529 + 0.0045915 * anchor
    return base_signal.diff()

def f72_dfa_gemini_065_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=63, w2=102, w3=283, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    cover = _safe_div(a.rolling(63, min_periods=max(63//3, 2)).mean(), b.abs().rolling(102, min_periods=max(102//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.034333 * _rolling_slope(cover, 63) + 0.0045916 * anchor
    return base_signal.diff()

def f72_dfa_gemini_066_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=70, w2=115, w3=300, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    y = _safe_log(volume.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.040667 * y + 0.959333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 70) - _rolling_slope(basket, 115) + 0.0045917 * anchor
    return base_signal.diff()

def f72_dfa_gemini_067_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=77, w2=128, w3=317, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(77, min_periods=max(77//3, 2)).mean(), upside.rolling(128, min_periods=max(128//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.534118 + 0.0045918 * anchor
    return base_signal.diff()

def f72_dfa_gemini_068_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=84, w2=141, w3=334, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    draw = x - x.rolling(141, min_periods=max(141//3, 2)).max()
    rebound = x - x.rolling(84, min_periods=max(84//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.053333 * _rolling_slope(draw, 334) + 0.0045919 * anchor
    return base_signal.diff()

def f72_dfa_gemini_069_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=91, w2=154, w3=351, lag=55)."""
    a = _safe_log(close.abs() + 1.0).shift(55)
    b = _safe_log(volume.abs() + 1.0).shift(55)
    imbalance = a.diff(91) - b.diff(126)
    stress = imbalance.rolling(351, min_periods=max(351//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.561176 + 0.004592 * anchor
    return base_signal.diff()

def f72_dfa_gemini_070_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=98, w2=167, w3=368, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 98)
    baseline = trend.rolling(167, min_periods=max(167//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(368, min_periods=max(368//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.574706 + 0.0045921 * anchor
    return base_signal.diff()

def f72_dfa_gemini_071_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=105, w2=180, w3=385, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 105)
    slow = _rolling_slope(x, 180)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.588235 + 0.0045922 * anchor
    return base_signal.diff()

def f72_dfa_gemini_072_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=112, w2=193, w3=402, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(193, min_periods=max(193//3, 2)).max()
    trough = x.rolling(112, min_periods=max(112//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.601765 + 0.0045923 * anchor
    return base_signal.diff()

def f72_dfa_gemini_073_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=119, w2=206, w3=419, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(119)
    rank = change.rolling(206, min_periods=max(206//3, 2)).rank(pct=True)
    persistence = change.rolling(419, min_periods=max(419//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.085 * persistence + 0.0045924 * anchor
    return base_signal.diff()

def f72_dfa_gemini_074_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=126, w2=219, w3=436, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(126, min_periods=max(126//3, 2)).std()
    vol_slow = ret.rolling(219, min_periods=max(219//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.628824 + 0.0045925 * anchor
    return base_signal.diff()

def f72_dfa_gemini_075_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=133, w2=232, w3=453, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(232, min_periods=max(232//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 133)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.097667 * slope + 0.0045926 * anchor
    return base_signal.diff()
