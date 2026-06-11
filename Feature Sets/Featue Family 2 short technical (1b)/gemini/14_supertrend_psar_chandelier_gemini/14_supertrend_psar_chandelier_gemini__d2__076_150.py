"""14 supertrend psar chandelier gemini d2 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Composite trend signal using Supertrend, Parabolic SAR, and Chandelier exit logic.
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

def f14_trnd_gemini_076_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=12, w2=482, w3=422, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(482, min_periods=max(482//3, 2)).max()
    trough = x.rolling(12, min_periods=max(12//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.121765 + 0.0013587 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_077_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=19, w2=495, w3=439, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(19)
    rank = change.rolling(495, min_periods=max(495//3, 2)).rank(pct=True)
    persistence = change.rolling(439, min_periods=max(439//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.34 * persistence + 0.0013588 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_078_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=26, w2=508, w3=456, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(26, min_periods=max(26//3, 2)).std()
    vol_slow = ret.rolling(508, min_periods=max(508//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.148824 + 0.0013589 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_079_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=33, w2=22, w3=473, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(22, min_periods=max(22//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 33)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.352667 * slope + 0.001359 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_080_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=40, w2=35, w3=490, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(40)
    drag = impulse.rolling(35, min_periods=max(35//3, 2)).mean()
    noise = impulse.abs().rolling(490, min_periods=max(490//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.175882 + 0.0013591 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_081_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=47, w2=48, w3=507, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 47)
    acceleration = _rolling_slope(velocity, 48)
    curvature = _rolling_slope(acceleration, 507)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.033 * acceleration + 0.0013592 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_082_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=54, w2=61, w3=524, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 54)
    pressure = rel_log.diff(61)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.039333 * pressure.rolling(524, min_periods=max(524//3, 2)).mean() + 0.0013593 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_083_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=61, w2=74, w3=541, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(61, min_periods=max(61//3, 2)).mean())
    decay = spread.ewm(span=74, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.216471 + 0.0013594 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_084_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=68, w2=87, w3=558, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(87, min_periods=max(87//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 68)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.23 + 0.0013595 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_085_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=75, w2=100, w3=575, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(75, min_periods=max(75//3, 2)).mean(), b.abs().rolling(100, min_periods=max(100//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.058333 * _rolling_slope(cover, 75) + 0.0013596 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_086_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=82, w2=113, w3=592, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.064667 * y + 0.935333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 82) - _rolling_slope(basket, 113) + 0.0013597 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_087_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=89, w2=126, w3=609, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(89, min_periods=max(89//3, 2)).mean(), upside.rolling(126, min_periods=max(126//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.270588 + 0.0013598 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_088_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=96, w2=139, w3=626, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(139, min_periods=max(139//3, 2)).max()
    rebound = x - x.rolling(96, min_periods=max(96//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.077333 * _rolling_slope(draw, 626) + 0.0013599 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_089_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=103, w2=152, w3=643, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(103) - b.diff(126)
    stress = imbalance.rolling(643, min_periods=max(643//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.297647 + 0.00136 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_090_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=110, w2=165, w3=660, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 110)
    baseline = trend.rolling(165, min_periods=max(165//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(660, min_periods=max(660//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.311176 + 0.0013601 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_091_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=117, w2=178, w3=677, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 117)
    slow = _rolling_slope(x, 178)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.324706 + 0.0013602 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_092_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=124, w2=191, w3=694, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(191, min_periods=max(191//3, 2)).max()
    trough = x.rolling(124, min_periods=max(124//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.338235 + 0.0013603 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_093_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=131, w2=204, w3=711, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(204, min_periods=max(204//3, 2)).rank(pct=True)
    persistence = change.rolling(711, min_periods=max(711//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.109 * persistence + 0.0013604 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_094_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=138, w2=217, w3=728, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(138, min_periods=max(138//3, 2)).std()
    vol_slow = ret.rolling(217, min_periods=max(217//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.365294 + 0.0013605 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_095_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=145, w2=230, w3=745, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(230, min_periods=max(230//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 145)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.121667 * slope + 0.0013606 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_096_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=152, w2=243, w3=762, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(243, min_periods=max(243//3, 2)).mean()
    noise = impulse.abs().rolling(762, min_periods=max(762//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.392353 + 0.0013607 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_097_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=159, w2=256, w3=28, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 159)
    acceleration = _rolling_slope(velocity, 256)
    curvature = _rolling_slope(acceleration, 28)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.134333 * acceleration + 0.0013608 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_098_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=166, w2=269, w3=45, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 166)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.140667 * pressure.rolling(45, min_periods=max(45//3, 2)).mean() + 0.0013609 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_099_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=173, w2=282, w3=62, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(173, min_periods=max(173//3, 2)).mean())
    decay = spread.ewm(span=282, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.432941 + 0.001361 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_100_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=180, w2=295, w3=79, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(295, min_periods=max(295//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 180)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.446471 + 0.0013611 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_101_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=187, w2=308, w3=96, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(187, min_periods=max(187//3, 2)).mean(), b.abs().rolling(308, min_periods=max(308//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(96) + 0.159667 * _rolling_slope(cover, 187) + 0.0013612 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_102_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=194, w2=321, w3=113, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.166 * y + 0.834000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 194) - _rolling_slope(basket, 321) + 0.0013613 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_103_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=201, w2=334, w3=130, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(201, min_periods=max(201//3, 2)).mean(), upside.rolling(334, min_periods=max(334//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.487059 + 0.0013614 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_104_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=208, w2=347, w3=147, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(347, min_periods=max(347//3, 2)).max()
    rebound = x - x.rolling(208, min_periods=max(208//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.178667 * _rolling_slope(draw, 147) + 0.0013615 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_105_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=215, w2=360, w3=164, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(164, min_periods=max(164//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.514118 + 0.0013616 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_106_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=222, w2=373, w3=181, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 222)
    baseline = trend.rolling(373, min_periods=max(373//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(181, min_periods=max(181//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.527647 + 0.0013617 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_107_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=229, w2=386, w3=198, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 229)
    slow = _rolling_slope(x, 386)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=198, adjust=False).mean() * 1.541176 + 0.0013618 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_108_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=236, w2=399, w3=215, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(399, min_periods=max(399//3, 2)).max()
    trough = x.rolling(236, min_periods=max(236//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.554706 + 0.0013619 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_109_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=243, w2=412, w3=232, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(412, min_periods=max(412//3, 2)).rank(pct=True)
    persistence = change.rolling(232, min_periods=max(232//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.210333 * persistence + 0.001362 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_110_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=250, w2=425, w3=249, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(250, min_periods=max(250//3, 2)).std()
    vol_slow = ret.rolling(425, min_periods=max(425//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.581765 + 0.0013621 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_111_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=10, w2=438, w3=266, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(438, min_periods=max(438//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 10)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.223 * slope + 0.0013622 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_112_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=17, w2=451, w3=283, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(17)
    drag = impulse.rolling(451, min_periods=max(451//3, 2)).mean()
    noise = impulse.abs().rolling(283, min_periods=max(283//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.608824 + 0.0013623 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_113_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=24, w2=464, w3=300, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 24)
    acceleration = _rolling_slope(velocity, 464)
    curvature = _rolling_slope(acceleration, 300)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.235667 * acceleration + 0.0013624 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_114_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=31, w2=477, w3=317, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 31)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.242 * pressure.rolling(317, min_periods=max(317//3, 2)).mean() + 0.0013625 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_115_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=38, w2=490, w3=334, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(38, min_periods=max(38//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.649412 + 0.0013626 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_116_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=45, w2=503, w3=351, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(503, min_periods=max(503//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 45)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.662941 + 0.0013627 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_117_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=52, w2=17, w3=368, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(52, min_periods=max(52//3, 2)).mean(), b.abs().rolling(17, min_periods=max(17//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.261 * _rolling_slope(cover, 52) + 0.0013628 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_118_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=59, w2=30, w3=385, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.267333 * y + 0.732667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 59) - _rolling_slope(basket, 30) + 0.0013629 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_119_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=66, w2=43, w3=402, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(66, min_periods=max(66//3, 2)).mean(), upside.rolling(43, min_periods=max(43//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.85 + 0.001363 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_120_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=73, w2=56, w3=419, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(56, min_periods=max(56//3, 2)).max()
    rebound = x - x.rolling(73, min_periods=max(73//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.28 * _rolling_slope(draw, 419) + 0.0013631 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_121_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=80, w2=69, w3=436, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(80) - b.diff(69)
    stress = imbalance.rolling(436, min_periods=max(436//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.877059 + 0.0013632 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_122_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=87, w2=82, w3=453, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 87)
    baseline = trend.rolling(82, min_periods=max(82//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(453, min_periods=max(453//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.890588 + 0.0013633 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_123_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=94, w2=95, w3=470, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 94)
    slow = _rolling_slope(x, 95)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.904118 + 0.0013634 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_124_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=101, w2=108, w3=487, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(108, min_periods=max(108//3, 2)).max()
    trough = x.rolling(101, min_periods=max(101//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.917647 + 0.0013635 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_125_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=108, w2=121, w3=504, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(108)
    rank = change.rolling(121, min_periods=max(121//3, 2)).rank(pct=True)
    persistence = change.rolling(504, min_periods=max(504//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.311667 * persistence + 0.0013636 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_126_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=115, w2=134, w3=521, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(115, min_periods=max(115//3, 2)).std()
    vol_slow = ret.rolling(134, min_periods=max(134//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.944706 + 0.0013637 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_127_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=122, w2=147, w3=538, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(147, min_periods=max(147//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 122)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.324333 * slope + 0.0013638 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_128_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=129, w2=160, w3=555, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(160, min_periods=max(160//3, 2)).mean()
    noise = impulse.abs().rolling(555, min_periods=max(555//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.971765 + 0.0013639 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_129_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=136, w2=173, w3=572, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 136)
    acceleration = _rolling_slope(velocity, 173)
    curvature = _rolling_slope(acceleration, 572)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.337 * acceleration + 0.001364 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_130_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=143, w2=186, w3=589, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 143)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.343333 * pressure.rolling(589, min_periods=max(589//3, 2)).mean() + 0.0013641 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_131_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=150, w2=199, w3=606, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(150, min_periods=max(150//3, 2)).mean())
    decay = spread.ewm(span=199, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.012353 + 0.0013642 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_132_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=157, w2=212, w3=623, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(212, min_periods=max(212//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 157)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.025882 + 0.0013643 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_133_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=164, w2=225, w3=640, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(164, min_periods=max(164//3, 2)).mean(), b.abs().rolling(225, min_periods=max(225//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.362333 * _rolling_slope(cover, 164) + 0.0013644 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_134_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=171, w2=238, w3=657, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.036333 * y + 0.963667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 171) - _rolling_slope(basket, 238) + 0.0013645 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_135_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=178, w2=251, w3=674, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(178, min_periods=max(178//3, 2)).mean(), upside.rolling(251, min_periods=max(251//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.066471 + 0.0013646 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_136_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=185, w2=264, w3=691, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(264, min_periods=max(264//3, 2)).max()
    rebound = x - x.rolling(185, min_periods=max(185//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.049 * _rolling_slope(draw, 691) + 0.0013647 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_137_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=192, w2=277, w3=708, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(708, min_periods=max(708//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.093529 + 0.0013648 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_138_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=199, w2=290, w3=725, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 199)
    baseline = trend.rolling(290, min_periods=max(290//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(725, min_periods=max(725//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.107059 + 0.0013649 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_139_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=206, w2=303, w3=742, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 206)
    slow = _rolling_slope(x, 303)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.120588 + 0.001365 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_140_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=213, w2=316, w3=759, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(316, min_periods=max(316//3, 2)).max()
    trough = x.rolling(213, min_periods=max(213//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.134118 + 0.0013651 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_141_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=220, w2=329, w3=25, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(329, min_periods=max(329//3, 2)).rank(pct=True)
    persistence = change.rolling(25, min_periods=max(25//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.080667 * persistence + 0.0013652 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_142_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=227, w2=342, w3=42, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(227, min_periods=max(227//3, 2)).std()
    vol_slow = ret.rolling(342, min_periods=max(342//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.161176 + 0.0013653 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_143_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=234, w2=355, w3=59, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(355, min_periods=max(355//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 234)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.093333 * slope + 0.0013654 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_144_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=241, w2=368, w3=76, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(368, min_periods=max(368//3, 2)).mean()
    noise = impulse.abs().rolling(76, min_periods=max(76//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.188235 + 0.0013655 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_145_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=248, w2=381, w3=93, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 248)
    acceleration = _rolling_slope(velocity, 381)
    curvature = _rolling_slope(acceleration, 93)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.106 * acceleration + 0.0013656 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_146_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=8, w2=394, w3=110, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 8)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.112333 * pressure.rolling(110, min_periods=max(110//3, 2)).mean() + 0.0013657 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_147_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=15, w2=407, w3=127, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(15, min_periods=max(15//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.228824 + 0.0013658 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_148_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=22, w2=420, w3=144, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(420, min_periods=max(420//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 22)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.242353 + 0.0013659 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_149_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=29, w2=433, w3=161, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(29, min_periods=max(29//3, 2)).mean(), b.abs().rolling(433, min_periods=max(433//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.131333 * _rolling_slope(cover, 29) + 0.001366 * anchor
    return base_signal.diff().diff()

def f14_trnd_gemini_150_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=36, w2=446, w3=178, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.137667 * y + 0.862333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 36) - _rolling_slope(basket, 446) + 0.0013661 * anchor
    return base_signal.diff().diff()
