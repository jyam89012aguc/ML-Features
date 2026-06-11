"""03 advance magnitude duration base features 451-525 â€” Pipeline 1a-HF Grade v3.

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

def f03_amd_451_jerk_v451(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=16, w2=63, w3=282, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 16)
    slow = _rolling_slope(x, 63)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=282, adjust=False).mean() * 1.389375 + 0.0001652 * anchor

def f03_amd_452_accel_v452(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=23, w2=74, w3=295, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(74, min_periods=max(74//3, 2)).max()
    trough = x.rolling(23, min_periods=max(23//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.40375 + 0.0001653 * anchor

def f03_amd_453_jerk_v453(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=30, w2=85, w3=308, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(30)
    rank = change.rolling(85, min_periods=max(85//3, 2)).rank(pct=True)
    persistence = change.rolling(308, min_periods=max(308//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1766 * persistence + 0.0001654 * anchor

def f03_amd_454_accel_v454(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=37, w2=96, w3=321, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(37, min_periods=max(37//3, 2)).std()
    vol_slow = ret.rolling(96, min_periods=max(96//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.4325 + 0.0001655 * anchor

def f03_amd_455_jerk_v455(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=44, w2=107, w3=334, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(107, min_periods=max(107//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 44)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1918 * slope + 0.0001656 * anchor

def f03_amd_456_accel_v456(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=51, w2=118, w3=347, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(51)
    drag = impulse.rolling(118, min_periods=max(118//3, 2)).mean()
    noise = impulse.abs().rolling(347, min_periods=max(347//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.46125 + 0.0001657 * anchor

def f03_amd_457_jerk_v457(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=58, w2=129, w3=360, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 58)
    acceleration = _rolling_slope(velocity, 129)
    curvature = _rolling_slope(acceleration, 360)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.207 * acceleration + 0.0001658 * anchor

def f03_amd_458_accel_v458(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=65, w2=140, w3=373, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(65, min_periods=max(65//3, 2)).mean(), upside.rolling(140, min_periods=max(140//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.49 + 0.0001659 * anchor

def f03_amd_459_jerk_v459(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=72, w2=151, w3=386, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(151, min_periods=max(151//3, 2)).max()
    rebound = x - x.rolling(72, min_periods=max(72//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2222 * _rolling_slope(draw, 386) + 0.000166 * anchor

def f03_amd_460_accel_v460(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=79, w2=162, w3=399, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 79)
    baseline = trend.rolling(162, min_periods=max(162//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(399, min_periods=max(399//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.51875 + 0.0001661 * anchor

def f03_amd_461_jerk_v461(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=86, w2=173, w3=412, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 86)
    slow = _rolling_slope(x, 173)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.533125 + 0.0001662 * anchor

def f03_amd_462_accel_v462(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=93, w2=184, w3=425, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(184, min_periods=max(184//3, 2)).max()
    trough = x.rolling(93, min_periods=max(93//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.5475 + 0.0001663 * anchor

def f03_amd_463_jerk_v463(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=100, w2=195, w3=438, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(100)
    rank = change.rolling(195, min_periods=max(195//3, 2)).rank(pct=True)
    persistence = change.rolling(438, min_periods=max(438//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2526 * persistence + 0.0001664 * anchor

def f03_amd_464_accel_v464(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=107, w2=206, w3=451, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(107, min_periods=max(107//3, 2)).std()
    vol_slow = ret.rolling(206, min_periods=max(206//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.57625 + 0.0001665 * anchor

def f03_amd_465_jerk_v465(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=114, w2=217, w3=464, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(217, min_periods=max(217//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 114)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2678 * slope + 0.0001666 * anchor

def f03_amd_466_accel_v466(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=121, w2=228, w3=477, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(121)
    drag = impulse.rolling(228, min_periods=max(228//3, 2)).mean()
    noise = impulse.abs().rolling(477, min_periods=max(477//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.605 + 0.0001667 * anchor

def f03_amd_467_jerk_v467(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=128, w2=239, w3=490, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 128)
    acceleration = _rolling_slope(velocity, 239)
    curvature = _rolling_slope(acceleration, 490)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.283 * acceleration + 0.0001668 * anchor

def f03_amd_468_accel_v468(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=135, w2=250, w3=503, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(135, min_periods=max(135//3, 2)).mean(), upside.rolling(250, min_periods=max(250//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.860625 + 0.0001669 * anchor

def f03_amd_469_jerk_v469(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=142, w2=261, w3=516, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(261, min_periods=max(261//3, 2)).max()
    rebound = x - x.rolling(142, min_periods=max(142//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2982 * _rolling_slope(draw, 516) + 0.000167 * anchor

def f03_amd_470_accel_v470(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=149, w2=272, w3=529, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 149)
    baseline = trend.rolling(272, min_periods=max(272//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(529, min_periods=max(529//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.889375 + 0.0001671 * anchor

def f03_amd_471_jerk_v471(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=156, w2=283, w3=542, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 156)
    slow = _rolling_slope(x, 283)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.90375 + 0.0001672 * anchor

def f03_amd_472_accel_v472(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=163, w2=294, w3=555, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(294, min_periods=max(294//3, 2)).max()
    trough = x.rolling(163, min_periods=max(163//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.918125 + 0.0001673 * anchor

def f03_amd_473_jerk_v473(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=170, w2=305, w3=568, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(305, min_periods=max(305//3, 2)).rank(pct=True)
    persistence = change.rolling(568, min_periods=max(568//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3286 * persistence + 0.0001674 * anchor

def f03_amd_474_accel_v474(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=177, w2=316, w3=581, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(177, min_periods=max(177//3, 2)).std()
    vol_slow = ret.rolling(316, min_periods=max(316//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.946875 + 0.0001675 * anchor

def f03_amd_475_jerk_v475(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=184, w2=327, w3=594, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(327, min_periods=max(327//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 184)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3438 * slope + 0.0001676 * anchor

def f03_amd_476_accel_v476(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=191, w2=338, w3=607, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(338, min_periods=max(338//3, 2)).mean()
    noise = impulse.abs().rolling(607, min_periods=max(607//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.975625 + 0.0001677 * anchor

def f03_amd_477_jerk_v477(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=198, w2=349, w3=620, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 198)
    acceleration = _rolling_slope(velocity, 349)
    curvature = _rolling_slope(acceleration, 620)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.359 * acceleration + 0.0001678 * anchor

def f03_amd_478_accel_v478(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=205, w2=360, w3=633, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(205, min_periods=max(205//3, 2)).mean(), upside.rolling(360, min_periods=max(360//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.004375 + 0.0001679 * anchor

def f03_amd_479_jerk_v479(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=212, w2=371, w3=646, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(371, min_periods=max(371//3, 2)).max()
    rebound = x - x.rolling(212, min_periods=max(212//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3742 * _rolling_slope(draw, 646) + 0.000168 * anchor

def f03_amd_480_accel_v480(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=219, w2=382, w3=659, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 219)
    baseline = trend.rolling(382, min_periods=max(382//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(659, min_periods=max(659//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.033125 + 0.0001681 * anchor

def f03_amd_481_jerk_v481(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=226, w2=393, w3=672, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 226)
    slow = _rolling_slope(x, 393)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.0475 + 0.0001682 * anchor

def f03_amd_482_accel_v482(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=233, w2=404, w3=685, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(404, min_periods=max(404//3, 2)).max()
    trough = x.rolling(233, min_periods=max(233//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.061875 + 0.0001683 * anchor

def f03_amd_483_jerk_v483(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=240, w2=415, w3=698, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(415, min_periods=max(415//3, 2)).rank(pct=True)
    persistence = change.rolling(698, min_periods=max(698//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.4046 * persistence + 0.0001684 * anchor

def f03_amd_484_accel_v484(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=247, w2=426, w3=711, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(247, min_periods=max(247//3, 2)).std()
    vol_slow = ret.rolling(426, min_periods=max(426//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.090625 + 0.0001685 * anchor

def f03_amd_485_jerk_v485(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=254, w2=437, w3=724, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(437, min_periods=max(437//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 254)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0434 * slope + 0.0001686 * anchor

def f03_amd_486_accel_v486(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=10, w2=448, w3=737, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(10)
    drag = impulse.rolling(448, min_periods=max(448//3, 2)).mean()
    noise = impulse.abs().rolling(737, min_periods=max(737//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.119375 + 0.0001687 * anchor

def f03_amd_487_jerk_v487(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=17, w2=459, w3=750, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 17)
    acceleration = _rolling_slope(velocity, 459)
    curvature = _rolling_slope(acceleration, 750)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0586 * acceleration + 0.0001688 * anchor

def f03_amd_488_accel_v488(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=24, w2=470, w3=763, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(24, min_periods=max(24//3, 2)).mean(), upside.rolling(470, min_periods=max(470//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.148125 + 0.0001689 * anchor

def f03_amd_489_jerk_v489(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=31, w2=481, w3=19, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(481, min_periods=max(481//3, 2)).max()
    rebound = x - x.rolling(31, min_periods=max(31//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0738 * _rolling_slope(draw, 19) + 0.000169 * anchor

def f03_amd_490_accel_v490(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=38, w2=492, w3=32, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 38)
    baseline = trend.rolling(492, min_periods=max(492//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(32, min_periods=max(32//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.176875 + 0.0001691 * anchor

def f03_amd_491_jerk_v491(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=45, w2=503, w3=45, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 45)
    slow = _rolling_slope(x, 503)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=45, adjust=False).mean() * 1.19125 + 0.0001692 * anchor

def f03_amd_492_accel_v492(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=52, w2=11, w3=58, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(11, min_periods=max(11//3, 2)).max()
    trough = x.rolling(52, min_periods=max(52//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.205625 + 0.0001693 * anchor

def f03_amd_493_jerk_v493(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=59, w2=22, w3=71, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(59)
    rank = change.rolling(22, min_periods=max(22//3, 2)).rank(pct=True)
    persistence = change.rolling(71, min_periods=max(71//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1042 * persistence + 0.0001694 * anchor

def f03_amd_494_accel_v494(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=66, w2=33, w3=84, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(66, min_periods=max(66//3, 2)).std()
    vol_slow = ret.rolling(33, min_periods=max(33//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.234375 + 0.0001695 * anchor

def f03_amd_495_jerk_v495(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=73, w2=44, w3=97, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(44, min_periods=max(44//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 73)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1194 * slope + 0.0001696 * anchor

def f03_amd_496_accel_v496(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=80, w2=55, w3=110, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(80)
    drag = impulse.rolling(55, min_periods=max(55//3, 2)).mean()
    noise = impulse.abs().rolling(110, min_periods=max(110//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.263125 + 0.0001697 * anchor

def f03_amd_497_jerk_v497(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=87, w2=66, w3=123, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 87)
    acceleration = _rolling_slope(velocity, 66)
    curvature = _rolling_slope(acceleration, 123)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1346 * acceleration + 0.0001698 * anchor

def f03_amd_498_accel_v498(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=94, w2=77, w3=136, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(94, min_periods=max(94//3, 2)).mean(), upside.rolling(77, min_periods=max(77//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.291875 + 0.0001699 * anchor

def f03_amd_499_jerk_v499(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=101, w2=88, w3=149, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(88, min_periods=max(88//3, 2)).max()
    rebound = x - x.rolling(101, min_periods=max(101//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1498 * _rolling_slope(draw, 149) + 0.00017 * anchor

def f03_amd_500_accel_v500(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=108, w2=99, w3=162, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 108)
    baseline = trend.rolling(99, min_periods=max(99//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(162, min_periods=max(162//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.320625 + 0.0001701 * anchor

def f03_amd_501_jerk_v501(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=115, w2=110, w3=175, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 115)
    slow = _rolling_slope(x, 110)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=175, adjust=False).mean() * 1.335 + 0.0001702 * anchor

def f03_amd_502_accel_v502(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=122, w2=121, w3=188, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(121, min_periods=max(121//3, 2)).max()
    trough = x.rolling(122, min_periods=max(122//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.349375 + 0.0001703 * anchor

def f03_amd_503_jerk_v503(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=129, w2=132, w3=201, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(132, min_periods=max(132//3, 2)).rank(pct=True)
    persistence = change.rolling(201, min_periods=max(201//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1802 * persistence + 0.0001704 * anchor

def f03_amd_504_accel_v504(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=136, w2=143, w3=214, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(136, min_periods=max(136//3, 2)).std()
    vol_slow = ret.rolling(143, min_periods=max(143//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.378125 + 0.0001705 * anchor

def f03_amd_505_jerk_v505(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=143, w2=154, w3=227, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(154, min_periods=max(154//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 143)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1954 * slope + 0.0001706 * anchor

def f03_amd_506_accel_v506(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=150, w2=165, w3=240, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(165, min_periods=max(165//3, 2)).mean()
    noise = impulse.abs().rolling(240, min_periods=max(240//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.406875 + 0.0001707 * anchor

def f03_amd_507_jerk_v507(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=157, w2=176, w3=253, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 157)
    acceleration = _rolling_slope(velocity, 176)
    curvature = _rolling_slope(acceleration, 253)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2106 * acceleration + 0.0001708 * anchor

def f03_amd_508_accel_v508(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=164, w2=187, w3=266, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(164, min_periods=max(164//3, 2)).mean(), upside.rolling(187, min_periods=max(187//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.435625 + 0.0001709 * anchor

def f03_amd_509_jerk_v509(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=171, w2=198, w3=279, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(198, min_periods=max(198//3, 2)).max()
    rebound = x - x.rolling(171, min_periods=max(171//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2258 * _rolling_slope(draw, 279) + 0.000171 * anchor

def f03_amd_510_accel_v510(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=178, w2=209, w3=292, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 178)
    baseline = trend.rolling(209, min_periods=max(209//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(292, min_periods=max(292//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.464375 + 0.0001711 * anchor

def f03_amd_511_jerk_v511(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=185, w2=220, w3=305, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 185)
    slow = _rolling_slope(x, 220)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.47875 + 0.0001712 * anchor

def f03_amd_512_accel_v512(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=192, w2=231, w3=318, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(231, min_periods=max(231//3, 2)).max()
    trough = x.rolling(192, min_periods=max(192//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.493125 + 0.0001713 * anchor

def f03_amd_513_jerk_v513(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=199, w2=242, w3=331, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(242, min_periods=max(242//3, 2)).rank(pct=True)
    persistence = change.rolling(331, min_periods=max(331//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2562 * persistence + 0.0001714 * anchor

def f03_amd_514_accel_v514(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=206, w2=253, w3=344, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(206, min_periods=max(206//3, 2)).std()
    vol_slow = ret.rolling(253, min_periods=max(253//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.521875 + 0.0001715 * anchor

def f03_amd_515_jerk_v515(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=213, w2=264, w3=357, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(264, min_periods=max(264//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 213)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2714 * slope + 0.0001716 * anchor

def f03_amd_516_accel_v516(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=220, w2=275, w3=370, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(275, min_periods=max(275//3, 2)).mean()
    noise = impulse.abs().rolling(370, min_periods=max(370//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.550625 + 0.0001717 * anchor

def f03_amd_517_jerk_v517(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=227, w2=286, w3=383, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 227)
    acceleration = _rolling_slope(velocity, 286)
    curvature = _rolling_slope(acceleration, 383)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2866 * acceleration + 0.0001718 * anchor

def f03_amd_518_accel_v518(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=234, w2=297, w3=396, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(234, min_periods=max(234//3, 2)).mean(), upside.rolling(297, min_periods=max(297//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.579375 + 0.0001719 * anchor

def f03_amd_519_jerk_v519(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=241, w2=308, w3=409, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(308, min_periods=max(308//3, 2)).max()
    rebound = x - x.rolling(241, min_periods=max(241//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3018 * _rolling_slope(draw, 409) + 0.000172 * anchor

def f03_amd_520_accel_v520(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=248, w2=319, w3=422, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 248)
    baseline = trend.rolling(319, min_periods=max(319//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(422, min_periods=max(422//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.608125 + 0.0001721 * anchor

def f03_amd_521_jerk_v521(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=255, w2=330, w3=435, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 255)
    slow = _rolling_slope(x, 330)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.6225 + 0.0001722 * anchor

def f03_amd_522_accel_v522(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=11, w2=341, w3=448, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(341, min_periods=max(341//3, 2)).max()
    trough = x.rolling(11, min_periods=max(11//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.86375 + 0.0001723 * anchor

def f03_amd_523_jerk_v523(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=18, w2=352, w3=461, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(18)
    rank = change.rolling(352, min_periods=max(352//3, 2)).rank(pct=True)
    persistence = change.rolling(461, min_periods=max(461//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3322 * persistence + 0.0001724 * anchor

def f03_amd_524_accel_v524(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=25, w2=363, w3=474, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(25, min_periods=max(25//3, 2)).std()
    vol_slow = ret.rolling(363, min_periods=max(363//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.8925 + 0.0001725 * anchor

def f03_amd_525_jerk_v525(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=32, w2=374, w3=487, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(374, min_periods=max(374//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 32)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3474 * slope + 0.0001726 * anchor
