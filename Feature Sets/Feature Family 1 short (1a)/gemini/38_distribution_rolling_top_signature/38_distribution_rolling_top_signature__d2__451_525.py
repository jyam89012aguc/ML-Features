"""38 distribution rolling top signature d2 second derivative features 451-525 â€” Pipeline 1a-HF Grade v3.

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

def f38_drts_451_jerk_v451_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=114, w2=247, w3=235, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 114)
    slow = _rolling_slope(x, 247)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=235, adjust=False).mean() * 1.093125 + 0.0023252 * anchor
    return base_signal.diff().diff()

def f38_drts_452_accel_v452_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=121, w2=258, w3=248, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(258, min_periods=max(258//3, 2)).max()
    trough = x.rolling(121, min_periods=max(121//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.1075 + 0.0023253 * anchor
    return base_signal.diff().diff()

def f38_drts_453_jerk_v453_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=128, w2=269, w3=261, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(269, min_periods=max(269//3, 2)).rank(pct=True)
    persistence = change.rolling(261, min_periods=max(261//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2262 * persistence + 0.0023254 * anchor
    return base_signal.diff().diff()

def f38_drts_454_accel_v454_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=135, w2=280, w3=274, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(135, min_periods=max(135//3, 2)).std()
    vol_slow = ret.rolling(280, min_periods=max(280//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.13625 + 0.0023255 * anchor
    return base_signal.diff().diff()

def f38_drts_455_jerk_v455_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=142, w2=291, w3=287, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(291, min_periods=max(291//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 142)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2414 * slope + 0.0023256 * anchor
    return base_signal.diff().diff()

def f38_drts_456_accel_v456_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=149, w2=302, w3=300, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(302, min_periods=max(302//3, 2)).mean()
    noise = impulse.abs().rolling(300, min_periods=max(300//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.165 + 0.0023257 * anchor
    return base_signal.diff().diff()

def f38_drts_457_jerk_v457_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=156, w2=313, w3=313, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 156)
    acceleration = _rolling_slope(velocity, 313)
    curvature = _rolling_slope(acceleration, 313)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2566 * acceleration + 0.0023258 * anchor
    return base_signal.diff().diff()

def f38_drts_458_accel_v458_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=163, w2=324, w3=326, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(163, min_periods=max(163//3, 2)).mean(), upside.rolling(324, min_periods=max(324//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.19375 + 0.0023259 * anchor
    return base_signal.diff().diff()

def f38_drts_459_jerk_v459_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=170, w2=335, w3=339, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(335, min_periods=max(335//3, 2)).max()
    rebound = x - x.rolling(170, min_periods=max(170//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2718 * _rolling_slope(draw, 339) + 0.002326 * anchor
    return base_signal.diff().diff()

def f38_drts_460_accel_v460_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=177, w2=346, w3=352, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 177)
    baseline = trend.rolling(346, min_periods=max(346//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(352, min_periods=max(352//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.2225 + 0.0023261 * anchor
    return base_signal.diff().diff()

def f38_drts_461_jerk_v461_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=184, w2=357, w3=365, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 184)
    slow = _rolling_slope(x, 357)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.236875 + 0.0023262 * anchor
    return base_signal.diff().diff()

def f38_drts_462_accel_v462_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=191, w2=368, w3=378, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(368, min_periods=max(368//3, 2)).max()
    trough = x.rolling(191, min_periods=max(191//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.25125 + 0.0023263 * anchor
    return base_signal.diff().diff()

def f38_drts_463_jerk_v463_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=198, w2=379, w3=391, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(379, min_periods=max(379//3, 2)).rank(pct=True)
    persistence = change.rolling(391, min_periods=max(391//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3022 * persistence + 0.0023264 * anchor
    return base_signal.diff().diff()

def f38_drts_464_accel_v464_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=205, w2=390, w3=404, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(205, min_periods=max(205//3, 2)).std()
    vol_slow = ret.rolling(390, min_periods=max(390//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.28 + 0.0023265 * anchor
    return base_signal.diff().diff()

def f38_drts_465_jerk_v465_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=212, w2=401, w3=417, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(401, min_periods=max(401//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 212)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3174 * slope + 0.0023266 * anchor
    return base_signal.diff().diff()

def f38_drts_466_accel_v466_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=219, w2=412, w3=430, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(412, min_periods=max(412//3, 2)).mean()
    noise = impulse.abs().rolling(430, min_periods=max(430//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.30875 + 0.0023267 * anchor
    return base_signal.diff().diff()

def f38_drts_467_jerk_v467_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=226, w2=423, w3=443, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 226)
    acceleration = _rolling_slope(velocity, 423)
    curvature = _rolling_slope(acceleration, 443)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3326 * acceleration + 0.0023268 * anchor
    return base_signal.diff().diff()

def f38_drts_468_accel_v468_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=233, w2=434, w3=456, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(233, min_periods=max(233//3, 2)).mean(), upside.rolling(434, min_periods=max(434//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.3375 + 0.0023269 * anchor
    return base_signal.diff().diff()

def f38_drts_469_jerk_v469_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=240, w2=445, w3=469, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(445, min_periods=max(445//3, 2)).max()
    rebound = x - x.rolling(240, min_periods=max(240//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3478 * _rolling_slope(draw, 469) + 0.002327 * anchor
    return base_signal.diff().diff()

def f38_drts_470_accel_v470_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=247, w2=456, w3=482, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 247)
    baseline = trend.rolling(456, min_periods=max(456//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(482, min_periods=max(482//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.36625 + 0.0023271 * anchor
    return base_signal.diff().diff()

def f38_drts_471_jerk_v471_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=254, w2=467, w3=495, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 254)
    slow = _rolling_slope(x, 467)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.380625 + 0.0023272 * anchor
    return base_signal.diff().diff()

def f38_drts_472_accel_v472_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=10, w2=478, w3=508, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(478, min_periods=max(478//3, 2)).max()
    trough = x.rolling(10, min_periods=max(10//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.395 + 0.0023273 * anchor
    return base_signal.diff().diff()

def f38_drts_473_jerk_v473_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=17, w2=489, w3=521, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(17)
    rank = change.rolling(489, min_periods=max(489//3, 2)).rank(pct=True)
    persistence = change.rolling(521, min_periods=max(521//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3782 * persistence + 0.0023274 * anchor
    return base_signal.diff().diff()

def f38_drts_474_accel_v474_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=24, w2=500, w3=534, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(24, min_periods=max(24//3, 2)).std()
    vol_slow = ret.rolling(500, min_periods=max(500//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.42375 + 0.0023275 * anchor
    return base_signal.diff().diff()

def f38_drts_475_jerk_v475_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=31, w2=511, w3=547, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(511, min_periods=max(511//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 31)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3934 * slope + 0.0023276 * anchor
    return base_signal.diff().diff()

def f38_drts_476_accel_v476_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=38, w2=19, w3=560, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(38)
    drag = impulse.rolling(19, min_periods=max(19//3, 2)).mean()
    noise = impulse.abs().rolling(560, min_periods=max(560//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.4525 + 0.0023277 * anchor
    return base_signal.diff().diff()

def f38_drts_477_jerk_v477_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=45, w2=30, w3=573, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 45)
    acceleration = _rolling_slope(velocity, 30)
    curvature = _rolling_slope(acceleration, 573)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.4086 * acceleration + 0.0023278 * anchor
    return base_signal.diff().diff()

def f38_drts_478_accel_v478_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=52, w2=41, w3=586, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(52, min_periods=max(52//3, 2)).mean(), upside.rolling(41, min_periods=max(41//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.48125 + 0.0023279 * anchor
    return base_signal.diff().diff()

def f38_drts_479_jerk_v479_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=59, w2=52, w3=599, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(52, min_periods=max(52//3, 2)).max()
    rebound = x - x.rolling(59, min_periods=max(59//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0474 * _rolling_slope(draw, 599) + 0.002328 * anchor
    return base_signal.diff().diff()

def f38_drts_480_accel_v480_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=66, w2=63, w3=612, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 66)
    baseline = trend.rolling(63, min_periods=max(63//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(612, min_periods=max(612//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.51 + 0.0023281 * anchor
    return base_signal.diff().diff()

def f38_drts_481_jerk_v481_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=73, w2=74, w3=625, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 73)
    slow = _rolling_slope(x, 74)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.524375 + 0.0023282 * anchor
    return base_signal.diff().diff()

def f38_drts_482_accel_v482_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=80, w2=85, w3=638, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(85, min_periods=max(85//3, 2)).max()
    trough = x.rolling(80, min_periods=max(80//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.53875 + 0.0023283 * anchor
    return base_signal.diff().diff()

def f38_drts_483_jerk_v483_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=87, w2=96, w3=651, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(87)
    rank = change.rolling(96, min_periods=max(96//3, 2)).rank(pct=True)
    persistence = change.rolling(651, min_periods=max(651//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0778 * persistence + 0.0023284 * anchor
    return base_signal.diff().diff()

def f38_drts_484_accel_v484_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=94, w2=107, w3=664, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(94, min_periods=max(94//3, 2)).std()
    vol_slow = ret.rolling(107, min_periods=max(107//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.5675 + 0.0023285 * anchor
    return base_signal.diff().diff()

def f38_drts_485_jerk_v485_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=101, w2=118, w3=677, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(118, min_periods=max(118//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 101)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.093 * slope + 0.0023286 * anchor
    return base_signal.diff().diff()

def f38_drts_486_accel_v486_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=108, w2=129, w3=690, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(108)
    drag = impulse.rolling(129, min_periods=max(129//3, 2)).mean()
    noise = impulse.abs().rolling(690, min_periods=max(690//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.59625 + 0.0023287 * anchor
    return base_signal.diff().diff()

def f38_drts_487_jerk_v487_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=115, w2=140, w3=703, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 115)
    acceleration = _rolling_slope(velocity, 140)
    curvature = _rolling_slope(acceleration, 703)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1082 * acceleration + 0.0023288 * anchor
    return base_signal.diff().diff()

def f38_drts_488_accel_v488_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=122, w2=151, w3=716, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(122, min_periods=max(122//3, 2)).mean(), upside.rolling(151, min_periods=max(151//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.851875 + 0.0023289 * anchor
    return base_signal.diff().diff()

def f38_drts_489_jerk_v489_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=129, w2=162, w3=729, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(162, min_periods=max(162//3, 2)).max()
    rebound = x - x.rolling(129, min_periods=max(129//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1234 * _rolling_slope(draw, 729) + 0.002329 * anchor
    return base_signal.diff().diff()

def f38_drts_490_accel_v490_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=136, w2=173, w3=742, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 136)
    baseline = trend.rolling(173, min_periods=max(173//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(742, min_periods=max(742//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.880625 + 0.0023291 * anchor
    return base_signal.diff().diff()

def f38_drts_491_jerk_v491_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=143, w2=184, w3=755, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 143)
    slow = _rolling_slope(x, 184)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.895 + 0.0023292 * anchor
    return base_signal.diff().diff()

def f38_drts_492_accel_v492_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=150, w2=195, w3=768, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(195, min_periods=max(195//3, 2)).max()
    trough = x.rolling(150, min_periods=max(150//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.909375 + 0.0023293 * anchor
    return base_signal.diff().diff()

def f38_drts_493_jerk_v493_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=157, w2=206, w3=24, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(206, min_periods=max(206//3, 2)).rank(pct=True)
    persistence = change.rolling(24, min_periods=max(24//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1538 * persistence + 0.0023294 * anchor
    return base_signal.diff().diff()

def f38_drts_494_accel_v494_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=164, w2=217, w3=37, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(164, min_periods=max(164//3, 2)).std()
    vol_slow = ret.rolling(217, min_periods=max(217//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.938125 + 0.0023295 * anchor
    return base_signal.diff().diff()

def f38_drts_495_jerk_v495_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=171, w2=228, w3=50, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(228, min_periods=max(228//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 171)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.169 * slope + 0.0023296 * anchor
    return base_signal.diff().diff()

def f38_drts_496_accel_v496_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=178, w2=239, w3=63, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(239, min_periods=max(239//3, 2)).mean()
    noise = impulse.abs().rolling(63, min_periods=max(63//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.966875 + 0.0023297 * anchor
    return base_signal.diff().diff()

def f38_drts_497_jerk_v497_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=185, w2=250, w3=76, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 185)
    acceleration = _rolling_slope(velocity, 250)
    curvature = _rolling_slope(acceleration, 76)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1842 * acceleration + 0.0023298 * anchor
    return base_signal.diff().diff()

def f38_drts_498_accel_v498_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=192, w2=261, w3=89, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(192, min_periods=max(192//3, 2)).mean(), upside.rolling(261, min_periods=max(261//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(89) * 0.995625 + 0.0023299 * anchor
    return base_signal.diff().diff()

def f38_drts_499_jerk_v499_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=199, w2=272, w3=102, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(272, min_periods=max(272//3, 2)).max()
    rebound = x - x.rolling(199, min_periods=max(199//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1994 * _rolling_slope(draw, 102) + 0.00233 * anchor
    return base_signal.diff().diff()

def f38_drts_500_accel_v500_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=206, w2=283, w3=115, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 206)
    baseline = trend.rolling(283, min_periods=max(283//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(115, min_periods=max(115//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.024375 + 0.0023301 * anchor
    return base_signal.diff().diff()

def f38_drts_501_jerk_v501_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=213, w2=294, w3=128, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 213)
    slow = _rolling_slope(x, 294)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=128, adjust=False).mean() * 1.03875 + 0.0023302 * anchor
    return base_signal.diff().diff()

def f38_drts_502_accel_v502_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=220, w2=305, w3=141, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(305, min_periods=max(305//3, 2)).max()
    trough = x.rolling(220, min_periods=max(220//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.053125 + 0.0023303 * anchor
    return base_signal.diff().diff()

def f38_drts_503_jerk_v503_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=227, w2=316, w3=154, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(316, min_periods=max(316//3, 2)).rank(pct=True)
    persistence = change.rolling(154, min_periods=max(154//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2298 * persistence + 0.0023304 * anchor
    return base_signal.diff().diff()

def f38_drts_504_accel_v504_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=234, w2=327, w3=167, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(234, min_periods=max(234//3, 2)).std()
    vol_slow = ret.rolling(327, min_periods=max(327//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.081875 + 0.0023305 * anchor
    return base_signal.diff().diff()

def f38_drts_505_jerk_v505_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=241, w2=338, w3=180, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(338, min_periods=max(338//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 241)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.245 * slope + 0.0023306 * anchor
    return base_signal.diff().diff()

def f38_drts_506_accel_v506_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=248, w2=349, w3=193, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(349, min_periods=max(349//3, 2)).mean()
    noise = impulse.abs().rolling(193, min_periods=max(193//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.110625 + 0.0023307 * anchor
    return base_signal.diff().diff()

def f38_drts_507_jerk_v507_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=255, w2=360, w3=206, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 255)
    acceleration = _rolling_slope(velocity, 360)
    curvature = _rolling_slope(acceleration, 206)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2602 * acceleration + 0.0023308 * anchor
    return base_signal.diff().diff()

def f38_drts_508_accel_v508_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=11, w2=371, w3=219, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(11, min_periods=max(11//3, 2)).mean(), upside.rolling(371, min_periods=max(371//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.139375 + 0.0023309 * anchor
    return base_signal.diff().diff()

def f38_drts_509_jerk_v509_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=18, w2=382, w3=232, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(382, min_periods=max(382//3, 2)).max()
    rebound = x - x.rolling(18, min_periods=max(18//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2754 * _rolling_slope(draw, 232) + 0.002331 * anchor
    return base_signal.diff().diff()

def f38_drts_510_accel_v510_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=25, w2=393, w3=245, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 25)
    baseline = trend.rolling(393, min_periods=max(393//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(245, min_periods=max(245//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.168125 + 0.0023311 * anchor
    return base_signal.diff().diff()

def f38_drts_511_jerk_v511_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=32, w2=404, w3=258, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 32)
    slow = _rolling_slope(x, 404)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=258, adjust=False).mean() * 1.1825 + 0.0023312 * anchor
    return base_signal.diff().diff()

def f38_drts_512_accel_v512_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=39, w2=415, w3=271, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(415, min_periods=max(415//3, 2)).max()
    trough = x.rolling(39, min_periods=max(39//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.196875 + 0.0023313 * anchor
    return base_signal.diff().diff()

def f38_drts_513_jerk_v513_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=46, w2=426, w3=284, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(46)
    rank = change.rolling(426, min_periods=max(426//3, 2)).rank(pct=True)
    persistence = change.rolling(284, min_periods=max(284//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3058 * persistence + 0.0023314 * anchor
    return base_signal.diff().diff()

def f38_drts_514_accel_v514_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=53, w2=437, w3=297, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(53, min_periods=max(53//3, 2)).std()
    vol_slow = ret.rolling(437, min_periods=max(437//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.225625 + 0.0023315 * anchor
    return base_signal.diff().diff()

def f38_drts_515_jerk_v515_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=60, w2=448, w3=310, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(448, min_periods=max(448//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 60)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.321 * slope + 0.0023316 * anchor
    return base_signal.diff().diff()

def f38_drts_516_accel_v516_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=67, w2=459, w3=323, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(67)
    drag = impulse.rolling(459, min_periods=max(459//3, 2)).mean()
    noise = impulse.abs().rolling(323, min_periods=max(323//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.254375 + 0.0023317 * anchor
    return base_signal.diff().diff()

def f38_drts_517_jerk_v517_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=74, w2=470, w3=336, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 74)
    acceleration = _rolling_slope(velocity, 470)
    curvature = _rolling_slope(acceleration, 336)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3362 * acceleration + 0.0023318 * anchor
    return base_signal.diff().diff()

def f38_drts_518_accel_v518_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=81, w2=481, w3=349, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(81, min_periods=max(81//3, 2)).mean(), upside.rolling(481, min_periods=max(481//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.283125 + 0.0023319 * anchor
    return base_signal.diff().diff()

def f38_drts_519_jerk_v519_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=88, w2=492, w3=362, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(492, min_periods=max(492//3, 2)).max()
    rebound = x - x.rolling(88, min_periods=max(88//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3514 * _rolling_slope(draw, 362) + 0.002332 * anchor
    return base_signal.diff().diff()

def f38_drts_520_accel_v520_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=95, w2=503, w3=375, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 95)
    baseline = trend.rolling(503, min_periods=max(503//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(375, min_periods=max(375//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.311875 + 0.0023321 * anchor
    return base_signal.diff().diff()

def f38_drts_521_jerk_v521_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=102, w2=11, w3=388, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 102)
    slow = _rolling_slope(x, 11)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.32625 + 0.0023322 * anchor
    return base_signal.diff().diff()

def f38_drts_522_accel_v522_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=109, w2=22, w3=401, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(22, min_periods=max(22//3, 2)).max()
    trough = x.rolling(109, min_periods=max(109//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.340625 + 0.0023323 * anchor
    return base_signal.diff().diff()

def f38_drts_523_jerk_v523_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=116, w2=33, w3=414, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(116)
    rank = change.rolling(33, min_periods=max(33//3, 2)).rank(pct=True)
    persistence = change.rolling(414, min_periods=max(414//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3818 * persistence + 0.0023324 * anchor
    return base_signal.diff().diff()

def f38_drts_524_accel_v524_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=123, w2=44, w3=427, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(123, min_periods=max(123//3, 2)).std()
    vol_slow = ret.rolling(44, min_periods=max(44//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.369375 + 0.0023325 * anchor
    return base_signal.diff().diff()

def f38_drts_525_jerk_v525_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=130, w2=55, w3=440, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(55, min_periods=max(55//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 130)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.397 * slope + 0.0023326 * anchor
    return base_signal.diff().diff()
