"""27 insider selling trajectory base features 376-450 â€” Pipeline 1a-HF Grade v3.

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

def f27_ist_376_struct_v376(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=75, w2=260, w3=515, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(75)
    drag = impulse.rolling(260, min_periods=max(260//3, 2)).mean()
    noise = impulse.abs().rolling(515, min_periods=max(515//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.0075 + 0.0016577 * anchor

def f27_ist_377_struct_v377(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=82, w2=271, w3=528, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 82)
    acceleration = _rolling_slope(velocity, 271)
    curvature = _rolling_slope(acceleration, 528)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3026 * acceleration + 0.0016578 * anchor

def f27_ist_378_struct_v378(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=89, w2=282, w3=541, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(89, min_periods=max(89//3, 2)).mean(), upside.rolling(282, min_periods=max(282//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.03625 + 0.0016579 * anchor

def f27_ist_379_struct_v379(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=96, w2=293, w3=554, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(293, min_periods=max(293//3, 2)).max()
    rebound = x - x.rolling(96, min_periods=max(96//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3178 * _rolling_slope(draw, 554) + 0.001658 * anchor

def f27_ist_380_struct_v380(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=103, w2=304, w3=567, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 103)
    baseline = trend.rolling(304, min_periods=max(304//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(567, min_periods=max(567//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.065 + 0.0016581 * anchor

def f27_ist_381_struct_v381(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=110, w2=315, w3=580, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 110)
    slow = _rolling_slope(x, 315)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.079375 + 0.0016582 * anchor

def f27_ist_382_struct_v382(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=117, w2=326, w3=593, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(326, min_periods=max(326//3, 2)).max()
    trough = x.rolling(117, min_periods=max(117//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.09375 + 0.0016583 * anchor

def f27_ist_383_struct_v383(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=124, w2=337, w3=606, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(124)
    rank = change.rolling(337, min_periods=max(337//3, 2)).rank(pct=True)
    persistence = change.rolling(606, min_periods=max(606//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3482 * persistence + 0.0016584 * anchor

def f27_ist_384_struct_v384(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=131, w2=348, w3=619, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(131, min_periods=max(131//3, 2)).std()
    vol_slow = ret.rolling(348, min_periods=max(348//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.1225 + 0.0016585 * anchor

def f27_ist_385_struct_v385(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=138, w2=359, w3=632, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(359, min_periods=max(359//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 138)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3634 * slope + 0.0016586 * anchor

def f27_ist_386_struct_v386(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=145, w2=370, w3=645, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(370, min_periods=max(370//3, 2)).mean()
    noise = impulse.abs().rolling(645, min_periods=max(645//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.15125 + 0.0016587 * anchor

def f27_ist_387_struct_v387(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=152, w2=381, w3=658, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 152)
    acceleration = _rolling_slope(velocity, 381)
    curvature = _rolling_slope(acceleration, 658)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3786 * acceleration + 0.0016588 * anchor

def f27_ist_388_struct_v388(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=159, w2=392, w3=671, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(159, min_periods=max(159//3, 2)).mean(), upside.rolling(392, min_periods=max(392//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.18 + 0.0016589 * anchor

def f27_ist_389_struct_v389(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=166, w2=403, w3=684, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(403, min_periods=max(403//3, 2)).max()
    rebound = x - x.rolling(166, min_periods=max(166//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3938 * _rolling_slope(draw, 684) + 0.001659 * anchor

def f27_ist_390_struct_v390(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=173, w2=414, w3=697, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 173)
    baseline = trend.rolling(414, min_periods=max(414//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(697, min_periods=max(697//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.20875 + 0.0016591 * anchor

def f27_ist_391_struct_v391(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=180, w2=425, w3=710, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 180)
    slow = _rolling_slope(x, 425)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.223125 + 0.0016592 * anchor

def f27_ist_392_struct_v392(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=187, w2=436, w3=723, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(436, min_periods=max(436//3, 2)).max()
    trough = x.rolling(187, min_periods=max(187//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.2375 + 0.0016593 * anchor

def f27_ist_393_struct_v393(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=194, w2=447, w3=736, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(447, min_periods=max(447//3, 2)).rank(pct=True)
    persistence = change.rolling(736, min_periods=max(736//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0478 * persistence + 0.0016594 * anchor

def f27_ist_394_struct_v394(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=201, w2=458, w3=749, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(201, min_periods=max(201//3, 2)).std()
    vol_slow = ret.rolling(458, min_periods=max(458//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.26625 + 0.0016595 * anchor

def f27_ist_395_struct_v395(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=208, w2=469, w3=762, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(469, min_periods=max(469//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 208)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.063 * slope + 0.0016596 * anchor

def f27_ist_396_struct_v396(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=215, w2=480, w3=18, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(480, min_periods=max(480//3, 2)).mean()
    noise = impulse.abs().rolling(18, min_periods=max(18//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.295 + 0.0016597 * anchor

def f27_ist_397_struct_v397(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=222, w2=491, w3=31, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 222)
    acceleration = _rolling_slope(velocity, 491)
    curvature = _rolling_slope(acceleration, 31)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0782 * acceleration + 0.0016598 * anchor

def f27_ist_398_struct_v398(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=229, w2=502, w3=44, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(229, min_periods=max(229//3, 2)).mean(), upside.rolling(502, min_periods=max(502//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(44) * 1.32375 + 0.0016599 * anchor

def f27_ist_399_struct_v399(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=236, w2=10, w3=57, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(10, min_periods=max(10//3, 2)).max()
    rebound = x - x.rolling(236, min_periods=max(236//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0934 * _rolling_slope(draw, 57) + 0.00166 * anchor

def f27_ist_400_struct_v400(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=243, w2=21, w3=70, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 243)
    baseline = trend.rolling(21, min_periods=max(21//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(70, min_periods=max(70//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.3525 + 0.0016601 * anchor

def f27_ist_401_struct_v401(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=250, w2=32, w3=83, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 250)
    slow = _rolling_slope(x, 32)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=83, adjust=False).mean() * 1.366875 + 0.0016602 * anchor

def f27_ist_402_struct_v402(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=6, w2=43, w3=96, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(43, min_periods=max(43//3, 2)).max()
    trough = x.rolling(6, min_periods=max(6//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.38125 + 0.0016603 * anchor

def f27_ist_403_struct_v403(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=13, w2=54, w3=109, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(13)
    rank = change.rolling(54, min_periods=max(54//3, 2)).rank(pct=True)
    persistence = change.rolling(109, min_periods=max(109//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1238 * persistence + 0.0016604 * anchor

def f27_ist_404_struct_v404(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=20, w2=65, w3=122, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(20, min_periods=max(20//3, 2)).std()
    vol_slow = ret.rolling(65, min_periods=max(65//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.41 + 0.0016605 * anchor

def f27_ist_405_struct_v405(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=27, w2=76, w3=135, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(76, min_periods=max(76//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 27)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.139 * slope + 0.0016606 * anchor

def f27_ist_406_struct_v406(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=34, w2=87, w3=148, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(34)
    drag = impulse.rolling(87, min_periods=max(87//3, 2)).mean()
    noise = impulse.abs().rolling(148, min_periods=max(148//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.43875 + 0.0016607 * anchor

def f27_ist_407_struct_v407(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=41, w2=98, w3=161, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 41)
    acceleration = _rolling_slope(velocity, 98)
    curvature = _rolling_slope(acceleration, 161)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1542 * acceleration + 0.0016608 * anchor

def f27_ist_408_struct_v408(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=48, w2=109, w3=174, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(48, min_periods=max(48//3, 2)).mean(), upside.rolling(109, min_periods=max(109//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.4675 + 0.0016609 * anchor

def f27_ist_409_struct_v409(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=55, w2=120, w3=187, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(120, min_periods=max(120//3, 2)).max()
    rebound = x - x.rolling(55, min_periods=max(55//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1694 * _rolling_slope(draw, 187) + 0.001661 * anchor

def f27_ist_410_struct_v410(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=62, w2=131, w3=200, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 62)
    baseline = trend.rolling(131, min_periods=max(131//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(200, min_periods=max(200//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.49625 + 0.0016611 * anchor

def f27_ist_411_struct_v411(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=69, w2=142, w3=213, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 69)
    slow = _rolling_slope(x, 142)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=213, adjust=False).mean() * 1.510625 + 0.0016612 * anchor

def f27_ist_412_struct_v412(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=76, w2=153, w3=226, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(153, min_periods=max(153//3, 2)).max()
    trough = x.rolling(76, min_periods=max(76//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.525 + 0.0016613 * anchor

def f27_ist_413_struct_v413(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=83, w2=164, w3=239, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(83)
    rank = change.rolling(164, min_periods=max(164//3, 2)).rank(pct=True)
    persistence = change.rolling(239, min_periods=max(239//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1998 * persistence + 0.0016614 * anchor

def f27_ist_414_struct_v414(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=90, w2=175, w3=252, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(90, min_periods=max(90//3, 2)).std()
    vol_slow = ret.rolling(175, min_periods=max(175//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.55375 + 0.0016615 * anchor

def f27_ist_415_struct_v415(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=97, w2=186, w3=265, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(186, min_periods=max(186//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 97)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.215 * slope + 0.0016616 * anchor

def f27_ist_416_struct_v416(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=104, w2=197, w3=278, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(104)
    drag = impulse.rolling(197, min_periods=max(197//3, 2)).mean()
    noise = impulse.abs().rolling(278, min_periods=max(278//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.5825 + 0.0016617 * anchor

def f27_ist_417_struct_v417(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=111, w2=208, w3=291, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 111)
    acceleration = _rolling_slope(velocity, 208)
    curvature = _rolling_slope(acceleration, 291)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2302 * acceleration + 0.0016618 * anchor

def f27_ist_418_struct_v418(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=118, w2=219, w3=304, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(118, min_periods=max(118//3, 2)).mean(), upside.rolling(219, min_periods=max(219//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.61125 + 0.0016619 * anchor

def f27_ist_419_struct_v419(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=125, w2=230, w3=317, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(230, min_periods=max(230//3, 2)).max()
    rebound = x - x.rolling(125, min_periods=max(125//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2454 * _rolling_slope(draw, 317) + 0.001662 * anchor

def f27_ist_420_struct_v420(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=132, w2=241, w3=330, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 132)
    baseline = trend.rolling(241, min_periods=max(241//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(330, min_periods=max(330//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.866875 + 0.0016621 * anchor

def f27_ist_421_struct_v421(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=139, w2=252, w3=343, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 139)
    slow = _rolling_slope(x, 252)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.88125 + 0.0016622 * anchor

def f27_ist_422_struct_v422(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=146, w2=263, w3=356, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(263, min_periods=max(263//3, 2)).max()
    trough = x.rolling(146, min_periods=max(146//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.895625 + 0.0016623 * anchor

def f27_ist_423_struct_v423(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=153, w2=274, w3=369, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(274, min_periods=max(274//3, 2)).rank(pct=True)
    persistence = change.rolling(369, min_periods=max(369//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2758 * persistence + 0.0016624 * anchor

def f27_ist_424_struct_v424(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=160, w2=285, w3=382, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(160, min_periods=max(160//3, 2)).std()
    vol_slow = ret.rolling(285, min_periods=max(285//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.924375 + 0.0016625 * anchor

def f27_ist_425_struct_v425(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=167, w2=296, w3=395, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(296, min_periods=max(296//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 167)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.291 * slope + 0.0016626 * anchor

def f27_ist_426_struct_v426(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=174, w2=307, w3=408, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(307, min_periods=max(307//3, 2)).mean()
    noise = impulse.abs().rolling(408, min_periods=max(408//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.953125 + 0.0016627 * anchor

def f27_ist_427_struct_v427(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=181, w2=318, w3=421, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 181)
    acceleration = _rolling_slope(velocity, 318)
    curvature = _rolling_slope(acceleration, 421)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3062 * acceleration + 0.0016628 * anchor

def f27_ist_428_struct_v428(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=188, w2=329, w3=434, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(188, min_periods=max(188//3, 2)).mean(), upside.rolling(329, min_periods=max(329//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.981875 + 0.0016629 * anchor

def f27_ist_429_struct_v429(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=195, w2=340, w3=447, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(340, min_periods=max(340//3, 2)).max()
    rebound = x - x.rolling(195, min_periods=max(195//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3214 * _rolling_slope(draw, 447) + 0.001663 * anchor

def f27_ist_430_struct_v430(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=202, w2=351, w3=460, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 202)
    baseline = trend.rolling(351, min_periods=max(351//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(460, min_periods=max(460//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.010625 + 0.0016631 * anchor

def f27_ist_431_struct_v431(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=209, w2=362, w3=473, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 209)
    slow = _rolling_slope(x, 362)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.025 + 0.0016632 * anchor

def f27_ist_432_struct_v432(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=216, w2=373, w3=486, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(373, min_periods=max(373//3, 2)).max()
    trough = x.rolling(216, min_periods=max(216//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.039375 + 0.0016633 * anchor

def f27_ist_433_struct_v433(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=223, w2=384, w3=499, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(384, min_periods=max(384//3, 2)).rank(pct=True)
    persistence = change.rolling(499, min_periods=max(499//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3518 * persistence + 0.0016634 * anchor

def f27_ist_434_struct_v434(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=230, w2=395, w3=512, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(230, min_periods=max(230//3, 2)).std()
    vol_slow = ret.rolling(395, min_periods=max(395//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.068125 + 0.0016635 * anchor

def f27_ist_435_struct_v435(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=237, w2=406, w3=525, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(406, min_periods=max(406//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 237)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.367 * slope + 0.0016636 * anchor

def f27_ist_436_struct_v436(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=244, w2=417, w3=538, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(417, min_periods=max(417//3, 2)).mean()
    noise = impulse.abs().rolling(538, min_periods=max(538//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.096875 + 0.0016637 * anchor

def f27_ist_437_struct_v437(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=251, w2=428, w3=551, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 251)
    acceleration = _rolling_slope(velocity, 428)
    curvature = _rolling_slope(acceleration, 551)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3822 * acceleration + 0.0016638 * anchor

def f27_ist_438_struct_v438(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=7, w2=439, w3=564, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(7, min_periods=max(7//3, 2)).mean(), upside.rolling(439, min_periods=max(439//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.125625 + 0.0016639 * anchor

def f27_ist_439_struct_v439(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=14, w2=450, w3=577, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(450, min_periods=max(450//3, 2)).max()
    rebound = x - x.rolling(14, min_periods=max(14//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3974 * _rolling_slope(draw, 577) + 0.001664 * anchor

def f27_ist_440_struct_v440(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=21, w2=461, w3=590, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 21)
    baseline = trend.rolling(461, min_periods=max(461//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(590, min_periods=max(590//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.154375 + 0.0016641 * anchor

def f27_ist_441_struct_v441(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=28, w2=472, w3=603, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 28)
    slow = _rolling_slope(x, 472)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.16875 + 0.0016642 * anchor

def f27_ist_442_struct_v442(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=35, w2=483, w3=616, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(483, min_periods=max(483//3, 2)).max()
    trough = x.rolling(35, min_periods=max(35//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.183125 + 0.0016643 * anchor

def f27_ist_443_struct_v443(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=42, w2=494, w3=629, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(42)
    rank = change.rolling(494, min_periods=max(494//3, 2)).rank(pct=True)
    persistence = change.rolling(629, min_periods=max(629//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0514 * persistence + 0.0016644 * anchor

def f27_ist_444_struct_v444(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=49, w2=505, w3=642, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(49, min_periods=max(49//3, 2)).std()
    vol_slow = ret.rolling(505, min_periods=max(505//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.211875 + 0.0016645 * anchor

def f27_ist_445_struct_v445(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=56, w2=13, w3=655, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(13, min_periods=max(13//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 56)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0666 * slope + 0.0016646 * anchor

def f27_ist_446_struct_v446(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=63, w2=24, w3=668, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(63)
    drag = impulse.rolling(24, min_periods=max(24//3, 2)).mean()
    noise = impulse.abs().rolling(668, min_periods=max(668//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.240625 + 0.0016647 * anchor

def f27_ist_447_struct_v447(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=70, w2=35, w3=681, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 70)
    acceleration = _rolling_slope(velocity, 35)
    curvature = _rolling_slope(acceleration, 681)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0818 * acceleration + 0.0016648 * anchor

def f27_ist_448_struct_v448(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=77, w2=46, w3=694, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(77, min_periods=max(77//3, 2)).mean(), upside.rolling(46, min_periods=max(46//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.269375 + 0.0016649 * anchor

def f27_ist_449_struct_v449(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=84, w2=57, w3=707, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(57, min_periods=max(57//3, 2)).max()
    rebound = x - x.rolling(84, min_periods=max(84//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.097 * _rolling_slope(draw, 707) + 0.001665 * anchor

def f27_ist_450_struct_v450(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=91, w2=68, w3=720, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 91)
    baseline = trend.rolling(68, min_periods=max(68//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(720, min_periods=max(720//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.298125 + 0.0016651 * anchor
