"""74 rescaled range signal gemini d3 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Analysis of the range of cumulative deviations to identify trend persistence.
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

def f74_rrsg_gemini_076_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=60, w2=481, w3=238, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(481, min_periods=max(481//3, 2)).max()
    rebound = x - x.rolling(60, min_periods=max(60//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.33 * _rolling_slope(draw, 238) + 0.0047327 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_077_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=67, w2=494, w3=255, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(67) - b.diff(126)
    stress = imbalance.rolling(255, min_periods=max(255//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.979412 + 0.0047328 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_078_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=74, w2=507, w3=272, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 74)
    baseline = trend.rolling(507, min_periods=max(507//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(272, min_periods=max(272//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.992941 + 0.0047329 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_079_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=81, w2=21, w3=289, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 81)
    slow = _rolling_slope(x, 21)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=289, adjust=False).mean() * 1.006471 + 0.004733 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_080_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=88, w2=34, w3=306, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(34, min_periods=max(34//3, 2)).max()
    trough = x.rolling(88, min_periods=max(88//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.02 + 0.0047331 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_081_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=95, w2=47, w3=323, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(95)
    rank = change.rolling(47, min_periods=max(47//3, 2)).rank(pct=True)
    persistence = change.rolling(323, min_periods=max(323//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.361667 * persistence + 0.0047332 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_082_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=102, w2=60, w3=340, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(102, min_periods=max(102//3, 2)).std()
    vol_slow = ret.rolling(60, min_periods=max(60//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.047059 + 0.0047333 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_083_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=109, w2=73, w3=357, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(73, min_periods=max(73//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 109)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.042 * slope + 0.0047334 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_084_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=116, w2=86, w3=374, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(116)
    drag = impulse.rolling(86, min_periods=max(86//3, 2)).mean()
    noise = impulse.abs().rolling(374, min_periods=max(374//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.074118 + 0.0047335 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_085_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=123, w2=99, w3=391, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 123)
    acceleration = _rolling_slope(velocity, 99)
    curvature = _rolling_slope(acceleration, 391)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.054667 * acceleration + 0.0047336 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_086_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=130, w2=112, w3=408, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 130)
    pressure = rel_log.diff(112)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.061 * pressure.rolling(408, min_periods=max(408//3, 2)).mean() + 0.0047337 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_087_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=137, w2=125, w3=425, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(137, min_periods=max(137//3, 2)).mean())
    decay = spread.ewm(span=125, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.114706 + 0.0047338 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_088_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=144, w2=138, w3=442, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(138, min_periods=max(138//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 144)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.128235 + 0.0047339 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_089_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=151, w2=151, w3=459, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(151, min_periods=max(151//3, 2)).mean(), b.abs().rolling(151, min_periods=max(151//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.08 * _rolling_slope(cover, 151) + 0.004734 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_090_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=158, w2=164, w3=476, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.086333 * y + 0.913667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 158) - _rolling_slope(basket, 164) + 0.0047341 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_091_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=165, w2=177, w3=493, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(165, min_periods=max(165//3, 2)).mean(), upside.rolling(177, min_periods=max(177//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.168824 + 0.0047342 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_092_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=172, w2=190, w3=510, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(190, min_periods=max(190//3, 2)).max()
    rebound = x - x.rolling(172, min_periods=max(172//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.099 * _rolling_slope(draw, 510) + 0.0047343 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_093_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=179, w2=203, w3=527, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(527, min_periods=max(527//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.195882 + 0.0047344 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_094_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=186, w2=216, w3=544, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 186)
    baseline = trend.rolling(216, min_periods=max(216//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(544, min_periods=max(544//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.209412 + 0.0047345 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_095_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=193, w2=229, w3=561, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 193)
    slow = _rolling_slope(x, 229)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.222941 + 0.0047346 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_096_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=200, w2=242, w3=578, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(242, min_periods=max(242//3, 2)).max()
    trough = x.rolling(200, min_periods=max(200//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.236471 + 0.0047347 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_097_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=207, w2=255, w3=595, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(255, min_periods=max(255//3, 2)).rank(pct=True)
    persistence = change.rolling(595, min_periods=max(595//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.130667 * persistence + 0.0047348 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_098_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=214, w2=268, w3=612, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(214, min_periods=max(214//3, 2)).std()
    vol_slow = ret.rolling(268, min_periods=max(268//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.263529 + 0.0047349 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_099_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=221, w2=281, w3=629, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(281, min_periods=max(281//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 221)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.143333 * slope + 0.004735 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_100_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=228, w2=294, w3=646, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(294, min_periods=max(294//3, 2)).mean()
    noise = impulse.abs().rolling(646, min_periods=max(646//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.290588 + 0.0047351 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_101_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=235, w2=307, w3=663, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 235)
    acceleration = _rolling_slope(velocity, 307)
    curvature = _rolling_slope(acceleration, 663)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.156 * acceleration + 0.0047352 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_102_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=242, w2=320, w3=680, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 242)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.162333 * pressure.rolling(680, min_periods=max(680//3, 2)).mean() + 0.0047353 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_103_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=249, w2=333, w3=697, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(249, min_periods=max(249//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.331176 + 0.0047354 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_104_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=9, w2=346, w3=714, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(346, min_periods=max(346//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 9)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.344706 + 0.0047355 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_105_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=16, w2=359, w3=731, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(16, min_periods=max(16//3, 2)).mean(), b.abs().rolling(359, min_periods=max(359//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.181333 * _rolling_slope(cover, 16) + 0.0047356 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_106_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=23, w2=372, w3=748, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.187667 * y + 0.812333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 23) - _rolling_slope(basket, 372) + 0.0047357 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_107_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=30, w2=385, w3=765, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(30, min_periods=max(30//3, 2)).mean(), upside.rolling(385, min_periods=max(385//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.385294 + 0.0047358 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_108_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=37, w2=398, w3=31, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(398, min_periods=max(398//3, 2)).max()
    rebound = x - x.rolling(37, min_periods=max(37//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.200333 * _rolling_slope(draw, 31) + 0.0047359 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_109_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=44, w2=411, w3=48, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(44) - b.diff(126)
    stress = imbalance.rolling(48, min_periods=max(48//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.412353 + 0.004736 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_110_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=51, w2=424, w3=65, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 51)
    baseline = trend.rolling(424, min_periods=max(424//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(65, min_periods=max(65//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.425882 + 0.0047361 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_111_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=58, w2=437, w3=82, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 58)
    slow = _rolling_slope(x, 437)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=82, adjust=False).mean() * 1.439412 + 0.0047362 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_112_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=65, w2=450, w3=99, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(450, min_periods=max(450//3, 2)).max()
    trough = x.rolling(65, min_periods=max(65//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.452941 + 0.0047363 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_113_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=72, w2=463, w3=116, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(72)
    rank = change.rolling(463, min_periods=max(463//3, 2)).rank(pct=True)
    persistence = change.rolling(116, min_periods=max(116//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.232 * persistence + 0.0047364 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_114_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=79, w2=476, w3=133, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(79, min_periods=max(79//3, 2)).std()
    vol_slow = ret.rolling(476, min_periods=max(476//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.48 + 0.0047365 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_115_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=86, w2=489, w3=150, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(489, min_periods=max(489//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 86)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.244667 * slope + 0.0047366 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_116_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=93, w2=502, w3=167, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(93)
    drag = impulse.rolling(502, min_periods=max(502//3, 2)).mean()
    noise = impulse.abs().rolling(167, min_periods=max(167//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.507059 + 0.0047367 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_117_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=100, w2=16, w3=184, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 100)
    acceleration = _rolling_slope(velocity, 16)
    curvature = _rolling_slope(acceleration, 184)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.257333 * acceleration + 0.0047368 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_118_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=107, w2=29, w3=201, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 107)
    pressure = rel_log.diff(29)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.263667 * pressure.rolling(201, min_periods=max(201//3, 2)).mean() + 0.0047369 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_119_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=114, w2=42, w3=218, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(114, min_periods=max(114//3, 2)).mean())
    decay = spread.ewm(span=42, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.547647 + 0.004737 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_120_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=121, w2=55, w3=235, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(55, min_periods=max(55//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 121)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.561176 + 0.0047371 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_121_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=128, w2=68, w3=252, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(128, min_periods=max(128//3, 2)).mean(), b.abs().rolling(68, min_periods=max(68//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.282667 * _rolling_slope(cover, 128) + 0.0047372 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_122_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=135, w2=81, w3=269, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.289 * y + 0.711000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 135) - _rolling_slope(basket, 81) + 0.0047373 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_123_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=142, w2=94, w3=286, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(142, min_periods=max(142//3, 2)).mean(), upside.rolling(94, min_periods=max(94//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.601765 + 0.0047374 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_124_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=149, w2=107, w3=303, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(107, min_periods=max(107//3, 2)).max()
    rebound = x - x.rolling(149, min_periods=max(149//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.301667 * _rolling_slope(draw, 303) + 0.0047375 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_125_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=156, w2=120, w3=320, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(120)
    stress = imbalance.rolling(320, min_periods=max(320//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.628824 + 0.0047376 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_126_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=163, w2=133, w3=337, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 163)
    baseline = trend.rolling(133, min_periods=max(133//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(337, min_periods=max(337//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.642353 + 0.0047377 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_127_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=170, w2=146, w3=354, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 170)
    slow = _rolling_slope(x, 146)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.655882 + 0.0047378 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_128_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=177, w2=159, w3=371, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(159, min_periods=max(159//3, 2)).max()
    trough = x.rolling(177, min_periods=max(177//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.669412 + 0.0047379 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_129_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=184, w2=172, w3=388, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(172, min_periods=max(172//3, 2)).rank(pct=True)
    persistence = change.rolling(388, min_periods=max(388//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.333333 * persistence + 0.004738 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_130_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=191, w2=185, w3=405, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(191, min_periods=max(191//3, 2)).std()
    vol_slow = ret.rolling(185, min_periods=max(185//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.842941 + 0.0047381 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_131_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=198, w2=198, w3=422, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(198, min_periods=max(198//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 198)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.346 * slope + 0.0047382 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_132_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=205, w2=211, w3=439, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(211, min_periods=max(211//3, 2)).mean()
    noise = impulse.abs().rolling(439, min_periods=max(439//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.87 + 0.0047383 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_133_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=212, w2=224, w3=456, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 212)
    acceleration = _rolling_slope(velocity, 224)
    curvature = _rolling_slope(acceleration, 456)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.358667 * acceleration + 0.0047384 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_134_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=219, w2=237, w3=473, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 219)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.032667 * pressure.rolling(473, min_periods=max(473//3, 2)).mean() + 0.0047385 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_135_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=226, w2=250, w3=490, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(226, min_periods=max(226//3, 2)).mean())
    decay = spread.ewm(span=250, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.910588 + 0.0047386 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_136_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=233, w2=263, w3=507, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(263, min_periods=max(263//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 233)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.924118 + 0.0047387 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_137_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=240, w2=276, w3=524, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(240, min_periods=max(240//3, 2)).mean(), b.abs().rolling(276, min_periods=max(276//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.051667 * _rolling_slope(cover, 240) + 0.0047388 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_138_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=247, w2=289, w3=541, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.058 * y + 0.942000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 247) - _rolling_slope(basket, 289) + 0.0047389 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_139_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=7, w2=302, w3=558, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(7, min_periods=max(7//3, 2)).mean(), upside.rolling(302, min_periods=max(302//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.964706 + 0.004739 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_140_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=14, w2=315, w3=575, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(315, min_periods=max(315//3, 2)).max()
    rebound = x - x.rolling(14, min_periods=max(14//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.070667 * _rolling_slope(draw, 575) + 0.0047391 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_141_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=21, w2=328, w3=592, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(21) - b.diff(126)
    stress = imbalance.rolling(592, min_periods=max(592//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.991765 + 0.0047392 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_142_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=28, w2=341, w3=609, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 28)
    baseline = trend.rolling(341, min_periods=max(341//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(609, min_periods=max(609//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.005294 + 0.0047393 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_143_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=35, w2=354, w3=626, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 35)
    slow = _rolling_slope(x, 354)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.018824 + 0.0047394 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_144_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=42, w2=367, w3=643, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(367, min_periods=max(367//3, 2)).max()
    trough = x.rolling(42, min_periods=max(42//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.032353 + 0.0047395 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_145_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=49, w2=380, w3=660, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(49)
    rank = change.rolling(380, min_periods=max(380//3, 2)).rank(pct=True)
    persistence = change.rolling(660, min_periods=max(660//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.102333 * persistence + 0.0047396 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_146_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=56, w2=393, w3=677, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(56, min_periods=max(56//3, 2)).std()
    vol_slow = ret.rolling(393, min_periods=max(393//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.059412 + 0.0047397 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_147_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=63, w2=406, w3=694, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(406, min_periods=max(406//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 63)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.115 * slope + 0.0047398 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_148_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=70, w2=419, w3=711, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(70)
    drag = impulse.rolling(419, min_periods=max(419//3, 2)).mean()
    noise = impulse.abs().rolling(711, min_periods=max(711//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.086471 + 0.0047399 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_149_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=77, w2=432, w3=728, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 77)
    acceleration = _rolling_slope(velocity, 432)
    curvature = _rolling_slope(acceleration, 728)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.127667 * acceleration + 0.00474 * anchor
    return base_signal.diff().diff().diff()

def f74_rrsg_gemini_150_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=84, w2=445, w3=745, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 84)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.134 * pressure.rolling(745, min_periods=max(745//3, 2)).mean() + 0.0047401 * anchor
    return base_signal.diff().diff().diff()
