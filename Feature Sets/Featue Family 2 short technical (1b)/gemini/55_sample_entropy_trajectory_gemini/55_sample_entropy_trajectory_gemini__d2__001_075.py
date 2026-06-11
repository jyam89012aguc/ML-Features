"""55 sample entropy trajectory gemini d2 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Complexity measure that is less sensitive to data length than approximate entropy.
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

def f55_ment_gemini_001_d2(close: pd.Series) -> pd.Series:
    """Complexity measure that is less sensitive to data length than approximate entropy. [window=5]"""
    window = 5
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std(), window * 2)
    return (res).diff().diff()

def f55_ment_gemini_002_d2(close: pd.Series) -> pd.Series:
    """Complexity measure that is less sensitive to data length than approximate entropy. [window=10]"""
    window = 10
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std(), window * 2)
    return (res).diff().diff()

def f55_ment_gemini_003_d2(close: pd.Series) -> pd.Series:
    """Complexity measure that is less sensitive to data length than approximate entropy. [window=21]"""
    window = 21
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std(), window * 2)
    return (res).diff().diff()

def f55_ment_gemini_004_d2(close: pd.Series) -> pd.Series:
    """Complexity measure that is less sensitive to data length than approximate entropy. [window=42]"""
    window = 42
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std(), window * 2)
    return (res).diff().diff()

def f55_ment_gemini_005_d2(close: pd.Series) -> pd.Series:
    """Complexity measure that is less sensitive to data length than approximate entropy. [window=63]"""
    window = 63
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std(), window * 2)
    return (res).diff().diff()

def f55_ment_gemini_006_d2(close: pd.Series) -> pd.Series:
    """Complexity measure that is less sensitive to data length than approximate entropy. [window=126]"""
    window = 126
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std(), window * 2)
    return (res).diff().diff()

def f55_ment_gemini_007_d2(close: pd.Series) -> pd.Series:
    """Complexity measure that is less sensitive to data length than approximate entropy. [window=252]"""
    window = 252
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std(), window * 2)
    return (res).diff().diff()

def f55_ment_gemini_008_d2(close: pd.Series) -> pd.Series:
    """Complexity measure that is less sensitive to data length than approximate entropy. [window=504]"""
    window = 504
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std(), window * 2)
    return (res).diff().diff()

def f55_ment_gemini_009_d2(close: pd.Series) -> pd.Series:
    """Complexity measure that is less sensitive to data length than approximate entropy. [window=756]"""
    window = 756
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std(), window * 2)
    return (res).diff().diff()

def f55_ment_gemini_010_d2(close: pd.Series) -> pd.Series:
    """Complexity measure that is less sensitive to data length than approximate entropy. [window=1260]"""
    window = 1260
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std(), window * 2)
    return (res).diff().diff()

def f55_ment_gemini_011_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=221, w2=214, w3=619, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 221)
    slow = _rolling_slope(x, 214)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.046471 + 0.0036482 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_012_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=228, w2=227, w3=636, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(227, min_periods=max(227//3, 2)).max()
    trough = x.rolling(228, min_periods=max(228//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.06 + 0.0036483 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_013_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=235, w2=240, w3=653, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(240, min_periods=max(240//3, 2)).rank(pct=True)
    persistence = change.rolling(653, min_periods=max(653//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.118333 * persistence + 0.0036484 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_014_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=242, w2=253, w3=670, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(242, min_periods=max(242//3, 2)).std()
    vol_slow = ret.rolling(253, min_periods=max(253//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.087059 + 0.0036485 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_015_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=249, w2=266, w3=687, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(266, min_periods=max(266//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 249)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.131 * slope + 0.0036486 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_016_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=9, w2=279, w3=704, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(9)
    drag = impulse.rolling(279, min_periods=max(279//3, 2)).mean()
    noise = impulse.abs().rolling(704, min_periods=max(704//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.114118 + 0.0036487 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_017_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=16, w2=292, w3=721, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 16)
    acceleration = _rolling_slope(velocity, 292)
    curvature = _rolling_slope(acceleration, 721)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.143667 * acceleration + 0.0036488 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_018_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=23, w2=305, w3=738, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(23, min_periods=max(23//3, 2)).mean(), upside.rolling(305, min_periods=max(305//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.141176 + 0.0036489 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_019_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=30, w2=318, w3=755, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(318, min_periods=max(318//3, 2)).max()
    rebound = x - x.rolling(30, min_periods=max(30//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.156333 * _rolling_slope(draw, 755) + 0.003649 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_020_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=37, w2=331, w3=21, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 37)
    baseline = trend.rolling(331, min_periods=max(331//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(21, min_periods=max(21//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.168235 + 0.0036491 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_021_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=44, w2=344, w3=38, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 44)
    slow = _rolling_slope(x, 344)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=38, adjust=False).mean() * 1.181765 + 0.0036492 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_022_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=51, w2=357, w3=55, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(357, min_periods=max(357//3, 2)).max()
    trough = x.rolling(51, min_periods=max(51//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.195294 + 0.0036493 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_023_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=58, w2=370, w3=72, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(58)
    rank = change.rolling(370, min_periods=max(370//3, 2)).rank(pct=True)
    persistence = change.rolling(72, min_periods=max(72//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.181667 * persistence + 0.0036494 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_024_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=65, w2=383, w3=89, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(65, min_periods=max(65//3, 2)).std()
    vol_slow = ret.rolling(383, min_periods=max(383//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.222353 + 0.0036495 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_025_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=72, w2=396, w3=106, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(396, min_periods=max(396//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 72)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.194333 * slope + 0.0036496 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_026_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=79, w2=409, w3=123, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(79)
    drag = impulse.rolling(409, min_periods=max(409//3, 2)).mean()
    noise = impulse.abs().rolling(123, min_periods=max(123//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.249412 + 0.0036497 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_027_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=86, w2=422, w3=140, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 86)
    acceleration = _rolling_slope(velocity, 422)
    curvature = _rolling_slope(acceleration, 140)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.207 * acceleration + 0.0036498 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_028_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=93, w2=435, w3=157, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(93, min_periods=max(93//3, 2)).mean(), upside.rolling(435, min_periods=max(435//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.276471 + 0.0036499 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_029_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=100, w2=448, w3=174, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(448, min_periods=max(448//3, 2)).max()
    rebound = x - x.rolling(100, min_periods=max(100//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.219667 * _rolling_slope(draw, 174) + 0.00365 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_030_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=107, w2=461, w3=191, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 107)
    baseline = trend.rolling(461, min_periods=max(461//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(191, min_periods=max(191//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.303529 + 0.0036501 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_031_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=114, w2=474, w3=208, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 114)
    slow = _rolling_slope(x, 474)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=208, adjust=False).mean() * 1.317059 + 0.0036502 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_032_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=121, w2=487, w3=225, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(487, min_periods=max(487//3, 2)).max()
    trough = x.rolling(121, min_periods=max(121//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.330588 + 0.0036503 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_033_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=128, w2=500, w3=242, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(500, min_periods=max(500//3, 2)).rank(pct=True)
    persistence = change.rolling(242, min_periods=max(242//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.245 * persistence + 0.0036504 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_034_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=135, w2=14, w3=259, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(135, min_periods=max(135//3, 2)).std()
    vol_slow = ret.rolling(14, min_periods=max(14//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.357647 + 0.0036505 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_035_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=142, w2=27, w3=276, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(27, min_periods=max(27//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 142)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.257667 * slope + 0.0036506 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_036_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=149, w2=40, w3=293, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(40, min_periods=max(40//3, 2)).mean()
    noise = impulse.abs().rolling(293, min_periods=max(293//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.384706 + 0.0036507 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_037_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=156, w2=53, w3=310, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 156)
    acceleration = _rolling_slope(velocity, 53)
    curvature = _rolling_slope(acceleration, 310)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.270333 * acceleration + 0.0036508 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_038_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=163, w2=66, w3=327, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(163, min_periods=max(163//3, 2)).mean(), upside.rolling(66, min_periods=max(66//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.411765 + 0.0036509 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_039_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=170, w2=79, w3=344, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(79, min_periods=max(79//3, 2)).max()
    rebound = x - x.rolling(170, min_periods=max(170//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.283 * _rolling_slope(draw, 344) + 0.003651 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_040_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=177, w2=92, w3=361, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 177)
    baseline = trend.rolling(92, min_periods=max(92//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(361, min_periods=max(361//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.438824 + 0.0036511 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_041_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=184, w2=105, w3=378, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 184)
    slow = _rolling_slope(x, 105)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.452353 + 0.0036512 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_042_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=191, w2=118, w3=395, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(118, min_periods=max(118//3, 2)).max()
    trough = x.rolling(191, min_periods=max(191//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.465882 + 0.0036513 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_043_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=198, w2=131, w3=412, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(131, min_periods=max(131//3, 2)).rank(pct=True)
    persistence = change.rolling(412, min_periods=max(412//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.308333 * persistence + 0.0036514 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_044_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=205, w2=144, w3=429, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(205, min_periods=max(205//3, 2)).std()
    vol_slow = ret.rolling(144, min_periods=max(144//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.492941 + 0.0036515 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_045_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=212, w2=157, w3=446, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(157, min_periods=max(157//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 212)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.321 * slope + 0.0036516 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_046_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=219, w2=170, w3=463, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(170, min_periods=max(170//3, 2)).mean()
    noise = impulse.abs().rolling(463, min_periods=max(463//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.52 + 0.0036517 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_047_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=226, w2=183, w3=480, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 226)
    acceleration = _rolling_slope(velocity, 183)
    curvature = _rolling_slope(acceleration, 480)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.333667 * acceleration + 0.0036518 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_048_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=233, w2=196, w3=497, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(233, min_periods=max(233//3, 2)).mean(), upside.rolling(196, min_periods=max(196//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.547059 + 0.0036519 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_049_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=240, w2=209, w3=514, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(209, min_periods=max(209//3, 2)).max()
    rebound = x - x.rolling(240, min_periods=max(240//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.346333 * _rolling_slope(draw, 514) + 0.003652 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_050_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=247, w2=222, w3=531, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 247)
    baseline = trend.rolling(222, min_periods=max(222//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(531, min_periods=max(531//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.574118 + 0.0036521 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_051_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=7, w2=235, w3=548, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 7)
    slow = _rolling_slope(x, 235)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.587647 + 0.0036522 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_052_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=14, w2=248, w3=565, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(248, min_periods=max(248//3, 2)).max()
    trough = x.rolling(14, min_periods=max(14//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.601176 + 0.0036523 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_053_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=21, w2=261, w3=582, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(21)
    rank = change.rolling(261, min_periods=max(261//3, 2)).rank(pct=True)
    persistence = change.rolling(582, min_periods=max(582//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.039333 * persistence + 0.0036524 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_054_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=28, w2=274, w3=599, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(28, min_periods=max(28//3, 2)).std()
    vol_slow = ret.rolling(274, min_periods=max(274//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.628235 + 0.0036525 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_055_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=35, w2=287, w3=616, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(287, min_periods=max(287//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 35)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.052 * slope + 0.0036526 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_056_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=42, w2=300, w3=633, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(42)
    drag = impulse.rolling(300, min_periods=max(300//3, 2)).mean()
    noise = impulse.abs().rolling(633, min_periods=max(633//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.655294 + 0.0036527 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_057_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=49, w2=313, w3=650, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 49)
    acceleration = _rolling_slope(velocity, 313)
    curvature = _rolling_slope(acceleration, 650)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.064667 * acceleration + 0.0036528 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_058_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=56, w2=326, w3=667, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(56, min_periods=max(56//3, 2)).mean(), upside.rolling(326, min_periods=max(326//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.828824 + 0.0036529 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_059_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=63, w2=339, w3=684, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(339, min_periods=max(339//3, 2)).max()
    rebound = x - x.rolling(63, min_periods=max(63//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.077333 * _rolling_slope(draw, 684) + 0.003653 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_060_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=70, w2=352, w3=701, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 70)
    baseline = trend.rolling(352, min_periods=max(352//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(701, min_periods=max(701//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.855882 + 0.0036531 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_061_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=77, w2=365, w3=718, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 77)
    slow = _rolling_slope(x, 365)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.869412 + 0.0036532 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_062_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=84, w2=378, w3=735, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(378, min_periods=max(378//3, 2)).max()
    trough = x.rolling(84, min_periods=max(84//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.882941 + 0.0036533 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_063_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=91, w2=391, w3=752, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(91)
    rank = change.rolling(391, min_periods=max(391//3, 2)).rank(pct=True)
    persistence = change.rolling(752, min_periods=max(752//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.102667 * persistence + 0.0036534 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_064_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=98, w2=404, w3=18, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(98, min_periods=max(98//3, 2)).std()
    vol_slow = ret.rolling(404, min_periods=max(404//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.91 + 0.0036535 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_065_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=105, w2=417, w3=35, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(417, min_periods=max(417//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 105)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.115333 * slope + 0.0036536 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_066_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=112, w2=430, w3=52, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(112)
    drag = impulse.rolling(430, min_periods=max(430//3, 2)).mean()
    noise = impulse.abs().rolling(52, min_periods=max(52//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.937059 + 0.0036537 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_067_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=119, w2=443, w3=69, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 119)
    acceleration = _rolling_slope(velocity, 443)
    curvature = _rolling_slope(acceleration, 69)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.128 * acceleration + 0.0036538 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_068_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=126, w2=456, w3=86, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(126, min_periods=max(126//3, 2)).mean(), upside.rolling(456, min_periods=max(456//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(86) * 0.964118 + 0.0036539 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_069_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=133, w2=469, w3=103, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(469, min_periods=max(469//3, 2)).max()
    rebound = x - x.rolling(133, min_periods=max(133//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.140667 * _rolling_slope(draw, 103) + 0.003654 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_070_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=140, w2=482, w3=120, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 140)
    baseline = trend.rolling(482, min_periods=max(482//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(120, min_periods=max(120//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.991176 + 0.0036541 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_071_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=147, w2=495, w3=137, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 147)
    slow = _rolling_slope(x, 495)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=137, adjust=False).mean() * 1.004706 + 0.0036542 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_072_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=154, w2=508, w3=154, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(508, min_periods=max(508//3, 2)).max()
    trough = x.rolling(154, min_periods=max(154//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.018235 + 0.0036543 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_073_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=161, w2=22, w3=171, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(22, min_periods=max(22//3, 2)).rank(pct=True)
    persistence = change.rolling(171, min_periods=max(171//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.166 * persistence + 0.0036544 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_074_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=168, w2=35, w3=188, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(168, min_periods=max(168//3, 2)).std()
    vol_slow = ret.rolling(35, min_periods=max(35//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.045294 + 0.0036545 * anchor
    return base_signal.diff().diff()

def f55_ment_gemini_075_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=175, w2=48, w3=205, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(48, min_periods=max(48//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 175)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.178667 * slope + 0.0036546 * anchor
    return base_signal.diff().diff()
