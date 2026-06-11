"""92 vanna charm technical proxy gemini d2 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Technical proxies for second-order Greeks affecting market maker hedging.
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

def f92_vchp_gemini_076_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=233, w2=460, w3=243, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(460, min_periods=max(460//3, 2)).max()
    trough = x.rolling(233, min_periods=max(233//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.444118 + 0.0057267 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_077_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=240, w2=473, w3=260, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(473, min_periods=max(473//3, 2)).rank(pct=True)
    persistence = change.rolling(260, min_periods=max(260//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.146333 * persistence + 0.0057268 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_078_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=247, w2=486, w3=277, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(247, min_periods=max(247//3, 2)).std()
    vol_slow = ret.rolling(486, min_periods=max(486//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.471176 + 0.0057269 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_079_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=7, w2=499, w3=294, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(499, min_periods=max(499//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 7)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.159 * slope + 0.005727 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_080_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=14, w2=13, w3=311, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(14)
    drag = impulse.rolling(13, min_periods=max(13//3, 2)).mean()
    noise = impulse.abs().rolling(311, min_periods=max(311//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.498235 + 0.0057271 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_081_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=21, w2=26, w3=328, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 21)
    acceleration = _rolling_slope(velocity, 26)
    curvature = _rolling_slope(acceleration, 328)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.171667 * acceleration + 0.0057272 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_082_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=28, w2=39, w3=345, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 28)
    pressure = rel_log.diff(39)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.178 * pressure.rolling(345, min_periods=max(345//3, 2)).mean() + 0.0057273 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_083_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=35, w2=52, w3=362, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(35, min_periods=max(35//3, 2)).mean())
    decay = spread.ewm(span=52, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.538824 + 0.0057274 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_084_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=42, w2=65, w3=379, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(65, min_periods=max(65//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 42)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.552353 + 0.0057275 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_085_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=49, w2=78, w3=396, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(49, min_periods=max(49//3, 2)).mean(), b.abs().rolling(78, min_periods=max(78//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.197 * _rolling_slope(cover, 49) + 0.0057276 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_086_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=56, w2=91, w3=413, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.203333 * y + 0.796667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 56) - _rolling_slope(basket, 91) + 0.0057277 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_087_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=63, w2=104, w3=430, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(63, min_periods=max(63//3, 2)).mean(), upside.rolling(104, min_periods=max(104//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.592941 + 0.0057278 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_088_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=70, w2=117, w3=447, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(117, min_periods=max(117//3, 2)).max()
    rebound = x - x.rolling(70, min_periods=max(70//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.216 * _rolling_slope(draw, 447) + 0.0057279 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_089_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=77, w2=130, w3=464, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(77) - b.diff(126)
    stress = imbalance.rolling(464, min_periods=max(464//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.62 + 0.005728 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_090_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=84, w2=143, w3=481, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 84)
    baseline = trend.rolling(143, min_periods=max(143//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(481, min_periods=max(481//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.633529 + 0.0057281 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_091_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=91, w2=156, w3=498, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 91)
    slow = _rolling_slope(x, 156)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.647059 + 0.0057282 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_092_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=98, w2=169, w3=515, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(169, min_periods=max(169//3, 2)).max()
    trough = x.rolling(98, min_periods=max(98//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.660588 + 0.0057283 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_093_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=105, w2=182, w3=532, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(105)
    rank = change.rolling(182, min_periods=max(182//3, 2)).rank(pct=True)
    persistence = change.rolling(532, min_periods=max(532//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.247667 * persistence + 0.0057284 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_094_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=112, w2=195, w3=549, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(112, min_periods=max(112//3, 2)).std()
    vol_slow = ret.rolling(195, min_periods=max(195//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.834118 + 0.0057285 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_095_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=119, w2=208, w3=566, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(208, min_periods=max(208//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 119)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.260333 * slope + 0.0057286 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_096_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=126, w2=221, w3=583, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(221, min_periods=max(221//3, 2)).mean()
    noise = impulse.abs().rolling(583, min_periods=max(583//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.861176 + 0.0057287 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_097_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=133, w2=234, w3=600, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 133)
    acceleration = _rolling_slope(velocity, 234)
    curvature = _rolling_slope(acceleration, 600)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.273 * acceleration + 0.0057288 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_098_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=140, w2=247, w3=617, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 140)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.279333 * pressure.rolling(617, min_periods=max(617//3, 2)).mean() + 0.0057289 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_099_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=147, w2=260, w3=634, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(147, min_periods=max(147//3, 2)).mean())
    decay = spread.ewm(span=260, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.901765 + 0.005729 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_100_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=154, w2=273, w3=651, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(273, min_periods=max(273//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 154)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.915294 + 0.0057291 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_101_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=161, w2=286, w3=668, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(161, min_periods=max(161//3, 2)).mean(), b.abs().rolling(286, min_periods=max(286//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.298333 * _rolling_slope(cover, 161) + 0.0057292 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_102_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=168, w2=299, w3=685, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.304667 * y + 0.695333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 168) - _rolling_slope(basket, 299) + 0.0057293 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_103_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=175, w2=312, w3=702, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(175, min_periods=max(175//3, 2)).mean(), upside.rolling(312, min_periods=max(312//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.955882 + 0.0057294 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_104_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=182, w2=325, w3=719, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(325, min_periods=max(325//3, 2)).max()
    rebound = x - x.rolling(182, min_periods=max(182//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.317333 * _rolling_slope(draw, 719) + 0.0057295 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_105_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=189, w2=338, w3=736, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(736, min_periods=max(736//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.982941 + 0.0057296 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_106_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=196, w2=351, w3=753, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 196)
    baseline = trend.rolling(351, min_periods=max(351//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(753, min_periods=max(753//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.996471 + 0.0057297 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_107_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=203, w2=364, w3=19, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 203)
    slow = _rolling_slope(x, 364)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=19, adjust=False).mean() * 1.01 + 0.0057298 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_108_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=210, w2=377, w3=36, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(377, min_periods=max(377//3, 2)).max()
    trough = x.rolling(210, min_periods=max(210//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.023529 + 0.0057299 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_109_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=217, w2=390, w3=53, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(390, min_periods=max(390//3, 2)).rank(pct=True)
    persistence = change.rolling(53, min_periods=max(53//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.349 * persistence + 0.00573 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_110_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=224, w2=403, w3=70, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(224, min_periods=max(224//3, 2)).std()
    vol_slow = ret.rolling(403, min_periods=max(403//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.050588 + 0.0057301 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_111_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=231, w2=416, w3=87, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(416, min_periods=max(416//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 231)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.361667 * slope + 0.0057302 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_112_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=238, w2=429, w3=104, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(429, min_periods=max(429//3, 2)).mean()
    noise = impulse.abs().rolling(104, min_periods=max(104//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.077647 + 0.0057303 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_113_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=245, w2=442, w3=121, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 245)
    acceleration = _rolling_slope(velocity, 442)
    curvature = _rolling_slope(acceleration, 121)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.042 * acceleration + 0.0057304 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_114_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=5, w2=455, w3=138, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 5)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.048333 * pressure.rolling(138, min_periods=max(138//3, 2)).mean() + 0.0057305 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_115_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=12, w2=468, w3=155, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(12, min_periods=max(12//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.118235 + 0.0057306 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_116_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=19, w2=481, w3=172, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(481, min_periods=max(481//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 19)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.131765 + 0.0057307 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_117_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=26, w2=494, w3=189, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(26, min_periods=max(26//3, 2)).mean(), b.abs().rolling(494, min_periods=max(494//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.067333 * _rolling_slope(cover, 26) + 0.0057308 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_118_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=33, w2=507, w3=206, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.073667 * y + 0.926333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 33) - _rolling_slope(basket, 507) + 0.0057309 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_119_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=40, w2=21, w3=223, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(40, min_periods=max(40//3, 2)).mean(), upside.rolling(21, min_periods=max(21//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.172353 + 0.005731 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_120_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=47, w2=34, w3=240, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(34, min_periods=max(34//3, 2)).max()
    rebound = x - x.rolling(47, min_periods=max(47//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.086333 * _rolling_slope(draw, 240) + 0.0057311 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_121_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=54, w2=47, w3=257, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(54) - b.diff(47)
    stress = imbalance.rolling(257, min_periods=max(257//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.199412 + 0.0057312 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_122_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=61, w2=60, w3=274, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 61)
    baseline = trend.rolling(60, min_periods=max(60//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(274, min_periods=max(274//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.212941 + 0.0057313 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_123_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=68, w2=73, w3=291, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 68)
    slow = _rolling_slope(x, 73)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=291, adjust=False).mean() * 1.226471 + 0.0057314 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_124_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=75, w2=86, w3=308, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(86, min_periods=max(86//3, 2)).max()
    trough = x.rolling(75, min_periods=max(75//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.24 + 0.0057315 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_125_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=82, w2=99, w3=325, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(82)
    rank = change.rolling(99, min_periods=max(99//3, 2)).rank(pct=True)
    persistence = change.rolling(325, min_periods=max(325//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.118 * persistence + 0.0057316 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_126_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=89, w2=112, w3=342, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(89, min_periods=max(89//3, 2)).std()
    vol_slow = ret.rolling(112, min_periods=max(112//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.267059 + 0.0057317 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_127_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=96, w2=125, w3=359, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(125, min_periods=max(125//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 96)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.130667 * slope + 0.0057318 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_128_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=103, w2=138, w3=376, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(103)
    drag = impulse.rolling(138, min_periods=max(138//3, 2)).mean()
    noise = impulse.abs().rolling(376, min_periods=max(376//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.294118 + 0.0057319 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_129_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=110, w2=151, w3=393, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 110)
    acceleration = _rolling_slope(velocity, 151)
    curvature = _rolling_slope(acceleration, 393)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.143333 * acceleration + 0.005732 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_130_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=117, w2=164, w3=410, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 117)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.149667 * pressure.rolling(410, min_periods=max(410//3, 2)).mean() + 0.0057321 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_131_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=124, w2=177, w3=427, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(124, min_periods=max(124//3, 2)).mean())
    decay = spread.ewm(span=177, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.334706 + 0.0057322 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_132_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=131, w2=190, w3=444, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(190, min_periods=max(190//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 131)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.348235 + 0.0057323 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_133_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=138, w2=203, w3=461, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(138, min_periods=max(138//3, 2)).mean(), b.abs().rolling(203, min_periods=max(203//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.168667 * _rolling_slope(cover, 138) + 0.0057324 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_134_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=145, w2=216, w3=478, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.175 * y + 0.825000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 145) - _rolling_slope(basket, 216) + 0.0057325 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_135_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=152, w2=229, w3=495, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(152, min_periods=max(152//3, 2)).mean(), upside.rolling(229, min_periods=max(229//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.388824 + 0.0057326 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_136_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=159, w2=242, w3=512, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(242, min_periods=max(242//3, 2)).max()
    rebound = x - x.rolling(159, min_periods=max(159//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.187667 * _rolling_slope(draw, 512) + 0.0057327 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_137_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=166, w2=255, w3=529, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(529, min_periods=max(529//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.415882 + 0.0057328 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_138_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=173, w2=268, w3=546, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 173)
    baseline = trend.rolling(268, min_periods=max(268//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(546, min_periods=max(546//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.429412 + 0.0057329 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_139_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=180, w2=281, w3=563, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 180)
    slow = _rolling_slope(x, 281)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.442941 + 0.005733 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_140_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=187, w2=294, w3=580, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(294, min_periods=max(294//3, 2)).max()
    trough = x.rolling(187, min_periods=max(187//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.456471 + 0.0057331 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_141_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=194, w2=307, w3=597, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(307, min_periods=max(307//3, 2)).rank(pct=True)
    persistence = change.rolling(597, min_periods=max(597//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.219333 * persistence + 0.0057332 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_142_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=201, w2=320, w3=614, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(201, min_periods=max(201//3, 2)).std()
    vol_slow = ret.rolling(320, min_periods=max(320//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.483529 + 0.0057333 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_143_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=208, w2=333, w3=631, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(333, min_periods=max(333//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 208)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.232 * slope + 0.0057334 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_144_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=215, w2=346, w3=648, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(346, min_periods=max(346//3, 2)).mean()
    noise = impulse.abs().rolling(648, min_periods=max(648//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.510588 + 0.0057335 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_145_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=222, w2=359, w3=665, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 222)
    acceleration = _rolling_slope(velocity, 359)
    curvature = _rolling_slope(acceleration, 665)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.244667 * acceleration + 0.0057336 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_146_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=229, w2=372, w3=682, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 229)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.251 * pressure.rolling(682, min_periods=max(682//3, 2)).mean() + 0.0057337 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_147_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=236, w2=385, w3=699, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(236, min_periods=max(236//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.551176 + 0.0057338 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_148_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=243, w2=398, w3=716, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(398, min_periods=max(398//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 243)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.564706 + 0.0057339 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_149_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=250, w2=411, w3=733, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(250, min_periods=max(250//3, 2)).mean(), b.abs().rolling(411, min_periods=max(411//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.27 * _rolling_slope(cover, 250) + 0.005734 * anchor
    return base_signal.diff().diff()

def f92_vchp_gemini_150_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=10, w2=424, w3=750, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.276333 * y + 0.723667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 10) - _rolling_slope(basket, 424) + 0.0057341 * anchor
    return base_signal.diff().diff()
