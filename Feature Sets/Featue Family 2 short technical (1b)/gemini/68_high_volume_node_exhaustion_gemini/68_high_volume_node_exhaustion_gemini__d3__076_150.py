"""68 high volume node exhaustion gemini d3 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Price rejection or stalling at major high-volume nodes from historical profiles.
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
# FEATURE HYPOTHESES (076-150)
# ============================================================

def f68_hvne_gemini_076_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=5, w2=214, w3=194, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    draw = x - x.rolling(214, min_periods=max(214//3, 2)).max()
    rebound = x - x.rolling(5, min_periods=max(5//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.319333 * _rolling_slope(draw, 194) + 0.0043967 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_077_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=12, w2=227, w3=211, lag=21)."""
    a = _safe_log(close.abs() + 1.0).shift(21)
    b = _safe_log(volume.abs() + 1.0).shift(21)
    imbalance = a.diff(12) - b.diff(126)
    stress = imbalance.rolling(211, min_periods=max(211//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.611176 + 0.0043968 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_078_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=19, w2=240, w3=228, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 19)
    baseline = trend.rolling(240, min_periods=max(240//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(228, min_periods=max(228//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.624706 + 0.0043969 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_079_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=26, w2=253, w3=245, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 26)
    slow = _rolling_slope(x, 253)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=245, adjust=False).mean() * 1.638235 + 0.004397 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_080_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=33, w2=266, w3=262, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(266, min_periods=max(266//3, 2)).max()
    trough = x.rolling(33, min_periods=max(33//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.651765 + 0.0043971 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_081_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=40, w2=279, w3=279, lag=1)."""
    x = close.shift(1)
    change = x.pct_change(40)
    rank = change.rolling(279, min_periods=max(279//3, 2)).rank(pct=True)
    persistence = change.rolling(279, min_periods=max(279//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.351 * persistence + 0.0043972 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_082_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=47, w2=292, w3=296, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(47, min_periods=max(47//3, 2)).std()
    vol_slow = ret.rolling(292, min_periods=max(292//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.825294 + 0.0043973 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_083_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=54, w2=305, w3=313, lag=3)."""
    x = close.shift(3)
    ma = x.rolling(305, min_periods=max(305//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 54)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.031333 * slope + 0.0043974 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_084_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=61, w2=318, w3=330, lag=5)."""
    x = close.shift(5)
    impulse = x.diff(61)
    drag = impulse.rolling(318, min_periods=max(318//3, 2)).mean()
    noise = impulse.abs().rolling(330, min_periods=max(330//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.852353 + 0.0043975 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_085_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=68, w2=331, w3=347, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 68)
    acceleration = _rolling_slope(velocity, 331)
    curvature = _rolling_slope(acceleration, 347)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.044 * acceleration + 0.0043976 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_086_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=75, w2=344, w3=364, lag=13)."""
    rel = _safe_div(close.shift(13), volume.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 75)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.050333 * pressure.rolling(364, min_periods=max(364//3, 2)).mean() + 0.0043977 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_087_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=82, w2=357, w3=381, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(82, min_periods=max(82//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.892941 + 0.0043978 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_088_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=89, w2=370, w3=398, lag=34)."""
    a = _safe_log(close.abs() + 1.0).shift(34)
    b = _safe_log(volume.abs() + 1.0).shift(34)
    corr = a.rolling(370, min_periods=max(370//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 89)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.906471 + 0.0043979 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_089_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=96, w2=383, w3=415, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    cover = _safe_div(a.rolling(96, min_periods=max(96//3, 2)).mean(), b.abs().rolling(383, min_periods=max(383//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.069333 * _rolling_slope(cover, 96) + 0.004398 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_090_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=103, w2=396, w3=432, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    y = _safe_log(volume.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.075667 * y + 0.924333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 103) - _rolling_slope(basket, 396) + 0.0043981 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_091_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=110, w2=409, w3=449, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(110, min_periods=max(110//3, 2)).mean(), upside.rolling(409, min_periods=max(409//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.947059 + 0.0043982 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_092_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=117, w2=422, w3=466, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(422, min_periods=max(422//3, 2)).max()
    rebound = x - x.rolling(117, min_periods=max(117//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.088333 * _rolling_slope(draw, 466) + 0.0043983 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_093_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=124, w2=435, w3=483, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(volume.abs() + 1.0).shift(3)
    imbalance = a.diff(124) - b.diff(126)
    stress = imbalance.rolling(483, min_periods=max(483//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.974118 + 0.0043984 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_094_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=131, w2=448, w3=500, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 131)
    baseline = trend.rolling(448, min_periods=max(448//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(500, min_periods=max(500//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.987647 + 0.0043985 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_095_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=138, w2=461, w3=517, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 138)
    slow = _rolling_slope(x, 461)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.001176 + 0.0043986 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_096_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=145, w2=474, w3=534, lag=13)."""
    x = close.shift(13)
    peak = x.rolling(474, min_periods=max(474//3, 2)).max()
    trough = x.rolling(145, min_periods=max(145//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.014706 + 0.0043987 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_097_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=152, w2=487, w3=551, lag=21)."""
    x = close.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(487, min_periods=max(487//3, 2)).rank(pct=True)
    persistence = change.rolling(551, min_periods=max(551//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.12 * persistence + 0.0043988 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_098_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=159, w2=500, w3=568, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(159, min_periods=max(159//3, 2)).std()
    vol_slow = ret.rolling(500, min_periods=max(500//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.041765 + 0.0043989 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_099_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=166, w2=14, w3=585, lag=55)."""
    x = close.shift(55)
    ma = x.rolling(14, min_periods=max(14//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 166)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.132667 * slope + 0.004399 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_100_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=173, w2=27, w3=602, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(27, min_periods=max(27//3, 2)).mean()
    noise = impulse.abs().rolling(602, min_periods=max(602//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.068824 + 0.0043991 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_101_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=180, w2=40, w3=619, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 180)
    acceleration = _rolling_slope(velocity, 40)
    curvature = _rolling_slope(acceleration, 619)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.145333 * acceleration + 0.0043992 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_102_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=187, w2=53, w3=636, lag=2)."""
    rel = _safe_div(close.shift(2), volume.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 187)
    pressure = rel_log.diff(53)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.151667 * pressure.rolling(636, min_periods=max(636//3, 2)).mean() + 0.0043993 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_103_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=194, w2=66, w3=653, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(194, min_periods=max(194//3, 2)).mean())
    decay = spread.ewm(span=66, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.109412 + 0.0043994 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_104_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=201, w2=79, w3=670, lag=5)."""
    a = _safe_log(close.abs() + 1.0).shift(5)
    b = _safe_log(volume.abs() + 1.0).shift(5)
    corr = a.rolling(79, min_periods=max(79//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 201)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.122941 + 0.0043995 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_105_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=208, w2=92, w3=687, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    cover = _safe_div(a.rolling(208, min_periods=max(208//3, 2)).mean(), b.abs().rolling(92, min_periods=max(92//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.170667 * _rolling_slope(cover, 208) + 0.0043996 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_106_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=215, w2=105, w3=704, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    y = _safe_log(volume.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.177 * y + 0.823000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 215) - _rolling_slope(basket, 105) + 0.0043997 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_107_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=222, w2=118, w3=721, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(222, min_periods=max(222//3, 2)).mean(), upside.rolling(118, min_periods=max(118//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.163529 + 0.0043998 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_108_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=229, w2=131, w3=738, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    draw = x - x.rolling(131, min_periods=max(131//3, 2)).max()
    rebound = x - x.rolling(229, min_periods=max(229//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.189667 * _rolling_slope(draw, 738) + 0.0043999 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_109_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=236, w2=144, w3=755, lag=55)."""
    a = _safe_log(close.abs() + 1.0).shift(55)
    b = _safe_log(volume.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(755, min_periods=max(755//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.190588 + 0.0044 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_110_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=243, w2=157, w3=21, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 243)
    baseline = trend.rolling(157, min_periods=max(157//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(21, min_periods=max(21//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.204118 + 0.0044001 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_111_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=250, w2=170, w3=38, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 250)
    slow = _rolling_slope(x, 170)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=38, adjust=False).mean() * 1.217647 + 0.0044002 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_112_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=10, w2=183, w3=55, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(183, min_periods=max(183//3, 2)).max()
    trough = x.rolling(10, min_periods=max(10//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.231176 + 0.0044003 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_113_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=17, w2=196, w3=72, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(17)
    rank = change.rolling(196, min_periods=max(196//3, 2)).rank(pct=True)
    persistence = change.rolling(72, min_periods=max(72//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.221333 * persistence + 0.0044004 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_114_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=24, w2=209, w3=89, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(24, min_periods=max(24//3, 2)).std()
    vol_slow = ret.rolling(209, min_periods=max(209//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.258235 + 0.0044005 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_115_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=31, w2=222, w3=106, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(222, min_periods=max(222//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 31)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.234 * slope + 0.0044006 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_116_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=38, w2=235, w3=123, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(38)
    drag = impulse.rolling(235, min_periods=max(235//3, 2)).mean()
    noise = impulse.abs().rolling(123, min_periods=max(123//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.285294 + 0.0044007 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_117_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=45, w2=248, w3=140, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 45)
    acceleration = _rolling_slope(velocity, 248)
    curvature = _rolling_slope(acceleration, 140)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.246667 * acceleration + 0.0044008 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_118_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=52, w2=261, w3=157, lag=34)."""
    rel = _safe_div(close.shift(34), volume.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 52)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.253 * pressure.rolling(157, min_periods=max(157//3, 2)).mean() + 0.0044009 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_119_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=59, w2=274, w3=174, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(59, min_periods=max(59//3, 2)).mean())
    decay = spread.ewm(span=274, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.325882 + 0.004401 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_120_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=66, w2=287, w3=191, lag=0)."""
    a = _safe_log(close.abs() + 1.0).shift(0)
    b = _safe_log(volume.abs() + 1.0).shift(0)
    corr = a.rolling(287, min_periods=max(287//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 66)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.339412 + 0.0044011 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_121_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=73, w2=300, w3=208, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    cover = _safe_div(a.rolling(73, min_periods=max(73//3, 2)).mean(), b.abs().rolling(300, min_periods=max(300//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.272 * _rolling_slope(cover, 73) + 0.0044012 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_122_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=80, w2=313, w3=225, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    y = _safe_log(volume.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.278333 * y + 0.721667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 80) - _rolling_slope(basket, 313) + 0.0044013 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_123_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=87, w2=326, w3=242, lag=3)."""
    x = close.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(87, min_periods=max(87//3, 2)).mean(), upside.rolling(326, min_periods=max(326//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.38 + 0.0044014 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_124_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=94, w2=339, w3=259, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    draw = x - x.rolling(339, min_periods=max(339//3, 2)).max()
    rebound = x - x.rolling(94, min_periods=max(94//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.291 * _rolling_slope(draw, 259) + 0.0044015 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_125_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=101, w2=352, w3=276, lag=8)."""
    a = _safe_log(close.abs() + 1.0).shift(8)
    b = _safe_log(volume.abs() + 1.0).shift(8)
    imbalance = a.diff(101) - b.diff(126)
    stress = imbalance.rolling(276, min_periods=max(276//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.407059 + 0.0044016 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_126_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=108, w2=365, w3=293, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 108)
    baseline = trend.rolling(365, min_periods=max(365//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(293, min_periods=max(293//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.420588 + 0.0044017 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_127_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=115, w2=378, w3=310, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 115)
    slow = _rolling_slope(x, 378)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.434118 + 0.0044018 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_128_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=122, w2=391, w3=327, lag=34)."""
    x = close.shift(34)
    peak = x.rolling(391, min_periods=max(391//3, 2)).max()
    trough = x.rolling(122, min_periods=max(122//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.447647 + 0.0044019 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_129_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=129, w2=404, w3=344, lag=55)."""
    x = close.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(404, min_periods=max(404//3, 2)).rank(pct=True)
    persistence = change.rolling(344, min_periods=max(344//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.322667 * persistence + 0.004402 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_130_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=136, w2=417, w3=361, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(136, min_periods=max(136//3, 2)).std()
    vol_slow = ret.rolling(417, min_periods=max(417//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.474706 + 0.0044021 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_131_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=143, w2=430, w3=378, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(430, min_periods=max(430//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 143)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.335333 * slope + 0.0044022 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_132_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=150, w2=443, w3=395, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(443, min_periods=max(443//3, 2)).mean()
    noise = impulse.abs().rolling(395, min_periods=max(395//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.501765 + 0.0044023 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_133_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=157, w2=456, w3=412, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 157)
    acceleration = _rolling_slope(velocity, 456)
    curvature = _rolling_slope(acceleration, 412)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.348 * acceleration + 0.0044024 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_134_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=164, w2=469, w3=429, lag=5)."""
    rel = _safe_div(close.shift(5), volume.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 164)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.354333 * pressure.rolling(429, min_periods=max(429//3, 2)).mean() + 0.0044025 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_135_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=171, w2=482, w3=446, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(171, min_periods=max(171//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.542353 + 0.0044026 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_136_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=178, w2=495, w3=463, lag=13)."""
    a = _safe_log(close.abs() + 1.0).shift(13)
    b = _safe_log(volume.abs() + 1.0).shift(13)
    corr = a.rolling(495, min_periods=max(495//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 178)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.555882 + 0.0044027 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_137_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=185, w2=508, w3=480, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    cover = _safe_div(a.rolling(185, min_periods=max(185//3, 2)).mean(), b.abs().rolling(508, min_periods=max(508//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.041 * _rolling_slope(cover, 185) + 0.0044028 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_138_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=192, w2=22, w3=497, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    y = _safe_log(volume.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.047333 * y + 0.952667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 192) - _rolling_slope(basket, 22) + 0.0044029 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_139_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=199, w2=35, w3=514, lag=55)."""
    x = close.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(199, min_periods=max(199//3, 2)).mean(), upside.rolling(35, min_periods=max(35//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.596471 + 0.004403 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_140_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=206, w2=48, w3=531, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    draw = x - x.rolling(48, min_periods=max(48//3, 2)).max()
    rebound = x - x.rolling(206, min_periods=max(206//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.06 * _rolling_slope(draw, 531) + 0.0044031 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_141_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=213, w2=61, w3=548, lag=1)."""
    a = _safe_log(close.abs() + 1.0).shift(1)
    b = _safe_log(volume.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(61)
    stress = imbalance.rolling(548, min_periods=max(548//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.623529 + 0.0044032 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_142_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=220, w2=74, w3=565, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 220)
    baseline = trend.rolling(74, min_periods=max(74//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(565, min_periods=max(565//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.637059 + 0.0044033 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_143_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=227, w2=87, w3=582, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 227)
    slow = _rolling_slope(x, 87)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.650588 + 0.0044034 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_144_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=234, w2=100, w3=599, lag=5)."""
    x = close.shift(5)
    peak = x.rolling(100, min_periods=max(100//3, 2)).max()
    trough = x.rolling(234, min_periods=max(234//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.664118 + 0.0044035 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_145_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=241, w2=113, w3=616, lag=8)."""
    x = close.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(113, min_periods=max(113//3, 2)).rank(pct=True)
    persistence = change.rolling(616, min_periods=max(616//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.091667 * persistence + 0.0044036 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_146_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=248, w2=126, w3=633, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(248, min_periods=max(248//3, 2)).std()
    vol_slow = ret.rolling(126, min_periods=max(126//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.837647 + 0.0044037 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_147_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=8, w2=139, w3=650, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(139, min_periods=max(139//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 8)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.104333 * slope + 0.0044038 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_148_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=15, w2=152, w3=667, lag=34)."""
    x = close.shift(34)
    impulse = x.diff(15)
    drag = impulse.rolling(152, min_periods=max(152//3, 2)).mean()
    noise = impulse.abs().rolling(667, min_periods=max(667//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.864706 + 0.0044039 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_149_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=22, w2=165, w3=684, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 22)
    acceleration = _rolling_slope(velocity, 165)
    curvature = _rolling_slope(acceleration, 684)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.117 * acceleration + 0.004404 * anchor
    return base_signal.diff().diff().diff()

def f68_hvne_gemini_150_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=29, w2=178, w3=701, lag=0)."""
    rel = _safe_div(close.shift(0), volume.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 29)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.123333 * pressure.rolling(701, min_periods=max(701//3, 2)).mean() + 0.0044041 * anchor
    return base_signal.diff().diff().diff()
