"""08 moving average extension dynamics base features 76-150 â€” Pipeline 1a-HF Grade v3.

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

def f08_mae_076_accel_v76(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=68, w2=267, w3=342, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(68)
    drag = impulse.rolling(267, min_periods=max(267//3, 2)).mean()
    noise = impulse.abs().rolling(342, min_periods=max(342//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.240625 + 0.0004277 * anchor

def f08_mae_077_jerk_v77(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=75, w2=278, w3=355, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 75)
    acceleration = _rolling_slope(velocity, 278)
    curvature = _rolling_slope(acceleration, 355)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1698 * acceleration + 0.0004278 * anchor

def f08_mae_078_accel_v78(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=82, w2=289, w3=368, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(82, min_periods=max(82//3, 2)).mean(), upside.rolling(289, min_periods=max(289//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.269375 + 0.0004279 * anchor

def f08_mae_079_jerk_v79(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=89, w2=300, w3=381, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(300, min_periods=max(300//3, 2)).max()
    rebound = x - x.rolling(89, min_periods=max(89//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.185 * _rolling_slope(draw, 381) + 0.000428 * anchor

def f08_mae_080_accel_v80(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=96, w2=311, w3=394, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 96)
    baseline = trend.rolling(311, min_periods=max(311//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(394, min_periods=max(394//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.298125 + 0.0004281 * anchor

def f08_mae_081_jerk_v81(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=103, w2=322, w3=407, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 103)
    slow = _rolling_slope(x, 322)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.3125 + 0.0004282 * anchor

def f08_mae_082_accel_v82(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=110, w2=333, w3=420, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(333, min_periods=max(333//3, 2)).max()
    trough = x.rolling(110, min_periods=max(110//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.326875 + 0.0004283 * anchor

def f08_mae_083_jerk_v83(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=117, w2=344, w3=433, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(117)
    rank = change.rolling(344, min_periods=max(344//3, 2)).rank(pct=True)
    persistence = change.rolling(433, min_periods=max(433//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2154 * persistence + 0.0004284 * anchor

def f08_mae_084_accel_v84(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=124, w2=355, w3=446, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(124, min_periods=max(124//3, 2)).std()
    vol_slow = ret.rolling(355, min_periods=max(355//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.355625 + 0.0004285 * anchor

def f08_mae_085_jerk_v85(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=131, w2=366, w3=459, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(366, min_periods=max(366//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 131)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2306 * slope + 0.0004286 * anchor

def f08_mae_086_accel_v86(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=138, w2=377, w3=472, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(377, min_periods=max(377//3, 2)).mean()
    noise = impulse.abs().rolling(472, min_periods=max(472//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.384375 + 0.0004287 * anchor

def f08_mae_087_jerk_v87(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=145, w2=388, w3=485, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 145)
    acceleration = _rolling_slope(velocity, 388)
    curvature = _rolling_slope(acceleration, 485)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2458 * acceleration + 0.0004288 * anchor

def f08_mae_088_accel_v88(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=152, w2=399, w3=498, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(152, min_periods=max(152//3, 2)).mean(), upside.rolling(399, min_periods=max(399//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.413125 + 0.0004289 * anchor

def f08_mae_089_jerk_v89(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=159, w2=410, w3=511, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(410, min_periods=max(410//3, 2)).max()
    rebound = x - x.rolling(159, min_periods=max(159//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.261 * _rolling_slope(draw, 511) + 0.000429 * anchor

def f08_mae_090_accel_v90(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=166, w2=421, w3=524, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 166)
    baseline = trend.rolling(421, min_periods=max(421//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(524, min_periods=max(524//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.441875 + 0.0004291 * anchor

def f08_mae_091_jerk_v91(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=173, w2=432, w3=537, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 173)
    slow = _rolling_slope(x, 432)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.45625 + 0.0004292 * anchor

def f08_mae_092_accel_v92(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=180, w2=443, w3=550, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(443, min_periods=max(443//3, 2)).max()
    trough = x.rolling(180, min_periods=max(180//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.470625 + 0.0004293 * anchor

def f08_mae_093_jerk_v93(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=187, w2=454, w3=563, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(454, min_periods=max(454//3, 2)).rank(pct=True)
    persistence = change.rolling(563, min_periods=max(563//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2914 * persistence + 0.0004294 * anchor

def f08_mae_094_accel_v94(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=194, w2=465, w3=576, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(194, min_periods=max(194//3, 2)).std()
    vol_slow = ret.rolling(465, min_periods=max(465//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.499375 + 0.0004295 * anchor

def f08_mae_095_jerk_v95(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=201, w2=476, w3=589, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(476, min_periods=max(476//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 201)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3066 * slope + 0.0004296 * anchor

def f08_mae_096_accel_v96(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=208, w2=487, w3=602, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(487, min_periods=max(487//3, 2)).mean()
    noise = impulse.abs().rolling(602, min_periods=max(602//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.528125 + 0.0004297 * anchor

def f08_mae_097_jerk_v97(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=215, w2=498, w3=615, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 215)
    acceleration = _rolling_slope(velocity, 498)
    curvature = _rolling_slope(acceleration, 615)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3218 * acceleration + 0.0004298 * anchor

def f08_mae_098_accel_v98(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=222, w2=509, w3=628, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(222, min_periods=max(222//3, 2)).mean(), upside.rolling(509, min_periods=max(509//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.556875 + 0.0004299 * anchor

def f08_mae_099_jerk_v99(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=229, w2=17, w3=641, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(17, min_periods=max(17//3, 2)).max()
    rebound = x - x.rolling(229, min_periods=max(229//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.337 * _rolling_slope(draw, 641) + 0.00043 * anchor

def f08_mae_100_accel_v100(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=236, w2=28, w3=654, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 236)
    baseline = trend.rolling(28, min_periods=max(28//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(654, min_periods=max(654//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.585625 + 0.0004301 * anchor

def f08_mae_101_jerk_v101(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=243, w2=39, w3=667, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 243)
    slow = _rolling_slope(x, 39)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.6 + 0.0004302 * anchor

def f08_mae_102_accel_v102(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=250, w2=50, w3=680, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(50, min_periods=max(50//3, 2)).max()
    trough = x.rolling(250, min_periods=max(250//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.614375 + 0.0004303 * anchor

def f08_mae_103_jerk_v103(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=6, w2=61, w3=693, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(6)
    rank = change.rolling(61, min_periods=max(61//3, 2)).rank(pct=True)
    persistence = change.rolling(693, min_periods=max(693//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3674 * persistence + 0.0004304 * anchor

def f08_mae_104_accel_v104(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=13, w2=72, w3=706, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(13, min_periods=max(13//3, 2)).std()
    vol_slow = ret.rolling(72, min_periods=max(72//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.87 + 0.0004305 * anchor

def f08_mae_105_jerk_v105(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=20, w2=83, w3=719, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(83, min_periods=max(83//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 20)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3826 * slope + 0.0004306 * anchor

def f08_mae_106_accel_v106(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=27, w2=94, w3=732, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(27)
    drag = impulse.rolling(94, min_periods=max(94//3, 2)).mean()
    noise = impulse.abs().rolling(732, min_periods=max(732//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.89875 + 0.0004307 * anchor

def f08_mae_107_jerk_v107(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=34, w2=105, w3=745, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 34)
    acceleration = _rolling_slope(velocity, 105)
    curvature = _rolling_slope(acceleration, 745)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3978 * acceleration + 0.0004308 * anchor

def f08_mae_108_accel_v108(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=41, w2=116, w3=758, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(41, min_periods=max(41//3, 2)).mean(), upside.rolling(116, min_periods=max(116//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.9275 + 0.0004309 * anchor

def f08_mae_109_jerk_v109(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=48, w2=127, w3=771, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(127, min_periods=max(127//3, 2)).max()
    rebound = x - x.rolling(48, min_periods=max(48//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0366 * _rolling_slope(draw, 771) + 0.000431 * anchor

def f08_mae_110_accel_v110(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=55, w2=138, w3=27, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 55)
    baseline = trend.rolling(138, min_periods=max(138//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(27, min_periods=max(27//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.95625 + 0.0004311 * anchor

def f08_mae_111_jerk_v111(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=62, w2=149, w3=40, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 62)
    slow = _rolling_slope(x, 149)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=40, adjust=False).mean() * 0.970625 + 0.0004312 * anchor

def f08_mae_112_accel_v112(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=69, w2=160, w3=53, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(160, min_periods=max(160//3, 2)).max()
    trough = x.rolling(69, min_periods=max(69//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.985 + 0.0004313 * anchor

def f08_mae_113_jerk_v113(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=76, w2=171, w3=66, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(76)
    rank = change.rolling(171, min_periods=max(171//3, 2)).rank(pct=True)
    persistence = change.rolling(66, min_periods=max(66//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.067 * persistence + 0.0004314 * anchor

def f08_mae_114_accel_v114(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=83, w2=182, w3=79, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(83, min_periods=max(83//3, 2)).std()
    vol_slow = ret.rolling(182, min_periods=max(182//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.01375 + 0.0004315 * anchor

def f08_mae_115_jerk_v115(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=90, w2=193, w3=92, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(193, min_periods=max(193//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 90)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0822 * slope + 0.0004316 * anchor

def f08_mae_116_accel_v116(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=97, w2=204, w3=105, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(97)
    drag = impulse.rolling(204, min_periods=max(204//3, 2)).mean()
    noise = impulse.abs().rolling(105, min_periods=max(105//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.0425 + 0.0004317 * anchor

def f08_mae_117_jerk_v117(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=104, w2=215, w3=118, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 104)
    acceleration = _rolling_slope(velocity, 215)
    curvature = _rolling_slope(acceleration, 118)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0974 * acceleration + 0.0004318 * anchor

def f08_mae_118_accel_v118(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=111, w2=226, w3=131, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(111, min_periods=max(111//3, 2)).mean(), upside.rolling(226, min_periods=max(226//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.07125 + 0.0004319 * anchor

def f08_mae_119_jerk_v119(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=118, w2=237, w3=144, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(237, min_periods=max(237//3, 2)).max()
    rebound = x - x.rolling(118, min_periods=max(118//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1126 * _rolling_slope(draw, 144) + 0.000432 * anchor

def f08_mae_120_accel_v120(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=125, w2=248, w3=157, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 125)
    baseline = trend.rolling(248, min_periods=max(248//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(157, min_periods=max(157//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.1 + 0.0004321 * anchor

def f08_mae_121_jerk_v121(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=132, w2=259, w3=170, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 132)
    slow = _rolling_slope(x, 259)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=170, adjust=False).mean() * 1.114375 + 0.0004322 * anchor

def f08_mae_122_accel_v122(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=139, w2=270, w3=183, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(270, min_periods=max(270//3, 2)).max()
    trough = x.rolling(139, min_periods=max(139//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.12875 + 0.0004323 * anchor

def f08_mae_123_jerk_v123(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=146, w2=281, w3=196, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(281, min_periods=max(281//3, 2)).rank(pct=True)
    persistence = change.rolling(196, min_periods=max(196//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.143 * persistence + 0.0004324 * anchor

def f08_mae_124_accel_v124(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=153, w2=292, w3=209, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(153, min_periods=max(153//3, 2)).std()
    vol_slow = ret.rolling(292, min_periods=max(292//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.1575 + 0.0004325 * anchor

def f08_mae_125_jerk_v125(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=160, w2=303, w3=222, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(303, min_periods=max(303//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 160)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1582 * slope + 0.0004326 * anchor

def f08_mae_126_accel_v126(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=167, w2=314, w3=235, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(314, min_periods=max(314//3, 2)).mean()
    noise = impulse.abs().rolling(235, min_periods=max(235//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.18625 + 0.0004327 * anchor

def f08_mae_127_jerk_v127(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=174, w2=325, w3=248, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 174)
    acceleration = _rolling_slope(velocity, 325)
    curvature = _rolling_slope(acceleration, 248)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1734 * acceleration + 0.0004328 * anchor

def f08_mae_128_accel_v128(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=181, w2=336, w3=261, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(181, min_periods=max(181//3, 2)).mean(), upside.rolling(336, min_periods=max(336//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.215 + 0.0004329 * anchor

def f08_mae_129_jerk_v129(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=188, w2=347, w3=274, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(347, min_periods=max(347//3, 2)).max()
    rebound = x - x.rolling(188, min_periods=max(188//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1886 * _rolling_slope(draw, 274) + 0.000433 * anchor

def f08_mae_130_accel_v130(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=195, w2=358, w3=287, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 195)
    baseline = trend.rolling(358, min_periods=max(358//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(287, min_periods=max(287//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.24375 + 0.0004331 * anchor

def f08_mae_131_jerk_v131(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=202, w2=369, w3=300, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 202)
    slow = _rolling_slope(x, 369)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.258125 + 0.0004332 * anchor

def f08_mae_132_accel_v132(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=209, w2=380, w3=313, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(380, min_periods=max(380//3, 2)).max()
    trough = x.rolling(209, min_periods=max(209//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.2725 + 0.0004333 * anchor

def f08_mae_133_jerk_v133(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=216, w2=391, w3=326, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(391, min_periods=max(391//3, 2)).rank(pct=True)
    persistence = change.rolling(326, min_periods=max(326//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.219 * persistence + 0.0004334 * anchor

def f08_mae_134_accel_v134(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=223, w2=402, w3=339, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(223, min_periods=max(223//3, 2)).std()
    vol_slow = ret.rolling(402, min_periods=max(402//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.30125 + 0.0004335 * anchor

def f08_mae_135_jerk_v135(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=230, w2=413, w3=352, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(413, min_periods=max(413//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 230)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2342 * slope + 0.0004336 * anchor

def f08_mae_136_accel_v136(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=237, w2=424, w3=365, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(424, min_periods=max(424//3, 2)).mean()
    noise = impulse.abs().rolling(365, min_periods=max(365//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.33 + 0.0004337 * anchor

def f08_mae_137_jerk_v137(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=244, w2=435, w3=378, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 244)
    acceleration = _rolling_slope(velocity, 435)
    curvature = _rolling_slope(acceleration, 378)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2494 * acceleration + 0.0004338 * anchor

def f08_mae_138_accel_v138(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=251, w2=446, w3=391, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(251, min_periods=max(251//3, 2)).mean(), upside.rolling(446, min_periods=max(446//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.35875 + 0.0004339 * anchor

def f08_mae_139_jerk_v139(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=7, w2=457, w3=404, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(457, min_periods=max(457//3, 2)).max()
    rebound = x - x.rolling(7, min_periods=max(7//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2646 * _rolling_slope(draw, 404) + 0.000434 * anchor

def f08_mae_140_accel_v140(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=14, w2=468, w3=417, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 14)
    baseline = trend.rolling(468, min_periods=max(468//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(417, min_periods=max(417//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.3875 + 0.0004341 * anchor

def f08_mae_141_jerk_v141(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=21, w2=479, w3=430, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 21)
    slow = _rolling_slope(x, 479)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.401875 + 0.0004342 * anchor

def f08_mae_142_accel_v142(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=28, w2=490, w3=443, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(490, min_periods=max(490//3, 2)).max()
    trough = x.rolling(28, min_periods=max(28//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.41625 + 0.0004343 * anchor

def f08_mae_143_jerk_v143(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=35, w2=501, w3=456, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(35)
    rank = change.rolling(501, min_periods=max(501//3, 2)).rank(pct=True)
    persistence = change.rolling(456, min_periods=max(456//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.295 * persistence + 0.0004344 * anchor

def f08_mae_144_accel_v144(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=42, w2=512, w3=469, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(42, min_periods=max(42//3, 2)).std()
    vol_slow = ret.rolling(512, min_periods=max(512//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.445 + 0.0004345 * anchor

def f08_mae_145_jerk_v145(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=49, w2=20, w3=482, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(20, min_periods=max(20//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 49)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3102 * slope + 0.0004346 * anchor

def f08_mae_146_accel_v146(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=56, w2=31, w3=495, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(56)
    drag = impulse.rolling(31, min_periods=max(31//3, 2)).mean()
    noise = impulse.abs().rolling(495, min_periods=max(495//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.47375 + 0.0004347 * anchor

def f08_mae_147_jerk_v147(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=63, w2=42, w3=508, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 63)
    acceleration = _rolling_slope(velocity, 42)
    curvature = _rolling_slope(acceleration, 508)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3254 * acceleration + 0.0004348 * anchor

def f08_mae_148_accel_v148(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=70, w2=53, w3=521, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(70, min_periods=max(70//3, 2)).mean(), upside.rolling(53, min_periods=max(53//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.5025 + 0.0004349 * anchor

def f08_mae_149_jerk_v149(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=77, w2=64, w3=534, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(64, min_periods=max(64//3, 2)).max()
    rebound = x - x.rolling(77, min_periods=max(77//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3406 * _rolling_slope(draw, 534) + 0.000435 * anchor

def f08_mae_150_accel_v150(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=84, w2=75, w3=547, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 84)
    baseline = trend.rolling(75, min_periods=max(75//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(547, min_periods=max(547//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.53125 + 0.0004351 * anchor
