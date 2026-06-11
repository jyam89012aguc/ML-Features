"""09 momentum exhaustion base features 451-525 â€” Pipeline 1a-HF Grade v3.

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

def f09_mex_451_jerk_v451(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=116, w2=429, w3=148, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 116)
    slow = _rolling_slope(x, 429)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=148, adjust=False).mean() * 1.34 + 0.0005252 * anchor

def f09_mex_452_accel_v452(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=123, w2=440, w3=161, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(440, min_periods=max(440//3, 2)).max()
    trough = x.rolling(123, min_periods=max(123//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.354375 + 0.0005253 * anchor

def f09_mex_453_jerk_v453(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=130, w2=451, w3=174, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(451, min_periods=max(451//3, 2)).rank(pct=True)
    persistence = change.rolling(174, min_periods=max(174//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0594 * persistence + 0.0005254 * anchor

def f09_mex_454_accel_v454(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=137, w2=462, w3=187, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(137, min_periods=max(137//3, 2)).std()
    vol_slow = ret.rolling(462, min_periods=max(462//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.383125 + 0.0005255 * anchor

def f09_mex_455_jerk_v455(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=144, w2=473, w3=200, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(473, min_periods=max(473//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 144)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0746 * slope + 0.0005256 * anchor

def f09_mex_456_accel_v456(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=151, w2=484, w3=213, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(484, min_periods=max(484//3, 2)).mean()
    noise = impulse.abs().rolling(213, min_periods=max(213//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.411875 + 0.0005257 * anchor

def f09_mex_457_jerk_v457(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=158, w2=495, w3=226, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 158)
    acceleration = _rolling_slope(velocity, 495)
    curvature = _rolling_slope(acceleration, 226)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0898 * acceleration + 0.0005258 * anchor

def f09_mex_458_accel_v458(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=165, w2=506, w3=239, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(165, min_periods=max(165//3, 2)).mean(), upside.rolling(506, min_periods=max(506//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.440625 + 0.0005259 * anchor

def f09_mex_459_jerk_v459(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=172, w2=14, w3=252, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(14, min_periods=max(14//3, 2)).max()
    rebound = x - x.rolling(172, min_periods=max(172//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.105 * _rolling_slope(draw, 252) + 0.000526 * anchor

def f09_mex_460_accel_v460(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=179, w2=25, w3=265, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 179)
    baseline = trend.rolling(25, min_periods=max(25//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(265, min_periods=max(265//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.469375 + 0.0005261 * anchor

def f09_mex_461_jerk_v461(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=186, w2=36, w3=278, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 186)
    slow = _rolling_slope(x, 36)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=278, adjust=False).mean() * 1.48375 + 0.0005262 * anchor

def f09_mex_462_accel_v462(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=193, w2=47, w3=291, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(47, min_periods=max(47//3, 2)).max()
    trough = x.rolling(193, min_periods=max(193//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.498125 + 0.0005263 * anchor

def f09_mex_463_jerk_v463(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=200, w2=58, w3=304, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(58, min_periods=max(58//3, 2)).rank(pct=True)
    persistence = change.rolling(304, min_periods=max(304//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1354 * persistence + 0.0005264 * anchor

def f09_mex_464_accel_v464(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=207, w2=69, w3=317, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(207, min_periods=max(207//3, 2)).std()
    vol_slow = ret.rolling(69, min_periods=max(69//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.526875 + 0.0005265 * anchor

def f09_mex_465_jerk_v465(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=214, w2=80, w3=330, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(80, min_periods=max(80//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 214)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1506 * slope + 0.0005266 * anchor

def f09_mex_466_accel_v466(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=221, w2=91, w3=343, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(91, min_periods=max(91//3, 2)).mean()
    noise = impulse.abs().rolling(343, min_periods=max(343//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.555625 + 0.0005267 * anchor

def f09_mex_467_jerk_v467(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=228, w2=102, w3=356, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 228)
    acceleration = _rolling_slope(velocity, 102)
    curvature = _rolling_slope(acceleration, 356)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1658 * acceleration + 0.0005268 * anchor

def f09_mex_468_accel_v468(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=235, w2=113, w3=369, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(235, min_periods=max(235//3, 2)).mean(), upside.rolling(113, min_periods=max(113//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.584375 + 0.0005269 * anchor

def f09_mex_469_jerk_v469(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=242, w2=124, w3=382, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(124, min_periods=max(124//3, 2)).max()
    rebound = x - x.rolling(242, min_periods=max(242//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.181 * _rolling_slope(draw, 382) + 0.000527 * anchor

def f09_mex_470_accel_v470(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=249, w2=135, w3=395, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 249)
    baseline = trend.rolling(135, min_periods=max(135//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(395, min_periods=max(395//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.613125 + 0.0005271 * anchor

def f09_mex_471_jerk_v471(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=5, w2=146, w3=408, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 5)
    slow = _rolling_slope(x, 146)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.854375 + 0.0005272 * anchor

def f09_mex_472_accel_v472(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=12, w2=157, w3=421, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(157, min_periods=max(157//3, 2)).max()
    trough = x.rolling(12, min_periods=max(12//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.86875 + 0.0005273 * anchor

def f09_mex_473_jerk_v473(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=19, w2=168, w3=434, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(19)
    rank = change.rolling(168, min_periods=max(168//3, 2)).rank(pct=True)
    persistence = change.rolling(434, min_periods=max(434//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2114 * persistence + 0.0005274 * anchor

def f09_mex_474_accel_v474(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=26, w2=179, w3=447, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(26, min_periods=max(26//3, 2)).std()
    vol_slow = ret.rolling(179, min_periods=max(179//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.8975 + 0.0005275 * anchor

def f09_mex_475_jerk_v475(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=33, w2=190, w3=460, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(190, min_periods=max(190//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 33)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2266 * slope + 0.0005276 * anchor

def f09_mex_476_accel_v476(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=40, w2=201, w3=473, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(40)
    drag = impulse.rolling(201, min_periods=max(201//3, 2)).mean()
    noise = impulse.abs().rolling(473, min_periods=max(473//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.92625 + 0.0005277 * anchor

def f09_mex_477_jerk_v477(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=47, w2=212, w3=486, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 47)
    acceleration = _rolling_slope(velocity, 212)
    curvature = _rolling_slope(acceleration, 486)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2418 * acceleration + 0.0005278 * anchor

def f09_mex_478_accel_v478(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=54, w2=223, w3=499, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(54, min_periods=max(54//3, 2)).mean(), upside.rolling(223, min_periods=max(223//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.955 + 0.0005279 * anchor

def f09_mex_479_jerk_v479(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=61, w2=234, w3=512, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(234, min_periods=max(234//3, 2)).max()
    rebound = x - x.rolling(61, min_periods=max(61//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.257 * _rolling_slope(draw, 512) + 0.000528 * anchor

def f09_mex_480_accel_v480(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=68, w2=245, w3=525, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 68)
    baseline = trend.rolling(245, min_periods=max(245//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(525, min_periods=max(525//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.98375 + 0.0005281 * anchor

def f09_mex_481_jerk_v481(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=75, w2=256, w3=538, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 75)
    slow = _rolling_slope(x, 256)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.998125 + 0.0005282 * anchor

def f09_mex_482_accel_v482(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=82, w2=267, w3=551, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(267, min_periods=max(267//3, 2)).max()
    trough = x.rolling(82, min_periods=max(82//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.0125 + 0.0005283 * anchor

def f09_mex_483_jerk_v483(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=89, w2=278, w3=564, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(89)
    rank = change.rolling(278, min_periods=max(278//3, 2)).rank(pct=True)
    persistence = change.rolling(564, min_periods=max(564//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2874 * persistence + 0.0005284 * anchor

def f09_mex_484_accel_v484(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=96, w2=289, w3=577, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(96, min_periods=max(96//3, 2)).std()
    vol_slow = ret.rolling(289, min_periods=max(289//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.04125 + 0.0005285 * anchor

def f09_mex_485_jerk_v485(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=103, w2=300, w3=590, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(300, min_periods=max(300//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 103)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3026 * slope + 0.0005286 * anchor

def f09_mex_486_accel_v486(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=110, w2=311, w3=603, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(110)
    drag = impulse.rolling(311, min_periods=max(311//3, 2)).mean()
    noise = impulse.abs().rolling(603, min_periods=max(603//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.07 + 0.0005287 * anchor

def f09_mex_487_jerk_v487(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=117, w2=322, w3=616, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 117)
    acceleration = _rolling_slope(velocity, 322)
    curvature = _rolling_slope(acceleration, 616)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3178 * acceleration + 0.0005288 * anchor

def f09_mex_488_accel_v488(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=124, w2=333, w3=629, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(124, min_periods=max(124//3, 2)).mean(), upside.rolling(333, min_periods=max(333//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.09875 + 0.0005289 * anchor

def f09_mex_489_jerk_v489(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=131, w2=344, w3=642, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(344, min_periods=max(344//3, 2)).max()
    rebound = x - x.rolling(131, min_periods=max(131//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.333 * _rolling_slope(draw, 642) + 0.000529 * anchor

def f09_mex_490_accel_v490(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=138, w2=355, w3=655, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 138)
    baseline = trend.rolling(355, min_periods=max(355//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(655, min_periods=max(655//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.1275 + 0.0005291 * anchor

def f09_mex_491_jerk_v491(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=145, w2=366, w3=668, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 145)
    slow = _rolling_slope(x, 366)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.141875 + 0.0005292 * anchor

def f09_mex_492_accel_v492(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=152, w2=377, w3=681, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(377, min_periods=max(377//3, 2)).max()
    trough = x.rolling(152, min_periods=max(152//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.15625 + 0.0005293 * anchor

def f09_mex_493_jerk_v493(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=159, w2=388, w3=694, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(388, min_periods=max(388//3, 2)).rank(pct=True)
    persistence = change.rolling(694, min_periods=max(694//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3634 * persistence + 0.0005294 * anchor

def f09_mex_494_accel_v494(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=166, w2=399, w3=707, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(166, min_periods=max(166//3, 2)).std()
    vol_slow = ret.rolling(399, min_periods=max(399//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.185 + 0.0005295 * anchor

def f09_mex_495_jerk_v495(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=173, w2=410, w3=720, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(410, min_periods=max(410//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 173)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3786 * slope + 0.0005296 * anchor

def f09_mex_496_accel_v496(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=180, w2=421, w3=733, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(421, min_periods=max(421//3, 2)).mean()
    noise = impulse.abs().rolling(733, min_periods=max(733//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.21375 + 0.0005297 * anchor

def f09_mex_497_jerk_v497(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=187, w2=432, w3=746, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 187)
    acceleration = _rolling_slope(velocity, 432)
    curvature = _rolling_slope(acceleration, 746)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3938 * acceleration + 0.0005298 * anchor

def f09_mex_498_accel_v498(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=194, w2=443, w3=759, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(194, min_periods=max(194//3, 2)).mean(), upside.rolling(443, min_periods=max(443//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.2425 + 0.0005299 * anchor

def f09_mex_499_jerk_v499(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=201, w2=454, w3=15, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(454, min_periods=max(454//3, 2)).max()
    rebound = x - x.rolling(201, min_periods=max(201//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.409 * _rolling_slope(draw, 15) + 0.00053 * anchor

def f09_mex_500_accel_v500(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=208, w2=465, w3=28, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 208)
    baseline = trend.rolling(465, min_periods=max(465//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(28, min_periods=max(28//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.27125 + 0.0005301 * anchor

def f09_mex_501_jerk_v501(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=215, w2=476, w3=41, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 215)
    slow = _rolling_slope(x, 476)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=41, adjust=False).mean() * 1.285625 + 0.0005302 * anchor

def f09_mex_502_accel_v502(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=222, w2=487, w3=54, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(487, min_periods=max(487//3, 2)).max()
    trough = x.rolling(222, min_periods=max(222//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.3 + 0.0005303 * anchor

def f09_mex_503_jerk_v503(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=229, w2=498, w3=67, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(498, min_periods=max(498//3, 2)).rank(pct=True)
    persistence = change.rolling(67, min_periods=max(67//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.063 * persistence + 0.0005304 * anchor

def f09_mex_504_accel_v504(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=236, w2=509, w3=80, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(236, min_periods=max(236//3, 2)).std()
    vol_slow = ret.rolling(509, min_periods=max(509//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.32875 + 0.0005305 * anchor

def f09_mex_505_jerk_v505(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=243, w2=17, w3=93, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(17, min_periods=max(17//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 243)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0782 * slope + 0.0005306 * anchor

def f09_mex_506_accel_v506(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=250, w2=28, w3=106, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(28, min_periods=max(28//3, 2)).mean()
    noise = impulse.abs().rolling(106, min_periods=max(106//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.3575 + 0.0005307 * anchor

def f09_mex_507_jerk_v507(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=6, w2=39, w3=119, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 6)
    acceleration = _rolling_slope(velocity, 39)
    curvature = _rolling_slope(acceleration, 119)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0934 * acceleration + 0.0005308 * anchor

def f09_mex_508_accel_v508(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=13, w2=50, w3=132, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(13, min_periods=max(13//3, 2)).mean(), upside.rolling(50, min_periods=max(50//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.38625 + 0.0005309 * anchor

def f09_mex_509_jerk_v509(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=20, w2=61, w3=145, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(61, min_periods=max(61//3, 2)).max()
    rebound = x - x.rolling(20, min_periods=max(20//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1086 * _rolling_slope(draw, 145) + 0.000531 * anchor

def f09_mex_510_accel_v510(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=27, w2=72, w3=158, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 27)
    baseline = trend.rolling(72, min_periods=max(72//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(158, min_periods=max(158//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.415 + 0.0005311 * anchor

def f09_mex_511_jerk_v511(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=34, w2=83, w3=171, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 34)
    slow = _rolling_slope(x, 83)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=171, adjust=False).mean() * 1.429375 + 0.0005312 * anchor

def f09_mex_512_accel_v512(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=41, w2=94, w3=184, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(94, min_periods=max(94//3, 2)).max()
    trough = x.rolling(41, min_periods=max(41//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.44375 + 0.0005313 * anchor

def f09_mex_513_jerk_v513(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=48, w2=105, w3=197, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(48)
    rank = change.rolling(105, min_periods=max(105//3, 2)).rank(pct=True)
    persistence = change.rolling(197, min_periods=max(197//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.139 * persistence + 0.0005314 * anchor

def f09_mex_514_accel_v514(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=55, w2=116, w3=210, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(55, min_periods=max(55//3, 2)).std()
    vol_slow = ret.rolling(116, min_periods=max(116//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.4725 + 0.0005315 * anchor

def f09_mex_515_jerk_v515(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=62, w2=127, w3=223, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(127, min_periods=max(127//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 62)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1542 * slope + 0.0005316 * anchor

def f09_mex_516_accel_v516(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=69, w2=138, w3=236, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(69)
    drag = impulse.rolling(138, min_periods=max(138//3, 2)).mean()
    noise = impulse.abs().rolling(236, min_periods=max(236//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.50125 + 0.0005317 * anchor

def f09_mex_517_jerk_v517(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=76, w2=149, w3=249, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 76)
    acceleration = _rolling_slope(velocity, 149)
    curvature = _rolling_slope(acceleration, 249)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1694 * acceleration + 0.0005318 * anchor

def f09_mex_518_accel_v518(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=83, w2=160, w3=262, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(83, min_periods=max(83//3, 2)).mean(), upside.rolling(160, min_periods=max(160//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.53 + 0.0005319 * anchor

def f09_mex_519_jerk_v519(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=90, w2=171, w3=275, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(171, min_periods=max(171//3, 2)).max()
    rebound = x - x.rolling(90, min_periods=max(90//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1846 * _rolling_slope(draw, 275) + 0.000532 * anchor

def f09_mex_520_accel_v520(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=97, w2=182, w3=288, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 97)
    baseline = trend.rolling(182, min_periods=max(182//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(288, min_periods=max(288//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.55875 + 0.0005321 * anchor

def f09_mex_521_jerk_v521(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=104, w2=193, w3=301, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 104)
    slow = _rolling_slope(x, 193)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.573125 + 0.0005322 * anchor

def f09_mex_522_accel_v522(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=111, w2=204, w3=314, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(204, min_periods=max(204//3, 2)).max()
    trough = x.rolling(111, min_periods=max(111//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.5875 + 0.0005323 * anchor

def f09_mex_523_jerk_v523(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=118, w2=215, w3=327, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(118)
    rank = change.rolling(215, min_periods=max(215//3, 2)).rank(pct=True)
    persistence = change.rolling(327, min_periods=max(327//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.215 * persistence + 0.0005324 * anchor

def f09_mex_524_accel_v524(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=125, w2=226, w3=340, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(125, min_periods=max(125//3, 2)).std()
    vol_slow = ret.rolling(226, min_periods=max(226//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.61625 + 0.0005325 * anchor

def f09_mex_525_jerk_v525(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=132, w2=237, w3=353, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(237, min_periods=max(237//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 132)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2302 * slope + 0.0005326 * anchor
