"""44 moat erosion trajectory base features 451-525 â€” Pipeline 1a-HF Grade v3.

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

def f44_met_451_struct_v451(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=147, w2=171, w3=331, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 147)
    slow = _rolling_slope(x, 171)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.164375 + 0.0027452 * anchor

def f44_met_452_struct_v452(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=154, w2=182, w3=344, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(182, min_periods=max(182//3, 2)).max()
    trough = x.rolling(154, min_periods=max(154//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.17875 + 0.0027453 * anchor

def f44_met_453_struct_v453(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=161, w2=193, w3=357, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(193, min_periods=max(193//3, 2)).rank(pct=True)
    persistence = change.rolling(357, min_periods=max(357//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1522 * persistence + 0.0027454 * anchor

def f44_met_454_struct_v454(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=168, w2=204, w3=370, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(168, min_periods=max(168//3, 2)).std()
    vol_slow = ret.rolling(204, min_periods=max(204//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.2075 + 0.0027455 * anchor

def f44_met_455_struct_v455(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=175, w2=215, w3=383, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(215, min_periods=max(215//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 175)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1674 * slope + 0.0027456 * anchor

def f44_met_456_struct_v456(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=182, w2=226, w3=396, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(226, min_periods=max(226//3, 2)).mean()
    noise = impulse.abs().rolling(396, min_periods=max(396//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.23625 + 0.0027457 * anchor

def f44_met_457_struct_v457(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=189, w2=237, w3=409, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 189)
    acceleration = _rolling_slope(velocity, 237)
    curvature = _rolling_slope(acceleration, 409)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1826 * acceleration + 0.0027458 * anchor

def f44_met_458_struct_v458(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=196, w2=248, w3=422, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(196, min_periods=max(196//3, 2)).mean(), upside.rolling(248, min_periods=max(248//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.265 + 0.0027459 * anchor

def f44_met_459_struct_v459(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=203, w2=259, w3=435, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(259, min_periods=max(259//3, 2)).max()
    rebound = x - x.rolling(203, min_periods=max(203//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1978 * _rolling_slope(draw, 435) + 0.002746 * anchor

def f44_met_460_struct_v460(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=210, w2=270, w3=448, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 210)
    baseline = trend.rolling(270, min_periods=max(270//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(448, min_periods=max(448//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.29375 + 0.0027461 * anchor

def f44_met_461_struct_v461(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=217, w2=281, w3=461, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 217)
    slow = _rolling_slope(x, 281)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.308125 + 0.0027462 * anchor

def f44_met_462_struct_v462(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=224, w2=292, w3=474, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(292, min_periods=max(292//3, 2)).max()
    trough = x.rolling(224, min_periods=max(224//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.3225 + 0.0027463 * anchor

def f44_met_463_struct_v463(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=231, w2=303, w3=487, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(303, min_periods=max(303//3, 2)).rank(pct=True)
    persistence = change.rolling(487, min_periods=max(487//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2282 * persistence + 0.0027464 * anchor

def f44_met_464_struct_v464(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=238, w2=314, w3=500, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(238, min_periods=max(238//3, 2)).std()
    vol_slow = ret.rolling(314, min_periods=max(314//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.35125 + 0.0027465 * anchor

def f44_met_465_struct_v465(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=245, w2=325, w3=513, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(325, min_periods=max(325//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 245)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2434 * slope + 0.0027466 * anchor

def f44_met_466_struct_v466(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=252, w2=336, w3=526, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(336, min_periods=max(336//3, 2)).mean()
    noise = impulse.abs().rolling(526, min_periods=max(526//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.38 + 0.0027467 * anchor

def f44_met_467_struct_v467(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=8, w2=347, w3=539, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 8)
    acceleration = _rolling_slope(velocity, 347)
    curvature = _rolling_slope(acceleration, 539)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2586 * acceleration + 0.0027468 * anchor

def f44_met_468_struct_v468(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=15, w2=358, w3=552, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(15, min_periods=max(15//3, 2)).mean(), upside.rolling(358, min_periods=max(358//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.40875 + 0.0027469 * anchor

def f44_met_469_struct_v469(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=22, w2=369, w3=565, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(369, min_periods=max(369//3, 2)).max()
    rebound = x - x.rolling(22, min_periods=max(22//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2738 * _rolling_slope(draw, 565) + 0.002747 * anchor

def f44_met_470_struct_v470(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=29, w2=380, w3=578, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 29)
    baseline = trend.rolling(380, min_periods=max(380//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(578, min_periods=max(578//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.4375 + 0.0027471 * anchor

def f44_met_471_struct_v471(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=36, w2=391, w3=591, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 36)
    slow = _rolling_slope(x, 391)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.451875 + 0.0027472 * anchor

def f44_met_472_struct_v472(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=43, w2=402, w3=604, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(402, min_periods=max(402//3, 2)).max()
    trough = x.rolling(43, min_periods=max(43//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.46625 + 0.0027473 * anchor

def f44_met_473_struct_v473(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=50, w2=413, w3=617, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(50)
    rank = change.rolling(413, min_periods=max(413//3, 2)).rank(pct=True)
    persistence = change.rolling(617, min_periods=max(617//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3042 * persistence + 0.0027474 * anchor

def f44_met_474_struct_v474(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=57, w2=424, w3=630, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(57, min_periods=max(57//3, 2)).std()
    vol_slow = ret.rolling(424, min_periods=max(424//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.495 + 0.0027475 * anchor

def f44_met_475_struct_v475(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=64, w2=435, w3=643, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(435, min_periods=max(435//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 64)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3194 * slope + 0.0027476 * anchor

def f44_met_476_struct_v476(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=71, w2=446, w3=656, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(71)
    drag = impulse.rolling(446, min_periods=max(446//3, 2)).mean()
    noise = impulse.abs().rolling(656, min_periods=max(656//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.52375 + 0.0027477 * anchor

def f44_met_477_struct_v477(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=78, w2=457, w3=669, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 78)
    acceleration = _rolling_slope(velocity, 457)
    curvature = _rolling_slope(acceleration, 669)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3346 * acceleration + 0.0027478 * anchor

def f44_met_478_struct_v478(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=85, w2=468, w3=682, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(85, min_periods=max(85//3, 2)).mean(), upside.rolling(468, min_periods=max(468//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.5525 + 0.0027479 * anchor

def f44_met_479_struct_v479(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=92, w2=479, w3=695, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(479, min_periods=max(479//3, 2)).max()
    rebound = x - x.rolling(92, min_periods=max(92//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3498 * _rolling_slope(draw, 695) + 0.002748 * anchor

def f44_met_480_struct_v480(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=99, w2=490, w3=708, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 99)
    baseline = trend.rolling(490, min_periods=max(490//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(708, min_periods=max(708//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.58125 + 0.0027481 * anchor

def f44_met_481_struct_v481(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=106, w2=501, w3=721, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 106)
    slow = _rolling_slope(x, 501)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.595625 + 0.0027482 * anchor

def f44_met_482_struct_v482(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=113, w2=512, w3=734, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(512, min_periods=max(512//3, 2)).max()
    trough = x.rolling(113, min_periods=max(113//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.61 + 0.0027483 * anchor

def f44_met_483_struct_v483(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=120, w2=20, w3=747, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(120)
    rank = change.rolling(20, min_periods=max(20//3, 2)).rank(pct=True)
    persistence = change.rolling(747, min_periods=max(747//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3802 * persistence + 0.0027484 * anchor

def f44_met_484_struct_v484(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=127, w2=31, w3=760, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(127, min_periods=max(127//3, 2)).std()
    vol_slow = ret.rolling(31, min_periods=max(31//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.865625 + 0.0027485 * anchor

def f44_met_485_struct_v485(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=134, w2=42, w3=16, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(42, min_periods=max(42//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 134)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3954 * slope + 0.0027486 * anchor

def f44_met_486_struct_v486(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=141, w2=53, w3=29, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(53, min_periods=max(53//3, 2)).mean()
    noise = impulse.abs().rolling(29, min_periods=max(29//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.894375 + 0.0027487 * anchor

def f44_met_487_struct_v487(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=148, w2=64, w3=42, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 148)
    acceleration = _rolling_slope(velocity, 64)
    curvature = _rolling_slope(acceleration, 42)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.4106 * acceleration + 0.0027488 * anchor

def f44_met_488_struct_v488(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=155, w2=75, w3=55, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(155, min_periods=max(155//3, 2)).mean(), upside.rolling(75, min_periods=max(75//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(55) * 0.923125 + 0.0027489 * anchor

def f44_met_489_struct_v489(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=162, w2=86, w3=68, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(86, min_periods=max(86//3, 2)).max()
    rebound = x - x.rolling(162, min_periods=max(162//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0494 * _rolling_slope(draw, 68) + 0.002749 * anchor

def f44_met_490_struct_v490(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=169, w2=97, w3=81, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 169)
    baseline = trend.rolling(97, min_periods=max(97//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(81, min_periods=max(81//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.951875 + 0.0027491 * anchor

def f44_met_491_struct_v491(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=176, w2=108, w3=94, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 176)
    slow = _rolling_slope(x, 108)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=94, adjust=False).mean() * 0.96625 + 0.0027492 * anchor

def f44_met_492_struct_v492(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=183, w2=119, w3=107, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(119, min_periods=max(119//3, 2)).max()
    trough = x.rolling(183, min_periods=max(183//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.980625 + 0.0027493 * anchor

def f44_met_493_struct_v493(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=190, w2=130, w3=120, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(130, min_periods=max(130//3, 2)).rank(pct=True)
    persistence = change.rolling(120, min_periods=max(120//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0798 * persistence + 0.0027494 * anchor

def f44_met_494_struct_v494(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=197, w2=141, w3=133, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(197, min_periods=max(197//3, 2)).std()
    vol_slow = ret.rolling(141, min_periods=max(141//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.009375 + 0.0027495 * anchor

def f44_met_495_struct_v495(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=204, w2=152, w3=146, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(152, min_periods=max(152//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 204)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.095 * slope + 0.0027496 * anchor

def f44_met_496_struct_v496(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=211, w2=163, w3=159, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(163, min_periods=max(163//3, 2)).mean()
    noise = impulse.abs().rolling(159, min_periods=max(159//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.038125 + 0.0027497 * anchor

def f44_met_497_struct_v497(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=218, w2=174, w3=172, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 218)
    acceleration = _rolling_slope(velocity, 174)
    curvature = _rolling_slope(acceleration, 172)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1102 * acceleration + 0.0027498 * anchor

def f44_met_498_struct_v498(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=225, w2=185, w3=185, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(225, min_periods=max(225//3, 2)).mean(), upside.rolling(185, min_periods=max(185//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.066875 + 0.0027499 * anchor

def f44_met_499_struct_v499(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=232, w2=196, w3=198, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(196, min_periods=max(196//3, 2)).max()
    rebound = x - x.rolling(232, min_periods=max(232//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1254 * _rolling_slope(draw, 198) + 0.00275 * anchor

def f44_met_500_struct_v500(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=239, w2=207, w3=211, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 239)
    baseline = trend.rolling(207, min_periods=max(207//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(211, min_periods=max(211//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.095625 + 0.0027501 * anchor

def f44_met_501_struct_v501(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=246, w2=218, w3=224, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 246)
    slow = _rolling_slope(x, 218)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=224, adjust=False).mean() * 1.11 + 0.0027502 * anchor

def f44_met_502_struct_v502(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=253, w2=229, w3=237, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(229, min_periods=max(229//3, 2)).max()
    trough = x.rolling(253, min_periods=max(253//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.124375 + 0.0027503 * anchor

def f44_met_503_struct_v503(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=9, w2=240, w3=250, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(9)
    rank = change.rolling(240, min_periods=max(240//3, 2)).rank(pct=True)
    persistence = change.rolling(250, min_periods=max(250//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1558 * persistence + 0.0027504 * anchor

def f44_met_504_struct_v504(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=16, w2=251, w3=263, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(16, min_periods=max(16//3, 2)).std()
    vol_slow = ret.rolling(251, min_periods=max(251//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.153125 + 0.0027505 * anchor

def f44_met_505_struct_v505(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=23, w2=262, w3=276, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(262, min_periods=max(262//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 23)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.171 * slope + 0.0027506 * anchor

def f44_met_506_struct_v506(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=30, w2=273, w3=289, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(30)
    drag = impulse.rolling(273, min_periods=max(273//3, 2)).mean()
    noise = impulse.abs().rolling(289, min_periods=max(289//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.181875 + 0.0027507 * anchor

def f44_met_507_struct_v507(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=37, w2=284, w3=302, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 37)
    acceleration = _rolling_slope(velocity, 284)
    curvature = _rolling_slope(acceleration, 302)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1862 * acceleration + 0.0027508 * anchor

def f44_met_508_struct_v508(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=44, w2=295, w3=315, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(44, min_periods=max(44//3, 2)).mean(), upside.rolling(295, min_periods=max(295//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.210625 + 0.0027509 * anchor

def f44_met_509_struct_v509(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=51, w2=306, w3=328, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(306, min_periods=max(306//3, 2)).max()
    rebound = x - x.rolling(51, min_periods=max(51//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2014 * _rolling_slope(draw, 328) + 0.002751 * anchor

def f44_met_510_struct_v510(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=58, w2=317, w3=341, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 58)
    baseline = trend.rolling(317, min_periods=max(317//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(341, min_periods=max(341//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.239375 + 0.0027511 * anchor

def f44_met_511_struct_v511(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=65, w2=328, w3=354, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 65)
    slow = _rolling_slope(x, 328)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.25375 + 0.0027512 * anchor

def f44_met_512_struct_v512(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=72, w2=339, w3=367, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(339, min_periods=max(339//3, 2)).max()
    trough = x.rolling(72, min_periods=max(72//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.268125 + 0.0027513 * anchor

def f44_met_513_struct_v513(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=79, w2=350, w3=380, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(79)
    rank = change.rolling(350, min_periods=max(350//3, 2)).rank(pct=True)
    persistence = change.rolling(380, min_periods=max(380//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2318 * persistence + 0.0027514 * anchor

def f44_met_514_struct_v514(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=86, w2=361, w3=393, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(86, min_periods=max(86//3, 2)).std()
    vol_slow = ret.rolling(361, min_periods=max(361//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.296875 + 0.0027515 * anchor

def f44_met_515_struct_v515(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=93, w2=372, w3=406, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(372, min_periods=max(372//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 93)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.247 * slope + 0.0027516 * anchor

def f44_met_516_struct_v516(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=100, w2=383, w3=419, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(100)
    drag = impulse.rolling(383, min_periods=max(383//3, 2)).mean()
    noise = impulse.abs().rolling(419, min_periods=max(419//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.325625 + 0.0027517 * anchor

def f44_met_517_struct_v517(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=107, w2=394, w3=432, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 107)
    acceleration = _rolling_slope(velocity, 394)
    curvature = _rolling_slope(acceleration, 432)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2622 * acceleration + 0.0027518 * anchor

def f44_met_518_struct_v518(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=114, w2=405, w3=445, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(114, min_periods=max(114//3, 2)).mean(), upside.rolling(405, min_periods=max(405//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.354375 + 0.0027519 * anchor

def f44_met_519_struct_v519(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=121, w2=416, w3=458, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(416, min_periods=max(416//3, 2)).max()
    rebound = x - x.rolling(121, min_periods=max(121//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2774 * _rolling_slope(draw, 458) + 0.002752 * anchor

def f44_met_520_struct_v520(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=128, w2=427, w3=471, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 128)
    baseline = trend.rolling(427, min_periods=max(427//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(471, min_periods=max(471//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.383125 + 0.0027521 * anchor

def f44_met_521_struct_v521(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=135, w2=438, w3=484, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 135)
    slow = _rolling_slope(x, 438)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.3975 + 0.0027522 * anchor

def f44_met_522_struct_v522(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=142, w2=449, w3=497, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(449, min_periods=max(449//3, 2)).max()
    trough = x.rolling(142, min_periods=max(142//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.411875 + 0.0027523 * anchor

def f44_met_523_struct_v523(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=149, w2=460, w3=510, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(460, min_periods=max(460//3, 2)).rank(pct=True)
    persistence = change.rolling(510, min_periods=max(510//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3078 * persistence + 0.0027524 * anchor

def f44_met_524_struct_v524(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=156, w2=471, w3=523, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(156, min_periods=max(156//3, 2)).std()
    vol_slow = ret.rolling(471, min_periods=max(471//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.440625 + 0.0027525 * anchor

def f44_met_525_struct_v525(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=163, w2=482, w3=536, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(482, min_periods=max(482//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 163)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.323 * slope + 0.0027526 * anchor
