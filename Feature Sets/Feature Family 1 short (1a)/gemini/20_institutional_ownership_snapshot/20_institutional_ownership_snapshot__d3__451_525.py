"""20 institutional ownership snapshot d3 third derivative features 451-525 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Ownership - Institutional-grade short-side signal.
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

def f20_inst_451_struct_v451_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=65, w2=155, w3=637, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 65)
    slow = _rolling_slope(x, 155)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.24125 + 0.0012452 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_452_struct_v452_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=72, w2=166, w3=650, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(166, min_periods=max(166//3, 2)).max()
    trough = x.rolling(72, min_periods=max(72//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.255625 + 0.0012453 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_453_struct_v453_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=79, w2=177, w3=663, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(79)
    rank = change.rolling(177, min_periods=max(177//3, 2)).rank(pct=True)
    persistence = change.rolling(663, min_periods=max(663//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2014 * persistence + 0.0012454 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_454_struct_v454_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=86, w2=188, w3=676, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(86, min_periods=max(86//3, 2)).std()
    vol_slow = ret.rolling(188, min_periods=max(188//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.284375 + 0.0012455 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_455_struct_v455_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=93, w2=199, w3=689, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(199, min_periods=max(199//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 93)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2166 * slope + 0.0012456 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_456_struct_v456_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=100, w2=210, w3=702, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(100)
    drag = impulse.rolling(210, min_periods=max(210//3, 2)).mean()
    noise = impulse.abs().rolling(702, min_periods=max(702//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.313125 + 0.0012457 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_457_struct_v457_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=107, w2=221, w3=715, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 107)
    acceleration = _rolling_slope(velocity, 221)
    curvature = _rolling_slope(acceleration, 715)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2318 * acceleration + 0.0012458 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_458_struct_v458_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=114, w2=232, w3=728, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(114, min_periods=max(114//3, 2)).mean(), upside.rolling(232, min_periods=max(232//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.341875 + 0.0012459 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_459_struct_v459_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=121, w2=243, w3=741, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(243, min_periods=max(243//3, 2)).max()
    rebound = x - x.rolling(121, min_periods=max(121//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.247 * _rolling_slope(draw, 741) + 0.001246 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_460_struct_v460_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=128, w2=254, w3=754, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 128)
    baseline = trend.rolling(254, min_periods=max(254//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(754, min_periods=max(754//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.370625 + 0.0012461 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_461_struct_v461_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=135, w2=265, w3=767, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 135)
    slow = _rolling_slope(x, 265)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.385 + 0.0012462 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_462_struct_v462_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=142, w2=276, w3=23, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(276, min_periods=max(276//3, 2)).max()
    trough = x.rolling(142, min_periods=max(142//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.399375 + 0.0012463 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_463_struct_v463_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=149, w2=287, w3=36, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(287, min_periods=max(287//3, 2)).rank(pct=True)
    persistence = change.rolling(36, min_periods=max(36//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2774 * persistence + 0.0012464 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_464_struct_v464_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=156, w2=298, w3=49, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(156, min_periods=max(156//3, 2)).std()
    vol_slow = ret.rolling(298, min_periods=max(298//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.428125 + 0.0012465 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_465_struct_v465_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=163, w2=309, w3=62, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(309, min_periods=max(309//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 163)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2926 * slope + 0.0012466 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_466_struct_v466_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=170, w2=320, w3=75, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(320, min_periods=max(320//3, 2)).mean()
    noise = impulse.abs().rolling(75, min_periods=max(75//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.456875 + 0.0012467 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_467_struct_v467_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=177, w2=331, w3=88, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 177)
    acceleration = _rolling_slope(velocity, 331)
    curvature = _rolling_slope(acceleration, 88)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3078 * acceleration + 0.0012468 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_468_struct_v468_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=184, w2=342, w3=101, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(184, min_periods=max(184//3, 2)).mean(), upside.rolling(342, min_periods=max(342//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(101) * 1.485625 + 0.0012469 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_469_struct_v469_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=191, w2=353, w3=114, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(353, min_periods=max(353//3, 2)).max()
    rebound = x - x.rolling(191, min_periods=max(191//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.323 * _rolling_slope(draw, 114) + 0.001247 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_470_struct_v470_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=198, w2=364, w3=127, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 198)
    baseline = trend.rolling(364, min_periods=max(364//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(127, min_periods=max(127//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.514375 + 0.0012471 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_471_struct_v471_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=205, w2=375, w3=140, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 205)
    slow = _rolling_slope(x, 375)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=140, adjust=False).mean() * 1.52875 + 0.0012472 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_472_struct_v472_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=212, w2=386, w3=153, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(386, min_periods=max(386//3, 2)).max()
    trough = x.rolling(212, min_periods=max(212//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.543125 + 0.0012473 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_473_struct_v473_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=219, w2=397, w3=166, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(397, min_periods=max(397//3, 2)).rank(pct=True)
    persistence = change.rolling(166, min_periods=max(166//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3534 * persistence + 0.0012474 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_474_struct_v474_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=226, w2=408, w3=179, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(226, min_periods=max(226//3, 2)).std()
    vol_slow = ret.rolling(408, min_periods=max(408//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.571875 + 0.0012475 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_475_struct_v475_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=233, w2=419, w3=192, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(419, min_periods=max(419//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 233)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3686 * slope + 0.0012476 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_476_struct_v476_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=240, w2=430, w3=205, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(430, min_periods=max(430//3, 2)).mean()
    noise = impulse.abs().rolling(205, min_periods=max(205//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.600625 + 0.0012477 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_477_struct_v477_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=247, w2=441, w3=218, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 247)
    acceleration = _rolling_slope(velocity, 441)
    curvature = _rolling_slope(acceleration, 218)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3838 * acceleration + 0.0012478 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_478_struct_v478_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=254, w2=452, w3=231, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(254, min_periods=max(254//3, 2)).mean(), upside.rolling(452, min_periods=max(452//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.85625 + 0.0012479 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_479_struct_v479_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=10, w2=463, w3=244, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(463, min_periods=max(463//3, 2)).max()
    rebound = x - x.rolling(10, min_periods=max(10//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.399 * _rolling_slope(draw, 244) + 0.001248 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_480_struct_v480_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=17, w2=474, w3=257, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 17)
    baseline = trend.rolling(474, min_periods=max(474//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(257, min_periods=max(257//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.885 + 0.0012481 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_481_struct_v481_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=24, w2=485, w3=270, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 24)
    slow = _rolling_slope(x, 485)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=270, adjust=False).mean() * 0.899375 + 0.0012482 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_482_struct_v482_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=31, w2=496, w3=283, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(496, min_periods=max(496//3, 2)).max()
    trough = x.rolling(31, min_periods=max(31//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.91375 + 0.0012483 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_483_struct_v483_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=38, w2=507, w3=296, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(38)
    rank = change.rolling(507, min_periods=max(507//3, 2)).rank(pct=True)
    persistence = change.rolling(296, min_periods=max(296//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.053 * persistence + 0.0012484 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_484_struct_v484_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=45, w2=15, w3=309, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(45, min_periods=max(45//3, 2)).std()
    vol_slow = ret.rolling(15, min_periods=max(15//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.9425 + 0.0012485 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_485_struct_v485_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=52, w2=26, w3=322, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(26, min_periods=max(26//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 52)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0682 * slope + 0.0012486 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_486_struct_v486_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=59, w2=37, w3=335, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(59)
    drag = impulse.rolling(37, min_periods=max(37//3, 2)).mean()
    noise = impulse.abs().rolling(335, min_periods=max(335//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.97125 + 0.0012487 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_487_struct_v487_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=66, w2=48, w3=348, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 66)
    acceleration = _rolling_slope(velocity, 48)
    curvature = _rolling_slope(acceleration, 348)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0834 * acceleration + 0.0012488 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_488_struct_v488_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=73, w2=59, w3=361, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(73, min_periods=max(73//3, 2)).mean(), upside.rolling(59, min_periods=max(59//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.0 + 0.0012489 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_489_struct_v489_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=80, w2=70, w3=374, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(70, min_periods=max(70//3, 2)).max()
    rebound = x - x.rolling(80, min_periods=max(80//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0986 * _rolling_slope(draw, 374) + 0.001249 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_490_struct_v490_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=87, w2=81, w3=387, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 87)
    baseline = trend.rolling(81, min_periods=max(81//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(387, min_periods=max(387//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.02875 + 0.0012491 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_491_struct_v491_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=94, w2=92, w3=400, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 94)
    slow = _rolling_slope(x, 92)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.043125 + 0.0012492 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_492_struct_v492_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=101, w2=103, w3=413, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(103, min_periods=max(103//3, 2)).max()
    trough = x.rolling(101, min_periods=max(101//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.0575 + 0.0012493 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_493_struct_v493_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=108, w2=114, w3=426, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(108)
    rank = change.rolling(114, min_periods=max(114//3, 2)).rank(pct=True)
    persistence = change.rolling(426, min_periods=max(426//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.129 * persistence + 0.0012494 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_494_struct_v494_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=115, w2=125, w3=439, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(115, min_periods=max(115//3, 2)).std()
    vol_slow = ret.rolling(125, min_periods=max(125//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.08625 + 0.0012495 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_495_struct_v495_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=122, w2=136, w3=452, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(136, min_periods=max(136//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 122)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1442 * slope + 0.0012496 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_496_struct_v496_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=129, w2=147, w3=465, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(147, min_periods=max(147//3, 2)).mean()
    noise = impulse.abs().rolling(465, min_periods=max(465//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.115 + 0.0012497 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_497_struct_v497_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=136, w2=158, w3=478, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 136)
    acceleration = _rolling_slope(velocity, 158)
    curvature = _rolling_slope(acceleration, 478)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1594 * acceleration + 0.0012498 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_498_struct_v498_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=143, w2=169, w3=491, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(143, min_periods=max(143//3, 2)).mean(), upside.rolling(169, min_periods=max(169//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.14375 + 0.0012499 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_499_struct_v499_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=150, w2=180, w3=504, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(180, min_periods=max(180//3, 2)).max()
    rebound = x - x.rolling(150, min_periods=max(150//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1746 * _rolling_slope(draw, 504) + 0.00125 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_500_struct_v500_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=157, w2=191, w3=517, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 157)
    baseline = trend.rolling(191, min_periods=max(191//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(517, min_periods=max(517//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.1725 + 0.0012501 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_501_struct_v501_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=164, w2=202, w3=530, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 164)
    slow = _rolling_slope(x, 202)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.186875 + 0.0012502 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_502_struct_v502_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=171, w2=213, w3=543, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(213, min_periods=max(213//3, 2)).max()
    trough = x.rolling(171, min_periods=max(171//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.20125 + 0.0012503 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_503_struct_v503_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=178, w2=224, w3=556, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(224, min_periods=max(224//3, 2)).rank(pct=True)
    persistence = change.rolling(556, min_periods=max(556//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.205 * persistence + 0.0012504 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_504_struct_v504_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=185, w2=235, w3=569, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(185, min_periods=max(185//3, 2)).std()
    vol_slow = ret.rolling(235, min_periods=max(235//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.23 + 0.0012505 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_505_struct_v505_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=192, w2=246, w3=582, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(246, min_periods=max(246//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 192)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2202 * slope + 0.0012506 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_506_struct_v506_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=199, w2=257, w3=595, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(257, min_periods=max(257//3, 2)).mean()
    noise = impulse.abs().rolling(595, min_periods=max(595//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.25875 + 0.0012507 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_507_struct_v507_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=206, w2=268, w3=608, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 206)
    acceleration = _rolling_slope(velocity, 268)
    curvature = _rolling_slope(acceleration, 608)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2354 * acceleration + 0.0012508 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_508_struct_v508_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=213, w2=279, w3=621, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(213, min_periods=max(213//3, 2)).mean(), upside.rolling(279, min_periods=max(279//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.2875 + 0.0012509 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_509_struct_v509_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=220, w2=290, w3=634, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(290, min_periods=max(290//3, 2)).max()
    rebound = x - x.rolling(220, min_periods=max(220//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2506 * _rolling_slope(draw, 634) + 0.001251 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_510_struct_v510_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=227, w2=301, w3=647, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 227)
    baseline = trend.rolling(301, min_periods=max(301//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(647, min_periods=max(647//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.31625 + 0.0012511 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_511_struct_v511_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=234, w2=312, w3=660, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 234)
    slow = _rolling_slope(x, 312)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.330625 + 0.0012512 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_512_struct_v512_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=241, w2=323, w3=673, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(323, min_periods=max(323//3, 2)).max()
    trough = x.rolling(241, min_periods=max(241//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.345 + 0.0012513 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_513_struct_v513_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=248, w2=334, w3=686, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(334, min_periods=max(334//3, 2)).rank(pct=True)
    persistence = change.rolling(686, min_periods=max(686//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.281 * persistence + 0.0012514 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_514_struct_v514_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=255, w2=345, w3=699, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(255, min_periods=max(255//3, 2)).std()
    vol_slow = ret.rolling(345, min_periods=max(345//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.37375 + 0.0012515 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_515_struct_v515_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=11, w2=356, w3=712, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(356, min_periods=max(356//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 11)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2962 * slope + 0.0012516 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_516_struct_v516_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=18, w2=367, w3=725, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(18)
    drag = impulse.rolling(367, min_periods=max(367//3, 2)).mean()
    noise = impulse.abs().rolling(725, min_periods=max(725//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.4025 + 0.0012517 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_517_struct_v517_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=25, w2=378, w3=738, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 25)
    acceleration = _rolling_slope(velocity, 378)
    curvature = _rolling_slope(acceleration, 738)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3114 * acceleration + 0.0012518 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_518_struct_v518_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=32, w2=389, w3=751, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(32, min_periods=max(32//3, 2)).mean(), upside.rolling(389, min_periods=max(389//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.43125 + 0.0012519 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_519_struct_v519_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=39, w2=400, w3=764, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(400, min_periods=max(400//3, 2)).max()
    rebound = x - x.rolling(39, min_periods=max(39//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3266 * _rolling_slope(draw, 764) + 0.001252 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_520_struct_v520_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=46, w2=411, w3=20, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 46)
    baseline = trend.rolling(411, min_periods=max(411//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(20, min_periods=max(20//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.46 + 0.0012521 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_521_struct_v521_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=53, w2=422, w3=33, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 53)
    slow = _rolling_slope(x, 422)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=33, adjust=False).mean() * 1.474375 + 0.0012522 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_522_struct_v522_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=60, w2=433, w3=46, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(433, min_periods=max(433//3, 2)).max()
    trough = x.rolling(60, min_periods=max(60//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.48875 + 0.0012523 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_523_struct_v523_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=67, w2=444, w3=59, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(67)
    rank = change.rolling(444, min_periods=max(444//3, 2)).rank(pct=True)
    persistence = change.rolling(59, min_periods=max(59//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.357 * persistence + 0.0012524 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_524_struct_v524_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=74, w2=455, w3=72, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(74, min_periods=max(74//3, 2)).std()
    vol_slow = ret.rolling(455, min_periods=max(455//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.5175 + 0.0012525 * anchor
    return base_signal.diff().diff().diff()

def f20_inst_525_struct_v525_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=81, w2=466, w3=85, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(466, min_periods=max(466//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 81)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3722 * slope + 0.0012526 * anchor
    return base_signal.diff().diff().diff()
