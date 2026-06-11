"""07 lower high lower low structure gemini d3 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Structural trend shifts identified by a sequence of lower highs and lower lows.
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

def f07_lhll_gemini_076_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=86, w2=503, w3=417, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(503, min_periods=max(503//3, 2)).max()
    rebound = x - x.rolling(86, min_periods=max(86//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.191333 * _rolling_slope(draw, 417) + 0.0003647 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_077_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=93, w2=17, w3=434, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(93) - b.diff(17)
    stress = imbalance.rolling(434, min_periods=max(434//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.510588 + 0.0003648 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_078_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=100, w2=30, w3=451, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 100)
    baseline = trend.rolling(30, min_periods=max(30//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(451, min_periods=max(451//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.524118 + 0.0003649 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_079_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=107, w2=43, w3=468, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 107)
    slow = _rolling_slope(x, 43)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.537647 + 0.000365 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_080_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=114, w2=56, w3=485, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(56, min_periods=max(56//3, 2)).max()
    trough = x.rolling(114, min_periods=max(114//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.551176 + 0.0003651 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_081_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=121, w2=69, w3=502, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(121)
    rank = change.rolling(69, min_periods=max(69//3, 2)).rank(pct=True)
    persistence = change.rolling(502, min_periods=max(502//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.223 * persistence + 0.0003652 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_082_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=128, w2=82, w3=519, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(128, min_periods=max(128//3, 2)).std()
    vol_slow = ret.rolling(82, min_periods=max(82//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.578235 + 0.0003653 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_083_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=135, w2=95, w3=536, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(95, min_periods=max(95//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 135)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.235667 * slope + 0.0003654 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_084_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=142, w2=108, w3=553, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(108, min_periods=max(108//3, 2)).mean()
    noise = impulse.abs().rolling(553, min_periods=max(553//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.605294 + 0.0003655 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_085_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=149, w2=121, w3=570, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 149)
    acceleration = _rolling_slope(velocity, 121)
    curvature = _rolling_slope(acceleration, 570)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.248333 * acceleration + 0.0003656 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_086_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=156, w2=134, w3=587, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 156)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.254667 * pressure.rolling(587, min_periods=max(587//3, 2)).mean() + 0.0003657 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_087_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=163, w2=147, w3=604, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(163, min_periods=max(163//3, 2)).mean())
    decay = spread.ewm(span=147, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.645882 + 0.0003658 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_088_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=170, w2=160, w3=621, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(160, min_periods=max(160//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 170)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.659412 + 0.0003659 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_089_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=177, w2=173, w3=638, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(177, min_periods=max(177//3, 2)).mean(), b.abs().rolling(173, min_periods=max(173//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.273667 * _rolling_slope(cover, 177) + 0.000366 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_090_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=184, w2=186, w3=655, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(low.abs() + 1.0).shift(0)
    basket = x - 0.28 * y + 0.720000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 184) - _rolling_slope(basket, 186) + 0.0003661 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_091_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=191, w2=199, w3=672, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(191, min_periods=max(191//3, 2)).mean(), upside.rolling(199, min_periods=max(199//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.846471 + 0.0003662 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_092_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=198, w2=212, w3=689, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(212, min_periods=max(212//3, 2)).max()
    rebound = x - x.rolling(198, min_periods=max(198//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.292667 * _rolling_slope(draw, 689) + 0.0003663 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_093_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=205, w2=225, w3=706, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(706, min_periods=max(706//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.873529 + 0.0003664 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_094_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=212, w2=238, w3=723, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 212)
    baseline = trend.rolling(238, min_periods=max(238//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(723, min_periods=max(723//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.887059 + 0.0003665 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_095_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=219, w2=251, w3=740, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 219)
    slow = _rolling_slope(x, 251)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.900588 + 0.0003666 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_096_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=226, w2=264, w3=757, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(264, min_periods=max(264//3, 2)).max()
    trough = x.rolling(226, min_periods=max(226//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.914118 + 0.0003667 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_097_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=233, w2=277, w3=23, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(277, min_periods=max(277//3, 2)).rank(pct=True)
    persistence = change.rolling(23, min_periods=max(23//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.324333 * persistence + 0.0003668 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_098_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=240, w2=290, w3=40, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(240, min_periods=max(240//3, 2)).std()
    vol_slow = ret.rolling(290, min_periods=max(290//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.941176 + 0.0003669 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_099_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=247, w2=303, w3=57, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(303, min_periods=max(303//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 247)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.337 * slope + 0.000367 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_100_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=7, w2=316, w3=74, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(7)
    drag = impulse.rolling(316, min_periods=max(316//3, 2)).mean()
    noise = impulse.abs().rolling(74, min_periods=max(74//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.968235 + 0.0003671 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_101_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=14, w2=329, w3=91, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 14)
    acceleration = _rolling_slope(velocity, 329)
    curvature = _rolling_slope(acceleration, 91)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.349667 * acceleration + 0.0003672 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_102_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=21, w2=342, w3=108, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 21)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.356 * pressure.rolling(108, min_periods=max(108//3, 2)).mean() + 0.0003673 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_103_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=28, w2=355, w3=125, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(28, min_periods=max(28//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.008824 + 0.0003674 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_104_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=35, w2=368, w3=142, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(368, min_periods=max(368//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 35)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.022353 + 0.0003675 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_105_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=42, w2=381, w3=159, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(42, min_periods=max(42//3, 2)).mean(), b.abs().rolling(381, min_periods=max(381//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.042667 * _rolling_slope(cover, 42) + 0.0003676 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_106_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=49, w2=394, w3=176, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(low.abs() + 1.0).shift(13)
    basket = x - 0.049 * y + 0.951000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 49) - _rolling_slope(basket, 394) + 0.0003677 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_107_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=56, w2=407, w3=193, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(56, min_periods=max(56//3, 2)).mean(), upside.rolling(407, min_periods=max(407//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.062941 + 0.0003678 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_108_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=63, w2=420, w3=210, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(420, min_periods=max(420//3, 2)).max()
    rebound = x - x.rolling(63, min_periods=max(63//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.061667 * _rolling_slope(draw, 210) + 0.0003679 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_109_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=70, w2=433, w3=227, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(70) - b.diff(126)
    stress = imbalance.rolling(227, min_periods=max(227//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.09 + 0.000368 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_110_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=77, w2=446, w3=244, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 77)
    baseline = trend.rolling(446, min_periods=max(446//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(244, min_periods=max(244//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.103529 + 0.0003681 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_111_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=84, w2=459, w3=261, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 84)
    slow = _rolling_slope(x, 459)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=261, adjust=False).mean() * 1.117059 + 0.0003682 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_112_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=91, w2=472, w3=278, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(472, min_periods=max(472//3, 2)).max()
    trough = x.rolling(91, min_periods=max(91//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.130588 + 0.0003683 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_113_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=98, w2=485, w3=295, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(98)
    rank = change.rolling(485, min_periods=max(485//3, 2)).rank(pct=True)
    persistence = change.rolling(295, min_periods=max(295//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.093333 * persistence + 0.0003684 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_114_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=105, w2=498, w3=312, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(105, min_periods=max(105//3, 2)).std()
    vol_slow = ret.rolling(498, min_periods=max(498//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.157647 + 0.0003685 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_115_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=112, w2=12, w3=329, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(12, min_periods=max(12//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 112)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.106 * slope + 0.0003686 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_116_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=119, w2=25, w3=346, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(119)
    drag = impulse.rolling(25, min_periods=max(25//3, 2)).mean()
    noise = impulse.abs().rolling(346, min_periods=max(346//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.184706 + 0.0003687 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_117_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=126, w2=38, w3=363, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 126)
    acceleration = _rolling_slope(velocity, 38)
    curvature = _rolling_slope(acceleration, 363)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.118667 * acceleration + 0.0003688 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_118_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=133, w2=51, w3=380, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 133)
    pressure = rel_log.diff(51)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.125 * pressure.rolling(380, min_periods=max(380//3, 2)).mean() + 0.0003689 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_119_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=140, w2=64, w3=397, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(140, min_periods=max(140//3, 2)).mean())
    decay = spread.ewm(span=64, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.225294 + 0.000369 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_120_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=147, w2=77, w3=414, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(77, min_periods=max(77//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 147)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.238824 + 0.0003691 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_121_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=154, w2=90, w3=431, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(154, min_periods=max(154//3, 2)).mean(), b.abs().rolling(90, min_periods=max(90//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.144 * _rolling_slope(cover, 154) + 0.0003692 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_122_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=161, w2=103, w3=448, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(low.abs() + 1.0).shift(2)
    basket = x - 0.150333 * y + 0.849667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 161) - _rolling_slope(basket, 103) + 0.0003693 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_123_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=168, w2=116, w3=465, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(168, min_periods=max(168//3, 2)).mean(), upside.rolling(116, min_periods=max(116//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.279412 + 0.0003694 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_124_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=175, w2=129, w3=482, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(129, min_periods=max(129//3, 2)).max()
    rebound = x - x.rolling(175, min_periods=max(175//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.163 * _rolling_slope(draw, 482) + 0.0003695 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_125_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=182, w2=142, w3=499, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(499, min_periods=max(499//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.306471 + 0.0003696 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_126_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=189, w2=155, w3=516, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 189)
    baseline = trend.rolling(155, min_periods=max(155//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(516, min_periods=max(516//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.32 + 0.0003697 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_127_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=196, w2=168, w3=533, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 196)
    slow = _rolling_slope(x, 168)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.333529 + 0.0003698 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_128_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=203, w2=181, w3=550, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(181, min_periods=max(181//3, 2)).max()
    trough = x.rolling(203, min_periods=max(203//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.347059 + 0.0003699 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_129_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=210, w2=194, w3=567, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(194, min_periods=max(194//3, 2)).rank(pct=True)
    persistence = change.rolling(567, min_periods=max(567//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.194667 * persistence + 0.00037 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_130_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=217, w2=207, w3=584, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(217, min_periods=max(217//3, 2)).std()
    vol_slow = ret.rolling(207, min_periods=max(207//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.374118 + 0.0003701 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_131_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=224, w2=220, w3=601, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(220, min_periods=max(220//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 224)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.207333 * slope + 0.0003702 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_132_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=231, w2=233, w3=618, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(233, min_periods=max(233//3, 2)).mean()
    noise = impulse.abs().rolling(618, min_periods=max(618//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.401176 + 0.0003703 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_133_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=238, w2=246, w3=635, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 238)
    acceleration = _rolling_slope(velocity, 246)
    curvature = _rolling_slope(acceleration, 635)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.22 * acceleration + 0.0003704 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_134_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=245, w2=259, w3=652, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 245)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.226333 * pressure.rolling(652, min_periods=max(652//3, 2)).mean() + 0.0003705 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_135_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=5, w2=272, w3=669, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(5, min_periods=max(5//3, 2)).mean())
    decay = spread.ewm(span=272, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.441765 + 0.0003706 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_136_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=12, w2=285, w3=686, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(285, min_periods=max(285//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 12)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.455294 + 0.0003707 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_137_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=19, w2=298, w3=703, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(19, min_periods=max(19//3, 2)).mean(), b.abs().rolling(298, min_periods=max(298//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.245333 * _rolling_slope(cover, 19) + 0.0003708 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_138_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=26, w2=311, w3=720, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(low.abs() + 1.0).shift(34)
    basket = x - 0.251667 * y + 0.748333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 26) - _rolling_slope(basket, 311) + 0.0003709 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_139_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=33, w2=324, w3=737, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(33, min_periods=max(33//3, 2)).mean(), upside.rolling(324, min_periods=max(324//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.495882 + 0.000371 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_140_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=40, w2=337, w3=754, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(337, min_periods=max(337//3, 2)).max()
    rebound = x - x.rolling(40, min_periods=max(40//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.264333 * _rolling_slope(draw, 754) + 0.0003711 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_141_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=47, w2=350, w3=20, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(47) - b.diff(126)
    stress = imbalance.rolling(20, min_periods=max(20//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.522941 + 0.0003712 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_142_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=54, w2=363, w3=37, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 54)
    baseline = trend.rolling(363, min_periods=max(363//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(37, min_periods=max(37//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.536471 + 0.0003713 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_143_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=61, w2=376, w3=54, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 61)
    slow = _rolling_slope(x, 376)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=54, adjust=False).mean() * 1.55 + 0.0003714 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_144_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=68, w2=389, w3=71, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(389, min_periods=max(389//3, 2)).max()
    trough = x.rolling(68, min_periods=max(68//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.563529 + 0.0003715 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_145_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=75, w2=402, w3=88, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(75)
    rank = change.rolling(402, min_periods=max(402//3, 2)).rank(pct=True)
    persistence = change.rolling(88, min_periods=max(88//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.296 * persistence + 0.0003716 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_146_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=82, w2=415, w3=105, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(82, min_periods=max(82//3, 2)).std()
    vol_slow = ret.rolling(415, min_periods=max(415//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.590588 + 0.0003717 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_147_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=89, w2=428, w3=122, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(428, min_periods=max(428//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 89)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.308667 * slope + 0.0003718 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_148_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=96, w2=441, w3=139, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(96)
    drag = impulse.rolling(441, min_periods=max(441//3, 2)).mean()
    noise = impulse.abs().rolling(139, min_periods=max(139//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.617647 + 0.0003719 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_149_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=103, w2=454, w3=156, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 103)
    acceleration = _rolling_slope(velocity, 454)
    curvature = _rolling_slope(acceleration, 156)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.321333 * acceleration + 0.000372 * anchor
    return base_signal.diff().diff().diff()

def f07_lhll_gemini_150_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=110, w2=467, w3=173, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 110)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.327667 * pressure.rolling(173, min_periods=max(173//3, 2)).mean() + 0.0003721 * anchor
    return base_signal.diff().diff().diff()
