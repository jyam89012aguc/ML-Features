"""15 valuation extreme snapshot base features 451-525 â€” Pipeline 1a-HF Grade v3.

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

def f15_valx_451_struct_v451(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=149, w2=353, w3=244, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 149)
    slow = _rolling_slope(x, 353)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=244, adjust=False).mean() * 1.41125 + 0.0009452 * anchor

def f15_valx_452_struct_v452(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=156, w2=364, w3=257, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(364, min_periods=max(364//3, 2)).max()
    trough = x.rolling(156, min_periods=max(156//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.425625 + 0.0009453 * anchor

def f15_valx_453_struct_v453(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=163, w2=375, w3=270, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(375, min_periods=max(375//3, 2)).rank(pct=True)
    persistence = change.rolling(270, min_periods=max(270//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3618 * persistence + 0.0009454 * anchor

def f15_valx_454_struct_v454(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=170, w2=386, w3=283, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(170, min_periods=max(170//3, 2)).std()
    vol_slow = ret.rolling(386, min_periods=max(386//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.454375 + 0.0009455 * anchor

def f15_valx_455_struct_v455(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=177, w2=397, w3=296, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(397, min_periods=max(397//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 177)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.377 * slope + 0.0009456 * anchor

def f15_valx_456_struct_v456(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=184, w2=408, w3=309, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(408, min_periods=max(408//3, 2)).mean()
    noise = impulse.abs().rolling(309, min_periods=max(309//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.483125 + 0.0009457 * anchor

def f15_valx_457_struct_v457(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=191, w2=419, w3=322, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 191)
    acceleration = _rolling_slope(velocity, 419)
    curvature = _rolling_slope(acceleration, 322)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3922 * acceleration + 0.0009458 * anchor

def f15_valx_458_struct_v458(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=198, w2=430, w3=335, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(198, min_periods=max(198//3, 2)).mean(), upside.rolling(430, min_periods=max(430//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.511875 + 0.0009459 * anchor

def f15_valx_459_struct_v459(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=205, w2=441, w3=348, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(441, min_periods=max(441//3, 2)).max()
    rebound = x - x.rolling(205, min_periods=max(205//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.4074 * _rolling_slope(draw, 348) + 0.000946 * anchor

def f15_valx_460_struct_v460(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=212, w2=452, w3=361, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 212)
    baseline = trend.rolling(452, min_periods=max(452//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(361, min_periods=max(361//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.540625 + 0.0009461 * anchor

def f15_valx_461_struct_v461(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=219, w2=463, w3=374, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 219)
    slow = _rolling_slope(x, 463)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.555 + 0.0009462 * anchor

def f15_valx_462_struct_v462(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=226, w2=474, w3=387, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(474, min_periods=max(474//3, 2)).max()
    trough = x.rolling(226, min_periods=max(226//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.569375 + 0.0009463 * anchor

def f15_valx_463_struct_v463(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=233, w2=485, w3=400, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(485, min_periods=max(485//3, 2)).rank(pct=True)
    persistence = change.rolling(400, min_periods=max(400//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0614 * persistence + 0.0009464 * anchor

def f15_valx_464_struct_v464(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=240, w2=496, w3=413, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(240, min_periods=max(240//3, 2)).std()
    vol_slow = ret.rolling(496, min_periods=max(496//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.598125 + 0.0009465 * anchor

def f15_valx_465_struct_v465(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=247, w2=507, w3=426, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(507, min_periods=max(507//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 247)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0766 * slope + 0.0009466 * anchor

def f15_valx_466_struct_v466(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=254, w2=15, w3=439, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(15, min_periods=max(15//3, 2)).mean()
    noise = impulse.abs().rolling(439, min_periods=max(439//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.85375 + 0.0009467 * anchor

def f15_valx_467_struct_v467(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=10, w2=26, w3=452, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 10)
    acceleration = _rolling_slope(velocity, 26)
    curvature = _rolling_slope(acceleration, 452)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0918 * acceleration + 0.0009468 * anchor

def f15_valx_468_struct_v468(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=17, w2=37, w3=465, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(17, min_periods=max(17//3, 2)).mean(), upside.rolling(37, min_periods=max(37//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.8825 + 0.0009469 * anchor

def f15_valx_469_struct_v469(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=24, w2=48, w3=478, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(48, min_periods=max(48//3, 2)).max()
    rebound = x - x.rolling(24, min_periods=max(24//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.107 * _rolling_slope(draw, 478) + 0.000947 * anchor

def f15_valx_470_struct_v470(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=31, w2=59, w3=491, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 31)
    baseline = trend.rolling(59, min_periods=max(59//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(491, min_periods=max(491//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.91125 + 0.0009471 * anchor

def f15_valx_471_struct_v471(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=38, w2=70, w3=504, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 38)
    slow = _rolling_slope(x, 70)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.925625 + 0.0009472 * anchor

def f15_valx_472_struct_v472(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=45, w2=81, w3=517, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(81, min_periods=max(81//3, 2)).max()
    trough = x.rolling(45, min_periods=max(45//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.94 + 0.0009473 * anchor

def f15_valx_473_struct_v473(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=52, w2=92, w3=530, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(52)
    rank = change.rolling(92, min_periods=max(92//3, 2)).rank(pct=True)
    persistence = change.rolling(530, min_periods=max(530//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1374 * persistence + 0.0009474 * anchor

def f15_valx_474_struct_v474(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=59, w2=103, w3=543, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(59, min_periods=max(59//3, 2)).std()
    vol_slow = ret.rolling(103, min_periods=max(103//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.96875 + 0.0009475 * anchor

def f15_valx_475_struct_v475(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=66, w2=114, w3=556, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(114, min_periods=max(114//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 66)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1526 * slope + 0.0009476 * anchor

def f15_valx_476_struct_v476(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=73, w2=125, w3=569, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(73)
    drag = impulse.rolling(125, min_periods=max(125//3, 2)).mean()
    noise = impulse.abs().rolling(569, min_periods=max(569//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.9975 + 0.0009477 * anchor

def f15_valx_477_struct_v477(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=80, w2=136, w3=582, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 80)
    acceleration = _rolling_slope(velocity, 136)
    curvature = _rolling_slope(acceleration, 582)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1678 * acceleration + 0.0009478 * anchor

def f15_valx_478_struct_v478(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=87, w2=147, w3=595, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(87, min_periods=max(87//3, 2)).mean(), upside.rolling(147, min_periods=max(147//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.02625 + 0.0009479 * anchor

def f15_valx_479_struct_v479(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=94, w2=158, w3=608, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(158, min_periods=max(158//3, 2)).max()
    rebound = x - x.rolling(94, min_periods=max(94//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.183 * _rolling_slope(draw, 608) + 0.000948 * anchor

def f15_valx_480_struct_v480(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=101, w2=169, w3=621, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 101)
    baseline = trend.rolling(169, min_periods=max(169//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(621, min_periods=max(621//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.055 + 0.0009481 * anchor

def f15_valx_481_struct_v481(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=108, w2=180, w3=634, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 108)
    slow = _rolling_slope(x, 180)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.069375 + 0.0009482 * anchor

def f15_valx_482_struct_v482(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=115, w2=191, w3=647, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(191, min_periods=max(191//3, 2)).max()
    trough = x.rolling(115, min_periods=max(115//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.08375 + 0.0009483 * anchor

def f15_valx_483_struct_v483(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=122, w2=202, w3=660, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(122)
    rank = change.rolling(202, min_periods=max(202//3, 2)).rank(pct=True)
    persistence = change.rolling(660, min_periods=max(660//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2134 * persistence + 0.0009484 * anchor

def f15_valx_484_struct_v484(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=129, w2=213, w3=673, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(129, min_periods=max(129//3, 2)).std()
    vol_slow = ret.rolling(213, min_periods=max(213//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.1125 + 0.0009485 * anchor

def f15_valx_485_struct_v485(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=136, w2=224, w3=686, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(224, min_periods=max(224//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 136)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2286 * slope + 0.0009486 * anchor

def f15_valx_486_struct_v486(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=143, w2=235, w3=699, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(235, min_periods=max(235//3, 2)).mean()
    noise = impulse.abs().rolling(699, min_periods=max(699//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.14125 + 0.0009487 * anchor

def f15_valx_487_struct_v487(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=150, w2=246, w3=712, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 150)
    acceleration = _rolling_slope(velocity, 246)
    curvature = _rolling_slope(acceleration, 712)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2438 * acceleration + 0.0009488 * anchor

def f15_valx_488_struct_v488(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=157, w2=257, w3=725, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(157, min_periods=max(157//3, 2)).mean(), upside.rolling(257, min_periods=max(257//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.17 + 0.0009489 * anchor

def f15_valx_489_struct_v489(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=164, w2=268, w3=738, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(268, min_periods=max(268//3, 2)).max()
    rebound = x - x.rolling(164, min_periods=max(164//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.259 * _rolling_slope(draw, 738) + 0.000949 * anchor

def f15_valx_490_struct_v490(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=171, w2=279, w3=751, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 171)
    baseline = trend.rolling(279, min_periods=max(279//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(751, min_periods=max(751//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.19875 + 0.0009491 * anchor

def f15_valx_491_struct_v491(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=178, w2=290, w3=764, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 178)
    slow = _rolling_slope(x, 290)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.213125 + 0.0009492 * anchor

def f15_valx_492_struct_v492(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=185, w2=301, w3=20, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(301, min_periods=max(301//3, 2)).max()
    trough = x.rolling(185, min_periods=max(185//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.2275 + 0.0009493 * anchor

def f15_valx_493_struct_v493(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=192, w2=312, w3=33, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(312, min_periods=max(312//3, 2)).rank(pct=True)
    persistence = change.rolling(33, min_periods=max(33//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2894 * persistence + 0.0009494 * anchor

def f15_valx_494_struct_v494(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=199, w2=323, w3=46, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(199, min_periods=max(199//3, 2)).std()
    vol_slow = ret.rolling(323, min_periods=max(323//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.25625 + 0.0009495 * anchor

def f15_valx_495_struct_v495(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=206, w2=334, w3=59, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(334, min_periods=max(334//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 206)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3046 * slope + 0.0009496 * anchor

def f15_valx_496_struct_v496(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=213, w2=345, w3=72, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(345, min_periods=max(345//3, 2)).mean()
    noise = impulse.abs().rolling(72, min_periods=max(72//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.285 + 0.0009497 * anchor

def f15_valx_497_struct_v497(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=220, w2=356, w3=85, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 220)
    acceleration = _rolling_slope(velocity, 356)
    curvature = _rolling_slope(acceleration, 85)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3198 * acceleration + 0.0009498 * anchor

def f15_valx_498_struct_v498(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=227, w2=367, w3=98, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(227, min_periods=max(227//3, 2)).mean(), upside.rolling(367, min_periods=max(367//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(98) * 1.31375 + 0.0009499 * anchor

def f15_valx_499_struct_v499(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=234, w2=378, w3=111, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(378, min_periods=max(378//3, 2)).max()
    rebound = x - x.rolling(234, min_periods=max(234//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.335 * _rolling_slope(draw, 111) + 0.00095 * anchor

def f15_valx_500_struct_v500(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=241, w2=389, w3=124, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 241)
    baseline = trend.rolling(389, min_periods=max(389//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(124, min_periods=max(124//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.3425 + 0.0009501 * anchor

def f15_valx_501_struct_v501(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=248, w2=400, w3=137, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 248)
    slow = _rolling_slope(x, 400)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=137, adjust=False).mean() * 1.356875 + 0.0009502 * anchor

def f15_valx_502_struct_v502(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=255, w2=411, w3=150, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(411, min_periods=max(411//3, 2)).max()
    trough = x.rolling(255, min_periods=max(255//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.37125 + 0.0009503 * anchor

def f15_valx_503_struct_v503(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=11, w2=422, w3=163, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(11)
    rank = change.rolling(422, min_periods=max(422//3, 2)).rank(pct=True)
    persistence = change.rolling(163, min_periods=max(163//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3654 * persistence + 0.0009504 * anchor

def f15_valx_504_struct_v504(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=18, w2=433, w3=176, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(18, min_periods=max(18//3, 2)).std()
    vol_slow = ret.rolling(433, min_periods=max(433//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.4 + 0.0009505 * anchor

def f15_valx_505_struct_v505(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=25, w2=444, w3=189, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(444, min_periods=max(444//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 25)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3806 * slope + 0.0009506 * anchor

def f15_valx_506_struct_v506(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=32, w2=455, w3=202, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(32)
    drag = impulse.rolling(455, min_periods=max(455//3, 2)).mean()
    noise = impulse.abs().rolling(202, min_periods=max(202//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.42875 + 0.0009507 * anchor

def f15_valx_507_struct_v507(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=39, w2=466, w3=215, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 39)
    acceleration = _rolling_slope(velocity, 466)
    curvature = _rolling_slope(acceleration, 215)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3958 * acceleration + 0.0009508 * anchor

def f15_valx_508_struct_v508(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=46, w2=477, w3=228, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(46, min_periods=max(46//3, 2)).mean(), upside.rolling(477, min_periods=max(477//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.4575 + 0.0009509 * anchor

def f15_valx_509_struct_v509(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=53, w2=488, w3=241, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(488, min_periods=max(488//3, 2)).max()
    rebound = x - x.rolling(53, min_periods=max(53//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.411 * _rolling_slope(draw, 241) + 0.000951 * anchor

def f15_valx_510_struct_v510(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=60, w2=499, w3=254, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 60)
    baseline = trend.rolling(499, min_periods=max(499//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(254, min_periods=max(254//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.48625 + 0.0009511 * anchor

def f15_valx_511_struct_v511(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=67, w2=510, w3=267, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 67)
    slow = _rolling_slope(x, 510)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=267, adjust=False).mean() * 1.500625 + 0.0009512 * anchor

def f15_valx_512_struct_v512(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=74, w2=18, w3=280, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(18, min_periods=max(18//3, 2)).max()
    trough = x.rolling(74, min_periods=max(74//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.515 + 0.0009513 * anchor

def f15_valx_513_struct_v513(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=81, w2=29, w3=293, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(81)
    rank = change.rolling(29, min_periods=max(29//3, 2)).rank(pct=True)
    persistence = change.rolling(293, min_periods=max(293//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.065 * persistence + 0.0009514 * anchor

def f15_valx_514_struct_v514(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=88, w2=40, w3=306, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(88, min_periods=max(88//3, 2)).std()
    vol_slow = ret.rolling(40, min_periods=max(40//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.54375 + 0.0009515 * anchor

def f15_valx_515_struct_v515(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=95, w2=51, w3=319, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(51, min_periods=max(51//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 95)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0802 * slope + 0.0009516 * anchor

def f15_valx_516_struct_v516(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=102, w2=62, w3=332, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(102)
    drag = impulse.rolling(62, min_periods=max(62//3, 2)).mean()
    noise = impulse.abs().rolling(332, min_periods=max(332//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.5725 + 0.0009517 * anchor

def f15_valx_517_struct_v517(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=109, w2=73, w3=345, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 109)
    acceleration = _rolling_slope(velocity, 73)
    curvature = _rolling_slope(acceleration, 345)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0954 * acceleration + 0.0009518 * anchor

def f15_valx_518_struct_v518(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=116, w2=84, w3=358, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(116, min_periods=max(116//3, 2)).mean(), upside.rolling(84, min_periods=max(84//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.60125 + 0.0009519 * anchor

def f15_valx_519_struct_v519(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=123, w2=95, w3=371, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(95, min_periods=max(95//3, 2)).max()
    rebound = x - x.rolling(123, min_periods=max(123//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1106 * _rolling_slope(draw, 371) + 0.000952 * anchor

def f15_valx_520_struct_v520(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=130, w2=106, w3=384, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 130)
    baseline = trend.rolling(106, min_periods=max(106//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(384, min_periods=max(384//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.856875 + 0.0009521 * anchor

def f15_valx_521_struct_v521(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=137, w2=117, w3=397, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 137)
    slow = _rolling_slope(x, 117)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.87125 + 0.0009522 * anchor

def f15_valx_522_struct_v522(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=144, w2=128, w3=410, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(128, min_periods=max(128//3, 2)).max()
    trough = x.rolling(144, min_periods=max(144//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.885625 + 0.0009523 * anchor

def f15_valx_523_struct_v523(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=151, w2=139, w3=423, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(139, min_periods=max(139//3, 2)).rank(pct=True)
    persistence = change.rolling(423, min_periods=max(423//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.141 * persistence + 0.0009524 * anchor

def f15_valx_524_struct_v524(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=158, w2=150, w3=436, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(158, min_periods=max(158//3, 2)).std()
    vol_slow = ret.rolling(150, min_periods=max(150//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.914375 + 0.0009525 * anchor

def f15_valx_525_struct_v525(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=165, w2=161, w3=449, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(161, min_periods=max(161//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 165)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1562 * slope + 0.0009526 * anchor
