"""29 revenue deceleration acceleration d2 second derivative features 76-150 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Kinetics_Fundamental - Institutional-grade short-side signal.
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

def f29_rda_076_struct_v76_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=100, w2=100, w3=103, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(100)
    drag = impulse.rolling(100, min_periods=max(100//3, 2)).mean()
    noise = impulse.abs().rolling(103, min_periods=max(103//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.575 + 0.0017477 * anchor
    return base_signal.diff().diff()

def f29_rda_077_struct_v77_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=107, w2=111, w3=116, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 107)
    acceleration = _rolling_slope(velocity, 111)
    curvature = _rolling_slope(acceleration, 116)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3674 * acceleration + 0.0017478 * anchor
    return base_signal.diff().diff()

def f29_rda_078_struct_v78_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=114, w2=122, w3=129, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(114, min_periods=max(114//3, 2)).mean(), upside.rolling(122, min_periods=max(122//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.60375 + 0.0017479 * anchor
    return base_signal.diff().diff()

def f29_rda_079_struct_v79_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=121, w2=133, w3=142, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(133, min_periods=max(133//3, 2)).max()
    rebound = x - x.rolling(121, min_periods=max(121//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3826 * _rolling_slope(draw, 142) + 0.001748 * anchor
    return base_signal.diff().diff()

def f29_rda_080_struct_v80_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=128, w2=144, w3=155, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 128)
    baseline = trend.rolling(144, min_periods=max(144//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(155, min_periods=max(155//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.859375 + 0.0017481 * anchor
    return base_signal.diff().diff()

def f29_rda_081_struct_v81_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=135, w2=155, w3=168, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 135)
    slow = _rolling_slope(x, 155)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=168, adjust=False).mean() * 0.87375 + 0.0017482 * anchor
    return base_signal.diff().diff()

def f29_rda_082_struct_v82_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=142, w2=166, w3=181, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(166, min_periods=max(166//3, 2)).max()
    trough = x.rolling(142, min_periods=max(142//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.888125 + 0.0017483 * anchor
    return base_signal.diff().diff()

def f29_rda_083_struct_v83_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=149, w2=177, w3=194, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(177, min_periods=max(177//3, 2)).rank(pct=True)
    persistence = change.rolling(194, min_periods=max(194//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0366 * persistence + 0.0017484 * anchor
    return base_signal.diff().diff()

def f29_rda_084_struct_v84_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=156, w2=188, w3=207, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(156, min_periods=max(156//3, 2)).std()
    vol_slow = ret.rolling(188, min_periods=max(188//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.916875 + 0.0017485 * anchor
    return base_signal.diff().diff()

def f29_rda_085_struct_v85_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=163, w2=199, w3=220, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(199, min_periods=max(199//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 163)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0518 * slope + 0.0017486 * anchor
    return base_signal.diff().diff()

def f29_rda_086_struct_v86_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=170, w2=210, w3=233, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(210, min_periods=max(210//3, 2)).mean()
    noise = impulse.abs().rolling(233, min_periods=max(233//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.945625 + 0.0017487 * anchor
    return base_signal.diff().diff()

def f29_rda_087_struct_v87_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=177, w2=221, w3=246, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 177)
    acceleration = _rolling_slope(velocity, 221)
    curvature = _rolling_slope(acceleration, 246)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.067 * acceleration + 0.0017488 * anchor
    return base_signal.diff().diff()

def f29_rda_088_struct_v88_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=184, w2=232, w3=259, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(184, min_periods=max(184//3, 2)).mean(), upside.rolling(232, min_periods=max(232//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.974375 + 0.0017489 * anchor
    return base_signal.diff().diff()

def f29_rda_089_struct_v89_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=191, w2=243, w3=272, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(243, min_periods=max(243//3, 2)).max()
    rebound = x - x.rolling(191, min_periods=max(191//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0822 * _rolling_slope(draw, 272) + 0.001749 * anchor
    return base_signal.diff().diff()

def f29_rda_090_struct_v90_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=198, w2=254, w3=285, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 198)
    baseline = trend.rolling(254, min_periods=max(254//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(285, min_periods=max(285//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.003125 + 0.0017491 * anchor
    return base_signal.diff().diff()

def f29_rda_091_struct_v91_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=205, w2=265, w3=298, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 205)
    slow = _rolling_slope(x, 265)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=298, adjust=False).mean() * 1.0175 + 0.0017492 * anchor
    return base_signal.diff().diff()

def f29_rda_092_struct_v92_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=212, w2=276, w3=311, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(276, min_periods=max(276//3, 2)).max()
    trough = x.rolling(212, min_periods=max(212//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.031875 + 0.0017493 * anchor
    return base_signal.diff().diff()

def f29_rda_093_struct_v93_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=219, w2=287, w3=324, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(287, min_periods=max(287//3, 2)).rank(pct=True)
    persistence = change.rolling(324, min_periods=max(324//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1126 * persistence + 0.0017494 * anchor
    return base_signal.diff().diff()

def f29_rda_094_struct_v94_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=226, w2=298, w3=337, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(226, min_periods=max(226//3, 2)).std()
    vol_slow = ret.rolling(298, min_periods=max(298//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.060625 + 0.0017495 * anchor
    return base_signal.diff().diff()

def f29_rda_095_struct_v95_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=233, w2=309, w3=350, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(309, min_periods=max(309//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 233)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1278 * slope + 0.0017496 * anchor
    return base_signal.diff().diff()

def f29_rda_096_struct_v96_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=240, w2=320, w3=363, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(320, min_periods=max(320//3, 2)).mean()
    noise = impulse.abs().rolling(363, min_periods=max(363//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.089375 + 0.0017497 * anchor
    return base_signal.diff().diff()

def f29_rda_097_struct_v97_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=247, w2=331, w3=376, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 247)
    acceleration = _rolling_slope(velocity, 331)
    curvature = _rolling_slope(acceleration, 376)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.143 * acceleration + 0.0017498 * anchor
    return base_signal.diff().diff()

def f29_rda_098_struct_v98_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=254, w2=342, w3=389, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(254, min_periods=max(254//3, 2)).mean(), upside.rolling(342, min_periods=max(342//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.118125 + 0.0017499 * anchor
    return base_signal.diff().diff()

def f29_rda_099_struct_v99_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=10, w2=353, w3=402, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(353, min_periods=max(353//3, 2)).max()
    rebound = x - x.rolling(10, min_periods=max(10//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1582 * _rolling_slope(draw, 402) + 0.00175 * anchor
    return base_signal.diff().diff()

def f29_rda_100_struct_v100_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=17, w2=364, w3=415, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 17)
    baseline = trend.rolling(364, min_periods=max(364//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(415, min_periods=max(415//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.146875 + 0.0017501 * anchor
    return base_signal.diff().diff()

def f29_rda_101_struct_v101_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=24, w2=375, w3=428, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 24)
    slow = _rolling_slope(x, 375)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.16125 + 0.0017502 * anchor
    return base_signal.diff().diff()

def f29_rda_102_struct_v102_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=31, w2=386, w3=441, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(386, min_periods=max(386//3, 2)).max()
    trough = x.rolling(31, min_periods=max(31//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.175625 + 0.0017503 * anchor
    return base_signal.diff().diff()

def f29_rda_103_struct_v103_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=38, w2=397, w3=454, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(38)
    rank = change.rolling(397, min_periods=max(397//3, 2)).rank(pct=True)
    persistence = change.rolling(454, min_periods=max(454//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1886 * persistence + 0.0017504 * anchor
    return base_signal.diff().diff()

def f29_rda_104_struct_v104_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=45, w2=408, w3=467, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(45, min_periods=max(45//3, 2)).std()
    vol_slow = ret.rolling(408, min_periods=max(408//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.204375 + 0.0017505 * anchor
    return base_signal.diff().diff()

def f29_rda_105_struct_v105_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=52, w2=419, w3=480, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(419, min_periods=max(419//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 52)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2038 * slope + 0.0017506 * anchor
    return base_signal.diff().diff()

def f29_rda_106_struct_v106_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=59, w2=430, w3=493, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(59)
    drag = impulse.rolling(430, min_periods=max(430//3, 2)).mean()
    noise = impulse.abs().rolling(493, min_periods=max(493//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.233125 + 0.0017507 * anchor
    return base_signal.diff().diff()

def f29_rda_107_struct_v107_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=66, w2=441, w3=506, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 66)
    acceleration = _rolling_slope(velocity, 441)
    curvature = _rolling_slope(acceleration, 506)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.219 * acceleration + 0.0017508 * anchor
    return base_signal.diff().diff()

def f29_rda_108_struct_v108_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=73, w2=452, w3=519, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(73, min_periods=max(73//3, 2)).mean(), upside.rolling(452, min_periods=max(452//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.261875 + 0.0017509 * anchor
    return base_signal.diff().diff()

def f29_rda_109_struct_v109_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=80, w2=463, w3=532, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(463, min_periods=max(463//3, 2)).max()
    rebound = x - x.rolling(80, min_periods=max(80//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2342 * _rolling_slope(draw, 532) + 0.001751 * anchor
    return base_signal.diff().diff()

def f29_rda_110_struct_v110_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=87, w2=474, w3=545, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 87)
    baseline = trend.rolling(474, min_periods=max(474//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(545, min_periods=max(545//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.290625 + 0.0017511 * anchor
    return base_signal.diff().diff()

def f29_rda_111_struct_v111_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=94, w2=485, w3=558, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 94)
    slow = _rolling_slope(x, 485)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.305 + 0.0017512 * anchor
    return base_signal.diff().diff()

def f29_rda_112_struct_v112_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=101, w2=496, w3=571, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(496, min_periods=max(496//3, 2)).max()
    trough = x.rolling(101, min_periods=max(101//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.319375 + 0.0017513 * anchor
    return base_signal.diff().diff()

def f29_rda_113_struct_v113_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=108, w2=507, w3=584, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(108)
    rank = change.rolling(507, min_periods=max(507//3, 2)).rank(pct=True)
    persistence = change.rolling(584, min_periods=max(584//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2646 * persistence + 0.0017514 * anchor
    return base_signal.diff().diff()

def f29_rda_114_struct_v114_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=115, w2=15, w3=597, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(115, min_periods=max(115//3, 2)).std()
    vol_slow = ret.rolling(15, min_periods=max(15//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.348125 + 0.0017515 * anchor
    return base_signal.diff().diff()

def f29_rda_115_struct_v115_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=122, w2=26, w3=610, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(26, min_periods=max(26//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 122)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2798 * slope + 0.0017516 * anchor
    return base_signal.diff().diff()

def f29_rda_116_struct_v116_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=129, w2=37, w3=623, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(37, min_periods=max(37//3, 2)).mean()
    noise = impulse.abs().rolling(623, min_periods=max(623//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.376875 + 0.0017517 * anchor
    return base_signal.diff().diff()

def f29_rda_117_struct_v117_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=136, w2=48, w3=636, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 136)
    acceleration = _rolling_slope(velocity, 48)
    curvature = _rolling_slope(acceleration, 636)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.295 * acceleration + 0.0017518 * anchor
    return base_signal.diff().diff()

def f29_rda_118_struct_v118_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=143, w2=59, w3=649, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(143, min_periods=max(143//3, 2)).mean(), upside.rolling(59, min_periods=max(59//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.405625 + 0.0017519 * anchor
    return base_signal.diff().diff()

def f29_rda_119_struct_v119_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=150, w2=70, w3=662, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(70, min_periods=max(70//3, 2)).max()
    rebound = x - x.rolling(150, min_periods=max(150//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3102 * _rolling_slope(draw, 662) + 0.001752 * anchor
    return base_signal.diff().diff()

def f29_rda_120_struct_v120_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=157, w2=81, w3=675, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 157)
    baseline = trend.rolling(81, min_periods=max(81//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(675, min_periods=max(675//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.434375 + 0.0017521 * anchor
    return base_signal.diff().diff()

def f29_rda_121_struct_v121_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=164, w2=92, w3=688, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 164)
    slow = _rolling_slope(x, 92)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.44875 + 0.0017522 * anchor
    return base_signal.diff().diff()

def f29_rda_122_struct_v122_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=171, w2=103, w3=701, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(103, min_periods=max(103//3, 2)).max()
    trough = x.rolling(171, min_periods=max(171//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.463125 + 0.0017523 * anchor
    return base_signal.diff().diff()

def f29_rda_123_struct_v123_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=178, w2=114, w3=714, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(114, min_periods=max(114//3, 2)).rank(pct=True)
    persistence = change.rolling(714, min_periods=max(714//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3406 * persistence + 0.0017524 * anchor
    return base_signal.diff().diff()

def f29_rda_124_struct_v124_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=185, w2=125, w3=727, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(185, min_periods=max(185//3, 2)).std()
    vol_slow = ret.rolling(125, min_periods=max(125//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.491875 + 0.0017525 * anchor
    return base_signal.diff().diff()

def f29_rda_125_struct_v125_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=192, w2=136, w3=740, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(136, min_periods=max(136//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 192)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3558 * slope + 0.0017526 * anchor
    return base_signal.diff().diff()

def f29_rda_126_struct_v126_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=199, w2=147, w3=753, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(147, min_periods=max(147//3, 2)).mean()
    noise = impulse.abs().rolling(753, min_periods=max(753//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.520625 + 0.0017527 * anchor
    return base_signal.diff().diff()

def f29_rda_127_struct_v127_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=206, w2=158, w3=766, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 206)
    acceleration = _rolling_slope(velocity, 158)
    curvature = _rolling_slope(acceleration, 766)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.371 * acceleration + 0.0017528 * anchor
    return base_signal.diff().diff()

def f29_rda_128_struct_v128_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=213, w2=169, w3=22, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(213, min_periods=max(213//3, 2)).mean(), upside.rolling(169, min_periods=max(169//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(22) * 1.549375 + 0.0017529 * anchor
    return base_signal.diff().diff()

def f29_rda_129_struct_v129_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=220, w2=180, w3=35, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(180, min_periods=max(180//3, 2)).max()
    rebound = x - x.rolling(220, min_periods=max(220//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3862 * _rolling_slope(draw, 35) + 0.001753 * anchor
    return base_signal.diff().diff()

def f29_rda_130_struct_v130_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=227, w2=191, w3=48, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 227)
    baseline = trend.rolling(191, min_periods=max(191//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(48, min_periods=max(48//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.578125 + 0.0017531 * anchor
    return base_signal.diff().diff()

def f29_rda_131_struct_v131_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=234, w2=202, w3=61, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 234)
    slow = _rolling_slope(x, 202)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=61, adjust=False).mean() * 1.5925 + 0.0017532 * anchor
    return base_signal.diff().diff()

def f29_rda_132_struct_v132_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=241, w2=213, w3=74, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(213, min_periods=max(213//3, 2)).max()
    trough = x.rolling(241, min_periods=max(241//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.606875 + 0.0017533 * anchor
    return base_signal.diff().diff()

def f29_rda_133_struct_v133_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=248, w2=224, w3=87, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(224, min_periods=max(224//3, 2)).rank(pct=True)
    persistence = change.rolling(87, min_periods=max(87//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0402 * persistence + 0.0017534 * anchor
    return base_signal.diff().diff()

def f29_rda_134_struct_v134_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=255, w2=235, w3=100, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(255, min_periods=max(255//3, 2)).std()
    vol_slow = ret.rolling(235, min_periods=max(235//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.8625 + 0.0017535 * anchor
    return base_signal.diff().diff()

def f29_rda_135_struct_v135_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=11, w2=246, w3=113, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(246, min_periods=max(246//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 11)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0554 * slope + 0.0017536 * anchor
    return base_signal.diff().diff()

def f29_rda_136_struct_v136_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=18, w2=257, w3=126, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(18)
    drag = impulse.rolling(257, min_periods=max(257//3, 2)).mean()
    noise = impulse.abs().rolling(126, min_periods=max(126//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.89125 + 0.0017537 * anchor
    return base_signal.diff().diff()

def f29_rda_137_struct_v137_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=25, w2=268, w3=139, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 25)
    acceleration = _rolling_slope(velocity, 268)
    curvature = _rolling_slope(acceleration, 139)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0706 * acceleration + 0.0017538 * anchor
    return base_signal.diff().diff()

def f29_rda_138_struct_v138_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=32, w2=279, w3=152, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(32, min_periods=max(32//3, 2)).mean(), upside.rolling(279, min_periods=max(279//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.92 + 0.0017539 * anchor
    return base_signal.diff().diff()

def f29_rda_139_struct_v139_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=39, w2=290, w3=165, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(290, min_periods=max(290//3, 2)).max()
    rebound = x - x.rolling(39, min_periods=max(39//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0858 * _rolling_slope(draw, 165) + 0.001754 * anchor
    return base_signal.diff().diff()

def f29_rda_140_struct_v140_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=46, w2=301, w3=178, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 46)
    baseline = trend.rolling(301, min_periods=max(301//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(178, min_periods=max(178//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.94875 + 0.0017541 * anchor
    return base_signal.diff().diff()

def f29_rda_141_struct_v141_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=53, w2=312, w3=191, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 53)
    slow = _rolling_slope(x, 312)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=191, adjust=False).mean() * 0.963125 + 0.0017542 * anchor
    return base_signal.diff().diff()

def f29_rda_142_struct_v142_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=60, w2=323, w3=204, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(323, min_periods=max(323//3, 2)).max()
    trough = x.rolling(60, min_periods=max(60//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.9775 + 0.0017543 * anchor
    return base_signal.diff().diff()

def f29_rda_143_struct_v143_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=67, w2=334, w3=217, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(67)
    rank = change.rolling(334, min_periods=max(334//3, 2)).rank(pct=True)
    persistence = change.rolling(217, min_periods=max(217//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1162 * persistence + 0.0017544 * anchor
    return base_signal.diff().diff()

def f29_rda_144_struct_v144_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=74, w2=345, w3=230, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(74, min_periods=max(74//3, 2)).std()
    vol_slow = ret.rolling(345, min_periods=max(345//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.00625 + 0.0017545 * anchor
    return base_signal.diff().diff()

def f29_rda_145_struct_v145_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=81, w2=356, w3=243, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(356, min_periods=max(356//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 81)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1314 * slope + 0.0017546 * anchor
    return base_signal.diff().diff()

def f29_rda_146_struct_v146_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=88, w2=367, w3=256, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(88)
    drag = impulse.rolling(367, min_periods=max(367//3, 2)).mean()
    noise = impulse.abs().rolling(256, min_periods=max(256//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.035 + 0.0017547 * anchor
    return base_signal.diff().diff()

def f29_rda_147_struct_v147_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=95, w2=378, w3=269, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 95)
    acceleration = _rolling_slope(velocity, 378)
    curvature = _rolling_slope(acceleration, 269)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1466 * acceleration + 0.0017548 * anchor
    return base_signal.diff().diff()

def f29_rda_148_struct_v148_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=102, w2=389, w3=282, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(102, min_periods=max(102//3, 2)).mean(), upside.rolling(389, min_periods=max(389//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.06375 + 0.0017549 * anchor
    return base_signal.diff().diff()

def f29_rda_149_struct_v149_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=109, w2=400, w3=295, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(400, min_periods=max(400//3, 2)).max()
    rebound = x - x.rolling(109, min_periods=max(109//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1618 * _rolling_slope(draw, 295) + 0.001755 * anchor
    return base_signal.diff().diff()

def f29_rda_150_struct_v150_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=116, w2=411, w3=308, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 116)
    baseline = trend.rolling(411, min_periods=max(411//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(308, min_periods=max(308//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.0925 + 0.0017551 * anchor
    return base_signal.diff().diff()
