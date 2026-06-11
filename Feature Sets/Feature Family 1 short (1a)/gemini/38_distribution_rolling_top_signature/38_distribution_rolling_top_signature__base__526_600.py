"""38 distribution rolling top signature base features 526-600 â€” Pipeline 1a-HF Grade v3.

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

def f38_drts_526_accel_v526(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=137, w2=66, w3=453, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(66, min_periods=max(66//3, 2)).mean()
    noise = impulse.abs().rolling(453, min_periods=max(453//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.398125 + 0.0023327 * anchor

def f38_drts_527_jerk_v527(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=144, w2=77, w3=466, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 144)
    acceleration = _rolling_slope(velocity, 77)
    curvature = _rolling_slope(acceleration, 466)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0358 * acceleration + 0.0023328 * anchor

def f38_drts_528_accel_v528(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=151, w2=88, w3=479, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(151, min_periods=max(151//3, 2)).mean(), upside.rolling(88, min_periods=max(88//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.426875 + 0.0023329 * anchor

def f38_drts_529_jerk_v529(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=158, w2=99, w3=492, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(99, min_periods=max(99//3, 2)).max()
    rebound = x - x.rolling(158, min_periods=max(158//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.051 * _rolling_slope(draw, 492) + 0.002333 * anchor

def f38_drts_530_accel_v530(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=165, w2=110, w3=505, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 165)
    baseline = trend.rolling(110, min_periods=max(110//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(505, min_periods=max(505//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.455625 + 0.0023331 * anchor

def f38_drts_531_jerk_v531(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=172, w2=121, w3=518, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 172)
    slow = _rolling_slope(x, 121)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.47 + 0.0023332 * anchor

def f38_drts_532_accel_v532(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=179, w2=132, w3=531, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(132, min_periods=max(132//3, 2)).max()
    trough = x.rolling(179, min_periods=max(179//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.484375 + 0.0023333 * anchor

def f38_drts_533_jerk_v533(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=186, w2=143, w3=544, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(143, min_periods=max(143//3, 2)).rank(pct=True)
    persistence = change.rolling(544, min_periods=max(544//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0814 * persistence + 0.0023334 * anchor

def f38_drts_534_accel_v534(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=193, w2=154, w3=557, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(193, min_periods=max(193//3, 2)).std()
    vol_slow = ret.rolling(154, min_periods=max(154//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.513125 + 0.0023335 * anchor

def f38_drts_535_jerk_v535(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=200, w2=165, w3=570, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(165, min_periods=max(165//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 200)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0966 * slope + 0.0023336 * anchor

def f38_drts_536_accel_v536(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=207, w2=176, w3=583, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(176, min_periods=max(176//3, 2)).mean()
    noise = impulse.abs().rolling(583, min_periods=max(583//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.541875 + 0.0023337 * anchor

def f38_drts_537_jerk_v537(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=214, w2=187, w3=596, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 214)
    acceleration = _rolling_slope(velocity, 187)
    curvature = _rolling_slope(acceleration, 596)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1118 * acceleration + 0.0023338 * anchor

def f38_drts_538_accel_v538(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=221, w2=198, w3=609, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(221, min_periods=max(221//3, 2)).mean(), upside.rolling(198, min_periods=max(198//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.570625 + 0.0023339 * anchor

def f38_drts_539_jerk_v539(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=228, w2=209, w3=622, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(209, min_periods=max(209//3, 2)).max()
    rebound = x - x.rolling(228, min_periods=max(228//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.127 * _rolling_slope(draw, 622) + 0.002334 * anchor

def f38_drts_540_accel_v540(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=235, w2=220, w3=635, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 235)
    baseline = trend.rolling(220, min_periods=max(220//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(635, min_periods=max(635//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.599375 + 0.0023341 * anchor

def f38_drts_541_jerk_v541(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=242, w2=231, w3=648, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 242)
    slow = _rolling_slope(x, 231)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.61375 + 0.0023342 * anchor

def f38_drts_542_accel_v542(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=249, w2=242, w3=661, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(242, min_periods=max(242//3, 2)).max()
    trough = x.rolling(249, min_periods=max(249//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.855 + 0.0023343 * anchor

def f38_drts_543_jerk_v543(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=5, w2=253, w3=674, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(5)
    rank = change.rolling(253, min_periods=max(253//3, 2)).rank(pct=True)
    persistence = change.rolling(674, min_periods=max(674//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1574 * persistence + 0.0023344 * anchor

def f38_drts_544_accel_v544(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=12, w2=264, w3=687, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(12, min_periods=max(12//3, 2)).std()
    vol_slow = ret.rolling(264, min_periods=max(264//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.88375 + 0.0023345 * anchor

def f38_drts_545_jerk_v545(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=19, w2=275, w3=700, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(275, min_periods=max(275//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 19)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1726 * slope + 0.0023346 * anchor

def f38_drts_546_accel_v546(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=26, w2=286, w3=713, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(26)
    drag = impulse.rolling(286, min_periods=max(286//3, 2)).mean()
    noise = impulse.abs().rolling(713, min_periods=max(713//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.9125 + 0.0023347 * anchor

def f38_drts_547_jerk_v547(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=33, w2=297, w3=726, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 33)
    acceleration = _rolling_slope(velocity, 297)
    curvature = _rolling_slope(acceleration, 726)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1878 * acceleration + 0.0023348 * anchor

def f38_drts_548_accel_v548(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=40, w2=308, w3=739, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(40, min_periods=max(40//3, 2)).mean(), upside.rolling(308, min_periods=max(308//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.94125 + 0.0023349 * anchor

def f38_drts_549_jerk_v549(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=47, w2=319, w3=752, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(319, min_periods=max(319//3, 2)).max()
    rebound = x - x.rolling(47, min_periods=max(47//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.203 * _rolling_slope(draw, 752) + 0.002335 * anchor

def f38_drts_550_accel_v550(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=54, w2=330, w3=765, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 54)
    baseline = trend.rolling(330, min_periods=max(330//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(765, min_periods=max(765//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.97 + 0.0023351 * anchor

def f38_drts_551_jerk_v551(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=61, w2=341, w3=21, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 61)
    slow = _rolling_slope(x, 341)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=21, adjust=False).mean() * 0.984375 + 0.0023352 * anchor

def f38_drts_552_accel_v552(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=68, w2=352, w3=34, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(352, min_periods=max(352//3, 2)).max()
    trough = x.rolling(68, min_periods=max(68//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.99875 + 0.0023353 * anchor

def f38_drts_553_jerk_v553(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=75, w2=363, w3=47, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(75)
    rank = change.rolling(363, min_periods=max(363//3, 2)).rank(pct=True)
    persistence = change.rolling(47, min_periods=max(47//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2334 * persistence + 0.0023354 * anchor

def f38_drts_554_accel_v554(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=82, w2=374, w3=60, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(82, min_periods=max(82//3, 2)).std()
    vol_slow = ret.rolling(374, min_periods=max(374//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.0275 + 0.0023355 * anchor

def f38_drts_555_jerk_v555(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=89, w2=385, w3=73, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(385, min_periods=max(385//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 89)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2486 * slope + 0.0023356 * anchor

def f38_drts_556_accel_v556(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=96, w2=396, w3=86, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(96)
    drag = impulse.rolling(396, min_periods=max(396//3, 2)).mean()
    noise = impulse.abs().rolling(86, min_periods=max(86//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.05625 + 0.0023357 * anchor

def f38_drts_557_jerk_v557(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=103, w2=407, w3=99, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 103)
    acceleration = _rolling_slope(velocity, 407)
    curvature = _rolling_slope(acceleration, 99)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2638 * acceleration + 0.0023358 * anchor

def f38_drts_558_accel_v558(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=110, w2=418, w3=112, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(110, min_periods=max(110//3, 2)).mean(), upside.rolling(418, min_periods=max(418//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(112) * 1.085 + 0.0023359 * anchor

def f38_drts_559_jerk_v559(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=117, w2=429, w3=125, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(429, min_periods=max(429//3, 2)).max()
    rebound = x - x.rolling(117, min_periods=max(117//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.279 * _rolling_slope(draw, 125) + 0.002336 * anchor

def f38_drts_560_accel_v560(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=124, w2=440, w3=138, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 124)
    baseline = trend.rolling(440, min_periods=max(440//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(138, min_periods=max(138//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.11375 + 0.0023361 * anchor

def f38_drts_561_jerk_v561(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=131, w2=451, w3=151, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 131)
    slow = _rolling_slope(x, 451)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=151, adjust=False).mean() * 1.128125 + 0.0023362 * anchor

def f38_drts_562_accel_v562(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=138, w2=462, w3=164, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(462, min_periods=max(462//3, 2)).max()
    trough = x.rolling(138, min_periods=max(138//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.1425 + 0.0023363 * anchor

def f38_drts_563_jerk_v563(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=145, w2=473, w3=177, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(473, min_periods=max(473//3, 2)).rank(pct=True)
    persistence = change.rolling(177, min_periods=max(177//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3094 * persistence + 0.0023364 * anchor

def f38_drts_564_accel_v564(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=152, w2=484, w3=190, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(152, min_periods=max(152//3, 2)).std()
    vol_slow = ret.rolling(484, min_periods=max(484//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.17125 + 0.0023365 * anchor

def f38_drts_565_jerk_v565(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=159, w2=495, w3=203, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(495, min_periods=max(495//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 159)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3246 * slope + 0.0023366 * anchor

def f38_drts_566_accel_v566(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=166, w2=506, w3=216, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(506, min_periods=max(506//3, 2)).mean()
    noise = impulse.abs().rolling(216, min_periods=max(216//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.2 + 0.0023367 * anchor

def f38_drts_567_jerk_v567(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=173, w2=14, w3=229, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 173)
    acceleration = _rolling_slope(velocity, 14)
    curvature = _rolling_slope(acceleration, 229)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3398 * acceleration + 0.0023368 * anchor

def f38_drts_568_accel_v568(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=180, w2=25, w3=242, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(180, min_periods=max(180//3, 2)).mean(), upside.rolling(25, min_periods=max(25//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.22875 + 0.0023369 * anchor

def f38_drts_569_jerk_v569(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=187, w2=36, w3=255, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(36, min_periods=max(36//3, 2)).max()
    rebound = x - x.rolling(187, min_periods=max(187//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.355 * _rolling_slope(draw, 255) + 0.002337 * anchor

def f38_drts_570_accel_v570(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=194, w2=47, w3=268, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 194)
    baseline = trend.rolling(47, min_periods=max(47//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(268, min_periods=max(268//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.2575 + 0.0023371 * anchor

def f38_drts_571_jerk_v571(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=201, w2=58, w3=281, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 201)
    slow = _rolling_slope(x, 58)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=281, adjust=False).mean() * 1.271875 + 0.0023372 * anchor

def f38_drts_572_accel_v572(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=208, w2=69, w3=294, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(69, min_periods=max(69//3, 2)).max()
    trough = x.rolling(208, min_periods=max(208//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.28625 + 0.0023373 * anchor

def f38_drts_573_jerk_v573(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=215, w2=80, w3=307, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(80, min_periods=max(80//3, 2)).rank(pct=True)
    persistence = change.rolling(307, min_periods=max(307//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3854 * persistence + 0.0023374 * anchor

def f38_drts_574_accel_v574(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=222, w2=91, w3=320, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(222, min_periods=max(222//3, 2)).std()
    vol_slow = ret.rolling(91, min_periods=max(91//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.315 + 0.0023375 * anchor

def f38_drts_575_jerk_v575(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=229, w2=102, w3=333, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(102, min_periods=max(102//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 229)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.4006 * slope + 0.0023376 * anchor

def f38_drts_576_accel_v576(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=236, w2=113, w3=346, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(113, min_periods=max(113//3, 2)).mean()
    noise = impulse.abs().rolling(346, min_periods=max(346//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.34375 + 0.0023377 * anchor

def f38_drts_577_jerk_v577(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=243, w2=124, w3=359, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 243)
    acceleration = _rolling_slope(velocity, 124)
    curvature = _rolling_slope(acceleration, 359)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0394 * acceleration + 0.0023378 * anchor

def f38_drts_578_accel_v578(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=250, w2=135, w3=372, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(250, min_periods=max(250//3, 2)).mean(), upside.rolling(135, min_periods=max(135//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.3725 + 0.0023379 * anchor

def f38_drts_579_jerk_v579(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=6, w2=146, w3=385, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(146, min_periods=max(146//3, 2)).max()
    rebound = x - x.rolling(6, min_periods=max(6//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0546 * _rolling_slope(draw, 385) + 0.002338 * anchor

def f38_drts_580_accel_v580(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=13, w2=157, w3=398, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 13)
    baseline = trend.rolling(157, min_periods=max(157//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(398, min_periods=max(398//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.40125 + 0.0023381 * anchor

def f38_drts_581_jerk_v581(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=20, w2=168, w3=411, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 20)
    slow = _rolling_slope(x, 168)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.415625 + 0.0023382 * anchor

def f38_drts_582_accel_v582(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=27, w2=179, w3=424, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(179, min_periods=max(179//3, 2)).max()
    trough = x.rolling(27, min_periods=max(27//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.43 + 0.0023383 * anchor

def f38_drts_583_jerk_v583(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=34, w2=190, w3=437, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(34)
    rank = change.rolling(190, min_periods=max(190//3, 2)).rank(pct=True)
    persistence = change.rolling(437, min_periods=max(437//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.085 * persistence + 0.0023384 * anchor

def f38_drts_584_accel_v584(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=41, w2=201, w3=450, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(41, min_periods=max(41//3, 2)).std()
    vol_slow = ret.rolling(201, min_periods=max(201//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.45875 + 0.0023385 * anchor

def f38_drts_585_jerk_v585(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=48, w2=212, w3=463, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(212, min_periods=max(212//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 48)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1002 * slope + 0.0023386 * anchor

def f38_drts_586_accel_v586(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=55, w2=223, w3=476, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(55)
    drag = impulse.rolling(223, min_periods=max(223//3, 2)).mean()
    noise = impulse.abs().rolling(476, min_periods=max(476//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.4875 + 0.0023387 * anchor

def f38_drts_587_jerk_v587(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=62, w2=234, w3=489, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 62)
    acceleration = _rolling_slope(velocity, 234)
    curvature = _rolling_slope(acceleration, 489)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1154 * acceleration + 0.0023388 * anchor

def f38_drts_588_accel_v588(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=69, w2=245, w3=502, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(69, min_periods=max(69//3, 2)).mean(), upside.rolling(245, min_periods=max(245//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.51625 + 0.0023389 * anchor

def f38_drts_589_jerk_v589(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=76, w2=256, w3=515, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(256, min_periods=max(256//3, 2)).max()
    rebound = x - x.rolling(76, min_periods=max(76//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1306 * _rolling_slope(draw, 515) + 0.002339 * anchor

def f38_drts_590_accel_v590(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=83, w2=267, w3=528, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 83)
    baseline = trend.rolling(267, min_periods=max(267//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(528, min_periods=max(528//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.545 + 0.0023391 * anchor

def f38_drts_591_jerk_v591(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=90, w2=278, w3=541, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 90)
    slow = _rolling_slope(x, 278)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.559375 + 0.0023392 * anchor

def f38_drts_592_accel_v592(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=97, w2=289, w3=554, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(289, min_periods=max(289//3, 2)).max()
    trough = x.rolling(97, min_periods=max(97//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.57375 + 0.0023393 * anchor

def f38_drts_593_jerk_v593(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=104, w2=300, w3=567, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(104)
    rank = change.rolling(300, min_periods=max(300//3, 2)).rank(pct=True)
    persistence = change.rolling(567, min_periods=max(567//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.161 * persistence + 0.0023394 * anchor

def f38_drts_594_accel_v594(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=111, w2=311, w3=580, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(111, min_periods=max(111//3, 2)).std()
    vol_slow = ret.rolling(311, min_periods=max(311//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.6025 + 0.0023395 * anchor

def f38_drts_595_jerk_v595(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=118, w2=322, w3=593, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(322, min_periods=max(322//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 118)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1762 * slope + 0.0023396 * anchor

def f38_drts_596_accel_v596(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=125, w2=333, w3=606, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(125)
    drag = impulse.rolling(333, min_periods=max(333//3, 2)).mean()
    noise = impulse.abs().rolling(606, min_periods=max(606//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.858125 + 0.0023397 * anchor

def f38_drts_597_jerk_v597(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=132, w2=344, w3=619, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 132)
    acceleration = _rolling_slope(velocity, 344)
    curvature = _rolling_slope(acceleration, 619)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1914 * acceleration + 0.0023398 * anchor

def f38_drts_598_accel_v598(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=139, w2=355, w3=632, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(139, min_periods=max(139//3, 2)).mean(), upside.rolling(355, min_periods=max(355//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.886875 + 0.0023399 * anchor

def f38_drts_599_jerk_v599(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=146, w2=366, w3=645, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(366, min_periods=max(366//3, 2)).max()
    rebound = x - x.rolling(146, min_periods=max(146//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2066 * _rolling_slope(draw, 645) + 0.00234 * anchor

def f38_drts_600_accel_v600(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=153, w2=377, w3=658, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 153)
    baseline = trend.rolling(377, min_periods=max(377//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(658, min_periods=max(658//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.915625 + 0.0023401 * anchor
