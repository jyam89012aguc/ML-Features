"""05 volume blowoff at peak d1 first derivative features 376-450 â€” Pipeline 1a-HF Grade v3.

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

def f05_vbp_376_accel_v376_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=110, w2=366, w3=524, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(110)
    drag = impulse.rolling(366, min_periods=max(366//3, 2)).mean()
    noise = impulse.abs().rolling(524, min_periods=max(524//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.325625 + 0.0002777 * anchor
    return base_signal.diff()

def f05_vbp_377_jerk_v377_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=117, w2=377, w3=537, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 117)
    acceleration = _rolling_slope(velocity, 377)
    curvature = _rolling_slope(acceleration, 537)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0618 * acceleration + 0.0002778 * anchor
    return base_signal.diff()

def f05_vbp_378_accel_v378_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=124, w2=388, w3=550, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(124, min_periods=max(124//3, 2)).mean(), upside.rolling(388, min_periods=max(388//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.354375 + 0.0002779 * anchor
    return base_signal.diff()

def f05_vbp_379_jerk_v379_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=131, w2=399, w3=563, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(399, min_periods=max(399//3, 2)).max()
    rebound = x - x.rolling(131, min_periods=max(131//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.077 * _rolling_slope(draw, 563) + 0.000278 * anchor
    return base_signal.diff()

def f05_vbp_380_accel_v380_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=138, w2=410, w3=576, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 138)
    baseline = trend.rolling(410, min_periods=max(410//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(576, min_periods=max(576//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.383125 + 0.0002781 * anchor
    return base_signal.diff()

def f05_vbp_381_jerk_v381_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=145, w2=421, w3=589, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 145)
    slow = _rolling_slope(x, 421)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.3975 + 0.0002782 * anchor
    return base_signal.diff()

def f05_vbp_382_accel_v382_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=152, w2=432, w3=602, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(432, min_periods=max(432//3, 2)).max()
    trough = x.rolling(152, min_periods=max(152//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.411875 + 0.0002783 * anchor
    return base_signal.diff()

def f05_vbp_383_jerk_v383_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=159, w2=443, w3=615, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(443, min_periods=max(443//3, 2)).rank(pct=True)
    persistence = change.rolling(615, min_periods=max(615//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1074 * persistence + 0.0002784 * anchor
    return base_signal.diff()

def f05_vbp_384_accel_v384_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=166, w2=454, w3=628, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(166, min_periods=max(166//3, 2)).std()
    vol_slow = ret.rolling(454, min_periods=max(454//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.440625 + 0.0002785 * anchor
    return base_signal.diff()

def f05_vbp_385_jerk_v385_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=173, w2=465, w3=641, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(465, min_periods=max(465//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 173)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1226 * slope + 0.0002786 * anchor
    return base_signal.diff()

def f05_vbp_386_accel_v386_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=180, w2=476, w3=654, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(476, min_periods=max(476//3, 2)).mean()
    noise = impulse.abs().rolling(654, min_periods=max(654//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.469375 + 0.0002787 * anchor
    return base_signal.diff()

def f05_vbp_387_jerk_v387_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=187, w2=487, w3=667, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 187)
    acceleration = _rolling_slope(velocity, 487)
    curvature = _rolling_slope(acceleration, 667)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1378 * acceleration + 0.0002788 * anchor
    return base_signal.diff()

def f05_vbp_388_accel_v388_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=194, w2=498, w3=680, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(194, min_periods=max(194//3, 2)).mean(), upside.rolling(498, min_periods=max(498//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.498125 + 0.0002789 * anchor
    return base_signal.diff()

def f05_vbp_389_jerk_v389_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=201, w2=509, w3=693, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(509, min_periods=max(509//3, 2)).max()
    rebound = x - x.rolling(201, min_periods=max(201//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.153 * _rolling_slope(draw, 693) + 0.000279 * anchor
    return base_signal.diff()

def f05_vbp_390_accel_v390_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=208, w2=17, w3=706, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 208)
    baseline = trend.rolling(17, min_periods=max(17//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(706, min_periods=max(706//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.526875 + 0.0002791 * anchor
    return base_signal.diff()

def f05_vbp_391_jerk_v391_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=215, w2=28, w3=719, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 215)
    slow = _rolling_slope(x, 28)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.54125 + 0.0002792 * anchor
    return base_signal.diff()

def f05_vbp_392_accel_v392_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=222, w2=39, w3=732, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(39, min_periods=max(39//3, 2)).max()
    trough = x.rolling(222, min_periods=max(222//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.555625 + 0.0002793 * anchor
    return base_signal.diff()

def f05_vbp_393_jerk_v393_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=229, w2=50, w3=745, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(50, min_periods=max(50//3, 2)).rank(pct=True)
    persistence = change.rolling(745, min_periods=max(745//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1834 * persistence + 0.0002794 * anchor
    return base_signal.diff()

def f05_vbp_394_accel_v394_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=236, w2=61, w3=758, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(236, min_periods=max(236//3, 2)).std()
    vol_slow = ret.rolling(61, min_periods=max(61//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.584375 + 0.0002795 * anchor
    return base_signal.diff()

def f05_vbp_395_jerk_v395_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=243, w2=72, w3=771, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(72, min_periods=max(72//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 243)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1986 * slope + 0.0002796 * anchor
    return base_signal.diff()

def f05_vbp_396_accel_v396_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=250, w2=83, w3=27, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(83, min_periods=max(83//3, 2)).mean()
    noise = impulse.abs().rolling(27, min_periods=max(27//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.613125 + 0.0002797 * anchor
    return base_signal.diff()

def f05_vbp_397_jerk_v397_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=6, w2=94, w3=40, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 6)
    acceleration = _rolling_slope(velocity, 94)
    curvature = _rolling_slope(acceleration, 40)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2138 * acceleration + 0.0002798 * anchor
    return base_signal.diff()

def f05_vbp_398_accel_v398_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=13, w2=105, w3=53, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(13, min_periods=max(13//3, 2)).mean(), upside.rolling(105, min_periods=max(105//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(53) * 0.86875 + 0.0002799 * anchor
    return base_signal.diff()

def f05_vbp_399_jerk_v399_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=20, w2=116, w3=66, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(116, min_periods=max(116//3, 2)).max()
    rebound = x - x.rolling(20, min_periods=max(20//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.229 * _rolling_slope(draw, 66) + 0.00028 * anchor
    return base_signal.diff()

def f05_vbp_400_accel_v400_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=27, w2=127, w3=79, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 27)
    baseline = trend.rolling(127, min_periods=max(127//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(79, min_periods=max(79//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.8975 + 0.0002801 * anchor
    return base_signal.diff()

def f05_vbp_401_jerk_v401_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=34, w2=138, w3=92, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 34)
    slow = _rolling_slope(x, 138)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=92, adjust=False).mean() * 0.911875 + 0.0002802 * anchor
    return base_signal.diff()

def f05_vbp_402_accel_v402_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=41, w2=149, w3=105, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(149, min_periods=max(149//3, 2)).max()
    trough = x.rolling(41, min_periods=max(41//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.92625 + 0.0002803 * anchor
    return base_signal.diff()

def f05_vbp_403_jerk_v403_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=48, w2=160, w3=118, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(48)
    rank = change.rolling(160, min_periods=max(160//3, 2)).rank(pct=True)
    persistence = change.rolling(118, min_periods=max(118//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2594 * persistence + 0.0002804 * anchor
    return base_signal.diff()

def f05_vbp_404_accel_v404_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=55, w2=171, w3=131, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(55, min_periods=max(55//3, 2)).std()
    vol_slow = ret.rolling(171, min_periods=max(171//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.955 + 0.0002805 * anchor
    return base_signal.diff()

def f05_vbp_405_jerk_v405_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=62, w2=182, w3=144, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(182, min_periods=max(182//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 62)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2746 * slope + 0.0002806 * anchor
    return base_signal.diff()

def f05_vbp_406_accel_v406_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=69, w2=193, w3=157, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(69)
    drag = impulse.rolling(193, min_periods=max(193//3, 2)).mean()
    noise = impulse.abs().rolling(157, min_periods=max(157//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.98375 + 0.0002807 * anchor
    return base_signal.diff()

def f05_vbp_407_jerk_v407_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=76, w2=204, w3=170, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 76)
    acceleration = _rolling_slope(velocity, 204)
    curvature = _rolling_slope(acceleration, 170)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2898 * acceleration + 0.0002808 * anchor
    return base_signal.diff()

def f05_vbp_408_accel_v408_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=83, w2=215, w3=183, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(83, min_periods=max(83//3, 2)).mean(), upside.rolling(215, min_periods=max(215//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.0125 + 0.0002809 * anchor
    return base_signal.diff()

def f05_vbp_409_jerk_v409_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=90, w2=226, w3=196, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(226, min_periods=max(226//3, 2)).max()
    rebound = x - x.rolling(90, min_periods=max(90//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.305 * _rolling_slope(draw, 196) + 0.000281 * anchor
    return base_signal.diff()

def f05_vbp_410_accel_v410_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=97, w2=237, w3=209, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 97)
    baseline = trend.rolling(237, min_periods=max(237//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(209, min_periods=max(209//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.04125 + 0.0002811 * anchor
    return base_signal.diff()

def f05_vbp_411_jerk_v411_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=104, w2=248, w3=222, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 104)
    slow = _rolling_slope(x, 248)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=222, adjust=False).mean() * 1.055625 + 0.0002812 * anchor
    return base_signal.diff()

def f05_vbp_412_accel_v412_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=111, w2=259, w3=235, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(259, min_periods=max(259//3, 2)).max()
    trough = x.rolling(111, min_periods=max(111//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.07 + 0.0002813 * anchor
    return base_signal.diff()

def f05_vbp_413_jerk_v413_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=118, w2=270, w3=248, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(118)
    rank = change.rolling(270, min_periods=max(270//3, 2)).rank(pct=True)
    persistence = change.rolling(248, min_periods=max(248//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3354 * persistence + 0.0002814 * anchor
    return base_signal.diff()

def f05_vbp_414_accel_v414_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=125, w2=281, w3=261, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(125, min_periods=max(125//3, 2)).std()
    vol_slow = ret.rolling(281, min_periods=max(281//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.09875 + 0.0002815 * anchor
    return base_signal.diff()

def f05_vbp_415_jerk_v415_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=132, w2=292, w3=274, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(292, min_periods=max(292//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 132)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3506 * slope + 0.0002816 * anchor
    return base_signal.diff()

def f05_vbp_416_accel_v416_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=139, w2=303, w3=287, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(303, min_periods=max(303//3, 2)).mean()
    noise = impulse.abs().rolling(287, min_periods=max(287//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.1275 + 0.0002817 * anchor
    return base_signal.diff()

def f05_vbp_417_jerk_v417_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=146, w2=314, w3=300, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 146)
    acceleration = _rolling_slope(velocity, 314)
    curvature = _rolling_slope(acceleration, 300)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3658 * acceleration + 0.0002818 * anchor
    return base_signal.diff()

def f05_vbp_418_accel_v418_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=153, w2=325, w3=313, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(153, min_periods=max(153//3, 2)).mean(), upside.rolling(325, min_periods=max(325//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.15625 + 0.0002819 * anchor
    return base_signal.diff()

def f05_vbp_419_jerk_v419_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=160, w2=336, w3=326, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(336, min_periods=max(336//3, 2)).max()
    rebound = x - x.rolling(160, min_periods=max(160//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.381 * _rolling_slope(draw, 326) + 0.000282 * anchor
    return base_signal.diff()

def f05_vbp_420_accel_v420_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=167, w2=347, w3=339, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 167)
    baseline = trend.rolling(347, min_periods=max(347//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(339, min_periods=max(339//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.185 + 0.0002821 * anchor
    return base_signal.diff()

def f05_vbp_421_jerk_v421_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=174, w2=358, w3=352, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 174)
    slow = _rolling_slope(x, 358)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.199375 + 0.0002822 * anchor
    return base_signal.diff()

def f05_vbp_422_accel_v422_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=181, w2=369, w3=365, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(369, min_periods=max(369//3, 2)).max()
    trough = x.rolling(181, min_periods=max(181//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.21375 + 0.0002823 * anchor
    return base_signal.diff()

def f05_vbp_423_jerk_v423_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=188, w2=380, w3=378, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(380, min_periods=max(380//3, 2)).rank(pct=True)
    persistence = change.rolling(378, min_periods=max(378//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.035 * persistence + 0.0002824 * anchor
    return base_signal.diff()

def f05_vbp_424_accel_v424_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=195, w2=391, w3=391, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(195, min_periods=max(195//3, 2)).std()
    vol_slow = ret.rolling(391, min_periods=max(391//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.2425 + 0.0002825 * anchor
    return base_signal.diff()

def f05_vbp_425_jerk_v425_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=202, w2=402, w3=404, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(402, min_periods=max(402//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 202)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0502 * slope + 0.0002826 * anchor
    return base_signal.diff()

def f05_vbp_426_accel_v426_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=209, w2=413, w3=417, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(413, min_periods=max(413//3, 2)).mean()
    noise = impulse.abs().rolling(417, min_periods=max(417//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.27125 + 0.0002827 * anchor
    return base_signal.diff()

def f05_vbp_427_jerk_v427_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=216, w2=424, w3=430, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 216)
    acceleration = _rolling_slope(velocity, 424)
    curvature = _rolling_slope(acceleration, 430)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0654 * acceleration + 0.0002828 * anchor
    return base_signal.diff()

def f05_vbp_428_accel_v428_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=223, w2=435, w3=443, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(223, min_periods=max(223//3, 2)).mean(), upside.rolling(435, min_periods=max(435//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.3 + 0.0002829 * anchor
    return base_signal.diff()

def f05_vbp_429_jerk_v429_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=230, w2=446, w3=456, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(446, min_periods=max(446//3, 2)).max()
    rebound = x - x.rolling(230, min_periods=max(230//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0806 * _rolling_slope(draw, 456) + 0.000283 * anchor
    return base_signal.diff()

def f05_vbp_430_accel_v430_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=237, w2=457, w3=469, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 237)
    baseline = trend.rolling(457, min_periods=max(457//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(469, min_periods=max(469//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.32875 + 0.0002831 * anchor
    return base_signal.diff()

def f05_vbp_431_jerk_v431_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=244, w2=468, w3=482, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 244)
    slow = _rolling_slope(x, 468)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.343125 + 0.0002832 * anchor
    return base_signal.diff()

def f05_vbp_432_accel_v432_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=251, w2=479, w3=495, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(479, min_periods=max(479//3, 2)).max()
    trough = x.rolling(251, min_periods=max(251//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.3575 + 0.0002833 * anchor
    return base_signal.diff()

def f05_vbp_433_jerk_v433_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=7, w2=490, w3=508, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(7)
    rank = change.rolling(490, min_periods=max(490//3, 2)).rank(pct=True)
    persistence = change.rolling(508, min_periods=max(508//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.111 * persistence + 0.0002834 * anchor
    return base_signal.diff()

def f05_vbp_434_accel_v434_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=14, w2=501, w3=521, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(14, min_periods=max(14//3, 2)).std()
    vol_slow = ret.rolling(501, min_periods=max(501//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.38625 + 0.0002835 * anchor
    return base_signal.diff()

def f05_vbp_435_jerk_v435_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=21, w2=512, w3=534, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(512, min_periods=max(512//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 21)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1262 * slope + 0.0002836 * anchor
    return base_signal.diff()

def f05_vbp_436_accel_v436_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=28, w2=20, w3=547, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(28)
    drag = impulse.rolling(20, min_periods=max(20//3, 2)).mean()
    noise = impulse.abs().rolling(547, min_periods=max(547//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.415 + 0.0002837 * anchor
    return base_signal.diff()

def f05_vbp_437_jerk_v437_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=35, w2=31, w3=560, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 35)
    acceleration = _rolling_slope(velocity, 31)
    curvature = _rolling_slope(acceleration, 560)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1414 * acceleration + 0.0002838 * anchor
    return base_signal.diff()

def f05_vbp_438_accel_v438_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=42, w2=42, w3=573, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(42, min_periods=max(42//3, 2)).mean(), upside.rolling(42, min_periods=max(42//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.44375 + 0.0002839 * anchor
    return base_signal.diff()

def f05_vbp_439_jerk_v439_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=49, w2=53, w3=586, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(53, min_periods=max(53//3, 2)).max()
    rebound = x - x.rolling(49, min_periods=max(49//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1566 * _rolling_slope(draw, 586) + 0.000284 * anchor
    return base_signal.diff()

def f05_vbp_440_accel_v440_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=56, w2=64, w3=599, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 56)
    baseline = trend.rolling(64, min_periods=max(64//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(599, min_periods=max(599//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.4725 + 0.0002841 * anchor
    return base_signal.diff()

def f05_vbp_441_jerk_v441_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=63, w2=75, w3=612, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 63)
    slow = _rolling_slope(x, 75)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.486875 + 0.0002842 * anchor
    return base_signal.diff()

def f05_vbp_442_accel_v442_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=70, w2=86, w3=625, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(86, min_periods=max(86//3, 2)).max()
    trough = x.rolling(70, min_periods=max(70//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.50125 + 0.0002843 * anchor
    return base_signal.diff()

def f05_vbp_443_jerk_v443_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=77, w2=97, w3=638, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(77)
    rank = change.rolling(97, min_periods=max(97//3, 2)).rank(pct=True)
    persistence = change.rolling(638, min_periods=max(638//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.187 * persistence + 0.0002844 * anchor
    return base_signal.diff()

def f05_vbp_444_accel_v444_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=84, w2=108, w3=651, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(84, min_periods=max(84//3, 2)).std()
    vol_slow = ret.rolling(108, min_periods=max(108//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.53 + 0.0002845 * anchor
    return base_signal.diff()

def f05_vbp_445_jerk_v445_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=91, w2=119, w3=664, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(119, min_periods=max(119//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 91)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2022 * slope + 0.0002846 * anchor
    return base_signal.diff()

def f05_vbp_446_accel_v446_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=98, w2=130, w3=677, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(98)
    drag = impulse.rolling(130, min_periods=max(130//3, 2)).mean()
    noise = impulse.abs().rolling(677, min_periods=max(677//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.55875 + 0.0002847 * anchor
    return base_signal.diff()

def f05_vbp_447_jerk_v447_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=105, w2=141, w3=690, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 105)
    acceleration = _rolling_slope(velocity, 141)
    curvature = _rolling_slope(acceleration, 690)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2174 * acceleration + 0.0002848 * anchor
    return base_signal.diff()

def f05_vbp_448_accel_v448_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=112, w2=152, w3=703, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(112, min_periods=max(112//3, 2)).mean(), upside.rolling(152, min_periods=max(152//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.5875 + 0.0002849 * anchor
    return base_signal.diff()

def f05_vbp_449_jerk_v449_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=119, w2=163, w3=716, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(163, min_periods=max(163//3, 2)).max()
    rebound = x - x.rolling(119, min_periods=max(119//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2326 * _rolling_slope(draw, 716) + 0.000285 * anchor
    return base_signal.diff()

def f05_vbp_450_accel_v450_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=126, w2=174, w3=729, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 126)
    baseline = trend.rolling(174, min_periods=max(174//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(729, min_periods=max(729//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.61625 + 0.0002851 * anchor
    return base_signal.diff()
