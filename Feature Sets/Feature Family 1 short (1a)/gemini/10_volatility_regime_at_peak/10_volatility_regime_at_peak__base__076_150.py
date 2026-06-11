"""10 volatility regime at peak base features 76-150 â€” Pipeline 1a-HF Grade v3.

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

def f10_vreg_076_accel_v76(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=118, w2=450, w3=275, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(118)
    drag = impulse.rolling(450, min_periods=max(450//3, 2)).mean()
    noise = impulse.abs().rolling(275, min_periods=max(275//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.6025 + 0.0006077 * anchor

def f10_vreg_077_jerk_v77(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=125, w2=461, w3=288, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 125)
    acceleration = _rolling_slope(velocity, 461)
    curvature = _rolling_slope(acceleration, 288)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2994 * acceleration + 0.0006078 * anchor

def f10_vreg_078_accel_v78(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=132, w2=472, w3=301, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(132, min_periods=max(132//3, 2)).mean(), upside.rolling(472, min_periods=max(472//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.858125 + 0.0006079 * anchor

def f10_vreg_079_jerk_v79(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=139, w2=483, w3=314, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(483, min_periods=max(483//3, 2)).max()
    rebound = x - x.rolling(139, min_periods=max(139//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3146 * _rolling_slope(draw, 314) + 0.000608 * anchor

def f10_vreg_080_accel_v80(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=146, w2=494, w3=327, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 146)
    baseline = trend.rolling(494, min_periods=max(494//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(327, min_periods=max(327//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.886875 + 0.0006081 * anchor

def f10_vreg_081_jerk_v81(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=153, w2=505, w3=340, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 153)
    slow = _rolling_slope(x, 505)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.90125 + 0.0006082 * anchor

def f10_vreg_082_accel_v82(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=160, w2=13, w3=353, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(13, min_periods=max(13//3, 2)).max()
    trough = x.rolling(160, min_periods=max(160//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.915625 + 0.0006083 * anchor

def f10_vreg_083_jerk_v83(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=167, w2=24, w3=366, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(24, min_periods=max(24//3, 2)).rank(pct=True)
    persistence = change.rolling(366, min_periods=max(366//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.345 * persistence + 0.0006084 * anchor

def f10_vreg_084_accel_v84(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=174, w2=35, w3=379, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(174, min_periods=max(174//3, 2)).std()
    vol_slow = ret.rolling(35, min_periods=max(35//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.944375 + 0.0006085 * anchor

def f10_vreg_085_jerk_v85(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=181, w2=46, w3=392, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(46, min_periods=max(46//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 181)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3602 * slope + 0.0006086 * anchor

def f10_vreg_086_accel_v86(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=188, w2=57, w3=405, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(57, min_periods=max(57//3, 2)).mean()
    noise = impulse.abs().rolling(405, min_periods=max(405//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.973125 + 0.0006087 * anchor

def f10_vreg_087_jerk_v87(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=195, w2=68, w3=418, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 195)
    acceleration = _rolling_slope(velocity, 68)
    curvature = _rolling_slope(acceleration, 418)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3754 * acceleration + 0.0006088 * anchor

def f10_vreg_088_accel_v88(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=202, w2=79, w3=431, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(202, min_periods=max(202//3, 2)).mean(), upside.rolling(79, min_periods=max(79//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.001875 + 0.0006089 * anchor

def f10_vreg_089_jerk_v89(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=209, w2=90, w3=444, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(90, min_periods=max(90//3, 2)).max()
    rebound = x - x.rolling(209, min_periods=max(209//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3906 * _rolling_slope(draw, 444) + 0.000609 * anchor

def f10_vreg_090_accel_v90(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=216, w2=101, w3=457, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 216)
    baseline = trend.rolling(101, min_periods=max(101//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(457, min_periods=max(457//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.030625 + 0.0006091 * anchor

def f10_vreg_091_jerk_v91(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=223, w2=112, w3=470, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 223)
    slow = _rolling_slope(x, 112)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.045 + 0.0006092 * anchor

def f10_vreg_092_accel_v92(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=230, w2=123, w3=483, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(123, min_periods=max(123//3, 2)).max()
    trough = x.rolling(230, min_periods=max(230//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.059375 + 0.0006093 * anchor

def f10_vreg_093_jerk_v93(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=237, w2=134, w3=496, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(134, min_periods=max(134//3, 2)).rank(pct=True)
    persistence = change.rolling(496, min_periods=max(496//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0446 * persistence + 0.0006094 * anchor

def f10_vreg_094_accel_v94(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=244, w2=145, w3=509, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(244, min_periods=max(244//3, 2)).std()
    vol_slow = ret.rolling(145, min_periods=max(145//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.088125 + 0.0006095 * anchor

def f10_vreg_095_jerk_v95(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=251, w2=156, w3=522, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(156, min_periods=max(156//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 251)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0598 * slope + 0.0006096 * anchor

def f10_vreg_096_accel_v96(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=7, w2=167, w3=535, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(7)
    drag = impulse.rolling(167, min_periods=max(167//3, 2)).mean()
    noise = impulse.abs().rolling(535, min_periods=max(535//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.116875 + 0.0006097 * anchor

def f10_vreg_097_jerk_v97(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=14, w2=178, w3=548, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 14)
    acceleration = _rolling_slope(velocity, 178)
    curvature = _rolling_slope(acceleration, 548)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.075 * acceleration + 0.0006098 * anchor

def f10_vreg_098_accel_v98(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=21, w2=189, w3=561, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(21, min_periods=max(21//3, 2)).mean(), upside.rolling(189, min_periods=max(189//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.145625 + 0.0006099 * anchor

def f10_vreg_099_jerk_v99(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=28, w2=200, w3=574, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(200, min_periods=max(200//3, 2)).max()
    rebound = x - x.rolling(28, min_periods=max(28//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0902 * _rolling_slope(draw, 574) + 0.00061 * anchor

def f10_vreg_100_accel_v100(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=35, w2=211, w3=587, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 35)
    baseline = trend.rolling(211, min_periods=max(211//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(587, min_periods=max(587//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.174375 + 0.0006101 * anchor

def f10_vreg_101_jerk_v101(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=42, w2=222, w3=600, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 42)
    slow = _rolling_slope(x, 222)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.18875 + 0.0006102 * anchor

def f10_vreg_102_accel_v102(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=49, w2=233, w3=613, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(233, min_periods=max(233//3, 2)).max()
    trough = x.rolling(49, min_periods=max(49//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.203125 + 0.0006103 * anchor

def f10_vreg_103_jerk_v103(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=56, w2=244, w3=626, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(56)
    rank = change.rolling(244, min_periods=max(244//3, 2)).rank(pct=True)
    persistence = change.rolling(626, min_periods=max(626//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1206 * persistence + 0.0006104 * anchor

def f10_vreg_104_accel_v104(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=63, w2=255, w3=639, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(63, min_periods=max(63//3, 2)).std()
    vol_slow = ret.rolling(255, min_periods=max(255//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.231875 + 0.0006105 * anchor

def f10_vreg_105_jerk_v105(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=70, w2=266, w3=652, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(266, min_periods=max(266//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 70)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1358 * slope + 0.0006106 * anchor

def f10_vreg_106_accel_v106(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=77, w2=277, w3=665, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(77)
    drag = impulse.rolling(277, min_periods=max(277//3, 2)).mean()
    noise = impulse.abs().rolling(665, min_periods=max(665//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.260625 + 0.0006107 * anchor

def f10_vreg_107_jerk_v107(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=84, w2=288, w3=678, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 84)
    acceleration = _rolling_slope(velocity, 288)
    curvature = _rolling_slope(acceleration, 678)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.151 * acceleration + 0.0006108 * anchor

def f10_vreg_108_accel_v108(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=91, w2=299, w3=691, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(91, min_periods=max(91//3, 2)).mean(), upside.rolling(299, min_periods=max(299//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.289375 + 0.0006109 * anchor

def f10_vreg_109_jerk_v109(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=98, w2=310, w3=704, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(310, min_periods=max(310//3, 2)).max()
    rebound = x - x.rolling(98, min_periods=max(98//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1662 * _rolling_slope(draw, 704) + 0.000611 * anchor

def f10_vreg_110_accel_v110(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=105, w2=321, w3=717, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 105)
    baseline = trend.rolling(321, min_periods=max(321//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(717, min_periods=max(717//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.318125 + 0.0006111 * anchor

def f10_vreg_111_jerk_v111(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=112, w2=332, w3=730, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 112)
    slow = _rolling_slope(x, 332)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.3325 + 0.0006112 * anchor

def f10_vreg_112_accel_v112(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=119, w2=343, w3=743, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(343, min_periods=max(343//3, 2)).max()
    trough = x.rolling(119, min_periods=max(119//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.346875 + 0.0006113 * anchor

def f10_vreg_113_jerk_v113(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=126, w2=354, w3=756, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(354, min_periods=max(354//3, 2)).rank(pct=True)
    persistence = change.rolling(756, min_periods=max(756//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1966 * persistence + 0.0006114 * anchor

def f10_vreg_114_accel_v114(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=133, w2=365, w3=769, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(133, min_periods=max(133//3, 2)).std()
    vol_slow = ret.rolling(365, min_periods=max(365//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.375625 + 0.0006115 * anchor

def f10_vreg_115_jerk_v115(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=140, w2=376, w3=25, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(376, min_periods=max(376//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 140)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2118 * slope + 0.0006116 * anchor

def f10_vreg_116_accel_v116(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=147, w2=387, w3=38, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(387, min_periods=max(387//3, 2)).mean()
    noise = impulse.abs().rolling(38, min_periods=max(38//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.404375 + 0.0006117 * anchor

def f10_vreg_117_jerk_v117(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=154, w2=398, w3=51, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 154)
    acceleration = _rolling_slope(velocity, 398)
    curvature = _rolling_slope(acceleration, 51)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.227 * acceleration + 0.0006118 * anchor

def f10_vreg_118_accel_v118(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=161, w2=409, w3=64, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(161, min_periods=max(161//3, 2)).mean(), upside.rolling(409, min_periods=max(409//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(64) * 1.433125 + 0.0006119 * anchor

def f10_vreg_119_jerk_v119(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=168, w2=420, w3=77, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(420, min_periods=max(420//3, 2)).max()
    rebound = x - x.rolling(168, min_periods=max(168//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2422 * _rolling_slope(draw, 77) + 0.000612 * anchor

def f10_vreg_120_accel_v120(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=175, w2=431, w3=90, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 175)
    baseline = trend.rolling(431, min_periods=max(431//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(90, min_periods=max(90//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.461875 + 0.0006121 * anchor

def f10_vreg_121_jerk_v121(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=182, w2=442, w3=103, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 182)
    slow = _rolling_slope(x, 442)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=103, adjust=False).mean() * 1.47625 + 0.0006122 * anchor

def f10_vreg_122_accel_v122(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=189, w2=453, w3=116, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(453, min_periods=max(453//3, 2)).max()
    trough = x.rolling(189, min_periods=max(189//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.490625 + 0.0006123 * anchor

def f10_vreg_123_jerk_v123(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=196, w2=464, w3=129, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(464, min_periods=max(464//3, 2)).rank(pct=True)
    persistence = change.rolling(129, min_periods=max(129//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2726 * persistence + 0.0006124 * anchor

def f10_vreg_124_accel_v124(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=203, w2=475, w3=142, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(203, min_periods=max(203//3, 2)).std()
    vol_slow = ret.rolling(475, min_periods=max(475//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.519375 + 0.0006125 * anchor

def f10_vreg_125_jerk_v125(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=210, w2=486, w3=155, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(486, min_periods=max(486//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 210)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2878 * slope + 0.0006126 * anchor

def f10_vreg_126_accel_v126(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=217, w2=497, w3=168, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(497, min_periods=max(497//3, 2)).mean()
    noise = impulse.abs().rolling(168, min_periods=max(168//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.548125 + 0.0006127 * anchor

def f10_vreg_127_jerk_v127(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=224, w2=508, w3=181, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 224)
    acceleration = _rolling_slope(velocity, 508)
    curvature = _rolling_slope(acceleration, 181)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.303 * acceleration + 0.0006128 * anchor

def f10_vreg_128_accel_v128(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=231, w2=16, w3=194, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(231, min_periods=max(231//3, 2)).mean(), upside.rolling(16, min_periods=max(16//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.576875 + 0.0006129 * anchor

def f10_vreg_129_jerk_v129(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=238, w2=27, w3=207, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(27, min_periods=max(27//3, 2)).max()
    rebound = x - x.rolling(238, min_periods=max(238//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3182 * _rolling_slope(draw, 207) + 0.000613 * anchor

def f10_vreg_130_accel_v130(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=245, w2=38, w3=220, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 245)
    baseline = trend.rolling(38, min_periods=max(38//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(220, min_periods=max(220//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.605625 + 0.0006131 * anchor

def f10_vreg_131_jerk_v131(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=252, w2=49, w3=233, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 252)
    slow = _rolling_slope(x, 49)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=233, adjust=False).mean() * 1.62 + 0.0006132 * anchor

def f10_vreg_132_accel_v132(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=8, w2=60, w3=246, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(60, min_periods=max(60//3, 2)).max()
    trough = x.rolling(8, min_periods=max(8//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.86125 + 0.0006133 * anchor

def f10_vreg_133_jerk_v133(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=15, w2=71, w3=259, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(15)
    rank = change.rolling(71, min_periods=max(71//3, 2)).rank(pct=True)
    persistence = change.rolling(259, min_periods=max(259//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3486 * persistence + 0.0006134 * anchor

def f10_vreg_134_accel_v134(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=22, w2=82, w3=272, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(22, min_periods=max(22//3, 2)).std()
    vol_slow = ret.rolling(82, min_periods=max(82//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.89 + 0.0006135 * anchor

def f10_vreg_135_jerk_v135(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=29, w2=93, w3=285, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(93, min_periods=max(93//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 29)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3638 * slope + 0.0006136 * anchor

def f10_vreg_136_accel_v136(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=36, w2=104, w3=298, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(36)
    drag = impulse.rolling(104, min_periods=max(104//3, 2)).mean()
    noise = impulse.abs().rolling(298, min_periods=max(298//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.91875 + 0.0006137 * anchor

def f10_vreg_137_jerk_v137(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=43, w2=115, w3=311, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 43)
    acceleration = _rolling_slope(velocity, 115)
    curvature = _rolling_slope(acceleration, 311)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.379 * acceleration + 0.0006138 * anchor

def f10_vreg_138_accel_v138(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=50, w2=126, w3=324, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(50, min_periods=max(50//3, 2)).mean(), upside.rolling(126, min_periods=max(126//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.9475 + 0.0006139 * anchor

def f10_vreg_139_jerk_v139(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=57, w2=137, w3=337, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(137, min_periods=max(137//3, 2)).max()
    rebound = x - x.rolling(57, min_periods=max(57//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3942 * _rolling_slope(draw, 337) + 0.000614 * anchor

def f10_vreg_140_accel_v140(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=64, w2=148, w3=350, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 64)
    baseline = trend.rolling(148, min_periods=max(148//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(350, min_periods=max(350//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.97625 + 0.0006141 * anchor

def f10_vreg_141_jerk_v141(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=71, w2=159, w3=363, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 71)
    slow = _rolling_slope(x, 159)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.990625 + 0.0006142 * anchor

def f10_vreg_142_accel_v142(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=78, w2=170, w3=376, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(170, min_periods=max(170//3, 2)).max()
    trough = x.rolling(78, min_periods=max(78//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.005 + 0.0006143 * anchor

def f10_vreg_143_jerk_v143(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=85, w2=181, w3=389, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(85)
    rank = change.rolling(181, min_periods=max(181//3, 2)).rank(pct=True)
    persistence = change.rolling(389, min_periods=max(389//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0482 * persistence + 0.0006144 * anchor

def f10_vreg_144_accel_v144(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=92, w2=192, w3=402, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(92, min_periods=max(92//3, 2)).std()
    vol_slow = ret.rolling(192, min_periods=max(192//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.03375 + 0.0006145 * anchor

def f10_vreg_145_jerk_v145(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=99, w2=203, w3=415, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(203, min_periods=max(203//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 99)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0634 * slope + 0.0006146 * anchor

def f10_vreg_146_accel_v146(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=106, w2=214, w3=428, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(106)
    drag = impulse.rolling(214, min_periods=max(214//3, 2)).mean()
    noise = impulse.abs().rolling(428, min_periods=max(428//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.0625 + 0.0006147 * anchor

def f10_vreg_147_jerk_v147(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=113, w2=225, w3=441, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 113)
    acceleration = _rolling_slope(velocity, 225)
    curvature = _rolling_slope(acceleration, 441)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0786 * acceleration + 0.0006148 * anchor

def f10_vreg_148_accel_v148(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=120, w2=236, w3=454, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(120, min_periods=max(120//3, 2)).mean(), upside.rolling(236, min_periods=max(236//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.09125 + 0.0006149 * anchor

def f10_vreg_149_jerk_v149(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=127, w2=247, w3=467, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(247, min_periods=max(247//3, 2)).max()
    rebound = x - x.rolling(127, min_periods=max(127//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0938 * _rolling_slope(draw, 467) + 0.000615 * anchor

def f10_vreg_150_accel_v150(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=134, w2=258, w3=480, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 134)
    baseline = trend.rolling(258, min_periods=max(258//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(480, min_periods=max(480//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.12 + 0.0006151 * anchor
