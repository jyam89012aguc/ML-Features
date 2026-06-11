"""21 revenue growth deceleration d2 second derivative features 376-450 â€” Pipeline 1a-HF Grade v3.

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

def f21_rgd_376_struct_v376_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=226, w2=397, w3=649, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(397, min_periods=max(397//3, 2)).mean()
    noise = impulse.abs().rolling(649, min_periods=max(649//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.056875 + 0.0012977 * anchor
    return base_signal.diff().diff()

def f21_rgd_377_struct_v377_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=233, w2=408, w3=662, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 233)
    acceleration = _rolling_slope(velocity, 408)
    curvature = _rolling_slope(acceleration, 662)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0434 * acceleration + 0.0012978 * anchor
    return base_signal.diff().diff()

def f21_rgd_378_struct_v378_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=240, w2=419, w3=675, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(240, min_periods=max(240//3, 2)).mean(), upside.rolling(419, min_periods=max(419//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.085625 + 0.0012979 * anchor
    return base_signal.diff().diff()

def f21_rgd_379_struct_v379_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=247, w2=430, w3=688, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(430, min_periods=max(430//3, 2)).max()
    rebound = x - x.rolling(247, min_periods=max(247//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0586 * _rolling_slope(draw, 688) + 0.001298 * anchor
    return base_signal.diff().diff()

def f21_rgd_380_struct_v380_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=254, w2=441, w3=701, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 254)
    baseline = trend.rolling(441, min_periods=max(441//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(701, min_periods=max(701//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.114375 + 0.0012981 * anchor
    return base_signal.diff().diff()

def f21_rgd_381_struct_v381_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=10, w2=452, w3=714, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 10)
    slow = _rolling_slope(x, 452)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.12875 + 0.0012982 * anchor
    return base_signal.diff().diff()

def f21_rgd_382_struct_v382_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=17, w2=463, w3=727, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(463, min_periods=max(463//3, 2)).max()
    trough = x.rolling(17, min_periods=max(17//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.143125 + 0.0012983 * anchor
    return base_signal.diff().diff()

def f21_rgd_383_struct_v383_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=24, w2=474, w3=740, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(24)
    rank = change.rolling(474, min_periods=max(474//3, 2)).rank(pct=True)
    persistence = change.rolling(740, min_periods=max(740//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.089 * persistence + 0.0012984 * anchor
    return base_signal.diff().diff()

def f21_rgd_384_struct_v384_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=31, w2=485, w3=753, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(31, min_periods=max(31//3, 2)).std()
    vol_slow = ret.rolling(485, min_periods=max(485//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.171875 + 0.0012985 * anchor
    return base_signal.diff().diff()

def f21_rgd_385_struct_v385_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=38, w2=496, w3=766, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(496, min_periods=max(496//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 38)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1042 * slope + 0.0012986 * anchor
    return base_signal.diff().diff()

def f21_rgd_386_struct_v386_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=45, w2=507, w3=22, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(45)
    drag = impulse.rolling(507, min_periods=max(507//3, 2)).mean()
    noise = impulse.abs().rolling(22, min_periods=max(22//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.200625 + 0.0012987 * anchor
    return base_signal.diff().diff()

def f21_rgd_387_struct_v387_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=52, w2=15, w3=35, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 52)
    acceleration = _rolling_slope(velocity, 15)
    curvature = _rolling_slope(acceleration, 35)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1194 * acceleration + 0.0012988 * anchor
    return base_signal.diff().diff()

def f21_rgd_388_struct_v388_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=59, w2=26, w3=48, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(59, min_periods=max(59//3, 2)).mean(), upside.rolling(26, min_periods=max(26//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(48) * 1.229375 + 0.0012989 * anchor
    return base_signal.diff().diff()

def f21_rgd_389_struct_v389_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=66, w2=37, w3=61, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(37, min_periods=max(37//3, 2)).max()
    rebound = x - x.rolling(66, min_periods=max(66//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1346 * _rolling_slope(draw, 61) + 0.001299 * anchor
    return base_signal.diff().diff()

def f21_rgd_390_struct_v390_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=73, w2=48, w3=74, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 73)
    baseline = trend.rolling(48, min_periods=max(48//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(74, min_periods=max(74//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.258125 + 0.0012991 * anchor
    return base_signal.diff().diff()

def f21_rgd_391_struct_v391_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=80, w2=59, w3=87, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 80)
    slow = _rolling_slope(x, 59)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=87, adjust=False).mean() * 1.2725 + 0.0012992 * anchor
    return base_signal.diff().diff()

def f21_rgd_392_struct_v392_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=87, w2=70, w3=100, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(70, min_periods=max(70//3, 2)).max()
    trough = x.rolling(87, min_periods=max(87//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.286875 + 0.0012993 * anchor
    return base_signal.diff().diff()

def f21_rgd_393_struct_v393_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=94, w2=81, w3=113, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(94)
    rank = change.rolling(81, min_periods=max(81//3, 2)).rank(pct=True)
    persistence = change.rolling(113, min_periods=max(113//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.165 * persistence + 0.0012994 * anchor
    return base_signal.diff().diff()

def f21_rgd_394_struct_v394_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=101, w2=92, w3=126, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(101, min_periods=max(101//3, 2)).std()
    vol_slow = ret.rolling(92, min_periods=max(92//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.315625 + 0.0012995 * anchor
    return base_signal.diff().diff()

def f21_rgd_395_struct_v395_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=108, w2=103, w3=139, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(103, min_periods=max(103//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 108)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1802 * slope + 0.0012996 * anchor
    return base_signal.diff().diff()

def f21_rgd_396_struct_v396_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=115, w2=114, w3=152, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(115)
    drag = impulse.rolling(114, min_periods=max(114//3, 2)).mean()
    noise = impulse.abs().rolling(152, min_periods=max(152//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.344375 + 0.0012997 * anchor
    return base_signal.diff().diff()

def f21_rgd_397_struct_v397_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=122, w2=125, w3=165, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 122)
    acceleration = _rolling_slope(velocity, 125)
    curvature = _rolling_slope(acceleration, 165)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1954 * acceleration + 0.0012998 * anchor
    return base_signal.diff().diff()

def f21_rgd_398_struct_v398_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=129, w2=136, w3=178, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(129, min_periods=max(129//3, 2)).mean(), upside.rolling(136, min_periods=max(136//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.373125 + 0.0012999 * anchor
    return base_signal.diff().diff()

def f21_rgd_399_struct_v399_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=136, w2=147, w3=191, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(147, min_periods=max(147//3, 2)).max()
    rebound = x - x.rolling(136, min_periods=max(136//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2106 * _rolling_slope(draw, 191) + 0.0013 * anchor
    return base_signal.diff().diff()

def f21_rgd_400_struct_v400_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=143, w2=158, w3=204, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 143)
    baseline = trend.rolling(158, min_periods=max(158//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(204, min_periods=max(204//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.401875 + 0.0013001 * anchor
    return base_signal.diff().diff()

def f21_rgd_401_struct_v401_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=150, w2=169, w3=217, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 150)
    slow = _rolling_slope(x, 169)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=217, adjust=False).mean() * 1.41625 + 0.0013002 * anchor
    return base_signal.diff().diff()

def f21_rgd_402_struct_v402_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=157, w2=180, w3=230, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(180, min_periods=max(180//3, 2)).max()
    trough = x.rolling(157, min_periods=max(157//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.430625 + 0.0013003 * anchor
    return base_signal.diff().diff()

def f21_rgd_403_struct_v403_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=164, w2=191, w3=243, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(191, min_periods=max(191//3, 2)).rank(pct=True)
    persistence = change.rolling(243, min_periods=max(243//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.241 * persistence + 0.0013004 * anchor
    return base_signal.diff().diff()

def f21_rgd_404_struct_v404_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=171, w2=202, w3=256, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(171, min_periods=max(171//3, 2)).std()
    vol_slow = ret.rolling(202, min_periods=max(202//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.459375 + 0.0013005 * anchor
    return base_signal.diff().diff()

def f21_rgd_405_struct_v405_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=178, w2=213, w3=269, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(213, min_periods=max(213//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 178)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2562 * slope + 0.0013006 * anchor
    return base_signal.diff().diff()

def f21_rgd_406_struct_v406_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=185, w2=224, w3=282, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(224, min_periods=max(224//3, 2)).mean()
    noise = impulse.abs().rolling(282, min_periods=max(282//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.488125 + 0.0013007 * anchor
    return base_signal.diff().diff()

def f21_rgd_407_struct_v407_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=192, w2=235, w3=295, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 192)
    acceleration = _rolling_slope(velocity, 235)
    curvature = _rolling_slope(acceleration, 295)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2714 * acceleration + 0.0013008 * anchor
    return base_signal.diff().diff()

def f21_rgd_408_struct_v408_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=199, w2=246, w3=308, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(199, min_periods=max(199//3, 2)).mean(), upside.rolling(246, min_periods=max(246//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.516875 + 0.0013009 * anchor
    return base_signal.diff().diff()

def f21_rgd_409_struct_v409_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=206, w2=257, w3=321, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(257, min_periods=max(257//3, 2)).max()
    rebound = x - x.rolling(206, min_periods=max(206//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2866 * _rolling_slope(draw, 321) + 0.001301 * anchor
    return base_signal.diff().diff()

def f21_rgd_410_struct_v410_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=213, w2=268, w3=334, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 213)
    baseline = trend.rolling(268, min_periods=max(268//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(334, min_periods=max(334//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.545625 + 0.0013011 * anchor
    return base_signal.diff().diff()

def f21_rgd_411_struct_v411_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=220, w2=279, w3=347, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 220)
    slow = _rolling_slope(x, 279)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.56 + 0.0013012 * anchor
    return base_signal.diff().diff()

def f21_rgd_412_struct_v412_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=227, w2=290, w3=360, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(290, min_periods=max(290//3, 2)).max()
    trough = x.rolling(227, min_periods=max(227//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.574375 + 0.0013013 * anchor
    return base_signal.diff().diff()

def f21_rgd_413_struct_v413_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=234, w2=301, w3=373, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(301, min_periods=max(301//3, 2)).rank(pct=True)
    persistence = change.rolling(373, min_periods=max(373//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.317 * persistence + 0.0013014 * anchor
    return base_signal.diff().diff()

def f21_rgd_414_struct_v414_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=241, w2=312, w3=386, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(241, min_periods=max(241//3, 2)).std()
    vol_slow = ret.rolling(312, min_periods=max(312//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.603125 + 0.0013015 * anchor
    return base_signal.diff().diff()

def f21_rgd_415_struct_v415_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=248, w2=323, w3=399, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(323, min_periods=max(323//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 248)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3322 * slope + 0.0013016 * anchor
    return base_signal.diff().diff()

def f21_rgd_416_struct_v416_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=255, w2=334, w3=412, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(334, min_periods=max(334//3, 2)).mean()
    noise = impulse.abs().rolling(412, min_periods=max(412//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.85875 + 0.0013017 * anchor
    return base_signal.diff().diff()

def f21_rgd_417_struct_v417_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=11, w2=345, w3=425, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 11)
    acceleration = _rolling_slope(velocity, 345)
    curvature = _rolling_slope(acceleration, 425)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3474 * acceleration + 0.0013018 * anchor
    return base_signal.diff().diff()

def f21_rgd_418_struct_v418_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=18, w2=356, w3=438, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(18, min_periods=max(18//3, 2)).mean(), upside.rolling(356, min_periods=max(356//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.8875 + 0.0013019 * anchor
    return base_signal.diff().diff()

def f21_rgd_419_struct_v419_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=25, w2=367, w3=451, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(367, min_periods=max(367//3, 2)).max()
    rebound = x - x.rolling(25, min_periods=max(25//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3626 * _rolling_slope(draw, 451) + 0.001302 * anchor
    return base_signal.diff().diff()

def f21_rgd_420_struct_v420_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=32, w2=378, w3=464, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 32)
    baseline = trend.rolling(378, min_periods=max(378//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(464, min_periods=max(464//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.91625 + 0.0013021 * anchor
    return base_signal.diff().diff()

def f21_rgd_421_struct_v421_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=39, w2=389, w3=477, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 39)
    slow = _rolling_slope(x, 389)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.930625 + 0.0013022 * anchor
    return base_signal.diff().diff()

def f21_rgd_422_struct_v422_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=46, w2=400, w3=490, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(400, min_periods=max(400//3, 2)).max()
    trough = x.rolling(46, min_periods=max(46//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.945 + 0.0013023 * anchor
    return base_signal.diff().diff()

def f21_rgd_423_struct_v423_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=53, w2=411, w3=503, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(53)
    rank = change.rolling(411, min_periods=max(411//3, 2)).rank(pct=True)
    persistence = change.rolling(503, min_periods=max(503//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.393 * persistence + 0.0013024 * anchor
    return base_signal.diff().diff()

def f21_rgd_424_struct_v424_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=60, w2=422, w3=516, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(60, min_periods=max(60//3, 2)).std()
    vol_slow = ret.rolling(422, min_periods=max(422//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.97375 + 0.0013025 * anchor
    return base_signal.diff().diff()

def f21_rgd_425_struct_v425_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=67, w2=433, w3=529, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(433, min_periods=max(433//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 67)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.4082 * slope + 0.0013026 * anchor
    return base_signal.diff().diff()

def f21_rgd_426_struct_v426_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=74, w2=444, w3=542, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(74)
    drag = impulse.rolling(444, min_periods=max(444//3, 2)).mean()
    noise = impulse.abs().rolling(542, min_periods=max(542//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.0025 + 0.0013027 * anchor
    return base_signal.diff().diff()

def f21_rgd_427_struct_v427_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=81, w2=455, w3=555, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 81)
    acceleration = _rolling_slope(velocity, 455)
    curvature = _rolling_slope(acceleration, 555)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.047 * acceleration + 0.0013028 * anchor
    return base_signal.diff().diff()

def f21_rgd_428_struct_v428_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=88, w2=466, w3=568, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(88, min_periods=max(88//3, 2)).mean(), upside.rolling(466, min_periods=max(466//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.03125 + 0.0013029 * anchor
    return base_signal.diff().diff()

def f21_rgd_429_struct_v429_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=95, w2=477, w3=581, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(477, min_periods=max(477//3, 2)).max()
    rebound = x - x.rolling(95, min_periods=max(95//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0622 * _rolling_slope(draw, 581) + 0.001303 * anchor
    return base_signal.diff().diff()

def f21_rgd_430_struct_v430_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=102, w2=488, w3=594, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 102)
    baseline = trend.rolling(488, min_periods=max(488//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(594, min_periods=max(594//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.06 + 0.0013031 * anchor
    return base_signal.diff().diff()

def f21_rgd_431_struct_v431_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=109, w2=499, w3=607, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 109)
    slow = _rolling_slope(x, 499)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.074375 + 0.0013032 * anchor
    return base_signal.diff().diff()

def f21_rgd_432_struct_v432_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=116, w2=510, w3=620, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(510, min_periods=max(510//3, 2)).max()
    trough = x.rolling(116, min_periods=max(116//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.08875 + 0.0013033 * anchor
    return base_signal.diff().diff()

def f21_rgd_433_struct_v433_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=123, w2=18, w3=633, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(123)
    rank = change.rolling(18, min_periods=max(18//3, 2)).rank(pct=True)
    persistence = change.rolling(633, min_periods=max(633//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0926 * persistence + 0.0013034 * anchor
    return base_signal.diff().diff()

def f21_rgd_434_struct_v434_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=130, w2=29, w3=646, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(130, min_periods=max(130//3, 2)).std()
    vol_slow = ret.rolling(29, min_periods=max(29//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.1175 + 0.0013035 * anchor
    return base_signal.diff().diff()

def f21_rgd_435_struct_v435_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=137, w2=40, w3=659, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(40, min_periods=max(40//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 137)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1078 * slope + 0.0013036 * anchor
    return base_signal.diff().diff()

def f21_rgd_436_struct_v436_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=144, w2=51, w3=672, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(51, min_periods=max(51//3, 2)).mean()
    noise = impulse.abs().rolling(672, min_periods=max(672//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.14625 + 0.0013037 * anchor
    return base_signal.diff().diff()

def f21_rgd_437_struct_v437_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=151, w2=62, w3=685, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 151)
    acceleration = _rolling_slope(velocity, 62)
    curvature = _rolling_slope(acceleration, 685)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.123 * acceleration + 0.0013038 * anchor
    return base_signal.diff().diff()

def f21_rgd_438_struct_v438_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=158, w2=73, w3=698, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(158, min_periods=max(158//3, 2)).mean(), upside.rolling(73, min_periods=max(73//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.175 + 0.0013039 * anchor
    return base_signal.diff().diff()

def f21_rgd_439_struct_v439_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=165, w2=84, w3=711, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(84, min_periods=max(84//3, 2)).max()
    rebound = x - x.rolling(165, min_periods=max(165//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1382 * _rolling_slope(draw, 711) + 0.001304 * anchor
    return base_signal.diff().diff()

def f21_rgd_440_struct_v440_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=172, w2=95, w3=724, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 172)
    baseline = trend.rolling(95, min_periods=max(95//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(724, min_periods=max(724//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.20375 + 0.0013041 * anchor
    return base_signal.diff().diff()

def f21_rgd_441_struct_v441_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=179, w2=106, w3=737, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 179)
    slow = _rolling_slope(x, 106)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.218125 + 0.0013042 * anchor
    return base_signal.diff().diff()

def f21_rgd_442_struct_v442_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=186, w2=117, w3=750, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(117, min_periods=max(117//3, 2)).max()
    trough = x.rolling(186, min_periods=max(186//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.2325 + 0.0013043 * anchor
    return base_signal.diff().diff()

def f21_rgd_443_struct_v443_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=193, w2=128, w3=763, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(128, min_periods=max(128//3, 2)).rank(pct=True)
    persistence = change.rolling(763, min_periods=max(763//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1686 * persistence + 0.0013044 * anchor
    return base_signal.diff().diff()

def f21_rgd_444_struct_v444_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=200, w2=139, w3=19, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(200, min_periods=max(200//3, 2)).std()
    vol_slow = ret.rolling(139, min_periods=max(139//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.26125 + 0.0013045 * anchor
    return base_signal.diff().diff()

def f21_rgd_445_struct_v445_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=207, w2=150, w3=32, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(150, min_periods=max(150//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 207)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1838 * slope + 0.0013046 * anchor
    return base_signal.diff().diff()

def f21_rgd_446_struct_v446_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=214, w2=161, w3=45, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(161, min_periods=max(161//3, 2)).mean()
    noise = impulse.abs().rolling(45, min_periods=max(45//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.29 + 0.0013047 * anchor
    return base_signal.diff().diff()

def f21_rgd_447_struct_v447_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=221, w2=172, w3=58, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 221)
    acceleration = _rolling_slope(velocity, 172)
    curvature = _rolling_slope(acceleration, 58)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.199 * acceleration + 0.0013048 * anchor
    return base_signal.diff().diff()

def f21_rgd_448_struct_v448_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=228, w2=183, w3=71, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(228, min_periods=max(228//3, 2)).mean(), upside.rolling(183, min_periods=max(183//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(71) * 1.31875 + 0.0013049 * anchor
    return base_signal.diff().diff()

def f21_rgd_449_struct_v449_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=235, w2=194, w3=84, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(194, min_periods=max(194//3, 2)).max()
    rebound = x - x.rolling(235, min_periods=max(235//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2142 * _rolling_slope(draw, 84) + 0.001305 * anchor
    return base_signal.diff().diff()

def f21_rgd_450_struct_v450_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=242, w2=205, w3=97, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 242)
    baseline = trend.rolling(205, min_periods=max(205//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(97, min_periods=max(97//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.3475 + 0.0013051 * anchor
    return base_signal.diff().diff()
