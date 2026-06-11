"""07 distribution signature base features 76-150 â€” Pipeline 1a-HF Grade v3.

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

def f07_dsi_076_accel_v76(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=135, w2=206, w3=112, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(206, min_periods=max(206//3, 2)).mean()
    noise = impulse.abs().rolling(112, min_periods=max(112//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.12 + 0.0003677 * anchor

def f07_dsi_077_jerk_v77(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=142, w2=217, w3=125, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 142)
    acceleration = _rolling_slope(velocity, 217)
    curvature = _rolling_slope(acceleration, 125)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1266 * acceleration + 0.0003678 * anchor

def f07_dsi_078_accel_v78(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=149, w2=228, w3=138, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(149, min_periods=max(149//3, 2)).mean(), upside.rolling(228, min_periods=max(228//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.14875 + 0.0003679 * anchor

def f07_dsi_079_jerk_v79(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=156, w2=239, w3=151, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(239, min_periods=max(239//3, 2)).max()
    rebound = x - x.rolling(156, min_periods=max(156//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1418 * _rolling_slope(draw, 151) + 0.000368 * anchor

def f07_dsi_080_accel_v80(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=163, w2=250, w3=164, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 163)
    baseline = trend.rolling(250, min_periods=max(250//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(164, min_periods=max(164//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.1775 + 0.0003681 * anchor

def f07_dsi_081_jerk_v81(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=170, w2=261, w3=177, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 170)
    slow = _rolling_slope(x, 261)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=177, adjust=False).mean() * 1.191875 + 0.0003682 * anchor

def f07_dsi_082_accel_v82(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=177, w2=272, w3=190, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(272, min_periods=max(272//3, 2)).max()
    trough = x.rolling(177, min_periods=max(177//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.20625 + 0.0003683 * anchor

def f07_dsi_083_jerk_v83(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=184, w2=283, w3=203, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(283, min_periods=max(283//3, 2)).rank(pct=True)
    persistence = change.rolling(203, min_periods=max(203//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1722 * persistence + 0.0003684 * anchor

def f07_dsi_084_accel_v84(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=191, w2=294, w3=216, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(191, min_periods=max(191//3, 2)).std()
    vol_slow = ret.rolling(294, min_periods=max(294//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.235 + 0.0003685 * anchor

def f07_dsi_085_jerk_v85(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=198, w2=305, w3=229, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(305, min_periods=max(305//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 198)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1874 * slope + 0.0003686 * anchor

def f07_dsi_086_accel_v86(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=205, w2=316, w3=242, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(316, min_periods=max(316//3, 2)).mean()
    noise = impulse.abs().rolling(242, min_periods=max(242//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.26375 + 0.0003687 * anchor

def f07_dsi_087_jerk_v87(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=212, w2=327, w3=255, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 212)
    acceleration = _rolling_slope(velocity, 327)
    curvature = _rolling_slope(acceleration, 255)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2026 * acceleration + 0.0003688 * anchor

def f07_dsi_088_accel_v88(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=219, w2=338, w3=268, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(219, min_periods=max(219//3, 2)).mean(), upside.rolling(338, min_periods=max(338//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.2925 + 0.0003689 * anchor

def f07_dsi_089_jerk_v89(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=226, w2=349, w3=281, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(349, min_periods=max(349//3, 2)).max()
    rebound = x - x.rolling(226, min_periods=max(226//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2178 * _rolling_slope(draw, 281) + 0.000369 * anchor

def f07_dsi_090_accel_v90(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=233, w2=360, w3=294, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 233)
    baseline = trend.rolling(360, min_periods=max(360//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(294, min_periods=max(294//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.32125 + 0.0003691 * anchor

def f07_dsi_091_jerk_v91(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=240, w2=371, w3=307, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 240)
    slow = _rolling_slope(x, 371)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.335625 + 0.0003692 * anchor

def f07_dsi_092_accel_v92(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=247, w2=382, w3=320, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(382, min_periods=max(382//3, 2)).max()
    trough = x.rolling(247, min_periods=max(247//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.35 + 0.0003693 * anchor

def f07_dsi_093_jerk_v93(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=254, w2=393, w3=333, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(393, min_periods=max(393//3, 2)).rank(pct=True)
    persistence = change.rolling(333, min_periods=max(333//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2482 * persistence + 0.0003694 * anchor

def f07_dsi_094_accel_v94(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=10, w2=404, w3=346, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(10, min_periods=max(10//3, 2)).std()
    vol_slow = ret.rolling(404, min_periods=max(404//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.37875 + 0.0003695 * anchor

def f07_dsi_095_jerk_v95(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=17, w2=415, w3=359, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(415, min_periods=max(415//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 17)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2634 * slope + 0.0003696 * anchor

def f07_dsi_096_accel_v96(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=24, w2=426, w3=372, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(24)
    drag = impulse.rolling(426, min_periods=max(426//3, 2)).mean()
    noise = impulse.abs().rolling(372, min_periods=max(372//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.4075 + 0.0003697 * anchor

def f07_dsi_097_jerk_v97(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=31, w2=437, w3=385, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 31)
    acceleration = _rolling_slope(velocity, 437)
    curvature = _rolling_slope(acceleration, 385)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2786 * acceleration + 0.0003698 * anchor

def f07_dsi_098_accel_v98(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=38, w2=448, w3=398, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(38, min_periods=max(38//3, 2)).mean(), upside.rolling(448, min_periods=max(448//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.43625 + 0.0003699 * anchor

def f07_dsi_099_jerk_v99(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=45, w2=459, w3=411, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(459, min_periods=max(459//3, 2)).max()
    rebound = x - x.rolling(45, min_periods=max(45//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2938 * _rolling_slope(draw, 411) + 0.00037 * anchor

def f07_dsi_100_accel_v100(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=52, w2=470, w3=424, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 52)
    baseline = trend.rolling(470, min_periods=max(470//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(424, min_periods=max(424//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.465 + 0.0003701 * anchor

def f07_dsi_101_jerk_v101(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=59, w2=481, w3=437, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 59)
    slow = _rolling_slope(x, 481)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.479375 + 0.0003702 * anchor

def f07_dsi_102_accel_v102(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=66, w2=492, w3=450, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(492, min_periods=max(492//3, 2)).max()
    trough = x.rolling(66, min_periods=max(66//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.49375 + 0.0003703 * anchor

def f07_dsi_103_jerk_v103(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=73, w2=503, w3=463, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(73)
    rank = change.rolling(503, min_periods=max(503//3, 2)).rank(pct=True)
    persistence = change.rolling(463, min_periods=max(463//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3242 * persistence + 0.0003704 * anchor

def f07_dsi_104_accel_v104(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=80, w2=11, w3=476, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(80, min_periods=max(80//3, 2)).std()
    vol_slow = ret.rolling(11, min_periods=max(11//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.5225 + 0.0003705 * anchor

def f07_dsi_105_jerk_v105(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=87, w2=22, w3=489, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(22, min_periods=max(22//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 87)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3394 * slope + 0.0003706 * anchor

def f07_dsi_106_accel_v106(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=94, w2=33, w3=502, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(94)
    drag = impulse.rolling(33, min_periods=max(33//3, 2)).mean()
    noise = impulse.abs().rolling(502, min_periods=max(502//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.55125 + 0.0003707 * anchor

def f07_dsi_107_jerk_v107(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=101, w2=44, w3=515, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 101)
    acceleration = _rolling_slope(velocity, 44)
    curvature = _rolling_slope(acceleration, 515)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3546 * acceleration + 0.0003708 * anchor

def f07_dsi_108_accel_v108(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=108, w2=55, w3=528, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(108, min_periods=max(108//3, 2)).mean(), upside.rolling(55, min_periods=max(55//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.58 + 0.0003709 * anchor

def f07_dsi_109_jerk_v109(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=115, w2=66, w3=541, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(66, min_periods=max(66//3, 2)).max()
    rebound = x - x.rolling(115, min_periods=max(115//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3698 * _rolling_slope(draw, 541) + 0.000371 * anchor

def f07_dsi_110_accel_v110(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=122, w2=77, w3=554, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 122)
    baseline = trend.rolling(77, min_periods=max(77//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(554, min_periods=max(554//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.60875 + 0.0003711 * anchor

def f07_dsi_111_jerk_v111(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=129, w2=88, w3=567, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 129)
    slow = _rolling_slope(x, 88)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.85 + 0.0003712 * anchor

def f07_dsi_112_accel_v112(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=136, w2=99, w3=580, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(99, min_periods=max(99//3, 2)).max()
    trough = x.rolling(136, min_periods=max(136//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.864375 + 0.0003713 * anchor

def f07_dsi_113_jerk_v113(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=143, w2=110, w3=593, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(110, min_periods=max(110//3, 2)).rank(pct=True)
    persistence = change.rolling(593, min_periods=max(593//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.4002 * persistence + 0.0003714 * anchor

def f07_dsi_114_accel_v114(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=150, w2=121, w3=606, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(150, min_periods=max(150//3, 2)).std()
    vol_slow = ret.rolling(121, min_periods=max(121//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.893125 + 0.0003715 * anchor

def f07_dsi_115_jerk_v115(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=157, w2=132, w3=619, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(132, min_periods=max(132//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 157)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.039 * slope + 0.0003716 * anchor

def f07_dsi_116_accel_v116(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=164, w2=143, w3=632, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(143, min_periods=max(143//3, 2)).mean()
    noise = impulse.abs().rolling(632, min_periods=max(632//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.921875 + 0.0003717 * anchor

def f07_dsi_117_jerk_v117(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=171, w2=154, w3=645, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 171)
    acceleration = _rolling_slope(velocity, 154)
    curvature = _rolling_slope(acceleration, 645)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0542 * acceleration + 0.0003718 * anchor

def f07_dsi_118_accel_v118(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=178, w2=165, w3=658, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(178, min_periods=max(178//3, 2)).mean(), upside.rolling(165, min_periods=max(165//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.950625 + 0.0003719 * anchor

def f07_dsi_119_jerk_v119(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=185, w2=176, w3=671, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(176, min_periods=max(176//3, 2)).max()
    rebound = x - x.rolling(185, min_periods=max(185//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0694 * _rolling_slope(draw, 671) + 0.000372 * anchor

def f07_dsi_120_accel_v120(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=192, w2=187, w3=684, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 192)
    baseline = trend.rolling(187, min_periods=max(187//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(684, min_periods=max(684//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.979375 + 0.0003721 * anchor

def f07_dsi_121_jerk_v121(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=199, w2=198, w3=697, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 199)
    slow = _rolling_slope(x, 198)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.99375 + 0.0003722 * anchor

def f07_dsi_122_accel_v122(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=206, w2=209, w3=710, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(209, min_periods=max(209//3, 2)).max()
    trough = x.rolling(206, min_periods=max(206//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.008125 + 0.0003723 * anchor

def f07_dsi_123_jerk_v123(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=213, w2=220, w3=723, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(220, min_periods=max(220//3, 2)).rank(pct=True)
    persistence = change.rolling(723, min_periods=max(723//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0998 * persistence + 0.0003724 * anchor

def f07_dsi_124_accel_v124(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=220, w2=231, w3=736, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(220, min_periods=max(220//3, 2)).std()
    vol_slow = ret.rolling(231, min_periods=max(231//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.036875 + 0.0003725 * anchor

def f07_dsi_125_jerk_v125(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=227, w2=242, w3=749, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(242, min_periods=max(242//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 227)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.115 * slope + 0.0003726 * anchor

def f07_dsi_126_accel_v126(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=234, w2=253, w3=762, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(253, min_periods=max(253//3, 2)).mean()
    noise = impulse.abs().rolling(762, min_periods=max(762//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.065625 + 0.0003727 * anchor

def f07_dsi_127_jerk_v127(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=241, w2=264, w3=18, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 241)
    acceleration = _rolling_slope(velocity, 264)
    curvature = _rolling_slope(acceleration, 18)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1302 * acceleration + 0.0003728 * anchor

def f07_dsi_128_accel_v128(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=248, w2=275, w3=31, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(248, min_periods=max(248//3, 2)).mean(), upside.rolling(275, min_periods=max(275//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(31) * 1.094375 + 0.0003729 * anchor

def f07_dsi_129_jerk_v129(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=255, w2=286, w3=44, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(286, min_periods=max(286//3, 2)).max()
    rebound = x - x.rolling(255, min_periods=max(255//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1454 * _rolling_slope(draw, 44) + 0.000373 * anchor

def f07_dsi_130_accel_v130(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=11, w2=297, w3=57, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 11)
    baseline = trend.rolling(297, min_periods=max(297//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(57, min_periods=max(57//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.123125 + 0.0003731 * anchor

def f07_dsi_131_jerk_v131(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=18, w2=308, w3=70, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 18)
    slow = _rolling_slope(x, 308)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=70, adjust=False).mean() * 1.1375 + 0.0003732 * anchor

def f07_dsi_132_accel_v132(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=25, w2=319, w3=83, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(319, min_periods=max(319//3, 2)).max()
    trough = x.rolling(25, min_periods=max(25//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.151875 + 0.0003733 * anchor

def f07_dsi_133_jerk_v133(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=32, w2=330, w3=96, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(32)
    rank = change.rolling(330, min_periods=max(330//3, 2)).rank(pct=True)
    persistence = change.rolling(96, min_periods=max(96//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1758 * persistence + 0.0003734 * anchor

def f07_dsi_134_accel_v134(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=39, w2=341, w3=109, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(39, min_periods=max(39//3, 2)).std()
    vol_slow = ret.rolling(341, min_periods=max(341//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.180625 + 0.0003735 * anchor

def f07_dsi_135_jerk_v135(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=46, w2=352, w3=122, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(352, min_periods=max(352//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 46)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.191 * slope + 0.0003736 * anchor

def f07_dsi_136_accel_v136(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=53, w2=363, w3=135, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(53)
    drag = impulse.rolling(363, min_periods=max(363//3, 2)).mean()
    noise = impulse.abs().rolling(135, min_periods=max(135//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.209375 + 0.0003737 * anchor

def f07_dsi_137_jerk_v137(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=60, w2=374, w3=148, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 60)
    acceleration = _rolling_slope(velocity, 374)
    curvature = _rolling_slope(acceleration, 148)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2062 * acceleration + 0.0003738 * anchor

def f07_dsi_138_accel_v138(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=67, w2=385, w3=161, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(67, min_periods=max(67//3, 2)).mean(), upside.rolling(385, min_periods=max(385//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.238125 + 0.0003739 * anchor

def f07_dsi_139_jerk_v139(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=74, w2=396, w3=174, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(396, min_periods=max(396//3, 2)).max()
    rebound = x - x.rolling(74, min_periods=max(74//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2214 * _rolling_slope(draw, 174) + 0.000374 * anchor

def f07_dsi_140_accel_v140(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=81, w2=407, w3=187, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 81)
    baseline = trend.rolling(407, min_periods=max(407//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(187, min_periods=max(187//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.266875 + 0.0003741 * anchor

def f07_dsi_141_jerk_v141(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=88, w2=418, w3=200, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 88)
    slow = _rolling_slope(x, 418)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=200, adjust=False).mean() * 1.28125 + 0.0003742 * anchor

def f07_dsi_142_accel_v142(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=95, w2=429, w3=213, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(429, min_periods=max(429//3, 2)).max()
    trough = x.rolling(95, min_periods=max(95//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.295625 + 0.0003743 * anchor

def f07_dsi_143_jerk_v143(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=102, w2=440, w3=226, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(102)
    rank = change.rolling(440, min_periods=max(440//3, 2)).rank(pct=True)
    persistence = change.rolling(226, min_periods=max(226//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2518 * persistence + 0.0003744 * anchor

def f07_dsi_144_accel_v144(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=109, w2=451, w3=239, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(109, min_periods=max(109//3, 2)).std()
    vol_slow = ret.rolling(451, min_periods=max(451//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.324375 + 0.0003745 * anchor

def f07_dsi_145_jerk_v145(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=116, w2=462, w3=252, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(462, min_periods=max(462//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 116)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.267 * slope + 0.0003746 * anchor

def f07_dsi_146_accel_v146(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=123, w2=473, w3=265, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(123)
    drag = impulse.rolling(473, min_periods=max(473//3, 2)).mean()
    noise = impulse.abs().rolling(265, min_periods=max(265//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.353125 + 0.0003747 * anchor

def f07_dsi_147_jerk_v147(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=130, w2=484, w3=278, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 130)
    acceleration = _rolling_slope(velocity, 484)
    curvature = _rolling_slope(acceleration, 278)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2822 * acceleration + 0.0003748 * anchor

def f07_dsi_148_accel_v148(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=137, w2=495, w3=291, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(137, min_periods=max(137//3, 2)).mean(), upside.rolling(495, min_periods=max(495//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.381875 + 0.0003749 * anchor

def f07_dsi_149_jerk_v149(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=144, w2=506, w3=304, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(506, min_periods=max(506//3, 2)).max()
    rebound = x - x.rolling(144, min_periods=max(144//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2974 * _rolling_slope(draw, 304) + 0.000375 * anchor

def f07_dsi_150_accel_v150(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=151, w2=14, w3=317, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 151)
    baseline = trend.rolling(14, min_periods=max(14//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(317, min_periods=max(317//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.410625 + 0.0003751 * anchor
