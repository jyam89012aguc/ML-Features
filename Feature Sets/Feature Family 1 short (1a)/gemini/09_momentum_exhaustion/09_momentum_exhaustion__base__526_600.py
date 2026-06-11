"""09 momentum exhaustion base features 526-600 â€” Pipeline 1a-HF Grade v3.

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

def f09_mex_526_accel_v526(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=139, w2=248, w3=366, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(248, min_periods=max(248//3, 2)).mean()
    noise = impulse.abs().rolling(366, min_periods=max(366//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.871875 + 0.0005327 * anchor

def f09_mex_527_jerk_v527(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=146, w2=259, w3=379, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 146)
    acceleration = _rolling_slope(velocity, 259)
    curvature = _rolling_slope(acceleration, 379)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2454 * acceleration + 0.0005328 * anchor

def f09_mex_528_accel_v528(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=153, w2=270, w3=392, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(153, min_periods=max(153//3, 2)).mean(), upside.rolling(270, min_periods=max(270//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.900625 + 0.0005329 * anchor

def f09_mex_529_jerk_v529(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=160, w2=281, w3=405, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(281, min_periods=max(281//3, 2)).max()
    rebound = x - x.rolling(160, min_periods=max(160//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2606 * _rolling_slope(draw, 405) + 0.000533 * anchor

def f09_mex_530_accel_v530(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=167, w2=292, w3=418, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 167)
    baseline = trend.rolling(292, min_periods=max(292//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(418, min_periods=max(418//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.929375 + 0.0005331 * anchor

def f09_mex_531_jerk_v531(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=174, w2=303, w3=431, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 174)
    slow = _rolling_slope(x, 303)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.94375 + 0.0005332 * anchor

def f09_mex_532_accel_v532(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=181, w2=314, w3=444, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(314, min_periods=max(314//3, 2)).max()
    trough = x.rolling(181, min_periods=max(181//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.958125 + 0.0005333 * anchor

def f09_mex_533_jerk_v533(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=188, w2=325, w3=457, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(325, min_periods=max(325//3, 2)).rank(pct=True)
    persistence = change.rolling(457, min_periods=max(457//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.291 * persistence + 0.0005334 * anchor

def f09_mex_534_accel_v534(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=195, w2=336, w3=470, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(195, min_periods=max(195//3, 2)).std()
    vol_slow = ret.rolling(336, min_periods=max(336//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.986875 + 0.0005335 * anchor

def f09_mex_535_jerk_v535(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=202, w2=347, w3=483, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(347, min_periods=max(347//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 202)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3062 * slope + 0.0005336 * anchor

def f09_mex_536_accel_v536(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=209, w2=358, w3=496, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(358, min_periods=max(358//3, 2)).mean()
    noise = impulse.abs().rolling(496, min_periods=max(496//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.015625 + 0.0005337 * anchor

def f09_mex_537_jerk_v537(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=216, w2=369, w3=509, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 216)
    acceleration = _rolling_slope(velocity, 369)
    curvature = _rolling_slope(acceleration, 509)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3214 * acceleration + 0.0005338 * anchor

def f09_mex_538_accel_v538(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=223, w2=380, w3=522, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(223, min_periods=max(223//3, 2)).mean(), upside.rolling(380, min_periods=max(380//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.044375 + 0.0005339 * anchor

def f09_mex_539_jerk_v539(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=230, w2=391, w3=535, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(391, min_periods=max(391//3, 2)).max()
    rebound = x - x.rolling(230, min_periods=max(230//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3366 * _rolling_slope(draw, 535) + 0.000534 * anchor

def f09_mex_540_accel_v540(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=237, w2=402, w3=548, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 237)
    baseline = trend.rolling(402, min_periods=max(402//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(548, min_periods=max(548//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.073125 + 0.0005341 * anchor

def f09_mex_541_jerk_v541(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=244, w2=413, w3=561, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 244)
    slow = _rolling_slope(x, 413)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.0875 + 0.0005342 * anchor

def f09_mex_542_accel_v542(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=251, w2=424, w3=574, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(424, min_periods=max(424//3, 2)).max()
    trough = x.rolling(251, min_periods=max(251//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.101875 + 0.0005343 * anchor

def f09_mex_543_jerk_v543(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=7, w2=435, w3=587, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(7)
    rank = change.rolling(435, min_periods=max(435//3, 2)).rank(pct=True)
    persistence = change.rolling(587, min_periods=max(587//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.367 * persistence + 0.0005344 * anchor

def f09_mex_544_accel_v544(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=14, w2=446, w3=600, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(14, min_periods=max(14//3, 2)).std()
    vol_slow = ret.rolling(446, min_periods=max(446//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.130625 + 0.0005345 * anchor

def f09_mex_545_jerk_v545(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=21, w2=457, w3=613, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(457, min_periods=max(457//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 21)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3822 * slope + 0.0005346 * anchor

def f09_mex_546_accel_v546(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=28, w2=468, w3=626, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(28)
    drag = impulse.rolling(468, min_periods=max(468//3, 2)).mean()
    noise = impulse.abs().rolling(626, min_periods=max(626//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.159375 + 0.0005347 * anchor

def f09_mex_547_jerk_v547(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=35, w2=479, w3=639, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 35)
    acceleration = _rolling_slope(velocity, 479)
    curvature = _rolling_slope(acceleration, 639)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3974 * acceleration + 0.0005348 * anchor

def f09_mex_548_accel_v548(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=42, w2=490, w3=652, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(42, min_periods=max(42//3, 2)).mean(), upside.rolling(490, min_periods=max(490//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.188125 + 0.0005349 * anchor

def f09_mex_549_jerk_v549(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=49, w2=501, w3=665, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(501, min_periods=max(501//3, 2)).max()
    rebound = x - x.rolling(49, min_periods=max(49//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0362 * _rolling_slope(draw, 665) + 0.000535 * anchor

def f09_mex_550_accel_v550(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=56, w2=512, w3=678, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 56)
    baseline = trend.rolling(512, min_periods=max(512//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(678, min_periods=max(678//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.216875 + 0.0005351 * anchor

def f09_mex_551_jerk_v551(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=63, w2=20, w3=691, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 63)
    slow = _rolling_slope(x, 20)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.23125 + 0.0005352 * anchor

def f09_mex_552_accel_v552(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=70, w2=31, w3=704, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(31, min_periods=max(31//3, 2)).max()
    trough = x.rolling(70, min_periods=max(70//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.245625 + 0.0005353 * anchor

def f09_mex_553_jerk_v553(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=77, w2=42, w3=717, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(77)
    rank = change.rolling(42, min_periods=max(42//3, 2)).rank(pct=True)
    persistence = change.rolling(717, min_periods=max(717//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0666 * persistence + 0.0005354 * anchor

def f09_mex_554_accel_v554(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=84, w2=53, w3=730, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(84, min_periods=max(84//3, 2)).std()
    vol_slow = ret.rolling(53, min_periods=max(53//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.274375 + 0.0005355 * anchor

def f09_mex_555_jerk_v555(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=91, w2=64, w3=743, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(64, min_periods=max(64//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 91)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0818 * slope + 0.0005356 * anchor

def f09_mex_556_accel_v556(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=98, w2=75, w3=756, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(98)
    drag = impulse.rolling(75, min_periods=max(75//3, 2)).mean()
    noise = impulse.abs().rolling(756, min_periods=max(756//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.303125 + 0.0005357 * anchor

def f09_mex_557_jerk_v557(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=105, w2=86, w3=769, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 105)
    acceleration = _rolling_slope(velocity, 86)
    curvature = _rolling_slope(acceleration, 769)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.097 * acceleration + 0.0005358 * anchor

def f09_mex_558_accel_v558(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=112, w2=97, w3=25, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(112, min_periods=max(112//3, 2)).mean(), upside.rolling(97, min_periods=max(97//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(25) * 1.331875 + 0.0005359 * anchor

def f09_mex_559_jerk_v559(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=119, w2=108, w3=38, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(108, min_periods=max(108//3, 2)).max()
    rebound = x - x.rolling(119, min_periods=max(119//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1122 * _rolling_slope(draw, 38) + 0.000536 * anchor

def f09_mex_560_accel_v560(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=126, w2=119, w3=51, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 126)
    baseline = trend.rolling(119, min_periods=max(119//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(51, min_periods=max(51//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.360625 + 0.0005361 * anchor

def f09_mex_561_jerk_v561(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=133, w2=130, w3=64, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 133)
    slow = _rolling_slope(x, 130)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=64, adjust=False).mean() * 1.375 + 0.0005362 * anchor

def f09_mex_562_accel_v562(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=140, w2=141, w3=77, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(141, min_periods=max(141//3, 2)).max()
    trough = x.rolling(140, min_periods=max(140//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.389375 + 0.0005363 * anchor

def f09_mex_563_jerk_v563(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=147, w2=152, w3=90, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(152, min_periods=max(152//3, 2)).rank(pct=True)
    persistence = change.rolling(90, min_periods=max(90//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1426 * persistence + 0.0005364 * anchor

def f09_mex_564_accel_v564(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=154, w2=163, w3=103, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(154, min_periods=max(154//3, 2)).std()
    vol_slow = ret.rolling(163, min_periods=max(163//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.418125 + 0.0005365 * anchor

def f09_mex_565_jerk_v565(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=161, w2=174, w3=116, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(174, min_periods=max(174//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 161)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1578 * slope + 0.0005366 * anchor

def f09_mex_566_accel_v566(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=168, w2=185, w3=129, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(185, min_periods=max(185//3, 2)).mean()
    noise = impulse.abs().rolling(129, min_periods=max(129//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.446875 + 0.0005367 * anchor

def f09_mex_567_jerk_v567(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=175, w2=196, w3=142, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 175)
    acceleration = _rolling_slope(velocity, 196)
    curvature = _rolling_slope(acceleration, 142)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.173 * acceleration + 0.0005368 * anchor

def f09_mex_568_accel_v568(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=182, w2=207, w3=155, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(182, min_periods=max(182//3, 2)).mean(), upside.rolling(207, min_periods=max(207//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.475625 + 0.0005369 * anchor

def f09_mex_569_jerk_v569(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=189, w2=218, w3=168, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(218, min_periods=max(218//3, 2)).max()
    rebound = x - x.rolling(189, min_periods=max(189//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1882 * _rolling_slope(draw, 168) + 0.000537 * anchor

def f09_mex_570_accel_v570(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=196, w2=229, w3=181, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 196)
    baseline = trend.rolling(229, min_periods=max(229//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(181, min_periods=max(181//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.504375 + 0.0005371 * anchor

def f09_mex_571_jerk_v571(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=203, w2=240, w3=194, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 203)
    slow = _rolling_slope(x, 240)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=194, adjust=False).mean() * 1.51875 + 0.0005372 * anchor

def f09_mex_572_accel_v572(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=210, w2=251, w3=207, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(251, min_periods=max(251//3, 2)).max()
    trough = x.rolling(210, min_periods=max(210//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.533125 + 0.0005373 * anchor

def f09_mex_573_jerk_v573(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=217, w2=262, w3=220, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(262, min_periods=max(262//3, 2)).rank(pct=True)
    persistence = change.rolling(220, min_periods=max(220//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2186 * persistence + 0.0005374 * anchor

def f09_mex_574_accel_v574(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=224, w2=273, w3=233, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(224, min_periods=max(224//3, 2)).std()
    vol_slow = ret.rolling(273, min_periods=max(273//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.561875 + 0.0005375 * anchor

def f09_mex_575_jerk_v575(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=231, w2=284, w3=246, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(284, min_periods=max(284//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 231)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2338 * slope + 0.0005376 * anchor

def f09_mex_576_accel_v576(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=238, w2=295, w3=259, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(295, min_periods=max(295//3, 2)).mean()
    noise = impulse.abs().rolling(259, min_periods=max(259//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.590625 + 0.0005377 * anchor

def f09_mex_577_jerk_v577(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=245, w2=306, w3=272, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 245)
    acceleration = _rolling_slope(velocity, 306)
    curvature = _rolling_slope(acceleration, 272)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.249 * acceleration + 0.0005378 * anchor

def f09_mex_578_accel_v578(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=252, w2=317, w3=285, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(252, min_periods=max(252//3, 2)).mean(), upside.rolling(317, min_periods=max(317//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.619375 + 0.0005379 * anchor

def f09_mex_579_jerk_v579(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=8, w2=328, w3=298, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(328, min_periods=max(328//3, 2)).max()
    rebound = x - x.rolling(8, min_periods=max(8//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2642 * _rolling_slope(draw, 298) + 0.000538 * anchor

def f09_mex_580_accel_v580(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=15, w2=339, w3=311, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 15)
    baseline = trend.rolling(339, min_periods=max(339//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(311, min_periods=max(311//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.875 + 0.0005381 * anchor

def f09_mex_581_jerk_v581(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=22, w2=350, w3=324, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 22)
    slow = _rolling_slope(x, 350)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.889375 + 0.0005382 * anchor

def f09_mex_582_accel_v582(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=29, w2=361, w3=337, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(361, min_periods=max(361//3, 2)).max()
    trough = x.rolling(29, min_periods=max(29//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.90375 + 0.0005383 * anchor

def f09_mex_583_jerk_v583(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=36, w2=372, w3=350, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(36)
    rank = change.rolling(372, min_periods=max(372//3, 2)).rank(pct=True)
    persistence = change.rolling(350, min_periods=max(350//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2946 * persistence + 0.0005384 * anchor

def f09_mex_584_accel_v584(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=43, w2=383, w3=363, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(43, min_periods=max(43//3, 2)).std()
    vol_slow = ret.rolling(383, min_periods=max(383//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.9325 + 0.0005385 * anchor

def f09_mex_585_jerk_v585(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=50, w2=394, w3=376, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(394, min_periods=max(394//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 50)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3098 * slope + 0.0005386 * anchor

def f09_mex_586_accel_v586(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=57, w2=405, w3=389, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(57)
    drag = impulse.rolling(405, min_periods=max(405//3, 2)).mean()
    noise = impulse.abs().rolling(389, min_periods=max(389//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.96125 + 0.0005387 * anchor

def f09_mex_587_jerk_v587(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=64, w2=416, w3=402, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 64)
    acceleration = _rolling_slope(velocity, 416)
    curvature = _rolling_slope(acceleration, 402)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.325 * acceleration + 0.0005388 * anchor

def f09_mex_588_accel_v588(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=71, w2=427, w3=415, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(71, min_periods=max(71//3, 2)).mean(), upside.rolling(427, min_periods=max(427//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.99 + 0.0005389 * anchor

def f09_mex_589_jerk_v589(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=78, w2=438, w3=428, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(438, min_periods=max(438//3, 2)).max()
    rebound = x - x.rolling(78, min_periods=max(78//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3402 * _rolling_slope(draw, 428) + 0.000539 * anchor

def f09_mex_590_accel_v590(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=85, w2=449, w3=441, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 85)
    baseline = trend.rolling(449, min_periods=max(449//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(441, min_periods=max(441//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.01875 + 0.0005391 * anchor

def f09_mex_591_jerk_v591(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=92, w2=460, w3=454, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 92)
    slow = _rolling_slope(x, 460)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.033125 + 0.0005392 * anchor

def f09_mex_592_accel_v592(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=99, w2=471, w3=467, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(471, min_periods=max(471//3, 2)).max()
    trough = x.rolling(99, min_periods=max(99//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.0475 + 0.0005393 * anchor

def f09_mex_593_jerk_v593(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=106, w2=482, w3=480, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(106)
    rank = change.rolling(482, min_periods=max(482//3, 2)).rank(pct=True)
    persistence = change.rolling(480, min_periods=max(480//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3706 * persistence + 0.0005394 * anchor

def f09_mex_594_accel_v594(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=113, w2=493, w3=493, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(113, min_periods=max(113//3, 2)).std()
    vol_slow = ret.rolling(493, min_periods=max(493//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.07625 + 0.0005395 * anchor

def f09_mex_595_jerk_v595(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=120, w2=504, w3=506, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(504, min_periods=max(504//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 120)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3858 * slope + 0.0005396 * anchor

def f09_mex_596_accel_v596(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=127, w2=12, w3=519, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(12, min_periods=max(12//3, 2)).mean()
    noise = impulse.abs().rolling(519, min_periods=max(519//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.105 + 0.0005397 * anchor

def f09_mex_597_jerk_v597(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=134, w2=23, w3=532, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 134)
    acceleration = _rolling_slope(velocity, 23)
    curvature = _rolling_slope(acceleration, 532)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.401 * acceleration + 0.0005398 * anchor

def f09_mex_598_accel_v598(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=141, w2=34, w3=545, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(141, min_periods=max(141//3, 2)).mean(), upside.rolling(34, min_periods=max(34//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.13375 + 0.0005399 * anchor

def f09_mex_599_jerk_v599(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=148, w2=45, w3=558, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(45, min_periods=max(45//3, 2)).max()
    rebound = x - x.rolling(148, min_periods=max(148//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0398 * _rolling_slope(draw, 558) + 0.00054 * anchor

def f09_mex_600_accel_v600(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=155, w2=56, w3=571, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 155)
    baseline = trend.rolling(56, min_periods=max(56//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(571, min_periods=max(571//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.1625 + 0.0005401 * anchor
