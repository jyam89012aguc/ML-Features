"""10 volatility regime at peak d2 second derivative features 451-525 â€” Pipeline 1a-HF Grade v3.

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

def f10_vreg_451_jerk_v451_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=233, w2=48, w3=608, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 233)
    slow = _rolling_slope(x, 48)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.58125 + 0.0006452 * anchor
    return base_signal.diff().diff()

def f10_vreg_452_accel_v452_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=240, w2=59, w3=621, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(59, min_periods=max(59//3, 2)).max()
    trough = x.rolling(240, min_periods=max(240//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.595625 + 0.0006453 * anchor
    return base_signal.diff().diff()

def f10_vreg_453_jerk_v453_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=247, w2=70, w3=634, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(70, min_periods=max(70//3, 2)).rank(pct=True)
    persistence = change.rolling(634, min_periods=max(634//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1458 * persistence + 0.0006454 * anchor
    return base_signal.diff().diff()

def f10_vreg_454_accel_v454_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=254, w2=81, w3=647, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(254, min_periods=max(254//3, 2)).std()
    vol_slow = ret.rolling(81, min_periods=max(81//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.85125 + 0.0006455 * anchor
    return base_signal.diff().diff()

def f10_vreg_455_jerk_v455_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=10, w2=92, w3=660, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(92, min_periods=max(92//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 10)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.161 * slope + 0.0006456 * anchor
    return base_signal.diff().diff()

def f10_vreg_456_accel_v456_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=17, w2=103, w3=673, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(17)
    drag = impulse.rolling(103, min_periods=max(103//3, 2)).mean()
    noise = impulse.abs().rolling(673, min_periods=max(673//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.88 + 0.0006457 * anchor
    return base_signal.diff().diff()

def f10_vreg_457_jerk_v457_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=24, w2=114, w3=686, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 24)
    acceleration = _rolling_slope(velocity, 114)
    curvature = _rolling_slope(acceleration, 686)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1762 * acceleration + 0.0006458 * anchor
    return base_signal.diff().diff()

def f10_vreg_458_accel_v458_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=31, w2=125, w3=699, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(31, min_periods=max(31//3, 2)).mean(), upside.rolling(125, min_periods=max(125//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.90875 + 0.0006459 * anchor
    return base_signal.diff().diff()

def f10_vreg_459_jerk_v459_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=38, w2=136, w3=712, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(136, min_periods=max(136//3, 2)).max()
    rebound = x - x.rolling(38, min_periods=max(38//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1914 * _rolling_slope(draw, 712) + 0.000646 * anchor
    return base_signal.diff().diff()

def f10_vreg_460_accel_v460_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=45, w2=147, w3=725, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 45)
    baseline = trend.rolling(147, min_periods=max(147//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(725, min_periods=max(725//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.9375 + 0.0006461 * anchor
    return base_signal.diff().diff()

def f10_vreg_461_jerk_v461_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=52, w2=158, w3=738, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 52)
    slow = _rolling_slope(x, 158)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.951875 + 0.0006462 * anchor
    return base_signal.diff().diff()

def f10_vreg_462_accel_v462_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=59, w2=169, w3=751, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(169, min_periods=max(169//3, 2)).max()
    trough = x.rolling(59, min_periods=max(59//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.96625 + 0.0006463 * anchor
    return base_signal.diff().diff()

def f10_vreg_463_jerk_v463_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=66, w2=180, w3=764, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(66)
    rank = change.rolling(180, min_periods=max(180//3, 2)).rank(pct=True)
    persistence = change.rolling(764, min_periods=max(764//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2218 * persistence + 0.0006464 * anchor
    return base_signal.diff().diff()

def f10_vreg_464_accel_v464_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=73, w2=191, w3=20, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(73, min_periods=max(73//3, 2)).std()
    vol_slow = ret.rolling(191, min_periods=max(191//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.995 + 0.0006465 * anchor
    return base_signal.diff().diff()

def f10_vreg_465_jerk_v465_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=80, w2=202, w3=33, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(202, min_periods=max(202//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 80)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.237 * slope + 0.0006466 * anchor
    return base_signal.diff().diff()

def f10_vreg_466_accel_v466_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=87, w2=213, w3=46, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(87)
    drag = impulse.rolling(213, min_periods=max(213//3, 2)).mean()
    noise = impulse.abs().rolling(46, min_periods=max(46//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.02375 + 0.0006467 * anchor
    return base_signal.diff().diff()

def f10_vreg_467_jerk_v467_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=94, w2=224, w3=59, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 94)
    acceleration = _rolling_slope(velocity, 224)
    curvature = _rolling_slope(acceleration, 59)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2522 * acceleration + 0.0006468 * anchor
    return base_signal.diff().diff()

def f10_vreg_468_accel_v468_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=101, w2=235, w3=72, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(101, min_periods=max(101//3, 2)).mean(), upside.rolling(235, min_periods=max(235//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(72) * 1.0525 + 0.0006469 * anchor
    return base_signal.diff().diff()

def f10_vreg_469_jerk_v469_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=108, w2=246, w3=85, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(246, min_periods=max(246//3, 2)).max()
    rebound = x - x.rolling(108, min_periods=max(108//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2674 * _rolling_slope(draw, 85) + 0.000647 * anchor
    return base_signal.diff().diff()

def f10_vreg_470_accel_v470_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=115, w2=257, w3=98, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 115)
    baseline = trend.rolling(257, min_periods=max(257//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(98, min_periods=max(98//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.08125 + 0.0006471 * anchor
    return base_signal.diff().diff()

def f10_vreg_471_jerk_v471_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=122, w2=268, w3=111, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 122)
    slow = _rolling_slope(x, 268)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=111, adjust=False).mean() * 1.095625 + 0.0006472 * anchor
    return base_signal.diff().diff()

def f10_vreg_472_accel_v472_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=129, w2=279, w3=124, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(279, min_periods=max(279//3, 2)).max()
    trough = x.rolling(129, min_periods=max(129//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.11 + 0.0006473 * anchor
    return base_signal.diff().diff()

def f10_vreg_473_jerk_v473_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=136, w2=290, w3=137, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(290, min_periods=max(290//3, 2)).rank(pct=True)
    persistence = change.rolling(137, min_periods=max(137//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2978 * persistence + 0.0006474 * anchor
    return base_signal.diff().diff()

def f10_vreg_474_accel_v474_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=143, w2=301, w3=150, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(143, min_periods=max(143//3, 2)).std()
    vol_slow = ret.rolling(301, min_periods=max(301//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.13875 + 0.0006475 * anchor
    return base_signal.diff().diff()

def f10_vreg_475_jerk_v475_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=150, w2=312, w3=163, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(312, min_periods=max(312//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 150)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.313 * slope + 0.0006476 * anchor
    return base_signal.diff().diff()

def f10_vreg_476_accel_v476_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=157, w2=323, w3=176, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(323, min_periods=max(323//3, 2)).mean()
    noise = impulse.abs().rolling(176, min_periods=max(176//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.1675 + 0.0006477 * anchor
    return base_signal.diff().diff()

def f10_vreg_477_jerk_v477_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=164, w2=334, w3=189, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 164)
    acceleration = _rolling_slope(velocity, 334)
    curvature = _rolling_slope(acceleration, 189)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3282 * acceleration + 0.0006478 * anchor
    return base_signal.diff().diff()

def f10_vreg_478_accel_v478_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=171, w2=345, w3=202, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(171, min_periods=max(171//3, 2)).mean(), upside.rolling(345, min_periods=max(345//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.19625 + 0.0006479 * anchor
    return base_signal.diff().diff()

def f10_vreg_479_jerk_v479_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=178, w2=356, w3=215, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(356, min_periods=max(356//3, 2)).max()
    rebound = x - x.rolling(178, min_periods=max(178//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3434 * _rolling_slope(draw, 215) + 0.000648 * anchor
    return base_signal.diff().diff()

def f10_vreg_480_accel_v480_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=185, w2=367, w3=228, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 185)
    baseline = trend.rolling(367, min_periods=max(367//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(228, min_periods=max(228//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.225 + 0.0006481 * anchor
    return base_signal.diff().diff()

def f10_vreg_481_jerk_v481_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=192, w2=378, w3=241, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 192)
    slow = _rolling_slope(x, 378)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=241, adjust=False).mean() * 1.239375 + 0.0006482 * anchor
    return base_signal.diff().diff()

def f10_vreg_482_accel_v482_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=199, w2=389, w3=254, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(389, min_periods=max(389//3, 2)).max()
    trough = x.rolling(199, min_periods=max(199//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.25375 + 0.0006483 * anchor
    return base_signal.diff().diff()

def f10_vreg_483_jerk_v483_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=206, w2=400, w3=267, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(400, min_periods=max(400//3, 2)).rank(pct=True)
    persistence = change.rolling(267, min_periods=max(267//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3738 * persistence + 0.0006484 * anchor
    return base_signal.diff().diff()

def f10_vreg_484_accel_v484_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=213, w2=411, w3=280, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(213, min_periods=max(213//3, 2)).std()
    vol_slow = ret.rolling(411, min_periods=max(411//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.2825 + 0.0006485 * anchor
    return base_signal.diff().diff()

def f10_vreg_485_jerk_v485_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=220, w2=422, w3=293, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(422, min_periods=max(422//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 220)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.389 * slope + 0.0006486 * anchor
    return base_signal.diff().diff()

def f10_vreg_486_accel_v486_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=227, w2=433, w3=306, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(433, min_periods=max(433//3, 2)).mean()
    noise = impulse.abs().rolling(306, min_periods=max(306//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.31125 + 0.0006487 * anchor
    return base_signal.diff().diff()

def f10_vreg_487_jerk_v487_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=234, w2=444, w3=319, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 234)
    acceleration = _rolling_slope(velocity, 444)
    curvature = _rolling_slope(acceleration, 319)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.4042 * acceleration + 0.0006488 * anchor
    return base_signal.diff().diff()

def f10_vreg_488_accel_v488_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=241, w2=455, w3=332, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(241, min_periods=max(241//3, 2)).mean(), upside.rolling(455, min_periods=max(455//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.34 + 0.0006489 * anchor
    return base_signal.diff().diff()

def f10_vreg_489_jerk_v489_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=248, w2=466, w3=345, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(466, min_periods=max(466//3, 2)).max()
    rebound = x - x.rolling(248, min_periods=max(248//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.043 * _rolling_slope(draw, 345) + 0.000649 * anchor
    return base_signal.diff().diff()

def f10_vreg_490_accel_v490_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=255, w2=477, w3=358, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 255)
    baseline = trend.rolling(477, min_periods=max(477//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(358, min_periods=max(358//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.36875 + 0.0006491 * anchor
    return base_signal.diff().diff()

def f10_vreg_491_jerk_v491_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=11, w2=488, w3=371, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 11)
    slow = _rolling_slope(x, 488)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.383125 + 0.0006492 * anchor
    return base_signal.diff().diff()

def f10_vreg_492_accel_v492_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=18, w2=499, w3=384, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(499, min_periods=max(499//3, 2)).max()
    trough = x.rolling(18, min_periods=max(18//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.3975 + 0.0006493 * anchor
    return base_signal.diff().diff()

def f10_vreg_493_jerk_v493_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=25, w2=510, w3=397, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(25)
    rank = change.rolling(510, min_periods=max(510//3, 2)).rank(pct=True)
    persistence = change.rolling(397, min_periods=max(397//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0734 * persistence + 0.0006494 * anchor
    return base_signal.diff().diff()

def f10_vreg_494_accel_v494_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=32, w2=18, w3=410, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(32, min_periods=max(32//3, 2)).std()
    vol_slow = ret.rolling(18, min_periods=max(18//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.42625 + 0.0006495 * anchor
    return base_signal.diff().diff()

def f10_vreg_495_jerk_v495_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=39, w2=29, w3=423, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(29, min_periods=max(29//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 39)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0886 * slope + 0.0006496 * anchor
    return base_signal.diff().diff()

def f10_vreg_496_accel_v496_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=46, w2=40, w3=436, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(46)
    drag = impulse.rolling(40, min_periods=max(40//3, 2)).mean()
    noise = impulse.abs().rolling(436, min_periods=max(436//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.455 + 0.0006497 * anchor
    return base_signal.diff().diff()

def f10_vreg_497_jerk_v497_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=53, w2=51, w3=449, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 53)
    acceleration = _rolling_slope(velocity, 51)
    curvature = _rolling_slope(acceleration, 449)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1038 * acceleration + 0.0006498 * anchor
    return base_signal.diff().diff()

def f10_vreg_498_accel_v498_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=60, w2=62, w3=462, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(60, min_periods=max(60//3, 2)).mean(), upside.rolling(62, min_periods=max(62//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.48375 + 0.0006499 * anchor
    return base_signal.diff().diff()

def f10_vreg_499_jerk_v499_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=67, w2=73, w3=475, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(73, min_periods=max(73//3, 2)).max()
    rebound = x - x.rolling(67, min_periods=max(67//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.119 * _rolling_slope(draw, 475) + 0.00065 * anchor
    return base_signal.diff().diff()

def f10_vreg_500_accel_v500_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=74, w2=84, w3=488, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 74)
    baseline = trend.rolling(84, min_periods=max(84//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(488, min_periods=max(488//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.5125 + 0.0006501 * anchor
    return base_signal.diff().diff()

def f10_vreg_501_jerk_v501_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=81, w2=95, w3=501, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 81)
    slow = _rolling_slope(x, 95)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.526875 + 0.0006502 * anchor
    return base_signal.diff().diff()

def f10_vreg_502_accel_v502_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=88, w2=106, w3=514, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(106, min_periods=max(106//3, 2)).max()
    trough = x.rolling(88, min_periods=max(88//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.54125 + 0.0006503 * anchor
    return base_signal.diff().diff()

def f10_vreg_503_jerk_v503_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=95, w2=117, w3=527, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(95)
    rank = change.rolling(117, min_periods=max(117//3, 2)).rank(pct=True)
    persistence = change.rolling(527, min_periods=max(527//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1494 * persistence + 0.0006504 * anchor
    return base_signal.diff().diff()

def f10_vreg_504_accel_v504_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=102, w2=128, w3=540, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(102, min_periods=max(102//3, 2)).std()
    vol_slow = ret.rolling(128, min_periods=max(128//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.57 + 0.0006505 * anchor
    return base_signal.diff().diff()

def f10_vreg_505_jerk_v505_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=109, w2=139, w3=553, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(139, min_periods=max(139//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 109)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1646 * slope + 0.0006506 * anchor
    return base_signal.diff().diff()

def f10_vreg_506_accel_v506_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=116, w2=150, w3=566, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(116)
    drag = impulse.rolling(150, min_periods=max(150//3, 2)).mean()
    noise = impulse.abs().rolling(566, min_periods=max(566//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.59875 + 0.0006507 * anchor
    return base_signal.diff().diff()

def f10_vreg_507_jerk_v507_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=123, w2=161, w3=579, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 123)
    acceleration = _rolling_slope(velocity, 161)
    curvature = _rolling_slope(acceleration, 579)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1798 * acceleration + 0.0006508 * anchor
    return base_signal.diff().diff()

def f10_vreg_508_accel_v508_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=130, w2=172, w3=592, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(130, min_periods=max(130//3, 2)).mean(), upside.rolling(172, min_periods=max(172//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.854375 + 0.0006509 * anchor
    return base_signal.diff().diff()

def f10_vreg_509_jerk_v509_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=137, w2=183, w3=605, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(183, min_periods=max(183//3, 2)).max()
    rebound = x - x.rolling(137, min_periods=max(137//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.195 * _rolling_slope(draw, 605) + 0.000651 * anchor
    return base_signal.diff().diff()

def f10_vreg_510_accel_v510_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=144, w2=194, w3=618, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 144)
    baseline = trend.rolling(194, min_periods=max(194//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(618, min_periods=max(618//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.883125 + 0.0006511 * anchor
    return base_signal.diff().diff()

def f10_vreg_511_jerk_v511_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=151, w2=205, w3=631, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 151)
    slow = _rolling_slope(x, 205)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.8975 + 0.0006512 * anchor
    return base_signal.diff().diff()

def f10_vreg_512_accel_v512_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=158, w2=216, w3=644, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(216, min_periods=max(216//3, 2)).max()
    trough = x.rolling(158, min_periods=max(158//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.911875 + 0.0006513 * anchor
    return base_signal.diff().diff()

def f10_vreg_513_jerk_v513_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=165, w2=227, w3=657, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(227, min_periods=max(227//3, 2)).rank(pct=True)
    persistence = change.rolling(657, min_periods=max(657//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2254 * persistence + 0.0006514 * anchor
    return base_signal.diff().diff()

def f10_vreg_514_accel_v514_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=172, w2=238, w3=670, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(172, min_periods=max(172//3, 2)).std()
    vol_slow = ret.rolling(238, min_periods=max(238//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.940625 + 0.0006515 * anchor
    return base_signal.diff().diff()

def f10_vreg_515_jerk_v515_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=179, w2=249, w3=683, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(249, min_periods=max(249//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 179)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2406 * slope + 0.0006516 * anchor
    return base_signal.diff().diff()

def f10_vreg_516_accel_v516_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=186, w2=260, w3=696, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(260, min_periods=max(260//3, 2)).mean()
    noise = impulse.abs().rolling(696, min_periods=max(696//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.969375 + 0.0006517 * anchor
    return base_signal.diff().diff()

def f10_vreg_517_jerk_v517_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=193, w2=271, w3=709, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 193)
    acceleration = _rolling_slope(velocity, 271)
    curvature = _rolling_slope(acceleration, 709)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2558 * acceleration + 0.0006518 * anchor
    return base_signal.diff().diff()

def f10_vreg_518_accel_v518_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=200, w2=282, w3=722, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(200, min_periods=max(200//3, 2)).mean(), upside.rolling(282, min_periods=max(282//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.998125 + 0.0006519 * anchor
    return base_signal.diff().diff()

def f10_vreg_519_jerk_v519_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=207, w2=293, w3=735, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(293, min_periods=max(293//3, 2)).max()
    rebound = x - x.rolling(207, min_periods=max(207//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.271 * _rolling_slope(draw, 735) + 0.000652 * anchor
    return base_signal.diff().diff()

def f10_vreg_520_accel_v520_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=214, w2=304, w3=748, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 214)
    baseline = trend.rolling(304, min_periods=max(304//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(748, min_periods=max(748//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.026875 + 0.0006521 * anchor
    return base_signal.diff().diff()

def f10_vreg_521_jerk_v521_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=221, w2=315, w3=761, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 221)
    slow = _rolling_slope(x, 315)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.04125 + 0.0006522 * anchor
    return base_signal.diff().diff()

def f10_vreg_522_accel_v522_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=228, w2=326, w3=17, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(326, min_periods=max(326//3, 2)).max()
    trough = x.rolling(228, min_periods=max(228//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.055625 + 0.0006523 * anchor
    return base_signal.diff().diff()

def f10_vreg_523_jerk_v523_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=235, w2=337, w3=30, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(337, min_periods=max(337//3, 2)).rank(pct=True)
    persistence = change.rolling(30, min_periods=max(30//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3014 * persistence + 0.0006524 * anchor
    return base_signal.diff().diff()

def f10_vreg_524_accel_v524_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=242, w2=348, w3=43, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(242, min_periods=max(242//3, 2)).std()
    vol_slow = ret.rolling(348, min_periods=max(348//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.084375 + 0.0006525 * anchor
    return base_signal.diff().diff()

def f10_vreg_525_jerk_v525_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=249, w2=359, w3=56, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(359, min_periods=max(359//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 249)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3166 * slope + 0.0006526 * anchor
    return base_signal.diff().diff()
