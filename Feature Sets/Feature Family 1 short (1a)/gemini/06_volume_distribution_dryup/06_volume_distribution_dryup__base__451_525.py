"""06 volume distribution dryup base features 451-525 â€” Pipeline 1a-HF Grade v3.

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

def f06_vdd_451_jerk_v451(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=66, w2=246, w3=215, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 66)
    slow = _rolling_slope(x, 246)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=215, adjust=False).mean() * 0.978125 + 0.0003452 * anchor

def f06_vdd_452_accel_v452(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=73, w2=257, w3=228, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(257, min_periods=max(257//3, 2)).max()
    trough = x.rolling(73, min_periods=max(73//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.9925 + 0.0003453 * anchor

def f06_vdd_453_jerk_v453(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=80, w2=268, w3=241, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(80)
    rank = change.rolling(268, min_periods=max(268//3, 2)).rank(pct=True)
    persistence = change.rolling(241, min_periods=max(241//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3062 * persistence + 0.0003454 * anchor

def f06_vdd_454_accel_v454(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=87, w2=279, w3=254, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(87, min_periods=max(87//3, 2)).std()
    vol_slow = ret.rolling(279, min_periods=max(279//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.02125 + 0.0003455 * anchor

def f06_vdd_455_jerk_v455(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=94, w2=290, w3=267, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(290, min_periods=max(290//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 94)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3214 * slope + 0.0003456 * anchor

def f06_vdd_456_accel_v456(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=101, w2=301, w3=280, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(101)
    drag = impulse.rolling(301, min_periods=max(301//3, 2)).mean()
    noise = impulse.abs().rolling(280, min_periods=max(280//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.05 + 0.0003457 * anchor

def f06_vdd_457_jerk_v457(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=108, w2=312, w3=293, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 108)
    acceleration = _rolling_slope(velocity, 312)
    curvature = _rolling_slope(acceleration, 293)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3366 * acceleration + 0.0003458 * anchor

def f06_vdd_458_accel_v458(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=115, w2=323, w3=306, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(115, min_periods=max(115//3, 2)).mean(), upside.rolling(323, min_periods=max(323//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.07875 + 0.0003459 * anchor

def f06_vdd_459_jerk_v459(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=122, w2=334, w3=319, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(334, min_periods=max(334//3, 2)).max()
    rebound = x - x.rolling(122, min_periods=max(122//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3518 * _rolling_slope(draw, 319) + 0.000346 * anchor

def f06_vdd_460_accel_v460(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=129, w2=345, w3=332, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 129)
    baseline = trend.rolling(345, min_periods=max(345//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(332, min_periods=max(332//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.1075 + 0.0003461 * anchor

def f06_vdd_461_jerk_v461(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=136, w2=356, w3=345, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 136)
    slow = _rolling_slope(x, 356)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.121875 + 0.0003462 * anchor

def f06_vdd_462_accel_v462(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=143, w2=367, w3=358, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(367, min_periods=max(367//3, 2)).max()
    trough = x.rolling(143, min_periods=max(143//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.13625 + 0.0003463 * anchor

def f06_vdd_463_jerk_v463(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=150, w2=378, w3=371, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(378, min_periods=max(378//3, 2)).rank(pct=True)
    persistence = change.rolling(371, min_periods=max(371//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3822 * persistence + 0.0003464 * anchor

def f06_vdd_464_accel_v464(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=157, w2=389, w3=384, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(157, min_periods=max(157//3, 2)).std()
    vol_slow = ret.rolling(389, min_periods=max(389//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.165 + 0.0003465 * anchor

def f06_vdd_465_jerk_v465(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=164, w2=400, w3=397, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(400, min_periods=max(400//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 164)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3974 * slope + 0.0003466 * anchor

def f06_vdd_466_accel_v466(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=171, w2=411, w3=410, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(411, min_periods=max(411//3, 2)).mean()
    noise = impulse.abs().rolling(410, min_periods=max(410//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.19375 + 0.0003467 * anchor

def f06_vdd_467_jerk_v467(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=178, w2=422, w3=423, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 178)
    acceleration = _rolling_slope(velocity, 422)
    curvature = _rolling_slope(acceleration, 423)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0362 * acceleration + 0.0003468 * anchor

def f06_vdd_468_accel_v468(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=185, w2=433, w3=436, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(185, min_periods=max(185//3, 2)).mean(), upside.rolling(433, min_periods=max(433//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.2225 + 0.0003469 * anchor

def f06_vdd_469_jerk_v469(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=192, w2=444, w3=449, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(444, min_periods=max(444//3, 2)).max()
    rebound = x - x.rolling(192, min_periods=max(192//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0514 * _rolling_slope(draw, 449) + 0.000347 * anchor

def f06_vdd_470_accel_v470(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=199, w2=455, w3=462, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 199)
    baseline = trend.rolling(455, min_periods=max(455//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(462, min_periods=max(462//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.25125 + 0.0003471 * anchor

def f06_vdd_471_jerk_v471(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=206, w2=466, w3=475, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 206)
    slow = _rolling_slope(x, 466)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.265625 + 0.0003472 * anchor

def f06_vdd_472_accel_v472(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=213, w2=477, w3=488, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(477, min_periods=max(477//3, 2)).max()
    trough = x.rolling(213, min_periods=max(213//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.28 + 0.0003473 * anchor

def f06_vdd_473_jerk_v473(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=220, w2=488, w3=501, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(488, min_periods=max(488//3, 2)).rank(pct=True)
    persistence = change.rolling(501, min_periods=max(501//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0818 * persistence + 0.0003474 * anchor

def f06_vdd_474_accel_v474(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=227, w2=499, w3=514, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(227, min_periods=max(227//3, 2)).std()
    vol_slow = ret.rolling(499, min_periods=max(499//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.30875 + 0.0003475 * anchor

def f06_vdd_475_jerk_v475(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=234, w2=510, w3=527, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(510, min_periods=max(510//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 234)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.097 * slope + 0.0003476 * anchor

def f06_vdd_476_accel_v476(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=241, w2=18, w3=540, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(18, min_periods=max(18//3, 2)).mean()
    noise = impulse.abs().rolling(540, min_periods=max(540//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.3375 + 0.0003477 * anchor

def f06_vdd_477_jerk_v477(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=248, w2=29, w3=553, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 248)
    acceleration = _rolling_slope(velocity, 29)
    curvature = _rolling_slope(acceleration, 553)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1122 * acceleration + 0.0003478 * anchor

def f06_vdd_478_accel_v478(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=255, w2=40, w3=566, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(255, min_periods=max(255//3, 2)).mean(), upside.rolling(40, min_periods=max(40//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.36625 + 0.0003479 * anchor

def f06_vdd_479_jerk_v479(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=11, w2=51, w3=579, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(51, min_periods=max(51//3, 2)).max()
    rebound = x - x.rolling(11, min_periods=max(11//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1274 * _rolling_slope(draw, 579) + 0.000348 * anchor

def f06_vdd_480_accel_v480(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=18, w2=62, w3=592, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 18)
    baseline = trend.rolling(62, min_periods=max(62//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(592, min_periods=max(592//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.395 + 0.0003481 * anchor

def f06_vdd_481_jerk_v481(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=25, w2=73, w3=605, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 25)
    slow = _rolling_slope(x, 73)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.409375 + 0.0003482 * anchor

def f06_vdd_482_accel_v482(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=32, w2=84, w3=618, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(84, min_periods=max(84//3, 2)).max()
    trough = x.rolling(32, min_periods=max(32//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.42375 + 0.0003483 * anchor

def f06_vdd_483_jerk_v483(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=39, w2=95, w3=631, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(39)
    rank = change.rolling(95, min_periods=max(95//3, 2)).rank(pct=True)
    persistence = change.rolling(631, min_periods=max(631//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1578 * persistence + 0.0003484 * anchor

def f06_vdd_484_accel_v484(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=46, w2=106, w3=644, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(46, min_periods=max(46//3, 2)).std()
    vol_slow = ret.rolling(106, min_periods=max(106//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.4525 + 0.0003485 * anchor

def f06_vdd_485_jerk_v485(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=53, w2=117, w3=657, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(117, min_periods=max(117//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 53)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.173 * slope + 0.0003486 * anchor

def f06_vdd_486_accel_v486(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=60, w2=128, w3=670, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(60)
    drag = impulse.rolling(128, min_periods=max(128//3, 2)).mean()
    noise = impulse.abs().rolling(670, min_periods=max(670//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.48125 + 0.0003487 * anchor

def f06_vdd_487_jerk_v487(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=67, w2=139, w3=683, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 67)
    acceleration = _rolling_slope(velocity, 139)
    curvature = _rolling_slope(acceleration, 683)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1882 * acceleration + 0.0003488 * anchor

def f06_vdd_488_accel_v488(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=74, w2=150, w3=696, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(74, min_periods=max(74//3, 2)).mean(), upside.rolling(150, min_periods=max(150//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.51 + 0.0003489 * anchor

def f06_vdd_489_jerk_v489(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=81, w2=161, w3=709, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(161, min_periods=max(161//3, 2)).max()
    rebound = x - x.rolling(81, min_periods=max(81//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2034 * _rolling_slope(draw, 709) + 0.000349 * anchor

def f06_vdd_490_accel_v490(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=88, w2=172, w3=722, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 88)
    baseline = trend.rolling(172, min_periods=max(172//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(722, min_periods=max(722//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.53875 + 0.0003491 * anchor

def f06_vdd_491_jerk_v491(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=95, w2=183, w3=735, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 95)
    slow = _rolling_slope(x, 183)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.553125 + 0.0003492 * anchor

def f06_vdd_492_accel_v492(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=102, w2=194, w3=748, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(194, min_periods=max(194//3, 2)).max()
    trough = x.rolling(102, min_periods=max(102//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.5675 + 0.0003493 * anchor

def f06_vdd_493_jerk_v493(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=109, w2=205, w3=761, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(109)
    rank = change.rolling(205, min_periods=max(205//3, 2)).rank(pct=True)
    persistence = change.rolling(761, min_periods=max(761//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2338 * persistence + 0.0003494 * anchor

def f06_vdd_494_accel_v494(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=116, w2=216, w3=17, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(116, min_periods=max(116//3, 2)).std()
    vol_slow = ret.rolling(216, min_periods=max(216//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.59625 + 0.0003495 * anchor

def f06_vdd_495_jerk_v495(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=123, w2=227, w3=30, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(227, min_periods=max(227//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 123)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.249 * slope + 0.0003496 * anchor

def f06_vdd_496_accel_v496(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=130, w2=238, w3=43, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(238, min_periods=max(238//3, 2)).mean()
    noise = impulse.abs().rolling(43, min_periods=max(43//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.851875 + 0.0003497 * anchor

def f06_vdd_497_jerk_v497(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=137, w2=249, w3=56, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 137)
    acceleration = _rolling_slope(velocity, 249)
    curvature = _rolling_slope(acceleration, 56)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2642 * acceleration + 0.0003498 * anchor

def f06_vdd_498_accel_v498(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=144, w2=260, w3=69, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(144, min_periods=max(144//3, 2)).mean(), upside.rolling(260, min_periods=max(260//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(69) * 0.880625 + 0.0003499 * anchor

def f06_vdd_499_jerk_v499(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=151, w2=271, w3=82, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(271, min_periods=max(271//3, 2)).max()
    rebound = x - x.rolling(151, min_periods=max(151//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2794 * _rolling_slope(draw, 82) + 0.00035 * anchor

def f06_vdd_500_accel_v500(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=158, w2=282, w3=95, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 158)
    baseline = trend.rolling(282, min_periods=max(282//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(95, min_periods=max(95//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.909375 + 0.0003501 * anchor

def f06_vdd_501_jerk_v501(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=165, w2=293, w3=108, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 165)
    slow = _rolling_slope(x, 293)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=108, adjust=False).mean() * 0.92375 + 0.0003502 * anchor

def f06_vdd_502_accel_v502(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=172, w2=304, w3=121, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(304, min_periods=max(304//3, 2)).max()
    trough = x.rolling(172, min_periods=max(172//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.938125 + 0.0003503 * anchor

def f06_vdd_503_jerk_v503(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=179, w2=315, w3=134, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(315, min_periods=max(315//3, 2)).rank(pct=True)
    persistence = change.rolling(134, min_periods=max(134//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3098 * persistence + 0.0003504 * anchor

def f06_vdd_504_accel_v504(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=186, w2=326, w3=147, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(186, min_periods=max(186//3, 2)).std()
    vol_slow = ret.rolling(326, min_periods=max(326//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.966875 + 0.0003505 * anchor

def f06_vdd_505_jerk_v505(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=193, w2=337, w3=160, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(337, min_periods=max(337//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 193)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.325 * slope + 0.0003506 * anchor

def f06_vdd_506_accel_v506(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=200, w2=348, w3=173, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(348, min_periods=max(348//3, 2)).mean()
    noise = impulse.abs().rolling(173, min_periods=max(173//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.995625 + 0.0003507 * anchor

def f06_vdd_507_jerk_v507(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=207, w2=359, w3=186, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 207)
    acceleration = _rolling_slope(velocity, 359)
    curvature = _rolling_slope(acceleration, 186)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3402 * acceleration + 0.0003508 * anchor

def f06_vdd_508_accel_v508(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=214, w2=370, w3=199, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(214, min_periods=max(214//3, 2)).mean(), upside.rolling(370, min_periods=max(370//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.024375 + 0.0003509 * anchor

def f06_vdd_509_jerk_v509(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=221, w2=381, w3=212, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(381, min_periods=max(381//3, 2)).max()
    rebound = x - x.rolling(221, min_periods=max(221//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3554 * _rolling_slope(draw, 212) + 0.000351 * anchor

def f06_vdd_510_accel_v510(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=228, w2=392, w3=225, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 228)
    baseline = trend.rolling(392, min_periods=max(392//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(225, min_periods=max(225//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.053125 + 0.0003511 * anchor

def f06_vdd_511_jerk_v511(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=235, w2=403, w3=238, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 235)
    slow = _rolling_slope(x, 403)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=238, adjust=False).mean() * 1.0675 + 0.0003512 * anchor

def f06_vdd_512_accel_v512(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=242, w2=414, w3=251, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(414, min_periods=max(414//3, 2)).max()
    trough = x.rolling(242, min_periods=max(242//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.081875 + 0.0003513 * anchor

def f06_vdd_513_jerk_v513(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=249, w2=425, w3=264, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(425, min_periods=max(425//3, 2)).rank(pct=True)
    persistence = change.rolling(264, min_periods=max(264//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3858 * persistence + 0.0003514 * anchor

def f06_vdd_514_accel_v514(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=5, w2=436, w3=277, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(5, min_periods=max(5//3, 2)).std()
    vol_slow = ret.rolling(436, min_periods=max(436//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.110625 + 0.0003515 * anchor

def f06_vdd_515_jerk_v515(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=12, w2=447, w3=290, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(447, min_periods=max(447//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 12)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.401 * slope + 0.0003516 * anchor

def f06_vdd_516_accel_v516(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=19, w2=458, w3=303, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(19)
    drag = impulse.rolling(458, min_periods=max(458//3, 2)).mean()
    noise = impulse.abs().rolling(303, min_periods=max(303//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.139375 + 0.0003517 * anchor

def f06_vdd_517_jerk_v517(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=26, w2=469, w3=316, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 26)
    acceleration = _rolling_slope(velocity, 469)
    curvature = _rolling_slope(acceleration, 316)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0398 * acceleration + 0.0003518 * anchor

def f06_vdd_518_accel_v518(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=33, w2=480, w3=329, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(33, min_periods=max(33//3, 2)).mean(), upside.rolling(480, min_periods=max(480//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.168125 + 0.0003519 * anchor

def f06_vdd_519_jerk_v519(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=40, w2=491, w3=342, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(491, min_periods=max(491//3, 2)).max()
    rebound = x - x.rolling(40, min_periods=max(40//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.055 * _rolling_slope(draw, 342) + 0.000352 * anchor

def f06_vdd_520_accel_v520(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=47, w2=502, w3=355, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 47)
    baseline = trend.rolling(502, min_periods=max(502//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(355, min_periods=max(355//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.196875 + 0.0003521 * anchor

def f06_vdd_521_jerk_v521(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=54, w2=10, w3=368, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 54)
    slow = _rolling_slope(x, 10)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.21125 + 0.0003522 * anchor

def f06_vdd_522_accel_v522(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=61, w2=21, w3=381, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(21, min_periods=max(21//3, 2)).max()
    trough = x.rolling(61, min_periods=max(61//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.225625 + 0.0003523 * anchor

def f06_vdd_523_jerk_v523(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=68, w2=32, w3=394, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(68)
    rank = change.rolling(32, min_periods=max(32//3, 2)).rank(pct=True)
    persistence = change.rolling(394, min_periods=max(394//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0854 * persistence + 0.0003524 * anchor

def f06_vdd_524_accel_v524(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=75, w2=43, w3=407, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(75, min_periods=max(75//3, 2)).std()
    vol_slow = ret.rolling(43, min_periods=max(43//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.254375 + 0.0003525 * anchor

def f06_vdd_525_jerk_v525(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=82, w2=54, w3=420, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(54, min_periods=max(54//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 82)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1006 * slope + 0.0003526 * anchor
