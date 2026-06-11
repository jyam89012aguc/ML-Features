"""38 distribution rolling top signature base features 76-150 â€” Pipeline 1a-HF Grade v3.

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

def f38_drts_076_accel_v76(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=250, w2=146, w3=659, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(146, min_periods=max(146//3, 2)).mean()
    noise = impulse.abs().rolling(659, min_periods=max(659//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.114375 + 0.0022877 * anchor

def f38_drts_077_jerk_v77(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=6, w2=157, w3=672, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 6)
    acceleration = _rolling_slope(velocity, 157)
    curvature = _rolling_slope(acceleration, 672)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3798 * acceleration + 0.0022878 * anchor

def f38_drts_078_accel_v78(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=13, w2=168, w3=685, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(13, min_periods=max(13//3, 2)).mean(), upside.rolling(168, min_periods=max(168//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.143125 + 0.0022879 * anchor

def f38_drts_079_jerk_v79(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=20, w2=179, w3=698, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(179, min_periods=max(179//3, 2)).max()
    rebound = x - x.rolling(20, min_periods=max(20//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.395 * _rolling_slope(draw, 698) + 0.002288 * anchor

def f38_drts_080_accel_v80(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=27, w2=190, w3=711, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 27)
    baseline = trend.rolling(190, min_periods=max(190//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(711, min_periods=max(711//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.171875 + 0.0022881 * anchor

def f38_drts_081_jerk_v81(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=34, w2=201, w3=724, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 34)
    slow = _rolling_slope(x, 201)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.18625 + 0.0022882 * anchor

def f38_drts_082_accel_v82(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=41, w2=212, w3=737, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(212, min_periods=max(212//3, 2)).max()
    trough = x.rolling(41, min_periods=max(41//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.200625 + 0.0022883 * anchor

def f38_drts_083_jerk_v83(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=48, w2=223, w3=750, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(48)
    rank = change.rolling(223, min_periods=max(223//3, 2)).rank(pct=True)
    persistence = change.rolling(750, min_periods=max(750//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.049 * persistence + 0.0022884 * anchor

def f38_drts_084_accel_v84(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=55, w2=234, w3=763, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(55, min_periods=max(55//3, 2)).std()
    vol_slow = ret.rolling(234, min_periods=max(234//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.229375 + 0.0022885 * anchor

def f38_drts_085_jerk_v85(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=62, w2=245, w3=19, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(245, min_periods=max(245//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 62)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0642 * slope + 0.0022886 * anchor

def f38_drts_086_accel_v86(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=69, w2=256, w3=32, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(69)
    drag = impulse.rolling(256, min_periods=max(256//3, 2)).mean()
    noise = impulse.abs().rolling(32, min_periods=max(32//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.258125 + 0.0022887 * anchor

def f38_drts_087_jerk_v87(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=76, w2=267, w3=45, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 76)
    acceleration = _rolling_slope(velocity, 267)
    curvature = _rolling_slope(acceleration, 45)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0794 * acceleration + 0.0022888 * anchor

def f38_drts_088_accel_v88(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=83, w2=278, w3=58, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(83, min_periods=max(83//3, 2)).mean(), upside.rolling(278, min_periods=max(278//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(58) * 1.286875 + 0.0022889 * anchor

def f38_drts_089_jerk_v89(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=90, w2=289, w3=71, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(289, min_periods=max(289//3, 2)).max()
    rebound = x - x.rolling(90, min_periods=max(90//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0946 * _rolling_slope(draw, 71) + 0.002289 * anchor

def f38_drts_090_accel_v90(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=97, w2=300, w3=84, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 97)
    baseline = trend.rolling(300, min_periods=max(300//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(84, min_periods=max(84//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.315625 + 0.0022891 * anchor

def f38_drts_091_jerk_v91(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=104, w2=311, w3=97, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 104)
    slow = _rolling_slope(x, 311)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=97, adjust=False).mean() * 1.33 + 0.0022892 * anchor

def f38_drts_092_accel_v92(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=111, w2=322, w3=110, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(322, min_periods=max(322//3, 2)).max()
    trough = x.rolling(111, min_periods=max(111//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.344375 + 0.0022893 * anchor

def f38_drts_093_jerk_v93(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=118, w2=333, w3=123, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(118)
    rank = change.rolling(333, min_periods=max(333//3, 2)).rank(pct=True)
    persistence = change.rolling(123, min_periods=max(123//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.125 * persistence + 0.0022894 * anchor

def f38_drts_094_accel_v94(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=125, w2=344, w3=136, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(125, min_periods=max(125//3, 2)).std()
    vol_slow = ret.rolling(344, min_periods=max(344//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.373125 + 0.0022895 * anchor

def f38_drts_095_jerk_v95(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=132, w2=355, w3=149, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(355, min_periods=max(355//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 132)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1402 * slope + 0.0022896 * anchor

def f38_drts_096_accel_v96(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=139, w2=366, w3=162, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(366, min_periods=max(366//3, 2)).mean()
    noise = impulse.abs().rolling(162, min_periods=max(162//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.401875 + 0.0022897 * anchor

def f38_drts_097_jerk_v97(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=146, w2=377, w3=175, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 146)
    acceleration = _rolling_slope(velocity, 377)
    curvature = _rolling_slope(acceleration, 175)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1554 * acceleration + 0.0022898 * anchor

def f38_drts_098_accel_v98(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=153, w2=388, w3=188, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(153, min_periods=max(153//3, 2)).mean(), upside.rolling(388, min_periods=max(388//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.430625 + 0.0022899 * anchor

def f38_drts_099_jerk_v99(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=160, w2=399, w3=201, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(399, min_periods=max(399//3, 2)).max()
    rebound = x - x.rolling(160, min_periods=max(160//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1706 * _rolling_slope(draw, 201) + 0.00229 * anchor

def f38_drts_100_accel_v100(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=167, w2=410, w3=214, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 167)
    baseline = trend.rolling(410, min_periods=max(410//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(214, min_periods=max(214//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.459375 + 0.0022901 * anchor

def f38_drts_101_jerk_v101(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=174, w2=421, w3=227, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 174)
    slow = _rolling_slope(x, 421)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=227, adjust=False).mean() * 1.47375 + 0.0022902 * anchor

def f38_drts_102_accel_v102(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=181, w2=432, w3=240, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(432, min_periods=max(432//3, 2)).max()
    trough = x.rolling(181, min_periods=max(181//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.488125 + 0.0022903 * anchor

def f38_drts_103_jerk_v103(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=188, w2=443, w3=253, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(443, min_periods=max(443//3, 2)).rank(pct=True)
    persistence = change.rolling(253, min_periods=max(253//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.201 * persistence + 0.0022904 * anchor

def f38_drts_104_accel_v104(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=195, w2=454, w3=266, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(195, min_periods=max(195//3, 2)).std()
    vol_slow = ret.rolling(454, min_periods=max(454//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.516875 + 0.0022905 * anchor

def f38_drts_105_jerk_v105(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=202, w2=465, w3=279, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(465, min_periods=max(465//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 202)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2162 * slope + 0.0022906 * anchor

def f38_drts_106_accel_v106(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=209, w2=476, w3=292, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(476, min_periods=max(476//3, 2)).mean()
    noise = impulse.abs().rolling(292, min_periods=max(292//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.545625 + 0.0022907 * anchor

def f38_drts_107_jerk_v107(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=216, w2=487, w3=305, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 216)
    acceleration = _rolling_slope(velocity, 487)
    curvature = _rolling_slope(acceleration, 305)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2314 * acceleration + 0.0022908 * anchor

def f38_drts_108_accel_v108(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=223, w2=498, w3=318, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(223, min_periods=max(223//3, 2)).mean(), upside.rolling(498, min_periods=max(498//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.574375 + 0.0022909 * anchor

def f38_drts_109_jerk_v109(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=230, w2=509, w3=331, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(509, min_periods=max(509//3, 2)).max()
    rebound = x - x.rolling(230, min_periods=max(230//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2466 * _rolling_slope(draw, 331) + 0.002291 * anchor

def f38_drts_110_accel_v110(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=237, w2=17, w3=344, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 237)
    baseline = trend.rolling(17, min_periods=max(17//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(344, min_periods=max(344//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.603125 + 0.0022911 * anchor

def f38_drts_111_jerk_v111(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=244, w2=28, w3=357, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 244)
    slow = _rolling_slope(x, 28)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.6175 + 0.0022912 * anchor

def f38_drts_112_accel_v112(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=251, w2=39, w3=370, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(39, min_periods=max(39//3, 2)).max()
    trough = x.rolling(251, min_periods=max(251//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.85875 + 0.0022913 * anchor

def f38_drts_113_jerk_v113(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=7, w2=50, w3=383, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(7)
    rank = change.rolling(50, min_periods=max(50//3, 2)).rank(pct=True)
    persistence = change.rolling(383, min_periods=max(383//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.277 * persistence + 0.0022914 * anchor

def f38_drts_114_accel_v114(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=14, w2=61, w3=396, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(14, min_periods=max(14//3, 2)).std()
    vol_slow = ret.rolling(61, min_periods=max(61//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.8875 + 0.0022915 * anchor

def f38_drts_115_jerk_v115(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=21, w2=72, w3=409, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(72, min_periods=max(72//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 21)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2922 * slope + 0.0022916 * anchor

def f38_drts_116_accel_v116(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=28, w2=83, w3=422, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(28)
    drag = impulse.rolling(83, min_periods=max(83//3, 2)).mean()
    noise = impulse.abs().rolling(422, min_periods=max(422//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.91625 + 0.0022917 * anchor

def f38_drts_117_jerk_v117(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=35, w2=94, w3=435, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 35)
    acceleration = _rolling_slope(velocity, 94)
    curvature = _rolling_slope(acceleration, 435)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3074 * acceleration + 0.0022918 * anchor

def f38_drts_118_accel_v118(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=42, w2=105, w3=448, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(42, min_periods=max(42//3, 2)).mean(), upside.rolling(105, min_periods=max(105//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.945 + 0.0022919 * anchor

def f38_drts_119_jerk_v119(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=49, w2=116, w3=461, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(116, min_periods=max(116//3, 2)).max()
    rebound = x - x.rolling(49, min_periods=max(49//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3226 * _rolling_slope(draw, 461) + 0.002292 * anchor

def f38_drts_120_accel_v120(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=56, w2=127, w3=474, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 56)
    baseline = trend.rolling(127, min_periods=max(127//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(474, min_periods=max(474//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.97375 + 0.0022921 * anchor

def f38_drts_121_jerk_v121(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=63, w2=138, w3=487, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 63)
    slow = _rolling_slope(x, 138)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.988125 + 0.0022922 * anchor

def f38_drts_122_accel_v122(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=70, w2=149, w3=500, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(149, min_periods=max(149//3, 2)).max()
    trough = x.rolling(70, min_periods=max(70//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.0025 + 0.0022923 * anchor

def f38_drts_123_jerk_v123(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=77, w2=160, w3=513, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(77)
    rank = change.rolling(160, min_periods=max(160//3, 2)).rank(pct=True)
    persistence = change.rolling(513, min_periods=max(513//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.353 * persistence + 0.0022924 * anchor

def f38_drts_124_accel_v124(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=84, w2=171, w3=526, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(84, min_periods=max(84//3, 2)).std()
    vol_slow = ret.rolling(171, min_periods=max(171//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.03125 + 0.0022925 * anchor

def f38_drts_125_jerk_v125(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=91, w2=182, w3=539, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(182, min_periods=max(182//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 91)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3682 * slope + 0.0022926 * anchor

def f38_drts_126_accel_v126(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=98, w2=193, w3=552, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(98)
    drag = impulse.rolling(193, min_periods=max(193//3, 2)).mean()
    noise = impulse.abs().rolling(552, min_periods=max(552//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.06 + 0.0022927 * anchor

def f38_drts_127_jerk_v127(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=105, w2=204, w3=565, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 105)
    acceleration = _rolling_slope(velocity, 204)
    curvature = _rolling_slope(acceleration, 565)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3834 * acceleration + 0.0022928 * anchor

def f38_drts_128_accel_v128(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=112, w2=215, w3=578, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(112, min_periods=max(112//3, 2)).mean(), upside.rolling(215, min_periods=max(215//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.08875 + 0.0022929 * anchor

def f38_drts_129_jerk_v129(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=119, w2=226, w3=591, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(226, min_periods=max(226//3, 2)).max()
    rebound = x - x.rolling(119, min_periods=max(119//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3986 * _rolling_slope(draw, 591) + 0.002293 * anchor

def f38_drts_130_accel_v130(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=126, w2=237, w3=604, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 126)
    baseline = trend.rolling(237, min_periods=max(237//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(604, min_periods=max(604//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.1175 + 0.0022931 * anchor

def f38_drts_131_jerk_v131(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=133, w2=248, w3=617, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 133)
    slow = _rolling_slope(x, 248)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.131875 + 0.0022932 * anchor

def f38_drts_132_accel_v132(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=140, w2=259, w3=630, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(259, min_periods=max(259//3, 2)).max()
    trough = x.rolling(140, min_periods=max(140//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.14625 + 0.0022933 * anchor

def f38_drts_133_jerk_v133(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=147, w2=270, w3=643, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(270, min_periods=max(270//3, 2)).rank(pct=True)
    persistence = change.rolling(643, min_periods=max(643//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0526 * persistence + 0.0022934 * anchor

def f38_drts_134_accel_v134(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=154, w2=281, w3=656, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(154, min_periods=max(154//3, 2)).std()
    vol_slow = ret.rolling(281, min_periods=max(281//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.175 + 0.0022935 * anchor

def f38_drts_135_jerk_v135(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=161, w2=292, w3=669, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(292, min_periods=max(292//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 161)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0678 * slope + 0.0022936 * anchor

def f38_drts_136_accel_v136(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=168, w2=303, w3=682, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(303, min_periods=max(303//3, 2)).mean()
    noise = impulse.abs().rolling(682, min_periods=max(682//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.20375 + 0.0022937 * anchor

def f38_drts_137_jerk_v137(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=175, w2=314, w3=695, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 175)
    acceleration = _rolling_slope(velocity, 314)
    curvature = _rolling_slope(acceleration, 695)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.083 * acceleration + 0.0022938 * anchor

def f38_drts_138_accel_v138(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=182, w2=325, w3=708, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(182, min_periods=max(182//3, 2)).mean(), upside.rolling(325, min_periods=max(325//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.2325 + 0.0022939 * anchor

def f38_drts_139_jerk_v139(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=189, w2=336, w3=721, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(336, min_periods=max(336//3, 2)).max()
    rebound = x - x.rolling(189, min_periods=max(189//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0982 * _rolling_slope(draw, 721) + 0.002294 * anchor

def f38_drts_140_accel_v140(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=196, w2=347, w3=734, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 196)
    baseline = trend.rolling(347, min_periods=max(347//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(734, min_periods=max(734//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.26125 + 0.0022941 * anchor

def f38_drts_141_jerk_v141(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=203, w2=358, w3=747, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 203)
    slow = _rolling_slope(x, 358)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.275625 + 0.0022942 * anchor

def f38_drts_142_accel_v142(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=210, w2=369, w3=760, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(369, min_periods=max(369//3, 2)).max()
    trough = x.rolling(210, min_periods=max(210//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.29 + 0.0022943 * anchor

def f38_drts_143_jerk_v143(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=217, w2=380, w3=16, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(380, min_periods=max(380//3, 2)).rank(pct=True)
    persistence = change.rolling(16, min_periods=max(16//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1286 * persistence + 0.0022944 * anchor

def f38_drts_144_accel_v144(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=224, w2=391, w3=29, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(224, min_periods=max(224//3, 2)).std()
    vol_slow = ret.rolling(391, min_periods=max(391//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.31875 + 0.0022945 * anchor

def f38_drts_145_jerk_v145(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=231, w2=402, w3=42, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(402, min_periods=max(402//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 231)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1438 * slope + 0.0022946 * anchor

def f38_drts_146_accel_v146(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=238, w2=413, w3=55, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(413, min_periods=max(413//3, 2)).mean()
    noise = impulse.abs().rolling(55, min_periods=max(55//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.3475 + 0.0022947 * anchor

def f38_drts_147_jerk_v147(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=245, w2=424, w3=68, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 245)
    acceleration = _rolling_slope(velocity, 424)
    curvature = _rolling_slope(acceleration, 68)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.159 * acceleration + 0.0022948 * anchor

def f38_drts_148_accel_v148(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=252, w2=435, w3=81, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(252, min_periods=max(252//3, 2)).mean(), upside.rolling(435, min_periods=max(435//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(81) * 1.37625 + 0.0022949 * anchor

def f38_drts_149_jerk_v149(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=8, w2=446, w3=94, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(446, min_periods=max(446//3, 2)).max()
    rebound = x - x.rolling(8, min_periods=max(8//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1742 * _rolling_slope(draw, 94) + 0.002295 * anchor

def f38_drts_150_accel_v150(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=15, w2=457, w3=107, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 15)
    baseline = trend.rolling(457, min_periods=max(457//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(107, min_periods=max(107//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.405 + 0.0022951 * anchor
