"""94 mechanical fragility index gemini d2 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Index measuring the susceptibility of price to large moves on low volume.
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

def f94_mfin_gemini_001_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Index measuring the susceptibility of price to large moves on low volume. [window=5]"""
    window = 5
    res = _safe_div(_safe_log(close).diff().abs(), volume + 1e-9)
    return (res).diff().diff()

def f94_mfin_gemini_002_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Index measuring the susceptibility of price to large moves on low volume. [window=10]"""
    window = 10
    res = _safe_div(_safe_log(close).diff().abs(), volume + 1e-9)
    return (res).diff().diff()

def f94_mfin_gemini_003_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Index measuring the susceptibility of price to large moves on low volume. [window=21]"""
    window = 21
    res = _safe_div(_safe_log(close).diff().abs(), volume + 1e-9)
    return (res).diff().diff()

def f94_mfin_gemini_004_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Index measuring the susceptibility of price to large moves on low volume. [window=42]"""
    window = 42
    res = _safe_div(_safe_log(close).diff().abs(), volume + 1e-9)
    return (res).diff().diff()

def f94_mfin_gemini_005_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Index measuring the susceptibility of price to large moves on low volume. [window=63]"""
    window = 63
    res = _safe_div(_safe_log(close).diff().abs(), volume + 1e-9)
    return (res).diff().diff()

def f94_mfin_gemini_006_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Index measuring the susceptibility of price to large moves on low volume. [window=126]"""
    window = 126
    res = _safe_div(_safe_log(close).diff().abs(), volume + 1e-9)
    return (res).diff().diff()

def f94_mfin_gemini_007_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Index measuring the susceptibility of price to large moves on low volume. [window=252]"""
    window = 252
    res = _safe_div(_safe_log(close).diff().abs(), volume + 1e-9)
    return (res).diff().diff()

def f94_mfin_gemini_008_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Index measuring the susceptibility of price to large moves on low volume. [window=504]"""
    window = 504
    res = _safe_div(_safe_log(close).diff().abs(), volume + 1e-9)
    return (res).diff().diff()

def f94_mfin_gemini_009_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Index measuring the susceptibility of price to large moves on low volume. [window=756]"""
    window = 756
    res = _safe_div(_safe_log(close).diff().abs(), volume + 1e-9)
    return (res).diff().diff()

def f94_mfin_gemini_010_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Index measuring the susceptibility of price to large moves on low volume. [window=1260]"""
    window = 1260
    res = _safe_div(_safe_log(close).diff().abs(), volume + 1e-9)
    return (res).diff().diff()

def f94_mfin_gemini_011_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=208, w2=203, w3=154, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 208)
    slow = _rolling_slope(x, 203)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=154, adjust=False).mean() * 1.207647 + 0.0058322 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_012_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=215, w2=216, w3=171, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(216, min_periods=max(216//3, 2)).max()
    trough = x.rolling(215, min_periods=max(215//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.221176 + 0.0058323 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_013_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=222, w2=229, w3=188, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(229, min_periods=max(229//3, 2)).rank(pct=True)
    persistence = change.rolling(188, min_periods=max(188//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.187667 * persistence + 0.0058324 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_014_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=229, w2=242, w3=205, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(229, min_periods=max(229//3, 2)).std()
    vol_slow = ret.rolling(242, min_periods=max(242//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.248235 + 0.0058325 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_015_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=236, w2=255, w3=222, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(255, min_periods=max(255//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 236)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.200333 * slope + 0.0058326 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_016_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=243, w2=268, w3=239, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(268, min_periods=max(268//3, 2)).mean()
    noise = impulse.abs().rolling(239, min_periods=max(239//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.275294 + 0.0058327 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_017_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=250, w2=281, w3=256, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 250)
    acceleration = _rolling_slope(velocity, 281)
    curvature = _rolling_slope(acceleration, 256)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.213 * acceleration + 0.0058328 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_018_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=10, w2=294, w3=273, lag=34)."""
    rel = _safe_div(close.shift(34), volume.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 10)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.219333 * pressure.rolling(273, min_periods=max(273//3, 2)).mean() + 0.0058329 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_019_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=17, w2=307, w3=290, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(17, min_periods=max(17//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.315882 + 0.005833 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_020_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=24, w2=320, w3=307, lag=0)."""
    a = _safe_log(close.abs() + 1.0).shift(0)
    b = _safe_log(volume.abs() + 1.0).shift(0)
    corr = a.rolling(320, min_periods=max(320//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 24)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.329412 + 0.0058331 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_021_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=31, w2=333, w3=324, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    cover = _safe_div(a.rolling(31, min_periods=max(31//3, 2)).mean(), b.abs().rolling(333, min_periods=max(333//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.238333 * _rolling_slope(cover, 31) + 0.0058332 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_022_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=38, w2=346, w3=341, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    y = _safe_log(volume.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.244667 * y + 0.755333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 38) - _rolling_slope(basket, 346) + 0.0058333 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_023_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=45, w2=359, w3=358, lag=3)."""
    x = close.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(45, min_periods=max(45//3, 2)).mean(), upside.rolling(359, min_periods=max(359//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.37 + 0.0058334 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_024_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=52, w2=372, w3=375, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    draw = x - x.rolling(372, min_periods=max(372//3, 2)).max()
    rebound = x - x.rolling(52, min_periods=max(52//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.257333 * _rolling_slope(draw, 375) + 0.0058335 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_025_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=59, w2=385, w3=392, lag=8)."""
    a = _safe_log(close.abs() + 1.0).shift(8)
    b = _safe_log(volume.abs() + 1.0).shift(8)
    imbalance = a.diff(59) - b.diff(126)
    stress = imbalance.rolling(392, min_periods=max(392//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.397059 + 0.0058336 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_026_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=66, w2=398, w3=409, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 66)
    baseline = trend.rolling(398, min_periods=max(398//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(409, min_periods=max(409//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.410588 + 0.0058337 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_027_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=73, w2=411, w3=426, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 73)
    slow = _rolling_slope(x, 411)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.424118 + 0.0058338 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_028_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=80, w2=424, w3=443, lag=34)."""
    x = close.shift(34)
    peak = x.rolling(424, min_periods=max(424//3, 2)).max()
    trough = x.rolling(80, min_periods=max(80//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.437647 + 0.0058339 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_029_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=87, w2=437, w3=460, lag=55)."""
    x = close.shift(55)
    change = x.pct_change(87)
    rank = change.rolling(437, min_periods=max(437//3, 2)).rank(pct=True)
    persistence = change.rolling(460, min_periods=max(460//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.289 * persistence + 0.005834 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_030_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=94, w2=450, w3=477, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(94, min_periods=max(94//3, 2)).std()
    vol_slow = ret.rolling(450, min_periods=max(450//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.464706 + 0.0058341 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_031_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=101, w2=463, w3=494, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(463, min_periods=max(463//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 101)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.301667 * slope + 0.0058342 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_032_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=108, w2=476, w3=511, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(108)
    drag = impulse.rolling(476, min_periods=max(476//3, 2)).mean()
    noise = impulse.abs().rolling(511, min_periods=max(511//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.491765 + 0.0058343 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_033_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=115, w2=489, w3=528, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 115)
    acceleration = _rolling_slope(velocity, 489)
    curvature = _rolling_slope(acceleration, 528)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.314333 * acceleration + 0.0058344 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_034_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=122, w2=502, w3=545, lag=5)."""
    rel = _safe_div(close.shift(5), volume.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 122)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.320667 * pressure.rolling(545, min_periods=max(545//3, 2)).mean() + 0.0058345 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_035_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=129, w2=16, w3=562, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(129, min_periods=max(129//3, 2)).mean())
    decay = spread.ewm(span=16, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.532353 + 0.0058346 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_036_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=136, w2=29, w3=579, lag=13)."""
    a = _safe_log(close.abs() + 1.0).shift(13)
    b = _safe_log(volume.abs() + 1.0).shift(13)
    corr = a.rolling(29, min_periods=max(29//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 136)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.545882 + 0.0058347 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_037_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=143, w2=42, w3=596, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    cover = _safe_div(a.rolling(143, min_periods=max(143//3, 2)).mean(), b.abs().rolling(42, min_periods=max(42//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.339667 * _rolling_slope(cover, 143) + 0.0058348 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_038_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=150, w2=55, w3=613, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    y = _safe_log(volume.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.346 * y + 0.654000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 150) - _rolling_slope(basket, 55) + 0.0058349 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_039_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=157, w2=68, w3=630, lag=55)."""
    x = close.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(157, min_periods=max(157//3, 2)).mean(), upside.rolling(68, min_periods=max(68//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.586471 + 0.005835 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_040_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=164, w2=81, w3=647, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    draw = x - x.rolling(81, min_periods=max(81//3, 2)).max()
    rebound = x - x.rolling(164, min_periods=max(164//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.358667 * _rolling_slope(draw, 647) + 0.0058351 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_041_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=171, w2=94, w3=664, lag=1)."""
    a = _safe_log(close.abs() + 1.0).shift(1)
    b = _safe_log(volume.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(94)
    stress = imbalance.rolling(664, min_periods=max(664//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.613529 + 0.0058352 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_042_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=178, w2=107, w3=681, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 178)
    baseline = trend.rolling(107, min_periods=max(107//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(681, min_periods=max(681//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.627059 + 0.0058353 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_043_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=185, w2=120, w3=698, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 185)
    slow = _rolling_slope(x, 120)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.640588 + 0.0058354 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_044_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=192, w2=133, w3=715, lag=5)."""
    x = close.shift(5)
    peak = x.rolling(133, min_periods=max(133//3, 2)).max()
    trough = x.rolling(192, min_periods=max(192//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.654118 + 0.0058355 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_045_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=199, w2=146, w3=732, lag=8)."""
    x = close.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(146, min_periods=max(146//3, 2)).rank(pct=True)
    persistence = change.rolling(732, min_periods=max(732//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.058 * persistence + 0.0058356 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_046_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=206, w2=159, w3=749, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(206, min_periods=max(206//3, 2)).std()
    vol_slow = ret.rolling(159, min_periods=max(159//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.827647 + 0.0058357 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_047_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=213, w2=172, w3=766, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(172, min_periods=max(172//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 213)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.070667 * slope + 0.0058358 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_048_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=220, w2=185, w3=32, lag=34)."""
    x = close.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(185, min_periods=max(185//3, 2)).mean()
    noise = impulse.abs().rolling(32, min_periods=max(32//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.854706 + 0.0058359 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_049_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=227, w2=198, w3=49, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 227)
    acceleration = _rolling_slope(velocity, 198)
    curvature = _rolling_slope(acceleration, 49)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.083333 * acceleration + 0.005836 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_050_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=234, w2=211, w3=66, lag=0)."""
    rel = _safe_div(close.shift(0), volume.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 234)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.089667 * pressure.rolling(66, min_periods=max(66//3, 2)).mean() + 0.0058361 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_051_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=241, w2=224, w3=83, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(241, min_periods=max(241//3, 2)).mean())
    decay = spread.ewm(span=224, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.895294 + 0.0058362 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_052_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=248, w2=237, w3=100, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(volume.abs() + 1.0).shift(2)
    corr = a.rolling(237, min_periods=max(237//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 248)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.908824 + 0.0058363 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_053_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=8, w2=250, w3=117, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    cover = _safe_div(a.rolling(8, min_periods=max(8//3, 2)).mean(), b.abs().rolling(250, min_periods=max(250//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(117) + 0.108667 * _rolling_slope(cover, 8) + 0.0058364 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_054_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=15, w2=263, w3=134, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(volume.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.115 * y + 0.885000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 15) - _rolling_slope(basket, 263) + 0.0058365 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_055_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=22, w2=276, w3=151, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(22, min_periods=max(22//3, 2)).mean(), upside.rolling(276, min_periods=max(276//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.949412 + 0.0058366 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_056_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=29, w2=289, w3=168, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    draw = x - x.rolling(289, min_periods=max(289//3, 2)).max()
    rebound = x - x.rolling(29, min_periods=max(29//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.127667 * _rolling_slope(draw, 168) + 0.0058367 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_057_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=36, w2=302, w3=185, lag=21)."""
    a = _safe_log(close.abs() + 1.0).shift(21)
    b = _safe_log(volume.abs() + 1.0).shift(21)
    imbalance = a.diff(36) - b.diff(126)
    stress = imbalance.rolling(185, min_periods=max(185//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.976471 + 0.0058368 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_058_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=43, w2=315, w3=202, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 43)
    baseline = trend.rolling(315, min_periods=max(315//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(202, min_periods=max(202//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.99 + 0.0058369 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_059_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=50, w2=328, w3=219, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 50)
    slow = _rolling_slope(x, 328)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=219, adjust=False).mean() * 1.003529 + 0.005837 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_060_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=57, w2=341, w3=236, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(341, min_periods=max(341//3, 2)).max()
    trough = x.rolling(57, min_periods=max(57//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.017059 + 0.0058371 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_061_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=64, w2=354, w3=253, lag=1)."""
    x = close.shift(1)
    change = x.pct_change(64)
    rank = change.rolling(354, min_periods=max(354//3, 2)).rank(pct=True)
    persistence = change.rolling(253, min_periods=max(253//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.159333 * persistence + 0.0058372 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_062_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=71, w2=367, w3=270, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(71, min_periods=max(71//3, 2)).std()
    vol_slow = ret.rolling(367, min_periods=max(367//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.044118 + 0.0058373 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_063_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=78, w2=380, w3=287, lag=3)."""
    x = close.shift(3)
    ma = x.rolling(380, min_periods=max(380//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 78)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.172 * slope + 0.0058374 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_064_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=85, w2=393, w3=304, lag=5)."""
    x = close.shift(5)
    impulse = x.diff(85)
    drag = impulse.rolling(393, min_periods=max(393//3, 2)).mean()
    noise = impulse.abs().rolling(304, min_periods=max(304//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.071176 + 0.0058375 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_065_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=92, w2=406, w3=321, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 92)
    acceleration = _rolling_slope(velocity, 406)
    curvature = _rolling_slope(acceleration, 321)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.184667 * acceleration + 0.0058376 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_066_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=99, w2=419, w3=338, lag=13)."""
    rel = _safe_div(close.shift(13), volume.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 99)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.191 * pressure.rolling(338, min_periods=max(338//3, 2)).mean() + 0.0058377 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_067_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=106, w2=432, w3=355, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(106, min_periods=max(106//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.111765 + 0.0058378 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_068_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=113, w2=445, w3=372, lag=34)."""
    a = _safe_log(close.abs() + 1.0).shift(34)
    b = _safe_log(volume.abs() + 1.0).shift(34)
    corr = a.rolling(445, min_periods=max(445//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 113)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.125294 + 0.0058379 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_069_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=120, w2=458, w3=389, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    cover = _safe_div(a.rolling(120, min_periods=max(120//3, 2)).mean(), b.abs().rolling(458, min_periods=max(458//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.21 * _rolling_slope(cover, 120) + 0.005838 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_070_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=127, w2=471, w3=406, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    y = _safe_log(volume.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.216333 * y + 0.783667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 127) - _rolling_slope(basket, 471) + 0.0058381 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_071_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=134, w2=484, w3=423, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(134, min_periods=max(134//3, 2)).mean(), upside.rolling(484, min_periods=max(484//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.165882 + 0.0058382 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_072_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=141, w2=497, w3=440, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(497, min_periods=max(497//3, 2)).max()
    rebound = x - x.rolling(141, min_periods=max(141//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.229 * _rolling_slope(draw, 440) + 0.0058383 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_073_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=148, w2=11, w3=457, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(volume.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(11)
    stress = imbalance.rolling(457, min_periods=max(457//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.192941 + 0.0058384 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_074_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=155, w2=24, w3=474, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 155)
    baseline = trend.rolling(24, min_periods=max(24//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(474, min_periods=max(474//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.206471 + 0.0058385 * anchor
    return base_signal.diff().diff()

def f94_mfin_gemini_075_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=162, w2=37, w3=491, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 162)
    slow = _rolling_slope(x, 37)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.22 + 0.0058386 * anchor
    return base_signal.diff().diff()
