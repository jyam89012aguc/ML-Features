"""05 failed breakout dynamics gemini d2 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Price action failing to maintain levels above prior resistance, indicating bull traps.
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

def f05_fbrk_gemini_076_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=158, w2=91, w3=25, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(91, min_periods=max(91//3, 2)).max()
    trough = x.rolling(158, min_periods=max(158//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.520588 + 0.0002387 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_077_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=165, w2=104, w3=42, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(104, min_periods=max(104//3, 2)).rank(pct=True)
    persistence = change.rolling(42, min_periods=max(42//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.193667 * persistence + 0.0002388 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_078_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=172, w2=117, w3=59, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(172, min_periods=max(172//3, 2)).std()
    vol_slow = ret.rolling(117, min_periods=max(117//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.547647 + 0.0002389 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_079_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=179, w2=130, w3=76, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(130, min_periods=max(130//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 179)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.206333 * slope + 0.000239 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_080_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=186, w2=143, w3=93, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(143, min_periods=max(143//3, 2)).mean()
    noise = impulse.abs().rolling(93, min_periods=max(93//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.574706 + 0.0002391 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_081_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=193, w2=156, w3=110, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 193)
    acceleration = _rolling_slope(velocity, 156)
    curvature = _rolling_slope(acceleration, 110)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.219 * acceleration + 0.0002392 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_082_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=200, w2=169, w3=127, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 200)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.225333 * pressure.rolling(127, min_periods=max(127//3, 2)).mean() + 0.0002393 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_083_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=207, w2=182, w3=144, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(207, min_periods=max(207//3, 2)).mean())
    decay = spread.ewm(span=182, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.615294 + 0.0002394 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_084_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=214, w2=195, w3=161, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(195, min_periods=max(195//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 214)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.628824 + 0.0002395 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_085_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=221, w2=208, w3=178, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(221, min_periods=max(221//3, 2)).mean(), b.abs().rolling(208, min_periods=max(208//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.244333 * _rolling_slope(cover, 221) + 0.0002396 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_086_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=228, w2=221, w3=195, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.250667 * y + 0.749333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 228) - _rolling_slope(basket, 221) + 0.0002397 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_087_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=235, w2=234, w3=212, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(235, min_periods=max(235//3, 2)).mean(), upside.rolling(234, min_periods=max(234//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.669412 + 0.0002398 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_088_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=242, w2=247, w3=229, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(247, min_periods=max(247//3, 2)).max()
    rebound = x - x.rolling(242, min_periods=max(242//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.263333 * _rolling_slope(draw, 229) + 0.0002399 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_089_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=249, w2=260, w3=246, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(246, min_periods=max(246//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.842941 + 0.00024 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_090_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=9, w2=273, w3=263, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 9)
    baseline = trend.rolling(273, min_periods=max(273//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(263, min_periods=max(263//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.856471 + 0.0002401 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_091_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=16, w2=286, w3=280, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 16)
    slow = _rolling_slope(x, 286)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=280, adjust=False).mean() * 0.87 + 0.0002402 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_092_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=23, w2=299, w3=297, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(299, min_periods=max(299//3, 2)).max()
    trough = x.rolling(23, min_periods=max(23//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.883529 + 0.0002403 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_093_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=30, w2=312, w3=314, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(30)
    rank = change.rolling(312, min_periods=max(312//3, 2)).rank(pct=True)
    persistence = change.rolling(314, min_periods=max(314//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.295 * persistence + 0.0002404 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_094_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=37, w2=325, w3=331, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(37, min_periods=max(37//3, 2)).std()
    vol_slow = ret.rolling(325, min_periods=max(325//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.910588 + 0.0002405 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_095_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=44, w2=338, w3=348, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(338, min_periods=max(338//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 44)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.307667 * slope + 0.0002406 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_096_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=51, w2=351, w3=365, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(51)
    drag = impulse.rolling(351, min_periods=max(351//3, 2)).mean()
    noise = impulse.abs().rolling(365, min_periods=max(365//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.937647 + 0.0002407 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_097_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=58, w2=364, w3=382, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 58)
    acceleration = _rolling_slope(velocity, 364)
    curvature = _rolling_slope(acceleration, 382)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.320333 * acceleration + 0.0002408 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_098_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=65, w2=377, w3=399, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 65)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.326667 * pressure.rolling(399, min_periods=max(399//3, 2)).mean() + 0.0002409 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_099_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=72, w2=390, w3=416, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(72, min_periods=max(72//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.978235 + 0.000241 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_100_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=79, w2=403, w3=433, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(403, min_periods=max(403//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 79)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.991765 + 0.0002411 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_101_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=86, w2=416, w3=450, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(86, min_periods=max(86//3, 2)).mean(), b.abs().rolling(416, min_periods=max(416//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.345667 * _rolling_slope(cover, 86) + 0.0002412 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_102_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=93, w2=429, w3=467, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.352 * y + 0.648000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 93) - _rolling_slope(basket, 429) + 0.0002413 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_103_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=100, w2=442, w3=484, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(100, min_periods=max(100//3, 2)).mean(), upside.rolling(442, min_periods=max(442//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.032353 + 0.0002414 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_104_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=107, w2=455, w3=501, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(455, min_periods=max(455//3, 2)).max()
    rebound = x - x.rolling(107, min_periods=max(107//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.032333 * _rolling_slope(draw, 501) + 0.0002415 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_105_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=114, w2=468, w3=518, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(114) - b.diff(126)
    stress = imbalance.rolling(518, min_periods=max(518//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.059412 + 0.0002416 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_106_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=121, w2=481, w3=535, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 121)
    baseline = trend.rolling(481, min_periods=max(481//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(535, min_periods=max(535//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.072941 + 0.0002417 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_107_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=128, w2=494, w3=552, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 128)
    slow = _rolling_slope(x, 494)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.086471 + 0.0002418 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_108_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=135, w2=507, w3=569, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(507, min_periods=max(507//3, 2)).max()
    trough = x.rolling(135, min_periods=max(135//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.1 + 0.0002419 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_109_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=142, w2=21, w3=586, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(21, min_periods=max(21//3, 2)).rank(pct=True)
    persistence = change.rolling(586, min_periods=max(586//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.064 * persistence + 0.000242 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_110_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=149, w2=34, w3=603, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(149, min_periods=max(149//3, 2)).std()
    vol_slow = ret.rolling(34, min_periods=max(34//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.127059 + 0.0002421 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_111_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=156, w2=47, w3=620, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(47, min_periods=max(47//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 156)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.076667 * slope + 0.0002422 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_112_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=163, w2=60, w3=637, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(60, min_periods=max(60//3, 2)).mean()
    noise = impulse.abs().rolling(637, min_periods=max(637//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.154118 + 0.0002423 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_113_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=170, w2=73, w3=654, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 170)
    acceleration = _rolling_slope(velocity, 73)
    curvature = _rolling_slope(acceleration, 654)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.089333 * acceleration + 0.0002424 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_114_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=177, w2=86, w3=671, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 177)
    pressure = rel_log.diff(86)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.095667 * pressure.rolling(671, min_periods=max(671//3, 2)).mean() + 0.0002425 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_115_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=184, w2=99, w3=688, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(184, min_periods=max(184//3, 2)).mean())
    decay = spread.ewm(span=99, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.194706 + 0.0002426 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_116_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=191, w2=112, w3=705, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(112, min_periods=max(112//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 191)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.208235 + 0.0002427 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_117_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=198, w2=125, w3=722, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(198, min_periods=max(198//3, 2)).mean(), b.abs().rolling(125, min_periods=max(125//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.114667 * _rolling_slope(cover, 198) + 0.0002428 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_118_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=205, w2=138, w3=739, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.121 * y + 0.879000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 205) - _rolling_slope(basket, 138) + 0.0002429 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_119_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=212, w2=151, w3=756, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(212, min_periods=max(212//3, 2)).mean(), upside.rolling(151, min_periods=max(151//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.248824 + 0.000243 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_120_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=219, w2=164, w3=22, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(164, min_periods=max(164//3, 2)).max()
    rebound = x - x.rolling(219, min_periods=max(219//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.133667 * _rolling_slope(draw, 22) + 0.0002431 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_121_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=226, w2=177, w3=39, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(39, min_periods=max(39//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.275882 + 0.0002432 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_122_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=233, w2=190, w3=56, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 233)
    baseline = trend.rolling(190, min_periods=max(190//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(56, min_periods=max(56//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.289412 + 0.0002433 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_123_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=240, w2=203, w3=73, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 240)
    slow = _rolling_slope(x, 203)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=73, adjust=False).mean() * 1.302941 + 0.0002434 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_124_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=247, w2=216, w3=90, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(216, min_periods=max(216//3, 2)).max()
    trough = x.rolling(247, min_periods=max(247//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.316471 + 0.0002435 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_125_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=7, w2=229, w3=107, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(7)
    rank = change.rolling(229, min_periods=max(229//3, 2)).rank(pct=True)
    persistence = change.rolling(107, min_periods=max(107//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.165333 * persistence + 0.0002436 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_126_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=14, w2=242, w3=124, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(14, min_periods=max(14//3, 2)).std()
    vol_slow = ret.rolling(242, min_periods=max(242//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.343529 + 0.0002437 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_127_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=21, w2=255, w3=141, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(255, min_periods=max(255//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 21)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.178 * slope + 0.0002438 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_128_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=28, w2=268, w3=158, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(28)
    drag = impulse.rolling(268, min_periods=max(268//3, 2)).mean()
    noise = impulse.abs().rolling(158, min_periods=max(158//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.370588 + 0.0002439 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_129_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=35, w2=281, w3=175, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 35)
    acceleration = _rolling_slope(velocity, 281)
    curvature = _rolling_slope(acceleration, 175)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.190667 * acceleration + 0.000244 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_130_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=42, w2=294, w3=192, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 42)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.197 * pressure.rolling(192, min_periods=max(192//3, 2)).mean() + 0.0002441 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_131_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=49, w2=307, w3=209, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(49, min_periods=max(49//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.411176 + 0.0002442 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_132_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=56, w2=320, w3=226, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(320, min_periods=max(320//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 56)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.424706 + 0.0002443 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_133_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=63, w2=333, w3=243, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(63, min_periods=max(63//3, 2)).mean(), b.abs().rolling(333, min_periods=max(333//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.216 * _rolling_slope(cover, 63) + 0.0002444 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_134_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=70, w2=346, w3=260, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.222333 * y + 0.777667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 70) - _rolling_slope(basket, 346) + 0.0002445 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_135_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=77, w2=359, w3=277, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(77, min_periods=max(77//3, 2)).mean(), upside.rolling(359, min_periods=max(359//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.465294 + 0.0002446 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_136_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=84, w2=372, w3=294, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(372, min_periods=max(372//3, 2)).max()
    rebound = x - x.rolling(84, min_periods=max(84//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.235 * _rolling_slope(draw, 294) + 0.0002447 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_137_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=91, w2=385, w3=311, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(91) - b.diff(126)
    stress = imbalance.rolling(311, min_periods=max(311//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.492353 + 0.0002448 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_138_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=98, w2=398, w3=328, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 98)
    baseline = trend.rolling(398, min_periods=max(398//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(328, min_periods=max(328//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.505882 + 0.0002449 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_139_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=105, w2=411, w3=345, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 105)
    slow = _rolling_slope(x, 411)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.519412 + 0.000245 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_140_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=112, w2=424, w3=362, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(424, min_periods=max(424//3, 2)).max()
    trough = x.rolling(112, min_periods=max(112//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.532941 + 0.0002451 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_141_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=119, w2=437, w3=379, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(119)
    rank = change.rolling(437, min_periods=max(437//3, 2)).rank(pct=True)
    persistence = change.rolling(379, min_periods=max(379//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.266667 * persistence + 0.0002452 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_142_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=126, w2=450, w3=396, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(126, min_periods=max(126//3, 2)).std()
    vol_slow = ret.rolling(450, min_periods=max(450//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.56 + 0.0002453 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_143_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=133, w2=463, w3=413, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(463, min_periods=max(463//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 133)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.279333 * slope + 0.0002454 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_144_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=140, w2=476, w3=430, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(476, min_periods=max(476//3, 2)).mean()
    noise = impulse.abs().rolling(430, min_periods=max(430//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.587059 + 0.0002455 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_145_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=147, w2=489, w3=447, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 147)
    acceleration = _rolling_slope(velocity, 489)
    curvature = _rolling_slope(acceleration, 447)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.292 * acceleration + 0.0002456 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_146_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=154, w2=502, w3=464, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 154)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.298333 * pressure.rolling(464, min_periods=max(464//3, 2)).mean() + 0.0002457 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_147_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=161, w2=16, w3=481, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(161, min_periods=max(161//3, 2)).mean())
    decay = spread.ewm(span=16, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.627647 + 0.0002458 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_148_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=168, w2=29, w3=498, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(29, min_periods=max(29//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 168)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.641176 + 0.0002459 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_149_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=175, w2=42, w3=515, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(175, min_periods=max(175//3, 2)).mean(), b.abs().rolling(42, min_periods=max(42//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.317333 * _rolling_slope(cover, 175) + 0.000246 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_150_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=182, w2=55, w3=532, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.323667 * y + 0.676333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 182) - _rolling_slope(basket, 55) + 0.0002461 * anchor
    return base_signal.diff().diff()
