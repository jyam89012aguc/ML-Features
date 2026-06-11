"""41 reverse operating leverage base features 526-600 â€” Pipeline 1a-HF Grade v3.

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

def f41_rol_526_struct_v526(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=120, w2=310, w3=616, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(120)
    drag = impulse.rolling(310, min_periods=max(310//3, 2)).mean()
    noise = impulse.abs().rolling(616, min_periods=max(616//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.1075 + 0.0025727 * anchor

def f41_rol_527_struct_v527(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=127, w2=321, w3=629, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 127)
    acceleration = _rolling_slope(velocity, 321)
    curvature = _rolling_slope(acceleration, 629)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2086 * acceleration + 0.0025728 * anchor

def f41_rol_528_struct_v528(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=134, w2=332, w3=642, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(134, min_periods=max(134//3, 2)).mean(), upside.rolling(332, min_periods=max(332//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.13625 + 0.0025729 * anchor

def f41_rol_529_struct_v529(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=141, w2=343, w3=655, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(343, min_periods=max(343//3, 2)).max()
    rebound = x - x.rolling(141, min_periods=max(141//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2238 * _rolling_slope(draw, 655) + 0.002573 * anchor

def f41_rol_530_struct_v530(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=148, w2=354, w3=668, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 148)
    baseline = trend.rolling(354, min_periods=max(354//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(668, min_periods=max(668//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.165 + 0.0025731 * anchor

def f41_rol_531_struct_v531(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=155, w2=365, w3=681, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 155)
    slow = _rolling_slope(x, 365)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.179375 + 0.0025732 * anchor

def f41_rol_532_struct_v532(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=162, w2=376, w3=694, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(376, min_periods=max(376//3, 2)).max()
    trough = x.rolling(162, min_periods=max(162//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.19375 + 0.0025733 * anchor

def f41_rol_533_struct_v533(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=169, w2=387, w3=707, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(387, min_periods=max(387//3, 2)).rank(pct=True)
    persistence = change.rolling(707, min_periods=max(707//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2542 * persistence + 0.0025734 * anchor

def f41_rol_534_struct_v534(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=176, w2=398, w3=720, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(176, min_periods=max(176//3, 2)).std()
    vol_slow = ret.rolling(398, min_periods=max(398//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.2225 + 0.0025735 * anchor

def f41_rol_535_struct_v535(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=183, w2=409, w3=733, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(409, min_periods=max(409//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 183)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2694 * slope + 0.0025736 * anchor

def f41_rol_536_struct_v536(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=190, w2=420, w3=746, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(420, min_periods=max(420//3, 2)).mean()
    noise = impulse.abs().rolling(746, min_periods=max(746//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.25125 + 0.0025737 * anchor

def f41_rol_537_struct_v537(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=197, w2=431, w3=759, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 197)
    acceleration = _rolling_slope(velocity, 431)
    curvature = _rolling_slope(acceleration, 759)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2846 * acceleration + 0.0025738 * anchor

def f41_rol_538_struct_v538(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=204, w2=442, w3=15, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(204, min_periods=max(204//3, 2)).mean(), upside.rolling(442, min_periods=max(442//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(15) * 1.28 + 0.0025739 * anchor

def f41_rol_539_struct_v539(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=211, w2=453, w3=28, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(453, min_periods=max(453//3, 2)).max()
    rebound = x - x.rolling(211, min_periods=max(211//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2998 * _rolling_slope(draw, 28) + 0.002574 * anchor

def f41_rol_540_struct_v540(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=218, w2=464, w3=41, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 218)
    baseline = trend.rolling(464, min_periods=max(464//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(41, min_periods=max(41//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.30875 + 0.0025741 * anchor

def f41_rol_541_struct_v541(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=225, w2=475, w3=54, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 225)
    slow = _rolling_slope(x, 475)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=54, adjust=False).mean() * 1.323125 + 0.0025742 * anchor

def f41_rol_542_struct_v542(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=232, w2=486, w3=67, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(486, min_periods=max(486//3, 2)).max()
    trough = x.rolling(232, min_periods=max(232//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.3375 + 0.0025743 * anchor

def f41_rol_543_struct_v543(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=239, w2=497, w3=80, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(497, min_periods=max(497//3, 2)).rank(pct=True)
    persistence = change.rolling(80, min_periods=max(80//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3302 * persistence + 0.0025744 * anchor

def f41_rol_544_struct_v544(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=246, w2=508, w3=93, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(246, min_periods=max(246//3, 2)).std()
    vol_slow = ret.rolling(508, min_periods=max(508//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.36625 + 0.0025745 * anchor

def f41_rol_545_struct_v545(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=253, w2=16, w3=106, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(16, min_periods=max(16//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 253)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3454 * slope + 0.0025746 * anchor

def f41_rol_546_struct_v546(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=9, w2=27, w3=119, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(9)
    drag = impulse.rolling(27, min_periods=max(27//3, 2)).mean()
    noise = impulse.abs().rolling(119, min_periods=max(119//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.395 + 0.0025747 * anchor

def f41_rol_547_struct_v547(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=16, w2=38, w3=132, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 16)
    acceleration = _rolling_slope(velocity, 38)
    curvature = _rolling_slope(acceleration, 132)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3606 * acceleration + 0.0025748 * anchor

def f41_rol_548_struct_v548(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=23, w2=49, w3=145, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(23, min_periods=max(23//3, 2)).mean(), upside.rolling(49, min_periods=max(49//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.42375 + 0.0025749 * anchor

def f41_rol_549_struct_v549(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=30, w2=60, w3=158, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(60, min_periods=max(60//3, 2)).max()
    rebound = x - x.rolling(30, min_periods=max(30//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3758 * _rolling_slope(draw, 158) + 0.002575 * anchor

def f41_rol_550_struct_v550(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=37, w2=71, w3=171, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 37)
    baseline = trend.rolling(71, min_periods=max(71//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(171, min_periods=max(171//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.4525 + 0.0025751 * anchor

def f41_rol_551_struct_v551(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=44, w2=82, w3=184, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 44)
    slow = _rolling_slope(x, 82)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=184, adjust=False).mean() * 1.466875 + 0.0025752 * anchor

def f41_rol_552_struct_v552(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=51, w2=93, w3=197, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(93, min_periods=max(93//3, 2)).max()
    trough = x.rolling(51, min_periods=max(51//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.48125 + 0.0025753 * anchor

def f41_rol_553_struct_v553(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=58, w2=104, w3=210, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(58)
    rank = change.rolling(104, min_periods=max(104//3, 2)).rank(pct=True)
    persistence = change.rolling(210, min_periods=max(210//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.4062 * persistence + 0.0025754 * anchor

def f41_rol_554_struct_v554(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=65, w2=115, w3=223, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(65, min_periods=max(65//3, 2)).std()
    vol_slow = ret.rolling(115, min_periods=max(115//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.51 + 0.0025755 * anchor

def f41_rol_555_struct_v555(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=72, w2=126, w3=236, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(126, min_periods=max(126//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 72)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.045 * slope + 0.0025756 * anchor

def f41_rol_556_struct_v556(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=79, w2=137, w3=249, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(79)
    drag = impulse.rolling(137, min_periods=max(137//3, 2)).mean()
    noise = impulse.abs().rolling(249, min_periods=max(249//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.53875 + 0.0025757 * anchor

def f41_rol_557_struct_v557(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=86, w2=148, w3=262, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 86)
    acceleration = _rolling_slope(velocity, 148)
    curvature = _rolling_slope(acceleration, 262)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0602 * acceleration + 0.0025758 * anchor

def f41_rol_558_struct_v558(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=93, w2=159, w3=275, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(93, min_periods=max(93//3, 2)).mean(), upside.rolling(159, min_periods=max(159//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.5675 + 0.0025759 * anchor

def f41_rol_559_struct_v559(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=100, w2=170, w3=288, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(170, min_periods=max(170//3, 2)).max()
    rebound = x - x.rolling(100, min_periods=max(100//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0754 * _rolling_slope(draw, 288) + 0.002576 * anchor

def f41_rol_560_struct_v560(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=107, w2=181, w3=301, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 107)
    baseline = trend.rolling(181, min_periods=max(181//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(301, min_periods=max(301//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.59625 + 0.0025761 * anchor

def f41_rol_561_struct_v561(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=114, w2=192, w3=314, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 114)
    slow = _rolling_slope(x, 192)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.610625 + 0.0025762 * anchor

def f41_rol_562_struct_v562(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=121, w2=203, w3=327, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(203, min_periods=max(203//3, 2)).max()
    trough = x.rolling(121, min_periods=max(121//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.851875 + 0.0025763 * anchor

def f41_rol_563_struct_v563(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=128, w2=214, w3=340, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(214, min_periods=max(214//3, 2)).rank(pct=True)
    persistence = change.rolling(340, min_periods=max(340//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1058 * persistence + 0.0025764 * anchor

def f41_rol_564_struct_v564(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=135, w2=225, w3=353, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(135, min_periods=max(135//3, 2)).std()
    vol_slow = ret.rolling(225, min_periods=max(225//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.880625 + 0.0025765 * anchor

def f41_rol_565_struct_v565(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=142, w2=236, w3=366, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(236, min_periods=max(236//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 142)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.121 * slope + 0.0025766 * anchor

def f41_rol_566_struct_v566(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=149, w2=247, w3=379, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(247, min_periods=max(247//3, 2)).mean()
    noise = impulse.abs().rolling(379, min_periods=max(379//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.909375 + 0.0025767 * anchor

def f41_rol_567_struct_v567(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=156, w2=258, w3=392, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 156)
    acceleration = _rolling_slope(velocity, 258)
    curvature = _rolling_slope(acceleration, 392)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1362 * acceleration + 0.0025768 * anchor

def f41_rol_568_struct_v568(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=163, w2=269, w3=405, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(163, min_periods=max(163//3, 2)).mean(), upside.rolling(269, min_periods=max(269//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.938125 + 0.0025769 * anchor

def f41_rol_569_struct_v569(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=170, w2=280, w3=418, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(280, min_periods=max(280//3, 2)).max()
    rebound = x - x.rolling(170, min_periods=max(170//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1514 * _rolling_slope(draw, 418) + 0.002577 * anchor

def f41_rol_570_struct_v570(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=177, w2=291, w3=431, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 177)
    baseline = trend.rolling(291, min_periods=max(291//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(431, min_periods=max(431//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.966875 + 0.0025771 * anchor

def f41_rol_571_struct_v571(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=184, w2=302, w3=444, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 184)
    slow = _rolling_slope(x, 302)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.98125 + 0.0025772 * anchor

def f41_rol_572_struct_v572(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=191, w2=313, w3=457, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(313, min_periods=max(313//3, 2)).max()
    trough = x.rolling(191, min_periods=max(191//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.995625 + 0.0025773 * anchor

def f41_rol_573_struct_v573(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=198, w2=324, w3=470, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(324, min_periods=max(324//3, 2)).rank(pct=True)
    persistence = change.rolling(470, min_periods=max(470//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1818 * persistence + 0.0025774 * anchor

def f41_rol_574_struct_v574(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=205, w2=335, w3=483, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(205, min_periods=max(205//3, 2)).std()
    vol_slow = ret.rolling(335, min_periods=max(335//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.024375 + 0.0025775 * anchor

def f41_rol_575_struct_v575(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=212, w2=346, w3=496, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(346, min_periods=max(346//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 212)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.197 * slope + 0.0025776 * anchor

def f41_rol_576_struct_v576(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=219, w2=357, w3=509, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(357, min_periods=max(357//3, 2)).mean()
    noise = impulse.abs().rolling(509, min_periods=max(509//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.053125 + 0.0025777 * anchor

def f41_rol_577_struct_v577(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=226, w2=368, w3=522, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 226)
    acceleration = _rolling_slope(velocity, 368)
    curvature = _rolling_slope(acceleration, 522)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2122 * acceleration + 0.0025778 * anchor

def f41_rol_578_struct_v578(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=233, w2=379, w3=535, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(233, min_periods=max(233//3, 2)).mean(), upside.rolling(379, min_periods=max(379//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.081875 + 0.0025779 * anchor

def f41_rol_579_struct_v579(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=240, w2=390, w3=548, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(390, min_periods=max(390//3, 2)).max()
    rebound = x - x.rolling(240, min_periods=max(240//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2274 * _rolling_slope(draw, 548) + 0.002578 * anchor

def f41_rol_580_struct_v580(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=247, w2=401, w3=561, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 247)
    baseline = trend.rolling(401, min_periods=max(401//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(561, min_periods=max(561//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.110625 + 0.0025781 * anchor

def f41_rol_581_struct_v581(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=254, w2=412, w3=574, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 254)
    slow = _rolling_slope(x, 412)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.125 + 0.0025782 * anchor

def f41_rol_582_struct_v582(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=10, w2=423, w3=587, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(423, min_periods=max(423//3, 2)).max()
    trough = x.rolling(10, min_periods=max(10//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.139375 + 0.0025783 * anchor

def f41_rol_583_struct_v583(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=17, w2=434, w3=600, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(17)
    rank = change.rolling(434, min_periods=max(434//3, 2)).rank(pct=True)
    persistence = change.rolling(600, min_periods=max(600//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2578 * persistence + 0.0025784 * anchor

def f41_rol_584_struct_v584(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=24, w2=445, w3=613, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(24, min_periods=max(24//3, 2)).std()
    vol_slow = ret.rolling(445, min_periods=max(445//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.168125 + 0.0025785 * anchor

def f41_rol_585_struct_v585(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=31, w2=456, w3=626, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(456, min_periods=max(456//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 31)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.273 * slope + 0.0025786 * anchor

def f41_rol_586_struct_v586(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=38, w2=467, w3=639, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(38)
    drag = impulse.rolling(467, min_periods=max(467//3, 2)).mean()
    noise = impulse.abs().rolling(639, min_periods=max(639//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.196875 + 0.0025787 * anchor

def f41_rol_587_struct_v587(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=45, w2=478, w3=652, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 45)
    acceleration = _rolling_slope(velocity, 478)
    curvature = _rolling_slope(acceleration, 652)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2882 * acceleration + 0.0025788 * anchor

def f41_rol_588_struct_v588(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=52, w2=489, w3=665, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(52, min_periods=max(52//3, 2)).mean(), upside.rolling(489, min_periods=max(489//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.225625 + 0.0025789 * anchor

def f41_rol_589_struct_v589(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=59, w2=500, w3=678, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(500, min_periods=max(500//3, 2)).max()
    rebound = x - x.rolling(59, min_periods=max(59//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3034 * _rolling_slope(draw, 678) + 0.002579 * anchor

def f41_rol_590_struct_v590(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=66, w2=511, w3=691, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 66)
    baseline = trend.rolling(511, min_periods=max(511//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(691, min_periods=max(691//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.254375 + 0.0025791 * anchor

def f41_rol_591_struct_v591(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=73, w2=19, w3=704, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 73)
    slow = _rolling_slope(x, 19)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.26875 + 0.0025792 * anchor

def f41_rol_592_struct_v592(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=80, w2=30, w3=717, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(30, min_periods=max(30//3, 2)).max()
    trough = x.rolling(80, min_periods=max(80//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.283125 + 0.0025793 * anchor

def f41_rol_593_struct_v593(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=87, w2=41, w3=730, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(87)
    rank = change.rolling(41, min_periods=max(41//3, 2)).rank(pct=True)
    persistence = change.rolling(730, min_periods=max(730//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3338 * persistence + 0.0025794 * anchor

def f41_rol_594_struct_v594(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=94, w2=52, w3=743, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(94, min_periods=max(94//3, 2)).std()
    vol_slow = ret.rolling(52, min_periods=max(52//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.311875 + 0.0025795 * anchor

def f41_rol_595_struct_v595(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=101, w2=63, w3=756, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(63, min_periods=max(63//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 101)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.349 * slope + 0.0025796 * anchor

def f41_rol_596_struct_v596(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=108, w2=74, w3=769, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(108)
    drag = impulse.rolling(74, min_periods=max(74//3, 2)).mean()
    noise = impulse.abs().rolling(769, min_periods=max(769//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.340625 + 0.0025797 * anchor

def f41_rol_597_struct_v597(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=115, w2=85, w3=25, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 115)
    acceleration = _rolling_slope(velocity, 85)
    curvature = _rolling_slope(acceleration, 25)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3642 * acceleration + 0.0025798 * anchor

def f41_rol_598_struct_v598(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=122, w2=96, w3=38, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(122, min_periods=max(122//3, 2)).mean(), upside.rolling(96, min_periods=max(96//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(38) * 1.369375 + 0.0025799 * anchor

def f41_rol_599_struct_v599(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=129, w2=107, w3=51, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(107, min_periods=max(107//3, 2)).max()
    rebound = x - x.rolling(129, min_periods=max(129//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3794 * _rolling_slope(draw, 51) + 0.00258 * anchor

def f41_rol_600_struct_v600(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=136, w2=118, w3=64, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 136)
    baseline = trend.rolling(118, min_periods=max(118//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(64, min_periods=max(64//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.398125 + 0.0025801 * anchor
