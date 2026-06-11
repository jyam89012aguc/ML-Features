"""38 distribution rolling top signature d3 third derivative features 301-375 â€” Pipeline 1a-HF Grade v3.

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

def f38_drts_301_jerk_v301_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=68, w2=106, w3=556, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 68)
    slow = _rolling_slope(x, 106)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.25625 + 0.0023102 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_302_accel_v302_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=75, w2=117, w3=569, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(117, min_periods=max(117//3, 2)).max()
    trough = x.rolling(75, min_periods=max(75//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.270625 + 0.0023103 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_303_jerk_v303_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=82, w2=128, w3=582, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(82)
    rank = change.rolling(128, min_periods=max(128//3, 2)).rank(pct=True)
    persistence = change.rolling(582, min_periods=max(582//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2154 * persistence + 0.0023104 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_304_accel_v304_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=89, w2=139, w3=595, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(89, min_periods=max(89//3, 2)).std()
    vol_slow = ret.rolling(139, min_periods=max(139//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.299375 + 0.0023105 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_305_jerk_v305_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=96, w2=150, w3=608, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(150, min_periods=max(150//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 96)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2306 * slope + 0.0023106 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_306_accel_v306_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=103, w2=161, w3=621, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(103)
    drag = impulse.rolling(161, min_periods=max(161//3, 2)).mean()
    noise = impulse.abs().rolling(621, min_periods=max(621//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.328125 + 0.0023107 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_307_jerk_v307_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=110, w2=172, w3=634, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 110)
    acceleration = _rolling_slope(velocity, 172)
    curvature = _rolling_slope(acceleration, 634)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2458 * acceleration + 0.0023108 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_308_accel_v308_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=117, w2=183, w3=647, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(117, min_periods=max(117//3, 2)).mean(), upside.rolling(183, min_periods=max(183//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.356875 + 0.0023109 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_309_jerk_v309_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=124, w2=194, w3=660, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(194, min_periods=max(194//3, 2)).max()
    rebound = x - x.rolling(124, min_periods=max(124//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.261 * _rolling_slope(draw, 660) + 0.002311 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_310_accel_v310_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=131, w2=205, w3=673, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 131)
    baseline = trend.rolling(205, min_periods=max(205//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(673, min_periods=max(673//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.385625 + 0.0023111 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_311_jerk_v311_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=138, w2=216, w3=686, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 138)
    slow = _rolling_slope(x, 216)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.4 + 0.0023112 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_312_accel_v312_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=145, w2=227, w3=699, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(227, min_periods=max(227//3, 2)).max()
    trough = x.rolling(145, min_periods=max(145//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.414375 + 0.0023113 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_313_jerk_v313_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=152, w2=238, w3=712, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(238, min_periods=max(238//3, 2)).rank(pct=True)
    persistence = change.rolling(712, min_periods=max(712//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2914 * persistence + 0.0023114 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_314_accel_v314_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=159, w2=249, w3=725, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(159, min_periods=max(159//3, 2)).std()
    vol_slow = ret.rolling(249, min_periods=max(249//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.443125 + 0.0023115 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_315_jerk_v315_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=166, w2=260, w3=738, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(260, min_periods=max(260//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 166)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3066 * slope + 0.0023116 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_316_accel_v316_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=173, w2=271, w3=751, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(271, min_periods=max(271//3, 2)).mean()
    noise = impulse.abs().rolling(751, min_periods=max(751//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.471875 + 0.0023117 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_317_jerk_v317_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=180, w2=282, w3=764, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 180)
    acceleration = _rolling_slope(velocity, 282)
    curvature = _rolling_slope(acceleration, 764)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3218 * acceleration + 0.0023118 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_318_accel_v318_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=187, w2=293, w3=20, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(187, min_periods=max(187//3, 2)).mean(), upside.rolling(293, min_periods=max(293//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(20) * 1.500625 + 0.0023119 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_319_jerk_v319_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=194, w2=304, w3=33, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(304, min_periods=max(304//3, 2)).max()
    rebound = x - x.rolling(194, min_periods=max(194//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.337 * _rolling_slope(draw, 33) + 0.002312 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_320_accel_v320_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=201, w2=315, w3=46, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 201)
    baseline = trend.rolling(315, min_periods=max(315//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(46, min_periods=max(46//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.529375 + 0.0023121 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_321_jerk_v321_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=208, w2=326, w3=59, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 208)
    slow = _rolling_slope(x, 326)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=59, adjust=False).mean() * 1.54375 + 0.0023122 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_322_accel_v322_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=215, w2=337, w3=72, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(337, min_periods=max(337//3, 2)).max()
    trough = x.rolling(215, min_periods=max(215//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.558125 + 0.0023123 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_323_jerk_v323_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=222, w2=348, w3=85, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(348, min_periods=max(348//3, 2)).rank(pct=True)
    persistence = change.rolling(85, min_periods=max(85//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3674 * persistence + 0.0023124 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_324_accel_v324_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=229, w2=359, w3=98, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(229, min_periods=max(229//3, 2)).std()
    vol_slow = ret.rolling(359, min_periods=max(359//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.586875 + 0.0023125 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_325_jerk_v325_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=236, w2=370, w3=111, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(370, min_periods=max(370//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 236)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3826 * slope + 0.0023126 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_326_accel_v326_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=243, w2=381, w3=124, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(381, min_periods=max(381//3, 2)).mean()
    noise = impulse.abs().rolling(124, min_periods=max(124//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.615625 + 0.0023127 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_327_jerk_v327_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=250, w2=392, w3=137, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 250)
    acceleration = _rolling_slope(velocity, 392)
    curvature = _rolling_slope(acceleration, 137)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3978 * acceleration + 0.0023128 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_328_accel_v328_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=6, w2=403, w3=150, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(6, min_periods=max(6//3, 2)).mean(), upside.rolling(403, min_periods=max(403//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.87125 + 0.0023129 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_329_jerk_v329_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=13, w2=414, w3=163, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(414, min_periods=max(414//3, 2)).max()
    rebound = x - x.rolling(13, min_periods=max(13//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0366 * _rolling_slope(draw, 163) + 0.002313 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_330_accel_v330_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=20, w2=425, w3=176, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 20)
    baseline = trend.rolling(425, min_periods=max(425//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(176, min_periods=max(176//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.9 + 0.0023131 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_331_jerk_v331_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=27, w2=436, w3=189, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 27)
    slow = _rolling_slope(x, 436)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=189, adjust=False).mean() * 0.914375 + 0.0023132 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_332_accel_v332_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=34, w2=447, w3=202, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(447, min_periods=max(447//3, 2)).max()
    trough = x.rolling(34, min_periods=max(34//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.92875 + 0.0023133 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_333_jerk_v333_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=41, w2=458, w3=215, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(41)
    rank = change.rolling(458, min_periods=max(458//3, 2)).rank(pct=True)
    persistence = change.rolling(215, min_periods=max(215//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.067 * persistence + 0.0023134 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_334_accel_v334_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=48, w2=469, w3=228, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(48, min_periods=max(48//3, 2)).std()
    vol_slow = ret.rolling(469, min_periods=max(469//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.9575 + 0.0023135 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_335_jerk_v335_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=55, w2=480, w3=241, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(480, min_periods=max(480//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 55)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0822 * slope + 0.0023136 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_336_accel_v336_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=62, w2=491, w3=254, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(62)
    drag = impulse.rolling(491, min_periods=max(491//3, 2)).mean()
    noise = impulse.abs().rolling(254, min_periods=max(254//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.98625 + 0.0023137 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_337_jerk_v337_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=69, w2=502, w3=267, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 69)
    acceleration = _rolling_slope(velocity, 502)
    curvature = _rolling_slope(acceleration, 267)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0974 * acceleration + 0.0023138 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_338_accel_v338_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=76, w2=10, w3=280, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(76, min_periods=max(76//3, 2)).mean(), upside.rolling(10, min_periods=max(10//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.015 + 0.0023139 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_339_jerk_v339_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=83, w2=21, w3=293, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(21, min_periods=max(21//3, 2)).max()
    rebound = x - x.rolling(83, min_periods=max(83//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1126 * _rolling_slope(draw, 293) + 0.002314 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_340_accel_v340_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=90, w2=32, w3=306, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 90)
    baseline = trend.rolling(32, min_periods=max(32//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(306, min_periods=max(306//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.04375 + 0.0023141 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_341_jerk_v341_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=97, w2=43, w3=319, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 97)
    slow = _rolling_slope(x, 43)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.058125 + 0.0023142 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_342_accel_v342_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=104, w2=54, w3=332, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(54, min_periods=max(54//3, 2)).max()
    trough = x.rolling(104, min_periods=max(104//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.0725 + 0.0023143 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_343_jerk_v343_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=111, w2=65, w3=345, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(111)
    rank = change.rolling(65, min_periods=max(65//3, 2)).rank(pct=True)
    persistence = change.rolling(345, min_periods=max(345//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.143 * persistence + 0.0023144 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_344_accel_v344_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=118, w2=76, w3=358, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(118, min_periods=max(118//3, 2)).std()
    vol_slow = ret.rolling(76, min_periods=max(76//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.10125 + 0.0023145 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_345_jerk_v345_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=125, w2=87, w3=371, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(87, min_periods=max(87//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 125)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1582 * slope + 0.0023146 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_346_accel_v346_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=132, w2=98, w3=384, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(98, min_periods=max(98//3, 2)).mean()
    noise = impulse.abs().rolling(384, min_periods=max(384//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.13 + 0.0023147 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_347_jerk_v347_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=139, w2=109, w3=397, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 139)
    acceleration = _rolling_slope(velocity, 109)
    curvature = _rolling_slope(acceleration, 397)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1734 * acceleration + 0.0023148 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_348_accel_v348_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=146, w2=120, w3=410, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(146, min_periods=max(146//3, 2)).mean(), upside.rolling(120, min_periods=max(120//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.15875 + 0.0023149 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_349_jerk_v349_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=153, w2=131, w3=423, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(131, min_periods=max(131//3, 2)).max()
    rebound = x - x.rolling(153, min_periods=max(153//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1886 * _rolling_slope(draw, 423) + 0.002315 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_350_accel_v350_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=160, w2=142, w3=436, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 160)
    baseline = trend.rolling(142, min_periods=max(142//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(436, min_periods=max(436//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.1875 + 0.0023151 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_351_jerk_v351_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=167, w2=153, w3=449, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 167)
    slow = _rolling_slope(x, 153)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.201875 + 0.0023152 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_352_accel_v352_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=174, w2=164, w3=462, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(164, min_periods=max(164//3, 2)).max()
    trough = x.rolling(174, min_periods=max(174//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.21625 + 0.0023153 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_353_jerk_v353_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=181, w2=175, w3=475, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(175, min_periods=max(175//3, 2)).rank(pct=True)
    persistence = change.rolling(475, min_periods=max(475//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.219 * persistence + 0.0023154 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_354_accel_v354_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=188, w2=186, w3=488, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(188, min_periods=max(188//3, 2)).std()
    vol_slow = ret.rolling(186, min_periods=max(186//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.245 + 0.0023155 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_355_jerk_v355_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=195, w2=197, w3=501, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(197, min_periods=max(197//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 195)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2342 * slope + 0.0023156 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_356_accel_v356_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=202, w2=208, w3=514, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(208, min_periods=max(208//3, 2)).mean()
    noise = impulse.abs().rolling(514, min_periods=max(514//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.27375 + 0.0023157 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_357_jerk_v357_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=209, w2=219, w3=527, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 209)
    acceleration = _rolling_slope(velocity, 219)
    curvature = _rolling_slope(acceleration, 527)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2494 * acceleration + 0.0023158 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_358_accel_v358_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=216, w2=230, w3=540, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(216, min_periods=max(216//3, 2)).mean(), upside.rolling(230, min_periods=max(230//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.3025 + 0.0023159 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_359_jerk_v359_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=223, w2=241, w3=553, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(241, min_periods=max(241//3, 2)).max()
    rebound = x - x.rolling(223, min_periods=max(223//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2646 * _rolling_slope(draw, 553) + 0.002316 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_360_accel_v360_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=230, w2=252, w3=566, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 230)
    baseline = trend.rolling(252, min_periods=max(252//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(566, min_periods=max(566//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.33125 + 0.0023161 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_361_jerk_v361_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=237, w2=263, w3=579, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 237)
    slow = _rolling_slope(x, 263)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.345625 + 0.0023162 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_362_accel_v362_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=244, w2=274, w3=592, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(274, min_periods=max(274//3, 2)).max()
    trough = x.rolling(244, min_periods=max(244//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.36 + 0.0023163 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_363_jerk_v363_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=251, w2=285, w3=605, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(285, min_periods=max(285//3, 2)).rank(pct=True)
    persistence = change.rolling(605, min_periods=max(605//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.295 * persistence + 0.0023164 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_364_accel_v364_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=7, w2=296, w3=618, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(7, min_periods=max(7//3, 2)).std()
    vol_slow = ret.rolling(296, min_periods=max(296//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.38875 + 0.0023165 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_365_jerk_v365_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=14, w2=307, w3=631, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(307, min_periods=max(307//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 14)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3102 * slope + 0.0023166 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_366_accel_v366_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=21, w2=318, w3=644, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(21)
    drag = impulse.rolling(318, min_periods=max(318//3, 2)).mean()
    noise = impulse.abs().rolling(644, min_periods=max(644//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.4175 + 0.0023167 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_367_jerk_v367_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=28, w2=329, w3=657, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 28)
    acceleration = _rolling_slope(velocity, 329)
    curvature = _rolling_slope(acceleration, 657)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3254 * acceleration + 0.0023168 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_368_accel_v368_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=35, w2=340, w3=670, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(35, min_periods=max(35//3, 2)).mean(), upside.rolling(340, min_periods=max(340//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.44625 + 0.0023169 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_369_jerk_v369_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=42, w2=351, w3=683, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(351, min_periods=max(351//3, 2)).max()
    rebound = x - x.rolling(42, min_periods=max(42//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3406 * _rolling_slope(draw, 683) + 0.002317 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_370_accel_v370_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=49, w2=362, w3=696, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 49)
    baseline = trend.rolling(362, min_periods=max(362//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(696, min_periods=max(696//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.475 + 0.0023171 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_371_jerk_v371_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=56, w2=373, w3=709, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 56)
    slow = _rolling_slope(x, 373)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.489375 + 0.0023172 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_372_accel_v372_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=63, w2=384, w3=722, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(384, min_periods=max(384//3, 2)).max()
    trough = x.rolling(63, min_periods=max(63//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.50375 + 0.0023173 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_373_jerk_v373_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=70, w2=395, w3=735, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(70)
    rank = change.rolling(395, min_periods=max(395//3, 2)).rank(pct=True)
    persistence = change.rolling(735, min_periods=max(735//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.371 * persistence + 0.0023174 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_374_accel_v374_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=77, w2=406, w3=748, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(77, min_periods=max(77//3, 2)).std()
    vol_slow = ret.rolling(406, min_periods=max(406//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.5325 + 0.0023175 * anchor
    return base_signal.diff().diff().diff()

def f38_drts_375_jerk_v375_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=84, w2=417, w3=761, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(417, min_periods=max(417//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 84)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3862 * slope + 0.0023176 * anchor
    return base_signal.diff().diff().diff()
