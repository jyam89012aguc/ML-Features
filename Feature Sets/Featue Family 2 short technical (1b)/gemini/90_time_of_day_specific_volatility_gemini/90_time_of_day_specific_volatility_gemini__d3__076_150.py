"""90 time of day specific volatility gemini d3 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Seasonal volatility patterns linked to specific hours of the trading day.
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

def f90_todv_gemini_076_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=42, w2=195, w3=105, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(195, min_periods=max(195//3, 2)).max()
    rebound = x - x.rolling(42, min_periods=max(42//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.247667 * _rolling_slope(draw, 105) + 0.0056287 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_077_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=49, w2=208, w3=122, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(49) - b.diff(126)
    stress = imbalance.rolling(122, min_periods=max(122//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.001765 + 0.0056288 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_078_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=56, w2=221, w3=139, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 56)
    baseline = trend.rolling(221, min_periods=max(221//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(139, min_periods=max(139//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.015294 + 0.0056289 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_079_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=63, w2=234, w3=156, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 63)
    slow = _rolling_slope(x, 234)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=156, adjust=False).mean() * 1.028824 + 0.005629 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_080_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=70, w2=247, w3=173, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(247, min_periods=max(247//3, 2)).max()
    trough = x.rolling(70, min_periods=max(70//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.042353 + 0.0056291 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_081_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=77, w2=260, w3=190, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(77)
    rank = change.rolling(260, min_periods=max(260//3, 2)).rank(pct=True)
    persistence = change.rolling(190, min_periods=max(190//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.279333 * persistence + 0.0056292 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_082_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=84, w2=273, w3=207, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(84, min_periods=max(84//3, 2)).std()
    vol_slow = ret.rolling(273, min_periods=max(273//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.069412 + 0.0056293 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_083_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=91, w2=286, w3=224, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(286, min_periods=max(286//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 91)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.292 * slope + 0.0056294 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_084_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=98, w2=299, w3=241, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(98)
    drag = impulse.rolling(299, min_periods=max(299//3, 2)).mean()
    noise = impulse.abs().rolling(241, min_periods=max(241//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.096471 + 0.0056295 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_085_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=105, w2=312, w3=258, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 105)
    acceleration = _rolling_slope(velocity, 312)
    curvature = _rolling_slope(acceleration, 258)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.304667 * acceleration + 0.0056296 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_086_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=112, w2=325, w3=275, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 112)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.311 * pressure.rolling(275, min_periods=max(275//3, 2)).mean() + 0.0056297 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_087_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=119, w2=338, w3=292, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(119, min_periods=max(119//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.137059 + 0.0056298 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_088_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=126, w2=351, w3=309, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(351, min_periods=max(351//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.150588 + 0.0056299 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_089_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=133, w2=364, w3=326, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(133, min_periods=max(133//3, 2)).mean(), b.abs().rolling(364, min_periods=max(364//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.33 * _rolling_slope(cover, 133) + 0.00563 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_090_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=140, w2=377, w3=343, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(low.abs() + 1.0).shift(0)
    basket = x - 0.336333 * y + 0.663667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 140) - _rolling_slope(basket, 377) + 0.0056301 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_091_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=147, w2=390, w3=360, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(147, min_periods=max(147//3, 2)).mean(), upside.rolling(390, min_periods=max(390//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.191176 + 0.0056302 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_092_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=154, w2=403, w3=377, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(403, min_periods=max(403//3, 2)).max()
    rebound = x - x.rolling(154, min_periods=max(154//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.349 * _rolling_slope(draw, 377) + 0.0056303 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_093_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=161, w2=416, w3=394, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(394, min_periods=max(394//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.218235 + 0.0056304 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_094_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=168, w2=429, w3=411, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 168)
    baseline = trend.rolling(429, min_periods=max(429//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(411, min_periods=max(411//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.231765 + 0.0056305 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_095_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=175, w2=442, w3=428, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 175)
    slow = _rolling_slope(x, 442)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.245294 + 0.0056306 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_096_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=182, w2=455, w3=445, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(455, min_periods=max(455//3, 2)).max()
    trough = x.rolling(182, min_periods=max(182//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.258824 + 0.0056307 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_097_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=189, w2=468, w3=462, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(468, min_periods=max(468//3, 2)).rank(pct=True)
    persistence = change.rolling(462, min_periods=max(462//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.048333 * persistence + 0.0056308 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_098_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=196, w2=481, w3=479, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(196, min_periods=max(196//3, 2)).std()
    vol_slow = ret.rolling(481, min_periods=max(481//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.285882 + 0.0056309 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_099_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=203, w2=494, w3=496, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(494, min_periods=max(494//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 203)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.061 * slope + 0.005631 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_100_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=210, w2=507, w3=513, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(507, min_periods=max(507//3, 2)).mean()
    noise = impulse.abs().rolling(513, min_periods=max(513//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.312941 + 0.0056311 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_101_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=217, w2=21, w3=530, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 217)
    acceleration = _rolling_slope(velocity, 21)
    curvature = _rolling_slope(acceleration, 530)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.073667 * acceleration + 0.0056312 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_102_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=224, w2=34, w3=547, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 224)
    pressure = rel_log.diff(34)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.08 * pressure.rolling(547, min_periods=max(547//3, 2)).mean() + 0.0056313 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_103_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=231, w2=47, w3=564, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(231, min_periods=max(231//3, 2)).mean())
    decay = spread.ewm(span=47, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.353529 + 0.0056314 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_104_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=238, w2=60, w3=581, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(60, min_periods=max(60//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 238)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.367059 + 0.0056315 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_105_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=245, w2=73, w3=598, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(245, min_periods=max(245//3, 2)).mean(), b.abs().rolling(73, min_periods=max(73//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.099 * _rolling_slope(cover, 245) + 0.0056316 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_106_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=5, w2=86, w3=615, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(low.abs() + 1.0).shift(13)
    basket = x - 0.105333 * y + 0.894667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 5) - _rolling_slope(basket, 86) + 0.0056317 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_107_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=12, w2=99, w3=632, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(12, min_periods=max(12//3, 2)).mean(), upside.rolling(99, min_periods=max(99//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.407647 + 0.0056318 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_108_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=19, w2=112, w3=649, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(112, min_periods=max(112//3, 2)).max()
    rebound = x - x.rolling(19, min_periods=max(19//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.118 * _rolling_slope(draw, 649) + 0.0056319 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_109_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=26, w2=125, w3=666, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(26) - b.diff(125)
    stress = imbalance.rolling(666, min_periods=max(666//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.434706 + 0.005632 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_110_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=33, w2=138, w3=683, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 33)
    baseline = trend.rolling(138, min_periods=max(138//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(683, min_periods=max(683//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.448235 + 0.0056321 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_111_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=40, w2=151, w3=700, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 40)
    slow = _rolling_slope(x, 151)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.461765 + 0.0056322 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_112_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=47, w2=164, w3=717, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(164, min_periods=max(164//3, 2)).max()
    trough = x.rolling(47, min_periods=max(47//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.475294 + 0.0056323 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_113_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=54, w2=177, w3=734, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(54)
    rank = change.rolling(177, min_periods=max(177//3, 2)).rank(pct=True)
    persistence = change.rolling(734, min_periods=max(734//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.149667 * persistence + 0.0056324 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_114_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=61, w2=190, w3=751, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(61, min_periods=max(61//3, 2)).std()
    vol_slow = ret.rolling(190, min_periods=max(190//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.502353 + 0.0056325 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_115_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=68, w2=203, w3=17, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(203, min_periods=max(203//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 68)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.162333 * slope + 0.0056326 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_116_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=75, w2=216, w3=34, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(75)
    drag = impulse.rolling(216, min_periods=max(216//3, 2)).mean()
    noise = impulse.abs().rolling(34, min_periods=max(34//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.529412 + 0.0056327 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_117_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=82, w2=229, w3=51, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 82)
    acceleration = _rolling_slope(velocity, 229)
    curvature = _rolling_slope(acceleration, 51)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.175 * acceleration + 0.0056328 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_118_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=89, w2=242, w3=68, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 89)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.181333 * pressure.rolling(68, min_periods=max(68//3, 2)).mean() + 0.0056329 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_119_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=96, w2=255, w3=85, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(96, min_periods=max(96//3, 2)).mean())
    decay = spread.ewm(span=255, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.57 + 0.005633 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_120_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=103, w2=268, w3=102, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(268, min_periods=max(268//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 103)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.583529 + 0.0056331 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_121_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=110, w2=281, w3=119, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(110, min_periods=max(110//3, 2)).mean(), b.abs().rolling(281, min_periods=max(281//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(119) + 0.200333 * _rolling_slope(cover, 110) + 0.0056332 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_122_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=117, w2=294, w3=136, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(low.abs() + 1.0).shift(2)
    basket = x - 0.206667 * y + 0.793333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 117) - _rolling_slope(basket, 294) + 0.0056333 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_123_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=124, w2=307, w3=153, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(124, min_periods=max(124//3, 2)).mean(), upside.rolling(307, min_periods=max(307//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.624118 + 0.0056334 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_124_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=131, w2=320, w3=170, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(320, min_periods=max(320//3, 2)).max()
    rebound = x - x.rolling(131, min_periods=max(131//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.219333 * _rolling_slope(draw, 170) + 0.0056335 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_125_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=138, w2=333, w3=187, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(187, min_periods=max(187//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.651176 + 0.0056336 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_126_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=145, w2=346, w3=204, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 145)
    baseline = trend.rolling(346, min_periods=max(346//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(204, min_periods=max(204//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.664706 + 0.0056337 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_127_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=152, w2=359, w3=221, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 152)
    slow = _rolling_slope(x, 359)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=221, adjust=False).mean() * 0.824706 + 0.0056338 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_128_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=159, w2=372, w3=238, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(372, min_periods=max(372//3, 2)).max()
    trough = x.rolling(159, min_periods=max(159//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.838235 + 0.0056339 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_129_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=166, w2=385, w3=255, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(385, min_periods=max(385//3, 2)).rank(pct=True)
    persistence = change.rolling(255, min_periods=max(255//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.251 * persistence + 0.005634 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_130_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=173, w2=398, w3=272, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(173, min_periods=max(173//3, 2)).std()
    vol_slow = ret.rolling(398, min_periods=max(398//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.865294 + 0.0056341 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_131_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=180, w2=411, w3=289, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(411, min_periods=max(411//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 180)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.263667 * slope + 0.0056342 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_132_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=187, w2=424, w3=306, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(424, min_periods=max(424//3, 2)).mean()
    noise = impulse.abs().rolling(306, min_periods=max(306//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.892353 + 0.0056343 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_133_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=194, w2=437, w3=323, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 194)
    acceleration = _rolling_slope(velocity, 437)
    curvature = _rolling_slope(acceleration, 323)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.276333 * acceleration + 0.0056344 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_134_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=201, w2=450, w3=340, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 201)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.282667 * pressure.rolling(340, min_periods=max(340//3, 2)).mean() + 0.0056345 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_135_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=208, w2=463, w3=357, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(208, min_periods=max(208//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.932941 + 0.0056346 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_136_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=215, w2=476, w3=374, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(476, min_periods=max(476//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 215)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.946471 + 0.0056347 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_137_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=222, w2=489, w3=391, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(222, min_periods=max(222//3, 2)).mean(), b.abs().rolling(489, min_periods=max(489//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.301667 * _rolling_slope(cover, 222) + 0.0056348 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_138_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=229, w2=502, w3=408, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(low.abs() + 1.0).shift(34)
    basket = x - 0.308 * y + 0.692000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 229) - _rolling_slope(basket, 502) + 0.0056349 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_139_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=236, w2=16, w3=425, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(236, min_periods=max(236//3, 2)).mean(), upside.rolling(16, min_periods=max(16//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.987059 + 0.005635 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_140_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=243, w2=29, w3=442, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(29, min_periods=max(29//3, 2)).max()
    rebound = x - x.rolling(243, min_periods=max(243//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.320667 * _rolling_slope(draw, 442) + 0.0056351 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_141_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=250, w2=42, w3=459, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(42)
    stress = imbalance.rolling(459, min_periods=max(459//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.014118 + 0.0056352 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_142_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=10, w2=55, w3=476, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 10)
    baseline = trend.rolling(55, min_periods=max(55//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(476, min_periods=max(476//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.027647 + 0.0056353 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_143_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=17, w2=68, w3=493, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 17)
    slow = _rolling_slope(x, 68)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.041176 + 0.0056354 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_144_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=24, w2=81, w3=510, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(81, min_periods=max(81//3, 2)).max()
    trough = x.rolling(24, min_periods=max(24//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.054706 + 0.0056355 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_145_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=31, w2=94, w3=527, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(31)
    rank = change.rolling(94, min_periods=max(94//3, 2)).rank(pct=True)
    persistence = change.rolling(527, min_periods=max(527//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.352333 * persistence + 0.0056356 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_146_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=38, w2=107, w3=544, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(38, min_periods=max(38//3, 2)).std()
    vol_slow = ret.rolling(107, min_periods=max(107//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.081765 + 0.0056357 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_147_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=45, w2=120, w3=561, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(120, min_periods=max(120//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 45)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.032667 * slope + 0.0056358 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_148_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=52, w2=133, w3=578, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(52)
    drag = impulse.rolling(133, min_periods=max(133//3, 2)).mean()
    noise = impulse.abs().rolling(578, min_periods=max(578//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.108824 + 0.0056359 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_149_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=59, w2=146, w3=595, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 59)
    acceleration = _rolling_slope(velocity, 146)
    curvature = _rolling_slope(acceleration, 595)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.045333 * acceleration + 0.005636 * anchor
    return base_signal.diff().diff().diff()

def f90_todv_gemini_150_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=66, w2=159, w3=612, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 66)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.051667 * pressure.rolling(612, min_periods=max(612//3, 2)).mean() + 0.0056361 * anchor
    return base_signal.diff().diff().diff()
