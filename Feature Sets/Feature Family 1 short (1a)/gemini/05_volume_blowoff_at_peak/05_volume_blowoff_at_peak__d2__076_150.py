"""05 volume blowoff at peak d2 second derivative features 76-150 â€” Pipeline 1a-HF Grade v3.

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

def f05_vbp_076_accel_v76_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=18, w2=84, w3=409, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(18)
    drag = impulse.rolling(84, min_periods=max(84//3, 2)).mean()
    noise = impulse.abs().rolling(409, min_periods=max(409//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.87875 + 0.0002477 * anchor
    return base_signal.diff().diff()

def f05_vbp_077_jerk_v77_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=25, w2=95, w3=422, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 25)
    acceleration = _rolling_slope(velocity, 95)
    curvature = _rolling_slope(acceleration, 422)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0402 * acceleration + 0.0002478 * anchor
    return base_signal.diff().diff()

def f05_vbp_078_accel_v78_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=32, w2=106, w3=435, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(32, min_periods=max(32//3, 2)).mean(), upside.rolling(106, min_periods=max(106//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.9075 + 0.0002479 * anchor
    return base_signal.diff().diff()

def f05_vbp_079_jerk_v79_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=39, w2=117, w3=448, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(117, min_periods=max(117//3, 2)).max()
    rebound = x - x.rolling(39, min_periods=max(39//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0554 * _rolling_slope(draw, 448) + 0.000248 * anchor
    return base_signal.diff().diff()

def f05_vbp_080_accel_v80_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=46, w2=128, w3=461, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 46)
    baseline = trend.rolling(128, min_periods=max(128//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(461, min_periods=max(461//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.93625 + 0.0002481 * anchor
    return base_signal.diff().diff()

def f05_vbp_081_jerk_v81_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=53, w2=139, w3=474, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 53)
    slow = _rolling_slope(x, 139)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.950625 + 0.0002482 * anchor
    return base_signal.diff().diff()

def f05_vbp_082_accel_v82_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=60, w2=150, w3=487, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(150, min_periods=max(150//3, 2)).max()
    trough = x.rolling(60, min_periods=max(60//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.965 + 0.0002483 * anchor
    return base_signal.diff().diff()

def f05_vbp_083_jerk_v83_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=67, w2=161, w3=500, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(67)
    rank = change.rolling(161, min_periods=max(161//3, 2)).rank(pct=True)
    persistence = change.rolling(500, min_periods=max(500//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0858 * persistence + 0.0002484 * anchor
    return base_signal.diff().diff()

def f05_vbp_084_accel_v84_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=74, w2=172, w3=513, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(74, min_periods=max(74//3, 2)).std()
    vol_slow = ret.rolling(172, min_periods=max(172//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.99375 + 0.0002485 * anchor
    return base_signal.diff().diff()

def f05_vbp_085_jerk_v85_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=81, w2=183, w3=526, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(183, min_periods=max(183//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 81)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.101 * slope + 0.0002486 * anchor
    return base_signal.diff().diff()

def f05_vbp_086_accel_v86_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=88, w2=194, w3=539, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(88)
    drag = impulse.rolling(194, min_periods=max(194//3, 2)).mean()
    noise = impulse.abs().rolling(539, min_periods=max(539//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.0225 + 0.0002487 * anchor
    return base_signal.diff().diff()

def f05_vbp_087_jerk_v87_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=95, w2=205, w3=552, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 95)
    acceleration = _rolling_slope(velocity, 205)
    curvature = _rolling_slope(acceleration, 552)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1162 * acceleration + 0.0002488 * anchor
    return base_signal.diff().diff()

def f05_vbp_088_accel_v88_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=102, w2=216, w3=565, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(102, min_periods=max(102//3, 2)).mean(), upside.rolling(216, min_periods=max(216//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.05125 + 0.0002489 * anchor
    return base_signal.diff().diff()

def f05_vbp_089_jerk_v89_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=109, w2=227, w3=578, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(227, min_periods=max(227//3, 2)).max()
    rebound = x - x.rolling(109, min_periods=max(109//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1314 * _rolling_slope(draw, 578) + 0.000249 * anchor
    return base_signal.diff().diff()

def f05_vbp_090_accel_v90_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=116, w2=238, w3=591, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 116)
    baseline = trend.rolling(238, min_periods=max(238//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(591, min_periods=max(591//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.08 + 0.0002491 * anchor
    return base_signal.diff().diff()

def f05_vbp_091_jerk_v91_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=123, w2=249, w3=604, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 123)
    slow = _rolling_slope(x, 249)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.094375 + 0.0002492 * anchor
    return base_signal.diff().diff()

def f05_vbp_092_accel_v92_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=130, w2=260, w3=617, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(260, min_periods=max(260//3, 2)).max()
    trough = x.rolling(130, min_periods=max(130//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.10875 + 0.0002493 * anchor
    return base_signal.diff().diff()

def f05_vbp_093_jerk_v93_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=137, w2=271, w3=630, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(271, min_periods=max(271//3, 2)).rank(pct=True)
    persistence = change.rolling(630, min_periods=max(630//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1618 * persistence + 0.0002494 * anchor
    return base_signal.diff().diff()

def f05_vbp_094_accel_v94_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=144, w2=282, w3=643, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(144, min_periods=max(144//3, 2)).std()
    vol_slow = ret.rolling(282, min_periods=max(282//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.1375 + 0.0002495 * anchor
    return base_signal.diff().diff()

def f05_vbp_095_jerk_v95_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=151, w2=293, w3=656, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(293, min_periods=max(293//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 151)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.177 * slope + 0.0002496 * anchor
    return base_signal.diff().diff()

def f05_vbp_096_accel_v96_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=158, w2=304, w3=669, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(304, min_periods=max(304//3, 2)).mean()
    noise = impulse.abs().rolling(669, min_periods=max(669//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.16625 + 0.0002497 * anchor
    return base_signal.diff().diff()

def f05_vbp_097_jerk_v97_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=165, w2=315, w3=682, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 165)
    acceleration = _rolling_slope(velocity, 315)
    curvature = _rolling_slope(acceleration, 682)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1922 * acceleration + 0.0002498 * anchor
    return base_signal.diff().diff()

def f05_vbp_098_accel_v98_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=172, w2=326, w3=695, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(172, min_periods=max(172//3, 2)).mean(), upside.rolling(326, min_periods=max(326//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.195 + 0.0002499 * anchor
    return base_signal.diff().diff()

def f05_vbp_099_jerk_v99_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=179, w2=337, w3=708, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(337, min_periods=max(337//3, 2)).max()
    rebound = x - x.rolling(179, min_periods=max(179//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2074 * _rolling_slope(draw, 708) + 0.00025 * anchor
    return base_signal.diff().diff()

def f05_vbp_100_accel_v100_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=186, w2=348, w3=721, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 186)
    baseline = trend.rolling(348, min_periods=max(348//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(721, min_periods=max(721//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.22375 + 0.0002501 * anchor
    return base_signal.diff().diff()

def f05_vbp_101_jerk_v101_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=193, w2=359, w3=734, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 193)
    slow = _rolling_slope(x, 359)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.238125 + 0.0002502 * anchor
    return base_signal.diff().diff()

def f05_vbp_102_accel_v102_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=200, w2=370, w3=747, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(370, min_periods=max(370//3, 2)).max()
    trough = x.rolling(200, min_periods=max(200//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.2525 + 0.0002503 * anchor
    return base_signal.diff().diff()

def f05_vbp_103_jerk_v103_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=207, w2=381, w3=760, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(381, min_periods=max(381//3, 2)).rank(pct=True)
    persistence = change.rolling(760, min_periods=max(760//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2378 * persistence + 0.0002504 * anchor
    return base_signal.diff().diff()

def f05_vbp_104_accel_v104_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=214, w2=392, w3=16, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(214, min_periods=max(214//3, 2)).std()
    vol_slow = ret.rolling(392, min_periods=max(392//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.28125 + 0.0002505 * anchor
    return base_signal.diff().diff()

def f05_vbp_105_jerk_v105_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=221, w2=403, w3=29, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(403, min_periods=max(403//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 221)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.253 * slope + 0.0002506 * anchor
    return base_signal.diff().diff()

def f05_vbp_106_accel_v106_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=228, w2=414, w3=42, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(414, min_periods=max(414//3, 2)).mean()
    noise = impulse.abs().rolling(42, min_periods=max(42//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.31 + 0.0002507 * anchor
    return base_signal.diff().diff()

def f05_vbp_107_jerk_v107_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=235, w2=425, w3=55, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 235)
    acceleration = _rolling_slope(velocity, 425)
    curvature = _rolling_slope(acceleration, 55)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2682 * acceleration + 0.0002508 * anchor
    return base_signal.diff().diff()

def f05_vbp_108_accel_v108_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=242, w2=436, w3=68, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(242, min_periods=max(242//3, 2)).mean(), upside.rolling(436, min_periods=max(436//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(68) * 1.33875 + 0.0002509 * anchor
    return base_signal.diff().diff()

def f05_vbp_109_jerk_v109_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=249, w2=447, w3=81, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(447, min_periods=max(447//3, 2)).max()
    rebound = x - x.rolling(249, min_periods=max(249//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2834 * _rolling_slope(draw, 81) + 0.000251 * anchor
    return base_signal.diff().diff()

def f05_vbp_110_accel_v110_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=5, w2=458, w3=94, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 5)
    baseline = trend.rolling(458, min_periods=max(458//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(94, min_periods=max(94//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.3675 + 0.0002511 * anchor
    return base_signal.diff().diff()

def f05_vbp_111_jerk_v111_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=12, w2=469, w3=107, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 12)
    slow = _rolling_slope(x, 469)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=107, adjust=False).mean() * 1.381875 + 0.0002512 * anchor
    return base_signal.diff().diff()

def f05_vbp_112_accel_v112_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=19, w2=480, w3=120, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(480, min_periods=max(480//3, 2)).max()
    trough = x.rolling(19, min_periods=max(19//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.39625 + 0.0002513 * anchor
    return base_signal.diff().diff()

def f05_vbp_113_jerk_v113_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=26, w2=491, w3=133, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(26)
    rank = change.rolling(491, min_periods=max(491//3, 2)).rank(pct=True)
    persistence = change.rolling(133, min_periods=max(133//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3138 * persistence + 0.0002514 * anchor
    return base_signal.diff().diff()

def f05_vbp_114_accel_v114_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=33, w2=502, w3=146, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(33, min_periods=max(33//3, 2)).std()
    vol_slow = ret.rolling(502, min_periods=max(502//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.425 + 0.0002515 * anchor
    return base_signal.diff().diff()

def f05_vbp_115_jerk_v115_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=40, w2=10, w3=159, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(10, min_periods=max(10//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 40)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.329 * slope + 0.0002516 * anchor
    return base_signal.diff().diff()

def f05_vbp_116_accel_v116_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=47, w2=21, w3=172, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(47)
    drag = impulse.rolling(21, min_periods=max(21//3, 2)).mean()
    noise = impulse.abs().rolling(172, min_periods=max(172//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.45375 + 0.0002517 * anchor
    return base_signal.diff().diff()

def f05_vbp_117_jerk_v117_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=54, w2=32, w3=185, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 54)
    acceleration = _rolling_slope(velocity, 32)
    curvature = _rolling_slope(acceleration, 185)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3442 * acceleration + 0.0002518 * anchor
    return base_signal.diff().diff()

def f05_vbp_118_accel_v118_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=61, w2=43, w3=198, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(61, min_periods=max(61//3, 2)).mean(), upside.rolling(43, min_periods=max(43//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.4825 + 0.0002519 * anchor
    return base_signal.diff().diff()

def f05_vbp_119_jerk_v119_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=68, w2=54, w3=211, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(54, min_periods=max(54//3, 2)).max()
    rebound = x - x.rolling(68, min_periods=max(68//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3594 * _rolling_slope(draw, 211) + 0.000252 * anchor
    return base_signal.diff().diff()

def f05_vbp_120_accel_v120_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=75, w2=65, w3=224, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 75)
    baseline = trend.rolling(65, min_periods=max(65//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(224, min_periods=max(224//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.51125 + 0.0002521 * anchor
    return base_signal.diff().diff()

def f05_vbp_121_jerk_v121_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=82, w2=76, w3=237, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 82)
    slow = _rolling_slope(x, 76)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=237, adjust=False).mean() * 1.525625 + 0.0002522 * anchor
    return base_signal.diff().diff()

def f05_vbp_122_accel_v122_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=89, w2=87, w3=250, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(87, min_periods=max(87//3, 2)).max()
    trough = x.rolling(89, min_periods=max(89//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.54 + 0.0002523 * anchor
    return base_signal.diff().diff()

def f05_vbp_123_jerk_v123_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=96, w2=98, w3=263, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(96)
    rank = change.rolling(98, min_periods=max(98//3, 2)).rank(pct=True)
    persistence = change.rolling(263, min_periods=max(263//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3898 * persistence + 0.0002524 * anchor
    return base_signal.diff().diff()

def f05_vbp_124_accel_v124_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=103, w2=109, w3=276, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(103, min_periods=max(103//3, 2)).std()
    vol_slow = ret.rolling(109, min_periods=max(109//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.56875 + 0.0002525 * anchor
    return base_signal.diff().diff()

def f05_vbp_125_jerk_v125_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=110, w2=120, w3=289, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(120, min_periods=max(120//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 110)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.405 * slope + 0.0002526 * anchor
    return base_signal.diff().diff()

def f05_vbp_126_accel_v126_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=117, w2=131, w3=302, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(117)
    drag = impulse.rolling(131, min_periods=max(131//3, 2)).mean()
    noise = impulse.abs().rolling(302, min_periods=max(302//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.5975 + 0.0002527 * anchor
    return base_signal.diff().diff()

def f05_vbp_127_jerk_v127_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=124, w2=142, w3=315, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 124)
    acceleration = _rolling_slope(velocity, 142)
    curvature = _rolling_slope(acceleration, 315)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0438 * acceleration + 0.0002528 * anchor
    return base_signal.diff().diff()

def f05_vbp_128_accel_v128_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=131, w2=153, w3=328, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(131, min_periods=max(131//3, 2)).mean(), upside.rolling(153, min_periods=max(153//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.853125 + 0.0002529 * anchor
    return base_signal.diff().diff()

def f05_vbp_129_jerk_v129_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=138, w2=164, w3=341, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(164, min_periods=max(164//3, 2)).max()
    rebound = x - x.rolling(138, min_periods=max(138//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.059 * _rolling_slope(draw, 341) + 0.000253 * anchor
    return base_signal.diff().diff()

def f05_vbp_130_accel_v130_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=145, w2=175, w3=354, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 145)
    baseline = trend.rolling(175, min_periods=max(175//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(354, min_periods=max(354//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.881875 + 0.0002531 * anchor
    return base_signal.diff().diff()

def f05_vbp_131_jerk_v131_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=152, w2=186, w3=367, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 152)
    slow = _rolling_slope(x, 186)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.89625 + 0.0002532 * anchor
    return base_signal.diff().diff()

def f05_vbp_132_accel_v132_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=159, w2=197, w3=380, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(197, min_periods=max(197//3, 2)).max()
    trough = x.rolling(159, min_periods=max(159//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.910625 + 0.0002533 * anchor
    return base_signal.diff().diff()

def f05_vbp_133_jerk_v133_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=166, w2=208, w3=393, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(208, min_periods=max(208//3, 2)).rank(pct=True)
    persistence = change.rolling(393, min_periods=max(393//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0894 * persistence + 0.0002534 * anchor
    return base_signal.diff().diff()

def f05_vbp_134_accel_v134_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=173, w2=219, w3=406, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(173, min_periods=max(173//3, 2)).std()
    vol_slow = ret.rolling(219, min_periods=max(219//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.939375 + 0.0002535 * anchor
    return base_signal.diff().diff()

def f05_vbp_135_jerk_v135_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=180, w2=230, w3=419, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(230, min_periods=max(230//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 180)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1046 * slope + 0.0002536 * anchor
    return base_signal.diff().diff()

def f05_vbp_136_accel_v136_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=187, w2=241, w3=432, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(241, min_periods=max(241//3, 2)).mean()
    noise = impulse.abs().rolling(432, min_periods=max(432//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.968125 + 0.0002537 * anchor
    return base_signal.diff().diff()

def f05_vbp_137_jerk_v137_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=194, w2=252, w3=445, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 194)
    acceleration = _rolling_slope(velocity, 252)
    curvature = _rolling_slope(acceleration, 445)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1198 * acceleration + 0.0002538 * anchor
    return base_signal.diff().diff()

def f05_vbp_138_accel_v138_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=201, w2=263, w3=458, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(201, min_periods=max(201//3, 2)).mean(), upside.rolling(263, min_periods=max(263//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.996875 + 0.0002539 * anchor
    return base_signal.diff().diff()

def f05_vbp_139_jerk_v139_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=208, w2=274, w3=471, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(274, min_periods=max(274//3, 2)).max()
    rebound = x - x.rolling(208, min_periods=max(208//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.135 * _rolling_slope(draw, 471) + 0.000254 * anchor
    return base_signal.diff().diff()

def f05_vbp_140_accel_v140_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=215, w2=285, w3=484, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 215)
    baseline = trend.rolling(285, min_periods=max(285//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(484, min_periods=max(484//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.025625 + 0.0002541 * anchor
    return base_signal.diff().diff()

def f05_vbp_141_jerk_v141_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=222, w2=296, w3=497, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 222)
    slow = _rolling_slope(x, 296)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.04 + 0.0002542 * anchor
    return base_signal.diff().diff()

def f05_vbp_142_accel_v142_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=229, w2=307, w3=510, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(307, min_periods=max(307//3, 2)).max()
    trough = x.rolling(229, min_periods=max(229//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.054375 + 0.0002543 * anchor
    return base_signal.diff().diff()

def f05_vbp_143_jerk_v143_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=236, w2=318, w3=523, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(318, min_periods=max(318//3, 2)).rank(pct=True)
    persistence = change.rolling(523, min_periods=max(523//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1654 * persistence + 0.0002544 * anchor
    return base_signal.diff().diff()

def f05_vbp_144_accel_v144_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=243, w2=329, w3=536, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(243, min_periods=max(243//3, 2)).std()
    vol_slow = ret.rolling(329, min_periods=max(329//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.083125 + 0.0002545 * anchor
    return base_signal.diff().diff()

def f05_vbp_145_jerk_v145_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=250, w2=340, w3=549, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(340, min_periods=max(340//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 250)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1806 * slope + 0.0002546 * anchor
    return base_signal.diff().diff()

def f05_vbp_146_accel_v146_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=6, w2=351, w3=562, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(6)
    drag = impulse.rolling(351, min_periods=max(351//3, 2)).mean()
    noise = impulse.abs().rolling(562, min_periods=max(562//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.111875 + 0.0002547 * anchor
    return base_signal.diff().diff()

def f05_vbp_147_jerk_v147_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=13, w2=362, w3=575, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 13)
    acceleration = _rolling_slope(velocity, 362)
    curvature = _rolling_slope(acceleration, 575)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1958 * acceleration + 0.0002548 * anchor
    return base_signal.diff().diff()

def f05_vbp_148_accel_v148_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=20, w2=373, w3=588, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(20, min_periods=max(20//3, 2)).mean(), upside.rolling(373, min_periods=max(373//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.140625 + 0.0002549 * anchor
    return base_signal.diff().diff()

def f05_vbp_149_jerk_v149_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=27, w2=384, w3=601, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(384, min_periods=max(384//3, 2)).max()
    rebound = x - x.rolling(27, min_periods=max(27//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.211 * _rolling_slope(draw, 601) + 0.000255 * anchor
    return base_signal.diff().diff()

def f05_vbp_150_accel_v150_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=34, w2=395, w3=614, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 34)
    baseline = trend.rolling(395, min_periods=max(395//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(614, min_periods=max(614//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.169375 + 0.0002551 * anchor
    return base_signal.diff().diff()
