"""02 advance speed d1 first derivative features 301-375 â€” Pipeline 1a-HF Grade v3.

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

def f02_adv_301_jerk_v301_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=37, w2=364, w3=373, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 37)
    slow = _rolling_slope(x, 364)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.431875 + 9.02e-05 * anchor
    return base_signal.diff()

def f02_adv_302_accel_v302_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=44, w2=375, w3=386, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(375, min_periods=max(375//3, 2)).max()
    trough = x.rolling(44, min_periods=max(44//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.44625 + 9.03e-05 * anchor
    return base_signal.diff()

def f02_adv_303_jerk_v303_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=51, w2=386, w3=399, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(51)
    rank = change.rolling(386, min_periods=max(386//3, 2)).rank(pct=True)
    persistence = change.rolling(399, min_periods=max(399//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1226 * persistence + 9.04e-05 * anchor
    return base_signal.diff()

def f02_adv_304_accel_v304_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=58, w2=397, w3=412, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(58, min_periods=max(58//3, 2)).std()
    vol_slow = ret.rolling(397, min_periods=max(397//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.475 + 9.05e-05 * anchor
    return base_signal.diff()

def f02_adv_305_jerk_v305_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=65, w2=408, w3=425, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(408, min_periods=max(408//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 65)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1378 * slope + 9.06e-05 * anchor
    return base_signal.diff()

def f02_adv_306_accel_v306_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=72, w2=419, w3=438, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(72)
    drag = impulse.rolling(419, min_periods=max(419//3, 2)).mean()
    noise = impulse.abs().rolling(438, min_periods=max(438//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.50375 + 9.07e-05 * anchor
    return base_signal.diff()

def f02_adv_307_jerk_v307_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=79, w2=430, w3=451, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 79)
    acceleration = _rolling_slope(velocity, 430)
    curvature = _rolling_slope(acceleration, 451)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.153 * acceleration + 9.08e-05 * anchor
    return base_signal.diff()

def f02_adv_308_accel_v308_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=86, w2=441, w3=464, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(86, min_periods=max(86//3, 2)).mean(), upside.rolling(441, min_periods=max(441//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.5325 + 9.09e-05 * anchor
    return base_signal.diff()

def f02_adv_309_jerk_v309_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=93, w2=452, w3=477, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(452, min_periods=max(452//3, 2)).max()
    rebound = x - x.rolling(93, min_periods=max(93//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1682 * _rolling_slope(draw, 477) + 9.1e-05 * anchor
    return base_signal.diff()

def f02_adv_310_accel_v310_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=100, w2=463, w3=490, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 100)
    baseline = trend.rolling(463, min_periods=max(463//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(490, min_periods=max(490//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.56125 + 9.11e-05 * anchor
    return base_signal.diff()

def f02_adv_311_jerk_v311_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=107, w2=474, w3=503, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 107)
    slow = _rolling_slope(x, 474)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.575625 + 9.12e-05 * anchor
    return base_signal.diff()

def f02_adv_312_accel_v312_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=114, w2=485, w3=516, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(485, min_periods=max(485//3, 2)).max()
    trough = x.rolling(114, min_periods=max(114//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.59 + 9.13e-05 * anchor
    return base_signal.diff()

def f02_adv_313_jerk_v313_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=121, w2=496, w3=529, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(121)
    rank = change.rolling(496, min_periods=max(496//3, 2)).rank(pct=True)
    persistence = change.rolling(529, min_periods=max(529//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1986 * persistence + 9.14e-05 * anchor
    return base_signal.diff()

def f02_adv_314_accel_v314_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=128, w2=507, w3=542, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(128, min_periods=max(128//3, 2)).std()
    vol_slow = ret.rolling(507, min_periods=max(507//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.61875 + 9.15e-05 * anchor
    return base_signal.diff()

def f02_adv_315_jerk_v315_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=135, w2=15, w3=555, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(15, min_periods=max(15//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 135)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2138 * slope + 9.16e-05 * anchor
    return base_signal.diff()

def f02_adv_316_accel_v316_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=142, w2=26, w3=568, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(26, min_periods=max(26//3, 2)).mean()
    noise = impulse.abs().rolling(568, min_periods=max(568//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.874375 + 9.17e-05 * anchor
    return base_signal.diff()

def f02_adv_317_jerk_v317_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=149, w2=37, w3=581, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 149)
    acceleration = _rolling_slope(velocity, 37)
    curvature = _rolling_slope(acceleration, 581)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.229 * acceleration + 9.18e-05 * anchor
    return base_signal.diff()

def f02_adv_318_accel_v318_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=156, w2=48, w3=594, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(156, min_periods=max(156//3, 2)).mean(), upside.rolling(48, min_periods=max(48//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.903125 + 9.19e-05 * anchor
    return base_signal.diff()

def f02_adv_319_jerk_v319_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=163, w2=59, w3=607, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(59, min_periods=max(59//3, 2)).max()
    rebound = x - x.rolling(163, min_periods=max(163//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2442 * _rolling_slope(draw, 607) + 9.2e-05 * anchor
    return base_signal.diff()

def f02_adv_320_accel_v320_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=170, w2=70, w3=620, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 170)
    baseline = trend.rolling(70, min_periods=max(70//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(620, min_periods=max(620//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.931875 + 9.21e-05 * anchor
    return base_signal.diff()

def f02_adv_321_jerk_v321_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=177, w2=81, w3=633, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 177)
    slow = _rolling_slope(x, 81)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.94625 + 9.22e-05 * anchor
    return base_signal.diff()

def f02_adv_322_accel_v322_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=184, w2=92, w3=646, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(92, min_periods=max(92//3, 2)).max()
    trough = x.rolling(184, min_periods=max(184//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.960625 + 9.23e-05 * anchor
    return base_signal.diff()

def f02_adv_323_jerk_v323_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=191, w2=103, w3=659, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(103, min_periods=max(103//3, 2)).rank(pct=True)
    persistence = change.rolling(659, min_periods=max(659//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2746 * persistence + 9.24e-05 * anchor
    return base_signal.diff()

def f02_adv_324_accel_v324_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=198, w2=114, w3=672, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(198, min_periods=max(198//3, 2)).std()
    vol_slow = ret.rolling(114, min_periods=max(114//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.989375 + 9.25e-05 * anchor
    return base_signal.diff()

def f02_adv_325_jerk_v325_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=205, w2=125, w3=685, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(125, min_periods=max(125//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 205)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2898 * slope + 9.26e-05 * anchor
    return base_signal.diff()

def f02_adv_326_accel_v326_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=212, w2=136, w3=698, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(136, min_periods=max(136//3, 2)).mean()
    noise = impulse.abs().rolling(698, min_periods=max(698//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.018125 + 9.27e-05 * anchor
    return base_signal.diff()

def f02_adv_327_jerk_v327_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=219, w2=147, w3=711, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 219)
    acceleration = _rolling_slope(velocity, 147)
    curvature = _rolling_slope(acceleration, 711)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.305 * acceleration + 9.28e-05 * anchor
    return base_signal.diff()

def f02_adv_328_accel_v328_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=226, w2=158, w3=724, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(226, min_periods=max(226//3, 2)).mean(), upside.rolling(158, min_periods=max(158//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.046875 + 9.29e-05 * anchor
    return base_signal.diff()

def f02_adv_329_jerk_v329_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=233, w2=169, w3=737, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(169, min_periods=max(169//3, 2)).max()
    rebound = x - x.rolling(233, min_periods=max(233//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3202 * _rolling_slope(draw, 737) + 9.3e-05 * anchor
    return base_signal.diff()

def f02_adv_330_accel_v330_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=240, w2=180, w3=750, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 240)
    baseline = trend.rolling(180, min_periods=max(180//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(750, min_periods=max(750//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.075625 + 9.31e-05 * anchor
    return base_signal.diff()

def f02_adv_331_jerk_v331_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=247, w2=191, w3=763, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 247)
    slow = _rolling_slope(x, 191)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.09 + 9.32e-05 * anchor
    return base_signal.diff()

def f02_adv_332_accel_v332_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=254, w2=202, w3=19, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(202, min_periods=max(202//3, 2)).max()
    trough = x.rolling(254, min_periods=max(254//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.104375 + 9.33e-05 * anchor
    return base_signal.diff()

def f02_adv_333_jerk_v333_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=10, w2=213, w3=32, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(10)
    rank = change.rolling(213, min_periods=max(213//3, 2)).rank(pct=True)
    persistence = change.rolling(32, min_periods=max(32//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3506 * persistence + 9.34e-05 * anchor
    return base_signal.diff()

def f02_adv_334_accel_v334_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=17, w2=224, w3=45, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(17, min_periods=max(17//3, 2)).std()
    vol_slow = ret.rolling(224, min_periods=max(224//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.133125 + 9.35e-05 * anchor
    return base_signal.diff()

def f02_adv_335_jerk_v335_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=24, w2=235, w3=58, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(235, min_periods=max(235//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 24)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3658 * slope + 9.36e-05 * anchor
    return base_signal.diff()

def f02_adv_336_accel_v336_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=31, w2=246, w3=71, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(31)
    drag = impulse.rolling(246, min_periods=max(246//3, 2)).mean()
    noise = impulse.abs().rolling(71, min_periods=max(71//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.161875 + 9.37e-05 * anchor
    return base_signal.diff()

def f02_adv_337_jerk_v337_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=38, w2=257, w3=84, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 38)
    acceleration = _rolling_slope(velocity, 257)
    curvature = _rolling_slope(acceleration, 84)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.381 * acceleration + 9.38e-05 * anchor
    return base_signal.diff()

def f02_adv_338_accel_v338_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=45, w2=268, w3=97, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(45, min_periods=max(45//3, 2)).mean(), upside.rolling(268, min_periods=max(268//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(97) * 1.190625 + 9.39e-05 * anchor
    return base_signal.diff()

def f02_adv_339_jerk_v339_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=52, w2=279, w3=110, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(279, min_periods=max(279//3, 2)).max()
    rebound = x - x.rolling(52, min_periods=max(52//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3962 * _rolling_slope(draw, 110) + 9.4e-05 * anchor
    return base_signal.diff()

def f02_adv_340_accel_v340_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=59, w2=290, w3=123, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 59)
    baseline = trend.rolling(290, min_periods=max(290//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(123, min_periods=max(123//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.219375 + 9.41e-05 * anchor
    return base_signal.diff()

def f02_adv_341_jerk_v341_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=66, w2=301, w3=136, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 66)
    slow = _rolling_slope(x, 301)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=136, adjust=False).mean() * 1.23375 + 9.42e-05 * anchor
    return base_signal.diff()

def f02_adv_342_accel_v342_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=73, w2=312, w3=149, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(312, min_periods=max(312//3, 2)).max()
    trough = x.rolling(73, min_periods=max(73//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.248125 + 9.43e-05 * anchor
    return base_signal.diff()

def f02_adv_343_jerk_v343_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=80, w2=323, w3=162, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(80)
    rank = change.rolling(323, min_periods=max(323//3, 2)).rank(pct=True)
    persistence = change.rolling(162, min_periods=max(162//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0502 * persistence + 9.44e-05 * anchor
    return base_signal.diff()

def f02_adv_344_accel_v344_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=87, w2=334, w3=175, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(87, min_periods=max(87//3, 2)).std()
    vol_slow = ret.rolling(334, min_periods=max(334//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.276875 + 9.45e-05 * anchor
    return base_signal.diff()

def f02_adv_345_jerk_v345_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=94, w2=345, w3=188, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(345, min_periods=max(345//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 94)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0654 * slope + 9.46e-05 * anchor
    return base_signal.diff()

def f02_adv_346_accel_v346_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=101, w2=356, w3=201, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(101)
    drag = impulse.rolling(356, min_periods=max(356//3, 2)).mean()
    noise = impulse.abs().rolling(201, min_periods=max(201//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.305625 + 9.47e-05 * anchor
    return base_signal.diff()

def f02_adv_347_jerk_v347_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=108, w2=367, w3=214, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 108)
    acceleration = _rolling_slope(velocity, 367)
    curvature = _rolling_slope(acceleration, 214)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0806 * acceleration + 9.48e-05 * anchor
    return base_signal.diff()

def f02_adv_348_accel_v348_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=115, w2=378, w3=227, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(115, min_periods=max(115//3, 2)).mean(), upside.rolling(378, min_periods=max(378//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.334375 + 9.49e-05 * anchor
    return base_signal.diff()

def f02_adv_349_jerk_v349_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=122, w2=389, w3=240, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(389, min_periods=max(389//3, 2)).max()
    rebound = x - x.rolling(122, min_periods=max(122//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0958 * _rolling_slope(draw, 240) + 9.5e-05 * anchor
    return base_signal.diff()

def f02_adv_350_accel_v350_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=129, w2=400, w3=253, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 129)
    baseline = trend.rolling(400, min_periods=max(400//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(253, min_periods=max(253//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.363125 + 9.51e-05 * anchor
    return base_signal.diff()

def f02_adv_351_jerk_v351_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=136, w2=411, w3=266, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 136)
    slow = _rolling_slope(x, 411)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=266, adjust=False).mean() * 1.3775 + 9.52e-05 * anchor
    return base_signal.diff()

def f02_adv_352_accel_v352_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=143, w2=422, w3=279, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(422, min_periods=max(422//3, 2)).max()
    trough = x.rolling(143, min_periods=max(143//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.391875 + 9.53e-05 * anchor
    return base_signal.diff()

def f02_adv_353_jerk_v353_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=150, w2=433, w3=292, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(433, min_periods=max(433//3, 2)).rank(pct=True)
    persistence = change.rolling(292, min_periods=max(292//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1262 * persistence + 9.54e-05 * anchor
    return base_signal.diff()

def f02_adv_354_accel_v354_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=157, w2=444, w3=305, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(157, min_periods=max(157//3, 2)).std()
    vol_slow = ret.rolling(444, min_periods=max(444//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.420625 + 9.55e-05 * anchor
    return base_signal.diff()

def f02_adv_355_jerk_v355_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=164, w2=455, w3=318, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(455, min_periods=max(455//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 164)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1414 * slope + 9.56e-05 * anchor
    return base_signal.diff()

def f02_adv_356_accel_v356_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=171, w2=466, w3=331, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(466, min_periods=max(466//3, 2)).mean()
    noise = impulse.abs().rolling(331, min_periods=max(331//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.449375 + 9.57e-05 * anchor
    return base_signal.diff()

def f02_adv_357_jerk_v357_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=178, w2=477, w3=344, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 178)
    acceleration = _rolling_slope(velocity, 477)
    curvature = _rolling_slope(acceleration, 344)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1566 * acceleration + 9.58e-05 * anchor
    return base_signal.diff()

def f02_adv_358_accel_v358_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=185, w2=488, w3=357, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(185, min_periods=max(185//3, 2)).mean(), upside.rolling(488, min_periods=max(488//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.478125 + 9.59e-05 * anchor
    return base_signal.diff()

def f02_adv_359_jerk_v359_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=192, w2=499, w3=370, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(499, min_periods=max(499//3, 2)).max()
    rebound = x - x.rolling(192, min_periods=max(192//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1718 * _rolling_slope(draw, 370) + 9.6e-05 * anchor
    return base_signal.diff()

def f02_adv_360_accel_v360_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=199, w2=510, w3=383, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 199)
    baseline = trend.rolling(510, min_periods=max(510//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(383, min_periods=max(383//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.506875 + 9.61e-05 * anchor
    return base_signal.diff()

def f02_adv_361_jerk_v361_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=206, w2=18, w3=396, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 206)
    slow = _rolling_slope(x, 18)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.52125 + 9.62e-05 * anchor
    return base_signal.diff()

def f02_adv_362_accel_v362_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=213, w2=29, w3=409, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(29, min_periods=max(29//3, 2)).max()
    trough = x.rolling(213, min_periods=max(213//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.535625 + 9.63e-05 * anchor
    return base_signal.diff()

def f02_adv_363_jerk_v363_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=220, w2=40, w3=422, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(40, min_periods=max(40//3, 2)).rank(pct=True)
    persistence = change.rolling(422, min_periods=max(422//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2022 * persistence + 9.64e-05 * anchor
    return base_signal.diff()

def f02_adv_364_accel_v364_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=227, w2=51, w3=435, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(227, min_periods=max(227//3, 2)).std()
    vol_slow = ret.rolling(51, min_periods=max(51//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.564375 + 9.65e-05 * anchor
    return base_signal.diff()

def f02_adv_365_jerk_v365_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=234, w2=62, w3=448, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(62, min_periods=max(62//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 234)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2174 * slope + 9.66e-05 * anchor
    return base_signal.diff()

def f02_adv_366_accel_v366_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=241, w2=73, w3=461, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(73, min_periods=max(73//3, 2)).mean()
    noise = impulse.abs().rolling(461, min_periods=max(461//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.593125 + 9.67e-05 * anchor
    return base_signal.diff()

def f02_adv_367_jerk_v367_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=248, w2=84, w3=474, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 248)
    acceleration = _rolling_slope(velocity, 84)
    curvature = _rolling_slope(acceleration, 474)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2326 * acceleration + 9.68e-05 * anchor
    return base_signal.diff()

def f02_adv_368_accel_v368_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=255, w2=95, w3=487, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(255, min_periods=max(255//3, 2)).mean(), upside.rolling(95, min_periods=max(95//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.621875 + 9.69e-05 * anchor
    return base_signal.diff()

def f02_adv_369_jerk_v369_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=11, w2=106, w3=500, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(106, min_periods=max(106//3, 2)).max()
    rebound = x - x.rolling(11, min_periods=max(11//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2478 * _rolling_slope(draw, 500) + 9.7e-05 * anchor
    return base_signal.diff()

def f02_adv_370_accel_v370_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=18, w2=117, w3=513, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 18)
    baseline = trend.rolling(117, min_periods=max(117//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(513, min_periods=max(513//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.8775 + 9.71e-05 * anchor
    return base_signal.diff()

def f02_adv_371_jerk_v371_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=25, w2=128, w3=526, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 25)
    slow = _rolling_slope(x, 128)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.891875 + 9.72e-05 * anchor
    return base_signal.diff()

def f02_adv_372_accel_v372_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=32, w2=139, w3=539, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(139, min_periods=max(139//3, 2)).max()
    trough = x.rolling(32, min_periods=max(32//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.90625 + 9.73e-05 * anchor
    return base_signal.diff()

def f02_adv_373_jerk_v373_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=39, w2=150, w3=552, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(39)
    rank = change.rolling(150, min_periods=max(150//3, 2)).rank(pct=True)
    persistence = change.rolling(552, min_periods=max(552//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2782 * persistence + 9.74e-05 * anchor
    return base_signal.diff()

def f02_adv_374_accel_v374_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=46, w2=161, w3=565, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(46, min_periods=max(46//3, 2)).std()
    vol_slow = ret.rolling(161, min_periods=max(161//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.935 + 9.75e-05 * anchor
    return base_signal.diff()

def f02_adv_375_jerk_v375_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=53, w2=172, w3=578, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(172, min_periods=max(172//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 53)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2934 * slope + 9.76e-05 * anchor
    return base_signal.diff()
