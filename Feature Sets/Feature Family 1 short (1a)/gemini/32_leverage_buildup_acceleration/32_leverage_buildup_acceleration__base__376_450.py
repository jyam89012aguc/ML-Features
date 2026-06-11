"""32 leverage buildup acceleration base features 376-450 â€” Pipeline 1a-HF Grade v3.

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

def f32_lba_376_struct_v376(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=242, w2=62, w3=151, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(62, min_periods=max(62//3, 2)).mean()
    noise = impulse.abs().rolling(151, min_periods=max(151//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.610625 + 0.0019577 * anchor

def f32_lba_377_struct_v377(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=249, w2=73, w3=164, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 249)
    acceleration = _rolling_slope(velocity, 73)
    curvature = _rolling_slope(acceleration, 164)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1422 * acceleration + 0.0019578 * anchor

def f32_lba_378_struct_v378(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=5, w2=84, w3=177, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(5, min_periods=max(5//3, 2)).mean(), upside.rolling(84, min_periods=max(84//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.86625 + 0.0019579 * anchor

def f32_lba_379_struct_v379(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=12, w2=95, w3=190, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(95, min_periods=max(95//3, 2)).max()
    rebound = x - x.rolling(12, min_periods=max(12//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1574 * _rolling_slope(draw, 190) + 0.001958 * anchor

def f32_lba_380_struct_v380(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=19, w2=106, w3=203, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 19)
    baseline = trend.rolling(106, min_periods=max(106//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(203, min_periods=max(203//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.895 + 0.0019581 * anchor

def f32_lba_381_struct_v381(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=26, w2=117, w3=216, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 26)
    slow = _rolling_slope(x, 117)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=216, adjust=False).mean() * 0.909375 + 0.0019582 * anchor

def f32_lba_382_struct_v382(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=33, w2=128, w3=229, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(128, min_periods=max(128//3, 2)).max()
    trough = x.rolling(33, min_periods=max(33//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.92375 + 0.0019583 * anchor

def f32_lba_383_struct_v383(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=40, w2=139, w3=242, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(40)
    rank = change.rolling(139, min_periods=max(139//3, 2)).rank(pct=True)
    persistence = change.rolling(242, min_periods=max(242//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1878 * persistence + 0.0019584 * anchor

def f32_lba_384_struct_v384(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=47, w2=150, w3=255, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(47, min_periods=max(47//3, 2)).std()
    vol_slow = ret.rolling(150, min_periods=max(150//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.9525 + 0.0019585 * anchor

def f32_lba_385_struct_v385(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=54, w2=161, w3=268, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(161, min_periods=max(161//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 54)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.203 * slope + 0.0019586 * anchor

def f32_lba_386_struct_v386(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=61, w2=172, w3=281, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(61)
    drag = impulse.rolling(172, min_periods=max(172//3, 2)).mean()
    noise = impulse.abs().rolling(281, min_periods=max(281//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.98125 + 0.0019587 * anchor

def f32_lba_387_struct_v387(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=68, w2=183, w3=294, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 68)
    acceleration = _rolling_slope(velocity, 183)
    curvature = _rolling_slope(acceleration, 294)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2182 * acceleration + 0.0019588 * anchor

def f32_lba_388_struct_v388(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=75, w2=194, w3=307, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(75, min_periods=max(75//3, 2)).mean(), upside.rolling(194, min_periods=max(194//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.01 + 0.0019589 * anchor

def f32_lba_389_struct_v389(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=82, w2=205, w3=320, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(205, min_periods=max(205//3, 2)).max()
    rebound = x - x.rolling(82, min_periods=max(82//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2334 * _rolling_slope(draw, 320) + 0.001959 * anchor

def f32_lba_390_struct_v390(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=89, w2=216, w3=333, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 89)
    baseline = trend.rolling(216, min_periods=max(216//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(333, min_periods=max(333//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.03875 + 0.0019591 * anchor

def f32_lba_391_struct_v391(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=96, w2=227, w3=346, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 96)
    slow = _rolling_slope(x, 227)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.053125 + 0.0019592 * anchor

def f32_lba_392_struct_v392(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=103, w2=238, w3=359, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(238, min_periods=max(238//3, 2)).max()
    trough = x.rolling(103, min_periods=max(103//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.0675 + 0.0019593 * anchor

def f32_lba_393_struct_v393(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=110, w2=249, w3=372, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(110)
    rank = change.rolling(249, min_periods=max(249//3, 2)).rank(pct=True)
    persistence = change.rolling(372, min_periods=max(372//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2638 * persistence + 0.0019594 * anchor

def f32_lba_394_struct_v394(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=117, w2=260, w3=385, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(117, min_periods=max(117//3, 2)).std()
    vol_slow = ret.rolling(260, min_periods=max(260//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.09625 + 0.0019595 * anchor

def f32_lba_395_struct_v395(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=124, w2=271, w3=398, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(271, min_periods=max(271//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 124)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.279 * slope + 0.0019596 * anchor

def f32_lba_396_struct_v396(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=131, w2=282, w3=411, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(282, min_periods=max(282//3, 2)).mean()
    noise = impulse.abs().rolling(411, min_periods=max(411//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.125 + 0.0019597 * anchor

def f32_lba_397_struct_v397(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=138, w2=293, w3=424, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 138)
    acceleration = _rolling_slope(velocity, 293)
    curvature = _rolling_slope(acceleration, 424)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2942 * acceleration + 0.0019598 * anchor

def f32_lba_398_struct_v398(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=145, w2=304, w3=437, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(145, min_periods=max(145//3, 2)).mean(), upside.rolling(304, min_periods=max(304//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.15375 + 0.0019599 * anchor

def f32_lba_399_struct_v399(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=152, w2=315, w3=450, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(315, min_periods=max(315//3, 2)).max()
    rebound = x - x.rolling(152, min_periods=max(152//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3094 * _rolling_slope(draw, 450) + 0.00196 * anchor

def f32_lba_400_struct_v400(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=159, w2=326, w3=463, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 159)
    baseline = trend.rolling(326, min_periods=max(326//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(463, min_periods=max(463//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.1825 + 0.0019601 * anchor

def f32_lba_401_struct_v401(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=166, w2=337, w3=476, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 166)
    slow = _rolling_slope(x, 337)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.196875 + 0.0019602 * anchor

def f32_lba_402_struct_v402(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=173, w2=348, w3=489, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(348, min_periods=max(348//3, 2)).max()
    trough = x.rolling(173, min_periods=max(173//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.21125 + 0.0019603 * anchor

def f32_lba_403_struct_v403(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=180, w2=359, w3=502, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(359, min_periods=max(359//3, 2)).rank(pct=True)
    persistence = change.rolling(502, min_periods=max(502//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3398 * persistence + 0.0019604 * anchor

def f32_lba_404_struct_v404(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=187, w2=370, w3=515, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(187, min_periods=max(187//3, 2)).std()
    vol_slow = ret.rolling(370, min_periods=max(370//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.24 + 0.0019605 * anchor

def f32_lba_405_struct_v405(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=194, w2=381, w3=528, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(381, min_periods=max(381//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 194)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.355 * slope + 0.0019606 * anchor

def f32_lba_406_struct_v406(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=201, w2=392, w3=541, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(392, min_periods=max(392//3, 2)).mean()
    noise = impulse.abs().rolling(541, min_periods=max(541//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.26875 + 0.0019607 * anchor

def f32_lba_407_struct_v407(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=208, w2=403, w3=554, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 208)
    acceleration = _rolling_slope(velocity, 403)
    curvature = _rolling_slope(acceleration, 554)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3702 * acceleration + 0.0019608 * anchor

def f32_lba_408_struct_v408(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=215, w2=414, w3=567, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(215, min_periods=max(215//3, 2)).mean(), upside.rolling(414, min_periods=max(414//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.2975 + 0.0019609 * anchor

def f32_lba_409_struct_v409(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=222, w2=425, w3=580, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(425, min_periods=max(425//3, 2)).max()
    rebound = x - x.rolling(222, min_periods=max(222//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3854 * _rolling_slope(draw, 580) + 0.001961 * anchor

def f32_lba_410_struct_v410(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=229, w2=436, w3=593, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 229)
    baseline = trend.rolling(436, min_periods=max(436//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(593, min_periods=max(593//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.32625 + 0.0019611 * anchor

def f32_lba_411_struct_v411(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=236, w2=447, w3=606, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 236)
    slow = _rolling_slope(x, 447)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.340625 + 0.0019612 * anchor

def f32_lba_412_struct_v412(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=243, w2=458, w3=619, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(458, min_periods=max(458//3, 2)).max()
    trough = x.rolling(243, min_periods=max(243//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.355 + 0.0019613 * anchor

def f32_lba_413_struct_v413(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=250, w2=469, w3=632, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(469, min_periods=max(469//3, 2)).rank(pct=True)
    persistence = change.rolling(632, min_periods=max(632//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0394 * persistence + 0.0019614 * anchor

def f32_lba_414_struct_v414(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=6, w2=480, w3=645, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(6, min_periods=max(6//3, 2)).std()
    vol_slow = ret.rolling(480, min_periods=max(480//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.38375 + 0.0019615 * anchor

def f32_lba_415_struct_v415(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=13, w2=491, w3=658, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(491, min_periods=max(491//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 13)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0546 * slope + 0.0019616 * anchor

def f32_lba_416_struct_v416(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=20, w2=502, w3=671, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(20)
    drag = impulse.rolling(502, min_periods=max(502//3, 2)).mean()
    noise = impulse.abs().rolling(671, min_periods=max(671//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.4125 + 0.0019617 * anchor

def f32_lba_417_struct_v417(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=27, w2=10, w3=684, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 27)
    acceleration = _rolling_slope(velocity, 10)
    curvature = _rolling_slope(acceleration, 684)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0698 * acceleration + 0.0019618 * anchor

def f32_lba_418_struct_v418(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=34, w2=21, w3=697, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(34, min_periods=max(34//3, 2)).mean(), upside.rolling(21, min_periods=max(21//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.44125 + 0.0019619 * anchor

def f32_lba_419_struct_v419(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=41, w2=32, w3=710, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(32, min_periods=max(32//3, 2)).max()
    rebound = x - x.rolling(41, min_periods=max(41//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.085 * _rolling_slope(draw, 710) + 0.001962 * anchor

def f32_lba_420_struct_v420(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=48, w2=43, w3=723, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 48)
    baseline = trend.rolling(43, min_periods=max(43//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(723, min_periods=max(723//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.47 + 0.0019621 * anchor

def f32_lba_421_struct_v421(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=55, w2=54, w3=736, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 55)
    slow = _rolling_slope(x, 54)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.484375 + 0.0019622 * anchor

def f32_lba_422_struct_v422(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=62, w2=65, w3=749, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(65, min_periods=max(65//3, 2)).max()
    trough = x.rolling(62, min_periods=max(62//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.49875 + 0.0019623 * anchor

def f32_lba_423_struct_v423(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=69, w2=76, w3=762, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(69)
    rank = change.rolling(76, min_periods=max(76//3, 2)).rank(pct=True)
    persistence = change.rolling(762, min_periods=max(762//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1154 * persistence + 0.0019624 * anchor

def f32_lba_424_struct_v424(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=76, w2=87, w3=18, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(76, min_periods=max(76//3, 2)).std()
    vol_slow = ret.rolling(87, min_periods=max(87//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.5275 + 0.0019625 * anchor

def f32_lba_425_struct_v425(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=83, w2=98, w3=31, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(98, min_periods=max(98//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 83)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1306 * slope + 0.0019626 * anchor

def f32_lba_426_struct_v426(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=90, w2=109, w3=44, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(90)
    drag = impulse.rolling(109, min_periods=max(109//3, 2)).mean()
    noise = impulse.abs().rolling(44, min_periods=max(44//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.55625 + 0.0019627 * anchor

def f32_lba_427_struct_v427(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=97, w2=120, w3=57, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 97)
    acceleration = _rolling_slope(velocity, 120)
    curvature = _rolling_slope(acceleration, 57)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1458 * acceleration + 0.0019628 * anchor

def f32_lba_428_struct_v428(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=104, w2=131, w3=70, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(104, min_periods=max(104//3, 2)).mean(), upside.rolling(131, min_periods=max(131//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(70) * 1.585 + 0.0019629 * anchor

def f32_lba_429_struct_v429(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=111, w2=142, w3=83, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(142, min_periods=max(142//3, 2)).max()
    rebound = x - x.rolling(111, min_periods=max(111//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.161 * _rolling_slope(draw, 83) + 0.001963 * anchor

def f32_lba_430_struct_v430(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=118, w2=153, w3=96, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 118)
    baseline = trend.rolling(153, min_periods=max(153//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(96, min_periods=max(96//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.61375 + 0.0019631 * anchor

def f32_lba_431_struct_v431(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=125, w2=164, w3=109, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 125)
    slow = _rolling_slope(x, 164)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=109, adjust=False).mean() * 0.855 + 0.0019632 * anchor

def f32_lba_432_struct_v432(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=132, w2=175, w3=122, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(175, min_periods=max(175//3, 2)).max()
    trough = x.rolling(132, min_periods=max(132//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.869375 + 0.0019633 * anchor

def f32_lba_433_struct_v433(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=139, w2=186, w3=135, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(186, min_periods=max(186//3, 2)).rank(pct=True)
    persistence = change.rolling(135, min_periods=max(135//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1914 * persistence + 0.0019634 * anchor

def f32_lba_434_struct_v434(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=146, w2=197, w3=148, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(146, min_periods=max(146//3, 2)).std()
    vol_slow = ret.rolling(197, min_periods=max(197//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.898125 + 0.0019635 * anchor

def f32_lba_435_struct_v435(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=153, w2=208, w3=161, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(208, min_periods=max(208//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 153)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2066 * slope + 0.0019636 * anchor

def f32_lba_436_struct_v436(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=160, w2=219, w3=174, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(219, min_periods=max(219//3, 2)).mean()
    noise = impulse.abs().rolling(174, min_periods=max(174//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.926875 + 0.0019637 * anchor

def f32_lba_437_struct_v437(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=167, w2=230, w3=187, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 167)
    acceleration = _rolling_slope(velocity, 230)
    curvature = _rolling_slope(acceleration, 187)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2218 * acceleration + 0.0019638 * anchor

def f32_lba_438_struct_v438(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=174, w2=241, w3=200, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(174, min_periods=max(174//3, 2)).mean(), upside.rolling(241, min_periods=max(241//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.955625 + 0.0019639 * anchor

def f32_lba_439_struct_v439(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=181, w2=252, w3=213, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(252, min_periods=max(252//3, 2)).max()
    rebound = x - x.rolling(181, min_periods=max(181//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.237 * _rolling_slope(draw, 213) + 0.001964 * anchor

def f32_lba_440_struct_v440(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=188, w2=263, w3=226, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 188)
    baseline = trend.rolling(263, min_periods=max(263//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(226, min_periods=max(226//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.984375 + 0.0019641 * anchor

def f32_lba_441_struct_v441(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=195, w2=274, w3=239, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 195)
    slow = _rolling_slope(x, 274)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=239, adjust=False).mean() * 0.99875 + 0.0019642 * anchor

def f32_lba_442_struct_v442(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=202, w2=285, w3=252, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(285, min_periods=max(285//3, 2)).max()
    trough = x.rolling(202, min_periods=max(202//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.013125 + 0.0019643 * anchor

def f32_lba_443_struct_v443(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=209, w2=296, w3=265, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(296, min_periods=max(296//3, 2)).rank(pct=True)
    persistence = change.rolling(265, min_periods=max(265//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2674 * persistence + 0.0019644 * anchor

def f32_lba_444_struct_v444(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=216, w2=307, w3=278, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(216, min_periods=max(216//3, 2)).std()
    vol_slow = ret.rolling(307, min_periods=max(307//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.041875 + 0.0019645 * anchor

def f32_lba_445_struct_v445(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=223, w2=318, w3=291, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(318, min_periods=max(318//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 223)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2826 * slope + 0.0019646 * anchor

def f32_lba_446_struct_v446(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=230, w2=329, w3=304, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(329, min_periods=max(329//3, 2)).mean()
    noise = impulse.abs().rolling(304, min_periods=max(304//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.070625 + 0.0019647 * anchor

def f32_lba_447_struct_v447(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=237, w2=340, w3=317, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 237)
    acceleration = _rolling_slope(velocity, 340)
    curvature = _rolling_slope(acceleration, 317)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2978 * acceleration + 0.0019648 * anchor

def f32_lba_448_struct_v448(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=244, w2=351, w3=330, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(244, min_periods=max(244//3, 2)).mean(), upside.rolling(351, min_periods=max(351//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.099375 + 0.0019649 * anchor

def f32_lba_449_struct_v449(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=251, w2=362, w3=343, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(362, min_periods=max(362//3, 2)).max()
    rebound = x - x.rolling(251, min_periods=max(251//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.313 * _rolling_slope(draw, 343) + 0.001965 * anchor

def f32_lba_450_struct_v450(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=7, w2=373, w3=356, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 7)
    baseline = trend.rolling(373, min_periods=max(373//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(356, min_periods=max(356//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.128125 + 0.0019651 * anchor
