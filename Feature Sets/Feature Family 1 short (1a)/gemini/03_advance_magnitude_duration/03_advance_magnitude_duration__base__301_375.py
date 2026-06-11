"""03 advance magnitude duration base features 301-375 â€” Pipeline 1a-HF Grade v3.

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

def f03_amd_301_jerk_v301(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=221, w2=425, w3=603, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 221)
    slow = _rolling_slope(x, 425)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.5525 + 0.0001502 * anchor

def f03_amd_302_accel_v302(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=228, w2=436, w3=616, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(436, min_periods=max(436//3, 2)).max()
    trough = x.rolling(228, min_periods=max(228//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.566875 + 0.0001503 * anchor

def f03_amd_303_jerk_v303(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=235, w2=447, w3=629, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(447, min_periods=max(447//3, 2)).rank(pct=True)
    persistence = change.rolling(629, min_periods=max(629//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1658 * persistence + 0.0001504 * anchor

def f03_amd_304_accel_v304(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=242, w2=458, w3=642, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(242, min_periods=max(242//3, 2)).std()
    vol_slow = ret.rolling(458, min_periods=max(458//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.595625 + 0.0001505 * anchor

def f03_amd_305_jerk_v305(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=249, w2=469, w3=655, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(469, min_periods=max(469//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 249)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.181 * slope + 0.0001506 * anchor

def f03_amd_306_accel_v306(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=5, w2=480, w3=668, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(5)
    drag = impulse.rolling(480, min_periods=max(480//3, 2)).mean()
    noise = impulse.abs().rolling(668, min_periods=max(668//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.85125 + 0.0001507 * anchor

def f03_amd_307_jerk_v307(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=12, w2=491, w3=681, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 12)
    acceleration = _rolling_slope(velocity, 491)
    curvature = _rolling_slope(acceleration, 681)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1962 * acceleration + 0.0001508 * anchor

def f03_amd_308_accel_v308(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=19, w2=502, w3=694, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(19, min_periods=max(19//3, 2)).mean(), upside.rolling(502, min_periods=max(502//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.88 + 0.0001509 * anchor

def f03_amd_309_jerk_v309(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=26, w2=10, w3=707, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(10, min_periods=max(10//3, 2)).max()
    rebound = x - x.rolling(26, min_periods=max(26//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2114 * _rolling_slope(draw, 707) + 0.000151 * anchor

def f03_amd_310_accel_v310(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=33, w2=21, w3=720, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 33)
    baseline = trend.rolling(21, min_periods=max(21//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(720, min_periods=max(720//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.90875 + 0.0001511 * anchor

def f03_amd_311_jerk_v311(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=40, w2=32, w3=733, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 40)
    slow = _rolling_slope(x, 32)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.923125 + 0.0001512 * anchor

def f03_amd_312_accel_v312(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=47, w2=43, w3=746, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(43, min_periods=max(43//3, 2)).max()
    trough = x.rolling(47, min_periods=max(47//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.9375 + 0.0001513 * anchor

def f03_amd_313_jerk_v313(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=54, w2=54, w3=759, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(54)
    rank = change.rolling(54, min_periods=max(54//3, 2)).rank(pct=True)
    persistence = change.rolling(759, min_periods=max(759//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2418 * persistence + 0.0001514 * anchor

def f03_amd_314_accel_v314(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=61, w2=65, w3=15, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(61, min_periods=max(61//3, 2)).std()
    vol_slow = ret.rolling(65, min_periods=max(65//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.96625 + 0.0001515 * anchor

def f03_amd_315_jerk_v315(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=68, w2=76, w3=28, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(76, min_periods=max(76//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 68)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.257 * slope + 0.0001516 * anchor

def f03_amd_316_accel_v316(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=75, w2=87, w3=41, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(75)
    drag = impulse.rolling(87, min_periods=max(87//3, 2)).mean()
    noise = impulse.abs().rolling(41, min_periods=max(41//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.995 + 0.0001517 * anchor

def f03_amd_317_jerk_v317(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=82, w2=98, w3=54, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 82)
    acceleration = _rolling_slope(velocity, 98)
    curvature = _rolling_slope(acceleration, 54)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2722 * acceleration + 0.0001518 * anchor

def f03_amd_318_accel_v318(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=89, w2=109, w3=67, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(89, min_periods=max(89//3, 2)).mean(), upside.rolling(109, min_periods=max(109//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(67) * 1.02375 + 0.0001519 * anchor

def f03_amd_319_jerk_v319(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=96, w2=120, w3=80, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(120, min_periods=max(120//3, 2)).max()
    rebound = x - x.rolling(96, min_periods=max(96//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2874 * _rolling_slope(draw, 80) + 0.000152 * anchor

def f03_amd_320_accel_v320(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=103, w2=131, w3=93, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 103)
    baseline = trend.rolling(131, min_periods=max(131//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(93, min_periods=max(93//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.0525 + 0.0001521 * anchor

def f03_amd_321_jerk_v321(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=110, w2=142, w3=106, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 110)
    slow = _rolling_slope(x, 142)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=106, adjust=False).mean() * 1.066875 + 0.0001522 * anchor

def f03_amd_322_accel_v322(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=117, w2=153, w3=119, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(153, min_periods=max(153//3, 2)).max()
    trough = x.rolling(117, min_periods=max(117//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.08125 + 0.0001523 * anchor

def f03_amd_323_jerk_v323(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=124, w2=164, w3=132, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(124)
    rank = change.rolling(164, min_periods=max(164//3, 2)).rank(pct=True)
    persistence = change.rolling(132, min_periods=max(132//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3178 * persistence + 0.0001524 * anchor

def f03_amd_324_accel_v324(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=131, w2=175, w3=145, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(131, min_periods=max(131//3, 2)).std()
    vol_slow = ret.rolling(175, min_periods=max(175//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.11 + 0.0001525 * anchor

def f03_amd_325_jerk_v325(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=138, w2=186, w3=158, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(186, min_periods=max(186//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 138)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.333 * slope + 0.0001526 * anchor

def f03_amd_326_accel_v326(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=145, w2=197, w3=171, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(197, min_periods=max(197//3, 2)).mean()
    noise = impulse.abs().rolling(171, min_periods=max(171//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.13875 + 0.0001527 * anchor

def f03_amd_327_jerk_v327(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=152, w2=208, w3=184, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 152)
    acceleration = _rolling_slope(velocity, 208)
    curvature = _rolling_slope(acceleration, 184)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3482 * acceleration + 0.0001528 * anchor

def f03_amd_328_accel_v328(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=159, w2=219, w3=197, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(159, min_periods=max(159//3, 2)).mean(), upside.rolling(219, min_periods=max(219//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.1675 + 0.0001529 * anchor

def f03_amd_329_jerk_v329(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=166, w2=230, w3=210, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(230, min_periods=max(230//3, 2)).max()
    rebound = x - x.rolling(166, min_periods=max(166//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3634 * _rolling_slope(draw, 210) + 0.000153 * anchor

def f03_amd_330_accel_v330(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=173, w2=241, w3=223, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 173)
    baseline = trend.rolling(241, min_periods=max(241//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(223, min_periods=max(223//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.19625 + 0.0001531 * anchor

def f03_amd_331_jerk_v331(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=180, w2=252, w3=236, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 180)
    slow = _rolling_slope(x, 252)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=236, adjust=False).mean() * 1.210625 + 0.0001532 * anchor

def f03_amd_332_accel_v332(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=187, w2=263, w3=249, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(263, min_periods=max(263//3, 2)).max()
    trough = x.rolling(187, min_periods=max(187//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.225 + 0.0001533 * anchor

def f03_amd_333_jerk_v333(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=194, w2=274, w3=262, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(274, min_periods=max(274//3, 2)).rank(pct=True)
    persistence = change.rolling(262, min_periods=max(262//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3938 * persistence + 0.0001534 * anchor

def f03_amd_334_accel_v334(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=201, w2=285, w3=275, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(201, min_periods=max(201//3, 2)).std()
    vol_slow = ret.rolling(285, min_periods=max(285//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.25375 + 0.0001535 * anchor

def f03_amd_335_jerk_v335(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=208, w2=296, w3=288, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(296, min_periods=max(296//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 208)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.409 * slope + 0.0001536 * anchor

def f03_amd_336_accel_v336(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=215, w2=307, w3=301, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(307, min_periods=max(307//3, 2)).mean()
    noise = impulse.abs().rolling(301, min_periods=max(301//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.2825 + 0.0001537 * anchor

def f03_amd_337_jerk_v337(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=222, w2=318, w3=314, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 222)
    acceleration = _rolling_slope(velocity, 318)
    curvature = _rolling_slope(acceleration, 314)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0478 * acceleration + 0.0001538 * anchor

def f03_amd_338_accel_v338(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=229, w2=329, w3=327, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(229, min_periods=max(229//3, 2)).mean(), upside.rolling(329, min_periods=max(329//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.31125 + 0.0001539 * anchor

def f03_amd_339_jerk_v339(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=236, w2=340, w3=340, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(340, min_periods=max(340//3, 2)).max()
    rebound = x - x.rolling(236, min_periods=max(236//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.063 * _rolling_slope(draw, 340) + 0.000154 * anchor

def f03_amd_340_accel_v340(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=243, w2=351, w3=353, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 243)
    baseline = trend.rolling(351, min_periods=max(351//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(353, min_periods=max(353//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.34 + 0.0001541 * anchor

def f03_amd_341_jerk_v341(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=250, w2=362, w3=366, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 250)
    slow = _rolling_slope(x, 362)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.354375 + 0.0001542 * anchor

def f03_amd_342_accel_v342(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=6, w2=373, w3=379, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(373, min_periods=max(373//3, 2)).max()
    trough = x.rolling(6, min_periods=max(6//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.36875 + 0.0001543 * anchor

def f03_amd_343_jerk_v343(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=13, w2=384, w3=392, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(13)
    rank = change.rolling(384, min_periods=max(384//3, 2)).rank(pct=True)
    persistence = change.rolling(392, min_periods=max(392//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0934 * persistence + 0.0001544 * anchor

def f03_amd_344_accel_v344(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=20, w2=395, w3=405, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(20, min_periods=max(20//3, 2)).std()
    vol_slow = ret.rolling(395, min_periods=max(395//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.3975 + 0.0001545 * anchor

def f03_amd_345_jerk_v345(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=27, w2=406, w3=418, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(406, min_periods=max(406//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 27)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1086 * slope + 0.0001546 * anchor

def f03_amd_346_accel_v346(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=34, w2=417, w3=431, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(34)
    drag = impulse.rolling(417, min_periods=max(417//3, 2)).mean()
    noise = impulse.abs().rolling(431, min_periods=max(431//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.42625 + 0.0001547 * anchor

def f03_amd_347_jerk_v347(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=41, w2=428, w3=444, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 41)
    acceleration = _rolling_slope(velocity, 428)
    curvature = _rolling_slope(acceleration, 444)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1238 * acceleration + 0.0001548 * anchor

def f03_amd_348_accel_v348(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=48, w2=439, w3=457, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(48, min_periods=max(48//3, 2)).mean(), upside.rolling(439, min_periods=max(439//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.455 + 0.0001549 * anchor

def f03_amd_349_jerk_v349(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=55, w2=450, w3=470, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(450, min_periods=max(450//3, 2)).max()
    rebound = x - x.rolling(55, min_periods=max(55//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.139 * _rolling_slope(draw, 470) + 0.000155 * anchor

def f03_amd_350_accel_v350(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=62, w2=461, w3=483, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 62)
    baseline = trend.rolling(461, min_periods=max(461//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(483, min_periods=max(483//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.48375 + 0.0001551 * anchor

def f03_amd_351_jerk_v351(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=69, w2=472, w3=496, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 69)
    slow = _rolling_slope(x, 472)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.498125 + 0.0001552 * anchor

def f03_amd_352_accel_v352(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=76, w2=483, w3=509, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(483, min_periods=max(483//3, 2)).max()
    trough = x.rolling(76, min_periods=max(76//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.5125 + 0.0001553 * anchor

def f03_amd_353_jerk_v353(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=83, w2=494, w3=522, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(83)
    rank = change.rolling(494, min_periods=max(494//3, 2)).rank(pct=True)
    persistence = change.rolling(522, min_periods=max(522//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1694 * persistence + 0.0001554 * anchor

def f03_amd_354_accel_v354(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=90, w2=505, w3=535, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(90, min_periods=max(90//3, 2)).std()
    vol_slow = ret.rolling(505, min_periods=max(505//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.54125 + 0.0001555 * anchor

def f03_amd_355_jerk_v355(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=97, w2=13, w3=548, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(13, min_periods=max(13//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 97)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1846 * slope + 0.0001556 * anchor

def f03_amd_356_accel_v356(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=104, w2=24, w3=561, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(104)
    drag = impulse.rolling(24, min_periods=max(24//3, 2)).mean()
    noise = impulse.abs().rolling(561, min_periods=max(561//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.57 + 0.0001557 * anchor

def f03_amd_357_jerk_v357(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=111, w2=35, w3=574, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 111)
    acceleration = _rolling_slope(velocity, 35)
    curvature = _rolling_slope(acceleration, 574)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1998 * acceleration + 0.0001558 * anchor

def f03_amd_358_accel_v358(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=118, w2=46, w3=587, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(118, min_periods=max(118//3, 2)).mean(), upside.rolling(46, min_periods=max(46//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.59875 + 0.0001559 * anchor

def f03_amd_359_jerk_v359(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=125, w2=57, w3=600, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(57, min_periods=max(57//3, 2)).max()
    rebound = x - x.rolling(125, min_periods=max(125//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.215 * _rolling_slope(draw, 600) + 0.000156 * anchor

def f03_amd_360_accel_v360(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=132, w2=68, w3=613, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 132)
    baseline = trend.rolling(68, min_periods=max(68//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(613, min_periods=max(613//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.854375 + 0.0001561 * anchor

def f03_amd_361_jerk_v361(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=139, w2=79, w3=626, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 139)
    slow = _rolling_slope(x, 79)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.86875 + 0.0001562 * anchor

def f03_amd_362_accel_v362(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=146, w2=90, w3=639, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(90, min_periods=max(90//3, 2)).max()
    trough = x.rolling(146, min_periods=max(146//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.883125 + 0.0001563 * anchor

def f03_amd_363_jerk_v363(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=153, w2=101, w3=652, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(101, min_periods=max(101//3, 2)).rank(pct=True)
    persistence = change.rolling(652, min_periods=max(652//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2454 * persistence + 0.0001564 * anchor

def f03_amd_364_accel_v364(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=160, w2=112, w3=665, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(160, min_periods=max(160//3, 2)).std()
    vol_slow = ret.rolling(112, min_periods=max(112//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.911875 + 0.0001565 * anchor

def f03_amd_365_jerk_v365(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=167, w2=123, w3=678, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(123, min_periods=max(123//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 167)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2606 * slope + 0.0001566 * anchor

def f03_amd_366_accel_v366(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=174, w2=134, w3=691, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(134, min_periods=max(134//3, 2)).mean()
    noise = impulse.abs().rolling(691, min_periods=max(691//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.940625 + 0.0001567 * anchor

def f03_amd_367_jerk_v367(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=181, w2=145, w3=704, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 181)
    acceleration = _rolling_slope(velocity, 145)
    curvature = _rolling_slope(acceleration, 704)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2758 * acceleration + 0.0001568 * anchor

def f03_amd_368_accel_v368(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=188, w2=156, w3=717, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(188, min_periods=max(188//3, 2)).mean(), upside.rolling(156, min_periods=max(156//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.969375 + 0.0001569 * anchor

def f03_amd_369_jerk_v369(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=195, w2=167, w3=730, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(167, min_periods=max(167//3, 2)).max()
    rebound = x - x.rolling(195, min_periods=max(195//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.291 * _rolling_slope(draw, 730) + 0.000157 * anchor

def f03_amd_370_accel_v370(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=202, w2=178, w3=743, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 202)
    baseline = trend.rolling(178, min_periods=max(178//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(743, min_periods=max(743//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.998125 + 0.0001571 * anchor

def f03_amd_371_jerk_v371(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=209, w2=189, w3=756, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 209)
    slow = _rolling_slope(x, 189)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.0125 + 0.0001572 * anchor

def f03_amd_372_accel_v372(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=216, w2=200, w3=769, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(200, min_periods=max(200//3, 2)).max()
    trough = x.rolling(216, min_periods=max(216//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.026875 + 0.0001573 * anchor

def f03_amd_373_jerk_v373(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=223, w2=211, w3=25, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(211, min_periods=max(211//3, 2)).rank(pct=True)
    persistence = change.rolling(25, min_periods=max(25//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3214 * persistence + 0.0001574 * anchor

def f03_amd_374_accel_v374(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=230, w2=222, w3=38, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(230, min_periods=max(230//3, 2)).std()
    vol_slow = ret.rolling(222, min_periods=max(222//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.055625 + 0.0001575 * anchor

def f03_amd_375_jerk_v375(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=237, w2=233, w3=51, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(233, min_periods=max(233//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 237)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3366 * slope + 0.0001576 * anchor
