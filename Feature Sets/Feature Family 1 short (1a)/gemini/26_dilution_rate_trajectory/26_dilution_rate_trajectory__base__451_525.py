"""26 dilution rate trajectory base features 451-525 â€” Pipeline 1a-HF Grade v3.

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

def f26_dlr_451_struct_v451(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=165, w2=18, w3=503, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 165)
    slow = _rolling_slope(x, 18)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.191875 + 0.0016052 * anchor

def f26_dlr_452_struct_v452(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=172, w2=29, w3=516, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(29, min_periods=max(29//3, 2)).max()
    trough = x.rolling(172, min_periods=max(172//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.20625 + 0.0016053 * anchor

def f26_dlr_453_struct_v453(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=179, w2=40, w3=529, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(40, min_periods=max(40//3, 2)).rank(pct=True)
    persistence = change.rolling(529, min_periods=max(529//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0842 * persistence + 0.0016054 * anchor

def f26_dlr_454_struct_v454(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=186, w2=51, w3=542, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(186, min_periods=max(186//3, 2)).std()
    vol_slow = ret.rolling(51, min_periods=max(51//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.235 + 0.0016055 * anchor

def f26_dlr_455_struct_v455(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=193, w2=62, w3=555, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(62, min_periods=max(62//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 193)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0994 * slope + 0.0016056 * anchor

def f26_dlr_456_struct_v456(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=200, w2=73, w3=568, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(73, min_periods=max(73//3, 2)).mean()
    noise = impulse.abs().rolling(568, min_periods=max(568//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.26375 + 0.0016057 * anchor

def f26_dlr_457_struct_v457(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=207, w2=84, w3=581, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 207)
    acceleration = _rolling_slope(velocity, 84)
    curvature = _rolling_slope(acceleration, 581)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1146 * acceleration + 0.0016058 * anchor

def f26_dlr_458_struct_v458(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=214, w2=95, w3=594, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(214, min_periods=max(214//3, 2)).mean(), upside.rolling(95, min_periods=max(95//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.2925 + 0.0016059 * anchor

def f26_dlr_459_struct_v459(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=221, w2=106, w3=607, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(106, min_periods=max(106//3, 2)).max()
    rebound = x - x.rolling(221, min_periods=max(221//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1298 * _rolling_slope(draw, 607) + 0.001606 * anchor

def f26_dlr_460_struct_v460(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=228, w2=117, w3=620, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 228)
    baseline = trend.rolling(117, min_periods=max(117//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(620, min_periods=max(620//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.32125 + 0.0016061 * anchor

def f26_dlr_461_struct_v461(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=235, w2=128, w3=633, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 235)
    slow = _rolling_slope(x, 128)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.335625 + 0.0016062 * anchor

def f26_dlr_462_struct_v462(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=242, w2=139, w3=646, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(139, min_periods=max(139//3, 2)).max()
    trough = x.rolling(242, min_periods=max(242//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.35 + 0.0016063 * anchor

def f26_dlr_463_struct_v463(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=249, w2=150, w3=659, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(150, min_periods=max(150//3, 2)).rank(pct=True)
    persistence = change.rolling(659, min_periods=max(659//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1602 * persistence + 0.0016064 * anchor

def f26_dlr_464_struct_v464(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=5, w2=161, w3=672, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(5, min_periods=max(5//3, 2)).std()
    vol_slow = ret.rolling(161, min_periods=max(161//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.37875 + 0.0016065 * anchor

def f26_dlr_465_struct_v465(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=12, w2=172, w3=685, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(172, min_periods=max(172//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 12)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1754 * slope + 0.0016066 * anchor

def f26_dlr_466_struct_v466(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=19, w2=183, w3=698, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(19)
    drag = impulse.rolling(183, min_periods=max(183//3, 2)).mean()
    noise = impulse.abs().rolling(698, min_periods=max(698//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.4075 + 0.0016067 * anchor

def f26_dlr_467_struct_v467(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=26, w2=194, w3=711, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 26)
    acceleration = _rolling_slope(velocity, 194)
    curvature = _rolling_slope(acceleration, 711)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1906 * acceleration + 0.0016068 * anchor

def f26_dlr_468_struct_v468(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=33, w2=205, w3=724, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(33, min_periods=max(33//3, 2)).mean(), upside.rolling(205, min_periods=max(205//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.43625 + 0.0016069 * anchor

def f26_dlr_469_struct_v469(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=40, w2=216, w3=737, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(216, min_periods=max(216//3, 2)).max()
    rebound = x - x.rolling(40, min_periods=max(40//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2058 * _rolling_slope(draw, 737) + 0.001607 * anchor

def f26_dlr_470_struct_v470(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=47, w2=227, w3=750, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 47)
    baseline = trend.rolling(227, min_periods=max(227//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(750, min_periods=max(750//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.465 + 0.0016071 * anchor

def f26_dlr_471_struct_v471(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=54, w2=238, w3=763, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 54)
    slow = _rolling_slope(x, 238)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.479375 + 0.0016072 * anchor

def f26_dlr_472_struct_v472(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=61, w2=249, w3=19, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(249, min_periods=max(249//3, 2)).max()
    trough = x.rolling(61, min_periods=max(61//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.49375 + 0.0016073 * anchor

def f26_dlr_473_struct_v473(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=68, w2=260, w3=32, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(68)
    rank = change.rolling(260, min_periods=max(260//3, 2)).rank(pct=True)
    persistence = change.rolling(32, min_periods=max(32//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2362 * persistence + 0.0016074 * anchor

def f26_dlr_474_struct_v474(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=75, w2=271, w3=45, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(75, min_periods=max(75//3, 2)).std()
    vol_slow = ret.rolling(271, min_periods=max(271//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.5225 + 0.0016075 * anchor

def f26_dlr_475_struct_v475(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=82, w2=282, w3=58, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(282, min_periods=max(282//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 82)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2514 * slope + 0.0016076 * anchor

def f26_dlr_476_struct_v476(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=89, w2=293, w3=71, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(89)
    drag = impulse.rolling(293, min_periods=max(293//3, 2)).mean()
    noise = impulse.abs().rolling(71, min_periods=max(71//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.55125 + 0.0016077 * anchor

def f26_dlr_477_struct_v477(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=96, w2=304, w3=84, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 96)
    acceleration = _rolling_slope(velocity, 304)
    curvature = _rolling_slope(acceleration, 84)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2666 * acceleration + 0.0016078 * anchor

def f26_dlr_478_struct_v478(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=103, w2=315, w3=97, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(103, min_periods=max(103//3, 2)).mean(), upside.rolling(315, min_periods=max(315//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(97) * 1.58 + 0.0016079 * anchor

def f26_dlr_479_struct_v479(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=110, w2=326, w3=110, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(326, min_periods=max(326//3, 2)).max()
    rebound = x - x.rolling(110, min_periods=max(110//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2818 * _rolling_slope(draw, 110) + 0.001608 * anchor

def f26_dlr_480_struct_v480(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=117, w2=337, w3=123, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 117)
    baseline = trend.rolling(337, min_periods=max(337//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(123, min_periods=max(123//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.60875 + 0.0016081 * anchor

def f26_dlr_481_struct_v481(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=124, w2=348, w3=136, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 124)
    slow = _rolling_slope(x, 348)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=136, adjust=False).mean() * 0.85 + 0.0016082 * anchor

def f26_dlr_482_struct_v482(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=131, w2=359, w3=149, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(359, min_periods=max(359//3, 2)).max()
    trough = x.rolling(131, min_periods=max(131//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.864375 + 0.0016083 * anchor

def f26_dlr_483_struct_v483(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=138, w2=370, w3=162, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(370, min_periods=max(370//3, 2)).rank(pct=True)
    persistence = change.rolling(162, min_periods=max(162//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3122 * persistence + 0.0016084 * anchor

def f26_dlr_484_struct_v484(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=145, w2=381, w3=175, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(145, min_periods=max(145//3, 2)).std()
    vol_slow = ret.rolling(381, min_periods=max(381//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.893125 + 0.0016085 * anchor

def f26_dlr_485_struct_v485(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=152, w2=392, w3=188, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(392, min_periods=max(392//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 152)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3274 * slope + 0.0016086 * anchor

def f26_dlr_486_struct_v486(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=159, w2=403, w3=201, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(403, min_periods=max(403//3, 2)).mean()
    noise = impulse.abs().rolling(201, min_periods=max(201//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.921875 + 0.0016087 * anchor

def f26_dlr_487_struct_v487(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=166, w2=414, w3=214, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 166)
    acceleration = _rolling_slope(velocity, 414)
    curvature = _rolling_slope(acceleration, 214)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3426 * acceleration + 0.0016088 * anchor

def f26_dlr_488_struct_v488(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=173, w2=425, w3=227, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(173, min_periods=max(173//3, 2)).mean(), upside.rolling(425, min_periods=max(425//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.950625 + 0.0016089 * anchor

def f26_dlr_489_struct_v489(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=180, w2=436, w3=240, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(436, min_periods=max(436//3, 2)).max()
    rebound = x - x.rolling(180, min_periods=max(180//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3578 * _rolling_slope(draw, 240) + 0.001609 * anchor

def f26_dlr_490_struct_v490(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=187, w2=447, w3=253, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 187)
    baseline = trend.rolling(447, min_periods=max(447//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(253, min_periods=max(253//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.979375 + 0.0016091 * anchor

def f26_dlr_491_struct_v491(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=194, w2=458, w3=266, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 194)
    slow = _rolling_slope(x, 458)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=266, adjust=False).mean() * 0.99375 + 0.0016092 * anchor

def f26_dlr_492_struct_v492(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=201, w2=469, w3=279, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(469, min_periods=max(469//3, 2)).max()
    trough = x.rolling(201, min_periods=max(201//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.008125 + 0.0016093 * anchor

def f26_dlr_493_struct_v493(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=208, w2=480, w3=292, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(480, min_periods=max(480//3, 2)).rank(pct=True)
    persistence = change.rolling(292, min_periods=max(292//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3882 * persistence + 0.0016094 * anchor

def f26_dlr_494_struct_v494(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=215, w2=491, w3=305, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(215, min_periods=max(215//3, 2)).std()
    vol_slow = ret.rolling(491, min_periods=max(491//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.036875 + 0.0016095 * anchor

def f26_dlr_495_struct_v495(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=222, w2=502, w3=318, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(502, min_periods=max(502//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 222)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.4034 * slope + 0.0016096 * anchor

def f26_dlr_496_struct_v496(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=229, w2=10, w3=331, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(10, min_periods=max(10//3, 2)).mean()
    noise = impulse.abs().rolling(331, min_periods=max(331//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.065625 + 0.0016097 * anchor

def f26_dlr_497_struct_v497(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=236, w2=21, w3=344, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 236)
    acceleration = _rolling_slope(velocity, 21)
    curvature = _rolling_slope(acceleration, 344)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0422 * acceleration + 0.0016098 * anchor

def f26_dlr_498_struct_v498(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=243, w2=32, w3=357, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(243, min_periods=max(243//3, 2)).mean(), upside.rolling(32, min_periods=max(32//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.094375 + 0.0016099 * anchor

def f26_dlr_499_struct_v499(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=250, w2=43, w3=370, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(43, min_periods=max(43//3, 2)).max()
    rebound = x - x.rolling(250, min_periods=max(250//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0574 * _rolling_slope(draw, 370) + 0.00161 * anchor

def f26_dlr_500_struct_v500(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=6, w2=54, w3=383, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 6)
    baseline = trend.rolling(54, min_periods=max(54//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(383, min_periods=max(383//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.123125 + 0.0016101 * anchor

def f26_dlr_501_struct_v501(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=13, w2=65, w3=396, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 13)
    slow = _rolling_slope(x, 65)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.1375 + 0.0016102 * anchor

def f26_dlr_502_struct_v502(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=20, w2=76, w3=409, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(76, min_periods=max(76//3, 2)).max()
    trough = x.rolling(20, min_periods=max(20//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.151875 + 0.0016103 * anchor

def f26_dlr_503_struct_v503(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=27, w2=87, w3=422, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(27)
    rank = change.rolling(87, min_periods=max(87//3, 2)).rank(pct=True)
    persistence = change.rolling(422, min_periods=max(422//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0878 * persistence + 0.0016104 * anchor

def f26_dlr_504_struct_v504(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=34, w2=98, w3=435, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(34, min_periods=max(34//3, 2)).std()
    vol_slow = ret.rolling(98, min_periods=max(98//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.180625 + 0.0016105 * anchor

def f26_dlr_505_struct_v505(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=41, w2=109, w3=448, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(109, min_periods=max(109//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 41)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.103 * slope + 0.0016106 * anchor

def f26_dlr_506_struct_v506(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=48, w2=120, w3=461, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(48)
    drag = impulse.rolling(120, min_periods=max(120//3, 2)).mean()
    noise = impulse.abs().rolling(461, min_periods=max(461//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.209375 + 0.0016107 * anchor

def f26_dlr_507_struct_v507(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=55, w2=131, w3=474, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 55)
    acceleration = _rolling_slope(velocity, 131)
    curvature = _rolling_slope(acceleration, 474)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1182 * acceleration + 0.0016108 * anchor

def f26_dlr_508_struct_v508(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=62, w2=142, w3=487, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(62, min_periods=max(62//3, 2)).mean(), upside.rolling(142, min_periods=max(142//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.238125 + 0.0016109 * anchor

def f26_dlr_509_struct_v509(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=69, w2=153, w3=500, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(153, min_periods=max(153//3, 2)).max()
    rebound = x - x.rolling(69, min_periods=max(69//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1334 * _rolling_slope(draw, 500) + 0.001611 * anchor

def f26_dlr_510_struct_v510(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=76, w2=164, w3=513, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 76)
    baseline = trend.rolling(164, min_periods=max(164//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(513, min_periods=max(513//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.266875 + 0.0016111 * anchor

def f26_dlr_511_struct_v511(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=83, w2=175, w3=526, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 83)
    slow = _rolling_slope(x, 175)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.28125 + 0.0016112 * anchor

def f26_dlr_512_struct_v512(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=90, w2=186, w3=539, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(186, min_periods=max(186//3, 2)).max()
    trough = x.rolling(90, min_periods=max(90//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.295625 + 0.0016113 * anchor

def f26_dlr_513_struct_v513(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=97, w2=197, w3=552, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(97)
    rank = change.rolling(197, min_periods=max(197//3, 2)).rank(pct=True)
    persistence = change.rolling(552, min_periods=max(552//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1638 * persistence + 0.0016114 * anchor

def f26_dlr_514_struct_v514(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=104, w2=208, w3=565, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(104, min_periods=max(104//3, 2)).std()
    vol_slow = ret.rolling(208, min_periods=max(208//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.324375 + 0.0016115 * anchor

def f26_dlr_515_struct_v515(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=111, w2=219, w3=578, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(219, min_periods=max(219//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 111)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.179 * slope + 0.0016116 * anchor

def f26_dlr_516_struct_v516(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=118, w2=230, w3=591, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(118)
    drag = impulse.rolling(230, min_periods=max(230//3, 2)).mean()
    noise = impulse.abs().rolling(591, min_periods=max(591//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.353125 + 0.0016117 * anchor

def f26_dlr_517_struct_v517(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=125, w2=241, w3=604, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 125)
    acceleration = _rolling_slope(velocity, 241)
    curvature = _rolling_slope(acceleration, 604)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1942 * acceleration + 0.0016118 * anchor

def f26_dlr_518_struct_v518(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=132, w2=252, w3=617, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(132, min_periods=max(132//3, 2)).mean(), upside.rolling(252, min_periods=max(252//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.381875 + 0.0016119 * anchor

def f26_dlr_519_struct_v519(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=139, w2=263, w3=630, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(263, min_periods=max(263//3, 2)).max()
    rebound = x - x.rolling(139, min_periods=max(139//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2094 * _rolling_slope(draw, 630) + 0.001612 * anchor

def f26_dlr_520_struct_v520(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=146, w2=274, w3=643, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 146)
    baseline = trend.rolling(274, min_periods=max(274//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(643, min_periods=max(643//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.410625 + 0.0016121 * anchor

def f26_dlr_521_struct_v521(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=153, w2=285, w3=656, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 153)
    slow = _rolling_slope(x, 285)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.425 + 0.0016122 * anchor

def f26_dlr_522_struct_v522(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=160, w2=296, w3=669, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(296, min_periods=max(296//3, 2)).max()
    trough = x.rolling(160, min_periods=max(160//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.439375 + 0.0016123 * anchor

def f26_dlr_523_struct_v523(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=167, w2=307, w3=682, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(307, min_periods=max(307//3, 2)).rank(pct=True)
    persistence = change.rolling(682, min_periods=max(682//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2398 * persistence + 0.0016124 * anchor

def f26_dlr_524_struct_v524(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=174, w2=318, w3=695, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(174, min_periods=max(174//3, 2)).std()
    vol_slow = ret.rolling(318, min_periods=max(318//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.468125 + 0.0016125 * anchor

def f26_dlr_525_struct_v525(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=181, w2=329, w3=708, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(329, min_periods=max(329//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 181)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.255 * slope + 0.0016126 * anchor
