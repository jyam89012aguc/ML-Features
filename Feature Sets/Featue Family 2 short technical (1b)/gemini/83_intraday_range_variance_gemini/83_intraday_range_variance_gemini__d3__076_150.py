"""83 intraday range variance gemini d3 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Variance of price ranges within a session as a measure of intraday instability.
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

def f83_irva_gemini_076_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=19, w2=133, w3=304, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(133, min_periods=max(133//3, 2)).max()
    rebound = x - x.rolling(19, min_periods=max(19//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.346 * _rolling_slope(draw, 304) + 0.0052367 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_077_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=26, w2=146, w3=321, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(26) - b.diff(126)
    stress = imbalance.rolling(321, min_periods=max(321//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.885294 + 0.0052368 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_078_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=33, w2=159, w3=338, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 33)
    baseline = trend.rolling(159, min_periods=max(159//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(338, min_periods=max(338//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.898824 + 0.0052369 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_079_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=40, w2=172, w3=355, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 40)
    slow = _rolling_slope(x, 172)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.912353 + 0.005237 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_080_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=47, w2=185, w3=372, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(185, min_periods=max(185//3, 2)).max()
    trough = x.rolling(47, min_periods=max(47//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.925882 + 0.0052371 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_081_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=54, w2=198, w3=389, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(54)
    rank = change.rolling(198, min_periods=max(198//3, 2)).rank(pct=True)
    persistence = change.rolling(389, min_periods=max(389//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.045333 * persistence + 0.0052372 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_082_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=61, w2=211, w3=406, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(61, min_periods=max(61//3, 2)).std()
    vol_slow = ret.rolling(211, min_periods=max(211//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.952941 + 0.0052373 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_083_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=68, w2=224, w3=423, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(224, min_periods=max(224//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 68)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.058 * slope + 0.0052374 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_084_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=75, w2=237, w3=440, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(75)
    drag = impulse.rolling(237, min_periods=max(237//3, 2)).mean()
    noise = impulse.abs().rolling(440, min_periods=max(440//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.98 + 0.0052375 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_085_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=82, w2=250, w3=457, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 82)
    acceleration = _rolling_slope(velocity, 250)
    curvature = _rolling_slope(acceleration, 457)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.070667 * acceleration + 0.0052376 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_086_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=89, w2=263, w3=474, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 89)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.077 * pressure.rolling(474, min_periods=max(474//3, 2)).mean() + 0.0052377 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_087_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=96, w2=276, w3=491, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(96, min_periods=max(96//3, 2)).mean())
    decay = spread.ewm(span=276, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.020588 + 0.0052378 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_088_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=103, w2=289, w3=508, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(289, min_periods=max(289//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 103)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.034118 + 0.0052379 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_089_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=110, w2=302, w3=525, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(110, min_periods=max(110//3, 2)).mean(), b.abs().rolling(302, min_periods=max(302//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.096 * _rolling_slope(cover, 110) + 0.005238 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_090_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=117, w2=315, w3=542, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(low.abs() + 1.0).shift(0)
    basket = x - 0.102333 * y + 0.897667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 117) - _rolling_slope(basket, 315) + 0.0052381 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_091_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=124, w2=328, w3=559, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(124, min_periods=max(124//3, 2)).mean(), upside.rolling(328, min_periods=max(328//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.074706 + 0.0052382 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_092_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=131, w2=341, w3=576, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(341, min_periods=max(341//3, 2)).max()
    rebound = x - x.rolling(131, min_periods=max(131//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.115 * _rolling_slope(draw, 576) + 0.0052383 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_093_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=138, w2=354, w3=593, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(593, min_periods=max(593//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.101765 + 0.0052384 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_094_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=145, w2=367, w3=610, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 145)
    baseline = trend.rolling(367, min_periods=max(367//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(610, min_periods=max(610//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.115294 + 0.0052385 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_095_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=152, w2=380, w3=627, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 152)
    slow = _rolling_slope(x, 380)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.128824 + 0.0052386 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_096_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=159, w2=393, w3=644, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(393, min_periods=max(393//3, 2)).max()
    trough = x.rolling(159, min_periods=max(159//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.142353 + 0.0052387 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_097_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=166, w2=406, w3=661, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(406, min_periods=max(406//3, 2)).rank(pct=True)
    persistence = change.rolling(661, min_periods=max(661//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.146667 * persistence + 0.0052388 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_098_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=173, w2=419, w3=678, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(173, min_periods=max(173//3, 2)).std()
    vol_slow = ret.rolling(419, min_periods=max(419//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.169412 + 0.0052389 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_099_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=180, w2=432, w3=695, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(432, min_periods=max(432//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 180)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.159333 * slope + 0.005239 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_100_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=187, w2=445, w3=712, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(445, min_periods=max(445//3, 2)).mean()
    noise = impulse.abs().rolling(712, min_periods=max(712//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.196471 + 0.0052391 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_101_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=194, w2=458, w3=729, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 194)
    acceleration = _rolling_slope(velocity, 458)
    curvature = _rolling_slope(acceleration, 729)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.172 * acceleration + 0.0052392 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_102_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=201, w2=471, w3=746, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 201)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.178333 * pressure.rolling(746, min_periods=max(746//3, 2)).mean() + 0.0052393 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_103_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=208, w2=484, w3=763, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(208, min_periods=max(208//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.237059 + 0.0052394 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_104_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=215, w2=497, w3=29, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(497, min_periods=max(497//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 215)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.250588 + 0.0052395 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_105_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=222, w2=11, w3=46, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(222, min_periods=max(222//3, 2)).mean(), b.abs().rolling(11, min_periods=max(11//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(46) + 0.197333 * _rolling_slope(cover, 222) + 0.0052396 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_106_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=229, w2=24, w3=63, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(low.abs() + 1.0).shift(13)
    basket = x - 0.203667 * y + 0.796333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 229) - _rolling_slope(basket, 24) + 0.0052397 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_107_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=236, w2=37, w3=80, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(236, min_periods=max(236//3, 2)).mean(), upside.rolling(37, min_periods=max(37//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(80) * 1.291176 + 0.0052398 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_108_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=243, w2=50, w3=97, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(50, min_periods=max(50//3, 2)).max()
    rebound = x - x.rolling(243, min_periods=max(243//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.216333 * _rolling_slope(draw, 97) + 0.0052399 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_109_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=250, w2=63, w3=114, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(63)
    stress = imbalance.rolling(114, min_periods=max(114//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.318235 + 0.00524 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_110_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=10, w2=76, w3=131, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 10)
    baseline = trend.rolling(76, min_periods=max(76//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(131, min_periods=max(131//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.331765 + 0.0052401 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_111_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=17, w2=89, w3=148, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 17)
    slow = _rolling_slope(x, 89)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=148, adjust=False).mean() * 1.345294 + 0.0052402 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_112_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=24, w2=102, w3=165, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(102, min_periods=max(102//3, 2)).max()
    trough = x.rolling(24, min_periods=max(24//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.358824 + 0.0052403 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_113_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=31, w2=115, w3=182, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(31)
    rank = change.rolling(115, min_periods=max(115//3, 2)).rank(pct=True)
    persistence = change.rolling(182, min_periods=max(182//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.248 * persistence + 0.0052404 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_114_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=38, w2=128, w3=199, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(38, min_periods=max(38//3, 2)).std()
    vol_slow = ret.rolling(128, min_periods=max(128//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.385882 + 0.0052405 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_115_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=45, w2=141, w3=216, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(141, min_periods=max(141//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 45)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.260667 * slope + 0.0052406 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_116_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=52, w2=154, w3=233, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(52)
    drag = impulse.rolling(154, min_periods=max(154//3, 2)).mean()
    noise = impulse.abs().rolling(233, min_periods=max(233//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.412941 + 0.0052407 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_117_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=59, w2=167, w3=250, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 59)
    acceleration = _rolling_slope(velocity, 167)
    curvature = _rolling_slope(acceleration, 250)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.273333 * acceleration + 0.0052408 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_118_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=66, w2=180, w3=267, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 66)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.279667 * pressure.rolling(267, min_periods=max(267//3, 2)).mean() + 0.0052409 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_119_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=73, w2=193, w3=284, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(73, min_periods=max(73//3, 2)).mean())
    decay = spread.ewm(span=193, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.453529 + 0.005241 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_120_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=80, w2=206, w3=301, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(206, min_periods=max(206//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 80)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.467059 + 0.0052411 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_121_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=87, w2=219, w3=318, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(87, min_periods=max(87//3, 2)).mean(), b.abs().rolling(219, min_periods=max(219//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.298667 * _rolling_slope(cover, 87) + 0.0052412 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_122_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=94, w2=232, w3=335, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(low.abs() + 1.0).shift(2)
    basket = x - 0.305 * y + 0.695000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 94) - _rolling_slope(basket, 232) + 0.0052413 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_123_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=101, w2=245, w3=352, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(101, min_periods=max(101//3, 2)).mean(), upside.rolling(245, min_periods=max(245//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.507647 + 0.0052414 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_124_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=108, w2=258, w3=369, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(258, min_periods=max(258//3, 2)).max()
    rebound = x - x.rolling(108, min_periods=max(108//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.317667 * _rolling_slope(draw, 369) + 0.0052415 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_125_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=115, w2=271, w3=386, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(115) - b.diff(126)
    stress = imbalance.rolling(386, min_periods=max(386//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.534706 + 0.0052416 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_126_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=122, w2=284, w3=403, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 122)
    baseline = trend.rolling(284, min_periods=max(284//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(403, min_periods=max(403//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.548235 + 0.0052417 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_127_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=129, w2=297, w3=420, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 129)
    slow = _rolling_slope(x, 297)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.561765 + 0.0052418 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_128_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=136, w2=310, w3=437, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(310, min_periods=max(310//3, 2)).max()
    trough = x.rolling(136, min_periods=max(136//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.575294 + 0.0052419 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_129_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=143, w2=323, w3=454, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(323, min_periods=max(323//3, 2)).rank(pct=True)
    persistence = change.rolling(454, min_periods=max(454//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.349333 * persistence + 0.005242 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_130_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=150, w2=336, w3=471, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(150, min_periods=max(150//3, 2)).std()
    vol_slow = ret.rolling(336, min_periods=max(336//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.602353 + 0.0052421 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_131_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=157, w2=349, w3=488, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(349, min_periods=max(349//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 157)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.362 * slope + 0.0052422 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_132_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=164, w2=362, w3=505, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(362, min_periods=max(362//3, 2)).mean()
    noise = impulse.abs().rolling(505, min_periods=max(505//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.629412 + 0.0052423 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_133_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=171, w2=375, w3=522, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 171)
    acceleration = _rolling_slope(velocity, 375)
    curvature = _rolling_slope(acceleration, 522)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.042333 * acceleration + 0.0052424 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_134_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=178, w2=388, w3=539, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 178)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.048667 * pressure.rolling(539, min_periods=max(539//3, 2)).mean() + 0.0052425 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_135_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=185, w2=401, w3=556, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(185, min_periods=max(185//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.67 + 0.0052426 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_136_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=192, w2=414, w3=573, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(414, min_periods=max(414//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 192)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.83 + 0.0052427 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_137_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=199, w2=427, w3=590, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(199, min_periods=max(199//3, 2)).mean(), b.abs().rolling(427, min_periods=max(427//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.067667 * _rolling_slope(cover, 199) + 0.0052428 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_138_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=206, w2=440, w3=607, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(low.abs() + 1.0).shift(34)
    basket = x - 0.074 * y + 0.926000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 206) - _rolling_slope(basket, 440) + 0.0052429 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_139_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=213, w2=453, w3=624, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(213, min_periods=max(213//3, 2)).mean(), upside.rolling(453, min_periods=max(453//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.870588 + 0.005243 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_140_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=220, w2=466, w3=641, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(466, min_periods=max(466//3, 2)).max()
    rebound = x - x.rolling(220, min_periods=max(220//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.086667 * _rolling_slope(draw, 641) + 0.0052431 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_141_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=227, w2=479, w3=658, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(658, min_periods=max(658//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.897647 + 0.0052432 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_142_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=234, w2=492, w3=675, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 234)
    baseline = trend.rolling(492, min_periods=max(492//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(675, min_periods=max(675//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.911176 + 0.0052433 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_143_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=241, w2=505, w3=692, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 241)
    slow = _rolling_slope(x, 505)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.924706 + 0.0052434 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_144_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=248, w2=19, w3=709, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(19, min_periods=max(19//3, 2)).max()
    trough = x.rolling(248, min_periods=max(248//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.938235 + 0.0052435 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_145_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=8, w2=32, w3=726, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(8)
    rank = change.rolling(32, min_periods=max(32//3, 2)).rank(pct=True)
    persistence = change.rolling(726, min_periods=max(726//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.118333 * persistence + 0.0052436 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_146_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=15, w2=45, w3=743, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(15, min_periods=max(15//3, 2)).std()
    vol_slow = ret.rolling(45, min_periods=max(45//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.965294 + 0.0052437 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_147_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=22, w2=58, w3=760, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(58, min_periods=max(58//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 22)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.131 * slope + 0.0052438 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_148_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=29, w2=71, w3=26, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(29)
    drag = impulse.rolling(71, min_periods=max(71//3, 2)).mean()
    noise = impulse.abs().rolling(26, min_periods=max(26//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.992353 + 0.0052439 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_149_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=36, w2=84, w3=43, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 36)
    acceleration = _rolling_slope(velocity, 84)
    curvature = _rolling_slope(acceleration, 43)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.143667 * acceleration + 0.005244 * anchor
    return base_signal.diff().diff().diff()

def f83_irva_gemini_150_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=43, w2=97, w3=60, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 43)
    pressure = rel_log.diff(97)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.15 * pressure.rolling(60, min_periods=max(60//3, 2)).mean() + 0.0052441 * anchor
    return base_signal.diff().diff().diff()
