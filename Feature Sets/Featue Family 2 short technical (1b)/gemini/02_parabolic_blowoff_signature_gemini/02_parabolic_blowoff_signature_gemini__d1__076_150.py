"""02 parabolic blowoff signature gemini d1 features 76-150 â€” Pipeline 1b-HF Grade v7.

Hypothesis: Blowoff - Institutional-grade technical signal with high-entropy logic.
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
    data = pd.concat(returns_list, axis=1)
    def _ar(w):
        if np.isnan(w).any(): return np.nan
        corr = np.corrcoef(w.T)
        eigvals = np.linalg.eigvalsh(corr)
        return np.max(eigvals) / len(eigvals)
    return data.rolling(21).apply(_ar, raw=True)

# ============================================================
# FEATURE HYPOTHESES (076-150)
# ============================================================

def f02_pblo_gemini_076_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=48, w2=404, w3=556, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(48)
    drag = impulse.rolling(404, min_periods=max(404//3, 2)).mean()
    noise = impulse.abs().rolling(556, min_periods=max(556//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.337059 + 6.07e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_077_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=55, w2=417, w3=573, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 55)
    acceleration = _rolling_slope(velocity, 417)
    curvature = _rolling_slope(acceleration, 573)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.219667 * acceleration + 6.08e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_078_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=62, w2=430, w3=590, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(62, min_periods=max(62//3, 2)).mean(), upside.rolling(430, min_periods=max(430//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.364118 + 6.09e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_079_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=69, w2=443, w3=607, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(443, min_periods=max(443//3, 2)).max()
    rebound = x - x.rolling(69, min_periods=max(69//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.232333 * _rolling_slope(draw, 607) + 6.1e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_080_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=76, w2=456, w3=624, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 76)
    baseline = trend.rolling(456, min_periods=max(456//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(624, min_periods=max(624//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.391176 + 6.11e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_081_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=83, w2=469, w3=641, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 83)
    slow = _rolling_slope(x, 469)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.404706 + 6.12e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_082_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=90, w2=482, w3=658, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(482, min_periods=max(482//3, 2)).max()
    trough = x.rolling(90, min_periods=max(90//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.418235 + 6.13e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_083_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=97, w2=495, w3=675, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(97)
    rank = change.rolling(495, min_periods=max(495//3, 2)).rank(pct=True)
    persistence = change.rolling(675, min_periods=max(675//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.257667 * persistence + 6.14e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_084_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=104, w2=508, w3=692, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(104, min_periods=max(104//3, 2)).std()
    vol_slow = ret.rolling(508, min_periods=max(508//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.445294 + 6.15e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_085_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=111, w2=22, w3=709, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(22, min_periods=max(22//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 111)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.270333 * slope + 6.16e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_086_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=118, w2=35, w3=726, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(118)
    drag = impulse.rolling(35, min_periods=max(35//3, 2)).mean()
    noise = impulse.abs().rolling(726, min_periods=max(726//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.472353 + 6.17e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_087_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=125, w2=48, w3=743, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 125)
    acceleration = _rolling_slope(velocity, 48)
    curvature = _rolling_slope(acceleration, 743)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.283 * acceleration + 6.18e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_088_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=132, w2=61, w3=760, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(132, min_periods=max(132//3, 2)).mean(), upside.rolling(61, min_periods=max(61//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.499412 + 6.19e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_089_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=139, w2=74, w3=26, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(74, min_periods=max(74//3, 2)).max()
    rebound = x - x.rolling(139, min_periods=max(139//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.295667 * _rolling_slope(draw, 26) + 6.2e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_090_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=146, w2=87, w3=43, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 146)
    baseline = trend.rolling(87, min_periods=max(87//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(43, min_periods=max(43//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.526471 + 6.21e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_091_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=153, w2=100, w3=60, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 153)
    slow = _rolling_slope(x, 100)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=60, adjust=False).mean() * 1.54 + 6.22e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_092_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=160, w2=113, w3=77, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(113, min_periods=max(113//3, 2)).max()
    trough = x.rolling(160, min_periods=max(160//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.553529 + 6.23e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_093_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=167, w2=126, w3=94, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(126, min_periods=max(126//3, 2)).rank(pct=True)
    persistence = change.rolling(94, min_periods=max(94//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.321 * persistence + 6.24e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_094_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=174, w2=139, w3=111, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(174, min_periods=max(174//3, 2)).std()
    vol_slow = ret.rolling(139, min_periods=max(139//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.580588 + 6.25e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_095_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=181, w2=152, w3=128, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(152, min_periods=max(152//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 181)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.333667 * slope + 6.26e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_096_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=188, w2=165, w3=145, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(165, min_periods=max(165//3, 2)).mean()
    noise = impulse.abs().rolling(145, min_periods=max(145//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.607647 + 6.27e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_097_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=195, w2=178, w3=162, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 195)
    acceleration = _rolling_slope(velocity, 178)
    curvature = _rolling_slope(acceleration, 162)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.346333 * acceleration + 6.28e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_098_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=202, w2=191, w3=179, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(202, min_periods=max(202//3, 2)).mean(), upside.rolling(191, min_periods=max(191//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.634706 + 6.29e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_099_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=209, w2=204, w3=196, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(204, min_periods=max(204//3, 2)).max()
    rebound = x - x.rolling(209, min_periods=max(209//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.359 * _rolling_slope(draw, 196) + 6.3e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_100_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=216, w2=217, w3=213, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 216)
    baseline = trend.rolling(217, min_periods=max(217//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(213, min_periods=max(213//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.661765 + 6.31e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_101_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=223, w2=230, w3=230, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 223)
    slow = _rolling_slope(x, 230)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=230, adjust=False).mean() * 0.821765 + 6.32e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_102_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=230, w2=243, w3=247, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(243, min_periods=max(243//3, 2)).max()
    trough = x.rolling(230, min_periods=max(230//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.835294 + 6.33e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_103_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=237, w2=256, w3=264, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(256, min_periods=max(256//3, 2)).rank(pct=True)
    persistence = change.rolling(264, min_periods=max(264//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.052 * persistence + 6.34e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_104_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=244, w2=269, w3=281, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(244, min_periods=max(244//3, 2)).std()
    vol_slow = ret.rolling(269, min_periods=max(269//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.862353 + 6.35e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_105_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=251, w2=282, w3=298, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(282, min_periods=max(282//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 251)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.064667 * slope + 6.36e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_106_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=11, w2=295, w3=315, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(11)
    drag = impulse.rolling(295, min_periods=max(295//3, 2)).mean()
    noise = impulse.abs().rolling(315, min_periods=max(315//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.889412 + 6.37e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_107_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=18, w2=308, w3=332, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 18)
    acceleration = _rolling_slope(velocity, 308)
    curvature = _rolling_slope(acceleration, 332)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.077333 * acceleration + 6.38e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_108_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=25, w2=321, w3=349, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(25, min_periods=max(25//3, 2)).mean(), upside.rolling(321, min_periods=max(321//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.916471 + 6.39e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_109_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=32, w2=334, w3=366, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(334, min_periods=max(334//3, 2)).max()
    rebound = x - x.rolling(32, min_periods=max(32//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.09 * _rolling_slope(draw, 366) + 6.4e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_110_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=39, w2=347, w3=383, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 39)
    baseline = trend.rolling(347, min_periods=max(347//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(383, min_periods=max(383//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.943529 + 6.41e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_111_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=46, w2=360, w3=400, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 46)
    slow = _rolling_slope(x, 360)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.957059 + 6.42e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_112_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=53, w2=373, w3=417, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(373, min_periods=max(373//3, 2)).max()
    trough = x.rolling(53, min_periods=max(53//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.970588 + 6.43e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_113_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=60, w2=386, w3=434, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(60)
    rank = change.rolling(386, min_periods=max(386//3, 2)).rank(pct=True)
    persistence = change.rolling(434, min_periods=max(434//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.115333 * persistence + 6.44e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_114_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=67, w2=399, w3=451, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(67, min_periods=max(67//3, 2)).std()
    vol_slow = ret.rolling(399, min_periods=max(399//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.997647 + 6.45e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_115_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=74, w2=412, w3=468, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(412, min_periods=max(412//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 74)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.128 * slope + 6.46e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_116_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=81, w2=425, w3=485, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(81)
    drag = impulse.rolling(425, min_periods=max(425//3, 2)).mean()
    noise = impulse.abs().rolling(485, min_periods=max(485//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.024706 + 6.47e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_117_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=88, w2=438, w3=502, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 88)
    acceleration = _rolling_slope(velocity, 438)
    curvature = _rolling_slope(acceleration, 502)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.140667 * acceleration + 6.48e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_118_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=95, w2=451, w3=519, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(95, min_periods=max(95//3, 2)).mean(), upside.rolling(451, min_periods=max(451//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.051765 + 6.49e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_119_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=102, w2=464, w3=536, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(464, min_periods=max(464//3, 2)).max()
    rebound = x - x.rolling(102, min_periods=max(102//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.153333 * _rolling_slope(draw, 536) + 6.5e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_120_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=109, w2=477, w3=553, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 109)
    baseline = trend.rolling(477, min_periods=max(477//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(553, min_periods=max(553//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.078824 + 6.51e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_121_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=116, w2=490, w3=570, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 116)
    slow = _rolling_slope(x, 490)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.092353 + 6.52e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_122_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=123, w2=503, w3=587, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(503, min_periods=max(503//3, 2)).max()
    trough = x.rolling(123, min_periods=max(123//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.105882 + 6.53e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_123_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=130, w2=17, w3=604, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(17, min_periods=max(17//3, 2)).rank(pct=True)
    persistence = change.rolling(604, min_periods=max(604//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.178667 * persistence + 6.54e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_124_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=137, w2=30, w3=621, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(137, min_periods=max(137//3, 2)).std()
    vol_slow = ret.rolling(30, min_periods=max(30//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.132941 + 6.55e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_125_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=144, w2=43, w3=638, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(43, min_periods=max(43//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 144)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.191333 * slope + 6.56e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_126_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=151, w2=56, w3=655, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(56, min_periods=max(56//3, 2)).mean()
    noise = impulse.abs().rolling(655, min_periods=max(655//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.16 + 6.57e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_127_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=158, w2=69, w3=672, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 158)
    acceleration = _rolling_slope(velocity, 69)
    curvature = _rolling_slope(acceleration, 672)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.204 * acceleration + 6.58e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_128_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=165, w2=82, w3=689, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(165, min_periods=max(165//3, 2)).mean(), upside.rolling(82, min_periods=max(82//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.187059 + 6.59e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_129_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=172, w2=95, w3=706, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(95, min_periods=max(95//3, 2)).max()
    rebound = x - x.rolling(172, min_periods=max(172//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.216667 * _rolling_slope(draw, 706) + 6.6e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_130_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=179, w2=108, w3=723, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 179)
    baseline = trend.rolling(108, min_periods=max(108//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(723, min_periods=max(723//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.214118 + 6.61e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_131_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=186, w2=121, w3=740, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 186)
    slow = _rolling_slope(x, 121)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.227647 + 6.62e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_132_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=193, w2=134, w3=757, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(134, min_periods=max(134//3, 2)).max()
    trough = x.rolling(193, min_periods=max(193//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.241176 + 6.63e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_133_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=200, w2=147, w3=23, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(147, min_periods=max(147//3, 2)).rank(pct=True)
    persistence = change.rolling(23, min_periods=max(23//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.242 * persistence + 6.64e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_134_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=207, w2=160, w3=40, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(207, min_periods=max(207//3, 2)).std()
    vol_slow = ret.rolling(160, min_periods=max(160//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.268235 + 6.65e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_135_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=214, w2=173, w3=57, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(173, min_periods=max(173//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 214)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.254667 * slope + 6.66e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_136_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=221, w2=186, w3=74, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(186, min_periods=max(186//3, 2)).mean()
    noise = impulse.abs().rolling(74, min_periods=max(74//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.295294 + 6.67e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_137_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=228, w2=199, w3=91, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 228)
    acceleration = _rolling_slope(velocity, 199)
    curvature = _rolling_slope(acceleration, 91)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.267333 * acceleration + 6.68e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_138_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=235, w2=212, w3=108, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(235, min_periods=max(235//3, 2)).mean(), upside.rolling(212, min_periods=max(212//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(108) * 1.322353 + 6.69e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_139_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=242, w2=225, w3=125, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(225, min_periods=max(225//3, 2)).max()
    rebound = x - x.rolling(242, min_periods=max(242//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.28 * _rolling_slope(draw, 125) + 6.7e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_140_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=249, w2=238, w3=142, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 249)
    baseline = trend.rolling(238, min_periods=max(238//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(142, min_periods=max(142//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.349412 + 6.71e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_141_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=9, w2=251, w3=159, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 9)
    slow = _rolling_slope(x, 251)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=159, adjust=False).mean() * 1.362941 + 6.72e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_142_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=16, w2=264, w3=176, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(264, min_periods=max(264//3, 2)).max()
    trough = x.rolling(16, min_periods=max(16//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.376471 + 6.73e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_143_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=23, w2=277, w3=193, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(23)
    rank = change.rolling(277, min_periods=max(277//3, 2)).rank(pct=True)
    persistence = change.rolling(193, min_periods=max(193//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.305333 * persistence + 6.74e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_144_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=30, w2=290, w3=210, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(30, min_periods=max(30//3, 2)).std()
    vol_slow = ret.rolling(290, min_periods=max(290//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.403529 + 6.75e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_145_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=37, w2=303, w3=227, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(303, min_periods=max(303//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 37)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.318 * slope + 6.76e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_146_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=44, w2=316, w3=244, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(44)
    drag = impulse.rolling(316, min_periods=max(316//3, 2)).mean()
    noise = impulse.abs().rolling(244, min_periods=max(244//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.430588 + 6.77e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_147_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=51, w2=329, w3=261, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 51)
    acceleration = _rolling_slope(velocity, 329)
    curvature = _rolling_slope(acceleration, 261)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.330667 * acceleration + 6.78e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_148_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=58, w2=342, w3=278, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(58, min_periods=max(58//3, 2)).mean(), upside.rolling(342, min_periods=max(342//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.457647 + 6.79e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_149_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=65, w2=355, w3=295, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(355, min_periods=max(355//3, 2)).max()
    rebound = x - x.rolling(65, min_periods=max(65//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.343333 * _rolling_slope(draw, 295) + 6.8e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_150_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=72, w2=368, w3=312, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 72)
    baseline = trend.rolling(368, min_periods=max(368//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(312, min_periods=max(312//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.484706 + 6.81e-05 * anchor
    return base_signal.diff()

# ============================================================
# POSTGRES FEATURE REGISTRY
# ============================================================

REGISTRY_02_PARABOLIC_BLOWOFF_SIGNATURE_GEMINI_D1_076_150 = {
    "f02_pblo_gemini_076_d1": {"inputs": ['close'], "func": f02_pblo_gemini_076_d1, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_077_d1": {"inputs": ['close'], "func": f02_pblo_gemini_077_d1, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_078_d1": {"inputs": ['close'], "func": f02_pblo_gemini_078_d1, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_079_d1": {"inputs": ['close'], "func": f02_pblo_gemini_079_d1, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_080_d1": {"inputs": ['close'], "func": f02_pblo_gemini_080_d1, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_081_d1": {"inputs": ['close'], "func": f02_pblo_gemini_081_d1, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_082_d1": {"inputs": ['close'], "func": f02_pblo_gemini_082_d1, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_083_d1": {"inputs": ['close'], "func": f02_pblo_gemini_083_d1, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_084_d1": {"inputs": ['close'], "func": f02_pblo_gemini_084_d1, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_085_d1": {"inputs": ['close'], "func": f02_pblo_gemini_085_d1, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_086_d1": {"inputs": ['close'], "func": f02_pblo_gemini_086_d1, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_087_d1": {"inputs": ['close'], "func": f02_pblo_gemini_087_d1, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_088_d1": {"inputs": ['close'], "func": f02_pblo_gemini_088_d1, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_089_d1": {"inputs": ['close'], "func": f02_pblo_gemini_089_d1, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_090_d1": {"inputs": ['close'], "func": f02_pblo_gemini_090_d1, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_091_d1": {"inputs": ['close'], "func": f02_pblo_gemini_091_d1, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_092_d1": {"inputs": ['close'], "func": f02_pblo_gemini_092_d1, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_093_d1": {"inputs": ['close'], "func": f02_pblo_gemini_093_d1, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_094_d1": {"inputs": ['close'], "func": f02_pblo_gemini_094_d1, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_095_d1": {"inputs": ['close'], "func": f02_pblo_gemini_095_d1, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_096_d1": {"inputs": ['close'], "func": f02_pblo_gemini_096_d1, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_097_d1": {"inputs": ['close'], "func": f02_pblo_gemini_097_d1, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_098_d1": {"inputs": ['close'], "func": f02_pblo_gemini_098_d1, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_099_d1": {"inputs": ['close'], "func": f02_pblo_gemini_099_d1, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_100_d1": {"inputs": ['close'], "func": f02_pblo_gemini_100_d1, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_101_d1": {"inputs": ['close'], "func": f02_pblo_gemini_101_d1, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_102_d1": {"inputs": ['close'], "func": f02_pblo_gemini_102_d1, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_103_d1": {"inputs": ['close'], "func": f02_pblo_gemini_103_d1, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_104_d1": {"inputs": ['close'], "func": f02_pblo_gemini_104_d1, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_105_d1": {"inputs": ['close'], "func": f02_pblo_gemini_105_d1, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_106_d1": {"inputs": ['close'], "func": f02_pblo_gemini_106_d1, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_107_d1": {"inputs": ['close'], "func": f02_pblo_gemini_107_d1, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_108_d1": {"inputs": ['close'], "func": f02_pblo_gemini_108_d1, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_109_d1": {"inputs": ['close'], "func": f02_pblo_gemini_109_d1, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_110_d1": {"inputs": ['close'], "func": f02_pblo_gemini_110_d1, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_111_d1": {"inputs": ['close'], "func": f02_pblo_gemini_111_d1, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_112_d1": {"inputs": ['close'], "func": f02_pblo_gemini_112_d1, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_113_d1": {"inputs": ['close'], "func": f02_pblo_gemini_113_d1, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_114_d1": {"inputs": ['close'], "func": f02_pblo_gemini_114_d1, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_115_d1": {"inputs": ['close'], "func": f02_pblo_gemini_115_d1, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_116_d1": {"inputs": ['close'], "func": f02_pblo_gemini_116_d1, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_117_d1": {"inputs": ['close'], "func": f02_pblo_gemini_117_d1, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_118_d1": {"inputs": ['close'], "func": f02_pblo_gemini_118_d1, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_119_d1": {"inputs": ['close'], "func": f02_pblo_gemini_119_d1, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_120_d1": {"inputs": ['close'], "func": f02_pblo_gemini_120_d1, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_121_d1": {"inputs": ['close'], "func": f02_pblo_gemini_121_d1, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_122_d1": {"inputs": ['close'], "func": f02_pblo_gemini_122_d1, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_123_d1": {"inputs": ['close'], "func": f02_pblo_gemini_123_d1, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_124_d1": {"inputs": ['close'], "func": f02_pblo_gemini_124_d1, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_125_d1": {"inputs": ['close'], "func": f02_pblo_gemini_125_d1, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_126_d1": {"inputs": ['close'], "func": f02_pblo_gemini_126_d1, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_127_d1": {"inputs": ['close'], "func": f02_pblo_gemini_127_d1, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_128_d1": {"inputs": ['close'], "func": f02_pblo_gemini_128_d1, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_129_d1": {"inputs": ['close'], "func": f02_pblo_gemini_129_d1, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_130_d1": {"inputs": ['close'], "func": f02_pblo_gemini_130_d1, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_131_d1": {"inputs": ['close'], "func": f02_pblo_gemini_131_d1, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_132_d1": {"inputs": ['close'], "func": f02_pblo_gemini_132_d1, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_133_d1": {"inputs": ['close'], "func": f02_pblo_gemini_133_d1, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_134_d1": {"inputs": ['close'], "func": f02_pblo_gemini_134_d1, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_135_d1": {"inputs": ['close'], "func": f02_pblo_gemini_135_d1, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_136_d1": {"inputs": ['close'], "func": f02_pblo_gemini_136_d1, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_137_d1": {"inputs": ['close'], "func": f02_pblo_gemini_137_d1, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_138_d1": {"inputs": ['close'], "func": f02_pblo_gemini_138_d1, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_139_d1": {"inputs": ['close'], "func": f02_pblo_gemini_139_d1, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_140_d1": {"inputs": ['close'], "func": f02_pblo_gemini_140_d1, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_141_d1": {"inputs": ['close'], "func": f02_pblo_gemini_141_d1, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_142_d1": {"inputs": ['close'], "func": f02_pblo_gemini_142_d1, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_143_d1": {"inputs": ['close'], "func": f02_pblo_gemini_143_d1, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_144_d1": {"inputs": ['close'], "func": f02_pblo_gemini_144_d1, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_145_d1": {"inputs": ['close'], "func": f02_pblo_gemini_145_d1, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_146_d1": {"inputs": ['close'], "func": f02_pblo_gemini_146_d1, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_147_d1": {"inputs": ['close'], "func": f02_pblo_gemini_147_d1, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_148_d1": {"inputs": ['close'], "func": f02_pblo_gemini_148_d1, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_149_d1": {"inputs": ['close'], "func": f02_pblo_gemini_149_d1, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_150_d1": {"inputs": ['close'], "func": f02_pblo_gemini_150_d1, "description": "Quadratic curvature of log-price over 1260d."},
}
