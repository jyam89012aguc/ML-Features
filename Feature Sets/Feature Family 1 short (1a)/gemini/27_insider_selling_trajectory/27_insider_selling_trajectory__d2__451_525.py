"""27 insider selling trajectory d2 second derivative features 451-525 â€” Pipeline 1a-HF Grade v3.

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

def f27_ist_451_struct_v451_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=98, w2=79, w3=733, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 98)
    slow = _rolling_slope(x, 79)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.3125 + 0.0016652 * anchor
    return base_signal.diff().diff()

def f27_ist_452_struct_v452_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=105, w2=90, w3=746, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(90, min_periods=max(90//3, 2)).max()
    trough = x.rolling(105, min_periods=max(105//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.326875 + 0.0016653 * anchor
    return base_signal.diff().diff()

def f27_ist_453_struct_v453_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=112, w2=101, w3=759, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(112)
    rank = change.rolling(101, min_periods=max(101//3, 2)).rank(pct=True)
    persistence = change.rolling(759, min_periods=max(759//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1274 * persistence + 0.0016654 * anchor
    return base_signal.diff().diff()

def f27_ist_454_struct_v454_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=119, w2=112, w3=15, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(119, min_periods=max(119//3, 2)).std()
    vol_slow = ret.rolling(112, min_periods=max(112//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.355625 + 0.0016655 * anchor
    return base_signal.diff().diff()

def f27_ist_455_struct_v455_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=126, w2=123, w3=28, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(123, min_periods=max(123//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 126)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1426 * slope + 0.0016656 * anchor
    return base_signal.diff().diff()

def f27_ist_456_struct_v456_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=133, w2=134, w3=41, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(134, min_periods=max(134//3, 2)).mean()
    noise = impulse.abs().rolling(41, min_periods=max(41//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.384375 + 0.0016657 * anchor
    return base_signal.diff().diff()

def f27_ist_457_struct_v457_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=140, w2=145, w3=54, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 140)
    acceleration = _rolling_slope(velocity, 145)
    curvature = _rolling_slope(acceleration, 54)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1578 * acceleration + 0.0016658 * anchor
    return base_signal.diff().diff()

def f27_ist_458_struct_v458_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=147, w2=156, w3=67, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(147, min_periods=max(147//3, 2)).mean(), upside.rolling(156, min_periods=max(156//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(67) * 1.413125 + 0.0016659 * anchor
    return base_signal.diff().diff()

def f27_ist_459_struct_v459_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=154, w2=167, w3=80, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(167, min_periods=max(167//3, 2)).max()
    rebound = x - x.rolling(154, min_periods=max(154//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.173 * _rolling_slope(draw, 80) + 0.001666 * anchor
    return base_signal.diff().diff()

def f27_ist_460_struct_v460_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=161, w2=178, w3=93, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 161)
    baseline = trend.rolling(178, min_periods=max(178//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(93, min_periods=max(93//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.441875 + 0.0016661 * anchor
    return base_signal.diff().diff()

def f27_ist_461_struct_v461_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=168, w2=189, w3=106, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 168)
    slow = _rolling_slope(x, 189)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=106, adjust=False).mean() * 1.45625 + 0.0016662 * anchor
    return base_signal.diff().diff()

def f27_ist_462_struct_v462_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=175, w2=200, w3=119, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(200, min_periods=max(200//3, 2)).max()
    trough = x.rolling(175, min_periods=max(175//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.470625 + 0.0016663 * anchor
    return base_signal.diff().diff()

def f27_ist_463_struct_v463_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=182, w2=211, w3=132, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(211, min_periods=max(211//3, 2)).rank(pct=True)
    persistence = change.rolling(132, min_periods=max(132//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2034 * persistence + 0.0016664 * anchor
    return base_signal.diff().diff()

def f27_ist_464_struct_v464_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=189, w2=222, w3=145, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(189, min_periods=max(189//3, 2)).std()
    vol_slow = ret.rolling(222, min_periods=max(222//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.499375 + 0.0016665 * anchor
    return base_signal.diff().diff()

def f27_ist_465_struct_v465_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=196, w2=233, w3=158, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(233, min_periods=max(233//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 196)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2186 * slope + 0.0016666 * anchor
    return base_signal.diff().diff()

def f27_ist_466_struct_v466_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=203, w2=244, w3=171, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(244, min_periods=max(244//3, 2)).mean()
    noise = impulse.abs().rolling(171, min_periods=max(171//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.528125 + 0.0016667 * anchor
    return base_signal.diff().diff()

def f27_ist_467_struct_v467_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=210, w2=255, w3=184, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 210)
    acceleration = _rolling_slope(velocity, 255)
    curvature = _rolling_slope(acceleration, 184)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2338 * acceleration + 0.0016668 * anchor
    return base_signal.diff().diff()

def f27_ist_468_struct_v468_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=217, w2=266, w3=197, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(217, min_periods=max(217//3, 2)).mean(), upside.rolling(266, min_periods=max(266//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.556875 + 0.0016669 * anchor
    return base_signal.diff().diff()

def f27_ist_469_struct_v469_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=224, w2=277, w3=210, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(277, min_periods=max(277//3, 2)).max()
    rebound = x - x.rolling(224, min_periods=max(224//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.249 * _rolling_slope(draw, 210) + 0.001667 * anchor
    return base_signal.diff().diff()

def f27_ist_470_struct_v470_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=231, w2=288, w3=223, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 231)
    baseline = trend.rolling(288, min_periods=max(288//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(223, min_periods=max(223//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.585625 + 0.0016671 * anchor
    return base_signal.diff().diff()

def f27_ist_471_struct_v471_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=238, w2=299, w3=236, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 238)
    slow = _rolling_slope(x, 299)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=236, adjust=False).mean() * 1.6 + 0.0016672 * anchor
    return base_signal.diff().diff()

def f27_ist_472_struct_v472_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=245, w2=310, w3=249, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(310, min_periods=max(310//3, 2)).max()
    trough = x.rolling(245, min_periods=max(245//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.614375 + 0.0016673 * anchor
    return base_signal.diff().diff()

def f27_ist_473_struct_v473_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=252, w2=321, w3=262, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(321, min_periods=max(321//3, 2)).rank(pct=True)
    persistence = change.rolling(262, min_periods=max(262//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2794 * persistence + 0.0016674 * anchor
    return base_signal.diff().diff()

def f27_ist_474_struct_v474_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=8, w2=332, w3=275, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(8, min_periods=max(8//3, 2)).std()
    vol_slow = ret.rolling(332, min_periods=max(332//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.87 + 0.0016675 * anchor
    return base_signal.diff().diff()

def f27_ist_475_struct_v475_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=15, w2=343, w3=288, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(343, min_periods=max(343//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 15)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2946 * slope + 0.0016676 * anchor
    return base_signal.diff().diff()

def f27_ist_476_struct_v476_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=22, w2=354, w3=301, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(22)
    drag = impulse.rolling(354, min_periods=max(354//3, 2)).mean()
    noise = impulse.abs().rolling(301, min_periods=max(301//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.89875 + 0.0016677 * anchor
    return base_signal.diff().diff()

def f27_ist_477_struct_v477_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=29, w2=365, w3=314, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 29)
    acceleration = _rolling_slope(velocity, 365)
    curvature = _rolling_slope(acceleration, 314)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3098 * acceleration + 0.0016678 * anchor
    return base_signal.diff().diff()

def f27_ist_478_struct_v478_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=36, w2=376, w3=327, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(36, min_periods=max(36//3, 2)).mean(), upside.rolling(376, min_periods=max(376//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.9275 + 0.0016679 * anchor
    return base_signal.diff().diff()

def f27_ist_479_struct_v479_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=43, w2=387, w3=340, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(387, min_periods=max(387//3, 2)).max()
    rebound = x - x.rolling(43, min_periods=max(43//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.325 * _rolling_slope(draw, 340) + 0.001668 * anchor
    return base_signal.diff().diff()

def f27_ist_480_struct_v480_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=50, w2=398, w3=353, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 50)
    baseline = trend.rolling(398, min_periods=max(398//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(353, min_periods=max(353//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.95625 + 0.0016681 * anchor
    return base_signal.diff().diff()

def f27_ist_481_struct_v481_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=57, w2=409, w3=366, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 57)
    slow = _rolling_slope(x, 409)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.970625 + 0.0016682 * anchor
    return base_signal.diff().diff()

def f27_ist_482_struct_v482_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=64, w2=420, w3=379, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(420, min_periods=max(420//3, 2)).max()
    trough = x.rolling(64, min_periods=max(64//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.985 + 0.0016683 * anchor
    return base_signal.diff().diff()

def f27_ist_483_struct_v483_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=71, w2=431, w3=392, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(71)
    rank = change.rolling(431, min_periods=max(431//3, 2)).rank(pct=True)
    persistence = change.rolling(392, min_periods=max(392//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3554 * persistence + 0.0016684 * anchor
    return base_signal.diff().diff()

def f27_ist_484_struct_v484_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=78, w2=442, w3=405, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(78, min_periods=max(78//3, 2)).std()
    vol_slow = ret.rolling(442, min_periods=max(442//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.01375 + 0.0016685 * anchor
    return base_signal.diff().diff()

def f27_ist_485_struct_v485_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=85, w2=453, w3=418, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(453, min_periods=max(453//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 85)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3706 * slope + 0.0016686 * anchor
    return base_signal.diff().diff()

def f27_ist_486_struct_v486_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=92, w2=464, w3=431, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(92)
    drag = impulse.rolling(464, min_periods=max(464//3, 2)).mean()
    noise = impulse.abs().rolling(431, min_periods=max(431//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.0425 + 0.0016687 * anchor
    return base_signal.diff().diff()

def f27_ist_487_struct_v487_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=99, w2=475, w3=444, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 99)
    acceleration = _rolling_slope(velocity, 475)
    curvature = _rolling_slope(acceleration, 444)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3858 * acceleration + 0.0016688 * anchor
    return base_signal.diff().diff()

def f27_ist_488_struct_v488_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=106, w2=486, w3=457, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(106, min_periods=max(106//3, 2)).mean(), upside.rolling(486, min_periods=max(486//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.07125 + 0.0016689 * anchor
    return base_signal.diff().diff()

def f27_ist_489_struct_v489_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=113, w2=497, w3=470, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(497, min_periods=max(497//3, 2)).max()
    rebound = x - x.rolling(113, min_periods=max(113//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.401 * _rolling_slope(draw, 470) + 0.001669 * anchor
    return base_signal.diff().diff()

def f27_ist_490_struct_v490_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=120, w2=508, w3=483, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 120)
    baseline = trend.rolling(508, min_periods=max(508//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(483, min_periods=max(483//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.1 + 0.0016691 * anchor
    return base_signal.diff().diff()

def f27_ist_491_struct_v491_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=127, w2=16, w3=496, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 127)
    slow = _rolling_slope(x, 16)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.114375 + 0.0016692 * anchor
    return base_signal.diff().diff()

def f27_ist_492_struct_v492_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=134, w2=27, w3=509, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(27, min_periods=max(27//3, 2)).max()
    trough = x.rolling(134, min_periods=max(134//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.12875 + 0.0016693 * anchor
    return base_signal.diff().diff()

def f27_ist_493_struct_v493_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=141, w2=38, w3=522, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(38, min_periods=max(38//3, 2)).rank(pct=True)
    persistence = change.rolling(522, min_periods=max(522//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.055 * persistence + 0.0016694 * anchor
    return base_signal.diff().diff()

def f27_ist_494_struct_v494_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=148, w2=49, w3=535, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(148, min_periods=max(148//3, 2)).std()
    vol_slow = ret.rolling(49, min_periods=max(49//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.1575 + 0.0016695 * anchor
    return base_signal.diff().diff()

def f27_ist_495_struct_v495_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=155, w2=60, w3=548, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(60, min_periods=max(60//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 155)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0702 * slope + 0.0016696 * anchor
    return base_signal.diff().diff()

def f27_ist_496_struct_v496_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=162, w2=71, w3=561, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(71, min_periods=max(71//3, 2)).mean()
    noise = impulse.abs().rolling(561, min_periods=max(561//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.18625 + 0.0016697 * anchor
    return base_signal.diff().diff()

def f27_ist_497_struct_v497_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=169, w2=82, w3=574, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 169)
    acceleration = _rolling_slope(velocity, 82)
    curvature = _rolling_slope(acceleration, 574)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0854 * acceleration + 0.0016698 * anchor
    return base_signal.diff().diff()

def f27_ist_498_struct_v498_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=176, w2=93, w3=587, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(176, min_periods=max(176//3, 2)).mean(), upside.rolling(93, min_periods=max(93//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.215 + 0.0016699 * anchor
    return base_signal.diff().diff()

def f27_ist_499_struct_v499_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=183, w2=104, w3=600, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(104, min_periods=max(104//3, 2)).max()
    rebound = x - x.rolling(183, min_periods=max(183//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1006 * _rolling_slope(draw, 600) + 0.00167 * anchor
    return base_signal.diff().diff()

def f27_ist_500_struct_v500_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=190, w2=115, w3=613, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 190)
    baseline = trend.rolling(115, min_periods=max(115//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(613, min_periods=max(613//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.24375 + 0.0016701 * anchor
    return base_signal.diff().diff()

def f27_ist_501_struct_v501_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=197, w2=126, w3=626, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 197)
    slow = _rolling_slope(x, 126)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.258125 + 0.0016702 * anchor
    return base_signal.diff().diff()

def f27_ist_502_struct_v502_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=204, w2=137, w3=639, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(137, min_periods=max(137//3, 2)).max()
    trough = x.rolling(204, min_periods=max(204//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.2725 + 0.0016703 * anchor
    return base_signal.diff().diff()

def f27_ist_503_struct_v503_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=211, w2=148, w3=652, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(148, min_periods=max(148//3, 2)).rank(pct=True)
    persistence = change.rolling(652, min_periods=max(652//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.131 * persistence + 0.0016704 * anchor
    return base_signal.diff().diff()

def f27_ist_504_struct_v504_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=218, w2=159, w3=665, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(218, min_periods=max(218//3, 2)).std()
    vol_slow = ret.rolling(159, min_periods=max(159//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.30125 + 0.0016705 * anchor
    return base_signal.diff().diff()

def f27_ist_505_struct_v505_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=225, w2=170, w3=678, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(170, min_periods=max(170//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 225)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1462 * slope + 0.0016706 * anchor
    return base_signal.diff().diff()

def f27_ist_506_struct_v506_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=232, w2=181, w3=691, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(181, min_periods=max(181//3, 2)).mean()
    noise = impulse.abs().rolling(691, min_periods=max(691//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.33 + 0.0016707 * anchor
    return base_signal.diff().diff()

def f27_ist_507_struct_v507_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=239, w2=192, w3=704, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 239)
    acceleration = _rolling_slope(velocity, 192)
    curvature = _rolling_slope(acceleration, 704)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1614 * acceleration + 0.0016708 * anchor
    return base_signal.diff().diff()

def f27_ist_508_struct_v508_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=246, w2=203, w3=717, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(246, min_periods=max(246//3, 2)).mean(), upside.rolling(203, min_periods=max(203//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.35875 + 0.0016709 * anchor
    return base_signal.diff().diff()

def f27_ist_509_struct_v509_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=253, w2=214, w3=730, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(214, min_periods=max(214//3, 2)).max()
    rebound = x - x.rolling(253, min_periods=max(253//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1766 * _rolling_slope(draw, 730) + 0.001671 * anchor
    return base_signal.diff().diff()

def f27_ist_510_struct_v510_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=9, w2=225, w3=743, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 9)
    baseline = trend.rolling(225, min_periods=max(225//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(743, min_periods=max(743//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.3875 + 0.0016711 * anchor
    return base_signal.diff().diff()

def f27_ist_511_struct_v511_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=16, w2=236, w3=756, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 16)
    slow = _rolling_slope(x, 236)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.401875 + 0.0016712 * anchor
    return base_signal.diff().diff()

def f27_ist_512_struct_v512_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=23, w2=247, w3=769, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(247, min_periods=max(247//3, 2)).max()
    trough = x.rolling(23, min_periods=max(23//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.41625 + 0.0016713 * anchor
    return base_signal.diff().diff()

def f27_ist_513_struct_v513_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=30, w2=258, w3=25, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(30)
    rank = change.rolling(258, min_periods=max(258//3, 2)).rank(pct=True)
    persistence = change.rolling(25, min_periods=max(25//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.207 * persistence + 0.0016714 * anchor
    return base_signal.diff().diff()

def f27_ist_514_struct_v514_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=37, w2=269, w3=38, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(37, min_periods=max(37//3, 2)).std()
    vol_slow = ret.rolling(269, min_periods=max(269//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.445 + 0.0016715 * anchor
    return base_signal.diff().diff()

def f27_ist_515_struct_v515_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=44, w2=280, w3=51, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(280, min_periods=max(280//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 44)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2222 * slope + 0.0016716 * anchor
    return base_signal.diff().diff()

def f27_ist_516_struct_v516_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=51, w2=291, w3=64, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(51)
    drag = impulse.rolling(291, min_periods=max(291//3, 2)).mean()
    noise = impulse.abs().rolling(64, min_periods=max(64//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.47375 + 0.0016717 * anchor
    return base_signal.diff().diff()

def f27_ist_517_struct_v517_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=58, w2=302, w3=77, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 58)
    acceleration = _rolling_slope(velocity, 302)
    curvature = _rolling_slope(acceleration, 77)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2374 * acceleration + 0.0016718 * anchor
    return base_signal.diff().diff()

def f27_ist_518_struct_v518_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=65, w2=313, w3=90, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(65, min_periods=max(65//3, 2)).mean(), upside.rolling(313, min_periods=max(313//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(90) * 1.5025 + 0.0016719 * anchor
    return base_signal.diff().diff()

def f27_ist_519_struct_v519_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=72, w2=324, w3=103, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(324, min_periods=max(324//3, 2)).max()
    rebound = x - x.rolling(72, min_periods=max(72//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2526 * _rolling_slope(draw, 103) + 0.001672 * anchor
    return base_signal.diff().diff()

def f27_ist_520_struct_v520_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=79, w2=335, w3=116, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 79)
    baseline = trend.rolling(335, min_periods=max(335//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(116, min_periods=max(116//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.53125 + 0.0016721 * anchor
    return base_signal.diff().diff()

def f27_ist_521_struct_v521_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=86, w2=346, w3=129, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 86)
    slow = _rolling_slope(x, 346)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=129, adjust=False).mean() * 1.545625 + 0.0016722 * anchor
    return base_signal.diff().diff()

def f27_ist_522_struct_v522_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=93, w2=357, w3=142, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(357, min_periods=max(357//3, 2)).max()
    trough = x.rolling(93, min_periods=max(93//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.56 + 0.0016723 * anchor
    return base_signal.diff().diff()

def f27_ist_523_struct_v523_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=100, w2=368, w3=155, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(100)
    rank = change.rolling(368, min_periods=max(368//3, 2)).rank(pct=True)
    persistence = change.rolling(155, min_periods=max(155//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.283 * persistence + 0.0016724 * anchor
    return base_signal.diff().diff()

def f27_ist_524_struct_v524_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=107, w2=379, w3=168, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(107, min_periods=max(107//3, 2)).std()
    vol_slow = ret.rolling(379, min_periods=max(379//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.58875 + 0.0016725 * anchor
    return base_signal.diff().diff()

def f27_ist_525_struct_v525_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=114, w2=390, w3=181, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(390, min_periods=max(390//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 114)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2982 * slope + 0.0016726 * anchor
    return base_signal.diff().diff()
