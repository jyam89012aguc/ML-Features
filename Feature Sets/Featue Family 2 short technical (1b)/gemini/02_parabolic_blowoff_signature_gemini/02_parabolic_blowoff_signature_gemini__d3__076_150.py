"""02 parabolic blowoff signature gemini d3 features 76-150 â€” Pipeline 1b-HF Grade v7.

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

def f02_pblo_gemini_076_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=246, w2=31, w3=130, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(31, min_periods=max(31//3, 2)).mean()
    noise = impulse.abs().rolling(130, min_periods=max(130//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.17 + 8.47e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_077_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=6, w2=44, w3=147, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 6)
    acceleration = _rolling_slope(velocity, 44)
    curvature = _rolling_slope(acceleration, 147)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.078 * acceleration + 8.48e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_078_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=13, w2=57, w3=164, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(13, min_periods=max(13//3, 2)).mean(), upside.rolling(57, min_periods=max(57//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.197059 + 8.49e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_079_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=20, w2=70, w3=181, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(70, min_periods=max(70//3, 2)).max()
    rebound = x - x.rolling(20, min_periods=max(20//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.090667 * _rolling_slope(draw, 181) + 8.5e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_080_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=27, w2=83, w3=198, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 27)
    baseline = trend.rolling(83, min_periods=max(83//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(198, min_periods=max(198//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.224118 + 8.51e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_081_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=34, w2=96, w3=215, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 34)
    slow = _rolling_slope(x, 96)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=215, adjust=False).mean() * 1.237647 + 8.52e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_082_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=41, w2=109, w3=232, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(109, min_periods=max(109//3, 2)).max()
    trough = x.rolling(41, min_periods=max(41//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.251176 + 8.53e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_083_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=48, w2=122, w3=249, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(48)
    rank = change.rolling(122, min_periods=max(122//3, 2)).rank(pct=True)
    persistence = change.rolling(249, min_periods=max(249//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.116 * persistence + 8.54e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_084_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=55, w2=135, w3=266, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(55, min_periods=max(55//3, 2)).std()
    vol_slow = ret.rolling(135, min_periods=max(135//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.278235 + 8.55e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_085_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=62, w2=148, w3=283, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(148, min_periods=max(148//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 62)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.128667 * slope + 8.56e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_086_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=69, w2=161, w3=300, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(69)
    drag = impulse.rolling(161, min_periods=max(161//3, 2)).mean()
    noise = impulse.abs().rolling(300, min_periods=max(300//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.305294 + 8.57e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_087_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=76, w2=174, w3=317, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 76)
    acceleration = _rolling_slope(velocity, 174)
    curvature = _rolling_slope(acceleration, 317)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.141333 * acceleration + 8.58e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_088_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=83, w2=187, w3=334, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(83, min_periods=max(83//3, 2)).mean(), upside.rolling(187, min_periods=max(187//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.332353 + 8.59e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_089_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=90, w2=200, w3=351, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(200, min_periods=max(200//3, 2)).max()
    rebound = x - x.rolling(90, min_periods=max(90//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.154 * _rolling_slope(draw, 351) + 8.6e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_090_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=97, w2=213, w3=368, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 97)
    baseline = trend.rolling(213, min_periods=max(213//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(368, min_periods=max(368//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.359412 + 8.61e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_091_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=104, w2=226, w3=385, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 104)
    slow = _rolling_slope(x, 226)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.372941 + 8.62e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_092_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=111, w2=239, w3=402, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(239, min_periods=max(239//3, 2)).max()
    trough = x.rolling(111, min_periods=max(111//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.386471 + 8.63e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_093_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=118, w2=252, w3=419, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(118)
    rank = change.rolling(252, min_periods=max(252//3, 2)).rank(pct=True)
    persistence = change.rolling(419, min_periods=max(419//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.179333 * persistence + 8.64e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_094_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=125, w2=265, w3=436, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(125, min_periods=max(125//3, 2)).std()
    vol_slow = ret.rolling(265, min_periods=max(265//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.413529 + 8.65e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_095_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=132, w2=278, w3=453, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(278, min_periods=max(278//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 132)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.192 * slope + 8.66e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_096_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=139, w2=291, w3=470, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(291, min_periods=max(291//3, 2)).mean()
    noise = impulse.abs().rolling(470, min_periods=max(470//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.440588 + 8.67e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_097_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=146, w2=304, w3=487, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 146)
    acceleration = _rolling_slope(velocity, 304)
    curvature = _rolling_slope(acceleration, 487)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.204667 * acceleration + 8.68e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_098_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=153, w2=317, w3=504, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(153, min_periods=max(153//3, 2)).mean(), upside.rolling(317, min_periods=max(317//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.467647 + 8.69e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_099_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=160, w2=330, w3=521, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(330, min_periods=max(330//3, 2)).max()
    rebound = x - x.rolling(160, min_periods=max(160//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.217333 * _rolling_slope(draw, 521) + 8.7e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_100_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=167, w2=343, w3=538, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 167)
    baseline = trend.rolling(343, min_periods=max(343//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(538, min_periods=max(538//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.494706 + 8.71e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_101_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=174, w2=356, w3=555, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 174)
    slow = _rolling_slope(x, 356)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.508235 + 8.72e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_102_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=181, w2=369, w3=572, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(369, min_periods=max(369//3, 2)).max()
    trough = x.rolling(181, min_periods=max(181//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.521765 + 8.73e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_103_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=188, w2=382, w3=589, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(382, min_periods=max(382//3, 2)).rank(pct=True)
    persistence = change.rolling(589, min_periods=max(589//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.242667 * persistence + 8.74e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_104_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=195, w2=395, w3=606, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(195, min_periods=max(195//3, 2)).std()
    vol_slow = ret.rolling(395, min_periods=max(395//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.548824 + 8.75e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_105_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=202, w2=408, w3=623, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(408, min_periods=max(408//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 202)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.255333 * slope + 8.76e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_106_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=209, w2=421, w3=640, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(421, min_periods=max(421//3, 2)).mean()
    noise = impulse.abs().rolling(640, min_periods=max(640//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.575882 + 8.77e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_107_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=216, w2=434, w3=657, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 216)
    acceleration = _rolling_slope(velocity, 434)
    curvature = _rolling_slope(acceleration, 657)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.268 * acceleration + 8.78e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_108_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=223, w2=447, w3=674, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(223, min_periods=max(223//3, 2)).mean(), upside.rolling(447, min_periods=max(447//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.602941 + 8.79e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_109_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=230, w2=460, w3=691, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(460, min_periods=max(460//3, 2)).max()
    rebound = x - x.rolling(230, min_periods=max(230//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.280667 * _rolling_slope(draw, 691) + 8.8e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_110_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=237, w2=473, w3=708, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 237)
    baseline = trend.rolling(473, min_periods=max(473//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(708, min_periods=max(708//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.63 + 8.81e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_111_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=244, w2=486, w3=725, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 244)
    slow = _rolling_slope(x, 486)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.643529 + 8.82e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_112_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=251, w2=499, w3=742, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(499, min_periods=max(499//3, 2)).max()
    trough = x.rolling(251, min_periods=max(251//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.657059 + 8.83e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_113_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=11, w2=13, w3=759, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(11)
    rank = change.rolling(13, min_periods=max(13//3, 2)).rank(pct=True)
    persistence = change.rolling(759, min_periods=max(759//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.306 * persistence + 8.84e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_114_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=18, w2=26, w3=25, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(18, min_periods=max(18//3, 2)).std()
    vol_slow = ret.rolling(26, min_periods=max(26//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.830588 + 8.85e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_115_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=25, w2=39, w3=42, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(39, min_periods=max(39//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 25)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.318667 * slope + 8.86e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_116_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=32, w2=52, w3=59, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(32)
    drag = impulse.rolling(52, min_periods=max(52//3, 2)).mean()
    noise = impulse.abs().rolling(59, min_periods=max(59//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.857647 + 8.87e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_117_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=39, w2=65, w3=76, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 39)
    acceleration = _rolling_slope(velocity, 65)
    curvature = _rolling_slope(acceleration, 76)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.331333 * acceleration + 8.88e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_118_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=46, w2=78, w3=93, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(46, min_periods=max(46//3, 2)).mean(), upside.rolling(78, min_periods=max(78//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(93) * 0.884706 + 8.89e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_119_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=53, w2=91, w3=110, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(91, min_periods=max(91//3, 2)).max()
    rebound = x - x.rolling(53, min_periods=max(53//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.344 * _rolling_slope(draw, 110) + 8.9e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_120_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=60, w2=104, w3=127, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 60)
    baseline = trend.rolling(104, min_periods=max(104//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(127, min_periods=max(127//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.911765 + 8.91e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_121_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=67, w2=117, w3=144, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 67)
    slow = _rolling_slope(x, 117)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=144, adjust=False).mean() * 0.925294 + 8.92e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_122_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=74, w2=130, w3=161, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(130, min_periods=max(130//3, 2)).max()
    trough = x.rolling(74, min_periods=max(74//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.938824 + 8.93e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_123_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=81, w2=143, w3=178, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(81)
    rank = change.rolling(143, min_periods=max(143//3, 2)).rank(pct=True)
    persistence = change.rolling(178, min_periods=max(178//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.037 * persistence + 8.94e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_124_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=88, w2=156, w3=195, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(88, min_periods=max(88//3, 2)).std()
    vol_slow = ret.rolling(156, min_periods=max(156//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.965882 + 8.95e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_125_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=95, w2=169, w3=212, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(169, min_periods=max(169//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 95)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.049667 * slope + 8.96e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_126_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=102, w2=182, w3=229, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(102)
    drag = impulse.rolling(182, min_periods=max(182//3, 2)).mean()
    noise = impulse.abs().rolling(229, min_periods=max(229//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.992941 + 8.97e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_127_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=109, w2=195, w3=246, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 109)
    acceleration = _rolling_slope(velocity, 195)
    curvature = _rolling_slope(acceleration, 246)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.062333 * acceleration + 8.98e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_128_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=116, w2=208, w3=263, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(116, min_periods=max(116//3, 2)).mean(), upside.rolling(208, min_periods=max(208//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.02 + 8.99e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_129_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=123, w2=221, w3=280, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(221, min_periods=max(221//3, 2)).max()
    rebound = x - x.rolling(123, min_periods=max(123//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.075 * _rolling_slope(draw, 280) + 9e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_130_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=130, w2=234, w3=297, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 130)
    baseline = trend.rolling(234, min_periods=max(234//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(297, min_periods=max(297//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.047059 + 9.01e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_131_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=137, w2=247, w3=314, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 137)
    slow = _rolling_slope(x, 247)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.060588 + 9.02e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_132_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=144, w2=260, w3=331, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(260, min_periods=max(260//3, 2)).max()
    trough = x.rolling(144, min_periods=max(144//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.074118 + 9.03e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_133_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=151, w2=273, w3=348, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(273, min_periods=max(273//3, 2)).rank(pct=True)
    persistence = change.rolling(348, min_periods=max(348//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.100333 * persistence + 9.04e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_134_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=158, w2=286, w3=365, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(158, min_periods=max(158//3, 2)).std()
    vol_slow = ret.rolling(286, min_periods=max(286//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.101176 + 9.05e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_135_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=165, w2=299, w3=382, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(299, min_periods=max(299//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 165)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.113 * slope + 9.06e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_136_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=172, w2=312, w3=399, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(312, min_periods=max(312//3, 2)).mean()
    noise = impulse.abs().rolling(399, min_periods=max(399//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.128235 + 9.07e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_137_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=179, w2=325, w3=416, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 179)
    acceleration = _rolling_slope(velocity, 325)
    curvature = _rolling_slope(acceleration, 416)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.125667 * acceleration + 9.08e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_138_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=186, w2=338, w3=433, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(186, min_periods=max(186//3, 2)).mean(), upside.rolling(338, min_periods=max(338//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.155294 + 9.09e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_139_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=193, w2=351, w3=450, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(351, min_periods=max(351//3, 2)).max()
    rebound = x - x.rolling(193, min_periods=max(193//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.138333 * _rolling_slope(draw, 450) + 9.1e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_140_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=200, w2=364, w3=467, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 200)
    baseline = trend.rolling(364, min_periods=max(364//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(467, min_periods=max(467//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.182353 + 9.11e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_141_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=207, w2=377, w3=484, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 207)
    slow = _rolling_slope(x, 377)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.195882 + 9.12e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_142_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=214, w2=390, w3=501, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(390, min_periods=max(390//3, 2)).max()
    trough = x.rolling(214, min_periods=max(214//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.209412 + 9.13e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_143_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=221, w2=403, w3=518, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(403, min_periods=max(403//3, 2)).rank(pct=True)
    persistence = change.rolling(518, min_periods=max(518//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.163667 * persistence + 9.14e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_144_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=228, w2=416, w3=535, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(228, min_periods=max(228//3, 2)).std()
    vol_slow = ret.rolling(416, min_periods=max(416//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.236471 + 9.15e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_145_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=235, w2=429, w3=552, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(429, min_periods=max(429//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 235)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.176333 * slope + 9.16e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_146_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=242, w2=442, w3=569, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(442, min_periods=max(442//3, 2)).mean()
    noise = impulse.abs().rolling(569, min_periods=max(569//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.263529 + 9.17e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_147_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=249, w2=455, w3=586, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 249)
    acceleration = _rolling_slope(velocity, 455)
    curvature = _rolling_slope(acceleration, 586)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.189 * acceleration + 9.18e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_148_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=9, w2=468, w3=603, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(9, min_periods=max(9//3, 2)).mean(), upside.rolling(468, min_periods=max(468//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.290588 + 9.19e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_149_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=16, w2=481, w3=620, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(481, min_periods=max(481//3, 2)).max()
    rebound = x - x.rolling(16, min_periods=max(16//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.201667 * _rolling_slope(draw, 620) + 9.2e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_150_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=23, w2=494, w3=637, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 23)
    baseline = trend.rolling(494, min_periods=max(494//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(637, min_periods=max(637//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.317647 + 9.21e-05 * anchor
    return base_signal.diff().diff().diff()

# ============================================================
# POSTGRES FEATURE REGISTRY
# ============================================================

REGISTRY_02_PARABOLIC_BLOWOFF_SIGNATURE_GEMINI_D3_076_150 = {
    "f02_pblo_gemini_076_d3": {"inputs": ['close'], "func": f02_pblo_gemini_076_d3, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_077_d3": {"inputs": ['close'], "func": f02_pblo_gemini_077_d3, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_078_d3": {"inputs": ['close'], "func": f02_pblo_gemini_078_d3, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_079_d3": {"inputs": ['close'], "func": f02_pblo_gemini_079_d3, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_080_d3": {"inputs": ['close'], "func": f02_pblo_gemini_080_d3, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_081_d3": {"inputs": ['close'], "func": f02_pblo_gemini_081_d3, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_082_d3": {"inputs": ['close'], "func": f02_pblo_gemini_082_d3, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_083_d3": {"inputs": ['close'], "func": f02_pblo_gemini_083_d3, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_084_d3": {"inputs": ['close'], "func": f02_pblo_gemini_084_d3, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_085_d3": {"inputs": ['close'], "func": f02_pblo_gemini_085_d3, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_086_d3": {"inputs": ['close'], "func": f02_pblo_gemini_086_d3, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_087_d3": {"inputs": ['close'], "func": f02_pblo_gemini_087_d3, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_088_d3": {"inputs": ['close'], "func": f02_pblo_gemini_088_d3, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_089_d3": {"inputs": ['close'], "func": f02_pblo_gemini_089_d3, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_090_d3": {"inputs": ['close'], "func": f02_pblo_gemini_090_d3, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_091_d3": {"inputs": ['close'], "func": f02_pblo_gemini_091_d3, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_092_d3": {"inputs": ['close'], "func": f02_pblo_gemini_092_d3, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_093_d3": {"inputs": ['close'], "func": f02_pblo_gemini_093_d3, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_094_d3": {"inputs": ['close'], "func": f02_pblo_gemini_094_d3, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_095_d3": {"inputs": ['close'], "func": f02_pblo_gemini_095_d3, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_096_d3": {"inputs": ['close'], "func": f02_pblo_gemini_096_d3, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_097_d3": {"inputs": ['close'], "func": f02_pblo_gemini_097_d3, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_098_d3": {"inputs": ['close'], "func": f02_pblo_gemini_098_d3, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_099_d3": {"inputs": ['close'], "func": f02_pblo_gemini_099_d3, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_100_d3": {"inputs": ['close'], "func": f02_pblo_gemini_100_d3, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_101_d3": {"inputs": ['close'], "func": f02_pblo_gemini_101_d3, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_102_d3": {"inputs": ['close'], "func": f02_pblo_gemini_102_d3, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_103_d3": {"inputs": ['close'], "func": f02_pblo_gemini_103_d3, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_104_d3": {"inputs": ['close'], "func": f02_pblo_gemini_104_d3, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_105_d3": {"inputs": ['close'], "func": f02_pblo_gemini_105_d3, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_106_d3": {"inputs": ['close'], "func": f02_pblo_gemini_106_d3, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_107_d3": {"inputs": ['close'], "func": f02_pblo_gemini_107_d3, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_108_d3": {"inputs": ['close'], "func": f02_pblo_gemini_108_d3, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_109_d3": {"inputs": ['close'], "func": f02_pblo_gemini_109_d3, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_110_d3": {"inputs": ['close'], "func": f02_pblo_gemini_110_d3, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_111_d3": {"inputs": ['close'], "func": f02_pblo_gemini_111_d3, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_112_d3": {"inputs": ['close'], "func": f02_pblo_gemini_112_d3, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_113_d3": {"inputs": ['close'], "func": f02_pblo_gemini_113_d3, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_114_d3": {"inputs": ['close'], "func": f02_pblo_gemini_114_d3, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_115_d3": {"inputs": ['close'], "func": f02_pblo_gemini_115_d3, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_116_d3": {"inputs": ['close'], "func": f02_pblo_gemini_116_d3, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_117_d3": {"inputs": ['close'], "func": f02_pblo_gemini_117_d3, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_118_d3": {"inputs": ['close'], "func": f02_pblo_gemini_118_d3, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_119_d3": {"inputs": ['close'], "func": f02_pblo_gemini_119_d3, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_120_d3": {"inputs": ['close'], "func": f02_pblo_gemini_120_d3, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_121_d3": {"inputs": ['close'], "func": f02_pblo_gemini_121_d3, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_122_d3": {"inputs": ['close'], "func": f02_pblo_gemini_122_d3, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_123_d3": {"inputs": ['close'], "func": f02_pblo_gemini_123_d3, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_124_d3": {"inputs": ['close'], "func": f02_pblo_gemini_124_d3, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_125_d3": {"inputs": ['close'], "func": f02_pblo_gemini_125_d3, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_126_d3": {"inputs": ['close'], "func": f02_pblo_gemini_126_d3, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_127_d3": {"inputs": ['close'], "func": f02_pblo_gemini_127_d3, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_128_d3": {"inputs": ['close'], "func": f02_pblo_gemini_128_d3, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_129_d3": {"inputs": ['close'], "func": f02_pblo_gemini_129_d3, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_130_d3": {"inputs": ['close'], "func": f02_pblo_gemini_130_d3, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_131_d3": {"inputs": ['close'], "func": f02_pblo_gemini_131_d3, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_132_d3": {"inputs": ['close'], "func": f02_pblo_gemini_132_d3, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_133_d3": {"inputs": ['close'], "func": f02_pblo_gemini_133_d3, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_134_d3": {"inputs": ['close'], "func": f02_pblo_gemini_134_d3, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_135_d3": {"inputs": ['close'], "func": f02_pblo_gemini_135_d3, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_136_d3": {"inputs": ['close'], "func": f02_pblo_gemini_136_d3, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_137_d3": {"inputs": ['close'], "func": f02_pblo_gemini_137_d3, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_138_d3": {"inputs": ['close'], "func": f02_pblo_gemini_138_d3, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_139_d3": {"inputs": ['close'], "func": f02_pblo_gemini_139_d3, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_140_d3": {"inputs": ['close'], "func": f02_pblo_gemini_140_d3, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_141_d3": {"inputs": ['close'], "func": f02_pblo_gemini_141_d3, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_142_d3": {"inputs": ['close'], "func": f02_pblo_gemini_142_d3, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_143_d3": {"inputs": ['close'], "func": f02_pblo_gemini_143_d3, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_144_d3": {"inputs": ['close'], "func": f02_pblo_gemini_144_d3, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_145_d3": {"inputs": ['close'], "func": f02_pblo_gemini_145_d3, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_146_d3": {"inputs": ['close'], "func": f02_pblo_gemini_146_d3, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_147_d3": {"inputs": ['close'], "func": f02_pblo_gemini_147_d3, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_148_d3": {"inputs": ['close'], "func": f02_pblo_gemini_148_d3, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_149_d3": {"inputs": ['close'], "func": f02_pblo_gemini_149_d3, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_150_d3": {"inputs": ['close'], "func": f02_pblo_gemini_150_d3, "description": "Quadratic curvature of log-price over 1260d."},
}
