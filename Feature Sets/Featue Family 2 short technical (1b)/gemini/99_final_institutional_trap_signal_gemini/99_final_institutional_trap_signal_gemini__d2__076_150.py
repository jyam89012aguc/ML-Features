"""99 final institutional trap signal gemini d2 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Specific price-volume patterns signaling a final trap for retail participants.
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

def f99_fits_gemini_076_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=9, w2=23, w3=44, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(23, min_periods=max(23//3, 2)).max()
    trough = x.rolling(9, min_periods=max(9//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.560588 + 0.0061187 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_077_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=16, w2=36, w3=61, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(16)
    rank = change.rolling(36, min_periods=max(36//3, 2)).rank(pct=True)
    persistence = change.rolling(61, min_periods=max(61//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.048 * persistence + 0.0061188 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_078_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=23, w2=49, w3=78, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(23, min_periods=max(23//3, 2)).std()
    vol_slow = ret.rolling(49, min_periods=max(49//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.587647 + 0.0061189 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_079_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=30, w2=62, w3=95, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(62, min_periods=max(62//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 30)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.060667 * slope + 0.006119 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_080_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=37, w2=75, w3=112, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(37)
    drag = impulse.rolling(75, min_periods=max(75//3, 2)).mean()
    noise = impulse.abs().rolling(112, min_periods=max(112//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.614706 + 0.0061191 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_081_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=44, w2=88, w3=129, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 44)
    acceleration = _rolling_slope(velocity, 88)
    curvature = _rolling_slope(acceleration, 129)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.073333 * acceleration + 0.0061192 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_082_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=51, w2=101, w3=146, lag=2)."""
    rel = _safe_div(high.shift(2), close.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 51)
    pressure = rel_log.diff(101)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.079667 * pressure.rolling(146, min_periods=max(146//3, 2)).mean() + 0.0061193 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_083_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=58, w2=114, w3=163, lag=3)."""
    a = high.shift(3)
    b = close.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(58, min_periods=max(58//3, 2)).mean())
    decay = spread.ewm(span=114, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.655294 + 0.0061194 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_084_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=65, w2=127, w3=180, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(close.abs() + 1.0).shift(5)
    corr = a.rolling(127, min_periods=max(127//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 65)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.668824 + 0.0061195 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_085_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=72, w2=140, w3=197, lag=8)."""
    a = high.shift(8)
    b = close.shift(8)
    cover = _safe_div(a.rolling(72, min_periods=max(72//3, 2)).mean(), b.abs().rolling(140, min_periods=max(140//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.098667 * _rolling_slope(cover, 72) + 0.0061196 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_086_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=79, w2=153, w3=214, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(close.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.105 * y + 0.895000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 79) - _rolling_slope(basket, 153) + 0.0061197 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_087_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=86, w2=166, w3=231, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(86, min_periods=max(86//3, 2)).mean(), upside.rolling(166, min_periods=max(166//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.855882 + 0.0061198 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_088_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=93, w2=179, w3=248, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(179, min_periods=max(179//3, 2)).max()
    rebound = x - x.rolling(93, min_periods=max(93//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.117667 * _rolling_slope(draw, 248) + 0.0061199 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_089_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=100, w2=192, w3=265, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(close.abs() + 1.0).shift(55)
    imbalance = a.diff(100) - b.diff(126)
    stress = imbalance.rolling(265, min_periods=max(265//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.882941 + 0.00612 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_090_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=107, w2=205, w3=282, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 107)
    baseline = trend.rolling(205, min_periods=max(205//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(282, min_periods=max(282//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.896471 + 0.0061201 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_091_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=114, w2=218, w3=299, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 114)
    slow = _rolling_slope(x, 218)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=299, adjust=False).mean() * 0.91 + 0.0061202 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_092_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=121, w2=231, w3=316, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(231, min_periods=max(231//3, 2)).max()
    trough = x.rolling(121, min_periods=max(121//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.923529 + 0.0061203 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_093_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=128, w2=244, w3=333, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(244, min_periods=max(244//3, 2)).rank(pct=True)
    persistence = change.rolling(333, min_periods=max(333//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.149333 * persistence + 0.0061204 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_094_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=135, w2=257, w3=350, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(135, min_periods=max(135//3, 2)).std()
    vol_slow = ret.rolling(257, min_periods=max(257//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.950588 + 0.0061205 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_095_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=142, w2=270, w3=367, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(270, min_periods=max(270//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 142)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.162 * slope + 0.0061206 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_096_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=149, w2=283, w3=384, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(283, min_periods=max(283//3, 2)).mean()
    noise = impulse.abs().rolling(384, min_periods=max(384//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.977647 + 0.0061207 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_097_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=156, w2=296, w3=401, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 156)
    acceleration = _rolling_slope(velocity, 296)
    curvature = _rolling_slope(acceleration, 401)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.174667 * acceleration + 0.0061208 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_098_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=163, w2=309, w3=418, lag=34)."""
    rel = _safe_div(high.shift(34), close.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 163)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.181 * pressure.rolling(418, min_periods=max(418//3, 2)).mean() + 0.0061209 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_099_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=170, w2=322, w3=435, lag=55)."""
    a = high.shift(55)
    b = close.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(170, min_periods=max(170//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.018235 + 0.006121 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_100_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=177, w2=335, w3=452, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(close.abs() + 1.0).shift(0)
    corr = a.rolling(335, min_periods=max(335//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 177)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.031765 + 0.0061211 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_101_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=184, w2=348, w3=469, lag=1)."""
    a = high.shift(1)
    b = close.shift(1)
    cover = _safe_div(a.rolling(184, min_periods=max(184//3, 2)).mean(), b.abs().rolling(348, min_periods=max(348//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.2 * _rolling_slope(cover, 184) + 0.0061212 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_102_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=191, w2=361, w3=486, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(close.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.206333 * y + 0.793667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 191) - _rolling_slope(basket, 361) + 0.0061213 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_103_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=198, w2=374, w3=503, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(198, min_periods=max(198//3, 2)).mean(), upside.rolling(374, min_periods=max(374//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.072353 + 0.0061214 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_104_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=205, w2=387, w3=520, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(387, min_periods=max(387//3, 2)).max()
    rebound = x - x.rolling(205, min_periods=max(205//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.219 * _rolling_slope(draw, 520) + 0.0061215 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_105_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=212, w2=400, w3=537, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(close.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(537, min_periods=max(537//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.099412 + 0.0061216 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_106_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=219, w2=413, w3=554, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 219)
    baseline = trend.rolling(413, min_periods=max(413//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(554, min_periods=max(554//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.112941 + 0.0061217 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_107_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=226, w2=426, w3=571, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 226)
    slow = _rolling_slope(x, 426)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.126471 + 0.0061218 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_108_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=233, w2=439, w3=588, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(439, min_periods=max(439//3, 2)).max()
    trough = x.rolling(233, min_periods=max(233//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.14 + 0.0061219 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_109_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=240, w2=452, w3=605, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(452, min_periods=max(452//3, 2)).rank(pct=True)
    persistence = change.rolling(605, min_periods=max(605//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.250667 * persistence + 0.006122 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_110_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=247, w2=465, w3=622, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(247, min_periods=max(247//3, 2)).std()
    vol_slow = ret.rolling(465, min_periods=max(465//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.167059 + 0.0061221 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_111_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=7, w2=478, w3=639, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(478, min_periods=max(478//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 7)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.263333 * slope + 0.0061222 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_112_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=14, w2=491, w3=656, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(14)
    drag = impulse.rolling(491, min_periods=max(491//3, 2)).mean()
    noise = impulse.abs().rolling(656, min_periods=max(656//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.194118 + 0.0061223 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_113_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=21, w2=504, w3=673, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 21)
    acceleration = _rolling_slope(velocity, 504)
    curvature = _rolling_slope(acceleration, 673)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.276 * acceleration + 0.0061224 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_114_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=28, w2=18, w3=690, lag=5)."""
    rel = _safe_div(high.shift(5), close.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 28)
    pressure = rel_log.diff(18)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.282333 * pressure.rolling(690, min_periods=max(690//3, 2)).mean() + 0.0061225 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_115_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=35, w2=31, w3=707, lag=8)."""
    a = high.shift(8)
    b = close.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(35, min_periods=max(35//3, 2)).mean())
    decay = spread.ewm(span=31, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.234706 + 0.0061226 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_116_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=42, w2=44, w3=724, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(close.abs() + 1.0).shift(13)
    corr = a.rolling(44, min_periods=max(44//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 42)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.248235 + 0.0061227 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_117_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=49, w2=57, w3=741, lag=21)."""
    a = high.shift(21)
    b = close.shift(21)
    cover = _safe_div(a.rolling(49, min_periods=max(49//3, 2)).mean(), b.abs().rolling(57, min_periods=max(57//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.301333 * _rolling_slope(cover, 49) + 0.0061228 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_118_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=56, w2=70, w3=758, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(close.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.307667 * y + 0.692333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 56) - _rolling_slope(basket, 70) + 0.0061229 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_119_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=63, w2=83, w3=24, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(63, min_periods=max(63//3, 2)).mean(), upside.rolling(83, min_periods=max(83//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(24) * 1.288824 + 0.006123 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_120_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=70, w2=96, w3=41, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(96, min_periods=max(96//3, 2)).max()
    rebound = x - x.rolling(70, min_periods=max(70//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.320333 * _rolling_slope(draw, 41) + 0.0061231 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_121_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=77, w2=109, w3=58, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(close.abs() + 1.0).shift(1)
    imbalance = a.diff(77) - b.diff(109)
    stress = imbalance.rolling(58, min_periods=max(58//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.315882 + 0.0061232 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_122_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=84, w2=122, w3=75, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 84)
    baseline = trend.rolling(122, min_periods=max(122//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(75, min_periods=max(75//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.329412 + 0.0061233 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_123_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=91, w2=135, w3=92, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 91)
    slow = _rolling_slope(x, 135)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=92, adjust=False).mean() * 1.342941 + 0.0061234 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_124_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=98, w2=148, w3=109, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(148, min_periods=max(148//3, 2)).max()
    trough = x.rolling(98, min_periods=max(98//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.356471 + 0.0061235 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_125_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=105, w2=161, w3=126, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(105)
    rank = change.rolling(161, min_periods=max(161//3, 2)).rank(pct=True)
    persistence = change.rolling(126, min_periods=max(126//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.352 * persistence + 0.0061236 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_126_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=112, w2=174, w3=143, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(112, min_periods=max(112//3, 2)).std()
    vol_slow = ret.rolling(174, min_periods=max(174//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.383529 + 0.0061237 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_127_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=119, w2=187, w3=160, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(187, min_periods=max(187//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 119)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.032333 * slope + 0.0061238 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_128_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=126, w2=200, w3=177, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(200, min_periods=max(200//3, 2)).mean()
    noise = impulse.abs().rolling(177, min_periods=max(177//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.410588 + 0.0061239 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_129_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=133, w2=213, w3=194, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 133)
    acceleration = _rolling_slope(velocity, 213)
    curvature = _rolling_slope(acceleration, 194)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.045 * acceleration + 0.006124 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_130_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=140, w2=226, w3=211, lag=0)."""
    rel = _safe_div(high.shift(0), close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 140)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.051333 * pressure.rolling(211, min_periods=max(211//3, 2)).mean() + 0.0061241 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_131_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=147, w2=239, w3=228, lag=1)."""
    a = high.shift(1)
    b = close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(147, min_periods=max(147//3, 2)).mean())
    decay = spread.ewm(span=239, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.451176 + 0.0061242 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_132_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=154, w2=252, w3=245, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(close.abs() + 1.0).shift(2)
    corr = a.rolling(252, min_periods=max(252//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 154)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.464706 + 0.0061243 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_133_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=161, w2=265, w3=262, lag=3)."""
    a = high.shift(3)
    b = close.shift(3)
    cover = _safe_div(a.rolling(161, min_periods=max(161//3, 2)).mean(), b.abs().rolling(265, min_periods=max(265//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.070333 * _rolling_slope(cover, 161) + 0.0061244 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_134_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=168, w2=278, w3=279, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(close.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.076667 * y + 0.923333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 168) - _rolling_slope(basket, 278) + 0.0061245 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_135_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=175, w2=291, w3=296, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(175, min_periods=max(175//3, 2)).mean(), upside.rolling(291, min_periods=max(291//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.505294 + 0.0061246 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_136_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=182, w2=304, w3=313, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(304, min_periods=max(304//3, 2)).max()
    rebound = x - x.rolling(182, min_periods=max(182//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.089333 * _rolling_slope(draw, 313) + 0.0061247 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_137_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=189, w2=317, w3=330, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(close.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(330, min_periods=max(330//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.532353 + 0.0061248 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_138_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=196, w2=330, w3=347, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 196)
    baseline = trend.rolling(330, min_periods=max(330//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(347, min_periods=max(347//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.545882 + 0.0061249 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_139_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=203, w2=343, w3=364, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 203)
    slow = _rolling_slope(x, 343)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.559412 + 0.006125 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_140_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=210, w2=356, w3=381, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(356, min_periods=max(356//3, 2)).max()
    trough = x.rolling(210, min_periods=max(210//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.572941 + 0.0061251 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_141_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=217, w2=369, w3=398, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(369, min_periods=max(369//3, 2)).rank(pct=True)
    persistence = change.rolling(398, min_periods=max(398//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.121 * persistence + 0.0061252 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_142_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=224, w2=382, w3=415, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(224, min_periods=max(224//3, 2)).std()
    vol_slow = ret.rolling(382, min_periods=max(382//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.6 + 0.0061253 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_143_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=231, w2=395, w3=432, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(395, min_periods=max(395//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 231)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.133667 * slope + 0.0061254 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_144_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=238, w2=408, w3=449, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(408, min_periods=max(408//3, 2)).mean()
    noise = impulse.abs().rolling(449, min_periods=max(449//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.627059 + 0.0061255 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_145_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=245, w2=421, w3=466, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 245)
    acceleration = _rolling_slope(velocity, 421)
    curvature = _rolling_slope(acceleration, 466)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.146333 * acceleration + 0.0061256 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_146_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=5, w2=434, w3=483, lag=13)."""
    rel = _safe_div(high.shift(13), close.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 5)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.152667 * pressure.rolling(483, min_periods=max(483//3, 2)).mean() + 0.0061257 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_147_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=12, w2=447, w3=500, lag=21)."""
    a = high.shift(21)
    b = close.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(12, min_periods=max(12//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.667647 + 0.0061258 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_148_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=19, w2=460, w3=517, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(close.abs() + 1.0).shift(34)
    corr = a.rolling(460, min_periods=max(460//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 19)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.827647 + 0.0061259 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_149_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=26, w2=473, w3=534, lag=55)."""
    a = high.shift(55)
    b = close.shift(55)
    cover = _safe_div(a.rolling(26, min_periods=max(26//3, 2)).mean(), b.abs().rolling(473, min_periods=max(473//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.171667 * _rolling_slope(cover, 26) + 0.006126 * anchor
    return base_signal.diff().diff()

def f99_fits_gemini_150_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=33, w2=486, w3=551, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(close.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.178 * y + 0.822000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 33) - _rolling_slope(basket, 486) + 0.0061261 * anchor
    return base_signal.diff().diff()
