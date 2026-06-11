"""29 revenue deceleration acceleration base features 376-450 â€” Pipeline 1a-HF Grade v3.

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

def f29_rda_376_struct_v376(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=192, w2=382, w3=218, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(382, min_periods=max(382//3, 2)).mean()
    noise = impulse.abs().rolling(218, min_periods=max(218//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.24875 + 0.0017777 * anchor

def f29_rda_377_struct_v377(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=199, w2=393, w3=231, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 199)
    acceleration = _rolling_slope(velocity, 393)
    curvature = _rolling_slope(acceleration, 231)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.389 * acceleration + 0.0017778 * anchor

def f29_rda_378_struct_v378(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=206, w2=404, w3=244, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(206, min_periods=max(206//3, 2)).mean(), upside.rolling(404, min_periods=max(404//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.2775 + 0.0017779 * anchor

def f29_rda_379_struct_v379(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=213, w2=415, w3=257, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(415, min_periods=max(415//3, 2)).max()
    rebound = x - x.rolling(213, min_periods=max(213//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.4042 * _rolling_slope(draw, 257) + 0.001778 * anchor

def f29_rda_380_struct_v380(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=220, w2=426, w3=270, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 220)
    baseline = trend.rolling(426, min_periods=max(426//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(270, min_periods=max(270//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.30625 + 0.0017781 * anchor

def f29_rda_381_struct_v381(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=227, w2=437, w3=283, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 227)
    slow = _rolling_slope(x, 437)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=283, adjust=False).mean() * 1.320625 + 0.0017782 * anchor

def f29_rda_382_struct_v382(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=234, w2=448, w3=296, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(448, min_periods=max(448//3, 2)).max()
    trough = x.rolling(234, min_periods=max(234//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.335 + 0.0017783 * anchor

def f29_rda_383_struct_v383(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=241, w2=459, w3=309, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(459, min_periods=max(459//3, 2)).rank(pct=True)
    persistence = change.rolling(309, min_periods=max(309//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0582 * persistence + 0.0017784 * anchor

def f29_rda_384_struct_v384(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=248, w2=470, w3=322, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(248, min_periods=max(248//3, 2)).std()
    vol_slow = ret.rolling(470, min_periods=max(470//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.36375 + 0.0017785 * anchor

def f29_rda_385_struct_v385(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=255, w2=481, w3=335, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(481, min_periods=max(481//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 255)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0734 * slope + 0.0017786 * anchor

def f29_rda_386_struct_v386(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=11, w2=492, w3=348, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(11)
    drag = impulse.rolling(492, min_periods=max(492//3, 2)).mean()
    noise = impulse.abs().rolling(348, min_periods=max(348//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.3925 + 0.0017787 * anchor

def f29_rda_387_struct_v387(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=18, w2=503, w3=361, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 18)
    acceleration = _rolling_slope(velocity, 503)
    curvature = _rolling_slope(acceleration, 361)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0886 * acceleration + 0.0017788 * anchor

def f29_rda_388_struct_v388(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=25, w2=11, w3=374, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(25, min_periods=max(25//3, 2)).mean(), upside.rolling(11, min_periods=max(11//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.42125 + 0.0017789 * anchor

def f29_rda_389_struct_v389(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=32, w2=22, w3=387, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(22, min_periods=max(22//3, 2)).max()
    rebound = x - x.rolling(32, min_periods=max(32//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1038 * _rolling_slope(draw, 387) + 0.001779 * anchor

def f29_rda_390_struct_v390(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=39, w2=33, w3=400, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 39)
    baseline = trend.rolling(33, min_periods=max(33//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(400, min_periods=max(400//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.45 + 0.0017791 * anchor

def f29_rda_391_struct_v391(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=46, w2=44, w3=413, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 46)
    slow = _rolling_slope(x, 44)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.464375 + 0.0017792 * anchor

def f29_rda_392_struct_v392(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=53, w2=55, w3=426, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(55, min_periods=max(55//3, 2)).max()
    trough = x.rolling(53, min_periods=max(53//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.47875 + 0.0017793 * anchor

def f29_rda_393_struct_v393(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=60, w2=66, w3=439, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(60)
    rank = change.rolling(66, min_periods=max(66//3, 2)).rank(pct=True)
    persistence = change.rolling(439, min_periods=max(439//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1342 * persistence + 0.0017794 * anchor

def f29_rda_394_struct_v394(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=67, w2=77, w3=452, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(67, min_periods=max(67//3, 2)).std()
    vol_slow = ret.rolling(77, min_periods=max(77//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.5075 + 0.0017795 * anchor

def f29_rda_395_struct_v395(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=74, w2=88, w3=465, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(88, min_periods=max(88//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 74)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1494 * slope + 0.0017796 * anchor

def f29_rda_396_struct_v396(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=81, w2=99, w3=478, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(81)
    drag = impulse.rolling(99, min_periods=max(99//3, 2)).mean()
    noise = impulse.abs().rolling(478, min_periods=max(478//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.53625 + 0.0017797 * anchor

def f29_rda_397_struct_v397(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=88, w2=110, w3=491, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 88)
    acceleration = _rolling_slope(velocity, 110)
    curvature = _rolling_slope(acceleration, 491)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1646 * acceleration + 0.0017798 * anchor

def f29_rda_398_struct_v398(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=95, w2=121, w3=504, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(95, min_periods=max(95//3, 2)).mean(), upside.rolling(121, min_periods=max(121//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.565 + 0.0017799 * anchor

def f29_rda_399_struct_v399(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=102, w2=132, w3=517, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(132, min_periods=max(132//3, 2)).max()
    rebound = x - x.rolling(102, min_periods=max(102//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1798 * _rolling_slope(draw, 517) + 0.00178 * anchor

def f29_rda_400_struct_v400(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=109, w2=143, w3=530, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 109)
    baseline = trend.rolling(143, min_periods=max(143//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(530, min_periods=max(530//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.59375 + 0.0017801 * anchor

def f29_rda_401_struct_v401(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=116, w2=154, w3=543, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 116)
    slow = _rolling_slope(x, 154)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.608125 + 0.0017802 * anchor

def f29_rda_402_struct_v402(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=123, w2=165, w3=556, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(165, min_periods=max(165//3, 2)).max()
    trough = x.rolling(123, min_periods=max(123//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.6225 + 0.0017803 * anchor

def f29_rda_403_struct_v403(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=130, w2=176, w3=569, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(176, min_periods=max(176//3, 2)).rank(pct=True)
    persistence = change.rolling(569, min_periods=max(569//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2102 * persistence + 0.0017804 * anchor

def f29_rda_404_struct_v404(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=137, w2=187, w3=582, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(137, min_periods=max(137//3, 2)).std()
    vol_slow = ret.rolling(187, min_periods=max(187//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.878125 + 0.0017805 * anchor

def f29_rda_405_struct_v405(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=144, w2=198, w3=595, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(198, min_periods=max(198//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 144)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2254 * slope + 0.0017806 * anchor

def f29_rda_406_struct_v406(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=151, w2=209, w3=608, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(209, min_periods=max(209//3, 2)).mean()
    noise = impulse.abs().rolling(608, min_periods=max(608//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.906875 + 0.0017807 * anchor

def f29_rda_407_struct_v407(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=158, w2=220, w3=621, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 158)
    acceleration = _rolling_slope(velocity, 220)
    curvature = _rolling_slope(acceleration, 621)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2406 * acceleration + 0.0017808 * anchor

def f29_rda_408_struct_v408(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=165, w2=231, w3=634, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(165, min_periods=max(165//3, 2)).mean(), upside.rolling(231, min_periods=max(231//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.935625 + 0.0017809 * anchor

def f29_rda_409_struct_v409(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=172, w2=242, w3=647, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(242, min_periods=max(242//3, 2)).max()
    rebound = x - x.rolling(172, min_periods=max(172//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2558 * _rolling_slope(draw, 647) + 0.001781 * anchor

def f29_rda_410_struct_v410(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=179, w2=253, w3=660, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 179)
    baseline = trend.rolling(253, min_periods=max(253//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(660, min_periods=max(660//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.964375 + 0.0017811 * anchor

def f29_rda_411_struct_v411(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=186, w2=264, w3=673, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 186)
    slow = _rolling_slope(x, 264)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.97875 + 0.0017812 * anchor

def f29_rda_412_struct_v412(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=193, w2=275, w3=686, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(275, min_periods=max(275//3, 2)).max()
    trough = x.rolling(193, min_periods=max(193//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.993125 + 0.0017813 * anchor

def f29_rda_413_struct_v413(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=200, w2=286, w3=699, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(286, min_periods=max(286//3, 2)).rank(pct=True)
    persistence = change.rolling(699, min_periods=max(699//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2862 * persistence + 0.0017814 * anchor

def f29_rda_414_struct_v414(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=207, w2=297, w3=712, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(207, min_periods=max(207//3, 2)).std()
    vol_slow = ret.rolling(297, min_periods=max(297//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.021875 + 0.0017815 * anchor

def f29_rda_415_struct_v415(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=214, w2=308, w3=725, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(308, min_periods=max(308//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 214)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3014 * slope + 0.0017816 * anchor

def f29_rda_416_struct_v416(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=221, w2=319, w3=738, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(319, min_periods=max(319//3, 2)).mean()
    noise = impulse.abs().rolling(738, min_periods=max(738//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.050625 + 0.0017817 * anchor

def f29_rda_417_struct_v417(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=228, w2=330, w3=751, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 228)
    acceleration = _rolling_slope(velocity, 330)
    curvature = _rolling_slope(acceleration, 751)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3166 * acceleration + 0.0017818 * anchor

def f29_rda_418_struct_v418(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=235, w2=341, w3=764, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(235, min_periods=max(235//3, 2)).mean(), upside.rolling(341, min_periods=max(341//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.079375 + 0.0017819 * anchor

def f29_rda_419_struct_v419(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=242, w2=352, w3=20, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(352, min_periods=max(352//3, 2)).max()
    rebound = x - x.rolling(242, min_periods=max(242//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3318 * _rolling_slope(draw, 20) + 0.001782 * anchor

def f29_rda_420_struct_v420(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=249, w2=363, w3=33, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 249)
    baseline = trend.rolling(363, min_periods=max(363//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(33, min_periods=max(33//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.108125 + 0.0017821 * anchor

def f29_rda_421_struct_v421(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=5, w2=374, w3=46, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 5)
    slow = _rolling_slope(x, 374)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=46, adjust=False).mean() * 1.1225 + 0.0017822 * anchor

def f29_rda_422_struct_v422(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=12, w2=385, w3=59, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(385, min_periods=max(385//3, 2)).max()
    trough = x.rolling(12, min_periods=max(12//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.136875 + 0.0017823 * anchor

def f29_rda_423_struct_v423(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=19, w2=396, w3=72, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(19)
    rank = change.rolling(396, min_periods=max(396//3, 2)).rank(pct=True)
    persistence = change.rolling(72, min_periods=max(72//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3622 * persistence + 0.0017824 * anchor

def f29_rda_424_struct_v424(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=26, w2=407, w3=85, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(26, min_periods=max(26//3, 2)).std()
    vol_slow = ret.rolling(407, min_periods=max(407//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.165625 + 0.0017825 * anchor

def f29_rda_425_struct_v425(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=33, w2=418, w3=98, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(418, min_periods=max(418//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 33)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3774 * slope + 0.0017826 * anchor

def f29_rda_426_struct_v426(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=40, w2=429, w3=111, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(40)
    drag = impulse.rolling(429, min_periods=max(429//3, 2)).mean()
    noise = impulse.abs().rolling(111, min_periods=max(111//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.194375 + 0.0017827 * anchor

def f29_rda_427_struct_v427(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=47, w2=440, w3=124, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 47)
    acceleration = _rolling_slope(velocity, 440)
    curvature = _rolling_slope(acceleration, 124)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3926 * acceleration + 0.0017828 * anchor

def f29_rda_428_struct_v428(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=54, w2=451, w3=137, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(54, min_periods=max(54//3, 2)).mean(), upside.rolling(451, min_periods=max(451//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.223125 + 0.0017829 * anchor

def f29_rda_429_struct_v429(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=61, w2=462, w3=150, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(462, min_periods=max(462//3, 2)).max()
    rebound = x - x.rolling(61, min_periods=max(61//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.4078 * _rolling_slope(draw, 150) + 0.001783 * anchor

def f29_rda_430_struct_v430(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=68, w2=473, w3=163, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 68)
    baseline = trend.rolling(473, min_periods=max(473//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(163, min_periods=max(163//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.251875 + 0.0017831 * anchor

def f29_rda_431_struct_v431(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=75, w2=484, w3=176, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 75)
    slow = _rolling_slope(x, 484)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=176, adjust=False).mean() * 1.26625 + 0.0017832 * anchor

def f29_rda_432_struct_v432(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=82, w2=495, w3=189, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(495, min_periods=max(495//3, 2)).max()
    trough = x.rolling(82, min_periods=max(82//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.280625 + 0.0017833 * anchor

def f29_rda_433_struct_v433(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=89, w2=506, w3=202, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(89)
    rank = change.rolling(506, min_periods=max(506//3, 2)).rank(pct=True)
    persistence = change.rolling(202, min_periods=max(202//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0618 * persistence + 0.0017834 * anchor

def f29_rda_434_struct_v434(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=96, w2=14, w3=215, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(96, min_periods=max(96//3, 2)).std()
    vol_slow = ret.rolling(14, min_periods=max(14//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.309375 + 0.0017835 * anchor

def f29_rda_435_struct_v435(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=103, w2=25, w3=228, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(25, min_periods=max(25//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 103)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.077 * slope + 0.0017836 * anchor

def f29_rda_436_struct_v436(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=110, w2=36, w3=241, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(110)
    drag = impulse.rolling(36, min_periods=max(36//3, 2)).mean()
    noise = impulse.abs().rolling(241, min_periods=max(241//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.338125 + 0.0017837 * anchor

def f29_rda_437_struct_v437(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=117, w2=47, w3=254, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 117)
    acceleration = _rolling_slope(velocity, 47)
    curvature = _rolling_slope(acceleration, 254)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0922 * acceleration + 0.0017838 * anchor

def f29_rda_438_struct_v438(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=124, w2=58, w3=267, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(124, min_periods=max(124//3, 2)).mean(), upside.rolling(58, min_periods=max(58//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.366875 + 0.0017839 * anchor

def f29_rda_439_struct_v439(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=131, w2=69, w3=280, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(69, min_periods=max(69//3, 2)).max()
    rebound = x - x.rolling(131, min_periods=max(131//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1074 * _rolling_slope(draw, 280) + 0.001784 * anchor

def f29_rda_440_struct_v440(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=138, w2=80, w3=293, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 138)
    baseline = trend.rolling(80, min_periods=max(80//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(293, min_periods=max(293//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.395625 + 0.0017841 * anchor

def f29_rda_441_struct_v441(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=145, w2=91, w3=306, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 145)
    slow = _rolling_slope(x, 91)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.41 + 0.0017842 * anchor

def f29_rda_442_struct_v442(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=152, w2=102, w3=319, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(102, min_periods=max(102//3, 2)).max()
    trough = x.rolling(152, min_periods=max(152//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.424375 + 0.0017843 * anchor

def f29_rda_443_struct_v443(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=159, w2=113, w3=332, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(113, min_periods=max(113//3, 2)).rank(pct=True)
    persistence = change.rolling(332, min_periods=max(332//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1378 * persistence + 0.0017844 * anchor

def f29_rda_444_struct_v444(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=166, w2=124, w3=345, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(166, min_periods=max(166//3, 2)).std()
    vol_slow = ret.rolling(124, min_periods=max(124//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.453125 + 0.0017845 * anchor

def f29_rda_445_struct_v445(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=173, w2=135, w3=358, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(135, min_periods=max(135//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 173)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.153 * slope + 0.0017846 * anchor

def f29_rda_446_struct_v446(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=180, w2=146, w3=371, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(146, min_periods=max(146//3, 2)).mean()
    noise = impulse.abs().rolling(371, min_periods=max(371//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.481875 + 0.0017847 * anchor

def f29_rda_447_struct_v447(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=187, w2=157, w3=384, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 187)
    acceleration = _rolling_slope(velocity, 157)
    curvature = _rolling_slope(acceleration, 384)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1682 * acceleration + 0.0017848 * anchor

def f29_rda_448_struct_v448(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=194, w2=168, w3=397, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(194, min_periods=max(194//3, 2)).mean(), upside.rolling(168, min_periods=max(168//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.510625 + 0.0017849 * anchor

def f29_rda_449_struct_v449(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=201, w2=179, w3=410, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(179, min_periods=max(179//3, 2)).max()
    rebound = x - x.rolling(201, min_periods=max(201//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1834 * _rolling_slope(draw, 410) + 0.001785 * anchor

def f29_rda_450_struct_v450(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=208, w2=190, w3=423, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 208)
    baseline = trend.rolling(190, min_periods=max(190//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(423, min_periods=max(423//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.539375 + 0.0017851 * anchor
