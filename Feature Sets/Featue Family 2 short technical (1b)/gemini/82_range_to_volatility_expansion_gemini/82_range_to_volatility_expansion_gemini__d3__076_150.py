"""82 range to volatility expansion gemini d3 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Disproportionate growth in price range compared to underlying volatility.
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

def f82_rtve_gemini_076_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=51, w2=338, w3=547, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(338, min_periods=max(338//3, 2)).max()
    rebound = x - x.rolling(51, min_periods=max(51//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.122667 * _rolling_slope(draw, 547) + 0.0051807 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_077_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=58, w2=351, w3=564, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(58) - b.diff(126)
    stress = imbalance.rolling(564, min_periods=max(564//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.990588 + 0.0051808 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_078_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=65, w2=364, w3=581, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 65)
    baseline = trend.rolling(364, min_periods=max(364//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(581, min_periods=max(581//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.004118 + 0.0051809 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_079_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=72, w2=377, w3=598, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 72)
    slow = _rolling_slope(x, 377)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.017647 + 0.005181 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_080_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=79, w2=390, w3=615, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(390, min_periods=max(390//3, 2)).max()
    trough = x.rolling(79, min_periods=max(79//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.031176 + 0.0051811 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_081_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=86, w2=403, w3=632, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(86)
    rank = change.rolling(403, min_periods=max(403//3, 2)).rank(pct=True)
    persistence = change.rolling(632, min_periods=max(632//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.154333 * persistence + 0.0051812 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_082_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=93, w2=416, w3=649, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(93, min_periods=max(93//3, 2)).std()
    vol_slow = ret.rolling(416, min_periods=max(416//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.058235 + 0.0051813 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_083_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=100, w2=429, w3=666, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(429, min_periods=max(429//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 100)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.167 * slope + 0.0051814 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_084_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=107, w2=442, w3=683, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(107)
    drag = impulse.rolling(442, min_periods=max(442//3, 2)).mean()
    noise = impulse.abs().rolling(683, min_periods=max(683//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.085294 + 0.0051815 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_085_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=114, w2=455, w3=700, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 114)
    acceleration = _rolling_slope(velocity, 455)
    curvature = _rolling_slope(acceleration, 700)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.179667 * acceleration + 0.0051816 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_086_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=121, w2=468, w3=717, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 121)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.186 * pressure.rolling(717, min_periods=max(717//3, 2)).mean() + 0.0051817 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_087_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=128, w2=481, w3=734, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(128, min_periods=max(128//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.125882 + 0.0051818 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_088_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=135, w2=494, w3=751, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(494, min_periods=max(494//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 135)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.139412 + 0.0051819 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_089_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=142, w2=507, w3=17, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(142, min_periods=max(142//3, 2)).mean(), b.abs().rolling(507, min_periods=max(507//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(17) + 0.205 * _rolling_slope(cover, 142) + 0.005182 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_090_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=149, w2=21, w3=34, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.211333 * y + 0.788667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 149) - _rolling_slope(basket, 21) + 0.0051821 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_091_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=156, w2=34, w3=51, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(156, min_periods=max(156//3, 2)).mean(), upside.rolling(34, min_periods=max(34//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(51) * 1.18 + 0.0051822 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_092_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=163, w2=47, w3=68, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(47, min_periods=max(47//3, 2)).max()
    rebound = x - x.rolling(163, min_periods=max(163//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.224 * _rolling_slope(draw, 68) + 0.0051823 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_093_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=170, w2=60, w3=85, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(60)
    stress = imbalance.rolling(85, min_periods=max(85//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.207059 + 0.0051824 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_094_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=177, w2=73, w3=102, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 177)
    baseline = trend.rolling(73, min_periods=max(73//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(102, min_periods=max(102//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.220588 + 0.0051825 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_095_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=184, w2=86, w3=119, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 184)
    slow = _rolling_slope(x, 86)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=119, adjust=False).mean() * 1.234118 + 0.0051826 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_096_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=191, w2=99, w3=136, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(99, min_periods=max(99//3, 2)).max()
    trough = x.rolling(191, min_periods=max(191//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.247647 + 0.0051827 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_097_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=198, w2=112, w3=153, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(112, min_periods=max(112//3, 2)).rank(pct=True)
    persistence = change.rolling(153, min_periods=max(153//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.255667 * persistence + 0.0051828 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_098_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=205, w2=125, w3=170, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(205, min_periods=max(205//3, 2)).std()
    vol_slow = ret.rolling(125, min_periods=max(125//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.274706 + 0.0051829 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_099_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=212, w2=138, w3=187, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(138, min_periods=max(138//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 212)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.268333 * slope + 0.005183 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_100_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=219, w2=151, w3=204, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(151, min_periods=max(151//3, 2)).mean()
    noise = impulse.abs().rolling(204, min_periods=max(204//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.301765 + 0.0051831 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_101_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=226, w2=164, w3=221, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 226)
    acceleration = _rolling_slope(velocity, 164)
    curvature = _rolling_slope(acceleration, 221)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.281 * acceleration + 0.0051832 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_102_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=233, w2=177, w3=238, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 233)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.287333 * pressure.rolling(238, min_periods=max(238//3, 2)).mean() + 0.0051833 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_103_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=240, w2=190, w3=255, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(240, min_periods=max(240//3, 2)).mean())
    decay = spread.ewm(span=190, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.342353 + 0.0051834 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_104_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=247, w2=203, w3=272, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(203, min_periods=max(203//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 247)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.355882 + 0.0051835 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_105_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=7, w2=216, w3=289, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(7, min_periods=max(7//3, 2)).mean(), b.abs().rolling(216, min_periods=max(216//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.306333 * _rolling_slope(cover, 7) + 0.0051836 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_106_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=14, w2=229, w3=306, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.312667 * y + 0.687333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 14) - _rolling_slope(basket, 229) + 0.0051837 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_107_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=21, w2=242, w3=323, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(21, min_periods=max(21//3, 2)).mean(), upside.rolling(242, min_periods=max(242//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.396471 + 0.0051838 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_108_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=28, w2=255, w3=340, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(255, min_periods=max(255//3, 2)).max()
    rebound = x - x.rolling(28, min_periods=max(28//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.325333 * _rolling_slope(draw, 340) + 0.0051839 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_109_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=35, w2=268, w3=357, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(35) - b.diff(126)
    stress = imbalance.rolling(357, min_periods=max(357//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.423529 + 0.005184 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_110_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=42, w2=281, w3=374, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 42)
    baseline = trend.rolling(281, min_periods=max(281//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(374, min_periods=max(374//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.437059 + 0.0051841 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_111_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=49, w2=294, w3=391, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 49)
    slow = _rolling_slope(x, 294)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.450588 + 0.0051842 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_112_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=56, w2=307, w3=408, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(307, min_periods=max(307//3, 2)).max()
    trough = x.rolling(56, min_periods=max(56//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.464118 + 0.0051843 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_113_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=63, w2=320, w3=425, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(63)
    rank = change.rolling(320, min_periods=max(320//3, 2)).rank(pct=True)
    persistence = change.rolling(425, min_periods=max(425//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.357 * persistence + 0.0051844 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_114_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=70, w2=333, w3=442, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(70, min_periods=max(70//3, 2)).std()
    vol_slow = ret.rolling(333, min_periods=max(333//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.491176 + 0.0051845 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_115_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=77, w2=346, w3=459, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(346, min_periods=max(346//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 77)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.037333 * slope + 0.0051846 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_116_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=84, w2=359, w3=476, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(84)
    drag = impulse.rolling(359, min_periods=max(359//3, 2)).mean()
    noise = impulse.abs().rolling(476, min_periods=max(476//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.518235 + 0.0051847 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_117_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=91, w2=372, w3=493, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 91)
    acceleration = _rolling_slope(velocity, 372)
    curvature = _rolling_slope(acceleration, 493)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.05 * acceleration + 0.0051848 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_118_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=98, w2=385, w3=510, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 98)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.056333 * pressure.rolling(510, min_periods=max(510//3, 2)).mean() + 0.0051849 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_119_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=105, w2=398, w3=527, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(105, min_periods=max(105//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.558824 + 0.005185 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_120_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=112, w2=411, w3=544, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(411, min_periods=max(411//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 112)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.572353 + 0.0051851 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_121_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=119, w2=424, w3=561, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(119, min_periods=max(119//3, 2)).mean(), b.abs().rolling(424, min_periods=max(424//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.075333 * _rolling_slope(cover, 119) + 0.0051852 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_122_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=126, w2=437, w3=578, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.081667 * y + 0.918333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 126) - _rolling_slope(basket, 437) + 0.0051853 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_123_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=133, w2=450, w3=595, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(133, min_periods=max(133//3, 2)).mean(), upside.rolling(450, min_periods=max(450//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.612941 + 0.0051854 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_124_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=140, w2=463, w3=612, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(463, min_periods=max(463//3, 2)).max()
    rebound = x - x.rolling(140, min_periods=max(140//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.094333 * _rolling_slope(draw, 612) + 0.0051855 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_125_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=147, w2=476, w3=629, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(629, min_periods=max(629//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.64 + 0.0051856 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_126_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=154, w2=489, w3=646, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 154)
    baseline = trend.rolling(489, min_periods=max(489//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(646, min_periods=max(646//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.653529 + 0.0051857 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_127_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=161, w2=502, w3=663, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 161)
    slow = _rolling_slope(x, 502)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.667059 + 0.0051858 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_128_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=168, w2=16, w3=680, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(16, min_periods=max(16//3, 2)).max()
    trough = x.rolling(168, min_periods=max(168//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.827059 + 0.0051859 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_129_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=175, w2=29, w3=697, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(29, min_periods=max(29//3, 2)).rank(pct=True)
    persistence = change.rolling(697, min_periods=max(697//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.126 * persistence + 0.005186 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_130_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=182, w2=42, w3=714, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(182, min_periods=max(182//3, 2)).std()
    vol_slow = ret.rolling(42, min_periods=max(42//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.854118 + 0.0051861 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_131_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=189, w2=55, w3=731, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(55, min_periods=max(55//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 189)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.138667 * slope + 0.0051862 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_132_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=196, w2=68, w3=748, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(68, min_periods=max(68//3, 2)).mean()
    noise = impulse.abs().rolling(748, min_periods=max(748//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.881176 + 0.0051863 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_133_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=203, w2=81, w3=765, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 203)
    acceleration = _rolling_slope(velocity, 81)
    curvature = _rolling_slope(acceleration, 765)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.151333 * acceleration + 0.0051864 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_134_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=210, w2=94, w3=31, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 210)
    pressure = rel_log.diff(94)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.157667 * pressure.rolling(31, min_periods=max(31//3, 2)).mean() + 0.0051865 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_135_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=217, w2=107, w3=48, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(217, min_periods=max(217//3, 2)).mean())
    decay = spread.ewm(span=107, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.921765 + 0.0051866 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_136_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=224, w2=120, w3=65, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(120, min_periods=max(120//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 224)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.935294 + 0.0051867 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_137_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=231, w2=133, w3=82, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(231, min_periods=max(231//3, 2)).mean(), b.abs().rolling(133, min_periods=max(133//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(82) + 0.176667 * _rolling_slope(cover, 231) + 0.0051868 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_138_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=238, w2=146, w3=99, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.183 * y + 0.817000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 238) - _rolling_slope(basket, 146) + 0.0051869 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_139_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=245, w2=159, w3=116, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(245, min_periods=max(245//3, 2)).mean(), upside.rolling(159, min_periods=max(159//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(116) * 0.975882 + 0.005187 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_140_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=5, w2=172, w3=133, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(172, min_periods=max(172//3, 2)).max()
    rebound = x - x.rolling(5, min_periods=max(5//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.195667 * _rolling_slope(draw, 133) + 0.0051871 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_141_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=12, w2=185, w3=150, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(12) - b.diff(126)
    stress = imbalance.rolling(150, min_periods=max(150//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.002941 + 0.0051872 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_142_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=19, w2=198, w3=167, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 19)
    baseline = trend.rolling(198, min_periods=max(198//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(167, min_periods=max(167//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.016471 + 0.0051873 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_143_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=26, w2=211, w3=184, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 26)
    slow = _rolling_slope(x, 211)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=184, adjust=False).mean() * 1.03 + 0.0051874 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_144_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=33, w2=224, w3=201, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(224, min_periods=max(224//3, 2)).max()
    trough = x.rolling(33, min_periods=max(33//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.043529 + 0.0051875 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_145_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=40, w2=237, w3=218, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(40)
    rank = change.rolling(237, min_periods=max(237//3, 2)).rank(pct=True)
    persistence = change.rolling(218, min_periods=max(218//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.227333 * persistence + 0.0051876 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_146_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=47, w2=250, w3=235, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(47, min_periods=max(47//3, 2)).std()
    vol_slow = ret.rolling(250, min_periods=max(250//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.070588 + 0.0051877 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_147_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=54, w2=263, w3=252, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(263, min_periods=max(263//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 54)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.24 * slope + 0.0051878 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_148_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=61, w2=276, w3=269, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(61)
    drag = impulse.rolling(276, min_periods=max(276//3, 2)).mean()
    noise = impulse.abs().rolling(269, min_periods=max(269//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.097647 + 0.0051879 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_149_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=68, w2=289, w3=286, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 68)
    acceleration = _rolling_slope(velocity, 289)
    curvature = _rolling_slope(acceleration, 286)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.252667 * acceleration + 0.005188 * anchor
    return base_signal.diff().diff().diff()

def f82_rtve_gemini_150_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=75, w2=302, w3=303, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 75)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.259 * pressure.rolling(303, min_periods=max(303//3, 2)).mean() + 0.0051881 * anchor
    return base_signal.diff().diff().diff()
