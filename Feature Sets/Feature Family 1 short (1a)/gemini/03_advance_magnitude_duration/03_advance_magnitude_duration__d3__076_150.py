"""03 advance magnitude duration d3 third derivative features 76-150 â€” Pipeline 1a-HF Grade v3.

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

def f03_amd_076_accel_v76_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=152, w2=465, w3=706, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(465, min_periods=max(465//3, 2)).mean()
    noise = impulse.abs().rolling(706, min_periods=max(706//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.410625 + 0.0001277 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_077_jerk_v77_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=159, w2=476, w3=719, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 159)
    acceleration = _rolling_slope(velocity, 476)
    curvature = _rolling_slope(acceleration, 719)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3302 * acceleration + 0.0001278 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_078_accel_v78_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=166, w2=487, w3=732, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(166, min_periods=max(166//3, 2)).mean(), upside.rolling(487, min_periods=max(487//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.439375 + 0.0001279 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_079_jerk_v79_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=173, w2=498, w3=745, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(498, min_periods=max(498//3, 2)).max()
    rebound = x - x.rolling(173, min_periods=max(173//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3454 * _rolling_slope(draw, 745) + 0.000128 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_080_accel_v80_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=180, w2=509, w3=758, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 180)
    baseline = trend.rolling(509, min_periods=max(509//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(758, min_periods=max(758//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.468125 + 0.0001281 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_081_jerk_v81_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=187, w2=17, w3=771, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 187)
    slow = _rolling_slope(x, 17)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.4825 + 0.0001282 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_082_accel_v82_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=194, w2=28, w3=27, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(28, min_periods=max(28//3, 2)).max()
    trough = x.rolling(194, min_periods=max(194//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.496875 + 0.0001283 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_083_jerk_v83_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=201, w2=39, w3=40, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(39, min_periods=max(39//3, 2)).rank(pct=True)
    persistence = change.rolling(40, min_periods=max(40//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3758 * persistence + 0.0001284 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_084_accel_v84_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=208, w2=50, w3=53, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(208, min_periods=max(208//3, 2)).std()
    vol_slow = ret.rolling(50, min_periods=max(50//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.525625 + 0.0001285 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_085_jerk_v85_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=215, w2=61, w3=66, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(61, min_periods=max(61//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 215)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.391 * slope + 0.0001286 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_086_accel_v86_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=222, w2=72, w3=79, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(72, min_periods=max(72//3, 2)).mean()
    noise = impulse.abs().rolling(79, min_periods=max(79//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.554375 + 0.0001287 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_087_jerk_v87_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=229, w2=83, w3=92, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 229)
    acceleration = _rolling_slope(velocity, 83)
    curvature = _rolling_slope(acceleration, 92)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.4062 * acceleration + 0.0001288 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_088_accel_v88_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=236, w2=94, w3=105, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(236, min_periods=max(236//3, 2)).mean(), upside.rolling(94, min_periods=max(94//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(105) * 1.583125 + 0.0001289 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_089_jerk_v89_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=243, w2=105, w3=118, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(105, min_periods=max(105//3, 2)).max()
    rebound = x - x.rolling(243, min_periods=max(243//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.045 * _rolling_slope(draw, 118) + 0.000129 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_090_accel_v90_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=250, w2=116, w3=131, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 250)
    baseline = trend.rolling(116, min_periods=max(116//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(131, min_periods=max(131//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.611875 + 0.0001291 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_091_jerk_v91_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=6, w2=127, w3=144, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 6)
    slow = _rolling_slope(x, 127)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=144, adjust=False).mean() * 0.853125 + 0.0001292 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_092_accel_v92_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=13, w2=138, w3=157, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(138, min_periods=max(138//3, 2)).max()
    trough = x.rolling(13, min_periods=max(13//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.8675 + 0.0001293 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_093_jerk_v93_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=20, w2=149, w3=170, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(20)
    rank = change.rolling(149, min_periods=max(149//3, 2)).rank(pct=True)
    persistence = change.rolling(170, min_periods=max(170//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0754 * persistence + 0.0001294 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_094_accel_v94_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=27, w2=160, w3=183, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(27, min_periods=max(27//3, 2)).std()
    vol_slow = ret.rolling(160, min_periods=max(160//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.89625 + 0.0001295 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_095_jerk_v95_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=34, w2=171, w3=196, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(171, min_periods=max(171//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 34)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0906 * slope + 0.0001296 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_096_accel_v96_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=41, w2=182, w3=209, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(41)
    drag = impulse.rolling(182, min_periods=max(182//3, 2)).mean()
    noise = impulse.abs().rolling(209, min_periods=max(209//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.925 + 0.0001297 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_097_jerk_v97_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=48, w2=193, w3=222, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 48)
    acceleration = _rolling_slope(velocity, 193)
    curvature = _rolling_slope(acceleration, 222)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1058 * acceleration + 0.0001298 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_098_accel_v98_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=55, w2=204, w3=235, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(55, min_periods=max(55//3, 2)).mean(), upside.rolling(204, min_periods=max(204//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.95375 + 0.0001299 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_099_jerk_v99_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=62, w2=215, w3=248, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(215, min_periods=max(215//3, 2)).max()
    rebound = x - x.rolling(62, min_periods=max(62//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.121 * _rolling_slope(draw, 248) + 0.00013 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_100_accel_v100_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=69, w2=226, w3=261, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 69)
    baseline = trend.rolling(226, min_periods=max(226//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(261, min_periods=max(261//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.9825 + 0.0001301 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_101_jerk_v101_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=76, w2=237, w3=274, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 76)
    slow = _rolling_slope(x, 237)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=274, adjust=False).mean() * 0.996875 + 0.0001302 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_102_accel_v102_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=83, w2=248, w3=287, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(248, min_periods=max(248//3, 2)).max()
    trough = x.rolling(83, min_periods=max(83//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.01125 + 0.0001303 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_103_jerk_v103_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=90, w2=259, w3=300, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(90)
    rank = change.rolling(259, min_periods=max(259//3, 2)).rank(pct=True)
    persistence = change.rolling(300, min_periods=max(300//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1514 * persistence + 0.0001304 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_104_accel_v104_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=97, w2=270, w3=313, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(97, min_periods=max(97//3, 2)).std()
    vol_slow = ret.rolling(270, min_periods=max(270//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.04 + 0.0001305 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_105_jerk_v105_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=104, w2=281, w3=326, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(281, min_periods=max(281//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 104)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1666 * slope + 0.0001306 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_106_accel_v106_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=111, w2=292, w3=339, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(111)
    drag = impulse.rolling(292, min_periods=max(292//3, 2)).mean()
    noise = impulse.abs().rolling(339, min_periods=max(339//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.06875 + 0.0001307 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_107_jerk_v107_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=118, w2=303, w3=352, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 118)
    acceleration = _rolling_slope(velocity, 303)
    curvature = _rolling_slope(acceleration, 352)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1818 * acceleration + 0.0001308 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_108_accel_v108_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=125, w2=314, w3=365, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(125, min_periods=max(125//3, 2)).mean(), upside.rolling(314, min_periods=max(314//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.0975 + 0.0001309 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_109_jerk_v109_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=132, w2=325, w3=378, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(325, min_periods=max(325//3, 2)).max()
    rebound = x - x.rolling(132, min_periods=max(132//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.197 * _rolling_slope(draw, 378) + 0.000131 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_110_accel_v110_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=139, w2=336, w3=391, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 139)
    baseline = trend.rolling(336, min_periods=max(336//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(391, min_periods=max(391//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.12625 + 0.0001311 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_111_jerk_v111_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=146, w2=347, w3=404, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 146)
    slow = _rolling_slope(x, 347)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.140625 + 0.0001312 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_112_accel_v112_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=153, w2=358, w3=417, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(358, min_periods=max(358//3, 2)).max()
    trough = x.rolling(153, min_periods=max(153//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.155 + 0.0001313 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_113_jerk_v113_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=160, w2=369, w3=430, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(369, min_periods=max(369//3, 2)).rank(pct=True)
    persistence = change.rolling(430, min_periods=max(430//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2274 * persistence + 0.0001314 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_114_accel_v114_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=167, w2=380, w3=443, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(167, min_periods=max(167//3, 2)).std()
    vol_slow = ret.rolling(380, min_periods=max(380//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.18375 + 0.0001315 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_115_jerk_v115_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=174, w2=391, w3=456, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(391, min_periods=max(391//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 174)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2426 * slope + 0.0001316 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_116_accel_v116_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=181, w2=402, w3=469, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(402, min_periods=max(402//3, 2)).mean()
    noise = impulse.abs().rolling(469, min_periods=max(469//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.2125 + 0.0001317 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_117_jerk_v117_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=188, w2=413, w3=482, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 188)
    acceleration = _rolling_slope(velocity, 413)
    curvature = _rolling_slope(acceleration, 482)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2578 * acceleration + 0.0001318 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_118_accel_v118_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=195, w2=424, w3=495, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(195, min_periods=max(195//3, 2)).mean(), upside.rolling(424, min_periods=max(424//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.24125 + 0.0001319 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_119_jerk_v119_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=202, w2=435, w3=508, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(435, min_periods=max(435//3, 2)).max()
    rebound = x - x.rolling(202, min_periods=max(202//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.273 * _rolling_slope(draw, 508) + 0.000132 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_120_accel_v120_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=209, w2=446, w3=521, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 209)
    baseline = trend.rolling(446, min_periods=max(446//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(521, min_periods=max(521//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.27 + 0.0001321 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_121_jerk_v121_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=216, w2=457, w3=534, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 216)
    slow = _rolling_slope(x, 457)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.284375 + 0.0001322 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_122_accel_v122_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=223, w2=468, w3=547, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(468, min_periods=max(468//3, 2)).max()
    trough = x.rolling(223, min_periods=max(223//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.29875 + 0.0001323 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_123_jerk_v123_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=230, w2=479, w3=560, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(479, min_periods=max(479//3, 2)).rank(pct=True)
    persistence = change.rolling(560, min_periods=max(560//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3034 * persistence + 0.0001324 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_124_accel_v124_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=237, w2=490, w3=573, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(237, min_periods=max(237//3, 2)).std()
    vol_slow = ret.rolling(490, min_periods=max(490//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.3275 + 0.0001325 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_125_jerk_v125_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=244, w2=501, w3=586, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(501, min_periods=max(501//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 244)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3186 * slope + 0.0001326 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_126_accel_v126_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=251, w2=512, w3=599, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(512, min_periods=max(512//3, 2)).mean()
    noise = impulse.abs().rolling(599, min_periods=max(599//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.35625 + 0.0001327 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_127_jerk_v127_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=7, w2=20, w3=612, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 7)
    acceleration = _rolling_slope(velocity, 20)
    curvature = _rolling_slope(acceleration, 612)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3338 * acceleration + 0.0001328 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_128_accel_v128_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=14, w2=31, w3=625, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(14, min_periods=max(14//3, 2)).mean(), upside.rolling(31, min_periods=max(31//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.385 + 0.0001329 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_129_jerk_v129_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=21, w2=42, w3=638, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(42, min_periods=max(42//3, 2)).max()
    rebound = x - x.rolling(21, min_periods=max(21//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.349 * _rolling_slope(draw, 638) + 0.000133 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_130_accel_v130_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=28, w2=53, w3=651, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 28)
    baseline = trend.rolling(53, min_periods=max(53//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(651, min_periods=max(651//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.41375 + 0.0001331 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_131_jerk_v131_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=35, w2=64, w3=664, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 35)
    slow = _rolling_slope(x, 64)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.428125 + 0.0001332 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_132_accel_v132_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=42, w2=75, w3=677, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(75, min_periods=max(75//3, 2)).max()
    trough = x.rolling(42, min_periods=max(42//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.4425 + 0.0001333 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_133_jerk_v133_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=49, w2=86, w3=690, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(49)
    rank = change.rolling(86, min_periods=max(86//3, 2)).rank(pct=True)
    persistence = change.rolling(690, min_periods=max(690//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3794 * persistence + 0.0001334 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_134_accel_v134_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=56, w2=97, w3=703, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(56, min_periods=max(56//3, 2)).std()
    vol_slow = ret.rolling(97, min_periods=max(97//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.47125 + 0.0001335 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_135_jerk_v135_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=63, w2=108, w3=716, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(108, min_periods=max(108//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 63)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3946 * slope + 0.0001336 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_136_accel_v136_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=70, w2=119, w3=729, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(70)
    drag = impulse.rolling(119, min_periods=max(119//3, 2)).mean()
    noise = impulse.abs().rolling(729, min_periods=max(729//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.5 + 0.0001337 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_137_jerk_v137_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=77, w2=130, w3=742, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 77)
    acceleration = _rolling_slope(velocity, 130)
    curvature = _rolling_slope(acceleration, 742)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.4098 * acceleration + 0.0001338 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_138_accel_v138_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=84, w2=141, w3=755, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(84, min_periods=max(84//3, 2)).mean(), upside.rolling(141, min_periods=max(141//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.52875 + 0.0001339 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_139_jerk_v139_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=91, w2=152, w3=768, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(152, min_periods=max(152//3, 2)).max()
    rebound = x - x.rolling(91, min_periods=max(91//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0486 * _rolling_slope(draw, 768) + 0.000134 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_140_accel_v140_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=98, w2=163, w3=24, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 98)
    baseline = trend.rolling(163, min_periods=max(163//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(24, min_periods=max(24//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.5575 + 0.0001341 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_141_jerk_v141_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=105, w2=174, w3=37, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 105)
    slow = _rolling_slope(x, 174)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=37, adjust=False).mean() * 1.571875 + 0.0001342 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_142_accel_v142_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=112, w2=185, w3=50, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(185, min_periods=max(185//3, 2)).max()
    trough = x.rolling(112, min_periods=max(112//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.58625 + 0.0001343 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_143_jerk_v143_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=119, w2=196, w3=63, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(119)
    rank = change.rolling(196, min_periods=max(196//3, 2)).rank(pct=True)
    persistence = change.rolling(63, min_periods=max(63//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.079 * persistence + 0.0001344 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_144_accel_v144_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=126, w2=207, w3=76, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(126, min_periods=max(126//3, 2)).std()
    vol_slow = ret.rolling(207, min_periods=max(207//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.615 + 0.0001345 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_145_jerk_v145_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=133, w2=218, w3=89, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(218, min_periods=max(218//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 133)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0942 * slope + 0.0001346 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_146_accel_v146_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=140, w2=229, w3=102, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(229, min_periods=max(229//3, 2)).mean()
    noise = impulse.abs().rolling(102, min_periods=max(102//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.870625 + 0.0001347 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_147_jerk_v147_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=147, w2=240, w3=115, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 147)
    acceleration = _rolling_slope(velocity, 240)
    curvature = _rolling_slope(acceleration, 115)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1094 * acceleration + 0.0001348 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_148_accel_v148_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=154, w2=251, w3=128, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(154, min_periods=max(154//3, 2)).mean(), upside.rolling(251, min_periods=max(251//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.899375 + 0.0001349 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_149_jerk_v149_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=161, w2=262, w3=141, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(262, min_periods=max(262//3, 2)).max()
    rebound = x - x.rolling(161, min_periods=max(161//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1246 * _rolling_slope(draw, 141) + 0.000135 * anchor
    return base_signal.diff().diff().diff()

def f03_amd_150_accel_v150_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=168, w2=273, w3=154, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 168)
    baseline = trend.rolling(273, min_periods=max(273//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(154, min_periods=max(154//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.928125 + 0.0001351 * anchor
    return base_signal.diff().diff().diff()
