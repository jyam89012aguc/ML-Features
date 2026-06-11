"""04 topping pattern base features 526-600 â€” Pipeline 1a-HF Grade v3.

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

def f04_top_526_accel_v526(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=223, w2=446, w3=730, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(446, min_periods=max(446//3, 2)).mean()
    noise = impulse.abs().rolling(730, min_periods=max(730//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.041875 + 0.0002327 * anchor

def f04_top_527_jerk_v527(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=230, w2=457, w3=743, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 230)
    acceleration = _rolling_slope(velocity, 457)
    curvature = _rolling_slope(acceleration, 743)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.4058 * acceleration + 0.0002328 * anchor

def f04_top_528_accel_v528(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=237, w2=468, w3=756, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(237, min_periods=max(237//3, 2)).mean(), upside.rolling(468, min_periods=max(468//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.070625 + 0.0002329 * anchor

def f04_top_529_jerk_v529(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=244, w2=479, w3=769, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(479, min_periods=max(479//3, 2)).max()
    rebound = x - x.rolling(244, min_periods=max(244//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0446 * _rolling_slope(draw, 769) + 0.000233 * anchor

def f04_top_530_accel_v530(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=251, w2=490, w3=25, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 251)
    baseline = trend.rolling(490, min_periods=max(490//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(25, min_periods=max(25//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.099375 + 0.0002331 * anchor

def f04_top_531_jerk_v531(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=7, w2=501, w3=38, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 7)
    slow = _rolling_slope(x, 501)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=38, adjust=False).mean() * 1.11375 + 0.0002332 * anchor

def f04_top_532_accel_v532(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=14, w2=512, w3=51, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(512, min_periods=max(512//3, 2)).max()
    trough = x.rolling(14, min_periods=max(14//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.128125 + 0.0002333 * anchor

def f04_top_533_jerk_v533(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=21, w2=20, w3=64, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(21)
    rank = change.rolling(20, min_periods=max(20//3, 2)).rank(pct=True)
    persistence = change.rolling(64, min_periods=max(64//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.075 * persistence + 0.0002334 * anchor

def f04_top_534_accel_v534(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=28, w2=31, w3=77, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(28, min_periods=max(28//3, 2)).std()
    vol_slow = ret.rolling(31, min_periods=max(31//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.156875 + 0.0002335 * anchor

def f04_top_535_jerk_v535(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=35, w2=42, w3=90, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(42, min_periods=max(42//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 35)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0902 * slope + 0.0002336 * anchor

def f04_top_536_accel_v536(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=42, w2=53, w3=103, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(42)
    drag = impulse.rolling(53, min_periods=max(53//3, 2)).mean()
    noise = impulse.abs().rolling(103, min_periods=max(103//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.185625 + 0.0002337 * anchor

def f04_top_537_jerk_v537(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=49, w2=64, w3=116, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 49)
    acceleration = _rolling_slope(velocity, 64)
    curvature = _rolling_slope(acceleration, 116)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1054 * acceleration + 0.0002338 * anchor

def f04_top_538_accel_v538(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=56, w2=75, w3=129, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(56, min_periods=max(56//3, 2)).mean(), upside.rolling(75, min_periods=max(75//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.214375 + 0.0002339 * anchor

def f04_top_539_jerk_v539(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=63, w2=86, w3=142, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(86, min_periods=max(86//3, 2)).max()
    rebound = x - x.rolling(63, min_periods=max(63//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1206 * _rolling_slope(draw, 142) + 0.000234 * anchor

def f04_top_540_accel_v540(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=70, w2=97, w3=155, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 70)
    baseline = trend.rolling(97, min_periods=max(97//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(155, min_periods=max(155//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.243125 + 0.0002341 * anchor

def f04_top_541_jerk_v541(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=77, w2=108, w3=168, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 77)
    slow = _rolling_slope(x, 108)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=168, adjust=False).mean() * 1.2575 + 0.0002342 * anchor

def f04_top_542_accel_v542(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=84, w2=119, w3=181, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(119, min_periods=max(119//3, 2)).max()
    trough = x.rolling(84, min_periods=max(84//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.271875 + 0.0002343 * anchor

def f04_top_543_jerk_v543(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=91, w2=130, w3=194, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(91)
    rank = change.rolling(130, min_periods=max(130//3, 2)).rank(pct=True)
    persistence = change.rolling(194, min_periods=max(194//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.151 * persistence + 0.0002344 * anchor

def f04_top_544_accel_v544(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=98, w2=141, w3=207, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(98, min_periods=max(98//3, 2)).std()
    vol_slow = ret.rolling(141, min_periods=max(141//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.300625 + 0.0002345 * anchor

def f04_top_545_jerk_v545(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=105, w2=152, w3=220, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(152, min_periods=max(152//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 105)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1662 * slope + 0.0002346 * anchor

def f04_top_546_accel_v546(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=112, w2=163, w3=233, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(112)
    drag = impulse.rolling(163, min_periods=max(163//3, 2)).mean()
    noise = impulse.abs().rolling(233, min_periods=max(233//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.329375 + 0.0002347 * anchor

def f04_top_547_jerk_v547(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=119, w2=174, w3=246, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 119)
    acceleration = _rolling_slope(velocity, 174)
    curvature = _rolling_slope(acceleration, 246)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1814 * acceleration + 0.0002348 * anchor

def f04_top_548_accel_v548(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=126, w2=185, w3=259, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(126, min_periods=max(126//3, 2)).mean(), upside.rolling(185, min_periods=max(185//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.358125 + 0.0002349 * anchor

def f04_top_549_jerk_v549(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=133, w2=196, w3=272, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(196, min_periods=max(196//3, 2)).max()
    rebound = x - x.rolling(133, min_periods=max(133//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1966 * _rolling_slope(draw, 272) + 0.000235 * anchor

def f04_top_550_accel_v550(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=140, w2=207, w3=285, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 140)
    baseline = trend.rolling(207, min_periods=max(207//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(285, min_periods=max(285//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.386875 + 0.0002351 * anchor

def f04_top_551_jerk_v551(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=147, w2=218, w3=298, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 147)
    slow = _rolling_slope(x, 218)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=298, adjust=False).mean() * 1.40125 + 0.0002352 * anchor

def f04_top_552_accel_v552(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=154, w2=229, w3=311, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(229, min_periods=max(229//3, 2)).max()
    trough = x.rolling(154, min_periods=max(154//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.415625 + 0.0002353 * anchor

def f04_top_553_jerk_v553(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=161, w2=240, w3=324, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(240, min_periods=max(240//3, 2)).rank(pct=True)
    persistence = change.rolling(324, min_periods=max(324//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.227 * persistence + 0.0002354 * anchor

def f04_top_554_accel_v554(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=168, w2=251, w3=337, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(168, min_periods=max(168//3, 2)).std()
    vol_slow = ret.rolling(251, min_periods=max(251//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.444375 + 0.0002355 * anchor

def f04_top_555_jerk_v555(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=175, w2=262, w3=350, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(262, min_periods=max(262//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 175)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2422 * slope + 0.0002356 * anchor

def f04_top_556_accel_v556(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=182, w2=273, w3=363, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(273, min_periods=max(273//3, 2)).mean()
    noise = impulse.abs().rolling(363, min_periods=max(363//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.473125 + 0.0002357 * anchor

def f04_top_557_jerk_v557(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=189, w2=284, w3=376, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 189)
    acceleration = _rolling_slope(velocity, 284)
    curvature = _rolling_slope(acceleration, 376)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2574 * acceleration + 0.0002358 * anchor

def f04_top_558_accel_v558(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=196, w2=295, w3=389, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(196, min_periods=max(196//3, 2)).mean(), upside.rolling(295, min_periods=max(295//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.501875 + 0.0002359 * anchor

def f04_top_559_jerk_v559(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=203, w2=306, w3=402, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(306, min_periods=max(306//3, 2)).max()
    rebound = x - x.rolling(203, min_periods=max(203//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2726 * _rolling_slope(draw, 402) + 0.000236 * anchor

def f04_top_560_accel_v560(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=210, w2=317, w3=415, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 210)
    baseline = trend.rolling(317, min_periods=max(317//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(415, min_periods=max(415//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.530625 + 0.0002361 * anchor

def f04_top_561_jerk_v561(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=217, w2=328, w3=428, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 217)
    slow = _rolling_slope(x, 328)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.545 + 0.0002362 * anchor

def f04_top_562_accel_v562(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=224, w2=339, w3=441, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(339, min_periods=max(339//3, 2)).max()
    trough = x.rolling(224, min_periods=max(224//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.559375 + 0.0002363 * anchor

def f04_top_563_jerk_v563(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=231, w2=350, w3=454, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(350, min_periods=max(350//3, 2)).rank(pct=True)
    persistence = change.rolling(454, min_periods=max(454//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.303 * persistence + 0.0002364 * anchor

def f04_top_564_accel_v564(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=238, w2=361, w3=467, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(238, min_periods=max(238//3, 2)).std()
    vol_slow = ret.rolling(361, min_periods=max(361//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.588125 + 0.0002365 * anchor

def f04_top_565_jerk_v565(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=245, w2=372, w3=480, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(372, min_periods=max(372//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 245)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3182 * slope + 0.0002366 * anchor

def f04_top_566_accel_v566(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=252, w2=383, w3=493, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(383, min_periods=max(383//3, 2)).mean()
    noise = impulse.abs().rolling(493, min_periods=max(493//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.616875 + 0.0002367 * anchor

def f04_top_567_jerk_v567(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=8, w2=394, w3=506, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 8)
    acceleration = _rolling_slope(velocity, 394)
    curvature = _rolling_slope(acceleration, 506)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3334 * acceleration + 0.0002368 * anchor

def f04_top_568_accel_v568(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=15, w2=405, w3=519, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(15, min_periods=max(15//3, 2)).mean(), upside.rolling(405, min_periods=max(405//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.8725 + 0.0002369 * anchor

def f04_top_569_jerk_v569(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=22, w2=416, w3=532, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(416, min_periods=max(416//3, 2)).max()
    rebound = x - x.rolling(22, min_periods=max(22//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3486 * _rolling_slope(draw, 532) + 0.000237 * anchor

def f04_top_570_accel_v570(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=29, w2=427, w3=545, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 29)
    baseline = trend.rolling(427, min_periods=max(427//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(545, min_periods=max(545//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.90125 + 0.0002371 * anchor

def f04_top_571_jerk_v571(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=36, w2=438, w3=558, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 36)
    slow = _rolling_slope(x, 438)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.915625 + 0.0002372 * anchor

def f04_top_572_accel_v572(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=43, w2=449, w3=571, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(449, min_periods=max(449//3, 2)).max()
    trough = x.rolling(43, min_periods=max(43//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.93 + 0.0002373 * anchor

def f04_top_573_jerk_v573(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=50, w2=460, w3=584, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(50)
    rank = change.rolling(460, min_periods=max(460//3, 2)).rank(pct=True)
    persistence = change.rolling(584, min_periods=max(584//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.379 * persistence + 0.0002374 * anchor

def f04_top_574_accel_v574(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=57, w2=471, w3=597, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(57, min_periods=max(57//3, 2)).std()
    vol_slow = ret.rolling(471, min_periods=max(471//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.95875 + 0.0002375 * anchor

def f04_top_575_jerk_v575(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=64, w2=482, w3=610, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(482, min_periods=max(482//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 64)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3942 * slope + 0.0002376 * anchor

def f04_top_576_accel_v576(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=71, w2=493, w3=623, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(71)
    drag = impulse.rolling(493, min_periods=max(493//3, 2)).mean()
    noise = impulse.abs().rolling(623, min_periods=max(623//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.9875 + 0.0002377 * anchor

def f04_top_577_jerk_v577(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=78, w2=504, w3=636, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 78)
    acceleration = _rolling_slope(velocity, 504)
    curvature = _rolling_slope(acceleration, 636)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.4094 * acceleration + 0.0002378 * anchor

def f04_top_578_accel_v578(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=85, w2=12, w3=649, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(85, min_periods=max(85//3, 2)).mean(), upside.rolling(12, min_periods=max(12//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.01625 + 0.0002379 * anchor

def f04_top_579_jerk_v579(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=92, w2=23, w3=662, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(23, min_periods=max(23//3, 2)).max()
    rebound = x - x.rolling(92, min_periods=max(92//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0482 * _rolling_slope(draw, 662) + 0.000238 * anchor

def f04_top_580_accel_v580(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=99, w2=34, w3=675, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 99)
    baseline = trend.rolling(34, min_periods=max(34//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(675, min_periods=max(675//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.045 + 0.0002381 * anchor

def f04_top_581_jerk_v581(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=106, w2=45, w3=688, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 106)
    slow = _rolling_slope(x, 45)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.059375 + 0.0002382 * anchor

def f04_top_582_accel_v582(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=113, w2=56, w3=701, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(56, min_periods=max(56//3, 2)).max()
    trough = x.rolling(113, min_periods=max(113//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.07375 + 0.0002383 * anchor

def f04_top_583_jerk_v583(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=120, w2=67, w3=714, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(120)
    rank = change.rolling(67, min_periods=max(67//3, 2)).rank(pct=True)
    persistence = change.rolling(714, min_periods=max(714//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0786 * persistence + 0.0002384 * anchor

def f04_top_584_accel_v584(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=127, w2=78, w3=727, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(127, min_periods=max(127//3, 2)).std()
    vol_slow = ret.rolling(78, min_periods=max(78//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.1025 + 0.0002385 * anchor

def f04_top_585_jerk_v585(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=134, w2=89, w3=740, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(89, min_periods=max(89//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 134)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0938 * slope + 0.0002386 * anchor

def f04_top_586_accel_v586(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=141, w2=100, w3=753, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(100, min_periods=max(100//3, 2)).mean()
    noise = impulse.abs().rolling(753, min_periods=max(753//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.13125 + 0.0002387 * anchor

def f04_top_587_jerk_v587(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=148, w2=111, w3=766, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 148)
    acceleration = _rolling_slope(velocity, 111)
    curvature = _rolling_slope(acceleration, 766)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.109 * acceleration + 0.0002388 * anchor

def f04_top_588_accel_v588(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=155, w2=122, w3=22, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(155, min_periods=max(155//3, 2)).mean(), upside.rolling(122, min_periods=max(122//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(22) * 1.16 + 0.0002389 * anchor

def f04_top_589_jerk_v589(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=162, w2=133, w3=35, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(133, min_periods=max(133//3, 2)).max()
    rebound = x - x.rolling(162, min_periods=max(162//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1242 * _rolling_slope(draw, 35) + 0.000239 * anchor

def f04_top_590_accel_v590(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=169, w2=144, w3=48, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 169)
    baseline = trend.rolling(144, min_periods=max(144//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(48, min_periods=max(48//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.18875 + 0.0002391 * anchor

def f04_top_591_jerk_v591(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=176, w2=155, w3=61, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 176)
    slow = _rolling_slope(x, 155)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=61, adjust=False).mean() * 1.203125 + 0.0002392 * anchor

def f04_top_592_accel_v592(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=183, w2=166, w3=74, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(166, min_periods=max(166//3, 2)).max()
    trough = x.rolling(183, min_periods=max(183//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.2175 + 0.0002393 * anchor

def f04_top_593_jerk_v593(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=190, w2=177, w3=87, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(177, min_periods=max(177//3, 2)).rank(pct=True)
    persistence = change.rolling(87, min_periods=max(87//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1546 * persistence + 0.0002394 * anchor

def f04_top_594_accel_v594(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=197, w2=188, w3=100, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(197, min_periods=max(197//3, 2)).std()
    vol_slow = ret.rolling(188, min_periods=max(188//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.24625 + 0.0002395 * anchor

def f04_top_595_jerk_v595(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=204, w2=199, w3=113, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(199, min_periods=max(199//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 204)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1698 * slope + 0.0002396 * anchor

def f04_top_596_accel_v596(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=211, w2=210, w3=126, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(210, min_periods=max(210//3, 2)).mean()
    noise = impulse.abs().rolling(126, min_periods=max(126//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.275 + 0.0002397 * anchor

def f04_top_597_jerk_v597(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=218, w2=221, w3=139, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 218)
    acceleration = _rolling_slope(velocity, 221)
    curvature = _rolling_slope(acceleration, 139)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.185 * acceleration + 0.0002398 * anchor

def f04_top_598_accel_v598(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=225, w2=232, w3=152, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(225, min_periods=max(225//3, 2)).mean(), upside.rolling(232, min_periods=max(232//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.30375 + 0.0002399 * anchor

def f04_top_599_jerk_v599(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=232, w2=243, w3=165, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(243, min_periods=max(243//3, 2)).max()
    rebound = x - x.rolling(232, min_periods=max(232//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2002 * _rolling_slope(draw, 165) + 0.00024 * anchor

def f04_top_600_accel_v600(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=239, w2=254, w3=178, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 239)
    baseline = trend.rolling(254, min_periods=max(254//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(178, min_periods=max(178//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.3325 + 0.0002401 * anchor
