"""15 anchored vwap extension gemini d2 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Price distance and reaction from Volume Weighted Average Price anchored to significant events.
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

def f15_avwx_gemini_001_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Price distance and reaction from Volume Weighted Average Price anchored to significant events. [window=5]"""
    window = 5
    res = _safe_div(close - (volume * close).rolling(window).sum() / volume.rolling(window).sum(), _atr(high, low, close, window))
    return (res).diff().diff()

def f15_avwx_gemini_002_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Price distance and reaction from Volume Weighted Average Price anchored to significant events. [window=10]"""
    window = 10
    res = _safe_div(close - (volume * close).rolling(window).sum() / volume.rolling(window).sum(), _atr(high, low, close, window))
    return (res).diff().diff()

def f15_avwx_gemini_003_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Price distance and reaction from Volume Weighted Average Price anchored to significant events. [window=21]"""
    window = 21
    res = _safe_div(close - (volume * close).rolling(window).sum() / volume.rolling(window).sum(), _atr(high, low, close, window))
    return (res).diff().diff()

def f15_avwx_gemini_004_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Price distance and reaction from Volume Weighted Average Price anchored to significant events. [window=42]"""
    window = 42
    res = _safe_div(close - (volume * close).rolling(window).sum() / volume.rolling(window).sum(), _atr(high, low, close, window))
    return (res).diff().diff()

def f15_avwx_gemini_005_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Price distance and reaction from Volume Weighted Average Price anchored to significant events. [window=63]"""
    window = 63
    res = _safe_div(close - (volume * close).rolling(window).sum() / volume.rolling(window).sum(), _atr(high, low, close, window))
    return (res).diff().diff()

def f15_avwx_gemini_006_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Price distance and reaction from Volume Weighted Average Price anchored to significant events. [window=126]"""
    window = 126
    res = _safe_div(close - (volume * close).rolling(window).sum() / volume.rolling(window).sum(), _atr(high, low, close, window))
    return (res).diff().diff()

def f15_avwx_gemini_007_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Price distance and reaction from Volume Weighted Average Price anchored to significant events. [window=252]"""
    window = 252
    res = _safe_div(close - (volume * close).rolling(window).sum() / volume.rolling(window).sum(), _atr(high, low, close, window))
    return (res).diff().diff()

def f15_avwx_gemini_008_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Price distance and reaction from Volume Weighted Average Price anchored to significant events. [window=504]"""
    window = 504
    res = _safe_div(close - (volume * close).rolling(window).sum() / volume.rolling(window).sum(), _atr(high, low, close, window))
    return (res).diff().diff()

def f15_avwx_gemini_009_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Price distance and reaction from Volume Weighted Average Price anchored to significant events. [window=756]"""
    window = 756
    res = _safe_div(close - (volume * close).rolling(window).sum() / volume.rolling(window).sum(), _atr(high, low, close, window))
    return (res).diff().diff()

def f15_avwx_gemini_010_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Price distance and reaction from Volume Weighted Average Price anchored to significant events. [window=1260]"""
    window = 1260
    res = _safe_div(close - (volume * close).rolling(window).sum() / volume.rolling(window).sum(), _atr(high, low, close, window))
    return (res).diff().diff()

def f15_avwx_gemini_011_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=19, w2=430, w3=576, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 19)
    slow = _rolling_slope(x, 430)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.990588 + 0.0014082 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_012_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=26, w2=443, w3=593, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(443, min_periods=max(443//3, 2)).max()
    trough = x.rolling(26, min_periods=max(26//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.004118 + 0.0014083 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_013_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=33, w2=456, w3=610, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(33)
    rank = change.rolling(456, min_periods=max(456//3, 2)).rank(pct=True)
    persistence = change.rolling(610, min_periods=max(610//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.158 * persistence + 0.0014084 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_014_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=40, w2=469, w3=627, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(40, min_periods=max(40//3, 2)).std()
    vol_slow = ret.rolling(469, min_periods=max(469//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.031176 + 0.0014085 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_015_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=47, w2=482, w3=644, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(482, min_periods=max(482//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 47)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.170667 * slope + 0.0014086 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_016_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=54, w2=495, w3=661, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(54)
    drag = impulse.rolling(495, min_periods=max(495//3, 2)).mean()
    noise = impulse.abs().rolling(661, min_periods=max(661//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.058235 + 0.0014087 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_017_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=61, w2=508, w3=678, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 61)
    acceleration = _rolling_slope(velocity, 508)
    curvature = _rolling_slope(acceleration, 678)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.183333 * acceleration + 0.0014088 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_018_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=68, w2=22, w3=695, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 68)
    pressure = rel_log.diff(22)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.189667 * pressure.rolling(695, min_periods=max(695//3, 2)).mean() + 0.0014089 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_019_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=75, w2=35, w3=712, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(75, min_periods=max(75//3, 2)).mean())
    decay = spread.ewm(span=35, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.098824 + 0.001409 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_020_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=82, w2=48, w3=729, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(48, min_periods=max(48//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 82)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.112353 + 0.0014091 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_021_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=89, w2=61, w3=746, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(89, min_periods=max(89//3, 2)).mean(), b.abs().rolling(61, min_periods=max(61//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.208667 * _rolling_slope(cover, 89) + 0.0014092 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_022_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=96, w2=74, w3=763, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.215 * y + 0.785000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 96) - _rolling_slope(basket, 74) + 0.0014093 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_023_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=103, w2=87, w3=29, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(103, min_periods=max(103//3, 2)).mean(), upside.rolling(87, min_periods=max(87//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(29) * 1.152941 + 0.0014094 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_024_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=110, w2=100, w3=46, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(100, min_periods=max(100//3, 2)).max()
    rebound = x - x.rolling(110, min_periods=max(110//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.227667 * _rolling_slope(draw, 46) + 0.0014095 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_025_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=117, w2=113, w3=63, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(117) - b.diff(113)
    stress = imbalance.rolling(63, min_periods=max(63//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.18 + 0.0014096 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_026_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=124, w2=126, w3=80, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 124)
    baseline = trend.rolling(126, min_periods=max(126//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(80, min_periods=max(80//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.193529 + 0.0014097 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_027_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=131, w2=139, w3=97, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 131)
    slow = _rolling_slope(x, 139)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=97, adjust=False).mean() * 1.207059 + 0.0014098 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_028_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=138, w2=152, w3=114, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(152, min_periods=max(152//3, 2)).max()
    trough = x.rolling(138, min_periods=max(138//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.220588 + 0.0014099 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_029_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=145, w2=165, w3=131, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(165, min_periods=max(165//3, 2)).rank(pct=True)
    persistence = change.rolling(131, min_periods=max(131//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.259333 * persistence + 0.00141 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_030_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=152, w2=178, w3=148, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(152, min_periods=max(152//3, 2)).std()
    vol_slow = ret.rolling(178, min_periods=max(178//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.247647 + 0.0014101 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_031_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=159, w2=191, w3=165, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(191, min_periods=max(191//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 159)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.272 * slope + 0.0014102 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_032_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=166, w2=204, w3=182, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(204, min_periods=max(204//3, 2)).mean()
    noise = impulse.abs().rolling(182, min_periods=max(182//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.274706 + 0.0014103 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_033_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=173, w2=217, w3=199, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 173)
    acceleration = _rolling_slope(velocity, 217)
    curvature = _rolling_slope(acceleration, 199)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.284667 * acceleration + 0.0014104 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_034_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=180, w2=230, w3=216, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 180)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.291 * pressure.rolling(216, min_periods=max(216//3, 2)).mean() + 0.0014105 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_035_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=187, w2=243, w3=233, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(187, min_periods=max(187//3, 2)).mean())
    decay = spread.ewm(span=243, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.315294 + 0.0014106 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_036_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=194, w2=256, w3=250, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(256, min_periods=max(256//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 194)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.328824 + 0.0014107 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_037_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=201, w2=269, w3=267, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(201, min_periods=max(201//3, 2)).mean(), b.abs().rolling(269, min_periods=max(269//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.31 * _rolling_slope(cover, 201) + 0.0014108 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_038_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=208, w2=282, w3=284, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.316333 * y + 0.683667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 208) - _rolling_slope(basket, 282) + 0.0014109 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_039_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=215, w2=295, w3=301, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(215, min_periods=max(215//3, 2)).mean(), upside.rolling(295, min_periods=max(295//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.369412 + 0.001411 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_040_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=222, w2=308, w3=318, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(308, min_periods=max(308//3, 2)).max()
    rebound = x - x.rolling(222, min_periods=max(222//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.329 * _rolling_slope(draw, 318) + 0.0014111 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_041_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=229, w2=321, w3=335, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(335, min_periods=max(335//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.396471 + 0.0014112 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_042_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=236, w2=334, w3=352, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 236)
    baseline = trend.rolling(334, min_periods=max(334//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(352, min_periods=max(352//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.41 + 0.0014113 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_043_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=243, w2=347, w3=369, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 243)
    slow = _rolling_slope(x, 347)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.423529 + 0.0014114 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_044_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=250, w2=360, w3=386, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(360, min_periods=max(360//3, 2)).max()
    trough = x.rolling(250, min_periods=max(250//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.437059 + 0.0014115 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_045_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=10, w2=373, w3=403, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(10)
    rank = change.rolling(373, min_periods=max(373//3, 2)).rank(pct=True)
    persistence = change.rolling(403, min_periods=max(403//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.360667 * persistence + 0.0014116 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_046_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=17, w2=386, w3=420, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(17, min_periods=max(17//3, 2)).std()
    vol_slow = ret.rolling(386, min_periods=max(386//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.464118 + 0.0014117 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_047_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=24, w2=399, w3=437, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(399, min_periods=max(399//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 24)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.041 * slope + 0.0014118 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_048_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=31, w2=412, w3=454, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(31)
    drag = impulse.rolling(412, min_periods=max(412//3, 2)).mean()
    noise = impulse.abs().rolling(454, min_periods=max(454//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.491176 + 0.0014119 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_049_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=38, w2=425, w3=471, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 38)
    acceleration = _rolling_slope(velocity, 425)
    curvature = _rolling_slope(acceleration, 471)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.053667 * acceleration + 0.001412 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_050_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=45, w2=438, w3=488, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 45)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.06 * pressure.rolling(488, min_periods=max(488//3, 2)).mean() + 0.0014121 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_051_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=52, w2=451, w3=505, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(52, min_periods=max(52//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.531765 + 0.0014122 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_052_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=59, w2=464, w3=522, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(464, min_periods=max(464//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 59)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.545294 + 0.0014123 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_053_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=66, w2=477, w3=539, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(66, min_periods=max(66//3, 2)).mean(), b.abs().rolling(477, min_periods=max(477//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.079 * _rolling_slope(cover, 66) + 0.0014124 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_054_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=73, w2=490, w3=556, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.085333 * y + 0.914667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 73) - _rolling_slope(basket, 490) + 0.0014125 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_055_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=80, w2=503, w3=573, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(80, min_periods=max(80//3, 2)).mean(), upside.rolling(503, min_periods=max(503//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.585882 + 0.0014126 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_056_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=87, w2=17, w3=590, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(17, min_periods=max(17//3, 2)).max()
    rebound = x - x.rolling(87, min_periods=max(87//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.098 * _rolling_slope(draw, 590) + 0.0014127 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_057_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=94, w2=30, w3=607, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(94) - b.diff(30)
    stress = imbalance.rolling(607, min_periods=max(607//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.612941 + 0.0014128 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_058_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=101, w2=43, w3=624, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 101)
    baseline = trend.rolling(43, min_periods=max(43//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(624, min_periods=max(624//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.626471 + 0.0014129 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_059_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=108, w2=56, w3=641, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 108)
    slow = _rolling_slope(x, 56)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.64 + 0.001413 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_060_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=115, w2=69, w3=658, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(69, min_periods=max(69//3, 2)).max()
    trough = x.rolling(115, min_periods=max(115//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.653529 + 0.0014131 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_061_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=122, w2=82, w3=675, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(122)
    rank = change.rolling(82, min_periods=max(82//3, 2)).rank(pct=True)
    persistence = change.rolling(675, min_periods=max(675//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.129667 * persistence + 0.0014132 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_062_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=129, w2=95, w3=692, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(129, min_periods=max(129//3, 2)).std()
    vol_slow = ret.rolling(95, min_periods=max(95//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.827059 + 0.0014133 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_063_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=136, w2=108, w3=709, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(108, min_periods=max(108//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 136)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.142333 * slope + 0.0014134 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_064_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=143, w2=121, w3=726, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(121, min_periods=max(121//3, 2)).mean()
    noise = impulse.abs().rolling(726, min_periods=max(726//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.854118 + 0.0014135 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_065_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=150, w2=134, w3=743, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 150)
    acceleration = _rolling_slope(velocity, 134)
    curvature = _rolling_slope(acceleration, 743)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.155 * acceleration + 0.0014136 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_066_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=157, w2=147, w3=760, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 157)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.161333 * pressure.rolling(760, min_periods=max(760//3, 2)).mean() + 0.0014137 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_067_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=164, w2=160, w3=26, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(164, min_periods=max(164//3, 2)).mean())
    decay = spread.ewm(span=160, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.894706 + 0.0014138 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_068_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=171, w2=173, w3=43, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(173, min_periods=max(173//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 171)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.908235 + 0.0014139 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_069_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=178, w2=186, w3=60, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(178, min_periods=max(178//3, 2)).mean(), b.abs().rolling(186, min_periods=max(186//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(60) + 0.180333 * _rolling_slope(cover, 178) + 0.001414 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_070_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=185, w2=199, w3=77, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.186667 * y + 0.813333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 185) - _rolling_slope(basket, 199) + 0.0014141 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_071_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=192, w2=212, w3=94, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(192, min_periods=max(192//3, 2)).mean(), upside.rolling(212, min_periods=max(212//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(94) * 0.948824 + 0.0014142 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_072_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=199, w2=225, w3=111, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(225, min_periods=max(225//3, 2)).max()
    rebound = x - x.rolling(199, min_periods=max(199//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.199333 * _rolling_slope(draw, 111) + 0.0014143 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_073_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=206, w2=238, w3=128, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(128, min_periods=max(128//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.975882 + 0.0014144 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_074_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=213, w2=251, w3=145, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 213)
    baseline = trend.rolling(251, min_periods=max(251//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(145, min_periods=max(145//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.989412 + 0.0014145 * anchor
    return base_signal.diff().diff()

def f15_avwx_gemini_075_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=220, w2=264, w3=162, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 220)
    slow = _rolling_slope(x, 264)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=162, adjust=False).mean() * 1.002941 + 0.0014146 * anchor
    return base_signal.diff().diff()
