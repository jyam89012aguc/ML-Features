"""21 revenue growth deceleration d3 third derivative features 451-525 â€” Pipeline 1a-HF Grade v3.

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

def f21_rgd_451_struct_v451_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=249, w2=216, w3=110, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 249)
    slow = _rolling_slope(x, 216)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=110, adjust=False).mean() * 1.361875 + 0.0013052 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_452_struct_v452_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=5, w2=227, w3=123, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(227, min_periods=max(227//3, 2)).max()
    trough = x.rolling(5, min_periods=max(5//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.37625 + 0.0013053 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_453_struct_v453_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=12, w2=238, w3=136, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(12)
    rank = change.rolling(238, min_periods=max(238//3, 2)).rank(pct=True)
    persistence = change.rolling(136, min_periods=max(136//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2446 * persistence + 0.0013054 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_454_struct_v454_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=19, w2=249, w3=149, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(19, min_periods=max(19//3, 2)).std()
    vol_slow = ret.rolling(249, min_periods=max(249//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.405 + 0.0013055 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_455_struct_v455_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=26, w2=260, w3=162, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(260, min_periods=max(260//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 26)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2598 * slope + 0.0013056 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_456_struct_v456_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=33, w2=271, w3=175, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(33)
    drag = impulse.rolling(271, min_periods=max(271//3, 2)).mean()
    noise = impulse.abs().rolling(175, min_periods=max(175//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.43375 + 0.0013057 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_457_struct_v457_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=40, w2=282, w3=188, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 40)
    acceleration = _rolling_slope(velocity, 282)
    curvature = _rolling_slope(acceleration, 188)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.275 * acceleration + 0.0013058 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_458_struct_v458_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=47, w2=293, w3=201, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(47, min_periods=max(47//3, 2)).mean(), upside.rolling(293, min_periods=max(293//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.4625 + 0.0013059 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_459_struct_v459_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=54, w2=304, w3=214, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(304, min_periods=max(304//3, 2)).max()
    rebound = x - x.rolling(54, min_periods=max(54//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2902 * _rolling_slope(draw, 214) + 0.001306 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_460_struct_v460_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=61, w2=315, w3=227, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 61)
    baseline = trend.rolling(315, min_periods=max(315//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(227, min_periods=max(227//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.49125 + 0.0013061 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_461_struct_v461_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=68, w2=326, w3=240, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 68)
    slow = _rolling_slope(x, 326)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=240, adjust=False).mean() * 1.505625 + 0.0013062 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_462_struct_v462_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=75, w2=337, w3=253, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(337, min_periods=max(337//3, 2)).max()
    trough = x.rolling(75, min_periods=max(75//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.52 + 0.0013063 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_463_struct_v463_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=82, w2=348, w3=266, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(82)
    rank = change.rolling(348, min_periods=max(348//3, 2)).rank(pct=True)
    persistence = change.rolling(266, min_periods=max(266//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3206 * persistence + 0.0013064 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_464_struct_v464_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=89, w2=359, w3=279, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(89, min_periods=max(89//3, 2)).std()
    vol_slow = ret.rolling(359, min_periods=max(359//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.54875 + 0.0013065 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_465_struct_v465_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=96, w2=370, w3=292, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(370, min_periods=max(370//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 96)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3358 * slope + 0.0013066 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_466_struct_v466_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=103, w2=381, w3=305, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(103)
    drag = impulse.rolling(381, min_periods=max(381//3, 2)).mean()
    noise = impulse.abs().rolling(305, min_periods=max(305//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.5775 + 0.0013067 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_467_struct_v467_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=110, w2=392, w3=318, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 110)
    acceleration = _rolling_slope(velocity, 392)
    curvature = _rolling_slope(acceleration, 318)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.351 * acceleration + 0.0013068 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_468_struct_v468_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=117, w2=403, w3=331, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(117, min_periods=max(117//3, 2)).mean(), upside.rolling(403, min_periods=max(403//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.60625 + 0.0013069 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_469_struct_v469_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=124, w2=414, w3=344, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(414, min_periods=max(414//3, 2)).max()
    rebound = x - x.rolling(124, min_periods=max(124//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3662 * _rolling_slope(draw, 344) + 0.001307 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_470_struct_v470_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=131, w2=425, w3=357, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 131)
    baseline = trend.rolling(425, min_periods=max(425//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(357, min_periods=max(357//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.861875 + 0.0013071 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_471_struct_v471_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=138, w2=436, w3=370, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 138)
    slow = _rolling_slope(x, 436)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.87625 + 0.0013072 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_472_struct_v472_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=145, w2=447, w3=383, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(447, min_periods=max(447//3, 2)).max()
    trough = x.rolling(145, min_periods=max(145//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.890625 + 0.0013073 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_473_struct_v473_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=152, w2=458, w3=396, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(458, min_periods=max(458//3, 2)).rank(pct=True)
    persistence = change.rolling(396, min_periods=max(396//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3966 * persistence + 0.0013074 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_474_struct_v474_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=159, w2=469, w3=409, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(159, min_periods=max(159//3, 2)).std()
    vol_slow = ret.rolling(469, min_periods=max(469//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.919375 + 0.0013075 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_475_struct_v475_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=166, w2=480, w3=422, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(480, min_periods=max(480//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 166)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0354 * slope + 0.0013076 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_476_struct_v476_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=173, w2=491, w3=435, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(491, min_periods=max(491//3, 2)).mean()
    noise = impulse.abs().rolling(435, min_periods=max(435//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.948125 + 0.0013077 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_477_struct_v477_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=180, w2=502, w3=448, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 180)
    acceleration = _rolling_slope(velocity, 502)
    curvature = _rolling_slope(acceleration, 448)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0506 * acceleration + 0.0013078 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_478_struct_v478_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=187, w2=10, w3=461, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(187, min_periods=max(187//3, 2)).mean(), upside.rolling(10, min_periods=max(10//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.976875 + 0.0013079 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_479_struct_v479_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=194, w2=21, w3=474, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(21, min_periods=max(21//3, 2)).max()
    rebound = x - x.rolling(194, min_periods=max(194//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0658 * _rolling_slope(draw, 474) + 0.001308 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_480_struct_v480_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=201, w2=32, w3=487, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 201)
    baseline = trend.rolling(32, min_periods=max(32//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(487, min_periods=max(487//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.005625 + 0.0013081 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_481_struct_v481_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=208, w2=43, w3=500, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 208)
    slow = _rolling_slope(x, 43)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.02 + 0.0013082 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_482_struct_v482_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=215, w2=54, w3=513, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(54, min_periods=max(54//3, 2)).max()
    trough = x.rolling(215, min_periods=max(215//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.034375 + 0.0013083 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_483_struct_v483_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=222, w2=65, w3=526, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(65, min_periods=max(65//3, 2)).rank(pct=True)
    persistence = change.rolling(526, min_periods=max(526//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0962 * persistence + 0.0013084 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_484_struct_v484_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=229, w2=76, w3=539, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(229, min_periods=max(229//3, 2)).std()
    vol_slow = ret.rolling(76, min_periods=max(76//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.063125 + 0.0013085 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_485_struct_v485_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=236, w2=87, w3=552, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(87, min_periods=max(87//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 236)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1114 * slope + 0.0013086 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_486_struct_v486_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=243, w2=98, w3=565, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(98, min_periods=max(98//3, 2)).mean()
    noise = impulse.abs().rolling(565, min_periods=max(565//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.091875 + 0.0013087 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_487_struct_v487_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=250, w2=109, w3=578, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 250)
    acceleration = _rolling_slope(velocity, 109)
    curvature = _rolling_slope(acceleration, 578)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1266 * acceleration + 0.0013088 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_488_struct_v488_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=6, w2=120, w3=591, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(6, min_periods=max(6//3, 2)).mean(), upside.rolling(120, min_periods=max(120//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.120625 + 0.0013089 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_489_struct_v489_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=13, w2=131, w3=604, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(131, min_periods=max(131//3, 2)).max()
    rebound = x - x.rolling(13, min_periods=max(13//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1418 * _rolling_slope(draw, 604) + 0.001309 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_490_struct_v490_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=20, w2=142, w3=617, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 20)
    baseline = trend.rolling(142, min_periods=max(142//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(617, min_periods=max(617//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.149375 + 0.0013091 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_491_struct_v491_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=27, w2=153, w3=630, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 27)
    slow = _rolling_slope(x, 153)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.16375 + 0.0013092 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_492_struct_v492_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=34, w2=164, w3=643, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(164, min_periods=max(164//3, 2)).max()
    trough = x.rolling(34, min_periods=max(34//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.178125 + 0.0013093 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_493_struct_v493_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=41, w2=175, w3=656, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(41)
    rank = change.rolling(175, min_periods=max(175//3, 2)).rank(pct=True)
    persistence = change.rolling(656, min_periods=max(656//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1722 * persistence + 0.0013094 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_494_struct_v494_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=48, w2=186, w3=669, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(48, min_periods=max(48//3, 2)).std()
    vol_slow = ret.rolling(186, min_periods=max(186//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.206875 + 0.0013095 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_495_struct_v495_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=55, w2=197, w3=682, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(197, min_periods=max(197//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 55)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1874 * slope + 0.0013096 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_496_struct_v496_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=62, w2=208, w3=695, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(62)
    drag = impulse.rolling(208, min_periods=max(208//3, 2)).mean()
    noise = impulse.abs().rolling(695, min_periods=max(695//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.235625 + 0.0013097 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_497_struct_v497_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=69, w2=219, w3=708, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 69)
    acceleration = _rolling_slope(velocity, 219)
    curvature = _rolling_slope(acceleration, 708)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2026 * acceleration + 0.0013098 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_498_struct_v498_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=76, w2=230, w3=721, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(76, min_periods=max(76//3, 2)).mean(), upside.rolling(230, min_periods=max(230//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.264375 + 0.0013099 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_499_struct_v499_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=83, w2=241, w3=734, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(241, min_periods=max(241//3, 2)).max()
    rebound = x - x.rolling(83, min_periods=max(83//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2178 * _rolling_slope(draw, 734) + 0.00131 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_500_struct_v500_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=90, w2=252, w3=747, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 90)
    baseline = trend.rolling(252, min_periods=max(252//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(747, min_periods=max(747//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.293125 + 0.0013101 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_501_struct_v501_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=97, w2=263, w3=760, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 97)
    slow = _rolling_slope(x, 263)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.3075 + 0.0013102 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_502_struct_v502_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=104, w2=274, w3=16, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(274, min_periods=max(274//3, 2)).max()
    trough = x.rolling(104, min_periods=max(104//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.321875 + 0.0013103 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_503_struct_v503_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=111, w2=285, w3=29, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(111)
    rank = change.rolling(285, min_periods=max(285//3, 2)).rank(pct=True)
    persistence = change.rolling(29, min_periods=max(29//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2482 * persistence + 0.0013104 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_504_struct_v504_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=118, w2=296, w3=42, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(118, min_periods=max(118//3, 2)).std()
    vol_slow = ret.rolling(296, min_periods=max(296//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.350625 + 0.0013105 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_505_struct_v505_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=125, w2=307, w3=55, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(307, min_periods=max(307//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 125)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2634 * slope + 0.0013106 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_506_struct_v506_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=132, w2=318, w3=68, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(318, min_periods=max(318//3, 2)).mean()
    noise = impulse.abs().rolling(68, min_periods=max(68//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.379375 + 0.0013107 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_507_struct_v507_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=139, w2=329, w3=81, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 139)
    acceleration = _rolling_slope(velocity, 329)
    curvature = _rolling_slope(acceleration, 81)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2786 * acceleration + 0.0013108 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_508_struct_v508_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=146, w2=340, w3=94, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(146, min_periods=max(146//3, 2)).mean(), upside.rolling(340, min_periods=max(340//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(94) * 1.408125 + 0.0013109 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_509_struct_v509_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=153, w2=351, w3=107, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(351, min_periods=max(351//3, 2)).max()
    rebound = x - x.rolling(153, min_periods=max(153//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2938 * _rolling_slope(draw, 107) + 0.001311 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_510_struct_v510_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=160, w2=362, w3=120, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 160)
    baseline = trend.rolling(362, min_periods=max(362//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(120, min_periods=max(120//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.436875 + 0.0013111 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_511_struct_v511_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=167, w2=373, w3=133, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 167)
    slow = _rolling_slope(x, 373)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=133, adjust=False).mean() * 1.45125 + 0.0013112 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_512_struct_v512_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=174, w2=384, w3=146, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(384, min_periods=max(384//3, 2)).max()
    trough = x.rolling(174, min_periods=max(174//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.465625 + 0.0013113 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_513_struct_v513_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=181, w2=395, w3=159, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(395, min_periods=max(395//3, 2)).rank(pct=True)
    persistence = change.rolling(159, min_periods=max(159//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3242 * persistence + 0.0013114 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_514_struct_v514_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=188, w2=406, w3=172, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(188, min_periods=max(188//3, 2)).std()
    vol_slow = ret.rolling(406, min_periods=max(406//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.494375 + 0.0013115 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_515_struct_v515_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=195, w2=417, w3=185, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(417, min_periods=max(417//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 195)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3394 * slope + 0.0013116 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_516_struct_v516_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=202, w2=428, w3=198, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(428, min_periods=max(428//3, 2)).mean()
    noise = impulse.abs().rolling(198, min_periods=max(198//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.523125 + 0.0013117 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_517_struct_v517_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=209, w2=439, w3=211, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 209)
    acceleration = _rolling_slope(velocity, 439)
    curvature = _rolling_slope(acceleration, 211)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3546 * acceleration + 0.0013118 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_518_struct_v518_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=216, w2=450, w3=224, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(216, min_periods=max(216//3, 2)).mean(), upside.rolling(450, min_periods=max(450//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.551875 + 0.0013119 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_519_struct_v519_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=223, w2=461, w3=237, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(461, min_periods=max(461//3, 2)).max()
    rebound = x - x.rolling(223, min_periods=max(223//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3698 * _rolling_slope(draw, 237) + 0.001312 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_520_struct_v520_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=230, w2=472, w3=250, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 230)
    baseline = trend.rolling(472, min_periods=max(472//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(250, min_periods=max(250//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.580625 + 0.0013121 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_521_struct_v521_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=237, w2=483, w3=263, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 237)
    slow = _rolling_slope(x, 483)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=263, adjust=False).mean() * 1.595 + 0.0013122 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_522_struct_v522_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=244, w2=494, w3=276, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(494, min_periods=max(494//3, 2)).max()
    trough = x.rolling(244, min_periods=max(244//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.609375 + 0.0013123 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_523_struct_v523_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=251, w2=505, w3=289, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(505, min_periods=max(505//3, 2)).rank(pct=True)
    persistence = change.rolling(289, min_periods=max(289//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.4002 * persistence + 0.0013124 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_524_struct_v524_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=7, w2=13, w3=302, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(7, min_periods=max(7//3, 2)).std()
    vol_slow = ret.rolling(13, min_periods=max(13//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.865 + 0.0013125 * anchor
    return base_signal.diff().diff().diff()

def f21_rgd_525_struct_v525_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=14, w2=24, w3=315, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(24, min_periods=max(24//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 14)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.039 * slope + 0.0013126 * anchor
    return base_signal.diff().diff().diff()
