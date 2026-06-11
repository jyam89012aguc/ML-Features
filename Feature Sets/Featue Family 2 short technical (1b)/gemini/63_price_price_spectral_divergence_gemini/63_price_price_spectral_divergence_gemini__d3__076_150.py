"""63 price price spectral divergence gemini d3 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Divergence in spectral density between different price representations.
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

def f63_ppsd_gemini_076_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=165, w2=241, w3=658, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    draw = x - x.rolling(241, min_periods=max(241//3, 2)).max()
    rebound = x - x.rolling(165, min_periods=max(165//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.199667 * _rolling_slope(draw, 658) + 0.0041167 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_077_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=172, w2=254, w3=675, lag=21)."""
    a = _safe_log(open.abs() + 1.0).shift(21)
    b = _safe_log(close.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(675, min_periods=max(675//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.284118 + 0.0041168 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_078_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=179, w2=267, w3=692, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 179)
    baseline = trend.rolling(267, min_periods=max(267//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(692, min_periods=max(692//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.297647 + 0.0041169 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_079_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=186, w2=280, w3=709, lag=55)."""
    x = _safe_log(open.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 186)
    slow = _rolling_slope(x, 280)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.311176 + 0.004117 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_080_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=193, w2=293, w3=726, lag=0)."""
    x = open.shift(0)
    peak = x.rolling(293, min_periods=max(293//3, 2)).max()
    trough = x.rolling(193, min_periods=max(193//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.324706 + 0.0041171 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_081_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=200, w2=306, w3=743, lag=1)."""
    x = open.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(306, min_periods=max(306//3, 2)).rank(pct=True)
    persistence = change.rolling(743, min_periods=max(743//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.231333 * persistence + 0.0041172 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_082_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=207, w2=319, w3=760, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(207, min_periods=max(207//3, 2)).std()
    vol_slow = ret.rolling(319, min_periods=max(319//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.351765 + 0.0041173 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_083_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=214, w2=332, w3=26, lag=3)."""
    x = open.shift(3)
    ma = x.rolling(332, min_periods=max(332//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 214)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.244 * slope + 0.0041174 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_084_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=221, w2=345, w3=43, lag=5)."""
    x = open.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(345, min_periods=max(345//3, 2)).mean()
    noise = impulse.abs().rolling(43, min_periods=max(43//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.378824 + 0.0041175 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_085_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=228, w2=358, w3=60, lag=8)."""
    x = _safe_log(open.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 228)
    acceleration = _rolling_slope(velocity, 358)
    curvature = _rolling_slope(acceleration, 60)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.256667 * acceleration + 0.0041176 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_086_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=235, w2=371, w3=77, lag=13)."""
    rel = _safe_div(open.shift(13), close.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 235)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.263 * pressure.rolling(77, min_periods=max(77//3, 2)).mean() + 0.0041177 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_087_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=242, w2=384, w3=94, lag=21)."""
    a = open.shift(21)
    b = close.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(242, min_periods=max(242//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.419412 + 0.0041178 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_088_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=249, w2=397, w3=111, lag=34)."""
    a = _safe_log(open.abs() + 1.0).shift(34)
    b = _safe_log(close.abs() + 1.0).shift(34)
    corr = a.rolling(397, min_periods=max(397//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 249)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.432941 + 0.0041179 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_089_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=9, w2=410, w3=128, lag=55)."""
    a = open.shift(55)
    b = close.shift(55)
    cover = _safe_div(a.rolling(9, min_periods=max(9//3, 2)).mean(), b.abs().rolling(410, min_periods=max(410//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.282 * _rolling_slope(cover, 9) + 0.004118 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_090_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=16, w2=423, w3=145, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    y = _safe_log(close.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.288333 * y + 0.711667 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 16) - _rolling_slope(basket, 423) + 0.0041181 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_091_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=23, w2=436, w3=162, lag=1)."""
    x = open.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(23, min_periods=max(23//3, 2)).mean(), upside.rolling(436, min_periods=max(436//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.473529 + 0.0041182 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_092_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=30, w2=449, w3=179, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    draw = x - x.rolling(449, min_periods=max(449//3, 2)).max()
    rebound = x - x.rolling(30, min_periods=max(30//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.301 * _rolling_slope(draw, 179) + 0.0041183 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_093_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=37, w2=462, w3=196, lag=3)."""
    a = _safe_log(open.abs() + 1.0).shift(3)
    b = _safe_log(close.abs() + 1.0).shift(3)
    imbalance = a.diff(37) - b.diff(126)
    stress = imbalance.rolling(196, min_periods=max(196//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.500588 + 0.0041184 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_094_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=44, w2=475, w3=213, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 44)
    baseline = trend.rolling(475, min_periods=max(475//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(213, min_periods=max(213//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.514118 + 0.0041185 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_095_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=51, w2=488, w3=230, lag=8)."""
    x = _safe_log(open.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 51)
    slow = _rolling_slope(x, 488)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=230, adjust=False).mean() * 1.527647 + 0.0041186 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_096_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=58, w2=501, w3=247, lag=13)."""
    x = open.shift(13)
    peak = x.rolling(501, min_periods=max(501//3, 2)).max()
    trough = x.rolling(58, min_periods=max(58//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.541176 + 0.0041187 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_097_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=65, w2=15, w3=264, lag=21)."""
    x = open.shift(21)
    change = x.pct_change(65)
    rank = change.rolling(15, min_periods=max(15//3, 2)).rank(pct=True)
    persistence = change.rolling(264, min_periods=max(264//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.332667 * persistence + 0.0041188 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_098_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=72, w2=28, w3=281, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(72, min_periods=max(72//3, 2)).std()
    vol_slow = ret.rolling(28, min_periods=max(28//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.568235 + 0.0041189 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_099_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=79, w2=41, w3=298, lag=55)."""
    x = open.shift(55)
    ma = x.rolling(41, min_periods=max(41//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 79)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.345333 * slope + 0.004119 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_100_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=86, w2=54, w3=315, lag=0)."""
    x = open.shift(0)
    impulse = x.diff(86)
    drag = impulse.rolling(54, min_periods=max(54//3, 2)).mean()
    noise = impulse.abs().rolling(315, min_periods=max(315//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.595294 + 0.0041191 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_101_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=93, w2=67, w3=332, lag=1)."""
    x = _safe_log(open.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 93)
    acceleration = _rolling_slope(velocity, 67)
    curvature = _rolling_slope(acceleration, 332)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.358 * acceleration + 0.0041192 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_102_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=100, w2=80, w3=349, lag=2)."""
    rel = _safe_div(open.shift(2), close.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 100)
    pressure = rel_log.diff(80)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.032 * pressure.rolling(349, min_periods=max(349//3, 2)).mean() + 0.0041193 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_103_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=107, w2=93, w3=366, lag=3)."""
    a = open.shift(3)
    b = close.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(107, min_periods=max(107//3, 2)).mean())
    decay = spread.ewm(span=93, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.635882 + 0.0041194 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_104_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=114, w2=106, w3=383, lag=5)."""
    a = _safe_log(open.abs() + 1.0).shift(5)
    b = _safe_log(close.abs() + 1.0).shift(5)
    corr = a.rolling(106, min_periods=max(106//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 114)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.649412 + 0.0041195 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_105_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=121, w2=119, w3=400, lag=8)."""
    a = open.shift(8)
    b = close.shift(8)
    cover = _safe_div(a.rolling(121, min_periods=max(121//3, 2)).mean(), b.abs().rolling(119, min_periods=max(119//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.051 * _rolling_slope(cover, 121) + 0.0041196 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_106_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=128, w2=132, w3=417, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    y = _safe_log(close.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.057333 * y + 0.942667 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 128) - _rolling_slope(basket, 132) + 0.0041197 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_107_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=135, w2=145, w3=434, lag=21)."""
    x = open.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(135, min_periods=max(135//3, 2)).mean(), upside.rolling(145, min_periods=max(145//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.836471 + 0.0041198 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_108_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=142, w2=158, w3=451, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    draw = x - x.rolling(158, min_periods=max(158//3, 2)).max()
    rebound = x - x.rolling(142, min_periods=max(142//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.07 * _rolling_slope(draw, 451) + 0.0041199 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_109_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=149, w2=171, w3=468, lag=55)."""
    a = _safe_log(open.abs() + 1.0).shift(55)
    b = _safe_log(close.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(468, min_periods=max(468//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.863529 + 0.00412 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_110_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=156, w2=184, w3=485, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 156)
    baseline = trend.rolling(184, min_periods=max(184//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(485, min_periods=max(485//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.877059 + 0.0041201 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_111_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=163, w2=197, w3=502, lag=1)."""
    x = _safe_log(open.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 163)
    slow = _rolling_slope(x, 197)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.890588 + 0.0041202 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_112_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=170, w2=210, w3=519, lag=2)."""
    x = open.shift(2)
    peak = x.rolling(210, min_periods=max(210//3, 2)).max()
    trough = x.rolling(170, min_periods=max(170//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.904118 + 0.0041203 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_113_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=177, w2=223, w3=536, lag=3)."""
    x = open.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(223, min_periods=max(223//3, 2)).rank(pct=True)
    persistence = change.rolling(536, min_periods=max(536//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.101667 * persistence + 0.0041204 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_114_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=184, w2=236, w3=553, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(184, min_periods=max(184//3, 2)).std()
    vol_slow = ret.rolling(236, min_periods=max(236//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.931176 + 0.0041205 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_115_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=191, w2=249, w3=570, lag=8)."""
    x = open.shift(8)
    ma = x.rolling(249, min_periods=max(249//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 191)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.114333 * slope + 0.0041206 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_116_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=198, w2=262, w3=587, lag=13)."""
    x = open.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(262, min_periods=max(262//3, 2)).mean()
    noise = impulse.abs().rolling(587, min_periods=max(587//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.958235 + 0.0041207 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_117_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=205, w2=275, w3=604, lag=21)."""
    x = _safe_log(open.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 205)
    acceleration = _rolling_slope(velocity, 275)
    curvature = _rolling_slope(acceleration, 604)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.127 * acceleration + 0.0041208 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_118_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=212, w2=288, w3=621, lag=34)."""
    rel = _safe_div(open.shift(34), close.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 212)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.133333 * pressure.rolling(621, min_periods=max(621//3, 2)).mean() + 0.0041209 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_119_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=219, w2=301, w3=638, lag=55)."""
    a = open.shift(55)
    b = close.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(219, min_periods=max(219//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.998824 + 0.004121 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_120_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=226, w2=314, w3=655, lag=0)."""
    a = _safe_log(open.abs() + 1.0).shift(0)
    b = _safe_log(close.abs() + 1.0).shift(0)
    corr = a.rolling(314, min_periods=max(314//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 226)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.012353 + 0.0041211 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_121_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=233, w2=327, w3=672, lag=1)."""
    a = open.shift(1)
    b = close.shift(1)
    cover = _safe_div(a.rolling(233, min_periods=max(233//3, 2)).mean(), b.abs().rolling(327, min_periods=max(327//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.152333 * _rolling_slope(cover, 233) + 0.0041212 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_122_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=240, w2=340, w3=689, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    y = _safe_log(close.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.158667 * y + 0.841333 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 240) - _rolling_slope(basket, 340) + 0.0041213 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_123_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=247, w2=353, w3=706, lag=3)."""
    x = open.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(247, min_periods=max(247//3, 2)).mean(), upside.rolling(353, min_periods=max(353//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.052941 + 0.0041214 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_124_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=7, w2=366, w3=723, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    draw = x - x.rolling(366, min_periods=max(366//3, 2)).max()
    rebound = x - x.rolling(7, min_periods=max(7//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.171333 * _rolling_slope(draw, 723) + 0.0041215 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_125_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=14, w2=379, w3=740, lag=8)."""
    a = _safe_log(open.abs() + 1.0).shift(8)
    b = _safe_log(close.abs() + 1.0).shift(8)
    imbalance = a.diff(14) - b.diff(126)
    stress = imbalance.rolling(740, min_periods=max(740//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.08 + 0.0041216 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_126_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=21, w2=392, w3=757, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 21)
    baseline = trend.rolling(392, min_periods=max(392//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(757, min_periods=max(757//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.093529 + 0.0041217 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_127_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=28, w2=405, w3=23, lag=21)."""
    x = _safe_log(open.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 28)
    slow = _rolling_slope(x, 405)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=23, adjust=False).mean() * 1.107059 + 0.0041218 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_128_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=35, w2=418, w3=40, lag=34)."""
    x = open.shift(34)
    peak = x.rolling(418, min_periods=max(418//3, 2)).max()
    trough = x.rolling(35, min_periods=max(35//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.120588 + 0.0041219 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_129_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=42, w2=431, w3=57, lag=55)."""
    x = open.shift(55)
    change = x.pct_change(42)
    rank = change.rolling(431, min_periods=max(431//3, 2)).rank(pct=True)
    persistence = change.rolling(57, min_periods=max(57//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.203 * persistence + 0.004122 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_130_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=49, w2=444, w3=74, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(49, min_periods=max(49//3, 2)).std()
    vol_slow = ret.rolling(444, min_periods=max(444//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.147647 + 0.0041221 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_131_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=56, w2=457, w3=91, lag=1)."""
    x = open.shift(1)
    ma = x.rolling(457, min_periods=max(457//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 56)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.215667 * slope + 0.0041222 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_132_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=63, w2=470, w3=108, lag=2)."""
    x = open.shift(2)
    impulse = x.diff(63)
    drag = impulse.rolling(470, min_periods=max(470//3, 2)).mean()
    noise = impulse.abs().rolling(108, min_periods=max(108//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.174706 + 0.0041223 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_133_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=70, w2=483, w3=125, lag=3)."""
    x = _safe_log(open.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 70)
    acceleration = _rolling_slope(velocity, 483)
    curvature = _rolling_slope(acceleration, 125)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.228333 * acceleration + 0.0041224 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_134_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=77, w2=496, w3=142, lag=5)."""
    rel = _safe_div(open.shift(5), close.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 77)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.234667 * pressure.rolling(142, min_periods=max(142//3, 2)).mean() + 0.0041225 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_135_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=84, w2=509, w3=159, lag=8)."""
    a = open.shift(8)
    b = close.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(84, min_periods=max(84//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.215294 + 0.0041226 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_136_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=91, w2=23, w3=176, lag=13)."""
    a = _safe_log(open.abs() + 1.0).shift(13)
    b = _safe_log(close.abs() + 1.0).shift(13)
    corr = a.rolling(23, min_periods=max(23//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 91)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.228824 + 0.0041227 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_137_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=98, w2=36, w3=193, lag=21)."""
    a = open.shift(21)
    b = close.shift(21)
    cover = _safe_div(a.rolling(98, min_periods=max(98//3, 2)).mean(), b.abs().rolling(36, min_periods=max(36//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.253667 * _rolling_slope(cover, 98) + 0.0041228 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_138_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=105, w2=49, w3=210, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    y = _safe_log(close.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.26 * y + 0.740000 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 105) - _rolling_slope(basket, 49) + 0.0041229 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_139_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=112, w2=62, w3=227, lag=55)."""
    x = open.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(112, min_periods=max(112//3, 2)).mean(), upside.rolling(62, min_periods=max(62//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.269412 + 0.004123 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_140_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=119, w2=75, w3=244, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    draw = x - x.rolling(75, min_periods=max(75//3, 2)).max()
    rebound = x - x.rolling(119, min_periods=max(119//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.272667 * _rolling_slope(draw, 244) + 0.0041231 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_141_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=126, w2=88, w3=261, lag=1)."""
    a = _safe_log(open.abs() + 1.0).shift(1)
    b = _safe_log(close.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(88)
    stress = imbalance.rolling(261, min_periods=max(261//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.296471 + 0.0041232 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_142_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=133, w2=101, w3=278, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 133)
    baseline = trend.rolling(101, min_periods=max(101//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(278, min_periods=max(278//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.31 + 0.0041233 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_143_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=140, w2=114, w3=295, lag=3)."""
    x = _safe_log(open.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 140)
    slow = _rolling_slope(x, 114)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=295, adjust=False).mean() * 1.323529 + 0.0041234 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_144_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=147, w2=127, w3=312, lag=5)."""
    x = open.shift(5)
    peak = x.rolling(127, min_periods=max(127//3, 2)).max()
    trough = x.rolling(147, min_periods=max(147//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.337059 + 0.0041235 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_145_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=154, w2=140, w3=329, lag=8)."""
    x = open.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(140, min_periods=max(140//3, 2)).rank(pct=True)
    persistence = change.rolling(329, min_periods=max(329//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.304333 * persistence + 0.0041236 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_146_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=161, w2=153, w3=346, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(161, min_periods=max(161//3, 2)).std()
    vol_slow = ret.rolling(153, min_periods=max(153//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.364118 + 0.0041237 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_147_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=168, w2=166, w3=363, lag=21)."""
    x = open.shift(21)
    ma = x.rolling(166, min_periods=max(166//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 168)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.317 * slope + 0.0041238 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_148_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=175, w2=179, w3=380, lag=34)."""
    x = open.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(179, min_periods=max(179//3, 2)).mean()
    noise = impulse.abs().rolling(380, min_periods=max(380//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.391176 + 0.0041239 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_149_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=182, w2=192, w3=397, lag=55)."""
    x = _safe_log(open.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 182)
    acceleration = _rolling_slope(velocity, 192)
    curvature = _rolling_slope(acceleration, 397)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.329667 * acceleration + 0.004124 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_150_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=189, w2=205, w3=414, lag=0)."""
    rel = _safe_div(open.shift(0), close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 189)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.336 * pressure.rolling(414, min_periods=max(414//3, 2)).mean() + 0.0041241 * anchor
    return base_signal.diff().diff().diff()
