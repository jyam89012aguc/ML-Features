"""83 asset turnover decay base features 376-450 â€” Pipeline 1a-HF Grade v3.

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

def f83_atd_376_struct_v376(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=156, w2=185, w3=631, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(185, min_periods=max(185//3, 2)).mean()
    noise = impulse.abs().rolling(631, min_periods=max(631//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.19375 + 0.0040577 * anchor

def f83_atd_377_struct_v377(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=163, w2=196, w3=644, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 163)
    acceleration = _rolling_slope(velocity, 196)
    curvature = _rolling_slope(acceleration, 644)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1486 * acceleration + 0.0040578 * anchor

def f83_atd_378_struct_v378(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=170, w2=207, w3=657, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(170, min_periods=max(170//3, 2)).mean(), upside.rolling(207, min_periods=max(207//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.2225 + 0.0040579 * anchor

def f83_atd_379_struct_v379(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=177, w2=218, w3=670, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(218, min_periods=max(218//3, 2)).max()
    rebound = x - x.rolling(177, min_periods=max(177//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1638 * _rolling_slope(draw, 670) + 0.004058 * anchor

def f83_atd_380_struct_v380(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=184, w2=229, w3=683, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 184)
    baseline = trend.rolling(229, min_periods=max(229//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(683, min_periods=max(683//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.25125 + 0.0040581 * anchor

def f83_atd_381_struct_v381(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=191, w2=240, w3=696, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 191)
    slow = _rolling_slope(x, 240)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.265625 + 0.0040582 * anchor

def f83_atd_382_struct_v382(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=198, w2=251, w3=709, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(251, min_periods=max(251//3, 2)).max()
    trough = x.rolling(198, min_periods=max(198//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.28 + 0.0040583 * anchor

def f83_atd_383_struct_v383(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=205, w2=262, w3=722, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(262, min_periods=max(262//3, 2)).rank(pct=True)
    persistence = change.rolling(722, min_periods=max(722//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1942 * persistence + 0.0040584 * anchor

def f83_atd_384_struct_v384(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=212, w2=273, w3=735, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(212, min_periods=max(212//3, 2)).std()
    vol_slow = ret.rolling(273, min_periods=max(273//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.30875 + 0.0040585 * anchor

def f83_atd_385_struct_v385(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=219, w2=284, w3=748, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(284, min_periods=max(284//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 219)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2094 * slope + 0.0040586 * anchor

def f83_atd_386_struct_v386(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=226, w2=295, w3=761, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(295, min_periods=max(295//3, 2)).mean()
    noise = impulse.abs().rolling(761, min_periods=max(761//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.3375 + 0.0040587 * anchor

def f83_atd_387_struct_v387(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=233, w2=306, w3=17, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 233)
    acceleration = _rolling_slope(velocity, 306)
    curvature = _rolling_slope(acceleration, 17)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2246 * acceleration + 0.0040588 * anchor

def f83_atd_388_struct_v388(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=240, w2=317, w3=30, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(240, min_periods=max(240//3, 2)).mean(), upside.rolling(317, min_periods=max(317//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(30) * 1.36625 + 0.0040589 * anchor

def f83_atd_389_struct_v389(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=247, w2=328, w3=43, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(328, min_periods=max(328//3, 2)).max()
    rebound = x - x.rolling(247, min_periods=max(247//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2398 * _rolling_slope(draw, 43) + 0.004059 * anchor

def f83_atd_390_struct_v390(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=254, w2=339, w3=56, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 254)
    baseline = trend.rolling(339, min_periods=max(339//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(56, min_periods=max(56//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.395 + 0.0040591 * anchor

def f83_atd_391_struct_v391(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=10, w2=350, w3=69, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 10)
    slow = _rolling_slope(x, 350)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=69, adjust=False).mean() * 1.409375 + 0.0040592 * anchor

def f83_atd_392_struct_v392(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=17, w2=361, w3=82, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(361, min_periods=max(361//3, 2)).max()
    trough = x.rolling(17, min_periods=max(17//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.42375 + 0.0040593 * anchor

def f83_atd_393_struct_v393(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=24, w2=372, w3=95, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(24)
    rank = change.rolling(372, min_periods=max(372//3, 2)).rank(pct=True)
    persistence = change.rolling(95, min_periods=max(95//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2702 * persistence + 0.0040594 * anchor

def f83_atd_394_struct_v394(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=31, w2=383, w3=108, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(31, min_periods=max(31//3, 2)).std()
    vol_slow = ret.rolling(383, min_periods=max(383//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.4525 + 0.0040595 * anchor

def f83_atd_395_struct_v395(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=38, w2=394, w3=121, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(394, min_periods=max(394//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 38)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2854 * slope + 0.0040596 * anchor

def f83_atd_396_struct_v396(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=45, w2=405, w3=134, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(45)
    drag = impulse.rolling(405, min_periods=max(405//3, 2)).mean()
    noise = impulse.abs().rolling(134, min_periods=max(134//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.48125 + 0.0040597 * anchor

def f83_atd_397_struct_v397(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=52, w2=416, w3=147, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 52)
    acceleration = _rolling_slope(velocity, 416)
    curvature = _rolling_slope(acceleration, 147)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3006 * acceleration + 0.0040598 * anchor

def f83_atd_398_struct_v398(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=59, w2=427, w3=160, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(59, min_periods=max(59//3, 2)).mean(), upside.rolling(427, min_periods=max(427//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.51 + 0.0040599 * anchor

def f83_atd_399_struct_v399(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=66, w2=438, w3=173, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(438, min_periods=max(438//3, 2)).max()
    rebound = x - x.rolling(66, min_periods=max(66//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3158 * _rolling_slope(draw, 173) + 0.00406 * anchor

def f83_atd_400_struct_v400(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=73, w2=449, w3=186, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 73)
    baseline = trend.rolling(449, min_periods=max(449//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(186, min_periods=max(186//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.53875 + 0.0040601 * anchor

def f83_atd_401_struct_v401(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=80, w2=460, w3=199, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 80)
    slow = _rolling_slope(x, 460)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=199, adjust=False).mean() * 1.553125 + 0.0040602 * anchor

def f83_atd_402_struct_v402(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=87, w2=471, w3=212, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(471, min_periods=max(471//3, 2)).max()
    trough = x.rolling(87, min_periods=max(87//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.5675 + 0.0040603 * anchor

def f83_atd_403_struct_v403(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=94, w2=482, w3=225, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(94)
    rank = change.rolling(482, min_periods=max(482//3, 2)).rank(pct=True)
    persistence = change.rolling(225, min_periods=max(225//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3462 * persistence + 0.0040604 * anchor

def f83_atd_404_struct_v404(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=101, w2=493, w3=238, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(101, min_periods=max(101//3, 2)).std()
    vol_slow = ret.rolling(493, min_periods=max(493//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.59625 + 0.0040605 * anchor

def f83_atd_405_struct_v405(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=108, w2=504, w3=251, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(504, min_periods=max(504//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 108)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3614 * slope + 0.0040606 * anchor

def f83_atd_406_struct_v406(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=115, w2=12, w3=264, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(115)
    drag = impulse.rolling(12, min_periods=max(12//3, 2)).mean()
    noise = impulse.abs().rolling(264, min_periods=max(264//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.851875 + 0.0040607 * anchor

def f83_atd_407_struct_v407(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=122, w2=23, w3=277, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 122)
    acceleration = _rolling_slope(velocity, 23)
    curvature = _rolling_slope(acceleration, 277)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3766 * acceleration + 0.0040608 * anchor

def f83_atd_408_struct_v408(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=129, w2=34, w3=290, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(129, min_periods=max(129//3, 2)).mean(), upside.rolling(34, min_periods=max(34//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.880625 + 0.0040609 * anchor

def f83_atd_409_struct_v409(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=136, w2=45, w3=303, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(45, min_periods=max(45//3, 2)).max()
    rebound = x - x.rolling(136, min_periods=max(136//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3918 * _rolling_slope(draw, 303) + 0.004061 * anchor

def f83_atd_410_struct_v410(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=143, w2=56, w3=316, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 143)
    baseline = trend.rolling(56, min_periods=max(56//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(316, min_periods=max(316//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.909375 + 0.0040611 * anchor

def f83_atd_411_struct_v411(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=150, w2=67, w3=329, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 150)
    slow = _rolling_slope(x, 67)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.92375 + 0.0040612 * anchor

def f83_atd_412_struct_v412(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=157, w2=78, w3=342, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(78, min_periods=max(78//3, 2)).max()
    trough = x.rolling(157, min_periods=max(157//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.938125 + 0.0040613 * anchor

def f83_atd_413_struct_v413(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=164, w2=89, w3=355, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(89, min_periods=max(89//3, 2)).rank(pct=True)
    persistence = change.rolling(355, min_periods=max(355//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0458 * persistence + 0.0040614 * anchor

def f83_atd_414_struct_v414(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=171, w2=100, w3=368, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(171, min_periods=max(171//3, 2)).std()
    vol_slow = ret.rolling(100, min_periods=max(100//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.966875 + 0.0040615 * anchor

def f83_atd_415_struct_v415(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=178, w2=111, w3=381, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(111, min_periods=max(111//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 178)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.061 * slope + 0.0040616 * anchor

def f83_atd_416_struct_v416(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=185, w2=122, w3=394, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(122, min_periods=max(122//3, 2)).mean()
    noise = impulse.abs().rolling(394, min_periods=max(394//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.995625 + 0.0040617 * anchor

def f83_atd_417_struct_v417(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=192, w2=133, w3=407, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 192)
    acceleration = _rolling_slope(velocity, 133)
    curvature = _rolling_slope(acceleration, 407)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0762 * acceleration + 0.0040618 * anchor

def f83_atd_418_struct_v418(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=199, w2=144, w3=420, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(199, min_periods=max(199//3, 2)).mean(), upside.rolling(144, min_periods=max(144//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.024375 + 0.0040619 * anchor

def f83_atd_419_struct_v419(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=206, w2=155, w3=433, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(155, min_periods=max(155//3, 2)).max()
    rebound = x - x.rolling(206, min_periods=max(206//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0914 * _rolling_slope(draw, 433) + 0.004062 * anchor

def f83_atd_420_struct_v420(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=213, w2=166, w3=446, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 213)
    baseline = trend.rolling(166, min_periods=max(166//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(446, min_periods=max(446//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.053125 + 0.0040621 * anchor

def f83_atd_421_struct_v421(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=220, w2=177, w3=459, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 220)
    slow = _rolling_slope(x, 177)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.0675 + 0.0040622 * anchor

def f83_atd_422_struct_v422(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=227, w2=188, w3=472, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(188, min_periods=max(188//3, 2)).max()
    trough = x.rolling(227, min_periods=max(227//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.081875 + 0.0040623 * anchor

def f83_atd_423_struct_v423(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=234, w2=199, w3=485, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(199, min_periods=max(199//3, 2)).rank(pct=True)
    persistence = change.rolling(485, min_periods=max(485//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1218 * persistence + 0.0040624 * anchor

def f83_atd_424_struct_v424(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=241, w2=210, w3=498, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(241, min_periods=max(241//3, 2)).std()
    vol_slow = ret.rolling(210, min_periods=max(210//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.110625 + 0.0040625 * anchor

def f83_atd_425_struct_v425(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=248, w2=221, w3=511, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(221, min_periods=max(221//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 248)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.137 * slope + 0.0040626 * anchor

def f83_atd_426_struct_v426(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=255, w2=232, w3=524, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(232, min_periods=max(232//3, 2)).mean()
    noise = impulse.abs().rolling(524, min_periods=max(524//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.139375 + 0.0040627 * anchor

def f83_atd_427_struct_v427(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=11, w2=243, w3=537, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 11)
    acceleration = _rolling_slope(velocity, 243)
    curvature = _rolling_slope(acceleration, 537)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1522 * acceleration + 0.0040628 * anchor

def f83_atd_428_struct_v428(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=18, w2=254, w3=550, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(18, min_periods=max(18//3, 2)).mean(), upside.rolling(254, min_periods=max(254//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.168125 + 0.0040629 * anchor

def f83_atd_429_struct_v429(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=25, w2=265, w3=563, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(265, min_periods=max(265//3, 2)).max()
    rebound = x - x.rolling(25, min_periods=max(25//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1674 * _rolling_slope(draw, 563) + 0.004063 * anchor

def f83_atd_430_struct_v430(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=32, w2=276, w3=576, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 32)
    baseline = trend.rolling(276, min_periods=max(276//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(576, min_periods=max(576//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.196875 + 0.0040631 * anchor

def f83_atd_431_struct_v431(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=39, w2=287, w3=589, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 39)
    slow = _rolling_slope(x, 287)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.21125 + 0.0040632 * anchor

def f83_atd_432_struct_v432(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=46, w2=298, w3=602, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(298, min_periods=max(298//3, 2)).max()
    trough = x.rolling(46, min_periods=max(46//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.225625 + 0.0040633 * anchor

def f83_atd_433_struct_v433(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=53, w2=309, w3=615, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(53)
    rank = change.rolling(309, min_periods=max(309//3, 2)).rank(pct=True)
    persistence = change.rolling(615, min_periods=max(615//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1978 * persistence + 0.0040634 * anchor

def f83_atd_434_struct_v434(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=60, w2=320, w3=628, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(60, min_periods=max(60//3, 2)).std()
    vol_slow = ret.rolling(320, min_periods=max(320//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.254375 + 0.0040635 * anchor

def f83_atd_435_struct_v435(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=67, w2=331, w3=641, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(331, min_periods=max(331//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 67)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.213 * slope + 0.0040636 * anchor

def f83_atd_436_struct_v436(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=74, w2=342, w3=654, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(74)
    drag = impulse.rolling(342, min_periods=max(342//3, 2)).mean()
    noise = impulse.abs().rolling(654, min_periods=max(654//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.283125 + 0.0040637 * anchor

def f83_atd_437_struct_v437(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=81, w2=353, w3=667, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 81)
    acceleration = _rolling_slope(velocity, 353)
    curvature = _rolling_slope(acceleration, 667)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2282 * acceleration + 0.0040638 * anchor

def f83_atd_438_struct_v438(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=88, w2=364, w3=680, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(88, min_periods=max(88//3, 2)).mean(), upside.rolling(364, min_periods=max(364//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.311875 + 0.0040639 * anchor

def f83_atd_439_struct_v439(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=95, w2=375, w3=693, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(375, min_periods=max(375//3, 2)).max()
    rebound = x - x.rolling(95, min_periods=max(95//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2434 * _rolling_slope(draw, 693) + 0.004064 * anchor

def f83_atd_440_struct_v440(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=102, w2=386, w3=706, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 102)
    baseline = trend.rolling(386, min_periods=max(386//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(706, min_periods=max(706//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.340625 + 0.0040641 * anchor

def f83_atd_441_struct_v441(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=109, w2=397, w3=719, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 109)
    slow = _rolling_slope(x, 397)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.355 + 0.0040642 * anchor

def f83_atd_442_struct_v442(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=116, w2=408, w3=732, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(408, min_periods=max(408//3, 2)).max()
    trough = x.rolling(116, min_periods=max(116//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.369375 + 0.0040643 * anchor

def f83_atd_443_struct_v443(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=123, w2=419, w3=745, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(123)
    rank = change.rolling(419, min_periods=max(419//3, 2)).rank(pct=True)
    persistence = change.rolling(745, min_periods=max(745//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2738 * persistence + 0.0040644 * anchor

def f83_atd_444_struct_v444(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=130, w2=430, w3=758, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(130, min_periods=max(130//3, 2)).std()
    vol_slow = ret.rolling(430, min_periods=max(430//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.398125 + 0.0040645 * anchor

def f83_atd_445_struct_v445(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=137, w2=441, w3=771, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(441, min_periods=max(441//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 137)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.289 * slope + 0.0040646 * anchor

def f83_atd_446_struct_v446(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=144, w2=452, w3=27, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(452, min_periods=max(452//3, 2)).mean()
    noise = impulse.abs().rolling(27, min_periods=max(27//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.426875 + 0.0040647 * anchor

def f83_atd_447_struct_v447(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=151, w2=463, w3=40, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 151)
    acceleration = _rolling_slope(velocity, 463)
    curvature = _rolling_slope(acceleration, 40)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3042 * acceleration + 0.0040648 * anchor

def f83_atd_448_struct_v448(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=158, w2=474, w3=53, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(158, min_periods=max(158//3, 2)).mean(), upside.rolling(474, min_periods=max(474//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(53) * 1.455625 + 0.0040649 * anchor

def f83_atd_449_struct_v449(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=165, w2=485, w3=66, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(485, min_periods=max(485//3, 2)).max()
    rebound = x - x.rolling(165, min_periods=max(165//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3194 * _rolling_slope(draw, 66) + 0.004065 * anchor

def f83_atd_450_struct_v450(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=172, w2=496, w3=79, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 172)
    baseline = trend.rolling(496, min_periods=max(496//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(79, min_periods=max(79//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.484375 + 0.0040651 * anchor
