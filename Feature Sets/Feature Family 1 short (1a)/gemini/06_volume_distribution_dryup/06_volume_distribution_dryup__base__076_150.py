"""06 volume distribution dryup base features 76-150 â€” Pipeline 1a-HF Grade v3.

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

def f06_vdd_076_accel_v76(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=202, w2=145, w3=639, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(145, min_periods=max(145//3, 2)).mean()
    noise = impulse.abs().rolling(639, min_periods=max(639//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.999375 + 0.0003077 * anchor

def f06_vdd_077_jerk_v77(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=209, w2=156, w3=652, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 209)
    acceleration = _rolling_slope(velocity, 156)
    curvature = _rolling_slope(acceleration, 652)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0834 * acceleration + 0.0003078 * anchor

def f06_vdd_078_accel_v78(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=216, w2=167, w3=665, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(216, min_periods=max(216//3, 2)).mean(), upside.rolling(167, min_periods=max(167//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.028125 + 0.0003079 * anchor

def f06_vdd_079_jerk_v79(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=223, w2=178, w3=678, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(178, min_periods=max(178//3, 2)).max()
    rebound = x - x.rolling(223, min_periods=max(223//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0986 * _rolling_slope(draw, 678) + 0.000308 * anchor

def f06_vdd_080_accel_v80(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=230, w2=189, w3=691, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 230)
    baseline = trend.rolling(189, min_periods=max(189//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(691, min_periods=max(691//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.056875 + 0.0003081 * anchor

def f06_vdd_081_jerk_v81(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=237, w2=200, w3=704, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 237)
    slow = _rolling_slope(x, 200)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.07125 + 0.0003082 * anchor

def f06_vdd_082_accel_v82(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=244, w2=211, w3=717, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(211, min_periods=max(211//3, 2)).max()
    trough = x.rolling(244, min_periods=max(244//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.085625 + 0.0003083 * anchor

def f06_vdd_083_jerk_v83(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=251, w2=222, w3=730, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(222, min_periods=max(222//3, 2)).rank(pct=True)
    persistence = change.rolling(730, min_periods=max(730//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.129 * persistence + 0.0003084 * anchor

def f06_vdd_084_accel_v84(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=7, w2=233, w3=743, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(7, min_periods=max(7//3, 2)).std()
    vol_slow = ret.rolling(233, min_periods=max(233//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.114375 + 0.0003085 * anchor

def f06_vdd_085_jerk_v85(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=14, w2=244, w3=756, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(244, min_periods=max(244//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 14)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1442 * slope + 0.0003086 * anchor

def f06_vdd_086_accel_v86(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=21, w2=255, w3=769, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(21)
    drag = impulse.rolling(255, min_periods=max(255//3, 2)).mean()
    noise = impulse.abs().rolling(769, min_periods=max(769//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.143125 + 0.0003087 * anchor

def f06_vdd_087_jerk_v87(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=28, w2=266, w3=25, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 28)
    acceleration = _rolling_slope(velocity, 266)
    curvature = _rolling_slope(acceleration, 25)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1594 * acceleration + 0.0003088 * anchor

def f06_vdd_088_accel_v88(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=35, w2=277, w3=38, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(35, min_periods=max(35//3, 2)).mean(), upside.rolling(277, min_periods=max(277//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(38) * 1.171875 + 0.0003089 * anchor

def f06_vdd_089_jerk_v89(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=42, w2=288, w3=51, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(288, min_periods=max(288//3, 2)).max()
    rebound = x - x.rolling(42, min_periods=max(42//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1746 * _rolling_slope(draw, 51) + 0.000309 * anchor

def f06_vdd_090_accel_v90(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=49, w2=299, w3=64, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 49)
    baseline = trend.rolling(299, min_periods=max(299//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(64, min_periods=max(64//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.200625 + 0.0003091 * anchor

def f06_vdd_091_jerk_v91(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=56, w2=310, w3=77, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 56)
    slow = _rolling_slope(x, 310)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=77, adjust=False).mean() * 1.215 + 0.0003092 * anchor

def f06_vdd_092_accel_v92(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=63, w2=321, w3=90, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(321, min_periods=max(321//3, 2)).max()
    trough = x.rolling(63, min_periods=max(63//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.229375 + 0.0003093 * anchor

def f06_vdd_093_jerk_v93(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=70, w2=332, w3=103, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(70)
    rank = change.rolling(332, min_periods=max(332//3, 2)).rank(pct=True)
    persistence = change.rolling(103, min_periods=max(103//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.205 * persistence + 0.0003094 * anchor

def f06_vdd_094_accel_v94(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=77, w2=343, w3=116, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(77, min_periods=max(77//3, 2)).std()
    vol_slow = ret.rolling(343, min_periods=max(343//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.258125 + 0.0003095 * anchor

def f06_vdd_095_jerk_v95(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=84, w2=354, w3=129, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(354, min_periods=max(354//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 84)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2202 * slope + 0.0003096 * anchor

def f06_vdd_096_accel_v96(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=91, w2=365, w3=142, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(91)
    drag = impulse.rolling(365, min_periods=max(365//3, 2)).mean()
    noise = impulse.abs().rolling(142, min_periods=max(142//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.286875 + 0.0003097 * anchor

def f06_vdd_097_jerk_v97(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=98, w2=376, w3=155, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 98)
    acceleration = _rolling_slope(velocity, 376)
    curvature = _rolling_slope(acceleration, 155)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2354 * acceleration + 0.0003098 * anchor

def f06_vdd_098_accel_v98(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=105, w2=387, w3=168, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(105, min_periods=max(105//3, 2)).mean(), upside.rolling(387, min_periods=max(387//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.315625 + 0.0003099 * anchor

def f06_vdd_099_jerk_v99(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=112, w2=398, w3=181, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(398, min_periods=max(398//3, 2)).max()
    rebound = x - x.rolling(112, min_periods=max(112//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2506 * _rolling_slope(draw, 181) + 0.00031 * anchor

def f06_vdd_100_accel_v100(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=119, w2=409, w3=194, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 119)
    baseline = trend.rolling(409, min_periods=max(409//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(194, min_periods=max(194//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.344375 + 0.0003101 * anchor

def f06_vdd_101_jerk_v101(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=126, w2=420, w3=207, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 126)
    slow = _rolling_slope(x, 420)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=207, adjust=False).mean() * 1.35875 + 0.0003102 * anchor

def f06_vdd_102_accel_v102(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=133, w2=431, w3=220, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(431, min_periods=max(431//3, 2)).max()
    trough = x.rolling(133, min_periods=max(133//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.373125 + 0.0003103 * anchor

def f06_vdd_103_jerk_v103(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=140, w2=442, w3=233, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(442, min_periods=max(442//3, 2)).rank(pct=True)
    persistence = change.rolling(233, min_periods=max(233//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.281 * persistence + 0.0003104 * anchor

def f06_vdd_104_accel_v104(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=147, w2=453, w3=246, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(147, min_periods=max(147//3, 2)).std()
    vol_slow = ret.rolling(453, min_periods=max(453//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.401875 + 0.0003105 * anchor

def f06_vdd_105_jerk_v105(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=154, w2=464, w3=259, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(464, min_periods=max(464//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 154)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2962 * slope + 0.0003106 * anchor

def f06_vdd_106_accel_v106(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=161, w2=475, w3=272, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(475, min_periods=max(475//3, 2)).mean()
    noise = impulse.abs().rolling(272, min_periods=max(272//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.430625 + 0.0003107 * anchor

def f06_vdd_107_jerk_v107(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=168, w2=486, w3=285, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 168)
    acceleration = _rolling_slope(velocity, 486)
    curvature = _rolling_slope(acceleration, 285)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3114 * acceleration + 0.0003108 * anchor

def f06_vdd_108_accel_v108(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=175, w2=497, w3=298, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(175, min_periods=max(175//3, 2)).mean(), upside.rolling(497, min_periods=max(497//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.459375 + 0.0003109 * anchor

def f06_vdd_109_jerk_v109(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=182, w2=508, w3=311, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(508, min_periods=max(508//3, 2)).max()
    rebound = x - x.rolling(182, min_periods=max(182//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3266 * _rolling_slope(draw, 311) + 0.000311 * anchor

def f06_vdd_110_accel_v110(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=189, w2=16, w3=324, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 189)
    baseline = trend.rolling(16, min_periods=max(16//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(324, min_periods=max(324//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.488125 + 0.0003111 * anchor

def f06_vdd_111_jerk_v111(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=196, w2=27, w3=337, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 196)
    slow = _rolling_slope(x, 27)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.5025 + 0.0003112 * anchor

def f06_vdd_112_accel_v112(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=203, w2=38, w3=350, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(38, min_periods=max(38//3, 2)).max()
    trough = x.rolling(203, min_periods=max(203//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.516875 + 0.0003113 * anchor

def f06_vdd_113_jerk_v113(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=210, w2=49, w3=363, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(49, min_periods=max(49//3, 2)).rank(pct=True)
    persistence = change.rolling(363, min_periods=max(363//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.357 * persistence + 0.0003114 * anchor

def f06_vdd_114_accel_v114(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=217, w2=60, w3=376, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(217, min_periods=max(217//3, 2)).std()
    vol_slow = ret.rolling(60, min_periods=max(60//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.545625 + 0.0003115 * anchor

def f06_vdd_115_jerk_v115(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=224, w2=71, w3=389, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(71, min_periods=max(71//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 224)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3722 * slope + 0.0003116 * anchor

def f06_vdd_116_accel_v116(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=231, w2=82, w3=402, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(82, min_periods=max(82//3, 2)).mean()
    noise = impulse.abs().rolling(402, min_periods=max(402//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.574375 + 0.0003117 * anchor

def f06_vdd_117_jerk_v117(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=238, w2=93, w3=415, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 238)
    acceleration = _rolling_slope(velocity, 93)
    curvature = _rolling_slope(acceleration, 415)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3874 * acceleration + 0.0003118 * anchor

def f06_vdd_118_accel_v118(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=245, w2=104, w3=428, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(245, min_periods=max(245//3, 2)).mean(), upside.rolling(104, min_periods=max(104//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.603125 + 0.0003119 * anchor

def f06_vdd_119_jerk_v119(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=252, w2=115, w3=441, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(115, min_periods=max(115//3, 2)).max()
    rebound = x - x.rolling(252, min_periods=max(252//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.4026 * _rolling_slope(draw, 441) + 0.000312 * anchor

def f06_vdd_120_accel_v120(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=8, w2=126, w3=454, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 8)
    baseline = trend.rolling(126, min_periods=max(126//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(454, min_periods=max(454//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.85875 + 0.0003121 * anchor

def f06_vdd_121_jerk_v121(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=15, w2=137, w3=467, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 15)
    slow = _rolling_slope(x, 137)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.873125 + 0.0003122 * anchor

def f06_vdd_122_accel_v122(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=22, w2=148, w3=480, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(148, min_periods=max(148//3, 2)).max()
    trough = x.rolling(22, min_periods=max(22//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.8875 + 0.0003123 * anchor

def f06_vdd_123_jerk_v123(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=29, w2=159, w3=493, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(29)
    rank = change.rolling(159, min_periods=max(159//3, 2)).rank(pct=True)
    persistence = change.rolling(493, min_periods=max(493//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0566 * persistence + 0.0003124 * anchor

def f06_vdd_124_accel_v124(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=36, w2=170, w3=506, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(36, min_periods=max(36//3, 2)).std()
    vol_slow = ret.rolling(170, min_periods=max(170//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.91625 + 0.0003125 * anchor

def f06_vdd_125_jerk_v125(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=43, w2=181, w3=519, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(181, min_periods=max(181//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 43)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0718 * slope + 0.0003126 * anchor

def f06_vdd_126_accel_v126(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=50, w2=192, w3=532, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(50)
    drag = impulse.rolling(192, min_periods=max(192//3, 2)).mean()
    noise = impulse.abs().rolling(532, min_periods=max(532//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.945 + 0.0003127 * anchor

def f06_vdd_127_jerk_v127(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=57, w2=203, w3=545, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 57)
    acceleration = _rolling_slope(velocity, 203)
    curvature = _rolling_slope(acceleration, 545)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.087 * acceleration + 0.0003128 * anchor

def f06_vdd_128_accel_v128(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=64, w2=214, w3=558, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(64, min_periods=max(64//3, 2)).mean(), upside.rolling(214, min_periods=max(214//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.97375 + 0.0003129 * anchor

def f06_vdd_129_jerk_v129(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=71, w2=225, w3=571, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(225, min_periods=max(225//3, 2)).max()
    rebound = x - x.rolling(71, min_periods=max(71//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1022 * _rolling_slope(draw, 571) + 0.000313 * anchor

def f06_vdd_130_accel_v130(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=78, w2=236, w3=584, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 78)
    baseline = trend.rolling(236, min_periods=max(236//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(584, min_periods=max(584//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.0025 + 0.0003131 * anchor

def f06_vdd_131_jerk_v131(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=85, w2=247, w3=597, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 85)
    slow = _rolling_slope(x, 247)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.016875 + 0.0003132 * anchor

def f06_vdd_132_accel_v132(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=92, w2=258, w3=610, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(258, min_periods=max(258//3, 2)).max()
    trough = x.rolling(92, min_periods=max(92//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.03125 + 0.0003133 * anchor

def f06_vdd_133_jerk_v133(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=99, w2=269, w3=623, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(99)
    rank = change.rolling(269, min_periods=max(269//3, 2)).rank(pct=True)
    persistence = change.rolling(623, min_periods=max(623//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1326 * persistence + 0.0003134 * anchor

def f06_vdd_134_accel_v134(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=106, w2=280, w3=636, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(106, min_periods=max(106//3, 2)).std()
    vol_slow = ret.rolling(280, min_periods=max(280//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.06 + 0.0003135 * anchor

def f06_vdd_135_jerk_v135(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=113, w2=291, w3=649, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(291, min_periods=max(291//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 113)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1478 * slope + 0.0003136 * anchor

def f06_vdd_136_accel_v136(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=120, w2=302, w3=662, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(120)
    drag = impulse.rolling(302, min_periods=max(302//3, 2)).mean()
    noise = impulse.abs().rolling(662, min_periods=max(662//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.08875 + 0.0003137 * anchor

def f06_vdd_137_jerk_v137(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=127, w2=313, w3=675, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 127)
    acceleration = _rolling_slope(velocity, 313)
    curvature = _rolling_slope(acceleration, 675)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.163 * acceleration + 0.0003138 * anchor

def f06_vdd_138_accel_v138(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=134, w2=324, w3=688, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(134, min_periods=max(134//3, 2)).mean(), upside.rolling(324, min_periods=max(324//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.1175 + 0.0003139 * anchor

def f06_vdd_139_jerk_v139(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=141, w2=335, w3=701, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(335, min_periods=max(335//3, 2)).max()
    rebound = x - x.rolling(141, min_periods=max(141//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1782 * _rolling_slope(draw, 701) + 0.000314 * anchor

def f06_vdd_140_accel_v140(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=148, w2=346, w3=714, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 148)
    baseline = trend.rolling(346, min_periods=max(346//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(714, min_periods=max(714//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.14625 + 0.0003141 * anchor

def f06_vdd_141_jerk_v141(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=155, w2=357, w3=727, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 155)
    slow = _rolling_slope(x, 357)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.160625 + 0.0003142 * anchor

def f06_vdd_142_accel_v142(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=162, w2=368, w3=740, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(368, min_periods=max(368//3, 2)).max()
    trough = x.rolling(162, min_periods=max(162//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.175 + 0.0003143 * anchor

def f06_vdd_143_jerk_v143(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=169, w2=379, w3=753, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(379, min_periods=max(379//3, 2)).rank(pct=True)
    persistence = change.rolling(753, min_periods=max(753//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2086 * persistence + 0.0003144 * anchor

def f06_vdd_144_accel_v144(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=176, w2=390, w3=766, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(176, min_periods=max(176//3, 2)).std()
    vol_slow = ret.rolling(390, min_periods=max(390//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.20375 + 0.0003145 * anchor

def f06_vdd_145_jerk_v145(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=183, w2=401, w3=22, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(401, min_periods=max(401//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 183)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2238 * slope + 0.0003146 * anchor

def f06_vdd_146_accel_v146(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=190, w2=412, w3=35, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(412, min_periods=max(412//3, 2)).mean()
    noise = impulse.abs().rolling(35, min_periods=max(35//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.2325 + 0.0003147 * anchor

def f06_vdd_147_jerk_v147(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=197, w2=423, w3=48, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 197)
    acceleration = _rolling_slope(velocity, 423)
    curvature = _rolling_slope(acceleration, 48)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.239 * acceleration + 0.0003148 * anchor

def f06_vdd_148_accel_v148(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=204, w2=434, w3=61, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(204, min_periods=max(204//3, 2)).mean(), upside.rolling(434, min_periods=max(434//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(61) * 1.26125 + 0.0003149 * anchor

def f06_vdd_149_jerk_v149(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=211, w2=445, w3=74, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(445, min_periods=max(445//3, 2)).max()
    rebound = x - x.rolling(211, min_periods=max(211//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2542 * _rolling_slope(draw, 74) + 0.000315 * anchor

def f06_vdd_150_accel_v150(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=218, w2=456, w3=87, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 218)
    baseline = trend.rolling(456, min_periods=max(456//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(87, min_periods=max(87//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.29 + 0.0003151 * anchor
