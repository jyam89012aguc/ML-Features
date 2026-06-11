"""44 moat erosion trajectory d3 third derivative features 526-600 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Fundamental_Trajectory - Institutional-grade short-side signal.
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

def f44_met_526_struct_v526_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=170, w2=493, w3=549, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(493, min_periods=max(493//3, 2)).mean()
    noise = impulse.abs().rolling(549, min_periods=max(549//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.469375 + 0.0027527 * anchor
    return base_signal.diff().diff().diff()

def f44_met_527_struct_v527_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=177, w2=504, w3=562, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 177)
    acceleration = _rolling_slope(velocity, 504)
    curvature = _rolling_slope(acceleration, 562)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3382 * acceleration + 0.0027528 * anchor
    return base_signal.diff().diff().diff()

def f44_met_528_struct_v528_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=184, w2=12, w3=575, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(184, min_periods=max(184//3, 2)).mean(), upside.rolling(12, min_periods=max(12//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.498125 + 0.0027529 * anchor
    return base_signal.diff().diff().diff()

def f44_met_529_struct_v529_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=191, w2=23, w3=588, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(23, min_periods=max(23//3, 2)).max()
    rebound = x - x.rolling(191, min_periods=max(191//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3534 * _rolling_slope(draw, 588) + 0.002753 * anchor
    return base_signal.diff().diff().diff()

def f44_met_530_struct_v530_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=198, w2=34, w3=601, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 198)
    baseline = trend.rolling(34, min_periods=max(34//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(601, min_periods=max(601//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.526875 + 0.0027531 * anchor
    return base_signal.diff().diff().diff()

def f44_met_531_struct_v531_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=205, w2=45, w3=614, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 205)
    slow = _rolling_slope(x, 45)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.54125 + 0.0027532 * anchor
    return base_signal.diff().diff().diff()

def f44_met_532_struct_v532_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=212, w2=56, w3=627, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(56, min_periods=max(56//3, 2)).max()
    trough = x.rolling(212, min_periods=max(212//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.555625 + 0.0027533 * anchor
    return base_signal.diff().diff().diff()

def f44_met_533_struct_v533_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=219, w2=67, w3=640, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(67, min_periods=max(67//3, 2)).rank(pct=True)
    persistence = change.rolling(640, min_periods=max(640//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3838 * persistence + 0.0027534 * anchor
    return base_signal.diff().diff().diff()

def f44_met_534_struct_v534_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=226, w2=78, w3=653, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(226, min_periods=max(226//3, 2)).std()
    vol_slow = ret.rolling(78, min_periods=max(78//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.584375 + 0.0027535 * anchor
    return base_signal.diff().diff().diff()

def f44_met_535_struct_v535_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=233, w2=89, w3=666, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(89, min_periods=max(89//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 233)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.399 * slope + 0.0027536 * anchor
    return base_signal.diff().diff().diff()

def f44_met_536_struct_v536_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=240, w2=100, w3=679, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(100, min_periods=max(100//3, 2)).mean()
    noise = impulse.abs().rolling(679, min_periods=max(679//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.613125 + 0.0027537 * anchor
    return base_signal.diff().diff().diff()

def f44_met_537_struct_v537_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=247, w2=111, w3=692, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 247)
    acceleration = _rolling_slope(velocity, 111)
    curvature = _rolling_slope(acceleration, 692)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0378 * acceleration + 0.0027538 * anchor
    return base_signal.diff().diff().diff()

def f44_met_538_struct_v538_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=254, w2=122, w3=705, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(254, min_periods=max(254//3, 2)).mean(), upside.rolling(122, min_periods=max(122//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.86875 + 0.0027539 * anchor
    return base_signal.diff().diff().diff()

def f44_met_539_struct_v539_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=10, w2=133, w3=718, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(133, min_periods=max(133//3, 2)).max()
    rebound = x - x.rolling(10, min_periods=max(10//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.053 * _rolling_slope(draw, 718) + 0.002754 * anchor
    return base_signal.diff().diff().diff()

def f44_met_540_struct_v540_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=17, w2=144, w3=731, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 17)
    baseline = trend.rolling(144, min_periods=max(144//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(731, min_periods=max(731//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.8975 + 0.0027541 * anchor
    return base_signal.diff().diff().diff()

def f44_met_541_struct_v541_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=24, w2=155, w3=744, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 24)
    slow = _rolling_slope(x, 155)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.911875 + 0.0027542 * anchor
    return base_signal.diff().diff().diff()

def f44_met_542_struct_v542_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=31, w2=166, w3=757, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(166, min_periods=max(166//3, 2)).max()
    trough = x.rolling(31, min_periods=max(31//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.92625 + 0.0027543 * anchor
    return base_signal.diff().diff().diff()

def f44_met_543_struct_v543_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=38, w2=177, w3=770, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(38)
    rank = change.rolling(177, min_periods=max(177//3, 2)).rank(pct=True)
    persistence = change.rolling(770, min_periods=max(770//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0834 * persistence + 0.0027544 * anchor
    return base_signal.diff().diff().diff()

def f44_met_544_struct_v544_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=45, w2=188, w3=26, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(45, min_periods=max(45//3, 2)).std()
    vol_slow = ret.rolling(188, min_periods=max(188//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.955 + 0.0027545 * anchor
    return base_signal.diff().diff().diff()

def f44_met_545_struct_v545_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=52, w2=199, w3=39, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(199, min_periods=max(199//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 52)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0986 * slope + 0.0027546 * anchor
    return base_signal.diff().diff().diff()

def f44_met_546_struct_v546_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=59, w2=210, w3=52, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(59)
    drag = impulse.rolling(210, min_periods=max(210//3, 2)).mean()
    noise = impulse.abs().rolling(52, min_periods=max(52//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.98375 + 0.0027547 * anchor
    return base_signal.diff().diff().diff()

def f44_met_547_struct_v547_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=66, w2=221, w3=65, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 66)
    acceleration = _rolling_slope(velocity, 221)
    curvature = _rolling_slope(acceleration, 65)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1138 * acceleration + 0.0027548 * anchor
    return base_signal.diff().diff().diff()

def f44_met_548_struct_v548_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=73, w2=232, w3=78, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(73, min_periods=max(73//3, 2)).mean(), upside.rolling(232, min_periods=max(232//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(78) * 1.0125 + 0.0027549 * anchor
    return base_signal.diff().diff().diff()

def f44_met_549_struct_v549_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=80, w2=243, w3=91, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(243, min_periods=max(243//3, 2)).max()
    rebound = x - x.rolling(80, min_periods=max(80//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.129 * _rolling_slope(draw, 91) + 0.002755 * anchor
    return base_signal.diff().diff().diff()

def f44_met_550_struct_v550_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=87, w2=254, w3=104, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 87)
    baseline = trend.rolling(254, min_periods=max(254//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(104, min_periods=max(104//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.04125 + 0.0027551 * anchor
    return base_signal.diff().diff().diff()

def f44_met_551_struct_v551_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=94, w2=265, w3=117, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 94)
    slow = _rolling_slope(x, 265)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=117, adjust=False).mean() * 1.055625 + 0.0027552 * anchor
    return base_signal.diff().diff().diff()

def f44_met_552_struct_v552_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=101, w2=276, w3=130, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(276, min_periods=max(276//3, 2)).max()
    trough = x.rolling(101, min_periods=max(101//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.07 + 0.0027553 * anchor
    return base_signal.diff().diff().diff()

def f44_met_553_struct_v553_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=108, w2=287, w3=143, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(108)
    rank = change.rolling(287, min_periods=max(287//3, 2)).rank(pct=True)
    persistence = change.rolling(143, min_periods=max(143//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1594 * persistence + 0.0027554 * anchor
    return base_signal.diff().diff().diff()

def f44_met_554_struct_v554_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=115, w2=298, w3=156, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(115, min_periods=max(115//3, 2)).std()
    vol_slow = ret.rolling(298, min_periods=max(298//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.09875 + 0.0027555 * anchor
    return base_signal.diff().diff().diff()

def f44_met_555_struct_v555_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=122, w2=309, w3=169, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(309, min_periods=max(309//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 122)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1746 * slope + 0.0027556 * anchor
    return base_signal.diff().diff().diff()

def f44_met_556_struct_v556_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=129, w2=320, w3=182, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(320, min_periods=max(320//3, 2)).mean()
    noise = impulse.abs().rolling(182, min_periods=max(182//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.1275 + 0.0027557 * anchor
    return base_signal.diff().diff().diff()

def f44_met_557_struct_v557_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=136, w2=331, w3=195, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 136)
    acceleration = _rolling_slope(velocity, 331)
    curvature = _rolling_slope(acceleration, 195)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1898 * acceleration + 0.0027558 * anchor
    return base_signal.diff().diff().diff()

def f44_met_558_struct_v558_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=143, w2=342, w3=208, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(143, min_periods=max(143//3, 2)).mean(), upside.rolling(342, min_periods=max(342//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.15625 + 0.0027559 * anchor
    return base_signal.diff().diff().diff()

def f44_met_559_struct_v559_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=150, w2=353, w3=221, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(353, min_periods=max(353//3, 2)).max()
    rebound = x - x.rolling(150, min_periods=max(150//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.205 * _rolling_slope(draw, 221) + 0.002756 * anchor
    return base_signal.diff().diff().diff()

def f44_met_560_struct_v560_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=157, w2=364, w3=234, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 157)
    baseline = trend.rolling(364, min_periods=max(364//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(234, min_periods=max(234//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.185 + 0.0027561 * anchor
    return base_signal.diff().diff().diff()

def f44_met_561_struct_v561_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=164, w2=375, w3=247, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 164)
    slow = _rolling_slope(x, 375)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=247, adjust=False).mean() * 1.199375 + 0.0027562 * anchor
    return base_signal.diff().diff().diff()

def f44_met_562_struct_v562_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=171, w2=386, w3=260, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(386, min_periods=max(386//3, 2)).max()
    trough = x.rolling(171, min_periods=max(171//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.21375 + 0.0027563 * anchor
    return base_signal.diff().diff().diff()

def f44_met_563_struct_v563_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=178, w2=397, w3=273, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(397, min_periods=max(397//3, 2)).rank(pct=True)
    persistence = change.rolling(273, min_periods=max(273//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2354 * persistence + 0.0027564 * anchor
    return base_signal.diff().diff().diff()

def f44_met_564_struct_v564_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=185, w2=408, w3=286, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(185, min_periods=max(185//3, 2)).std()
    vol_slow = ret.rolling(408, min_periods=max(408//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.2425 + 0.0027565 * anchor
    return base_signal.diff().diff().diff()

def f44_met_565_struct_v565_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=192, w2=419, w3=299, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(419, min_periods=max(419//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 192)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2506 * slope + 0.0027566 * anchor
    return base_signal.diff().diff().diff()

def f44_met_566_struct_v566_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=199, w2=430, w3=312, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(430, min_periods=max(430//3, 2)).mean()
    noise = impulse.abs().rolling(312, min_periods=max(312//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.27125 + 0.0027567 * anchor
    return base_signal.diff().diff().diff()

def f44_met_567_struct_v567_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=206, w2=441, w3=325, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 206)
    acceleration = _rolling_slope(velocity, 441)
    curvature = _rolling_slope(acceleration, 325)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2658 * acceleration + 0.0027568 * anchor
    return base_signal.diff().diff().diff()

def f44_met_568_struct_v568_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=213, w2=452, w3=338, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(213, min_periods=max(213//3, 2)).mean(), upside.rolling(452, min_periods=max(452//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.3 + 0.0027569 * anchor
    return base_signal.diff().diff().diff()

def f44_met_569_struct_v569_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=220, w2=463, w3=351, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(463, min_periods=max(463//3, 2)).max()
    rebound = x - x.rolling(220, min_periods=max(220//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.281 * _rolling_slope(draw, 351) + 0.002757 * anchor
    return base_signal.diff().diff().diff()

def f44_met_570_struct_v570_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=227, w2=474, w3=364, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 227)
    baseline = trend.rolling(474, min_periods=max(474//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(364, min_periods=max(364//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.32875 + 0.0027571 * anchor
    return base_signal.diff().diff().diff()

def f44_met_571_struct_v571_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=234, w2=485, w3=377, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 234)
    slow = _rolling_slope(x, 485)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.343125 + 0.0027572 * anchor
    return base_signal.diff().diff().diff()

def f44_met_572_struct_v572_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=241, w2=496, w3=390, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(496, min_periods=max(496//3, 2)).max()
    trough = x.rolling(241, min_periods=max(241//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.3575 + 0.0027573 * anchor
    return base_signal.diff().diff().diff()

def f44_met_573_struct_v573_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=248, w2=507, w3=403, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(507, min_periods=max(507//3, 2)).rank(pct=True)
    persistence = change.rolling(403, min_periods=max(403//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3114 * persistence + 0.0027574 * anchor
    return base_signal.diff().diff().diff()

def f44_met_574_struct_v574_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=255, w2=15, w3=416, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(255, min_periods=max(255//3, 2)).std()
    vol_slow = ret.rolling(15, min_periods=max(15//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.38625 + 0.0027575 * anchor
    return base_signal.diff().diff().diff()

def f44_met_575_struct_v575_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=11, w2=26, w3=429, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(26, min_periods=max(26//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 11)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3266 * slope + 0.0027576 * anchor
    return base_signal.diff().diff().diff()

def f44_met_576_struct_v576_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=18, w2=37, w3=442, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(18)
    drag = impulse.rolling(37, min_periods=max(37//3, 2)).mean()
    noise = impulse.abs().rolling(442, min_periods=max(442//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.415 + 0.0027577 * anchor
    return base_signal.diff().diff().diff()

def f44_met_577_struct_v577_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=25, w2=48, w3=455, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 25)
    acceleration = _rolling_slope(velocity, 48)
    curvature = _rolling_slope(acceleration, 455)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3418 * acceleration + 0.0027578 * anchor
    return base_signal.diff().diff().diff()

def f44_met_578_struct_v578_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=32, w2=59, w3=468, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(32, min_periods=max(32//3, 2)).mean(), upside.rolling(59, min_periods=max(59//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.44375 + 0.0027579 * anchor
    return base_signal.diff().diff().diff()

def f44_met_579_struct_v579_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=39, w2=70, w3=481, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(70, min_periods=max(70//3, 2)).max()
    rebound = x - x.rolling(39, min_periods=max(39//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.357 * _rolling_slope(draw, 481) + 0.002758 * anchor
    return base_signal.diff().diff().diff()

def f44_met_580_struct_v580_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=46, w2=81, w3=494, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 46)
    baseline = trend.rolling(81, min_periods=max(81//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(494, min_periods=max(494//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.4725 + 0.0027581 * anchor
    return base_signal.diff().diff().diff()

def f44_met_581_struct_v581_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=53, w2=92, w3=507, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 53)
    slow = _rolling_slope(x, 92)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.486875 + 0.0027582 * anchor
    return base_signal.diff().diff().diff()

def f44_met_582_struct_v582_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=60, w2=103, w3=520, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(103, min_periods=max(103//3, 2)).max()
    trough = x.rolling(60, min_periods=max(60//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.50125 + 0.0027583 * anchor
    return base_signal.diff().diff().diff()

def f44_met_583_struct_v583_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=67, w2=114, w3=533, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(67)
    rank = change.rolling(114, min_periods=max(114//3, 2)).rank(pct=True)
    persistence = change.rolling(533, min_periods=max(533//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3874 * persistence + 0.0027584 * anchor
    return base_signal.diff().diff().diff()

def f44_met_584_struct_v584_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=74, w2=125, w3=546, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(74, min_periods=max(74//3, 2)).std()
    vol_slow = ret.rolling(125, min_periods=max(125//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.53 + 0.0027585 * anchor
    return base_signal.diff().diff().diff()

def f44_met_585_struct_v585_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=81, w2=136, w3=559, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(136, min_periods=max(136//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 81)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.4026 * slope + 0.0027586 * anchor
    return base_signal.diff().diff().diff()

def f44_met_586_struct_v586_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=88, w2=147, w3=572, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(88)
    drag = impulse.rolling(147, min_periods=max(147//3, 2)).mean()
    noise = impulse.abs().rolling(572, min_periods=max(572//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.55875 + 0.0027587 * anchor
    return base_signal.diff().diff().diff()

def f44_met_587_struct_v587_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=95, w2=158, w3=585, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 95)
    acceleration = _rolling_slope(velocity, 158)
    curvature = _rolling_slope(acceleration, 585)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0414 * acceleration + 0.0027588 * anchor
    return base_signal.diff().diff().diff()

def f44_met_588_struct_v588_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=102, w2=169, w3=598, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(102, min_periods=max(102//3, 2)).mean(), upside.rolling(169, min_periods=max(169//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.5875 + 0.0027589 * anchor
    return base_signal.diff().diff().diff()

def f44_met_589_struct_v589_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=109, w2=180, w3=611, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(180, min_periods=max(180//3, 2)).max()
    rebound = x - x.rolling(109, min_periods=max(109//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0566 * _rolling_slope(draw, 611) + 0.002759 * anchor
    return base_signal.diff().diff().diff()

def f44_met_590_struct_v590_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=116, w2=191, w3=624, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 116)
    baseline = trend.rolling(191, min_periods=max(191//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(624, min_periods=max(624//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.61625 + 0.0027591 * anchor
    return base_signal.diff().diff().diff()

def f44_met_591_struct_v591_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=123, w2=202, w3=637, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 123)
    slow = _rolling_slope(x, 202)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.8575 + 0.0027592 * anchor
    return base_signal.diff().diff().diff()

def f44_met_592_struct_v592_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=130, w2=213, w3=650, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(213, min_periods=max(213//3, 2)).max()
    trough = x.rolling(130, min_periods=max(130//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.871875 + 0.0027593 * anchor
    return base_signal.diff().diff().diff()

def f44_met_593_struct_v593_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=137, w2=224, w3=663, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(224, min_periods=max(224//3, 2)).rank(pct=True)
    persistence = change.rolling(663, min_periods=max(663//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.087 * persistence + 0.0027594 * anchor
    return base_signal.diff().diff().diff()

def f44_met_594_struct_v594_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=144, w2=235, w3=676, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(144, min_periods=max(144//3, 2)).std()
    vol_slow = ret.rolling(235, min_periods=max(235//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.900625 + 0.0027595 * anchor
    return base_signal.diff().diff().diff()

def f44_met_595_struct_v595_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=151, w2=246, w3=689, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(246, min_periods=max(246//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 151)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1022 * slope + 0.0027596 * anchor
    return base_signal.diff().diff().diff()

def f44_met_596_struct_v596_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=158, w2=257, w3=702, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(257, min_periods=max(257//3, 2)).mean()
    noise = impulse.abs().rolling(702, min_periods=max(702//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.929375 + 0.0027597 * anchor
    return base_signal.diff().diff().diff()

def f44_met_597_struct_v597_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=165, w2=268, w3=715, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 165)
    acceleration = _rolling_slope(velocity, 268)
    curvature = _rolling_slope(acceleration, 715)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1174 * acceleration + 0.0027598 * anchor
    return base_signal.diff().diff().diff()

def f44_met_598_struct_v598_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=172, w2=279, w3=728, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(172, min_periods=max(172//3, 2)).mean(), upside.rolling(279, min_periods=max(279//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.958125 + 0.0027599 * anchor
    return base_signal.diff().diff().diff()

def f44_met_599_struct_v599_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=179, w2=290, w3=741, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(290, min_periods=max(290//3, 2)).max()
    rebound = x - x.rolling(179, min_periods=max(179//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1326 * _rolling_slope(draw, 741) + 0.00276 * anchor
    return base_signal.diff().diff().diff()

def f44_met_600_struct_v600_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=186, w2=301, w3=754, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 186)
    baseline = trend.rolling(301, min_periods=max(301//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(754, min_periods=max(754//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.986875 + 0.0027601 * anchor
    return base_signal.diff().diff().diff()
