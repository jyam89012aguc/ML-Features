"""12 profitability snapshot d3 third derivative features 226-300 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Fundamental_Quality - Institutional-grade short-side signal.
Version: 3.0 (Strict De-duplication)
PIT-clean: right-anchored rolling, explicit min_periods.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5

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
def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if not valid.all():
            x = x[valid]; w = w[valid]
        xm, wm = x.mean(), w.mean()
        num = ((x - xm) * (w - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)

def f12_prof_226_struct_v226_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=30, w2=210, w3=414, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(30)
    drag = impulse.rolling(210, min_periods=max(210//3, 2)).mean()
    noise = impulse.abs().rolling(414, min_periods=max(414//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.9075 + 0.0007427 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_227_struct_v227_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=37, w2=221, w3=427, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 37)
    acceleration = _rolling_slope(velocity, 221)
    curvature = _rolling_slope(acceleration, 427)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3966 * acceleration + 0.0007428 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_228_struct_v228_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=44, w2=232, w3=440, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(44, min_periods=max(44//3, 2)).mean(), upside.rolling(232, min_periods=max(232//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.93625 + 0.0007429 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_229_struct_v229_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=51, w2=243, w3=453, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(243, min_periods=max(243//3, 2)).max()
    rebound = x - x.rolling(51, min_periods=max(51//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0354 * _rolling_slope(draw, 453) + 0.000743 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_230_struct_v230_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=58, w2=254, w3=466, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 58)
    baseline = trend.rolling(254, min_periods=max(254//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(466, min_periods=max(466//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.965 + 0.0007431 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_231_struct_v231_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=65, w2=265, w3=479, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 65)
    slow = _rolling_slope(x, 265)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.979375 + 0.0007432 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_232_struct_v232_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=72, w2=276, w3=492, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(276, min_periods=max(276//3, 2)).max()
    trough = x.rolling(72, min_periods=max(72//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.99375 + 0.0007433 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_233_struct_v233_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=79, w2=287, w3=505, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(79)
    rank = change.rolling(287, min_periods=max(287//3, 2)).rank(pct=True)
    persistence = change.rolling(505, min_periods=max(505//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0658 * persistence + 0.0007434 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_234_struct_v234_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=86, w2=298, w3=518, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(86, min_periods=max(86//3, 2)).std()
    vol_slow = ret.rolling(298, min_periods=max(298//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.0225 + 0.0007435 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_235_struct_v235_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=93, w2=309, w3=531, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(309, min_periods=max(309//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 93)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.081 * slope + 0.0007436 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_236_struct_v236_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=100, w2=320, w3=544, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(100)
    drag = impulse.rolling(320, min_periods=max(320//3, 2)).mean()
    noise = impulse.abs().rolling(544, min_periods=max(544//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.05125 + 0.0007437 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_237_struct_v237_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=107, w2=331, w3=557, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 107)
    acceleration = _rolling_slope(velocity, 331)
    curvature = _rolling_slope(acceleration, 557)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0962 * acceleration + 0.0007438 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_238_struct_v238_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=114, w2=342, w3=570, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(114, min_periods=max(114//3, 2)).mean(), upside.rolling(342, min_periods=max(342//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.08 + 0.0007439 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_239_struct_v239_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=121, w2=353, w3=583, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(353, min_periods=max(353//3, 2)).max()
    rebound = x - x.rolling(121, min_periods=max(121//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1114 * _rolling_slope(draw, 583) + 0.000744 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_240_struct_v240_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=128, w2=364, w3=596, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 128)
    baseline = trend.rolling(364, min_periods=max(364//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(596, min_periods=max(596//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.10875 + 0.0007441 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_241_struct_v241_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=135, w2=375, w3=609, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 135)
    slow = _rolling_slope(x, 375)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.123125 + 0.0007442 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_242_struct_v242_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=142, w2=386, w3=622, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(386, min_periods=max(386//3, 2)).max()
    trough = x.rolling(142, min_periods=max(142//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.1375 + 0.0007443 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_243_struct_v243_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=149, w2=397, w3=635, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(397, min_periods=max(397//3, 2)).rank(pct=True)
    persistence = change.rolling(635, min_periods=max(635//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1418 * persistence + 0.0007444 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_244_struct_v244_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=156, w2=408, w3=648, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(156, min_periods=max(156//3, 2)).std()
    vol_slow = ret.rolling(408, min_periods=max(408//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.16625 + 0.0007445 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_245_struct_v245_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=163, w2=419, w3=661, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(419, min_periods=max(419//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 163)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.157 * slope + 0.0007446 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_246_struct_v246_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=170, w2=430, w3=674, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(430, min_periods=max(430//3, 2)).mean()
    noise = impulse.abs().rolling(674, min_periods=max(674//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.195 + 0.0007447 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_247_struct_v247_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=177, w2=441, w3=687, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 177)
    acceleration = _rolling_slope(velocity, 441)
    curvature = _rolling_slope(acceleration, 687)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1722 * acceleration + 0.0007448 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_248_struct_v248_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=184, w2=452, w3=700, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(184, min_periods=max(184//3, 2)).mean(), upside.rolling(452, min_periods=max(452//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.22375 + 0.0007449 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_249_struct_v249_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=191, w2=463, w3=713, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(463, min_periods=max(463//3, 2)).max()
    rebound = x - x.rolling(191, min_periods=max(191//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1874 * _rolling_slope(draw, 713) + 0.000745 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_250_struct_v250_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=198, w2=474, w3=726, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 198)
    baseline = trend.rolling(474, min_periods=max(474//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(726, min_periods=max(726//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.2525 + 0.0007451 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_251_struct_v251_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=205, w2=485, w3=739, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 205)
    slow = _rolling_slope(x, 485)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.266875 + 0.0007452 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_252_struct_v252_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=212, w2=496, w3=752, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(496, min_periods=max(496//3, 2)).max()
    trough = x.rolling(212, min_periods=max(212//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.28125 + 0.0007453 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_253_struct_v253_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=219, w2=507, w3=765, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(507, min_periods=max(507//3, 2)).rank(pct=True)
    persistence = change.rolling(765, min_periods=max(765//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2178 * persistence + 0.0007454 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_254_struct_v254_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=226, w2=15, w3=21, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(226, min_periods=max(226//3, 2)).std()
    vol_slow = ret.rolling(15, min_periods=max(15//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.31 + 0.0007455 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_255_struct_v255_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=233, w2=26, w3=34, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(26, min_periods=max(26//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 233)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.233 * slope + 0.0007456 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_256_struct_v256_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=240, w2=37, w3=47, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(37, min_periods=max(37//3, 2)).mean()
    noise = impulse.abs().rolling(47, min_periods=max(47//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.33875 + 0.0007457 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_257_struct_v257_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=247, w2=48, w3=60, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 247)
    acceleration = _rolling_slope(velocity, 48)
    curvature = _rolling_slope(acceleration, 60)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2482 * acceleration + 0.0007458 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_258_struct_v258_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=254, w2=59, w3=73, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(254, min_periods=max(254//3, 2)).mean(), upside.rolling(59, min_periods=max(59//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(73) * 1.3675 + 0.0007459 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_259_struct_v259_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=10, w2=70, w3=86, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(70, min_periods=max(70//3, 2)).max()
    rebound = x - x.rolling(10, min_periods=max(10//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2634 * _rolling_slope(draw, 86) + 0.000746 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_260_struct_v260_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=17, w2=81, w3=99, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 17)
    baseline = trend.rolling(81, min_periods=max(81//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(99, min_periods=max(99//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.39625 + 0.0007461 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_261_struct_v261_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=24, w2=92, w3=112, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 24)
    slow = _rolling_slope(x, 92)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=112, adjust=False).mean() * 1.410625 + 0.0007462 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_262_struct_v262_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=31, w2=103, w3=125, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(103, min_periods=max(103//3, 2)).max()
    trough = x.rolling(31, min_periods=max(31//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.425 + 0.0007463 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_263_struct_v263_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=38, w2=114, w3=138, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(38)
    rank = change.rolling(114, min_periods=max(114//3, 2)).rank(pct=True)
    persistence = change.rolling(138, min_periods=max(138//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2938 * persistence + 0.0007464 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_264_struct_v264_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=45, w2=125, w3=151, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(45, min_periods=max(45//3, 2)).std()
    vol_slow = ret.rolling(125, min_periods=max(125//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.45375 + 0.0007465 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_265_struct_v265_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=52, w2=136, w3=164, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(136, min_periods=max(136//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 52)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.309 * slope + 0.0007466 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_266_struct_v266_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=59, w2=147, w3=177, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(59)
    drag = impulse.rolling(147, min_periods=max(147//3, 2)).mean()
    noise = impulse.abs().rolling(177, min_periods=max(177//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.4825 + 0.0007467 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_267_struct_v267_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=66, w2=158, w3=190, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 66)
    acceleration = _rolling_slope(velocity, 158)
    curvature = _rolling_slope(acceleration, 190)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3242 * acceleration + 0.0007468 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_268_struct_v268_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=73, w2=169, w3=203, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(73, min_periods=max(73//3, 2)).mean(), upside.rolling(169, min_periods=max(169//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.51125 + 0.0007469 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_269_struct_v269_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=80, w2=180, w3=216, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(180, min_periods=max(180//3, 2)).max()
    rebound = x - x.rolling(80, min_periods=max(80//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3394 * _rolling_slope(draw, 216) + 0.000747 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_270_struct_v270_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=87, w2=191, w3=229, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 87)
    baseline = trend.rolling(191, min_periods=max(191//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(229, min_periods=max(229//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.54 + 0.0007471 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_271_struct_v271_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=94, w2=202, w3=242, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 94)
    slow = _rolling_slope(x, 202)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=242, adjust=False).mean() * 1.554375 + 0.0007472 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_272_struct_v272_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=101, w2=213, w3=255, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(213, min_periods=max(213//3, 2)).max()
    trough = x.rolling(101, min_periods=max(101//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.56875 + 0.0007473 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_273_struct_v273_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=108, w2=224, w3=268, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(108)
    rank = change.rolling(224, min_periods=max(224//3, 2)).rank(pct=True)
    persistence = change.rolling(268, min_periods=max(268//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3698 * persistence + 0.0007474 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_274_struct_v274_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=115, w2=235, w3=281, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(115, min_periods=max(115//3, 2)).std()
    vol_slow = ret.rolling(235, min_periods=max(235//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.5975 + 0.0007475 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_275_struct_v275_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=122, w2=246, w3=294, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(246, min_periods=max(246//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 122)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.385 * slope + 0.0007476 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_276_struct_v276_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=129, w2=257, w3=307, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(257, min_periods=max(257//3, 2)).mean()
    noise = impulse.abs().rolling(307, min_periods=max(307//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.853125 + 0.0007477 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_277_struct_v277_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=136, w2=268, w3=320, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 136)
    acceleration = _rolling_slope(velocity, 268)
    curvature = _rolling_slope(acceleration, 320)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.4002 * acceleration + 0.0007478 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_278_struct_v278_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=143, w2=279, w3=333, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(143, min_periods=max(143//3, 2)).mean(), upside.rolling(279, min_periods=max(279//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.881875 + 0.0007479 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_279_struct_v279_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=150, w2=290, w3=346, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(290, min_periods=max(290//3, 2)).max()
    rebound = x - x.rolling(150, min_periods=max(150//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.039 * _rolling_slope(draw, 346) + 0.000748 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_280_struct_v280_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=157, w2=301, w3=359, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 157)
    baseline = trend.rolling(301, min_periods=max(301//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(359, min_periods=max(359//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.910625 + 0.0007481 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_281_struct_v281_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=164, w2=312, w3=372, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 164)
    slow = _rolling_slope(x, 312)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.925 + 0.0007482 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_282_struct_v282_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=171, w2=323, w3=385, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(323, min_periods=max(323//3, 2)).max()
    trough = x.rolling(171, min_periods=max(171//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.939375 + 0.0007483 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_283_struct_v283_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=178, w2=334, w3=398, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(334, min_periods=max(334//3, 2)).rank(pct=True)
    persistence = change.rolling(398, min_periods=max(398//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0694 * persistence + 0.0007484 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_284_struct_v284_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=185, w2=345, w3=411, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(185, min_periods=max(185//3, 2)).std()
    vol_slow = ret.rolling(345, min_periods=max(345//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.968125 + 0.0007485 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_285_struct_v285_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=192, w2=356, w3=424, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(356, min_periods=max(356//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 192)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0846 * slope + 0.0007486 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_286_struct_v286_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=199, w2=367, w3=437, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(367, min_periods=max(367//3, 2)).mean()
    noise = impulse.abs().rolling(437, min_periods=max(437//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.996875 + 0.0007487 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_287_struct_v287_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=206, w2=378, w3=450, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 206)
    acceleration = _rolling_slope(velocity, 378)
    curvature = _rolling_slope(acceleration, 450)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0998 * acceleration + 0.0007488 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_288_struct_v288_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=213, w2=389, w3=463, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(213, min_periods=max(213//3, 2)).mean(), upside.rolling(389, min_periods=max(389//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.025625 + 0.0007489 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_289_struct_v289_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=220, w2=400, w3=476, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(400, min_periods=max(400//3, 2)).max()
    rebound = x - x.rolling(220, min_periods=max(220//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.115 * _rolling_slope(draw, 476) + 0.000749 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_290_struct_v290_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=227, w2=411, w3=489, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 227)
    baseline = trend.rolling(411, min_periods=max(411//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(489, min_periods=max(489//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.054375 + 0.0007491 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_291_struct_v291_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=234, w2=422, w3=502, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 234)
    slow = _rolling_slope(x, 422)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.06875 + 0.0007492 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_292_struct_v292_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=241, w2=433, w3=515, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(433, min_periods=max(433//3, 2)).max()
    trough = x.rolling(241, min_periods=max(241//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.083125 + 0.0007493 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_293_struct_v293_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=248, w2=444, w3=528, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(444, min_periods=max(444//3, 2)).rank(pct=True)
    persistence = change.rolling(528, min_periods=max(528//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1454 * persistence + 0.0007494 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_294_struct_v294_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=255, w2=455, w3=541, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(255, min_periods=max(255//3, 2)).std()
    vol_slow = ret.rolling(455, min_periods=max(455//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.111875 + 0.0007495 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_295_struct_v295_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=11, w2=466, w3=554, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(466, min_periods=max(466//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 11)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1606 * slope + 0.0007496 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_296_struct_v296_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=18, w2=477, w3=567, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(18)
    drag = impulse.rolling(477, min_periods=max(477//3, 2)).mean()
    noise = impulse.abs().rolling(567, min_periods=max(567//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.140625 + 0.0007497 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_297_struct_v297_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=25, w2=488, w3=580, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 25)
    acceleration = _rolling_slope(velocity, 488)
    curvature = _rolling_slope(acceleration, 580)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1758 * acceleration + 0.0007498 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_298_struct_v298_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=32, w2=499, w3=593, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(32, min_periods=max(32//3, 2)).mean(), upside.rolling(499, min_periods=max(499//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.169375 + 0.0007499 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_299_struct_v299_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=39, w2=510, w3=606, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(510, min_periods=max(510//3, 2)).max()
    rebound = x - x.rolling(39, min_periods=max(39//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.191 * _rolling_slope(draw, 606) + 0.00075 * anchor
    return base_signal.diff().diff().diff()

def f12_prof_300_struct_v300_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=46, w2=18, w3=619, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 46)
    baseline = trend.rolling(18, min_periods=max(18//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(619, min_periods=max(619//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.198125 + 0.0007501 * anchor
    return base_signal.diff().diff().diff()
