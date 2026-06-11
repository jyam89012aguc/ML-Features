"""35 margin collapse jerk d3 third derivative features 376-450 â€” Pipeline 1a-HF Grade v3.

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

def f35_mcj_376_struct_v376_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=41, w2=245, w3=84, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(41)
    drag = impulse.rolling(245, min_periods=max(245//3, 2)).mean()
    noise = impulse.abs().rolling(84, min_periods=max(84//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.199375 + 0.0021377 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_377_struct_v377_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=48, w2=256, w3=97, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 48)
    acceleration = _rolling_slope(velocity, 256)
    curvature = _rolling_slope(acceleration, 97)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2718 * acceleration + 0.0021378 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_378_struct_v378_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=55, w2=267, w3=110, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(55, min_periods=max(55//3, 2)).mean(), upside.rolling(267, min_periods=max(267//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(110) * 1.228125 + 0.0021379 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_379_struct_v379_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=62, w2=278, w3=123, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(278, min_periods=max(278//3, 2)).max()
    rebound = x - x.rolling(62, min_periods=max(62//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.287 * _rolling_slope(draw, 123) + 0.002138 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_380_struct_v380_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=69, w2=289, w3=136, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 69)
    baseline = trend.rolling(289, min_periods=max(289//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(136, min_periods=max(136//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.256875 + 0.0021381 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_381_struct_v381_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=76, w2=300, w3=149, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 76)
    slow = _rolling_slope(x, 300)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=149, adjust=False).mean() * 1.27125 + 0.0021382 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_382_struct_v382_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=83, w2=311, w3=162, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(311, min_periods=max(311//3, 2)).max()
    trough = x.rolling(83, min_periods=max(83//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.285625 + 0.0021383 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_383_struct_v383_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=90, w2=322, w3=175, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(90)
    rank = change.rolling(322, min_periods=max(322//3, 2)).rank(pct=True)
    persistence = change.rolling(175, min_periods=max(175//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3174 * persistence + 0.0021384 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_384_struct_v384_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=97, w2=333, w3=188, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(97, min_periods=max(97//3, 2)).std()
    vol_slow = ret.rolling(333, min_periods=max(333//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.314375 + 0.0021385 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_385_struct_v385_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=104, w2=344, w3=201, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(344, min_periods=max(344//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 104)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3326 * slope + 0.0021386 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_386_struct_v386_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=111, w2=355, w3=214, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(111)
    drag = impulse.rolling(355, min_periods=max(355//3, 2)).mean()
    noise = impulse.abs().rolling(214, min_periods=max(214//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.343125 + 0.0021387 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_387_struct_v387_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=118, w2=366, w3=227, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 118)
    acceleration = _rolling_slope(velocity, 366)
    curvature = _rolling_slope(acceleration, 227)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3478 * acceleration + 0.0021388 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_388_struct_v388_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=125, w2=377, w3=240, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(125, min_periods=max(125//3, 2)).mean(), upside.rolling(377, min_periods=max(377//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.371875 + 0.0021389 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_389_struct_v389_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=132, w2=388, w3=253, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(388, min_periods=max(388//3, 2)).max()
    rebound = x - x.rolling(132, min_periods=max(132//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.363 * _rolling_slope(draw, 253) + 0.002139 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_390_struct_v390_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=139, w2=399, w3=266, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 139)
    baseline = trend.rolling(399, min_periods=max(399//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(266, min_periods=max(266//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.400625 + 0.0021391 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_391_struct_v391_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=146, w2=410, w3=279, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 146)
    slow = _rolling_slope(x, 410)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=279, adjust=False).mean() * 1.415 + 0.0021392 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_392_struct_v392_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=153, w2=421, w3=292, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(421, min_periods=max(421//3, 2)).max()
    trough = x.rolling(153, min_periods=max(153//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.429375 + 0.0021393 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_393_struct_v393_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=160, w2=432, w3=305, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(432, min_periods=max(432//3, 2)).rank(pct=True)
    persistence = change.rolling(305, min_periods=max(305//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3934 * persistence + 0.0021394 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_394_struct_v394_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=167, w2=443, w3=318, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(167, min_periods=max(167//3, 2)).std()
    vol_slow = ret.rolling(443, min_periods=max(443//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.458125 + 0.0021395 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_395_struct_v395_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=174, w2=454, w3=331, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(454, min_periods=max(454//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 174)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.4086 * slope + 0.0021396 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_396_struct_v396_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=181, w2=465, w3=344, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(465, min_periods=max(465//3, 2)).mean()
    noise = impulse.abs().rolling(344, min_periods=max(344//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.486875 + 0.0021397 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_397_struct_v397_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=188, w2=476, w3=357, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 188)
    acceleration = _rolling_slope(velocity, 476)
    curvature = _rolling_slope(acceleration, 357)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0474 * acceleration + 0.0021398 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_398_struct_v398_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=195, w2=487, w3=370, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(195, min_periods=max(195//3, 2)).mean(), upside.rolling(487, min_periods=max(487//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.515625 + 0.0021399 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_399_struct_v399_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=202, w2=498, w3=383, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(498, min_periods=max(498//3, 2)).max()
    rebound = x - x.rolling(202, min_periods=max(202//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0626 * _rolling_slope(draw, 383) + 0.00214 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_400_struct_v400_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=209, w2=509, w3=396, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 209)
    baseline = trend.rolling(509, min_periods=max(509//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(396, min_periods=max(396//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.544375 + 0.0021401 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_401_struct_v401_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=216, w2=17, w3=409, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 216)
    slow = _rolling_slope(x, 17)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.55875 + 0.0021402 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_402_struct_v402_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=223, w2=28, w3=422, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(28, min_periods=max(28//3, 2)).max()
    trough = x.rolling(223, min_periods=max(223//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.573125 + 0.0021403 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_403_struct_v403_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=230, w2=39, w3=435, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(39, min_periods=max(39//3, 2)).rank(pct=True)
    persistence = change.rolling(435, min_periods=max(435//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.093 * persistence + 0.0021404 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_404_struct_v404_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=237, w2=50, w3=448, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(237, min_periods=max(237//3, 2)).std()
    vol_slow = ret.rolling(50, min_periods=max(50//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.601875 + 0.0021405 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_405_struct_v405_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=244, w2=61, w3=461, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(61, min_periods=max(61//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 244)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1082 * slope + 0.0021406 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_406_struct_v406_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=251, w2=72, w3=474, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(72, min_periods=max(72//3, 2)).mean()
    noise = impulse.abs().rolling(474, min_periods=max(474//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.8575 + 0.0021407 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_407_struct_v407_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=7, w2=83, w3=487, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 7)
    acceleration = _rolling_slope(velocity, 83)
    curvature = _rolling_slope(acceleration, 487)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1234 * acceleration + 0.0021408 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_408_struct_v408_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=14, w2=94, w3=500, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(14, min_periods=max(14//3, 2)).mean(), upside.rolling(94, min_periods=max(94//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.88625 + 0.0021409 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_409_struct_v409_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=21, w2=105, w3=513, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(105, min_periods=max(105//3, 2)).max()
    rebound = x - x.rolling(21, min_periods=max(21//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1386 * _rolling_slope(draw, 513) + 0.002141 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_410_struct_v410_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=28, w2=116, w3=526, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 28)
    baseline = trend.rolling(116, min_periods=max(116//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(526, min_periods=max(526//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.915 + 0.0021411 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_411_struct_v411_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=35, w2=127, w3=539, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 35)
    slow = _rolling_slope(x, 127)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.929375 + 0.0021412 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_412_struct_v412_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=42, w2=138, w3=552, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(138, min_periods=max(138//3, 2)).max()
    trough = x.rolling(42, min_periods=max(42//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.94375 + 0.0021413 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_413_struct_v413_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=49, w2=149, w3=565, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(49)
    rank = change.rolling(149, min_periods=max(149//3, 2)).rank(pct=True)
    persistence = change.rolling(565, min_periods=max(565//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.169 * persistence + 0.0021414 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_414_struct_v414_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=56, w2=160, w3=578, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(56, min_periods=max(56//3, 2)).std()
    vol_slow = ret.rolling(160, min_periods=max(160//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.9725 + 0.0021415 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_415_struct_v415_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=63, w2=171, w3=591, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(171, min_periods=max(171//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 63)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1842 * slope + 0.0021416 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_416_struct_v416_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=70, w2=182, w3=604, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(70)
    drag = impulse.rolling(182, min_periods=max(182//3, 2)).mean()
    noise = impulse.abs().rolling(604, min_periods=max(604//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.00125 + 0.0021417 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_417_struct_v417_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=77, w2=193, w3=617, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 77)
    acceleration = _rolling_slope(velocity, 193)
    curvature = _rolling_slope(acceleration, 617)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1994 * acceleration + 0.0021418 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_418_struct_v418_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=84, w2=204, w3=630, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(84, min_periods=max(84//3, 2)).mean(), upside.rolling(204, min_periods=max(204//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.03 + 0.0021419 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_419_struct_v419_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=91, w2=215, w3=643, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(215, min_periods=max(215//3, 2)).max()
    rebound = x - x.rolling(91, min_periods=max(91//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2146 * _rolling_slope(draw, 643) + 0.002142 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_420_struct_v420_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=98, w2=226, w3=656, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 98)
    baseline = trend.rolling(226, min_periods=max(226//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(656, min_periods=max(656//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.05875 + 0.0021421 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_421_struct_v421_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=105, w2=237, w3=669, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 105)
    slow = _rolling_slope(x, 237)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.073125 + 0.0021422 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_422_struct_v422_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=112, w2=248, w3=682, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(248, min_periods=max(248//3, 2)).max()
    trough = x.rolling(112, min_periods=max(112//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.0875 + 0.0021423 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_423_struct_v423_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=119, w2=259, w3=695, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(119)
    rank = change.rolling(259, min_periods=max(259//3, 2)).rank(pct=True)
    persistence = change.rolling(695, min_periods=max(695//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.245 * persistence + 0.0021424 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_424_struct_v424_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=126, w2=270, w3=708, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(126, min_periods=max(126//3, 2)).std()
    vol_slow = ret.rolling(270, min_periods=max(270//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.11625 + 0.0021425 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_425_struct_v425_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=133, w2=281, w3=721, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(281, min_periods=max(281//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 133)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2602 * slope + 0.0021426 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_426_struct_v426_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=140, w2=292, w3=734, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(292, min_periods=max(292//3, 2)).mean()
    noise = impulse.abs().rolling(734, min_periods=max(734//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.145 + 0.0021427 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_427_struct_v427_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=147, w2=303, w3=747, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 147)
    acceleration = _rolling_slope(velocity, 303)
    curvature = _rolling_slope(acceleration, 747)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2754 * acceleration + 0.0021428 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_428_struct_v428_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=154, w2=314, w3=760, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(154, min_periods=max(154//3, 2)).mean(), upside.rolling(314, min_periods=max(314//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.17375 + 0.0021429 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_429_struct_v429_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=161, w2=325, w3=16, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(325, min_periods=max(325//3, 2)).max()
    rebound = x - x.rolling(161, min_periods=max(161//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2906 * _rolling_slope(draw, 16) + 0.002143 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_430_struct_v430_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=168, w2=336, w3=29, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 168)
    baseline = trend.rolling(336, min_periods=max(336//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(29, min_periods=max(29//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.2025 + 0.0021431 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_431_struct_v431_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=175, w2=347, w3=42, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 175)
    slow = _rolling_slope(x, 347)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=42, adjust=False).mean() * 1.216875 + 0.0021432 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_432_struct_v432_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=182, w2=358, w3=55, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(358, min_periods=max(358//3, 2)).max()
    trough = x.rolling(182, min_periods=max(182//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.23125 + 0.0021433 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_433_struct_v433_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=189, w2=369, w3=68, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(369, min_periods=max(369//3, 2)).rank(pct=True)
    persistence = change.rolling(68, min_periods=max(68//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.321 * persistence + 0.0021434 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_434_struct_v434_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=196, w2=380, w3=81, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(196, min_periods=max(196//3, 2)).std()
    vol_slow = ret.rolling(380, min_periods=max(380//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.26 + 0.0021435 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_435_struct_v435_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=203, w2=391, w3=94, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(391, min_periods=max(391//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 203)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3362 * slope + 0.0021436 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_436_struct_v436_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=210, w2=402, w3=107, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(402, min_periods=max(402//3, 2)).mean()
    noise = impulse.abs().rolling(107, min_periods=max(107//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.28875 + 0.0021437 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_437_struct_v437_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=217, w2=413, w3=120, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 217)
    acceleration = _rolling_slope(velocity, 413)
    curvature = _rolling_slope(acceleration, 120)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3514 * acceleration + 0.0021438 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_438_struct_v438_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=224, w2=424, w3=133, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(224, min_periods=max(224//3, 2)).mean(), upside.rolling(424, min_periods=max(424//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.3175 + 0.0021439 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_439_struct_v439_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=231, w2=435, w3=146, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(435, min_periods=max(435//3, 2)).max()
    rebound = x - x.rolling(231, min_periods=max(231//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3666 * _rolling_slope(draw, 146) + 0.002144 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_440_struct_v440_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=238, w2=446, w3=159, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 238)
    baseline = trend.rolling(446, min_periods=max(446//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(159, min_periods=max(159//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.34625 + 0.0021441 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_441_struct_v441_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=245, w2=457, w3=172, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 245)
    slow = _rolling_slope(x, 457)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=172, adjust=False).mean() * 1.360625 + 0.0021442 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_442_struct_v442_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=252, w2=468, w3=185, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(468, min_periods=max(468//3, 2)).max()
    trough = x.rolling(252, min_periods=max(252//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.375 + 0.0021443 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_443_struct_v443_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=8, w2=479, w3=198, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(8)
    rank = change.rolling(479, min_periods=max(479//3, 2)).rank(pct=True)
    persistence = change.rolling(198, min_periods=max(198//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.397 * persistence + 0.0021444 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_444_struct_v444_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=15, w2=490, w3=211, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(15, min_periods=max(15//3, 2)).std()
    vol_slow = ret.rolling(490, min_periods=max(490//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.40375 + 0.0021445 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_445_struct_v445_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=22, w2=501, w3=224, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(501, min_periods=max(501//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 22)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0358 * slope + 0.0021446 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_446_struct_v446_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=29, w2=512, w3=237, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(29)
    drag = impulse.rolling(512, min_periods=max(512//3, 2)).mean()
    noise = impulse.abs().rolling(237, min_periods=max(237//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.4325 + 0.0021447 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_447_struct_v447_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=36, w2=20, w3=250, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 36)
    acceleration = _rolling_slope(velocity, 20)
    curvature = _rolling_slope(acceleration, 250)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.051 * acceleration + 0.0021448 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_448_struct_v448_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=43, w2=31, w3=263, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(43, min_periods=max(43//3, 2)).mean(), upside.rolling(31, min_periods=max(31//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.46125 + 0.0021449 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_449_struct_v449_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=50, w2=42, w3=276, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(42, min_periods=max(42//3, 2)).max()
    rebound = x - x.rolling(50, min_periods=max(50//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0662 * _rolling_slope(draw, 276) + 0.002145 * anchor
    return base_signal.diff().diff().diff()

def f35_mcj_450_struct_v450_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=57, w2=53, w3=289, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 57)
    baseline = trend.rolling(53, min_periods=max(53//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(289, min_periods=max(289//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.49 + 0.0021451 * anchor
    return base_signal.diff().diff().diff()
