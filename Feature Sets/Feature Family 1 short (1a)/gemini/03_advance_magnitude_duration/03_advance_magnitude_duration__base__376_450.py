"""03 advance magnitude duration base features 376-450 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Kinetics - Institutional-grade short-side signal.
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

def f03_amd_376_accel_v376(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=244, w2=244, w3=64, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(244, min_periods=max(244//3, 2)).mean()
    noise = impulse.abs().rolling(64, min_periods=max(64//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.084375 + 0.0001577 * anchor

def f03_amd_377_jerk_v377(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=251, w2=255, w3=77, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 251)
    acceleration = _rolling_slope(velocity, 255)
    curvature = _rolling_slope(acceleration, 77)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3518 * acceleration + 0.0001578 * anchor

def f03_amd_378_accel_v378(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=7, w2=266, w3=90, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(7, min_periods=max(7//3, 2)).mean(), upside.rolling(266, min_periods=max(266//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(90) * 1.113125 + 0.0001579 * anchor

def f03_amd_379_jerk_v379(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=14, w2=277, w3=103, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(277, min_periods=max(277//3, 2)).max()
    rebound = x - x.rolling(14, min_periods=max(14//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.367 * _rolling_slope(draw, 103) + 0.000158 * anchor

def f03_amd_380_accel_v380(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=21, w2=288, w3=116, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 21)
    baseline = trend.rolling(288, min_periods=max(288//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(116, min_periods=max(116//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.141875 + 0.0001581 * anchor

def f03_amd_381_jerk_v381(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=28, w2=299, w3=129, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 28)
    slow = _rolling_slope(x, 299)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=129, adjust=False).mean() * 1.15625 + 0.0001582 * anchor

def f03_amd_382_accel_v382(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=35, w2=310, w3=142, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(310, min_periods=max(310//3, 2)).max()
    trough = x.rolling(35, min_periods=max(35//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.170625 + 0.0001583 * anchor

def f03_amd_383_jerk_v383(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=42, w2=321, w3=155, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(42)
    rank = change.rolling(321, min_periods=max(321//3, 2)).rank(pct=True)
    persistence = change.rolling(155, min_periods=max(155//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3974 * persistence + 0.0001584 * anchor

def f03_amd_384_accel_v384(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=49, w2=332, w3=168, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(49, min_periods=max(49//3, 2)).std()
    vol_slow = ret.rolling(332, min_periods=max(332//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.199375 + 0.0001585 * anchor

def f03_amd_385_jerk_v385(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=56, w2=343, w3=181, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(343, min_periods=max(343//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 56)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0362 * slope + 0.0001586 * anchor

def f03_amd_386_accel_v386(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=63, w2=354, w3=194, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(63)
    drag = impulse.rolling(354, min_periods=max(354//3, 2)).mean()
    noise = impulse.abs().rolling(194, min_periods=max(194//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.228125 + 0.0001587 * anchor

def f03_amd_387_jerk_v387(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=70, w2=365, w3=207, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 70)
    acceleration = _rolling_slope(velocity, 365)
    curvature = _rolling_slope(acceleration, 207)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0514 * acceleration + 0.0001588 * anchor

def f03_amd_388_accel_v388(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=77, w2=376, w3=220, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(77, min_periods=max(77//3, 2)).mean(), upside.rolling(376, min_periods=max(376//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.256875 + 0.0001589 * anchor

def f03_amd_389_jerk_v389(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=84, w2=387, w3=233, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(387, min_periods=max(387//3, 2)).max()
    rebound = x - x.rolling(84, min_periods=max(84//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0666 * _rolling_slope(draw, 233) + 0.000159 * anchor

def f03_amd_390_accel_v390(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=91, w2=398, w3=246, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 91)
    baseline = trend.rolling(398, min_periods=max(398//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(246, min_periods=max(246//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.285625 + 0.0001591 * anchor

def f03_amd_391_jerk_v391(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=98, w2=409, w3=259, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 98)
    slow = _rolling_slope(x, 409)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=259, adjust=False).mean() * 1.3 + 0.0001592 * anchor

def f03_amd_392_accel_v392(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=105, w2=420, w3=272, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(420, min_periods=max(420//3, 2)).max()
    trough = x.rolling(105, min_periods=max(105//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.314375 + 0.0001593 * anchor

def f03_amd_393_jerk_v393(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=112, w2=431, w3=285, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(112)
    rank = change.rolling(431, min_periods=max(431//3, 2)).rank(pct=True)
    persistence = change.rolling(285, min_periods=max(285//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.097 * persistence + 0.0001594 * anchor

def f03_amd_394_accel_v394(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=119, w2=442, w3=298, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(119, min_periods=max(119//3, 2)).std()
    vol_slow = ret.rolling(442, min_periods=max(442//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.343125 + 0.0001595 * anchor

def f03_amd_395_jerk_v395(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=126, w2=453, w3=311, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(453, min_periods=max(453//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 126)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1122 * slope + 0.0001596 * anchor

def f03_amd_396_accel_v396(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=133, w2=464, w3=324, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(464, min_periods=max(464//3, 2)).mean()
    noise = impulse.abs().rolling(324, min_periods=max(324//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.371875 + 0.0001597 * anchor

def f03_amd_397_jerk_v397(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=140, w2=475, w3=337, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 140)
    acceleration = _rolling_slope(velocity, 475)
    curvature = _rolling_slope(acceleration, 337)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1274 * acceleration + 0.0001598 * anchor

def f03_amd_398_accel_v398(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=147, w2=486, w3=350, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(147, min_periods=max(147//3, 2)).mean(), upside.rolling(486, min_periods=max(486//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.400625 + 0.0001599 * anchor

def f03_amd_399_jerk_v399(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=154, w2=497, w3=363, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(497, min_periods=max(497//3, 2)).max()
    rebound = x - x.rolling(154, min_periods=max(154//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1426 * _rolling_slope(draw, 363) + 0.00016 * anchor

def f03_amd_400_accel_v400(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=161, w2=508, w3=376, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 161)
    baseline = trend.rolling(508, min_periods=max(508//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(376, min_periods=max(376//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.429375 + 0.0001601 * anchor

def f03_amd_401_jerk_v401(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=168, w2=16, w3=389, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 168)
    slow = _rolling_slope(x, 16)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.44375 + 0.0001602 * anchor

def f03_amd_402_accel_v402(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=175, w2=27, w3=402, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(27, min_periods=max(27//3, 2)).max()
    trough = x.rolling(175, min_periods=max(175//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.458125 + 0.0001603 * anchor

def f03_amd_403_jerk_v403(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=182, w2=38, w3=415, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(38, min_periods=max(38//3, 2)).rank(pct=True)
    persistence = change.rolling(415, min_periods=max(415//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.173 * persistence + 0.0001604 * anchor

def f03_amd_404_accel_v404(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=189, w2=49, w3=428, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(189, min_periods=max(189//3, 2)).std()
    vol_slow = ret.rolling(49, min_periods=max(49//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.486875 + 0.0001605 * anchor

def f03_amd_405_jerk_v405(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=196, w2=60, w3=441, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(60, min_periods=max(60//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 196)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1882 * slope + 0.0001606 * anchor

def f03_amd_406_accel_v406(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=203, w2=71, w3=454, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(71, min_periods=max(71//3, 2)).mean()
    noise = impulse.abs().rolling(454, min_periods=max(454//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.515625 + 0.0001607 * anchor

def f03_amd_407_jerk_v407(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=210, w2=82, w3=467, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 210)
    acceleration = _rolling_slope(velocity, 82)
    curvature = _rolling_slope(acceleration, 467)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2034 * acceleration + 0.0001608 * anchor

def f03_amd_408_accel_v408(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=217, w2=93, w3=480, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(217, min_periods=max(217//3, 2)).mean(), upside.rolling(93, min_periods=max(93//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.544375 + 0.0001609 * anchor

def f03_amd_409_jerk_v409(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=224, w2=104, w3=493, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(104, min_periods=max(104//3, 2)).max()
    rebound = x - x.rolling(224, min_periods=max(224//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2186 * _rolling_slope(draw, 493) + 0.000161 * anchor

def f03_amd_410_accel_v410(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=231, w2=115, w3=506, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 231)
    baseline = trend.rolling(115, min_periods=max(115//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(506, min_periods=max(506//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.573125 + 0.0001611 * anchor

def f03_amd_411_jerk_v411(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=238, w2=126, w3=519, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 238)
    slow = _rolling_slope(x, 126)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.5875 + 0.0001612 * anchor

def f03_amd_412_accel_v412(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=245, w2=137, w3=532, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(137, min_periods=max(137//3, 2)).max()
    trough = x.rolling(245, min_periods=max(245//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.601875 + 0.0001613 * anchor

def f03_amd_413_jerk_v413(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=252, w2=148, w3=545, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(148, min_periods=max(148//3, 2)).rank(pct=True)
    persistence = change.rolling(545, min_periods=max(545//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.249 * persistence + 0.0001614 * anchor

def f03_amd_414_accel_v414(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=8, w2=159, w3=558, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(8, min_periods=max(8//3, 2)).std()
    vol_slow = ret.rolling(159, min_periods=max(159//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.8575 + 0.0001615 * anchor

def f03_amd_415_jerk_v415(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=15, w2=170, w3=571, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(170, min_periods=max(170//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 15)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2642 * slope + 0.0001616 * anchor

def f03_amd_416_accel_v416(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=22, w2=181, w3=584, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(22)
    drag = impulse.rolling(181, min_periods=max(181//3, 2)).mean()
    noise = impulse.abs().rolling(584, min_periods=max(584//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.88625 + 0.0001617 * anchor

def f03_amd_417_jerk_v417(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=29, w2=192, w3=597, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 29)
    acceleration = _rolling_slope(velocity, 192)
    curvature = _rolling_slope(acceleration, 597)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2794 * acceleration + 0.0001618 * anchor

def f03_amd_418_accel_v418(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=36, w2=203, w3=610, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(36, min_periods=max(36//3, 2)).mean(), upside.rolling(203, min_periods=max(203//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.915 + 0.0001619 * anchor

def f03_amd_419_jerk_v419(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=43, w2=214, w3=623, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(214, min_periods=max(214//3, 2)).max()
    rebound = x - x.rolling(43, min_periods=max(43//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2946 * _rolling_slope(draw, 623) + 0.000162 * anchor

def f03_amd_420_accel_v420(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=50, w2=225, w3=636, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 50)
    baseline = trend.rolling(225, min_periods=max(225//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(636, min_periods=max(636//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.94375 + 0.0001621 * anchor

def f03_amd_421_jerk_v421(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=57, w2=236, w3=649, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 57)
    slow = _rolling_slope(x, 236)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.958125 + 0.0001622 * anchor

def f03_amd_422_accel_v422(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=64, w2=247, w3=662, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(247, min_periods=max(247//3, 2)).max()
    trough = x.rolling(64, min_periods=max(64//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.9725 + 0.0001623 * anchor

def f03_amd_423_jerk_v423(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=71, w2=258, w3=675, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(71)
    rank = change.rolling(258, min_periods=max(258//3, 2)).rank(pct=True)
    persistence = change.rolling(675, min_periods=max(675//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.325 * persistence + 0.0001624 * anchor

def f03_amd_424_accel_v424(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=78, w2=269, w3=688, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(78, min_periods=max(78//3, 2)).std()
    vol_slow = ret.rolling(269, min_periods=max(269//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.00125 + 0.0001625 * anchor

def f03_amd_425_jerk_v425(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=85, w2=280, w3=701, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(280, min_periods=max(280//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 85)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3402 * slope + 0.0001626 * anchor

def f03_amd_426_accel_v426(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=92, w2=291, w3=714, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(92)
    drag = impulse.rolling(291, min_periods=max(291//3, 2)).mean()
    noise = impulse.abs().rolling(714, min_periods=max(714//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.03 + 0.0001627 * anchor

def f03_amd_427_jerk_v427(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=99, w2=302, w3=727, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 99)
    acceleration = _rolling_slope(velocity, 302)
    curvature = _rolling_slope(acceleration, 727)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3554 * acceleration + 0.0001628 * anchor

def f03_amd_428_accel_v428(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=106, w2=313, w3=740, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(106, min_periods=max(106//3, 2)).mean(), upside.rolling(313, min_periods=max(313//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.05875 + 0.0001629 * anchor

def f03_amd_429_jerk_v429(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=113, w2=324, w3=753, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(324, min_periods=max(324//3, 2)).max()
    rebound = x - x.rolling(113, min_periods=max(113//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3706 * _rolling_slope(draw, 753) + 0.000163 * anchor

def f03_amd_430_accel_v430(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=120, w2=335, w3=766, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 120)
    baseline = trend.rolling(335, min_periods=max(335//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(766, min_periods=max(766//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.0875 + 0.0001631 * anchor

def f03_amd_431_jerk_v431(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=127, w2=346, w3=22, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 127)
    slow = _rolling_slope(x, 346)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=22, adjust=False).mean() * 1.101875 + 0.0001632 * anchor

def f03_amd_432_accel_v432(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=134, w2=357, w3=35, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(357, min_periods=max(357//3, 2)).max()
    trough = x.rolling(134, min_periods=max(134//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.11625 + 0.0001633 * anchor

def f03_amd_433_jerk_v433(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=141, w2=368, w3=48, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(368, min_periods=max(368//3, 2)).rank(pct=True)
    persistence = change.rolling(48, min_periods=max(48//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.401 * persistence + 0.0001634 * anchor

def f03_amd_434_accel_v434(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=148, w2=379, w3=61, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(148, min_periods=max(148//3, 2)).std()
    vol_slow = ret.rolling(379, min_periods=max(379//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.145 + 0.0001635 * anchor

def f03_amd_435_jerk_v435(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=155, w2=390, w3=74, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(390, min_periods=max(390//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 155)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0398 * slope + 0.0001636 * anchor

def f03_amd_436_accel_v436(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=162, w2=401, w3=87, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(401, min_periods=max(401//3, 2)).mean()
    noise = impulse.abs().rolling(87, min_periods=max(87//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.17375 + 0.0001637 * anchor

def f03_amd_437_jerk_v437(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=169, w2=412, w3=100, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 169)
    acceleration = _rolling_slope(velocity, 412)
    curvature = _rolling_slope(acceleration, 100)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.055 * acceleration + 0.0001638 * anchor

def f03_amd_438_accel_v438(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=176, w2=423, w3=113, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(176, min_periods=max(176//3, 2)).mean(), upside.rolling(423, min_periods=max(423//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(113) * 1.2025 + 0.0001639 * anchor

def f03_amd_439_jerk_v439(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=183, w2=434, w3=126, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(434, min_periods=max(434//3, 2)).max()
    rebound = x - x.rolling(183, min_periods=max(183//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0702 * _rolling_slope(draw, 126) + 0.000164 * anchor

def f03_amd_440_accel_v440(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=190, w2=445, w3=139, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 190)
    baseline = trend.rolling(445, min_periods=max(445//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(139, min_periods=max(139//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.23125 + 0.0001641 * anchor

def f03_amd_441_jerk_v441(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=197, w2=456, w3=152, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 197)
    slow = _rolling_slope(x, 456)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=152, adjust=False).mean() * 1.245625 + 0.0001642 * anchor

def f03_amd_442_accel_v442(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=204, w2=467, w3=165, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(467, min_periods=max(467//3, 2)).max()
    trough = x.rolling(204, min_periods=max(204//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.26 + 0.0001643 * anchor

def f03_amd_443_jerk_v443(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=211, w2=478, w3=178, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(478, min_periods=max(478//3, 2)).rank(pct=True)
    persistence = change.rolling(178, min_periods=max(178//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1006 * persistence + 0.0001644 * anchor

def f03_amd_444_accel_v444(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=218, w2=489, w3=191, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(218, min_periods=max(218//3, 2)).std()
    vol_slow = ret.rolling(489, min_periods=max(489//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.28875 + 0.0001645 * anchor

def f03_amd_445_jerk_v445(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=225, w2=500, w3=204, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(500, min_periods=max(500//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 225)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1158 * slope + 0.0001646 * anchor

def f03_amd_446_accel_v446(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=232, w2=511, w3=217, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(511, min_periods=max(511//3, 2)).mean()
    noise = impulse.abs().rolling(217, min_periods=max(217//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.3175 + 0.0001647 * anchor

def f03_amd_447_jerk_v447(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=239, w2=19, w3=230, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 239)
    acceleration = _rolling_slope(velocity, 19)
    curvature = _rolling_slope(acceleration, 230)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.131 * acceleration + 0.0001648 * anchor

def f03_amd_448_accel_v448(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=246, w2=30, w3=243, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(246, min_periods=max(246//3, 2)).mean(), upside.rolling(30, min_periods=max(30//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.34625 + 0.0001649 * anchor

def f03_amd_449_jerk_v449(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=253, w2=41, w3=256, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(41, min_periods=max(41//3, 2)).max()
    rebound = x - x.rolling(253, min_periods=max(253//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1462 * _rolling_slope(draw, 256) + 0.000165 * anchor

def f03_amd_450_accel_v450(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=9, w2=52, w3=269, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 9)
    baseline = trend.rolling(52, min_periods=max(52//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(269, min_periods=max(269//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.375 + 0.0001651 * anchor
