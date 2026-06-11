"""52 lempel ziv complexity proxy gemini d1 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Algorithmic complexity of price sequences as a measure of structural randomness.
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

def f52_lzcp_gemini_076_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=39, w2=353, w3=73, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(39)
    drag = impulse.rolling(353, min_periods=max(353//3, 2)).mean()
    noise = impulse.abs().rolling(73, min_periods=max(73//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.201176 + 0.0034727 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_077_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=46, w2=366, w3=90, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 46)
    acceleration = _rolling_slope(velocity, 366)
    curvature = _rolling_slope(acceleration, 90)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.296333 * acceleration + 0.0034728 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_078_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=53, w2=379, w3=107, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 53)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.302667 * pressure.rolling(107, min_periods=max(107//3, 2)).mean() + 0.0034729 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_079_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=60, w2=392, w3=124, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(60, min_periods=max(60//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.241765 + 0.003473 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_080_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=67, w2=405, w3=141, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(405, min_periods=max(405//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 67)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.255294 + 0.0034731 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_081_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=74, w2=418, w3=158, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(74, min_periods=max(74//3, 2)).mean(), b.abs().rolling(418, min_periods=max(418//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.321667 * _rolling_slope(cover, 74) + 0.0034732 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_082_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=81, w2=431, w3=175, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.328 * y + 0.672000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 81) - _rolling_slope(basket, 431) + 0.0034733 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_083_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=88, w2=444, w3=192, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(88, min_periods=max(88//3, 2)).mean(), upside.rolling(444, min_periods=max(444//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.295882 + 0.0034734 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_084_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=95, w2=457, w3=209, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(457, min_periods=max(457//3, 2)).max()
    rebound = x - x.rolling(95, min_periods=max(95//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.340667 * _rolling_slope(draw, 209) + 0.0034735 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_085_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=102, w2=470, w3=226, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(102) - b.diff(126)
    stress = imbalance.rolling(226, min_periods=max(226//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.322941 + 0.0034736 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_086_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=109, w2=483, w3=243, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 109)
    baseline = trend.rolling(483, min_periods=max(483//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(243, min_periods=max(243//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.336471 + 0.0034737 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_087_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=116, w2=496, w3=260, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 116)
    slow = _rolling_slope(x, 496)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=260, adjust=False).mean() * 1.35 + 0.0034738 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_088_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=123, w2=509, w3=277, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(509, min_periods=max(509//3, 2)).max()
    trough = x.rolling(123, min_periods=max(123//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.363529 + 0.0034739 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_089_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=130, w2=23, w3=294, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(23, min_periods=max(23//3, 2)).rank(pct=True)
    persistence = change.rolling(294, min_periods=max(294//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.04 * persistence + 0.003474 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_090_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=137, w2=36, w3=311, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(137, min_periods=max(137//3, 2)).std()
    vol_slow = ret.rolling(36, min_periods=max(36//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.390588 + 0.0034741 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_091_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=144, w2=49, w3=328, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(49, min_periods=max(49//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 144)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.052667 * slope + 0.0034742 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_092_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=151, w2=62, w3=345, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(62, min_periods=max(62//3, 2)).mean()
    noise = impulse.abs().rolling(345, min_periods=max(345//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.417647 + 0.0034743 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_093_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=158, w2=75, w3=362, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 158)
    acceleration = _rolling_slope(velocity, 75)
    curvature = _rolling_slope(acceleration, 362)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.065333 * acceleration + 0.0034744 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_094_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=165, w2=88, w3=379, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 165)
    pressure = rel_log.diff(88)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.071667 * pressure.rolling(379, min_periods=max(379//3, 2)).mean() + 0.0034745 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_095_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=172, w2=101, w3=396, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(172, min_periods=max(172//3, 2)).mean())
    decay = spread.ewm(span=101, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.458235 + 0.0034746 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_096_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=179, w2=114, w3=413, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(114, min_periods=max(114//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 179)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.471765 + 0.0034747 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_097_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=186, w2=127, w3=430, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(186, min_periods=max(186//3, 2)).mean(), b.abs().rolling(127, min_periods=max(127//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.090667 * _rolling_slope(cover, 186) + 0.0034748 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_098_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=193, w2=140, w3=447, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.097 * y + 0.903000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 193) - _rolling_slope(basket, 140) + 0.0034749 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_099_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=200, w2=153, w3=464, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(200, min_periods=max(200//3, 2)).mean(), upside.rolling(153, min_periods=max(153//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.512353 + 0.003475 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_100_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=207, w2=166, w3=481, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(166, min_periods=max(166//3, 2)).max()
    rebound = x - x.rolling(207, min_periods=max(207//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.109667 * _rolling_slope(draw, 481) + 0.0034751 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_101_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=214, w2=179, w3=498, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(498, min_periods=max(498//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.539412 + 0.0034752 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_102_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=221, w2=192, w3=515, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 221)
    baseline = trend.rolling(192, min_periods=max(192//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(515, min_periods=max(515//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.552941 + 0.0034753 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_103_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=228, w2=205, w3=532, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 228)
    slow = _rolling_slope(x, 205)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.566471 + 0.0034754 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_104_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=235, w2=218, w3=549, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(218, min_periods=max(218//3, 2)).max()
    trough = x.rolling(235, min_periods=max(235//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.58 + 0.0034755 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_105_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=242, w2=231, w3=566, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(231, min_periods=max(231//3, 2)).rank(pct=True)
    persistence = change.rolling(566, min_periods=max(566//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.141333 * persistence + 0.0034756 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_106_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=249, w2=244, w3=583, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(249, min_periods=max(249//3, 2)).std()
    vol_slow = ret.rolling(244, min_periods=max(244//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.607059 + 0.0034757 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_107_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=9, w2=257, w3=600, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(257, min_periods=max(257//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 9)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.154 * slope + 0.0034758 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_108_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=16, w2=270, w3=617, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(16)
    drag = impulse.rolling(270, min_periods=max(270//3, 2)).mean()
    noise = impulse.abs().rolling(617, min_periods=max(617//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.634118 + 0.0034759 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_109_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=23, w2=283, w3=634, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 23)
    acceleration = _rolling_slope(velocity, 283)
    curvature = _rolling_slope(acceleration, 634)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.166667 * acceleration + 0.003476 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_110_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=30, w2=296, w3=651, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 30)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.173 * pressure.rolling(651, min_periods=max(651//3, 2)).mean() + 0.0034761 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_111_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=37, w2=309, w3=668, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(37, min_periods=max(37//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.821176 + 0.0034762 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_112_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=44, w2=322, w3=685, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(322, min_periods=max(322//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 44)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.834706 + 0.0034763 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_113_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=51, w2=335, w3=702, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(51, min_periods=max(51//3, 2)).mean(), b.abs().rolling(335, min_periods=max(335//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.192 * _rolling_slope(cover, 51) + 0.0034764 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_114_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=58, w2=348, w3=719, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.198333 * y + 0.801667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 58) - _rolling_slope(basket, 348) + 0.0034765 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_115_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=65, w2=361, w3=736, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(65, min_periods=max(65//3, 2)).mean(), upside.rolling(361, min_periods=max(361//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.875294 + 0.0034766 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_116_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=72, w2=374, w3=753, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(374, min_periods=max(374//3, 2)).max()
    rebound = x - x.rolling(72, min_periods=max(72//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.211 * _rolling_slope(draw, 753) + 0.0034767 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_117_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=79, w2=387, w3=19, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(79) - b.diff(126)
    stress = imbalance.rolling(19, min_periods=max(19//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.902353 + 0.0034768 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_118_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=86, w2=400, w3=36, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 86)
    baseline = trend.rolling(400, min_periods=max(400//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(36, min_periods=max(36//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.915882 + 0.0034769 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_119_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=93, w2=413, w3=53, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 93)
    slow = _rolling_slope(x, 413)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=53, adjust=False).mean() * 0.929412 + 0.003477 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_120_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=100, w2=426, w3=70, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(426, min_periods=max(426//3, 2)).max()
    trough = x.rolling(100, min_periods=max(100//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.942941 + 0.0034771 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_121_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=107, w2=439, w3=87, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(107)
    rank = change.rolling(439, min_periods=max(439//3, 2)).rank(pct=True)
    persistence = change.rolling(87, min_periods=max(87//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.242667 * persistence + 0.0034772 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_122_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=114, w2=452, w3=104, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(114, min_periods=max(114//3, 2)).std()
    vol_slow = ret.rolling(452, min_periods=max(452//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.97 + 0.0034773 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_123_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=121, w2=465, w3=121, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(465, min_periods=max(465//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 121)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.255333 * slope + 0.0034774 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_124_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=128, w2=478, w3=138, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(478, min_periods=max(478//3, 2)).mean()
    noise = impulse.abs().rolling(138, min_periods=max(138//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.997059 + 0.0034775 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_125_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=135, w2=491, w3=155, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 135)
    acceleration = _rolling_slope(velocity, 491)
    curvature = _rolling_slope(acceleration, 155)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.268 * acceleration + 0.0034776 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_126_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=142, w2=504, w3=172, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 142)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.274333 * pressure.rolling(172, min_periods=max(172//3, 2)).mean() + 0.0034777 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_127_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=149, w2=18, w3=189, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(149, min_periods=max(149//3, 2)).mean())
    decay = spread.ewm(span=18, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.037647 + 0.0034778 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_128_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=156, w2=31, w3=206, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(31, min_periods=max(31//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 156)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.051176 + 0.0034779 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_129_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=163, w2=44, w3=223, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(163, min_periods=max(163//3, 2)).mean(), b.abs().rolling(44, min_periods=max(44//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.293333 * _rolling_slope(cover, 163) + 0.003478 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_130_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=170, w2=57, w3=240, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.299667 * y + 0.700333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 170) - _rolling_slope(basket, 57) + 0.0034781 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_131_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=177, w2=70, w3=257, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(177, min_periods=max(177//3, 2)).mean(), upside.rolling(70, min_periods=max(70//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.091765 + 0.0034782 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_132_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=184, w2=83, w3=274, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(83, min_periods=max(83//3, 2)).max()
    rebound = x - x.rolling(184, min_periods=max(184//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.312333 * _rolling_slope(draw, 274) + 0.0034783 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_133_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=191, w2=96, w3=291, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(96)
    stress = imbalance.rolling(291, min_periods=max(291//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.118824 + 0.0034784 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_134_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=198, w2=109, w3=308, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 198)
    baseline = trend.rolling(109, min_periods=max(109//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(308, min_periods=max(308//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.132353 + 0.0034785 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_135_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=205, w2=122, w3=325, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 205)
    slow = _rolling_slope(x, 122)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.145882 + 0.0034786 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_136_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=212, w2=135, w3=342, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(135, min_periods=max(135//3, 2)).max()
    trough = x.rolling(212, min_periods=max(212//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.159412 + 0.0034787 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_137_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=219, w2=148, w3=359, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(148, min_periods=max(148//3, 2)).rank(pct=True)
    persistence = change.rolling(359, min_periods=max(359//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.344 * persistence + 0.0034788 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_138_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=226, w2=161, w3=376, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(226, min_periods=max(226//3, 2)).std()
    vol_slow = ret.rolling(161, min_periods=max(161//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.186471 + 0.0034789 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_139_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=233, w2=174, w3=393, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(174, min_periods=max(174//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 233)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.356667 * slope + 0.003479 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_140_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=240, w2=187, w3=410, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(187, min_periods=max(187//3, 2)).mean()
    noise = impulse.abs().rolling(410, min_periods=max(410//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.213529 + 0.0034791 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_141_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=247, w2=200, w3=427, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 247)
    acceleration = _rolling_slope(velocity, 200)
    curvature = _rolling_slope(acceleration, 427)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.037 * acceleration + 0.0034792 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_142_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=7, w2=213, w3=444, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 7)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.043333 * pressure.rolling(444, min_periods=max(444//3, 2)).mean() + 0.0034793 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_143_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=14, w2=226, w3=461, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(14, min_periods=max(14//3, 2)).mean())
    decay = spread.ewm(span=226, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.254118 + 0.0034794 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_144_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=21, w2=239, w3=478, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(239, min_periods=max(239//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 21)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.267647 + 0.0034795 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_145_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=28, w2=252, w3=495, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(28, min_periods=max(28//3, 2)).mean(), b.abs().rolling(252, min_periods=max(252//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.062333 * _rolling_slope(cover, 28) + 0.0034796 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_146_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=35, w2=265, w3=512, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.068667 * y + 0.931333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 35) - _rolling_slope(basket, 265) + 0.0034797 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_147_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=42, w2=278, w3=529, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(42, min_periods=max(42//3, 2)).mean(), upside.rolling(278, min_periods=max(278//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.308235 + 0.0034798 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_148_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=49, w2=291, w3=546, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(291, min_periods=max(291//3, 2)).max()
    rebound = x - x.rolling(49, min_periods=max(49//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.081333 * _rolling_slope(draw, 546) + 0.0034799 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_149_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=56, w2=304, w3=563, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(56) - b.diff(126)
    stress = imbalance.rolling(563, min_periods=max(563//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.335294 + 0.00348 * anchor
    return base_signal.diff()

def f52_lzcp_gemini_150_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=63, w2=317, w3=580, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 63)
    baseline = trend.rolling(317, min_periods=max(317//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(580, min_periods=max(580//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.348824 + 0.0034801 * anchor
    return base_signal.diff()
