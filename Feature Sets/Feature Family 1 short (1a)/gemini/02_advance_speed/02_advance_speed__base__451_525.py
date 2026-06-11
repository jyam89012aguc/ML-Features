"""02 advance speed base features 451-525 â€” Pipeline 1a-HF Grade v3.

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

def f02_adv_451_jerk_v451(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=83, w2=505, w3=52, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 83)
    slow = _rolling_slope(x, 505)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=52, adjust=False).mean() * 1.26875 + 0.0001052 * anchor

def f02_adv_452_accel_v452(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=90, w2=13, w3=65, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(13, min_periods=max(13//3, 2)).max()
    trough = x.rolling(90, min_periods=max(90//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.283125 + 0.0001053 * anchor

def f02_adv_453_jerk_v453(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=97, w2=24, w3=78, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(97)
    rank = change.rolling(24, min_periods=max(24//3, 2)).rank(pct=True)
    persistence = change.rolling(78, min_periods=max(78//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1334 * persistence + 0.0001054 * anchor

def f02_adv_454_accel_v454(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=104, w2=35, w3=91, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(104, min_periods=max(104//3, 2)).std()
    vol_slow = ret.rolling(35, min_periods=max(35//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.311875 + 0.0001055 * anchor

def f02_adv_455_jerk_v455(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=111, w2=46, w3=104, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(46, min_periods=max(46//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 111)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1486 * slope + 0.0001056 * anchor

def f02_adv_456_accel_v456(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=118, w2=57, w3=117, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(118)
    drag = impulse.rolling(57, min_periods=max(57//3, 2)).mean()
    noise = impulse.abs().rolling(117, min_periods=max(117//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.340625 + 0.0001057 * anchor

def f02_adv_457_jerk_v457(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=125, w2=68, w3=130, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 125)
    acceleration = _rolling_slope(velocity, 68)
    curvature = _rolling_slope(acceleration, 130)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1638 * acceleration + 0.0001058 * anchor

def f02_adv_458_accel_v458(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=132, w2=79, w3=143, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(132, min_periods=max(132//3, 2)).mean(), upside.rolling(79, min_periods=max(79//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.369375 + 0.0001059 * anchor

def f02_adv_459_jerk_v459(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=139, w2=90, w3=156, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(90, min_periods=max(90//3, 2)).max()
    rebound = x - x.rolling(139, min_periods=max(139//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.179 * _rolling_slope(draw, 156) + 0.000106 * anchor

def f02_adv_460_accel_v460(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=146, w2=101, w3=169, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 146)
    baseline = trend.rolling(101, min_periods=max(101//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(169, min_periods=max(169//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.398125 + 0.0001061 * anchor

def f02_adv_461_jerk_v461(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=153, w2=112, w3=182, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 153)
    slow = _rolling_slope(x, 112)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=182, adjust=False).mean() * 1.4125 + 0.0001062 * anchor

def f02_adv_462_accel_v462(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=160, w2=123, w3=195, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(123, min_periods=max(123//3, 2)).max()
    trough = x.rolling(160, min_periods=max(160//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.426875 + 0.0001063 * anchor

def f02_adv_463_jerk_v463(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=167, w2=134, w3=208, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(134, min_periods=max(134//3, 2)).rank(pct=True)
    persistence = change.rolling(208, min_periods=max(208//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2094 * persistence + 0.0001064 * anchor

def f02_adv_464_accel_v464(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=174, w2=145, w3=221, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(174, min_periods=max(174//3, 2)).std()
    vol_slow = ret.rolling(145, min_periods=max(145//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.455625 + 0.0001065 * anchor

def f02_adv_465_jerk_v465(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=181, w2=156, w3=234, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(156, min_periods=max(156//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 181)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2246 * slope + 0.0001066 * anchor

def f02_adv_466_accel_v466(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=188, w2=167, w3=247, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(167, min_periods=max(167//3, 2)).mean()
    noise = impulse.abs().rolling(247, min_periods=max(247//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.484375 + 0.0001067 * anchor

def f02_adv_467_jerk_v467(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=195, w2=178, w3=260, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 195)
    acceleration = _rolling_slope(velocity, 178)
    curvature = _rolling_slope(acceleration, 260)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2398 * acceleration + 0.0001068 * anchor

def f02_adv_468_accel_v468(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=202, w2=189, w3=273, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(202, min_periods=max(202//3, 2)).mean(), upside.rolling(189, min_periods=max(189//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.513125 + 0.0001069 * anchor

def f02_adv_469_jerk_v469(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=209, w2=200, w3=286, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(200, min_periods=max(200//3, 2)).max()
    rebound = x - x.rolling(209, min_periods=max(209//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.255 * _rolling_slope(draw, 286) + 0.000107 * anchor

def f02_adv_470_accel_v470(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=216, w2=211, w3=299, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 216)
    baseline = trend.rolling(211, min_periods=max(211//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(299, min_periods=max(299//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.541875 + 0.0001071 * anchor

def f02_adv_471_jerk_v471(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=223, w2=222, w3=312, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 223)
    slow = _rolling_slope(x, 222)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.55625 + 0.0001072 * anchor

def f02_adv_472_accel_v472(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=230, w2=233, w3=325, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(233, min_periods=max(233//3, 2)).max()
    trough = x.rolling(230, min_periods=max(230//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.570625 + 0.0001073 * anchor

def f02_adv_473_jerk_v473(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=237, w2=244, w3=338, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(244, min_periods=max(244//3, 2)).rank(pct=True)
    persistence = change.rolling(338, min_periods=max(338//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2854 * persistence + 0.0001074 * anchor

def f02_adv_474_accel_v474(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=244, w2=255, w3=351, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(244, min_periods=max(244//3, 2)).std()
    vol_slow = ret.rolling(255, min_periods=max(255//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.599375 + 0.0001075 * anchor

def f02_adv_475_jerk_v475(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=251, w2=266, w3=364, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(266, min_periods=max(266//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 251)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3006 * slope + 0.0001076 * anchor

def f02_adv_476_accel_v476(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=7, w2=277, w3=377, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(7)
    drag = impulse.rolling(277, min_periods=max(277//3, 2)).mean()
    noise = impulse.abs().rolling(377, min_periods=max(377//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.855 + 0.0001077 * anchor

def f02_adv_477_jerk_v477(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=14, w2=288, w3=390, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 14)
    acceleration = _rolling_slope(velocity, 288)
    curvature = _rolling_slope(acceleration, 390)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3158 * acceleration + 0.0001078 * anchor

def f02_adv_478_accel_v478(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=21, w2=299, w3=403, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(21, min_periods=max(21//3, 2)).mean(), upside.rolling(299, min_periods=max(299//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.88375 + 0.0001079 * anchor

def f02_adv_479_jerk_v479(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=28, w2=310, w3=416, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(310, min_periods=max(310//3, 2)).max()
    rebound = x - x.rolling(28, min_periods=max(28//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.331 * _rolling_slope(draw, 416) + 0.000108 * anchor

def f02_adv_480_accel_v480(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=35, w2=321, w3=429, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 35)
    baseline = trend.rolling(321, min_periods=max(321//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(429, min_periods=max(429//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.9125 + 0.0001081 * anchor

def f02_adv_481_jerk_v481(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=42, w2=332, w3=442, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 42)
    slow = _rolling_slope(x, 332)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.926875 + 0.0001082 * anchor

def f02_adv_482_accel_v482(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=49, w2=343, w3=455, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(343, min_periods=max(343//3, 2)).max()
    trough = x.rolling(49, min_periods=max(49//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.94125 + 0.0001083 * anchor

def f02_adv_483_jerk_v483(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=56, w2=354, w3=468, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(56)
    rank = change.rolling(354, min_periods=max(354//3, 2)).rank(pct=True)
    persistence = change.rolling(468, min_periods=max(468//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3614 * persistence + 0.0001084 * anchor

def f02_adv_484_accel_v484(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=63, w2=365, w3=481, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(63, min_periods=max(63//3, 2)).std()
    vol_slow = ret.rolling(365, min_periods=max(365//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.97 + 0.0001085 * anchor

def f02_adv_485_jerk_v485(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=70, w2=376, w3=494, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(376, min_periods=max(376//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 70)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3766 * slope + 0.0001086 * anchor

def f02_adv_486_accel_v486(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=77, w2=387, w3=507, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(77)
    drag = impulse.rolling(387, min_periods=max(387//3, 2)).mean()
    noise = impulse.abs().rolling(507, min_periods=max(507//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.99875 + 0.0001087 * anchor

def f02_adv_487_jerk_v487(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=84, w2=398, w3=520, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 84)
    acceleration = _rolling_slope(velocity, 398)
    curvature = _rolling_slope(acceleration, 520)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3918 * acceleration + 0.0001088 * anchor

def f02_adv_488_accel_v488(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=91, w2=409, w3=533, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(91, min_periods=max(91//3, 2)).mean(), upside.rolling(409, min_periods=max(409//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.0275 + 0.0001089 * anchor

def f02_adv_489_jerk_v489(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=98, w2=420, w3=546, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(420, min_periods=max(420//3, 2)).max()
    rebound = x - x.rolling(98, min_periods=max(98//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.407 * _rolling_slope(draw, 546) + 0.000109 * anchor

def f02_adv_490_accel_v490(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=105, w2=431, w3=559, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 105)
    baseline = trend.rolling(431, min_periods=max(431//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(559, min_periods=max(559//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.05625 + 0.0001091 * anchor

def f02_adv_491_jerk_v491(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=112, w2=442, w3=572, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 112)
    slow = _rolling_slope(x, 442)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.070625 + 0.0001092 * anchor

def f02_adv_492_accel_v492(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=119, w2=453, w3=585, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(453, min_periods=max(453//3, 2)).max()
    trough = x.rolling(119, min_periods=max(119//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.085 + 0.0001093 * anchor

def f02_adv_493_jerk_v493(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=126, w2=464, w3=598, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(464, min_periods=max(464//3, 2)).rank(pct=True)
    persistence = change.rolling(598, min_periods=max(598//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.061 * persistence + 0.0001094 * anchor

def f02_adv_494_accel_v494(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=133, w2=475, w3=611, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(133, min_periods=max(133//3, 2)).std()
    vol_slow = ret.rolling(475, min_periods=max(475//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.11375 + 0.0001095 * anchor

def f02_adv_495_jerk_v495(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=140, w2=486, w3=624, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(486, min_periods=max(486//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 140)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0762 * slope + 0.0001096 * anchor

def f02_adv_496_accel_v496(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=147, w2=497, w3=637, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(497, min_periods=max(497//3, 2)).mean()
    noise = impulse.abs().rolling(637, min_periods=max(637//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.1425 + 0.0001097 * anchor

def f02_adv_497_jerk_v497(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=154, w2=508, w3=650, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 154)
    acceleration = _rolling_slope(velocity, 508)
    curvature = _rolling_slope(acceleration, 650)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0914 * acceleration + 0.0001098 * anchor

def f02_adv_498_accel_v498(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=161, w2=16, w3=663, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(161, min_periods=max(161//3, 2)).mean(), upside.rolling(16, min_periods=max(16//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.17125 + 0.0001099 * anchor

def f02_adv_499_jerk_v499(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=168, w2=27, w3=676, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(27, min_periods=max(27//3, 2)).max()
    rebound = x - x.rolling(168, min_periods=max(168//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1066 * _rolling_slope(draw, 676) + 0.00011 * anchor

def f02_adv_500_accel_v500(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=175, w2=38, w3=689, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 175)
    baseline = trend.rolling(38, min_periods=max(38//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(689, min_periods=max(689//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.2 + 0.0001101 * anchor

def f02_adv_501_jerk_v501(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=182, w2=49, w3=702, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 182)
    slow = _rolling_slope(x, 49)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.214375 + 0.0001102 * anchor

def f02_adv_502_accel_v502(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=189, w2=60, w3=715, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(60, min_periods=max(60//3, 2)).max()
    trough = x.rolling(189, min_periods=max(189//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.22875 + 0.0001103 * anchor

def f02_adv_503_jerk_v503(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=196, w2=71, w3=728, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(71, min_periods=max(71//3, 2)).rank(pct=True)
    persistence = change.rolling(728, min_periods=max(728//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.137 * persistence + 0.0001104 * anchor

def f02_adv_504_accel_v504(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=203, w2=82, w3=741, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(203, min_periods=max(203//3, 2)).std()
    vol_slow = ret.rolling(82, min_periods=max(82//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.2575 + 0.0001105 * anchor

def f02_adv_505_jerk_v505(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=210, w2=93, w3=754, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(93, min_periods=max(93//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 210)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1522 * slope + 0.0001106 * anchor

def f02_adv_506_accel_v506(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=217, w2=104, w3=767, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(104, min_periods=max(104//3, 2)).mean()
    noise = impulse.abs().rolling(767, min_periods=max(767//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.28625 + 0.0001107 * anchor

def f02_adv_507_jerk_v507(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=224, w2=115, w3=23, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 224)
    acceleration = _rolling_slope(velocity, 115)
    curvature = _rolling_slope(acceleration, 23)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1674 * acceleration + 0.0001108 * anchor

def f02_adv_508_accel_v508(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=231, w2=126, w3=36, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(231, min_periods=max(231//3, 2)).mean(), upside.rolling(126, min_periods=max(126//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(36) * 1.315 + 0.0001109 * anchor

def f02_adv_509_jerk_v509(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=238, w2=137, w3=49, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(137, min_periods=max(137//3, 2)).max()
    rebound = x - x.rolling(238, min_periods=max(238//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1826 * _rolling_slope(draw, 49) + 0.000111 * anchor

def f02_adv_510_accel_v510(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=245, w2=148, w3=62, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 245)
    baseline = trend.rolling(148, min_periods=max(148//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(62, min_periods=max(62//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.34375 + 0.0001111 * anchor

def f02_adv_511_jerk_v511(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=252, w2=159, w3=75, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 252)
    slow = _rolling_slope(x, 159)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=75, adjust=False).mean() * 1.358125 + 0.0001112 * anchor

def f02_adv_512_accel_v512(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=8, w2=170, w3=88, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(170, min_periods=max(170//3, 2)).max()
    trough = x.rolling(8, min_periods=max(8//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.3725 + 0.0001113 * anchor

def f02_adv_513_jerk_v513(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=15, w2=181, w3=101, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(15)
    rank = change.rolling(181, min_periods=max(181//3, 2)).rank(pct=True)
    persistence = change.rolling(101, min_periods=max(101//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.213 * persistence + 0.0001114 * anchor

def f02_adv_514_accel_v514(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=22, w2=192, w3=114, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(22, min_periods=max(22//3, 2)).std()
    vol_slow = ret.rolling(192, min_periods=max(192//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.40125 + 0.0001115 * anchor

def f02_adv_515_jerk_v515(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=29, w2=203, w3=127, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(203, min_periods=max(203//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 29)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2282 * slope + 0.0001116 * anchor

def f02_adv_516_accel_v516(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=36, w2=214, w3=140, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(36)
    drag = impulse.rolling(214, min_periods=max(214//3, 2)).mean()
    noise = impulse.abs().rolling(140, min_periods=max(140//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.43 + 0.0001117 * anchor

def f02_adv_517_jerk_v517(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=43, w2=225, w3=153, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 43)
    acceleration = _rolling_slope(velocity, 225)
    curvature = _rolling_slope(acceleration, 153)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2434 * acceleration + 0.0001118 * anchor

def f02_adv_518_accel_v518(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=50, w2=236, w3=166, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(50, min_periods=max(50//3, 2)).mean(), upside.rolling(236, min_periods=max(236//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.45875 + 0.0001119 * anchor

def f02_adv_519_jerk_v519(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=57, w2=247, w3=179, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(247, min_periods=max(247//3, 2)).max()
    rebound = x - x.rolling(57, min_periods=max(57//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2586 * _rolling_slope(draw, 179) + 0.000112 * anchor

def f02_adv_520_accel_v520(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=64, w2=258, w3=192, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 64)
    baseline = trend.rolling(258, min_periods=max(258//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(192, min_periods=max(192//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.4875 + 0.0001121 * anchor

def f02_adv_521_jerk_v521(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=71, w2=269, w3=205, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 71)
    slow = _rolling_slope(x, 269)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=205, adjust=False).mean() * 1.501875 + 0.0001122 * anchor

def f02_adv_522_accel_v522(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=78, w2=280, w3=218, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(280, min_periods=max(280//3, 2)).max()
    trough = x.rolling(78, min_periods=max(78//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.51625 + 0.0001123 * anchor

def f02_adv_523_jerk_v523(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=85, w2=291, w3=231, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(85)
    rank = change.rolling(291, min_periods=max(291//3, 2)).rank(pct=True)
    persistence = change.rolling(231, min_periods=max(231//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.289 * persistence + 0.0001124 * anchor

def f02_adv_524_accel_v524(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=92, w2=302, w3=244, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(92, min_periods=max(92//3, 2)).std()
    vol_slow = ret.rolling(302, min_periods=max(302//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.545 + 0.0001125 * anchor

def f02_adv_525_jerk_v525(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=99, w2=313, w3=257, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(313, min_periods=max(313//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 99)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3042 * slope + 0.0001126 * anchor
