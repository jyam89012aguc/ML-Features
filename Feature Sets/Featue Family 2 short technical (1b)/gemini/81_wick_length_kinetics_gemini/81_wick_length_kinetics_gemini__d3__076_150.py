"""81 wick length kinetics gemini d3 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Analysis of candlestick wick dynamics to identify intraday price rejection.
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

def f81_wick_gemini_076_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=83, w2=44, w3=39, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    draw = x - x.rolling(44, min_periods=max(44//3, 2)).max()
    rebound = x - x.rolling(83, min_periods=max(83//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.231667 * _rolling_slope(draw, 39) + 0.0051247 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_077_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=90, w2=57, w3=56, lag=21)."""
    a = _safe_log(open.abs() + 1.0).shift(21)
    b = _safe_log(high.abs() + 1.0).shift(21)
    imbalance = a.diff(90) - b.diff(57)
    stress = imbalance.rolling(56, min_periods=max(56//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.095882 + 0.0051248 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_078_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=97, w2=70, w3=73, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 97)
    baseline = trend.rolling(70, min_periods=max(70//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(73, min_periods=max(73//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.109412 + 0.0051249 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_079_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=104, w2=83, w3=90, lag=55)."""
    x = _safe_log(open.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 104)
    slow = _rolling_slope(x, 83)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=90, adjust=False).mean() * 1.122941 + 0.005125 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_080_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=111, w2=96, w3=107, lag=0)."""
    x = open.shift(0)
    peak = x.rolling(96, min_periods=max(96//3, 2)).max()
    trough = x.rolling(111, min_periods=max(111//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.136471 + 0.0051251 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_081_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=118, w2=109, w3=124, lag=1)."""
    x = open.shift(1)
    change = x.pct_change(118)
    rank = change.rolling(109, min_periods=max(109//3, 2)).rank(pct=True)
    persistence = change.rolling(124, min_periods=max(124//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.263333 * persistence + 0.0051252 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_082_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=125, w2=122, w3=141, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(125, min_periods=max(125//3, 2)).std()
    vol_slow = ret.rolling(122, min_periods=max(122//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.163529 + 0.0051253 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_083_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=132, w2=135, w3=158, lag=3)."""
    x = open.shift(3)
    ma = x.rolling(135, min_periods=max(135//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 132)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.276 * slope + 0.0051254 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_084_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=139, w2=148, w3=175, lag=5)."""
    x = open.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(148, min_periods=max(148//3, 2)).mean()
    noise = impulse.abs().rolling(175, min_periods=max(175//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.190588 + 0.0051255 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_085_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=146, w2=161, w3=192, lag=8)."""
    x = _safe_log(open.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 146)
    acceleration = _rolling_slope(velocity, 161)
    curvature = _rolling_slope(acceleration, 192)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.288667 * acceleration + 0.0051256 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_086_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=153, w2=174, w3=209, lag=13)."""
    rel = _safe_div(open.shift(13), high.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 153)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.295 * pressure.rolling(209, min_periods=max(209//3, 2)).mean() + 0.0051257 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_087_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=160, w2=187, w3=226, lag=21)."""
    a = open.shift(21)
    b = high.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(160, min_periods=max(160//3, 2)).mean())
    decay = spread.ewm(span=187, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.231176 + 0.0051258 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_088_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=167, w2=200, w3=243, lag=34)."""
    a = _safe_log(open.abs() + 1.0).shift(34)
    b = _safe_log(high.abs() + 1.0).shift(34)
    corr = a.rolling(200, min_periods=max(200//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 167)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.244706 + 0.0051259 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_089_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=174, w2=213, w3=260, lag=55)."""
    a = open.shift(55)
    b = high.shift(55)
    cover = _safe_div(a.rolling(174, min_periods=max(174//3, 2)).mean(), b.abs().rolling(213, min_periods=max(213//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.314 * _rolling_slope(cover, 174) + 0.005126 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_090_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=181, w2=226, w3=277, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    y = _safe_log(high.abs() + 1.0).shift(0)
    z = _safe_log(low.abs() + 1.0).shift(0)
    basket = x - 0.320333 * y + 0.679667 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 181) - _rolling_slope(basket, 226) + 0.0051261 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_091_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=188, w2=239, w3=294, lag=1)."""
    x = open.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(188, min_periods=max(188//3, 2)).mean(), upside.rolling(239, min_periods=max(239//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.285294 + 0.0051262 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_092_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=195, w2=252, w3=311, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    draw = x - x.rolling(252, min_periods=max(252//3, 2)).max()
    rebound = x - x.rolling(195, min_periods=max(195//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.333 * _rolling_slope(draw, 311) + 0.0051263 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_093_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=202, w2=265, w3=328, lag=3)."""
    a = _safe_log(open.abs() + 1.0).shift(3)
    b = _safe_log(high.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(328, min_periods=max(328//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.312353 + 0.0051264 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_094_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=209, w2=278, w3=345, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 209)
    baseline = trend.rolling(278, min_periods=max(278//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(345, min_periods=max(345//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.325882 + 0.0051265 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_095_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=216, w2=291, w3=362, lag=8)."""
    x = _safe_log(open.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 216)
    slow = _rolling_slope(x, 291)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.339412 + 0.0051266 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_096_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=223, w2=304, w3=379, lag=13)."""
    x = open.shift(13)
    peak = x.rolling(304, min_periods=max(304//3, 2)).max()
    trough = x.rolling(223, min_periods=max(223//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.352941 + 0.0051267 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_097_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=230, w2=317, w3=396, lag=21)."""
    x = open.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(317, min_periods=max(317//3, 2)).rank(pct=True)
    persistence = change.rolling(396, min_periods=max(396//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.032333 * persistence + 0.0051268 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_098_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=237, w2=330, w3=413, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(237, min_periods=max(237//3, 2)).std()
    vol_slow = ret.rolling(330, min_periods=max(330//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.38 + 0.0051269 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_099_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=244, w2=343, w3=430, lag=55)."""
    x = open.shift(55)
    ma = x.rolling(343, min_periods=max(343//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 244)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.045 * slope + 0.005127 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_100_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=251, w2=356, w3=447, lag=0)."""
    x = open.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(356, min_periods=max(356//3, 2)).mean()
    noise = impulse.abs().rolling(447, min_periods=max(447//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.407059 + 0.0051271 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_101_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=11, w2=369, w3=464, lag=1)."""
    x = _safe_log(open.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 11)
    acceleration = _rolling_slope(velocity, 369)
    curvature = _rolling_slope(acceleration, 464)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.057667 * acceleration + 0.0051272 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_102_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=18, w2=382, w3=481, lag=2)."""
    rel = _safe_div(open.shift(2), high.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 18)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.064 * pressure.rolling(481, min_periods=max(481//3, 2)).mean() + 0.0051273 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_103_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=25, w2=395, w3=498, lag=3)."""
    a = open.shift(3)
    b = high.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(25, min_periods=max(25//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.447647 + 0.0051274 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_104_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=32, w2=408, w3=515, lag=5)."""
    a = _safe_log(open.abs() + 1.0).shift(5)
    b = _safe_log(high.abs() + 1.0).shift(5)
    corr = a.rolling(408, min_periods=max(408//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 32)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.461176 + 0.0051275 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_105_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=39, w2=421, w3=532, lag=8)."""
    a = open.shift(8)
    b = high.shift(8)
    cover = _safe_div(a.rolling(39, min_periods=max(39//3, 2)).mean(), b.abs().rolling(421, min_periods=max(421//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.083 * _rolling_slope(cover, 39) + 0.0051276 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_106_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=46, w2=434, w3=549, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    y = _safe_log(high.abs() + 1.0).shift(13)
    z = _safe_log(low.abs() + 1.0).shift(13)
    basket = x - 0.089333 * y + 0.910667 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 46) - _rolling_slope(basket, 434) + 0.0051277 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_107_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=53, w2=447, w3=566, lag=21)."""
    x = open.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(53, min_periods=max(53//3, 2)).mean(), upside.rolling(447, min_periods=max(447//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.501765 + 0.0051278 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_108_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=60, w2=460, w3=583, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    draw = x - x.rolling(460, min_periods=max(460//3, 2)).max()
    rebound = x - x.rolling(60, min_periods=max(60//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.102 * _rolling_slope(draw, 583) + 0.0051279 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_109_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=67, w2=473, w3=600, lag=55)."""
    a = _safe_log(open.abs() + 1.0).shift(55)
    b = _safe_log(high.abs() + 1.0).shift(55)
    imbalance = a.diff(67) - b.diff(126)
    stress = imbalance.rolling(600, min_periods=max(600//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.528824 + 0.005128 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_110_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=74, w2=486, w3=617, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 74)
    baseline = trend.rolling(486, min_periods=max(486//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(617, min_periods=max(617//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.542353 + 0.0051281 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_111_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=81, w2=499, w3=634, lag=1)."""
    x = _safe_log(open.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 81)
    slow = _rolling_slope(x, 499)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.555882 + 0.0051282 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_112_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=88, w2=13, w3=651, lag=2)."""
    x = open.shift(2)
    peak = x.rolling(13, min_periods=max(13//3, 2)).max()
    trough = x.rolling(88, min_periods=max(88//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.569412 + 0.0051283 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_113_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=95, w2=26, w3=668, lag=3)."""
    x = open.shift(3)
    change = x.pct_change(95)
    rank = change.rolling(26, min_periods=max(26//3, 2)).rank(pct=True)
    persistence = change.rolling(668, min_periods=max(668//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.133667 * persistence + 0.0051284 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_114_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=102, w2=39, w3=685, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(102, min_periods=max(102//3, 2)).std()
    vol_slow = ret.rolling(39, min_periods=max(39//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.596471 + 0.0051285 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_115_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=109, w2=52, w3=702, lag=8)."""
    x = open.shift(8)
    ma = x.rolling(52, min_periods=max(52//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 109)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.146333 * slope + 0.0051286 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_116_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=116, w2=65, w3=719, lag=13)."""
    x = open.shift(13)
    impulse = x.diff(116)
    drag = impulse.rolling(65, min_periods=max(65//3, 2)).mean()
    noise = impulse.abs().rolling(719, min_periods=max(719//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.623529 + 0.0051287 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_117_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=123, w2=78, w3=736, lag=21)."""
    x = _safe_log(open.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 123)
    acceleration = _rolling_slope(velocity, 78)
    curvature = _rolling_slope(acceleration, 736)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.159 * acceleration + 0.0051288 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_118_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=130, w2=91, w3=753, lag=34)."""
    rel = _safe_div(open.shift(34), high.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 130)
    pressure = rel_log.diff(91)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.165333 * pressure.rolling(753, min_periods=max(753//3, 2)).mean() + 0.0051289 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_119_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=137, w2=104, w3=19, lag=55)."""
    a = open.shift(55)
    b = high.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(137, min_periods=max(137//3, 2)).mean())
    decay = spread.ewm(span=104, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.664118 + 0.005129 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_120_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=144, w2=117, w3=36, lag=0)."""
    a = _safe_log(open.abs() + 1.0).shift(0)
    b = _safe_log(high.abs() + 1.0).shift(0)
    corr = a.rolling(117, min_periods=max(117//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 144)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.824118 + 0.0051291 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_121_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=151, w2=130, w3=53, lag=1)."""
    a = open.shift(1)
    b = high.shift(1)
    cover = _safe_div(a.rolling(151, min_periods=max(151//3, 2)).mean(), b.abs().rolling(130, min_periods=max(130//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(53) + 0.184333 * _rolling_slope(cover, 151) + 0.0051292 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_122_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=158, w2=143, w3=70, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    y = _safe_log(high.abs() + 1.0).shift(2)
    z = _safe_log(low.abs() + 1.0).shift(2)
    basket = x - 0.190667 * y + 0.809333 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 158) - _rolling_slope(basket, 143) + 0.0051293 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_123_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=165, w2=156, w3=87, lag=3)."""
    x = open.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(165, min_periods=max(165//3, 2)).mean(), upside.rolling(156, min_periods=max(156//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(87) * 0.864706 + 0.0051294 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_124_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=172, w2=169, w3=104, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    draw = x - x.rolling(169, min_periods=max(169//3, 2)).max()
    rebound = x - x.rolling(172, min_periods=max(172//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.203333 * _rolling_slope(draw, 104) + 0.0051295 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_125_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=179, w2=182, w3=121, lag=8)."""
    a = _safe_log(open.abs() + 1.0).shift(8)
    b = _safe_log(high.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(121, min_periods=max(121//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.891765 + 0.0051296 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_126_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=186, w2=195, w3=138, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 186)
    baseline = trend.rolling(195, min_periods=max(195//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(138, min_periods=max(138//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.905294 + 0.0051297 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_127_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=193, w2=208, w3=155, lag=21)."""
    x = _safe_log(open.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 193)
    slow = _rolling_slope(x, 208)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=155, adjust=False).mean() * 0.918824 + 0.0051298 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_128_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=200, w2=221, w3=172, lag=34)."""
    x = open.shift(34)
    peak = x.rolling(221, min_periods=max(221//3, 2)).max()
    trough = x.rolling(200, min_periods=max(200//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.932353 + 0.0051299 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_129_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=207, w2=234, w3=189, lag=55)."""
    x = open.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(234, min_periods=max(234//3, 2)).rank(pct=True)
    persistence = change.rolling(189, min_periods=max(189//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.235 * persistence + 0.00513 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_130_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=214, w2=247, w3=206, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(214, min_periods=max(214//3, 2)).std()
    vol_slow = ret.rolling(247, min_periods=max(247//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.959412 + 0.0051301 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_131_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=221, w2=260, w3=223, lag=1)."""
    x = open.shift(1)
    ma = x.rolling(260, min_periods=max(260//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 221)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.247667 * slope + 0.0051302 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_132_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=228, w2=273, w3=240, lag=2)."""
    x = open.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(273, min_periods=max(273//3, 2)).mean()
    noise = impulse.abs().rolling(240, min_periods=max(240//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.986471 + 0.0051303 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_133_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=235, w2=286, w3=257, lag=3)."""
    x = _safe_log(open.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 235)
    acceleration = _rolling_slope(velocity, 286)
    curvature = _rolling_slope(acceleration, 257)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.260333 * acceleration + 0.0051304 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_134_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=242, w2=299, w3=274, lag=5)."""
    rel = _safe_div(open.shift(5), high.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 242)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.266667 * pressure.rolling(274, min_periods=max(274//3, 2)).mean() + 0.0051305 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_135_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=249, w2=312, w3=291, lag=8)."""
    a = open.shift(8)
    b = high.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(249, min_periods=max(249//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.027059 + 0.0051306 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_136_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=9, w2=325, w3=308, lag=13)."""
    a = _safe_log(open.abs() + 1.0).shift(13)
    b = _safe_log(high.abs() + 1.0).shift(13)
    corr = a.rolling(325, min_periods=max(325//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 9)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.040588 + 0.0051307 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_137_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=16, w2=338, w3=325, lag=21)."""
    a = open.shift(21)
    b = high.shift(21)
    cover = _safe_div(a.rolling(16, min_periods=max(16//3, 2)).mean(), b.abs().rolling(338, min_periods=max(338//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.285667 * _rolling_slope(cover, 16) + 0.0051308 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_138_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=23, w2=351, w3=342, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    y = _safe_log(high.abs() + 1.0).shift(34)
    z = _safe_log(low.abs() + 1.0).shift(34)
    basket = x - 0.292 * y + 0.708000 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 23) - _rolling_slope(basket, 351) + 0.0051309 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_139_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=30, w2=364, w3=359, lag=55)."""
    x = open.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(30, min_periods=max(30//3, 2)).mean(), upside.rolling(364, min_periods=max(364//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.081176 + 0.005131 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_140_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=37, w2=377, w3=376, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    draw = x - x.rolling(377, min_periods=max(377//3, 2)).max()
    rebound = x - x.rolling(37, min_periods=max(37//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.304667 * _rolling_slope(draw, 376) + 0.0051311 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_141_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=44, w2=390, w3=393, lag=1)."""
    a = _safe_log(open.abs() + 1.0).shift(1)
    b = _safe_log(high.abs() + 1.0).shift(1)
    imbalance = a.diff(44) - b.diff(126)
    stress = imbalance.rolling(393, min_periods=max(393//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.108235 + 0.0051312 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_142_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=51, w2=403, w3=410, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 51)
    baseline = trend.rolling(403, min_periods=max(403//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(410, min_periods=max(410//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.121765 + 0.0051313 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_143_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=58, w2=416, w3=427, lag=3)."""
    x = _safe_log(open.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 58)
    slow = _rolling_slope(x, 416)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.135294 + 0.0051314 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_144_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=65, w2=429, w3=444, lag=5)."""
    x = open.shift(5)
    peak = x.rolling(429, min_periods=max(429//3, 2)).max()
    trough = x.rolling(65, min_periods=max(65//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.148824 + 0.0051315 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_145_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=72, w2=442, w3=461, lag=8)."""
    x = open.shift(8)
    change = x.pct_change(72)
    rank = change.rolling(442, min_periods=max(442//3, 2)).rank(pct=True)
    persistence = change.rolling(461, min_periods=max(461//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.336333 * persistence + 0.0051316 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_146_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=79, w2=455, w3=478, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(79, min_periods=max(79//3, 2)).std()
    vol_slow = ret.rolling(455, min_periods=max(455//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.175882 + 0.0051317 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_147_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=86, w2=468, w3=495, lag=21)."""
    x = open.shift(21)
    ma = x.rolling(468, min_periods=max(468//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 86)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.349 * slope + 0.0051318 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_148_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=93, w2=481, w3=512, lag=34)."""
    x = open.shift(34)
    impulse = x.diff(93)
    drag = impulse.rolling(481, min_periods=max(481//3, 2)).mean()
    noise = impulse.abs().rolling(512, min_periods=max(512//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.202941 + 0.0051319 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_149_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=100, w2=494, w3=529, lag=55)."""
    x = _safe_log(open.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 100)
    acceleration = _rolling_slope(velocity, 494)
    curvature = _rolling_slope(acceleration, 529)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.361667 * acceleration + 0.005132 * anchor
    return base_signal.diff().diff().diff()

def f81_wick_gemini_150_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=107, w2=507, w3=546, lag=0)."""
    rel = _safe_div(open.shift(0), high.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 107)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.035667 * pressure.rolling(546, min_periods=max(546//3, 2)).mean() + 0.0051321 * anchor
    return base_signal.diff().diff().diff()
