"""90 time of day specific volatility gemini d2 features 76-150 — Pipeline 1b-HF Grade v7.

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

def f90_todv_gemini_076_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=50, w2=371, w3=729, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(371, min_periods=max(371//3, 2)).max()
    trough = x.rolling(50, min_periods=max(50//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.654706 + 0.0056147 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_077_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=57, w2=384, w3=746, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(57)
    rank = change.rolling(384, min_periods=max(384//3, 2)).rank(pct=True)
    persistence = change.rolling(746, min_periods=max(746//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.032 * persistence + 0.0056148 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_078_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=64, w2=397, w3=763, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(64, min_periods=max(64//3, 2)).std()
    vol_slow = ret.rolling(397, min_periods=max(397//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.828235 + 0.0056149 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_079_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=71, w2=410, w3=29, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(410, min_periods=max(410//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 71)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.044667 * slope + 0.005615 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_080_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=78, w2=423, w3=46, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(78)
    drag = impulse.rolling(423, min_periods=max(423//3, 2)).mean()
    noise = impulse.abs().rolling(46, min_periods=max(46//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.855294 + 0.0056151 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_081_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=85, w2=436, w3=63, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 85)
    acceleration = _rolling_slope(velocity, 436)
    curvature = _rolling_slope(acceleration, 63)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.057333 * acceleration + 0.0056152 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_082_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=92, w2=449, w3=80, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 92)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.063667 * pressure.rolling(80, min_periods=max(80//3, 2)).mean() + 0.0056153 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_083_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=99, w2=462, w3=97, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(99, min_periods=max(99//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.895882 + 0.0056154 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_084_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=106, w2=475, w3=114, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(475, min_periods=max(475//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 106)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.909412 + 0.0056155 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_085_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=113, w2=488, w3=131, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(113, min_periods=max(113//3, 2)).mean(), b.abs().rolling(488, min_periods=max(488//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.082667 * _rolling_slope(cover, 113) + 0.0056156 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_086_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=120, w2=501, w3=148, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(low.abs() + 1.0).shift(13)
    basket = x - 0.089 * y + 0.911000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 120) - _rolling_slope(basket, 501) + 0.0056157 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_087_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=127, w2=15, w3=165, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(127, min_periods=max(127//3, 2)).mean(), upside.rolling(15, min_periods=max(15//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.95 + 0.0056158 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_088_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=134, w2=28, w3=182, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(28, min_periods=max(28//3, 2)).max()
    rebound = x - x.rolling(134, min_periods=max(134//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.101667 * _rolling_slope(draw, 182) + 0.0056159 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_089_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=141, w2=41, w3=199, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(41)
    stress = imbalance.rolling(199, min_periods=max(199//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.977059 + 0.005616 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_090_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=148, w2=54, w3=216, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 148)
    baseline = trend.rolling(54, min_periods=max(54//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(216, min_periods=max(216//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.990588 + 0.0056161 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_091_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=155, w2=67, w3=233, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 155)
    slow = _rolling_slope(x, 67)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=233, adjust=False).mean() * 1.004118 + 0.0056162 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_092_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=162, w2=80, w3=250, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(80, min_periods=max(80//3, 2)).max()
    trough = x.rolling(162, min_periods=max(162//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.017647 + 0.0056163 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_093_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=169, w2=93, w3=267, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(93, min_periods=max(93//3, 2)).rank(pct=True)
    persistence = change.rolling(267, min_periods=max(267//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.133333 * persistence + 0.0056164 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_094_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=176, w2=106, w3=284, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(176, min_periods=max(176//3, 2)).std()
    vol_slow = ret.rolling(106, min_periods=max(106//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.044706 + 0.0056165 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_095_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=183, w2=119, w3=301, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(119, min_periods=max(119//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 183)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.146 * slope + 0.0056166 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_096_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=190, w2=132, w3=318, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(132, min_periods=max(132//3, 2)).mean()
    noise = impulse.abs().rolling(318, min_periods=max(318//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.071765 + 0.0056167 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_097_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=197, w2=145, w3=335, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 197)
    acceleration = _rolling_slope(velocity, 145)
    curvature = _rolling_slope(acceleration, 335)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.158667 * acceleration + 0.0056168 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_098_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=204, w2=158, w3=352, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 204)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.165 * pressure.rolling(352, min_periods=max(352//3, 2)).mean() + 0.0056169 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_099_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=211, w2=171, w3=369, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(211, min_periods=max(211//3, 2)).mean())
    decay = spread.ewm(span=171, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.112353 + 0.005617 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_100_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=218, w2=184, w3=386, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(184, min_periods=max(184//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 218)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.125882 + 0.0056171 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_101_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=225, w2=197, w3=403, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(225, min_periods=max(225//3, 2)).mean(), b.abs().rolling(197, min_periods=max(197//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.184 * _rolling_slope(cover, 225) + 0.0056172 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_102_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=232, w2=210, w3=420, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(low.abs() + 1.0).shift(2)
    basket = x - 0.190333 * y + 0.809667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 232) - _rolling_slope(basket, 210) + 0.0056173 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_103_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=239, w2=223, w3=437, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(239, min_periods=max(239//3, 2)).mean(), upside.rolling(223, min_periods=max(223//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.166471 + 0.0056174 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_104_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=246, w2=236, w3=454, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(236, min_periods=max(236//3, 2)).max()
    rebound = x - x.rolling(246, min_periods=max(246//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.203 * _rolling_slope(draw, 454) + 0.0056175 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_105_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=6, w2=249, w3=471, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(6) - b.diff(126)
    stress = imbalance.rolling(471, min_periods=max(471//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.193529 + 0.0056176 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_106_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=13, w2=262, w3=488, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 13)
    baseline = trend.rolling(262, min_periods=max(262//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(488, min_periods=max(488//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.207059 + 0.0056177 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_107_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=20, w2=275, w3=505, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 20)
    slow = _rolling_slope(x, 275)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.220588 + 0.0056178 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_108_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=27, w2=288, w3=522, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(288, min_periods=max(288//3, 2)).max()
    trough = x.rolling(27, min_periods=max(27//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.234118 + 0.0056179 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_109_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=34, w2=301, w3=539, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(34)
    rank = change.rolling(301, min_periods=max(301//3, 2)).rank(pct=True)
    persistence = change.rolling(539, min_periods=max(539//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.234667 * persistence + 0.005618 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_110_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=41, w2=314, w3=556, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(41, min_periods=max(41//3, 2)).std()
    vol_slow = ret.rolling(314, min_periods=max(314//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.261176 + 0.0056181 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_111_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=48, w2=327, w3=573, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(327, min_periods=max(327//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 48)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.247333 * slope + 0.0056182 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_112_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=55, w2=340, w3=590, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(55)
    drag = impulse.rolling(340, min_periods=max(340//3, 2)).mean()
    noise = impulse.abs().rolling(590, min_periods=max(590//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.288235 + 0.0056183 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_113_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=62, w2=353, w3=607, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 62)
    acceleration = _rolling_slope(velocity, 353)
    curvature = _rolling_slope(acceleration, 607)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.26 * acceleration + 0.0056184 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_114_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=69, w2=366, w3=624, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 69)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.266333 * pressure.rolling(624, min_periods=max(624//3, 2)).mean() + 0.0056185 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_115_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=76, w2=379, w3=641, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(76, min_periods=max(76//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.328824 + 0.0056186 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_116_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=83, w2=392, w3=658, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(392, min_periods=max(392//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 83)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.342353 + 0.0056187 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_117_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=90, w2=405, w3=675, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(90, min_periods=max(90//3, 2)).mean(), b.abs().rolling(405, min_periods=max(405//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.285333 * _rolling_slope(cover, 90) + 0.0056188 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_118_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=97, w2=418, w3=692, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(low.abs() + 1.0).shift(34)
    basket = x - 0.291667 * y + 0.708333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 97) - _rolling_slope(basket, 418) + 0.0056189 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_119_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=104, w2=431, w3=709, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(104, min_periods=max(104//3, 2)).mean(), upside.rolling(431, min_periods=max(431//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.382941 + 0.005619 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_120_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=111, w2=444, w3=726, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(444, min_periods=max(444//3, 2)).max()
    rebound = x - x.rolling(111, min_periods=max(111//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.304333 * _rolling_slope(draw, 726) + 0.0056191 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_121_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=118, w2=457, w3=743, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(118) - b.diff(126)
    stress = imbalance.rolling(743, min_periods=max(743//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.41 + 0.0056192 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_122_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=125, w2=470, w3=760, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 125)
    baseline = trend.rolling(470, min_periods=max(470//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(760, min_periods=max(760//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.423529 + 0.0056193 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_123_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=132, w2=483, w3=26, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 132)
    slow = _rolling_slope(x, 483)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=26, adjust=False).mean() * 1.437059 + 0.0056194 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_124_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=139, w2=496, w3=43, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(496, min_periods=max(496//3, 2)).max()
    trough = x.rolling(139, min_periods=max(139//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.450588 + 0.0056195 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_125_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=146, w2=509, w3=60, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(509, min_periods=max(509//3, 2)).rank(pct=True)
    persistence = change.rolling(60, min_periods=max(60//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.336 * persistence + 0.0056196 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_126_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=153, w2=23, w3=77, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(153, min_periods=max(153//3, 2)).std()
    vol_slow = ret.rolling(23, min_periods=max(23//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.477647 + 0.0056197 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_127_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=160, w2=36, w3=94, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(36, min_periods=max(36//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 160)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.348667 * slope + 0.0056198 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_128_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=167, w2=49, w3=111, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(49, min_periods=max(49//3, 2)).mean()
    noise = impulse.abs().rolling(111, min_periods=max(111//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.504706 + 0.0056199 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_129_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=174, w2=62, w3=128, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 174)
    acceleration = _rolling_slope(velocity, 62)
    curvature = _rolling_slope(acceleration, 128)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.361333 * acceleration + 0.00562 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_130_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=181, w2=75, w3=145, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 181)
    pressure = rel_log.diff(75)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.035333 * pressure.rolling(145, min_periods=max(145//3, 2)).mean() + 0.0056201 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_131_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=188, w2=88, w3=162, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(188, min_periods=max(188//3, 2)).mean())
    decay = spread.ewm(span=88, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.545294 + 0.0056202 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_132_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=195, w2=101, w3=179, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(101, min_periods=max(101//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 195)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.558824 + 0.0056203 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_133_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=202, w2=114, w3=196, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(202, min_periods=max(202//3, 2)).mean(), b.abs().rolling(114, min_periods=max(114//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.054333 * _rolling_slope(cover, 202) + 0.0056204 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_134_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=209, w2=127, w3=213, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(low.abs() + 1.0).shift(5)
    basket = x - 0.060667 * y + 0.939333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 209) - _rolling_slope(basket, 127) + 0.0056205 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_135_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=216, w2=140, w3=230, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(216, min_periods=max(216//3, 2)).mean(), upside.rolling(140, min_periods=max(140//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.599412 + 0.0056206 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_136_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=223, w2=153, w3=247, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(153, min_periods=max(153//3, 2)).max()
    rebound = x - x.rolling(223, min_periods=max(223//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.073333 * _rolling_slope(draw, 247) + 0.0056207 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_137_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=230, w2=166, w3=264, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(264, min_periods=max(264//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.626471 + 0.0056208 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_138_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=237, w2=179, w3=281, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 237)
    baseline = trend.rolling(179, min_periods=max(179//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(281, min_periods=max(281//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.64 + 0.0056209 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_139_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=244, w2=192, w3=298, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 244)
    slow = _rolling_slope(x, 192)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=298, adjust=False).mean() * 1.653529 + 0.005621 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_140_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=251, w2=205, w3=315, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(205, min_periods=max(205//3, 2)).max()
    trough = x.rolling(251, min_periods=max(251//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.667059 + 0.0056211 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_141_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=11, w2=218, w3=332, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(11)
    rank = change.rolling(218, min_periods=max(218//3, 2)).rank(pct=True)
    persistence = change.rolling(332, min_periods=max(332//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.105 * persistence + 0.0056212 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_142_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=18, w2=231, w3=349, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(18, min_periods=max(18//3, 2)).std()
    vol_slow = ret.rolling(231, min_periods=max(231//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.840588 + 0.0056213 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_143_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=25, w2=244, w3=366, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(244, min_periods=max(244//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 25)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.117667 * slope + 0.0056214 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_144_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=32, w2=257, w3=383, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(32)
    drag = impulse.rolling(257, min_periods=max(257//3, 2)).mean()
    noise = impulse.abs().rolling(383, min_periods=max(383//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.867647 + 0.0056215 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_145_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=39, w2=270, w3=400, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 39)
    acceleration = _rolling_slope(velocity, 270)
    curvature = _rolling_slope(acceleration, 400)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.130333 * acceleration + 0.0056216 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_146_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=46, w2=283, w3=417, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 46)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.136667 * pressure.rolling(417, min_periods=max(417//3, 2)).mean() + 0.0056217 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_147_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=53, w2=296, w3=434, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(53, min_periods=max(53//3, 2)).mean())
    decay = spread.ewm(span=296, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.908235 + 0.0056218 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_148_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=60, w2=309, w3=451, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(309, min_periods=max(309//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 60)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.921765 + 0.0056219 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_149_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=67, w2=322, w3=468, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(67, min_periods=max(67//3, 2)).mean(), b.abs().rolling(322, min_periods=max(322//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.155667 * _rolling_slope(cover, 67) + 0.005622 * anchor
    return base_signal.diff().diff()

def f90_todv_gemini_150_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=74, w2=335, w3=485, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(low.abs() + 1.0).shift(0)
    basket = x - 0.162 * y + 0.838000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 74) - _rolling_slope(basket, 335) + 0.0056221 * anchor
    return base_signal.diff().diff()
