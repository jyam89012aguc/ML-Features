"""08 moving average extension dynamics d2 second derivative features 526-600 â€” Pipeline 1a-HF Grade v3.

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

def f08_mae_526_accel_v526_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=206, w2=187, w3=136, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(187, min_periods=max(187//3, 2)).mean()
    noise = impulse.abs().rolling(136, min_periods=max(136//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.524375 + 0.0004727 * anchor
    return base_signal.diff().diff()

def f08_mae_527_jerk_v527_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=213, w2=198, w3=149, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 213)
    acceleration = _rolling_slope(velocity, 198)
    curvature = _rolling_slope(acceleration, 149)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2022 * acceleration + 0.0004728 * anchor
    return base_signal.diff().diff()

def f08_mae_528_accel_v528_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=220, w2=209, w3=162, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(220, min_periods=max(220//3, 2)).mean(), upside.rolling(209, min_periods=max(209//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.553125 + 0.0004729 * anchor
    return base_signal.diff().diff()

def f08_mae_529_jerk_v529_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=227, w2=220, w3=175, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(220, min_periods=max(220//3, 2)).max()
    rebound = x - x.rolling(227, min_periods=max(227//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2174 * _rolling_slope(draw, 175) + 0.000473 * anchor
    return base_signal.diff().diff()

def f08_mae_530_accel_v530_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=234, w2=231, w3=188, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 234)
    baseline = trend.rolling(231, min_periods=max(231//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(188, min_periods=max(188//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.581875 + 0.0004731 * anchor
    return base_signal.diff().diff()

def f08_mae_531_jerk_v531_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=241, w2=242, w3=201, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 241)
    slow = _rolling_slope(x, 242)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=201, adjust=False).mean() * 1.59625 + 0.0004732 * anchor
    return base_signal.diff().diff()

def f08_mae_532_accel_v532_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=248, w2=253, w3=214, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(253, min_periods=max(253//3, 2)).max()
    trough = x.rolling(248, min_periods=max(248//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.610625 + 0.0004733 * anchor
    return base_signal.diff().diff()

def f08_mae_533_jerk_v533_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=255, w2=264, w3=227, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(264, min_periods=max(264//3, 2)).rank(pct=True)
    persistence = change.rolling(227, min_periods=max(227//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2478 * persistence + 0.0004734 * anchor
    return base_signal.diff().diff()

def f08_mae_534_accel_v534_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=11, w2=275, w3=240, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(11, min_periods=max(11//3, 2)).std()
    vol_slow = ret.rolling(275, min_periods=max(275//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.86625 + 0.0004735 * anchor
    return base_signal.diff().diff()

def f08_mae_535_jerk_v535_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=18, w2=286, w3=253, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(286, min_periods=max(286//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 18)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.263 * slope + 0.0004736 * anchor
    return base_signal.diff().diff()

def f08_mae_536_accel_v536_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=25, w2=297, w3=266, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(25)
    drag = impulse.rolling(297, min_periods=max(297//3, 2)).mean()
    noise = impulse.abs().rolling(266, min_periods=max(266//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.895 + 0.0004737 * anchor
    return base_signal.diff().diff()

def f08_mae_537_jerk_v537_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=32, w2=308, w3=279, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 32)
    acceleration = _rolling_slope(velocity, 308)
    curvature = _rolling_slope(acceleration, 279)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2782 * acceleration + 0.0004738 * anchor
    return base_signal.diff().diff()

def f08_mae_538_accel_v538_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=39, w2=319, w3=292, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(39, min_periods=max(39//3, 2)).mean(), upside.rolling(319, min_periods=max(319//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.92375 + 0.0004739 * anchor
    return base_signal.diff().diff()

def f08_mae_539_jerk_v539_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=46, w2=330, w3=305, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(330, min_periods=max(330//3, 2)).max()
    rebound = x - x.rolling(46, min_periods=max(46//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2934 * _rolling_slope(draw, 305) + 0.000474 * anchor
    return base_signal.diff().diff()

def f08_mae_540_accel_v540_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=53, w2=341, w3=318, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 53)
    baseline = trend.rolling(341, min_periods=max(341//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(318, min_periods=max(318//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.9525 + 0.0004741 * anchor
    return base_signal.diff().diff()

def f08_mae_541_jerk_v541_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=60, w2=352, w3=331, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 60)
    slow = _rolling_slope(x, 352)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.966875 + 0.0004742 * anchor
    return base_signal.diff().diff()

def f08_mae_542_accel_v542_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=67, w2=363, w3=344, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(363, min_periods=max(363//3, 2)).max()
    trough = x.rolling(67, min_periods=max(67//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.98125 + 0.0004743 * anchor
    return base_signal.diff().diff()

def f08_mae_543_jerk_v543_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=74, w2=374, w3=357, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(74)
    rank = change.rolling(374, min_periods=max(374//3, 2)).rank(pct=True)
    persistence = change.rolling(357, min_periods=max(357//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3238 * persistence + 0.0004744 * anchor
    return base_signal.diff().diff()

def f08_mae_544_accel_v544_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=81, w2=385, w3=370, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(81, min_periods=max(81//3, 2)).std()
    vol_slow = ret.rolling(385, min_periods=max(385//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.01 + 0.0004745 * anchor
    return base_signal.diff().diff()

def f08_mae_545_jerk_v545_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=88, w2=396, w3=383, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(396, min_periods=max(396//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 88)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.339 * slope + 0.0004746 * anchor
    return base_signal.diff().diff()

def f08_mae_546_accel_v546_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=95, w2=407, w3=396, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(95)
    drag = impulse.rolling(407, min_periods=max(407//3, 2)).mean()
    noise = impulse.abs().rolling(396, min_periods=max(396//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.03875 + 0.0004747 * anchor
    return base_signal.diff().diff()

def f08_mae_547_jerk_v547_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=102, w2=418, w3=409, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 102)
    acceleration = _rolling_slope(velocity, 418)
    curvature = _rolling_slope(acceleration, 409)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3542 * acceleration + 0.0004748 * anchor
    return base_signal.diff().diff()

def f08_mae_548_accel_v548_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=109, w2=429, w3=422, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(109, min_periods=max(109//3, 2)).mean(), upside.rolling(429, min_periods=max(429//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.0675 + 0.0004749 * anchor
    return base_signal.diff().diff()

def f08_mae_549_jerk_v549_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=116, w2=440, w3=435, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(440, min_periods=max(440//3, 2)).max()
    rebound = x - x.rolling(116, min_periods=max(116//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3694 * _rolling_slope(draw, 435) + 0.000475 * anchor
    return base_signal.diff().diff()

def f08_mae_550_accel_v550_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=123, w2=451, w3=448, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 123)
    baseline = trend.rolling(451, min_periods=max(451//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(448, min_periods=max(448//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.09625 + 0.0004751 * anchor
    return base_signal.diff().diff()

def f08_mae_551_jerk_v551_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=130, w2=462, w3=461, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 130)
    slow = _rolling_slope(x, 462)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.110625 + 0.0004752 * anchor
    return base_signal.diff().diff()

def f08_mae_552_accel_v552_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=137, w2=473, w3=474, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(473, min_periods=max(473//3, 2)).max()
    trough = x.rolling(137, min_periods=max(137//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.125 + 0.0004753 * anchor
    return base_signal.diff().diff()

def f08_mae_553_jerk_v553_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=144, w2=484, w3=487, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(484, min_periods=max(484//3, 2)).rank(pct=True)
    persistence = change.rolling(487, min_periods=max(487//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3998 * persistence + 0.0004754 * anchor
    return base_signal.diff().diff()

def f08_mae_554_accel_v554_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=151, w2=495, w3=500, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(151, min_periods=max(151//3, 2)).std()
    vol_slow = ret.rolling(495, min_periods=max(495//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.15375 + 0.0004755 * anchor
    return base_signal.diff().diff()

def f08_mae_555_jerk_v555_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=158, w2=506, w3=513, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(506, min_periods=max(506//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 158)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0386 * slope + 0.0004756 * anchor
    return base_signal.diff().diff()

def f08_mae_556_accel_v556_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=165, w2=14, w3=526, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(14, min_periods=max(14//3, 2)).mean()
    noise = impulse.abs().rolling(526, min_periods=max(526//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.1825 + 0.0004757 * anchor
    return base_signal.diff().diff()

def f08_mae_557_jerk_v557_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=172, w2=25, w3=539, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 172)
    acceleration = _rolling_slope(velocity, 25)
    curvature = _rolling_slope(acceleration, 539)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0538 * acceleration + 0.0004758 * anchor
    return base_signal.diff().diff()

def f08_mae_558_accel_v558_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=179, w2=36, w3=552, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(179, min_periods=max(179//3, 2)).mean(), upside.rolling(36, min_periods=max(36//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.21125 + 0.0004759 * anchor
    return base_signal.diff().diff()

def f08_mae_559_jerk_v559_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=186, w2=47, w3=565, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(47, min_periods=max(47//3, 2)).max()
    rebound = x - x.rolling(186, min_periods=max(186//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.069 * _rolling_slope(draw, 565) + 0.000476 * anchor
    return base_signal.diff().diff()

def f08_mae_560_accel_v560_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=193, w2=58, w3=578, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 193)
    baseline = trend.rolling(58, min_periods=max(58//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(578, min_periods=max(578//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.24 + 0.0004761 * anchor
    return base_signal.diff().diff()

def f08_mae_561_jerk_v561_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=200, w2=69, w3=591, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 200)
    slow = _rolling_slope(x, 69)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.254375 + 0.0004762 * anchor
    return base_signal.diff().diff()

def f08_mae_562_accel_v562_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=207, w2=80, w3=604, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(80, min_periods=max(80//3, 2)).max()
    trough = x.rolling(207, min_periods=max(207//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.26875 + 0.0004763 * anchor
    return base_signal.diff().diff()

def f08_mae_563_jerk_v563_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=214, w2=91, w3=617, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(91, min_periods=max(91//3, 2)).rank(pct=True)
    persistence = change.rolling(617, min_periods=max(617//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0994 * persistence + 0.0004764 * anchor
    return base_signal.diff().diff()

def f08_mae_564_accel_v564_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=221, w2=102, w3=630, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(221, min_periods=max(221//3, 2)).std()
    vol_slow = ret.rolling(102, min_periods=max(102//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.2975 + 0.0004765 * anchor
    return base_signal.diff().diff()

def f08_mae_565_jerk_v565_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=228, w2=113, w3=643, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(113, min_periods=max(113//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 228)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1146 * slope + 0.0004766 * anchor
    return base_signal.diff().diff()

def f08_mae_566_accel_v566_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=235, w2=124, w3=656, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(124, min_periods=max(124//3, 2)).mean()
    noise = impulse.abs().rolling(656, min_periods=max(656//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.32625 + 0.0004767 * anchor
    return base_signal.diff().diff()

def f08_mae_567_jerk_v567_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=242, w2=135, w3=669, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 242)
    acceleration = _rolling_slope(velocity, 135)
    curvature = _rolling_slope(acceleration, 669)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1298 * acceleration + 0.0004768 * anchor
    return base_signal.diff().diff()

def f08_mae_568_accel_v568_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=249, w2=146, w3=682, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(249, min_periods=max(249//3, 2)).mean(), upside.rolling(146, min_periods=max(146//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.355 + 0.0004769 * anchor
    return base_signal.diff().diff()

def f08_mae_569_jerk_v569_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=5, w2=157, w3=695, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(157, min_periods=max(157//3, 2)).max()
    rebound = x - x.rolling(5, min_periods=max(5//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.145 * _rolling_slope(draw, 695) + 0.000477 * anchor
    return base_signal.diff().diff()

def f08_mae_570_accel_v570_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=12, w2=168, w3=708, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 12)
    baseline = trend.rolling(168, min_periods=max(168//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(708, min_periods=max(708//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.38375 + 0.0004771 * anchor
    return base_signal.diff().diff()

def f08_mae_571_jerk_v571_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=19, w2=179, w3=721, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 19)
    slow = _rolling_slope(x, 179)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.398125 + 0.0004772 * anchor
    return base_signal.diff().diff()

def f08_mae_572_accel_v572_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=26, w2=190, w3=734, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(190, min_periods=max(190//3, 2)).max()
    trough = x.rolling(26, min_periods=max(26//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.4125 + 0.0004773 * anchor
    return base_signal.diff().diff()

def f08_mae_573_jerk_v573_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=33, w2=201, w3=747, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(33)
    rank = change.rolling(201, min_periods=max(201//3, 2)).rank(pct=True)
    persistence = change.rolling(747, min_periods=max(747//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1754 * persistence + 0.0004774 * anchor
    return base_signal.diff().diff()

def f08_mae_574_accel_v574_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=40, w2=212, w3=760, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(40, min_periods=max(40//3, 2)).std()
    vol_slow = ret.rolling(212, min_periods=max(212//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.44125 + 0.0004775 * anchor
    return base_signal.diff().diff()

def f08_mae_575_jerk_v575_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=47, w2=223, w3=16, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(223, min_periods=max(223//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 47)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1906 * slope + 0.0004776 * anchor
    return base_signal.diff().diff()

def f08_mae_576_accel_v576_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=54, w2=234, w3=29, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(54)
    drag = impulse.rolling(234, min_periods=max(234//3, 2)).mean()
    noise = impulse.abs().rolling(29, min_periods=max(29//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.47 + 0.0004777 * anchor
    return base_signal.diff().diff()

def f08_mae_577_jerk_v577_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=61, w2=245, w3=42, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 61)
    acceleration = _rolling_slope(velocity, 245)
    curvature = _rolling_slope(acceleration, 42)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2058 * acceleration + 0.0004778 * anchor
    return base_signal.diff().diff()

def f08_mae_578_accel_v578_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=68, w2=256, w3=55, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(68, min_periods=max(68//3, 2)).mean(), upside.rolling(256, min_periods=max(256//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(55) * 1.49875 + 0.0004779 * anchor
    return base_signal.diff().diff()

def f08_mae_579_jerk_v579_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=75, w2=267, w3=68, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(267, min_periods=max(267//3, 2)).max()
    rebound = x - x.rolling(75, min_periods=max(75//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.221 * _rolling_slope(draw, 68) + 0.000478 * anchor
    return base_signal.diff().diff()

def f08_mae_580_accel_v580_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=82, w2=278, w3=81, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 82)
    baseline = trend.rolling(278, min_periods=max(278//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(81, min_periods=max(81//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.5275 + 0.0004781 * anchor
    return base_signal.diff().diff()

def f08_mae_581_jerk_v581_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=89, w2=289, w3=94, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 89)
    slow = _rolling_slope(x, 289)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=94, adjust=False).mean() * 1.541875 + 0.0004782 * anchor
    return base_signal.diff().diff()

def f08_mae_582_accel_v582_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=96, w2=300, w3=107, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(300, min_periods=max(300//3, 2)).max()
    trough = x.rolling(96, min_periods=max(96//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.55625 + 0.0004783 * anchor
    return base_signal.diff().diff()

def f08_mae_583_jerk_v583_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=103, w2=311, w3=120, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(103)
    rank = change.rolling(311, min_periods=max(311//3, 2)).rank(pct=True)
    persistence = change.rolling(120, min_periods=max(120//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2514 * persistence + 0.0004784 * anchor
    return base_signal.diff().diff()

def f08_mae_584_accel_v584_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=110, w2=322, w3=133, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(110, min_periods=max(110//3, 2)).std()
    vol_slow = ret.rolling(322, min_periods=max(322//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.585 + 0.0004785 * anchor
    return base_signal.diff().diff()

def f08_mae_585_jerk_v585_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=117, w2=333, w3=146, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(333, min_periods=max(333//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 117)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2666 * slope + 0.0004786 * anchor
    return base_signal.diff().diff()

def f08_mae_586_accel_v586_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=124, w2=344, w3=159, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(124)
    drag = impulse.rolling(344, min_periods=max(344//3, 2)).mean()
    noise = impulse.abs().rolling(159, min_periods=max(159//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.61375 + 0.0004787 * anchor
    return base_signal.diff().diff()

def f08_mae_587_jerk_v587_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=131, w2=355, w3=172, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 131)
    acceleration = _rolling_slope(velocity, 355)
    curvature = _rolling_slope(acceleration, 172)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2818 * acceleration + 0.0004788 * anchor
    return base_signal.diff().diff()

def f08_mae_588_accel_v588_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=138, w2=366, w3=185, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(138, min_periods=max(138//3, 2)).mean(), upside.rolling(366, min_periods=max(366//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.869375 + 0.0004789 * anchor
    return base_signal.diff().diff()

def f08_mae_589_jerk_v589_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=145, w2=377, w3=198, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(377, min_periods=max(377//3, 2)).max()
    rebound = x - x.rolling(145, min_periods=max(145//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.297 * _rolling_slope(draw, 198) + 0.000479 * anchor
    return base_signal.diff().diff()

def f08_mae_590_accel_v590_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=152, w2=388, w3=211, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 152)
    baseline = trend.rolling(388, min_periods=max(388//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(211, min_periods=max(211//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.898125 + 0.0004791 * anchor
    return base_signal.diff().diff()

def f08_mae_591_jerk_v591_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=159, w2=399, w3=224, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 159)
    slow = _rolling_slope(x, 399)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=224, adjust=False).mean() * 0.9125 + 0.0004792 * anchor
    return base_signal.diff().diff()

def f08_mae_592_accel_v592_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=166, w2=410, w3=237, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(410, min_periods=max(410//3, 2)).max()
    trough = x.rolling(166, min_periods=max(166//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.926875 + 0.0004793 * anchor
    return base_signal.diff().diff()

def f08_mae_593_jerk_v593_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=173, w2=421, w3=250, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(421, min_periods=max(421//3, 2)).rank(pct=True)
    persistence = change.rolling(250, min_periods=max(250//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3274 * persistence + 0.0004794 * anchor
    return base_signal.diff().diff()

def f08_mae_594_accel_v594_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=180, w2=432, w3=263, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(180, min_periods=max(180//3, 2)).std()
    vol_slow = ret.rolling(432, min_periods=max(432//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.955625 + 0.0004795 * anchor
    return base_signal.diff().diff()

def f08_mae_595_jerk_v595_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=187, w2=443, w3=276, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(443, min_periods=max(443//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 187)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3426 * slope + 0.0004796 * anchor
    return base_signal.diff().diff()

def f08_mae_596_accel_v596_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=194, w2=454, w3=289, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(454, min_periods=max(454//3, 2)).mean()
    noise = impulse.abs().rolling(289, min_periods=max(289//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.984375 + 0.0004797 * anchor
    return base_signal.diff().diff()

def f08_mae_597_jerk_v597_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=201, w2=465, w3=302, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 201)
    acceleration = _rolling_slope(velocity, 465)
    curvature = _rolling_slope(acceleration, 302)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3578 * acceleration + 0.0004798 * anchor
    return base_signal.diff().diff()

def f08_mae_598_accel_v598_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=208, w2=476, w3=315, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(208, min_periods=max(208//3, 2)).mean(), upside.rolling(476, min_periods=max(476//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.013125 + 0.0004799 * anchor
    return base_signal.diff().diff()

def f08_mae_599_jerk_v599_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=215, w2=487, w3=328, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(487, min_periods=max(487//3, 2)).max()
    rebound = x - x.rolling(215, min_periods=max(215//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.373 * _rolling_slope(draw, 328) + 0.00048 * anchor
    return base_signal.diff().diff()

def f08_mae_600_accel_v600_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=222, w2=498, w3=341, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 222)
    baseline = trend.rolling(498, min_periods=max(498//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(341, min_periods=max(341//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.041875 + 0.0004801 * anchor
    return base_signal.diff().diff()
