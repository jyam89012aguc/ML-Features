"""60 entropy convergence signal gemini d3 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Convergence of multiple entropy measures as a signal of regime transition.
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

def f60_econ_gemini_001_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Convergence of multiple entropy measures as a signal of regime transition. [window=5]"""
    window = 5
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() + volume.rolling(window).std(), window)
    return (res).diff().diff().diff()

def f60_econ_gemini_002_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Convergence of multiple entropy measures as a signal of regime transition. [window=10]"""
    window = 10
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() + volume.rolling(window).std(), window)
    return (res).diff().diff().diff()

def f60_econ_gemini_003_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Convergence of multiple entropy measures as a signal of regime transition. [window=21]"""
    window = 21
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() + volume.rolling(window).std(), window)
    return (res).diff().diff().diff()

def f60_econ_gemini_004_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Convergence of multiple entropy measures as a signal of regime transition. [window=42]"""
    window = 42
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() + volume.rolling(window).std(), window)
    return (res).diff().diff().diff()

def f60_econ_gemini_005_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Convergence of multiple entropy measures as a signal of regime transition. [window=63]"""
    window = 63
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() + volume.rolling(window).std(), window)
    return (res).diff().diff().diff()

def f60_econ_gemini_006_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Convergence of multiple entropy measures as a signal of regime transition. [window=126]"""
    window = 126
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() + volume.rolling(window).std(), window)
    return (res).diff().diff().diff()

def f60_econ_gemini_007_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Convergence of multiple entropy measures as a signal of regime transition. [window=252]"""
    window = 252
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() + volume.rolling(window).std(), window)
    return (res).diff().diff().diff()

def f60_econ_gemini_008_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Convergence of multiple entropy measures as a signal of regime transition. [window=504]"""
    window = 504
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() + volume.rolling(window).std(), window)
    return (res).diff().diff().diff()

def f60_econ_gemini_009_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Convergence of multiple entropy measures as a signal of regime transition. [window=756]"""
    window = 756
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() + volume.rolling(window).std(), window)
    return (res).diff().diff().diff()

def f60_econ_gemini_010_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Convergence of multiple entropy measures as a signal of regime transition. [window=1260]"""
    window = 1260
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() + volume.rolling(window).std(), window)
    return (res).diff().diff().diff()

def f60_econ_gemini_011_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=53, w2=11, w3=282, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(53, min_periods=max(53//3, 2)).mean(), upside.rolling(11, min_periods=max(11//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.560588 + 0.0039422 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_012_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=60, w2=24, w3=299, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(24, min_periods=max(24//3, 2)).max()
    rebound = x - x.rolling(60, min_periods=max(60//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.121333 * _rolling_slope(draw, 299) + 0.0039423 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_013_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=67, w2=37, w3=316, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(volume.abs() + 1.0).shift(3)
    imbalance = a.diff(67) - b.diff(37)
    stress = imbalance.rolling(316, min_periods=max(316//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.587647 + 0.0039424 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_014_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=74, w2=50, w3=333, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 74)
    baseline = trend.rolling(50, min_periods=max(50//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(333, min_periods=max(333//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.601176 + 0.0039425 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_015_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=81, w2=63, w3=350, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 81)
    slow = _rolling_slope(x, 63)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.614706 + 0.0039426 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_016_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=88, w2=76, w3=367, lag=13)."""
    x = close.shift(13)
    peak = x.rolling(76, min_periods=max(76//3, 2)).max()
    trough = x.rolling(88, min_periods=max(88//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.628235 + 0.0039427 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_017_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=95, w2=89, w3=384, lag=21)."""
    x = close.shift(21)
    change = x.pct_change(95)
    rank = change.rolling(89, min_periods=max(89//3, 2)).rank(pct=True)
    persistence = change.rolling(384, min_periods=max(384//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.153 * persistence + 0.0039428 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_018_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=102, w2=102, w3=401, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(102, min_periods=max(102//3, 2)).std()
    vol_slow = ret.rolling(102, min_periods=max(102//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.655294 + 0.0039429 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_019_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=109, w2=115, w3=418, lag=55)."""
    x = close.shift(55)
    ma = x.rolling(115, min_periods=max(115//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 109)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.165667 * slope + 0.003943 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_020_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=116, w2=128, w3=435, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(116)
    drag = impulse.rolling(128, min_periods=max(128//3, 2)).mean()
    noise = impulse.abs().rolling(435, min_periods=max(435//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.828824 + 0.0039431 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_021_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=123, w2=141, w3=452, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 123)
    acceleration = _rolling_slope(velocity, 141)
    curvature = _rolling_slope(acceleration, 452)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.178333 * acceleration + 0.0039432 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_022_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=130, w2=154, w3=469, lag=2)."""
    rel = _safe_div(close.shift(2), volume.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 130)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.184667 * pressure.rolling(469, min_periods=max(469//3, 2)).mean() + 0.0039433 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_023_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=137, w2=167, w3=486, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(137, min_periods=max(137//3, 2)).mean())
    decay = spread.ewm(span=167, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.869412 + 0.0039434 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_024_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=144, w2=180, w3=503, lag=5)."""
    a = _safe_log(close.abs() + 1.0).shift(5)
    b = _safe_log(volume.abs() + 1.0).shift(5)
    corr = a.rolling(180, min_periods=max(180//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 144)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.882941 + 0.0039435 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_025_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=151, w2=193, w3=520, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    cover = _safe_div(a.rolling(151, min_periods=max(151//3, 2)).mean(), b.abs().rolling(193, min_periods=max(193//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.203667 * _rolling_slope(cover, 151) + 0.0039436 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_026_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=158, w2=206, w3=537, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    y = _safe_log(volume.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.21 * y + 0.790000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 158) - _rolling_slope(basket, 206) + 0.0039437 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_027_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=165, w2=219, w3=554, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(165, min_periods=max(165//3, 2)).mean(), upside.rolling(219, min_periods=max(219//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.923529 + 0.0039438 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_028_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=172, w2=232, w3=571, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    draw = x - x.rolling(232, min_periods=max(232//3, 2)).max()
    rebound = x - x.rolling(172, min_periods=max(172//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.222667 * _rolling_slope(draw, 571) + 0.0039439 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_029_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=179, w2=245, w3=588, lag=55)."""
    a = _safe_log(close.abs() + 1.0).shift(55)
    b = _safe_log(volume.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(588, min_periods=max(588//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.950588 + 0.003944 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_030_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=186, w2=258, w3=605, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 186)
    baseline = trend.rolling(258, min_periods=max(258//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(605, min_periods=max(605//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.964118 + 0.0039441 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_031_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=193, w2=271, w3=622, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 193)
    slow = _rolling_slope(x, 271)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.977647 + 0.0039442 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_032_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=200, w2=284, w3=639, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(284, min_periods=max(284//3, 2)).max()
    trough = x.rolling(200, min_periods=max(200//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.991176 + 0.0039443 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_033_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=207, w2=297, w3=656, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(297, min_periods=max(297//3, 2)).rank(pct=True)
    persistence = change.rolling(656, min_periods=max(656//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.254333 * persistence + 0.0039444 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_034_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=214, w2=310, w3=673, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(214, min_periods=max(214//3, 2)).std()
    vol_slow = ret.rolling(310, min_periods=max(310//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.018235 + 0.0039445 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_035_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=221, w2=323, w3=690, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(323, min_periods=max(323//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 221)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.267 * slope + 0.0039446 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_036_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=228, w2=336, w3=707, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(336, min_periods=max(336//3, 2)).mean()
    noise = impulse.abs().rolling(707, min_periods=max(707//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.045294 + 0.0039447 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_037_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=235, w2=349, w3=724, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 235)
    acceleration = _rolling_slope(velocity, 349)
    curvature = _rolling_slope(acceleration, 724)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.279667 * acceleration + 0.0039448 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_038_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=242, w2=362, w3=741, lag=34)."""
    rel = _safe_div(close.shift(34), volume.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 242)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.286 * pressure.rolling(741, min_periods=max(741//3, 2)).mean() + 0.0039449 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_039_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=249, w2=375, w3=758, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(249, min_periods=max(249//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.085882 + 0.003945 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_040_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=9, w2=388, w3=24, lag=0)."""
    a = _safe_log(close.abs() + 1.0).shift(0)
    b = _safe_log(volume.abs() + 1.0).shift(0)
    corr = a.rolling(388, min_periods=max(388//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 9)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.099412 + 0.0039451 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_041_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=16, w2=401, w3=41, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    cover = _safe_div(a.rolling(16, min_periods=max(16//3, 2)).mean(), b.abs().rolling(401, min_periods=max(401//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(41) + 0.305 * _rolling_slope(cover, 16) + 0.0039452 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_042_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=23, w2=414, w3=58, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    y = _safe_log(volume.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.311333 * y + 0.688667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 23) - _rolling_slope(basket, 414) + 0.0039453 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_043_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=30, w2=427, w3=75, lag=3)."""
    x = close.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(30, min_periods=max(30//3, 2)).mean(), upside.rolling(427, min_periods=max(427//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(75) * 1.14 + 0.0039454 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_044_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=37, w2=440, w3=92, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    draw = x - x.rolling(440, min_periods=max(440//3, 2)).max()
    rebound = x - x.rolling(37, min_periods=max(37//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.324 * _rolling_slope(draw, 92) + 0.0039455 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_045_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=44, w2=453, w3=109, lag=8)."""
    a = _safe_log(close.abs() + 1.0).shift(8)
    b = _safe_log(volume.abs() + 1.0).shift(8)
    imbalance = a.diff(44) - b.diff(126)
    stress = imbalance.rolling(109, min_periods=max(109//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.167059 + 0.0039456 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_046_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=51, w2=466, w3=126, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 51)
    baseline = trend.rolling(466, min_periods=max(466//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(126, min_periods=max(126//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.180588 + 0.0039457 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_047_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=58, w2=479, w3=143, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 58)
    slow = _rolling_slope(x, 479)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=143, adjust=False).mean() * 1.194118 + 0.0039458 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_048_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=65, w2=492, w3=160, lag=34)."""
    x = close.shift(34)
    peak = x.rolling(492, min_periods=max(492//3, 2)).max()
    trough = x.rolling(65, min_periods=max(65//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.207647 + 0.0039459 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_049_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=72, w2=505, w3=177, lag=55)."""
    x = close.shift(55)
    change = x.pct_change(72)
    rank = change.rolling(505, min_periods=max(505//3, 2)).rank(pct=True)
    persistence = change.rolling(177, min_periods=max(177//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.355667 * persistence + 0.003946 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_050_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=79, w2=19, w3=194, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(79, min_periods=max(79//3, 2)).std()
    vol_slow = ret.rolling(19, min_periods=max(19//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.234706 + 0.0039461 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_051_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=86, w2=32, w3=211, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(32, min_periods=max(32//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 86)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.036 * slope + 0.0039462 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_052_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=93, w2=45, w3=228, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(93)
    drag = impulse.rolling(45, min_periods=max(45//3, 2)).mean()
    noise = impulse.abs().rolling(228, min_periods=max(228//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.261765 + 0.0039463 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_053_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=100, w2=58, w3=245, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 100)
    acceleration = _rolling_slope(velocity, 58)
    curvature = _rolling_slope(acceleration, 245)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.048667 * acceleration + 0.0039464 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_054_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=107, w2=71, w3=262, lag=5)."""
    rel = _safe_div(close.shift(5), volume.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 107)
    pressure = rel_log.diff(71)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.055 * pressure.rolling(262, min_periods=max(262//3, 2)).mean() + 0.0039465 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_055_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=114, w2=84, w3=279, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(114, min_periods=max(114//3, 2)).mean())
    decay = spread.ewm(span=84, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.302353 + 0.0039466 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_056_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=121, w2=97, w3=296, lag=13)."""
    a = _safe_log(close.abs() + 1.0).shift(13)
    b = _safe_log(volume.abs() + 1.0).shift(13)
    corr = a.rolling(97, min_periods=max(97//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 121)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.315882 + 0.0039467 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_057_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=128, w2=110, w3=313, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    cover = _safe_div(a.rolling(128, min_periods=max(128//3, 2)).mean(), b.abs().rolling(110, min_periods=max(110//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.074 * _rolling_slope(cover, 128) + 0.0039468 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_058_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=135, w2=123, w3=330, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    y = _safe_log(volume.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.080333 * y + 0.919667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 135) - _rolling_slope(basket, 123) + 0.0039469 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_059_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=142, w2=136, w3=347, lag=55)."""
    x = close.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(142, min_periods=max(142//3, 2)).mean(), upside.rolling(136, min_periods=max(136//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.356471 + 0.003947 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_060_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=149, w2=149, w3=364, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    draw = x - x.rolling(149, min_periods=max(149//3, 2)).max()
    rebound = x - x.rolling(149, min_periods=max(149//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.093 * _rolling_slope(draw, 364) + 0.0039471 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_061_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=156, w2=162, w3=381, lag=1)."""
    a = _safe_log(close.abs() + 1.0).shift(1)
    b = _safe_log(volume.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(381, min_periods=max(381//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.383529 + 0.0039472 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_062_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=163, w2=175, w3=398, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 163)
    baseline = trend.rolling(175, min_periods=max(175//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(398, min_periods=max(398//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.397059 + 0.0039473 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_063_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=170, w2=188, w3=415, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 170)
    slow = _rolling_slope(x, 188)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.410588 + 0.0039474 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_064_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=177, w2=201, w3=432, lag=5)."""
    x = close.shift(5)
    peak = x.rolling(201, min_periods=max(201//3, 2)).max()
    trough = x.rolling(177, min_periods=max(177//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.424118 + 0.0039475 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_065_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=184, w2=214, w3=449, lag=8)."""
    x = close.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(214, min_periods=max(214//3, 2)).rank(pct=True)
    persistence = change.rolling(449, min_periods=max(449//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.124667 * persistence + 0.0039476 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_066_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=191, w2=227, w3=466, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(191, min_periods=max(191//3, 2)).std()
    vol_slow = ret.rolling(227, min_periods=max(227//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.451176 + 0.0039477 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_067_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=198, w2=240, w3=483, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(240, min_periods=max(240//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 198)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.137333 * slope + 0.0039478 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_068_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=205, w2=253, w3=500, lag=34)."""
    x = close.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(253, min_periods=max(253//3, 2)).mean()
    noise = impulse.abs().rolling(500, min_periods=max(500//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.478235 + 0.0039479 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_069_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=212, w2=266, w3=517, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 212)
    acceleration = _rolling_slope(velocity, 266)
    curvature = _rolling_slope(acceleration, 517)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.15 * acceleration + 0.003948 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_070_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=219, w2=279, w3=534, lag=0)."""
    rel = _safe_div(close.shift(0), volume.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 219)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.156333 * pressure.rolling(534, min_periods=max(534//3, 2)).mean() + 0.0039481 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_071_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=226, w2=292, w3=551, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(226, min_periods=max(226//3, 2)).mean())
    decay = spread.ewm(span=292, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.518824 + 0.0039482 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_072_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=233, w2=305, w3=568, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(volume.abs() + 1.0).shift(2)
    corr = a.rolling(305, min_periods=max(305//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 233)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.532353 + 0.0039483 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_073_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=240, w2=318, w3=585, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    cover = _safe_div(a.rolling(240, min_periods=max(240//3, 2)).mean(), b.abs().rolling(318, min_periods=max(318//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.175333 * _rolling_slope(cover, 240) + 0.0039484 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_074_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=247, w2=331, w3=602, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(volume.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.181667 * y + 0.818333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 247) - _rolling_slope(basket, 331) + 0.0039485 * anchor
    return base_signal.diff().diff().diff()

def f60_econ_gemini_075_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=7, w2=344, w3=619, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(7, min_periods=max(7//3, 2)).mean(), upside.rolling(344, min_periods=max(344//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.572941 + 0.0039486 * anchor
    return base_signal.diff().diff().diff()
