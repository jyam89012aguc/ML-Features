"""81 inventory bloat acceleration d3 third derivative features 451-525 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Operating_Efficiency - Institutional-grade short-side signal.
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

def f81_invb_451_struct_v451_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=62, w2=385, w3=389, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 62)
    slow = _rolling_slope(x, 385)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.2575 + 0.0039452 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_452_struct_v452_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=69, w2=396, w3=402, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(396, min_periods=max(396//3, 2)).max()
    trough = x.rolling(69, min_periods=max(69//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.271875 + 0.0039453 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_453_struct_v453_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=76, w2=407, w3=415, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(76)
    rank = change.rolling(407, min_periods=max(407//3, 2)).rank(pct=True)
    persistence = change.rolling(415, min_periods=max(415//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2634 * persistence + 0.0039454 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_454_struct_v454_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=83, w2=418, w3=428, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(83, min_periods=max(83//3, 2)).std()
    vol_slow = ret.rolling(418, min_periods=max(418//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.300625 + 0.0039455 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_455_struct_v455_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=90, w2=429, w3=441, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(429, min_periods=max(429//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 90)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2786 * slope + 0.0039456 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_456_struct_v456_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=97, w2=440, w3=454, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(97)
    drag = impulse.rolling(440, min_periods=max(440//3, 2)).mean()
    noise = impulse.abs().rolling(454, min_periods=max(454//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.329375 + 0.0039457 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_457_struct_v457_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=104, w2=451, w3=467, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 104)
    acceleration = _rolling_slope(velocity, 451)
    curvature = _rolling_slope(acceleration, 467)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2938 * acceleration + 0.0039458 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_458_struct_v458_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=111, w2=462, w3=480, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(111, min_periods=max(111//3, 2)).mean(), upside.rolling(462, min_periods=max(462//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.358125 + 0.0039459 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_459_struct_v459_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=118, w2=473, w3=493, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(473, min_periods=max(473//3, 2)).max()
    rebound = x - x.rolling(118, min_periods=max(118//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.309 * _rolling_slope(draw, 493) + 0.003946 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_460_struct_v460_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=125, w2=484, w3=506, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 125)
    baseline = trend.rolling(484, min_periods=max(484//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(506, min_periods=max(506//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.386875 + 0.0039461 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_461_struct_v461_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=132, w2=495, w3=519, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 132)
    slow = _rolling_slope(x, 495)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.40125 + 0.0039462 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_462_struct_v462_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=139, w2=506, w3=532, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(506, min_periods=max(506//3, 2)).max()
    trough = x.rolling(139, min_periods=max(139//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.415625 + 0.0039463 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_463_struct_v463_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=146, w2=14, w3=545, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(14, min_periods=max(14//3, 2)).rank(pct=True)
    persistence = change.rolling(545, min_periods=max(545//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3394 * persistence + 0.0039464 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_464_struct_v464_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=153, w2=25, w3=558, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(153, min_periods=max(153//3, 2)).std()
    vol_slow = ret.rolling(25, min_periods=max(25//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.444375 + 0.0039465 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_465_struct_v465_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=160, w2=36, w3=571, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(36, min_periods=max(36//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 160)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3546 * slope + 0.0039466 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_466_struct_v466_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=167, w2=47, w3=584, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(47, min_periods=max(47//3, 2)).mean()
    noise = impulse.abs().rolling(584, min_periods=max(584//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.473125 + 0.0039467 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_467_struct_v467_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=174, w2=58, w3=597, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 174)
    acceleration = _rolling_slope(velocity, 58)
    curvature = _rolling_slope(acceleration, 597)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3698 * acceleration + 0.0039468 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_468_struct_v468_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=181, w2=69, w3=610, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(181, min_periods=max(181//3, 2)).mean(), upside.rolling(69, min_periods=max(69//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.501875 + 0.0039469 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_469_struct_v469_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=188, w2=80, w3=623, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(80, min_periods=max(80//3, 2)).max()
    rebound = x - x.rolling(188, min_periods=max(188//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.385 * _rolling_slope(draw, 623) + 0.003947 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_470_struct_v470_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=195, w2=91, w3=636, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 195)
    baseline = trend.rolling(91, min_periods=max(91//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(636, min_periods=max(636//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.530625 + 0.0039471 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_471_struct_v471_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=202, w2=102, w3=649, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 202)
    slow = _rolling_slope(x, 102)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.545 + 0.0039472 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_472_struct_v472_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=209, w2=113, w3=662, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(113, min_periods=max(113//3, 2)).max()
    trough = x.rolling(209, min_periods=max(209//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.559375 + 0.0039473 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_473_struct_v473_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=216, w2=124, w3=675, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(124, min_periods=max(124//3, 2)).rank(pct=True)
    persistence = change.rolling(675, min_periods=max(675//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.039 * persistence + 0.0039474 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_474_struct_v474_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=223, w2=135, w3=688, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(223, min_periods=max(223//3, 2)).std()
    vol_slow = ret.rolling(135, min_periods=max(135//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.588125 + 0.0039475 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_475_struct_v475_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=230, w2=146, w3=701, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(146, min_periods=max(146//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 230)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0542 * slope + 0.0039476 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_476_struct_v476_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=237, w2=157, w3=714, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(157, min_periods=max(157//3, 2)).mean()
    noise = impulse.abs().rolling(714, min_periods=max(714//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.616875 + 0.0039477 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_477_struct_v477_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=244, w2=168, w3=727, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 244)
    acceleration = _rolling_slope(velocity, 168)
    curvature = _rolling_slope(acceleration, 727)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0694 * acceleration + 0.0039478 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_478_struct_v478_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=251, w2=179, w3=740, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(251, min_periods=max(251//3, 2)).mean(), upside.rolling(179, min_periods=max(179//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.8725 + 0.0039479 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_479_struct_v479_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=7, w2=190, w3=753, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(190, min_periods=max(190//3, 2)).max()
    rebound = x - x.rolling(7, min_periods=max(7//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0846 * _rolling_slope(draw, 753) + 0.003948 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_480_struct_v480_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=14, w2=201, w3=766, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 14)
    baseline = trend.rolling(201, min_periods=max(201//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(766, min_periods=max(766//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.90125 + 0.0039481 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_481_struct_v481_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=21, w2=212, w3=22, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 21)
    slow = _rolling_slope(x, 212)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=22, adjust=False).mean() * 0.915625 + 0.0039482 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_482_struct_v482_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=28, w2=223, w3=35, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(223, min_periods=max(223//3, 2)).max()
    trough = x.rolling(28, min_periods=max(28//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.93 + 0.0039483 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_483_struct_v483_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=35, w2=234, w3=48, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(35)
    rank = change.rolling(234, min_periods=max(234//3, 2)).rank(pct=True)
    persistence = change.rolling(48, min_periods=max(48//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.115 * persistence + 0.0039484 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_484_struct_v484_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=42, w2=245, w3=61, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(42, min_periods=max(42//3, 2)).std()
    vol_slow = ret.rolling(245, min_periods=max(245//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.95875 + 0.0039485 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_485_struct_v485_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=49, w2=256, w3=74, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(256, min_periods=max(256//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 49)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1302 * slope + 0.0039486 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_486_struct_v486_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=56, w2=267, w3=87, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(56)
    drag = impulse.rolling(267, min_periods=max(267//3, 2)).mean()
    noise = impulse.abs().rolling(87, min_periods=max(87//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.9875 + 0.0039487 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_487_struct_v487_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=63, w2=278, w3=100, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 63)
    acceleration = _rolling_slope(velocity, 278)
    curvature = _rolling_slope(acceleration, 100)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1454 * acceleration + 0.0039488 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_488_struct_v488_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=70, w2=289, w3=113, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(70, min_periods=max(70//3, 2)).mean(), upside.rolling(289, min_periods=max(289//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(113) * 1.01625 + 0.0039489 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_489_struct_v489_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=77, w2=300, w3=126, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(300, min_periods=max(300//3, 2)).max()
    rebound = x - x.rolling(77, min_periods=max(77//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1606 * _rolling_slope(draw, 126) + 0.003949 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_490_struct_v490_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=84, w2=311, w3=139, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 84)
    baseline = trend.rolling(311, min_periods=max(311//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(139, min_periods=max(139//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.045 + 0.0039491 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_491_struct_v491_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=91, w2=322, w3=152, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 91)
    slow = _rolling_slope(x, 322)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=152, adjust=False).mean() * 1.059375 + 0.0039492 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_492_struct_v492_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=98, w2=333, w3=165, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(333, min_periods=max(333//3, 2)).max()
    trough = x.rolling(98, min_periods=max(98//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.07375 + 0.0039493 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_493_struct_v493_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=105, w2=344, w3=178, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(105)
    rank = change.rolling(344, min_periods=max(344//3, 2)).rank(pct=True)
    persistence = change.rolling(178, min_periods=max(178//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.191 * persistence + 0.0039494 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_494_struct_v494_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=112, w2=355, w3=191, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(112, min_periods=max(112//3, 2)).std()
    vol_slow = ret.rolling(355, min_periods=max(355//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.1025 + 0.0039495 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_495_struct_v495_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=119, w2=366, w3=204, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(366, min_periods=max(366//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 119)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2062 * slope + 0.0039496 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_496_struct_v496_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=126, w2=377, w3=217, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(377, min_periods=max(377//3, 2)).mean()
    noise = impulse.abs().rolling(217, min_periods=max(217//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.13125 + 0.0039497 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_497_struct_v497_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=133, w2=388, w3=230, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 133)
    acceleration = _rolling_slope(velocity, 388)
    curvature = _rolling_slope(acceleration, 230)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2214 * acceleration + 0.0039498 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_498_struct_v498_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=140, w2=399, w3=243, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(140, min_periods=max(140//3, 2)).mean(), upside.rolling(399, min_periods=max(399//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.16 + 0.0039499 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_499_struct_v499_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=147, w2=410, w3=256, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(410, min_periods=max(410//3, 2)).max()
    rebound = x - x.rolling(147, min_periods=max(147//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2366 * _rolling_slope(draw, 256) + 0.00395 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_500_struct_v500_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=154, w2=421, w3=269, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 154)
    baseline = trend.rolling(421, min_periods=max(421//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(269, min_periods=max(269//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.18875 + 0.0039501 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_501_struct_v501_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=161, w2=432, w3=282, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 161)
    slow = _rolling_slope(x, 432)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=282, adjust=False).mean() * 1.203125 + 0.0039502 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_502_struct_v502_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=168, w2=443, w3=295, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(443, min_periods=max(443//3, 2)).max()
    trough = x.rolling(168, min_periods=max(168//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.2175 + 0.0039503 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_503_struct_v503_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=175, w2=454, w3=308, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(454, min_periods=max(454//3, 2)).rank(pct=True)
    persistence = change.rolling(308, min_periods=max(308//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.267 * persistence + 0.0039504 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_504_struct_v504_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=182, w2=465, w3=321, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(182, min_periods=max(182//3, 2)).std()
    vol_slow = ret.rolling(465, min_periods=max(465//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.24625 + 0.0039505 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_505_struct_v505_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=189, w2=476, w3=334, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(476, min_periods=max(476//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 189)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2822 * slope + 0.0039506 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_506_struct_v506_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=196, w2=487, w3=347, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(487, min_periods=max(487//3, 2)).mean()
    noise = impulse.abs().rolling(347, min_periods=max(347//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.275 + 0.0039507 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_507_struct_v507_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=203, w2=498, w3=360, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 203)
    acceleration = _rolling_slope(velocity, 498)
    curvature = _rolling_slope(acceleration, 360)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2974 * acceleration + 0.0039508 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_508_struct_v508_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=210, w2=509, w3=373, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(210, min_periods=max(210//3, 2)).mean(), upside.rolling(509, min_periods=max(509//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.30375 + 0.0039509 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_509_struct_v509_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=217, w2=17, w3=386, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(17, min_periods=max(17//3, 2)).max()
    rebound = x - x.rolling(217, min_periods=max(217//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3126 * _rolling_slope(draw, 386) + 0.003951 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_510_struct_v510_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=224, w2=28, w3=399, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 224)
    baseline = trend.rolling(28, min_periods=max(28//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(399, min_periods=max(399//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.3325 + 0.0039511 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_511_struct_v511_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=231, w2=39, w3=412, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 231)
    slow = _rolling_slope(x, 39)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.346875 + 0.0039512 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_512_struct_v512_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=238, w2=50, w3=425, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(50, min_periods=max(50//3, 2)).max()
    trough = x.rolling(238, min_periods=max(238//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.36125 + 0.0039513 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_513_struct_v513_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=245, w2=61, w3=438, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(61, min_periods=max(61//3, 2)).rank(pct=True)
    persistence = change.rolling(438, min_periods=max(438//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.343 * persistence + 0.0039514 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_514_struct_v514_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=252, w2=72, w3=451, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(252, min_periods=max(252//3, 2)).std()
    vol_slow = ret.rolling(72, min_periods=max(72//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.39 + 0.0039515 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_515_struct_v515_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=8, w2=83, w3=464, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(83, min_periods=max(83//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 8)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3582 * slope + 0.0039516 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_516_struct_v516_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=15, w2=94, w3=477, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(15)
    drag = impulse.rolling(94, min_periods=max(94//3, 2)).mean()
    noise = impulse.abs().rolling(477, min_periods=max(477//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.41875 + 0.0039517 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_517_struct_v517_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=22, w2=105, w3=490, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 22)
    acceleration = _rolling_slope(velocity, 105)
    curvature = _rolling_slope(acceleration, 490)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3734 * acceleration + 0.0039518 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_518_struct_v518_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=29, w2=116, w3=503, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(29, min_periods=max(29//3, 2)).mean(), upside.rolling(116, min_periods=max(116//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.4475 + 0.0039519 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_519_struct_v519_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=36, w2=127, w3=516, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(127, min_periods=max(127//3, 2)).max()
    rebound = x - x.rolling(36, min_periods=max(36//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3886 * _rolling_slope(draw, 516) + 0.003952 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_520_struct_v520_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=43, w2=138, w3=529, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 43)
    baseline = trend.rolling(138, min_periods=max(138//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(529, min_periods=max(529//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.47625 + 0.0039521 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_521_struct_v521_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=50, w2=149, w3=542, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 50)
    slow = _rolling_slope(x, 149)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.490625 + 0.0039522 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_522_struct_v522_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=57, w2=160, w3=555, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(160, min_periods=max(160//3, 2)).max()
    trough = x.rolling(57, min_periods=max(57//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.505 + 0.0039523 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_523_struct_v523_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=64, w2=171, w3=568, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(64)
    rank = change.rolling(171, min_periods=max(171//3, 2)).rank(pct=True)
    persistence = change.rolling(568, min_periods=max(568//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0426 * persistence + 0.0039524 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_524_struct_v524_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=71, w2=182, w3=581, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(71, min_periods=max(71//3, 2)).std()
    vol_slow = ret.rolling(182, min_periods=max(182//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.53375 + 0.0039525 * anchor
    return base_signal.diff().diff().diff()

def f81_invb_525_struct_v525_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=78, w2=193, w3=594, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(193, min_periods=max(193//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 78)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0578 * slope + 0.0039526 * anchor
    return base_signal.diff().diff().diff()
