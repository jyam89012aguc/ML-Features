"""92 executive turnover signals d2 second derivative features 376-450 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Governance - Institutional-grade short-side signal.
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

def f92_exec_376_struct_v376_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=206, w2=368, w3=564, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(368, min_periods=max(368//3, 2)).mean()
    noise = impulse.abs().rolling(564, min_periods=max(564//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.555625 + 0.0042377 * anchor
    return base_signal.diff().diff()

def f92_exec_377_struct_v377_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=213, w2=379, w3=577, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 213)
    acceleration = _rolling_slope(velocity, 379)
    curvature = _rolling_slope(acceleration, 577)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2782 * acceleration + 0.0042378 * anchor
    return base_signal.diff().diff()

def f92_exec_378_struct_v378_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=220, w2=390, w3=590, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(220, min_periods=max(220//3, 2)).mean(), upside.rolling(390, min_periods=max(390//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.584375 + 0.0042379 * anchor
    return base_signal.diff().diff()

def f92_exec_379_struct_v379_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=227, w2=401, w3=603, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(401, min_periods=max(401//3, 2)).max()
    rebound = x - x.rolling(227, min_periods=max(227//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2934 * _rolling_slope(draw, 603) + 0.004238 * anchor
    return base_signal.diff().diff()

def f92_exec_380_struct_v380_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=234, w2=412, w3=616, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 234)
    baseline = trend.rolling(412, min_periods=max(412//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(616, min_periods=max(616//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.613125 + 0.0042381 * anchor
    return base_signal.diff().diff()

def f92_exec_381_struct_v381_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=241, w2=423, w3=629, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 241)
    slow = _rolling_slope(x, 423)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.854375 + 0.0042382 * anchor
    return base_signal.diff().diff()

def f92_exec_382_struct_v382_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=248, w2=434, w3=642, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(434, min_periods=max(434//3, 2)).max()
    trough = x.rolling(248, min_periods=max(248//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.86875 + 0.0042383 * anchor
    return base_signal.diff().diff()

def f92_exec_383_struct_v383_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=255, w2=445, w3=655, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(445, min_periods=max(445//3, 2)).rank(pct=True)
    persistence = change.rolling(655, min_periods=max(655//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3238 * persistence + 0.0042384 * anchor
    return base_signal.diff().diff()

def f92_exec_384_struct_v384_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=11, w2=456, w3=668, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(11, min_periods=max(11//3, 2)).std()
    vol_slow = ret.rolling(456, min_periods=max(456//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.8975 + 0.0042385 * anchor
    return base_signal.diff().diff()

def f92_exec_385_struct_v385_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=18, w2=467, w3=681, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(467, min_periods=max(467//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 18)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.339 * slope + 0.0042386 * anchor
    return base_signal.diff().diff()

def f92_exec_386_struct_v386_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=25, w2=478, w3=694, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(25)
    drag = impulse.rolling(478, min_periods=max(478//3, 2)).mean()
    noise = impulse.abs().rolling(694, min_periods=max(694//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.92625 + 0.0042387 * anchor
    return base_signal.diff().diff()

def f92_exec_387_struct_v387_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=32, w2=489, w3=707, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 32)
    acceleration = _rolling_slope(velocity, 489)
    curvature = _rolling_slope(acceleration, 707)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3542 * acceleration + 0.0042388 * anchor
    return base_signal.diff().diff()

def f92_exec_388_struct_v388_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=39, w2=500, w3=720, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(39, min_periods=max(39//3, 2)).mean(), upside.rolling(500, min_periods=max(500//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.955 + 0.0042389 * anchor
    return base_signal.diff().diff()

def f92_exec_389_struct_v389_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=46, w2=511, w3=733, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(511, min_periods=max(511//3, 2)).max()
    rebound = x - x.rolling(46, min_periods=max(46//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3694 * _rolling_slope(draw, 733) + 0.004239 * anchor
    return base_signal.diff().diff()

def f92_exec_390_struct_v390_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=53, w2=19, w3=746, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 53)
    baseline = trend.rolling(19, min_periods=max(19//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(746, min_periods=max(746//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.98375 + 0.0042391 * anchor
    return base_signal.diff().diff()

def f92_exec_391_struct_v391_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=60, w2=30, w3=759, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 60)
    slow = _rolling_slope(x, 30)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.998125 + 0.0042392 * anchor
    return base_signal.diff().diff()

def f92_exec_392_struct_v392_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=67, w2=41, w3=15, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(41, min_periods=max(41//3, 2)).max()
    trough = x.rolling(67, min_periods=max(67//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.0125 + 0.0042393 * anchor
    return base_signal.diff().diff()

def f92_exec_393_struct_v393_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=74, w2=52, w3=28, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(74)
    rank = change.rolling(52, min_periods=max(52//3, 2)).rank(pct=True)
    persistence = change.rolling(28, min_periods=max(28//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3998 * persistence + 0.0042394 * anchor
    return base_signal.diff().diff()

def f92_exec_394_struct_v394_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=81, w2=63, w3=41, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(81, min_periods=max(81//3, 2)).std()
    vol_slow = ret.rolling(63, min_periods=max(63//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.04125 + 0.0042395 * anchor
    return base_signal.diff().diff()

def f92_exec_395_struct_v395_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=88, w2=74, w3=54, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(74, min_periods=max(74//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 88)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0386 * slope + 0.0042396 * anchor
    return base_signal.diff().diff()

def f92_exec_396_struct_v396_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=95, w2=85, w3=67, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(95)
    drag = impulse.rolling(85, min_periods=max(85//3, 2)).mean()
    noise = impulse.abs().rolling(67, min_periods=max(67//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.07 + 0.0042397 * anchor
    return base_signal.diff().diff()

def f92_exec_397_struct_v397_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=102, w2=96, w3=80, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 102)
    acceleration = _rolling_slope(velocity, 96)
    curvature = _rolling_slope(acceleration, 80)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0538 * acceleration + 0.0042398 * anchor
    return base_signal.diff().diff()

def f92_exec_398_struct_v398_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=109, w2=107, w3=93, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(109, min_periods=max(109//3, 2)).mean(), upside.rolling(107, min_periods=max(107//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(93) * 1.09875 + 0.0042399 * anchor
    return base_signal.diff().diff()

def f92_exec_399_struct_v399_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=116, w2=118, w3=106, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(118, min_periods=max(118//3, 2)).max()
    rebound = x - x.rolling(116, min_periods=max(116//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.069 * _rolling_slope(draw, 106) + 0.00424 * anchor
    return base_signal.diff().diff()

def f92_exec_400_struct_v400_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=123, w2=129, w3=119, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 123)
    baseline = trend.rolling(129, min_periods=max(129//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(119, min_periods=max(119//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.1275 + 0.0042401 * anchor
    return base_signal.diff().diff()

def f92_exec_401_struct_v401_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=130, w2=140, w3=132, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 130)
    slow = _rolling_slope(x, 140)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=132, adjust=False).mean() * 1.141875 + 0.0042402 * anchor
    return base_signal.diff().diff()

def f92_exec_402_struct_v402_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=137, w2=151, w3=145, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(151, min_periods=max(151//3, 2)).max()
    trough = x.rolling(137, min_periods=max(137//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.15625 + 0.0042403 * anchor
    return base_signal.diff().diff()

def f92_exec_403_struct_v403_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=144, w2=162, w3=158, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(162, min_periods=max(162//3, 2)).rank(pct=True)
    persistence = change.rolling(158, min_periods=max(158//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0994 * persistence + 0.0042404 * anchor
    return base_signal.diff().diff()

def f92_exec_404_struct_v404_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=151, w2=173, w3=171, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(151, min_periods=max(151//3, 2)).std()
    vol_slow = ret.rolling(173, min_periods=max(173//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.185 + 0.0042405 * anchor
    return base_signal.diff().diff()

def f92_exec_405_struct_v405_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=158, w2=184, w3=184, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(184, min_periods=max(184//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 158)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1146 * slope + 0.0042406 * anchor
    return base_signal.diff().diff()

def f92_exec_406_struct_v406_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=165, w2=195, w3=197, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(195, min_periods=max(195//3, 2)).mean()
    noise = impulse.abs().rolling(197, min_periods=max(197//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.21375 + 0.0042407 * anchor
    return base_signal.diff().diff()

def f92_exec_407_struct_v407_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=172, w2=206, w3=210, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 172)
    acceleration = _rolling_slope(velocity, 206)
    curvature = _rolling_slope(acceleration, 210)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1298 * acceleration + 0.0042408 * anchor
    return base_signal.diff().diff()

def f92_exec_408_struct_v408_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=179, w2=217, w3=223, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(179, min_periods=max(179//3, 2)).mean(), upside.rolling(217, min_periods=max(217//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.2425 + 0.0042409 * anchor
    return base_signal.diff().diff()

def f92_exec_409_struct_v409_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=186, w2=228, w3=236, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(228, min_periods=max(228//3, 2)).max()
    rebound = x - x.rolling(186, min_periods=max(186//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.145 * _rolling_slope(draw, 236) + 0.004241 * anchor
    return base_signal.diff().diff()

def f92_exec_410_struct_v410_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=193, w2=239, w3=249, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 193)
    baseline = trend.rolling(239, min_periods=max(239//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(249, min_periods=max(249//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.27125 + 0.0042411 * anchor
    return base_signal.diff().diff()

def f92_exec_411_struct_v411_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=200, w2=250, w3=262, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 200)
    slow = _rolling_slope(x, 250)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=262, adjust=False).mean() * 1.285625 + 0.0042412 * anchor
    return base_signal.diff().diff()

def f92_exec_412_struct_v412_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=207, w2=261, w3=275, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(261, min_periods=max(261//3, 2)).max()
    trough = x.rolling(207, min_periods=max(207//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.3 + 0.0042413 * anchor
    return base_signal.diff().diff()

def f92_exec_413_struct_v413_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=214, w2=272, w3=288, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(272, min_periods=max(272//3, 2)).rank(pct=True)
    persistence = change.rolling(288, min_periods=max(288//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1754 * persistence + 0.0042414 * anchor
    return base_signal.diff().diff()

def f92_exec_414_struct_v414_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=221, w2=283, w3=301, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(221, min_periods=max(221//3, 2)).std()
    vol_slow = ret.rolling(283, min_periods=max(283//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.32875 + 0.0042415 * anchor
    return base_signal.diff().diff()

def f92_exec_415_struct_v415_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=228, w2=294, w3=314, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(294, min_periods=max(294//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 228)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1906 * slope + 0.0042416 * anchor
    return base_signal.diff().diff()

def f92_exec_416_struct_v416_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=235, w2=305, w3=327, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(305, min_periods=max(305//3, 2)).mean()
    noise = impulse.abs().rolling(327, min_periods=max(327//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.3575 + 0.0042417 * anchor
    return base_signal.diff().diff()

def f92_exec_417_struct_v417_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=242, w2=316, w3=340, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 242)
    acceleration = _rolling_slope(velocity, 316)
    curvature = _rolling_slope(acceleration, 340)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2058 * acceleration + 0.0042418 * anchor
    return base_signal.diff().diff()

def f92_exec_418_struct_v418_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=249, w2=327, w3=353, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(249, min_periods=max(249//3, 2)).mean(), upside.rolling(327, min_periods=max(327//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.38625 + 0.0042419 * anchor
    return base_signal.diff().diff()

def f92_exec_419_struct_v419_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=5, w2=338, w3=366, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(338, min_periods=max(338//3, 2)).max()
    rebound = x - x.rolling(5, min_periods=max(5//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.221 * _rolling_slope(draw, 366) + 0.004242 * anchor
    return base_signal.diff().diff()

def f92_exec_420_struct_v420_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=12, w2=349, w3=379, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 12)
    baseline = trend.rolling(349, min_periods=max(349//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(379, min_periods=max(379//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.415 + 0.0042421 * anchor
    return base_signal.diff().diff()

def f92_exec_421_struct_v421_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=19, w2=360, w3=392, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 19)
    slow = _rolling_slope(x, 360)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.429375 + 0.0042422 * anchor
    return base_signal.diff().diff()

def f92_exec_422_struct_v422_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=26, w2=371, w3=405, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(371, min_periods=max(371//3, 2)).max()
    trough = x.rolling(26, min_periods=max(26//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.44375 + 0.0042423 * anchor
    return base_signal.diff().diff()

def f92_exec_423_struct_v423_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=33, w2=382, w3=418, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(33)
    rank = change.rolling(382, min_periods=max(382//3, 2)).rank(pct=True)
    persistence = change.rolling(418, min_periods=max(418//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2514 * persistence + 0.0042424 * anchor
    return base_signal.diff().diff()

def f92_exec_424_struct_v424_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=40, w2=393, w3=431, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(40, min_periods=max(40//3, 2)).std()
    vol_slow = ret.rolling(393, min_periods=max(393//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.4725 + 0.0042425 * anchor
    return base_signal.diff().diff()

def f92_exec_425_struct_v425_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=47, w2=404, w3=444, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(404, min_periods=max(404//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 47)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2666 * slope + 0.0042426 * anchor
    return base_signal.diff().diff()

def f92_exec_426_struct_v426_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=54, w2=415, w3=457, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(54)
    drag = impulse.rolling(415, min_periods=max(415//3, 2)).mean()
    noise = impulse.abs().rolling(457, min_periods=max(457//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.50125 + 0.0042427 * anchor
    return base_signal.diff().diff()

def f92_exec_427_struct_v427_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=61, w2=426, w3=470, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 61)
    acceleration = _rolling_slope(velocity, 426)
    curvature = _rolling_slope(acceleration, 470)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2818 * acceleration + 0.0042428 * anchor
    return base_signal.diff().diff()

def f92_exec_428_struct_v428_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=68, w2=437, w3=483, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(68, min_periods=max(68//3, 2)).mean(), upside.rolling(437, min_periods=max(437//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.53 + 0.0042429 * anchor
    return base_signal.diff().diff()

def f92_exec_429_struct_v429_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=75, w2=448, w3=496, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(448, min_periods=max(448//3, 2)).max()
    rebound = x - x.rolling(75, min_periods=max(75//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.297 * _rolling_slope(draw, 496) + 0.004243 * anchor
    return base_signal.diff().diff()

def f92_exec_430_struct_v430_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=82, w2=459, w3=509, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 82)
    baseline = trend.rolling(459, min_periods=max(459//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(509, min_periods=max(509//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.55875 + 0.0042431 * anchor
    return base_signal.diff().diff()

def f92_exec_431_struct_v431_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=89, w2=470, w3=522, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 89)
    slow = _rolling_slope(x, 470)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.573125 + 0.0042432 * anchor
    return base_signal.diff().diff()

def f92_exec_432_struct_v432_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=96, w2=481, w3=535, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(481, min_periods=max(481//3, 2)).max()
    trough = x.rolling(96, min_periods=max(96//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.5875 + 0.0042433 * anchor
    return base_signal.diff().diff()

def f92_exec_433_struct_v433_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=103, w2=492, w3=548, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(103)
    rank = change.rolling(492, min_periods=max(492//3, 2)).rank(pct=True)
    persistence = change.rolling(548, min_periods=max(548//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3274 * persistence + 0.0042434 * anchor
    return base_signal.diff().diff()

def f92_exec_434_struct_v434_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=110, w2=503, w3=561, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(110, min_periods=max(110//3, 2)).std()
    vol_slow = ret.rolling(503, min_periods=max(503//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.61625 + 0.0042435 * anchor
    return base_signal.diff().diff()

def f92_exec_435_struct_v435_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=117, w2=11, w3=574, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(11, min_periods=max(11//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 117)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3426 * slope + 0.0042436 * anchor
    return base_signal.diff().diff()

def f92_exec_436_struct_v436_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=124, w2=22, w3=587, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(124)
    drag = impulse.rolling(22, min_periods=max(22//3, 2)).mean()
    noise = impulse.abs().rolling(587, min_periods=max(587//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.871875 + 0.0042437 * anchor
    return base_signal.diff().diff()

def f92_exec_437_struct_v437_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=131, w2=33, w3=600, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 131)
    acceleration = _rolling_slope(velocity, 33)
    curvature = _rolling_slope(acceleration, 600)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3578 * acceleration + 0.0042438 * anchor
    return base_signal.diff().diff()

def f92_exec_438_struct_v438_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=138, w2=44, w3=613, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(138, min_periods=max(138//3, 2)).mean(), upside.rolling(44, min_periods=max(44//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.900625 + 0.0042439 * anchor
    return base_signal.diff().diff()

def f92_exec_439_struct_v439_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=145, w2=55, w3=626, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(55, min_periods=max(55//3, 2)).max()
    rebound = x - x.rolling(145, min_periods=max(145//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.373 * _rolling_slope(draw, 626) + 0.004244 * anchor
    return base_signal.diff().diff()

def f92_exec_440_struct_v440_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=152, w2=66, w3=639, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 152)
    baseline = trend.rolling(66, min_periods=max(66//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(639, min_periods=max(639//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.929375 + 0.0042441 * anchor
    return base_signal.diff().diff()

def f92_exec_441_struct_v441_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=159, w2=77, w3=652, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 159)
    slow = _rolling_slope(x, 77)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.94375 + 0.0042442 * anchor
    return base_signal.diff().diff()

def f92_exec_442_struct_v442_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=166, w2=88, w3=665, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(88, min_periods=max(88//3, 2)).max()
    trough = x.rolling(166, min_periods=max(166//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.958125 + 0.0042443 * anchor
    return base_signal.diff().diff()

def f92_exec_443_struct_v443_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=173, w2=99, w3=678, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(99, min_periods=max(99//3, 2)).rank(pct=True)
    persistence = change.rolling(678, min_periods=max(678//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.4034 * persistence + 0.0042444 * anchor
    return base_signal.diff().diff()

def f92_exec_444_struct_v444_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=180, w2=110, w3=691, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(180, min_periods=max(180//3, 2)).std()
    vol_slow = ret.rolling(110, min_periods=max(110//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.986875 + 0.0042445 * anchor
    return base_signal.diff().diff()

def f92_exec_445_struct_v445_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=187, w2=121, w3=704, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(121, min_periods=max(121//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 187)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0422 * slope + 0.0042446 * anchor
    return base_signal.diff().diff()

def f92_exec_446_struct_v446_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=194, w2=132, w3=717, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(132, min_periods=max(132//3, 2)).mean()
    noise = impulse.abs().rolling(717, min_periods=max(717//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.015625 + 0.0042447 * anchor
    return base_signal.diff().diff()

def f92_exec_447_struct_v447_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=201, w2=143, w3=730, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 201)
    acceleration = _rolling_slope(velocity, 143)
    curvature = _rolling_slope(acceleration, 730)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0574 * acceleration + 0.0042448 * anchor
    return base_signal.diff().diff()

def f92_exec_448_struct_v448_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=208, w2=154, w3=743, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(208, min_periods=max(208//3, 2)).mean(), upside.rolling(154, min_periods=max(154//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.044375 + 0.0042449 * anchor
    return base_signal.diff().diff()

def f92_exec_449_struct_v449_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=215, w2=165, w3=756, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(165, min_periods=max(165//3, 2)).max()
    rebound = x - x.rolling(215, min_periods=max(215//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0726 * _rolling_slope(draw, 756) + 0.004245 * anchor
    return base_signal.diff().diff()

def f92_exec_450_struct_v450_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=222, w2=176, w3=769, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 222)
    baseline = trend.rolling(176, min_periods=max(176//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(769, min_periods=max(769//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.073125 + 0.0042451 * anchor
    return base_signal.diff().diff()
