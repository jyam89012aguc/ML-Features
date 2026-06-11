"""10 volatility regime at peak d1 first derivative features 376-450 â€” Pipeline 1a-HF Grade v3.

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

def f10_vreg_376_accel_v376_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=210, w2=229, w3=390, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(229, min_periods=max(229//3, 2)).mean()
    noise = impulse.abs().rolling(390, min_periods=max(390//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.27625 + 0.0006377 * anchor
    return base_signal.diff()

def f10_vreg_377_jerk_v377_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=217, w2=240, w3=403, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 217)
    acceleration = _rolling_slope(velocity, 240)
    curvature = _rolling_slope(acceleration, 403)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.321 * acceleration + 0.0006378 * anchor
    return base_signal.diff()

def f10_vreg_378_accel_v378_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=224, w2=251, w3=416, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(224, min_periods=max(224//3, 2)).mean(), upside.rolling(251, min_periods=max(251//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.305 + 0.0006379 * anchor
    return base_signal.diff()

def f10_vreg_379_jerk_v379_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=231, w2=262, w3=429, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(262, min_periods=max(262//3, 2)).max()
    rebound = x - x.rolling(231, min_periods=max(231//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3362 * _rolling_slope(draw, 429) + 0.000638 * anchor
    return base_signal.diff()

def f10_vreg_380_accel_v380_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=238, w2=273, w3=442, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 238)
    baseline = trend.rolling(273, min_periods=max(273//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(442, min_periods=max(442//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.33375 + 0.0006381 * anchor
    return base_signal.diff()

def f10_vreg_381_jerk_v381_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=245, w2=284, w3=455, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 245)
    slow = _rolling_slope(x, 284)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.348125 + 0.0006382 * anchor
    return base_signal.diff()

def f10_vreg_382_accel_v382_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=252, w2=295, w3=468, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(295, min_periods=max(295//3, 2)).max()
    trough = x.rolling(252, min_periods=max(252//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.3625 + 0.0006383 * anchor
    return base_signal.diff()

def f10_vreg_383_jerk_v383_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=8, w2=306, w3=481, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(8)
    rank = change.rolling(306, min_periods=max(306//3, 2)).rank(pct=True)
    persistence = change.rolling(481, min_periods=max(481//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3666 * persistence + 0.0006384 * anchor
    return base_signal.diff()

def f10_vreg_384_accel_v384_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=15, w2=317, w3=494, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(15, min_periods=max(15//3, 2)).std()
    vol_slow = ret.rolling(317, min_periods=max(317//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.39125 + 0.0006385 * anchor
    return base_signal.diff()

def f10_vreg_385_jerk_v385_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=22, w2=328, w3=507, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(328, min_periods=max(328//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 22)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3818 * slope + 0.0006386 * anchor
    return base_signal.diff()

def f10_vreg_386_accel_v386_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=29, w2=339, w3=520, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(29)
    drag = impulse.rolling(339, min_periods=max(339//3, 2)).mean()
    noise = impulse.abs().rolling(520, min_periods=max(520//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.42 + 0.0006387 * anchor
    return base_signal.diff()

def f10_vreg_387_jerk_v387_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=36, w2=350, w3=533, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 36)
    acceleration = _rolling_slope(velocity, 350)
    curvature = _rolling_slope(acceleration, 533)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.397 * acceleration + 0.0006388 * anchor
    return base_signal.diff()

def f10_vreg_388_accel_v388_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=43, w2=361, w3=546, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(43, min_periods=max(43//3, 2)).mean(), upside.rolling(361, min_periods=max(361//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.44875 + 0.0006389 * anchor
    return base_signal.diff()

def f10_vreg_389_jerk_v389_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=50, w2=372, w3=559, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(372, min_periods=max(372//3, 2)).max()
    rebound = x - x.rolling(50, min_periods=max(50//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0358 * _rolling_slope(draw, 559) + 0.000639 * anchor
    return base_signal.diff()

def f10_vreg_390_accel_v390_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=57, w2=383, w3=572, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 57)
    baseline = trend.rolling(383, min_periods=max(383//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(572, min_periods=max(572//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.4775 + 0.0006391 * anchor
    return base_signal.diff()

def f10_vreg_391_jerk_v391_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=64, w2=394, w3=585, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 64)
    slow = _rolling_slope(x, 394)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.491875 + 0.0006392 * anchor
    return base_signal.diff()

def f10_vreg_392_accel_v392_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=71, w2=405, w3=598, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(405, min_periods=max(405//3, 2)).max()
    trough = x.rolling(71, min_periods=max(71//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.50625 + 0.0006393 * anchor
    return base_signal.diff()

def f10_vreg_393_jerk_v393_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=78, w2=416, w3=611, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(78)
    rank = change.rolling(416, min_periods=max(416//3, 2)).rank(pct=True)
    persistence = change.rolling(611, min_periods=max(611//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0662 * persistence + 0.0006394 * anchor
    return base_signal.diff()

def f10_vreg_394_accel_v394_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=85, w2=427, w3=624, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(85, min_periods=max(85//3, 2)).std()
    vol_slow = ret.rolling(427, min_periods=max(427//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.535 + 0.0006395 * anchor
    return base_signal.diff()

def f10_vreg_395_jerk_v395_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=92, w2=438, w3=637, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(438, min_periods=max(438//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 92)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0814 * slope + 0.0006396 * anchor
    return base_signal.diff()

def f10_vreg_396_accel_v396_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=99, w2=449, w3=650, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(99)
    drag = impulse.rolling(449, min_periods=max(449//3, 2)).mean()
    noise = impulse.abs().rolling(650, min_periods=max(650//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.56375 + 0.0006397 * anchor
    return base_signal.diff()

def f10_vreg_397_jerk_v397_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=106, w2=460, w3=663, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 106)
    acceleration = _rolling_slope(velocity, 460)
    curvature = _rolling_slope(acceleration, 663)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0966 * acceleration + 0.0006398 * anchor
    return base_signal.diff()

def f10_vreg_398_accel_v398_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=113, w2=471, w3=676, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(113, min_periods=max(113//3, 2)).mean(), upside.rolling(471, min_periods=max(471//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.5925 + 0.0006399 * anchor
    return base_signal.diff()

def f10_vreg_399_jerk_v399_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=120, w2=482, w3=689, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(482, min_periods=max(482//3, 2)).max()
    rebound = x - x.rolling(120, min_periods=max(120//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1118 * _rolling_slope(draw, 689) + 0.00064 * anchor
    return base_signal.diff()

def f10_vreg_400_accel_v400_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=127, w2=493, w3=702, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 127)
    baseline = trend.rolling(493, min_periods=max(493//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(702, min_periods=max(702//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.62125 + 0.0006401 * anchor
    return base_signal.diff()

def f10_vreg_401_jerk_v401_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=134, w2=504, w3=715, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 134)
    slow = _rolling_slope(x, 504)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.8625 + 0.0006402 * anchor
    return base_signal.diff()

def f10_vreg_402_accel_v402_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=141, w2=12, w3=728, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(12, min_periods=max(12//3, 2)).max()
    trough = x.rolling(141, min_periods=max(141//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.876875 + 0.0006403 * anchor
    return base_signal.diff()

def f10_vreg_403_jerk_v403_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=148, w2=23, w3=741, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(23, min_periods=max(23//3, 2)).rank(pct=True)
    persistence = change.rolling(741, min_periods=max(741//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1422 * persistence + 0.0006404 * anchor
    return base_signal.diff()

def f10_vreg_404_accel_v404_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=155, w2=34, w3=754, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(155, min_periods=max(155//3, 2)).std()
    vol_slow = ret.rolling(34, min_periods=max(34//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.905625 + 0.0006405 * anchor
    return base_signal.diff()

def f10_vreg_405_jerk_v405_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=162, w2=45, w3=767, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(45, min_periods=max(45//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 162)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1574 * slope + 0.0006406 * anchor
    return base_signal.diff()

def f10_vreg_406_accel_v406_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=169, w2=56, w3=23, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(56, min_periods=max(56//3, 2)).mean()
    noise = impulse.abs().rolling(23, min_periods=max(23//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.934375 + 0.0006407 * anchor
    return base_signal.diff()

def f10_vreg_407_jerk_v407_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=176, w2=67, w3=36, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 176)
    acceleration = _rolling_slope(velocity, 67)
    curvature = _rolling_slope(acceleration, 36)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1726 * acceleration + 0.0006408 * anchor
    return base_signal.diff()

def f10_vreg_408_accel_v408_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=183, w2=78, w3=49, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(183, min_periods=max(183//3, 2)).mean(), upside.rolling(78, min_periods=max(78//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(49) * 0.963125 + 0.0006409 * anchor
    return base_signal.diff()

def f10_vreg_409_jerk_v409_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=190, w2=89, w3=62, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(89, min_periods=max(89//3, 2)).max()
    rebound = x - x.rolling(190, min_periods=max(190//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1878 * _rolling_slope(draw, 62) + 0.000641 * anchor
    return base_signal.diff()

def f10_vreg_410_accel_v410_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=197, w2=100, w3=75, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 197)
    baseline = trend.rolling(100, min_periods=max(100//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(75, min_periods=max(75//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.991875 + 0.0006411 * anchor
    return base_signal.diff()

def f10_vreg_411_jerk_v411_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=204, w2=111, w3=88, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 204)
    slow = _rolling_slope(x, 111)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=88, adjust=False).mean() * 1.00625 + 0.0006412 * anchor
    return base_signal.diff()

def f10_vreg_412_accel_v412_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=211, w2=122, w3=101, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(122, min_periods=max(122//3, 2)).max()
    trough = x.rolling(211, min_periods=max(211//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.020625 + 0.0006413 * anchor
    return base_signal.diff()

def f10_vreg_413_jerk_v413_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=218, w2=133, w3=114, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(133, min_periods=max(133//3, 2)).rank(pct=True)
    persistence = change.rolling(114, min_periods=max(114//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2182 * persistence + 0.0006414 * anchor
    return base_signal.diff()

def f10_vreg_414_accel_v414_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=225, w2=144, w3=127, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(225, min_periods=max(225//3, 2)).std()
    vol_slow = ret.rolling(144, min_periods=max(144//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.049375 + 0.0006415 * anchor
    return base_signal.diff()

def f10_vreg_415_jerk_v415_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=232, w2=155, w3=140, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(155, min_periods=max(155//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 232)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2334 * slope + 0.0006416 * anchor
    return base_signal.diff()

def f10_vreg_416_accel_v416_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=239, w2=166, w3=153, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(166, min_periods=max(166//3, 2)).mean()
    noise = impulse.abs().rolling(153, min_periods=max(153//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.078125 + 0.0006417 * anchor
    return base_signal.diff()

def f10_vreg_417_jerk_v417_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=246, w2=177, w3=166, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 246)
    acceleration = _rolling_slope(velocity, 177)
    curvature = _rolling_slope(acceleration, 166)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2486 * acceleration + 0.0006418 * anchor
    return base_signal.diff()

def f10_vreg_418_accel_v418_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=253, w2=188, w3=179, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(253, min_periods=max(253//3, 2)).mean(), upside.rolling(188, min_periods=max(188//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.106875 + 0.0006419 * anchor
    return base_signal.diff()

def f10_vreg_419_jerk_v419_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=9, w2=199, w3=192, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(199, min_periods=max(199//3, 2)).max()
    rebound = x - x.rolling(9, min_periods=max(9//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2638 * _rolling_slope(draw, 192) + 0.000642 * anchor
    return base_signal.diff()

def f10_vreg_420_accel_v420_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=16, w2=210, w3=205, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 16)
    baseline = trend.rolling(210, min_periods=max(210//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(205, min_periods=max(205//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.135625 + 0.0006421 * anchor
    return base_signal.diff()

def f10_vreg_421_jerk_v421_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=23, w2=221, w3=218, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 23)
    slow = _rolling_slope(x, 221)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=218, adjust=False).mean() * 1.15 + 0.0006422 * anchor
    return base_signal.diff()

def f10_vreg_422_accel_v422_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=30, w2=232, w3=231, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(232, min_periods=max(232//3, 2)).max()
    trough = x.rolling(30, min_periods=max(30//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.164375 + 0.0006423 * anchor
    return base_signal.diff()

def f10_vreg_423_jerk_v423_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=37, w2=243, w3=244, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(37)
    rank = change.rolling(243, min_periods=max(243//3, 2)).rank(pct=True)
    persistence = change.rolling(244, min_periods=max(244//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2942 * persistence + 0.0006424 * anchor
    return base_signal.diff()

def f10_vreg_424_accel_v424_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=44, w2=254, w3=257, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(44, min_periods=max(44//3, 2)).std()
    vol_slow = ret.rolling(254, min_periods=max(254//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.193125 + 0.0006425 * anchor
    return base_signal.diff()

def f10_vreg_425_jerk_v425_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=51, w2=265, w3=270, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(265, min_periods=max(265//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 51)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3094 * slope + 0.0006426 * anchor
    return base_signal.diff()

def f10_vreg_426_accel_v426_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=58, w2=276, w3=283, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(58)
    drag = impulse.rolling(276, min_periods=max(276//3, 2)).mean()
    noise = impulse.abs().rolling(283, min_periods=max(283//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.221875 + 0.0006427 * anchor
    return base_signal.diff()

def f10_vreg_427_jerk_v427_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=65, w2=287, w3=296, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 65)
    acceleration = _rolling_slope(velocity, 287)
    curvature = _rolling_slope(acceleration, 296)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3246 * acceleration + 0.0006428 * anchor
    return base_signal.diff()

def f10_vreg_428_accel_v428_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=72, w2=298, w3=309, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(72, min_periods=max(72//3, 2)).mean(), upside.rolling(298, min_periods=max(298//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.250625 + 0.0006429 * anchor
    return base_signal.diff()

def f10_vreg_429_jerk_v429_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=79, w2=309, w3=322, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(309, min_periods=max(309//3, 2)).max()
    rebound = x - x.rolling(79, min_periods=max(79//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3398 * _rolling_slope(draw, 322) + 0.000643 * anchor
    return base_signal.diff()

def f10_vreg_430_accel_v430_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=86, w2=320, w3=335, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 86)
    baseline = trend.rolling(320, min_periods=max(320//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(335, min_periods=max(335//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.279375 + 0.0006431 * anchor
    return base_signal.diff()

def f10_vreg_431_jerk_v431_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=93, w2=331, w3=348, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 93)
    slow = _rolling_slope(x, 331)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.29375 + 0.0006432 * anchor
    return base_signal.diff()

def f10_vreg_432_accel_v432_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=100, w2=342, w3=361, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(342, min_periods=max(342//3, 2)).max()
    trough = x.rolling(100, min_periods=max(100//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.308125 + 0.0006433 * anchor
    return base_signal.diff()

def f10_vreg_433_jerk_v433_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=107, w2=353, w3=374, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(107)
    rank = change.rolling(353, min_periods=max(353//3, 2)).rank(pct=True)
    persistence = change.rolling(374, min_periods=max(374//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3702 * persistence + 0.0006434 * anchor
    return base_signal.diff()

def f10_vreg_434_accel_v434_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=114, w2=364, w3=387, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(114, min_periods=max(114//3, 2)).std()
    vol_slow = ret.rolling(364, min_periods=max(364//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.336875 + 0.0006435 * anchor
    return base_signal.diff()

def f10_vreg_435_jerk_v435_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=121, w2=375, w3=400, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(375, min_periods=max(375//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 121)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3854 * slope + 0.0006436 * anchor
    return base_signal.diff()

def f10_vreg_436_accel_v436_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=128, w2=386, w3=413, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(386, min_periods=max(386//3, 2)).mean()
    noise = impulse.abs().rolling(413, min_periods=max(413//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.365625 + 0.0006437 * anchor
    return base_signal.diff()

def f10_vreg_437_jerk_v437_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=135, w2=397, w3=426, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 135)
    acceleration = _rolling_slope(velocity, 397)
    curvature = _rolling_slope(acceleration, 426)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.4006 * acceleration + 0.0006438 * anchor
    return base_signal.diff()

def f10_vreg_438_accel_v438_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=142, w2=408, w3=439, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(142, min_periods=max(142//3, 2)).mean(), upside.rolling(408, min_periods=max(408//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.394375 + 0.0006439 * anchor
    return base_signal.diff()

def f10_vreg_439_jerk_v439_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=149, w2=419, w3=452, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(419, min_periods=max(419//3, 2)).max()
    rebound = x - x.rolling(149, min_periods=max(149//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0394 * _rolling_slope(draw, 452) + 0.000644 * anchor
    return base_signal.diff()

def f10_vreg_440_accel_v440_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=156, w2=430, w3=465, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 156)
    baseline = trend.rolling(430, min_periods=max(430//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(465, min_periods=max(465//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.423125 + 0.0006441 * anchor
    return base_signal.diff()

def f10_vreg_441_jerk_v441_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=163, w2=441, w3=478, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 163)
    slow = _rolling_slope(x, 441)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.4375 + 0.0006442 * anchor
    return base_signal.diff()

def f10_vreg_442_accel_v442_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=170, w2=452, w3=491, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(452, min_periods=max(452//3, 2)).max()
    trough = x.rolling(170, min_periods=max(170//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.451875 + 0.0006443 * anchor
    return base_signal.diff()

def f10_vreg_443_jerk_v443_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=177, w2=463, w3=504, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(463, min_periods=max(463//3, 2)).rank(pct=True)
    persistence = change.rolling(504, min_periods=max(504//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0698 * persistence + 0.0006444 * anchor
    return base_signal.diff()

def f10_vreg_444_accel_v444_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=184, w2=474, w3=517, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(184, min_periods=max(184//3, 2)).std()
    vol_slow = ret.rolling(474, min_periods=max(474//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.480625 + 0.0006445 * anchor
    return base_signal.diff()

def f10_vreg_445_jerk_v445_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=191, w2=485, w3=530, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(485, min_periods=max(485//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 191)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.085 * slope + 0.0006446 * anchor
    return base_signal.diff()

def f10_vreg_446_accel_v446_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=198, w2=496, w3=543, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(496, min_periods=max(496//3, 2)).mean()
    noise = impulse.abs().rolling(543, min_periods=max(543//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.509375 + 0.0006447 * anchor
    return base_signal.diff()

def f10_vreg_447_jerk_v447_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=205, w2=507, w3=556, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 205)
    acceleration = _rolling_slope(velocity, 507)
    curvature = _rolling_slope(acceleration, 556)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1002 * acceleration + 0.0006448 * anchor
    return base_signal.diff()

def f10_vreg_448_accel_v448_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=212, w2=15, w3=569, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(212, min_periods=max(212//3, 2)).mean(), upside.rolling(15, min_periods=max(15//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.538125 + 0.0006449 * anchor
    return base_signal.diff()

def f10_vreg_449_jerk_v449_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=219, w2=26, w3=582, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(26, min_periods=max(26//3, 2)).max()
    rebound = x - x.rolling(219, min_periods=max(219//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1154 * _rolling_slope(draw, 582) + 0.000645 * anchor
    return base_signal.diff()

def f10_vreg_450_accel_v450_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=226, w2=37, w3=595, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 226)
    baseline = trend.rolling(37, min_periods=max(37//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(595, min_periods=max(595//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.566875 + 0.0006451 * anchor
    return base_signal.diff()
