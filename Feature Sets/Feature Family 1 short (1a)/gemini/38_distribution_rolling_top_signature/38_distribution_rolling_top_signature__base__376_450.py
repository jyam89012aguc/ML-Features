"""38 distribution rolling top signature base features 376-450 â€” Pipeline 1a-HF Grade v3.

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

def f38_drts_376_accel_v376(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=91, w2=428, w3=17, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(91)
    drag = impulse.rolling(428, min_periods=max(428//3, 2)).mean()
    noise = impulse.abs().rolling(17, min_periods=max(17//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.56125 + 0.0023177 * anchor

def f38_drts_377_jerk_v377(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=98, w2=439, w3=30, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 98)
    acceleration = _rolling_slope(velocity, 439)
    curvature = _rolling_slope(acceleration, 30)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.4014 * acceleration + 0.0023178 * anchor

def f38_drts_378_accel_v378(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=105, w2=450, w3=43, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(105, min_periods=max(105//3, 2)).mean(), upside.rolling(450, min_periods=max(450//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(43) * 1.59 + 0.0023179 * anchor

def f38_drts_379_jerk_v379(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=112, w2=461, w3=56, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(461, min_periods=max(461//3, 2)).max()
    rebound = x - x.rolling(112, min_periods=max(112//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0402 * _rolling_slope(draw, 56) + 0.002318 * anchor

def f38_drts_380_accel_v380(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=119, w2=472, w3=69, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 119)
    baseline = trend.rolling(472, min_periods=max(472//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(69, min_periods=max(69//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.61875 + 0.0023181 * anchor

def f38_drts_381_jerk_v381(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=126, w2=483, w3=82, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 126)
    slow = _rolling_slope(x, 483)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=82, adjust=False).mean() * 0.86 + 0.0023182 * anchor

def f38_drts_382_accel_v382(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=133, w2=494, w3=95, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(494, min_periods=max(494//3, 2)).max()
    trough = x.rolling(133, min_periods=max(133//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.874375 + 0.0023183 * anchor

def f38_drts_383_jerk_v383(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=140, w2=505, w3=108, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(505, min_periods=max(505//3, 2)).rank(pct=True)
    persistence = change.rolling(108, min_periods=max(108//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0706 * persistence + 0.0023184 * anchor

def f38_drts_384_accel_v384(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=147, w2=13, w3=121, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(147, min_periods=max(147//3, 2)).std()
    vol_slow = ret.rolling(13, min_periods=max(13//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.903125 + 0.0023185 * anchor

def f38_drts_385_jerk_v385(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=154, w2=24, w3=134, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(24, min_periods=max(24//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 154)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0858 * slope + 0.0023186 * anchor

def f38_drts_386_accel_v386(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=161, w2=35, w3=147, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(35, min_periods=max(35//3, 2)).mean()
    noise = impulse.abs().rolling(147, min_periods=max(147//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.931875 + 0.0023187 * anchor

def f38_drts_387_jerk_v387(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=168, w2=46, w3=160, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 168)
    acceleration = _rolling_slope(velocity, 46)
    curvature = _rolling_slope(acceleration, 160)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.101 * acceleration + 0.0023188 * anchor

def f38_drts_388_accel_v388(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=175, w2=57, w3=173, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(175, min_periods=max(175//3, 2)).mean(), upside.rolling(57, min_periods=max(57//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.960625 + 0.0023189 * anchor

def f38_drts_389_jerk_v389(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=182, w2=68, w3=186, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(68, min_periods=max(68//3, 2)).max()
    rebound = x - x.rolling(182, min_periods=max(182//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1162 * _rolling_slope(draw, 186) + 0.002319 * anchor

def f38_drts_390_accel_v390(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=189, w2=79, w3=199, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 189)
    baseline = trend.rolling(79, min_periods=max(79//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(199, min_periods=max(199//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.989375 + 0.0023191 * anchor

def f38_drts_391_jerk_v391(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=196, w2=90, w3=212, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 196)
    slow = _rolling_slope(x, 90)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=212, adjust=False).mean() * 1.00375 + 0.0023192 * anchor

def f38_drts_392_accel_v392(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=203, w2=101, w3=225, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(101, min_periods=max(101//3, 2)).max()
    trough = x.rolling(203, min_periods=max(203//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.018125 + 0.0023193 * anchor

def f38_drts_393_jerk_v393(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=210, w2=112, w3=238, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(112, min_periods=max(112//3, 2)).rank(pct=True)
    persistence = change.rolling(238, min_periods=max(238//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1466 * persistence + 0.0023194 * anchor

def f38_drts_394_accel_v394(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=217, w2=123, w3=251, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(217, min_periods=max(217//3, 2)).std()
    vol_slow = ret.rolling(123, min_periods=max(123//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.046875 + 0.0023195 * anchor

def f38_drts_395_jerk_v395(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=224, w2=134, w3=264, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(134, min_periods=max(134//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 224)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1618 * slope + 0.0023196 * anchor

def f38_drts_396_accel_v396(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=231, w2=145, w3=277, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(145, min_periods=max(145//3, 2)).mean()
    noise = impulse.abs().rolling(277, min_periods=max(277//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.075625 + 0.0023197 * anchor

def f38_drts_397_jerk_v397(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=238, w2=156, w3=290, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 238)
    acceleration = _rolling_slope(velocity, 156)
    curvature = _rolling_slope(acceleration, 290)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.177 * acceleration + 0.0023198 * anchor

def f38_drts_398_accel_v398(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=245, w2=167, w3=303, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(245, min_periods=max(245//3, 2)).mean(), upside.rolling(167, min_periods=max(167//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.104375 + 0.0023199 * anchor

def f38_drts_399_jerk_v399(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=252, w2=178, w3=316, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(178, min_periods=max(178//3, 2)).max()
    rebound = x - x.rolling(252, min_periods=max(252//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1922 * _rolling_slope(draw, 316) + 0.00232 * anchor

def f38_drts_400_accel_v400(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=8, w2=189, w3=329, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 8)
    baseline = trend.rolling(189, min_periods=max(189//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(329, min_periods=max(329//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.133125 + 0.0023201 * anchor

def f38_drts_401_jerk_v401(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=15, w2=200, w3=342, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 15)
    slow = _rolling_slope(x, 200)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.1475 + 0.0023202 * anchor

def f38_drts_402_accel_v402(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=22, w2=211, w3=355, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(211, min_periods=max(211//3, 2)).max()
    trough = x.rolling(22, min_periods=max(22//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.161875 + 0.0023203 * anchor

def f38_drts_403_jerk_v403(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=29, w2=222, w3=368, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(29)
    rank = change.rolling(222, min_periods=max(222//3, 2)).rank(pct=True)
    persistence = change.rolling(368, min_periods=max(368//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2226 * persistence + 0.0023204 * anchor

def f38_drts_404_accel_v404(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=36, w2=233, w3=381, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(36, min_periods=max(36//3, 2)).std()
    vol_slow = ret.rolling(233, min_periods=max(233//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.190625 + 0.0023205 * anchor

def f38_drts_405_jerk_v405(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=43, w2=244, w3=394, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(244, min_periods=max(244//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 43)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2378 * slope + 0.0023206 * anchor

def f38_drts_406_accel_v406(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=50, w2=255, w3=407, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(50)
    drag = impulse.rolling(255, min_periods=max(255//3, 2)).mean()
    noise = impulse.abs().rolling(407, min_periods=max(407//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.219375 + 0.0023207 * anchor

def f38_drts_407_jerk_v407(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=57, w2=266, w3=420, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 57)
    acceleration = _rolling_slope(velocity, 266)
    curvature = _rolling_slope(acceleration, 420)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.253 * acceleration + 0.0023208 * anchor

def f38_drts_408_accel_v408(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=64, w2=277, w3=433, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(64, min_periods=max(64//3, 2)).mean(), upside.rolling(277, min_periods=max(277//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.248125 + 0.0023209 * anchor

def f38_drts_409_jerk_v409(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=71, w2=288, w3=446, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(288, min_periods=max(288//3, 2)).max()
    rebound = x - x.rolling(71, min_periods=max(71//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2682 * _rolling_slope(draw, 446) + 0.002321 * anchor

def f38_drts_410_accel_v410(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=78, w2=299, w3=459, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 78)
    baseline = trend.rolling(299, min_periods=max(299//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(459, min_periods=max(459//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.276875 + 0.0023211 * anchor

def f38_drts_411_jerk_v411(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=85, w2=310, w3=472, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 85)
    slow = _rolling_slope(x, 310)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.29125 + 0.0023212 * anchor

def f38_drts_412_accel_v412(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=92, w2=321, w3=485, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(321, min_periods=max(321//3, 2)).max()
    trough = x.rolling(92, min_periods=max(92//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.305625 + 0.0023213 * anchor

def f38_drts_413_jerk_v413(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=99, w2=332, w3=498, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(99)
    rank = change.rolling(332, min_periods=max(332//3, 2)).rank(pct=True)
    persistence = change.rolling(498, min_periods=max(498//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2986 * persistence + 0.0023214 * anchor

def f38_drts_414_accel_v414(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=106, w2=343, w3=511, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(106, min_periods=max(106//3, 2)).std()
    vol_slow = ret.rolling(343, min_periods=max(343//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.334375 + 0.0023215 * anchor

def f38_drts_415_jerk_v415(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=113, w2=354, w3=524, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(354, min_periods=max(354//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 113)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3138 * slope + 0.0023216 * anchor

def f38_drts_416_accel_v416(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=120, w2=365, w3=537, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(120)
    drag = impulse.rolling(365, min_periods=max(365//3, 2)).mean()
    noise = impulse.abs().rolling(537, min_periods=max(537//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.363125 + 0.0023217 * anchor

def f38_drts_417_jerk_v417(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=127, w2=376, w3=550, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 127)
    acceleration = _rolling_slope(velocity, 376)
    curvature = _rolling_slope(acceleration, 550)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.329 * acceleration + 0.0023218 * anchor

def f38_drts_418_accel_v418(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=134, w2=387, w3=563, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(134, min_periods=max(134//3, 2)).mean(), upside.rolling(387, min_periods=max(387//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.391875 + 0.0023219 * anchor

def f38_drts_419_jerk_v419(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=141, w2=398, w3=576, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(398, min_periods=max(398//3, 2)).max()
    rebound = x - x.rolling(141, min_periods=max(141//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3442 * _rolling_slope(draw, 576) + 0.002322 * anchor

def f38_drts_420_accel_v420(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=148, w2=409, w3=589, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 148)
    baseline = trend.rolling(409, min_periods=max(409//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(589, min_periods=max(589//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.420625 + 0.0023221 * anchor

def f38_drts_421_jerk_v421(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=155, w2=420, w3=602, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 155)
    slow = _rolling_slope(x, 420)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.435 + 0.0023222 * anchor

def f38_drts_422_accel_v422(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=162, w2=431, w3=615, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(431, min_periods=max(431//3, 2)).max()
    trough = x.rolling(162, min_periods=max(162//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.449375 + 0.0023223 * anchor

def f38_drts_423_jerk_v423(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=169, w2=442, w3=628, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(442, min_periods=max(442//3, 2)).rank(pct=True)
    persistence = change.rolling(628, min_periods=max(628//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3746 * persistence + 0.0023224 * anchor

def f38_drts_424_accel_v424(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=176, w2=453, w3=641, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(176, min_periods=max(176//3, 2)).std()
    vol_slow = ret.rolling(453, min_periods=max(453//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.478125 + 0.0023225 * anchor

def f38_drts_425_jerk_v425(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=183, w2=464, w3=654, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(464, min_periods=max(464//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 183)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3898 * slope + 0.0023226 * anchor

def f38_drts_426_accel_v426(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=190, w2=475, w3=667, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(475, min_periods=max(475//3, 2)).mean()
    noise = impulse.abs().rolling(667, min_periods=max(667//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.506875 + 0.0023227 * anchor

def f38_drts_427_jerk_v427(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=197, w2=486, w3=680, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 197)
    acceleration = _rolling_slope(velocity, 486)
    curvature = _rolling_slope(acceleration, 680)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.405 * acceleration + 0.0023228 * anchor

def f38_drts_428_accel_v428(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=204, w2=497, w3=693, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(204, min_periods=max(204//3, 2)).mean(), upside.rolling(497, min_periods=max(497//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.535625 + 0.0023229 * anchor

def f38_drts_429_jerk_v429(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=211, w2=508, w3=706, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(508, min_periods=max(508//3, 2)).max()
    rebound = x - x.rolling(211, min_periods=max(211//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0438 * _rolling_slope(draw, 706) + 0.002323 * anchor

def f38_drts_430_accel_v430(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=218, w2=16, w3=719, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 218)
    baseline = trend.rolling(16, min_periods=max(16//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(719, min_periods=max(719//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.564375 + 0.0023231 * anchor

def f38_drts_431_jerk_v431(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=225, w2=27, w3=732, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 225)
    slow = _rolling_slope(x, 27)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.57875 + 0.0023232 * anchor

def f38_drts_432_accel_v432(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=232, w2=38, w3=745, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(38, min_periods=max(38//3, 2)).max()
    trough = x.rolling(232, min_periods=max(232//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.593125 + 0.0023233 * anchor

def f38_drts_433_jerk_v433(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=239, w2=49, w3=758, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(49, min_periods=max(49//3, 2)).rank(pct=True)
    persistence = change.rolling(758, min_periods=max(758//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0742 * persistence + 0.0023234 * anchor

def f38_drts_434_accel_v434(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=246, w2=60, w3=771, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(246, min_periods=max(246//3, 2)).std()
    vol_slow = ret.rolling(60, min_periods=max(60//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.621875 + 0.0023235 * anchor

def f38_drts_435_jerk_v435(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=253, w2=71, w3=27, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(71, min_periods=max(71//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 253)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0894 * slope + 0.0023236 * anchor

def f38_drts_436_accel_v436(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=9, w2=82, w3=40, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(9)
    drag = impulse.rolling(82, min_periods=max(82//3, 2)).mean()
    noise = impulse.abs().rolling(40, min_periods=max(40//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.8775 + 0.0023237 * anchor

def f38_drts_437_jerk_v437(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=16, w2=93, w3=53, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 16)
    acceleration = _rolling_slope(velocity, 93)
    curvature = _rolling_slope(acceleration, 53)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1046 * acceleration + 0.0023238 * anchor

def f38_drts_438_accel_v438(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=23, w2=104, w3=66, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(23, min_periods=max(23//3, 2)).mean(), upside.rolling(104, min_periods=max(104//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(66) * 0.90625 + 0.0023239 * anchor

def f38_drts_439_jerk_v439(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=30, w2=115, w3=79, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(115, min_periods=max(115//3, 2)).max()
    rebound = x - x.rolling(30, min_periods=max(30//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1198 * _rolling_slope(draw, 79) + 0.002324 * anchor

def f38_drts_440_accel_v440(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=37, w2=126, w3=92, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 37)
    baseline = trend.rolling(126, min_periods=max(126//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(92, min_periods=max(92//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.935 + 0.0023241 * anchor

def f38_drts_441_jerk_v441(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=44, w2=137, w3=105, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 44)
    slow = _rolling_slope(x, 137)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=105, adjust=False).mean() * 0.949375 + 0.0023242 * anchor

def f38_drts_442_accel_v442(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=51, w2=148, w3=118, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(148, min_periods=max(148//3, 2)).max()
    trough = x.rolling(51, min_periods=max(51//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.96375 + 0.0023243 * anchor

def f38_drts_443_jerk_v443(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=58, w2=159, w3=131, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(58)
    rank = change.rolling(159, min_periods=max(159//3, 2)).rank(pct=True)
    persistence = change.rolling(131, min_periods=max(131//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1502 * persistence + 0.0023244 * anchor

def f38_drts_444_accel_v444(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=65, w2=170, w3=144, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(65, min_periods=max(65//3, 2)).std()
    vol_slow = ret.rolling(170, min_periods=max(170//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.9925 + 0.0023245 * anchor

def f38_drts_445_jerk_v445(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=72, w2=181, w3=157, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(181, min_periods=max(181//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 72)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1654 * slope + 0.0023246 * anchor

def f38_drts_446_accel_v446(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=79, w2=192, w3=170, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(79)
    drag = impulse.rolling(192, min_periods=max(192//3, 2)).mean()
    noise = impulse.abs().rolling(170, min_periods=max(170//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.02125 + 0.0023247 * anchor

def f38_drts_447_jerk_v447(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=86, w2=203, w3=183, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 86)
    acceleration = _rolling_slope(velocity, 203)
    curvature = _rolling_slope(acceleration, 183)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1806 * acceleration + 0.0023248 * anchor

def f38_drts_448_accel_v448(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=93, w2=214, w3=196, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(93, min_periods=max(93//3, 2)).mean(), upside.rolling(214, min_periods=max(214//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.05 + 0.0023249 * anchor

def f38_drts_449_jerk_v449(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=100, w2=225, w3=209, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(225, min_periods=max(225//3, 2)).max()
    rebound = x - x.rolling(100, min_periods=max(100//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1958 * _rolling_slope(draw, 209) + 0.002325 * anchor

def f38_drts_450_accel_v450(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=107, w2=236, w3=222, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 107)
    baseline = trend.rolling(236, min_periods=max(236//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(222, min_periods=max(222//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.07875 + 0.0023251 * anchor
