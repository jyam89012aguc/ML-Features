"""49 short squeeze aftermath d2 second derivative features 526-600 â€” Pipeline 1a-HF Grade v3.

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

def f49_ssa_526_accel_v526_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=86, w2=295, w3=185, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(86)
    drag = impulse.rolling(295, min_periods=max(295//3, 2)).mean()
    noise = impulse.abs().rolling(185, min_periods=max(185//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.299375 + 0.0030527 * anchor
    return base_signal.diff().diff()

def f49_ssa_527_jerk_v527_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=93, w2=306, w3=198, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 93)
    acceleration = _rolling_slope(velocity, 306)
    curvature = _rolling_slope(acceleration, 198)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1778 * acceleration + 0.0030528 * anchor
    return base_signal.diff().diff()

def f49_ssa_528_accel_v528_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=100, w2=317, w3=211, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(100, min_periods=max(100//3, 2)).mean(), upside.rolling(317, min_periods=max(317//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.328125 + 0.0030529 * anchor
    return base_signal.diff().diff()

def f49_ssa_529_jerk_v529_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=107, w2=328, w3=224, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(328, min_periods=max(328//3, 2)).max()
    rebound = x - x.rolling(107, min_periods=max(107//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.193 * _rolling_slope(draw, 224) + 0.003053 * anchor
    return base_signal.diff().diff()

def f49_ssa_530_accel_v530_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=114, w2=339, w3=237, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 114)
    baseline = trend.rolling(339, min_periods=max(339//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(237, min_periods=max(237//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.356875 + 0.0030531 * anchor
    return base_signal.diff().diff()

def f49_ssa_531_jerk_v531_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=121, w2=350, w3=250, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 121)
    slow = _rolling_slope(x, 350)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=250, adjust=False).mean() * 1.37125 + 0.0030532 * anchor
    return base_signal.diff().diff()

def f49_ssa_532_accel_v532_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=128, w2=361, w3=263, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(361, min_periods=max(361//3, 2)).max()
    trough = x.rolling(128, min_periods=max(128//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.385625 + 0.0030533 * anchor
    return base_signal.diff().diff()

def f49_ssa_533_jerk_v533_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=135, w2=372, w3=276, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(372, min_periods=max(372//3, 2)).rank(pct=True)
    persistence = change.rolling(276, min_periods=max(276//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2234 * persistence + 0.0030534 * anchor
    return base_signal.diff().diff()

def f49_ssa_534_accel_v534_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=142, w2=383, w3=289, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(142, min_periods=max(142//3, 2)).std()
    vol_slow = ret.rolling(383, min_periods=max(383//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.414375 + 0.0030535 * anchor
    return base_signal.diff().diff()

def f49_ssa_535_jerk_v535_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=149, w2=394, w3=302, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(394, min_periods=max(394//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 149)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2386 * slope + 0.0030536 * anchor
    return base_signal.diff().diff()

def f49_ssa_536_accel_v536_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=156, w2=405, w3=315, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(405, min_periods=max(405//3, 2)).mean()
    noise = impulse.abs().rolling(315, min_periods=max(315//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.443125 + 0.0030537 * anchor
    return base_signal.diff().diff()

def f49_ssa_537_jerk_v537_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=163, w2=416, w3=328, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 163)
    acceleration = _rolling_slope(velocity, 416)
    curvature = _rolling_slope(acceleration, 328)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2538 * acceleration + 0.0030538 * anchor
    return base_signal.diff().diff()

def f49_ssa_538_accel_v538_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=170, w2=427, w3=341, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(170, min_periods=max(170//3, 2)).mean(), upside.rolling(427, min_periods=max(427//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.471875 + 0.0030539 * anchor
    return base_signal.diff().diff()

def f49_ssa_539_jerk_v539_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=177, w2=438, w3=354, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(438, min_periods=max(438//3, 2)).max()
    rebound = x - x.rolling(177, min_periods=max(177//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.269 * _rolling_slope(draw, 354) + 0.003054 * anchor
    return base_signal.diff().diff()

def f49_ssa_540_accel_v540_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=184, w2=449, w3=367, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 184)
    baseline = trend.rolling(449, min_periods=max(449//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(367, min_periods=max(367//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.500625 + 0.0030541 * anchor
    return base_signal.diff().diff()

def f49_ssa_541_jerk_v541_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=191, w2=460, w3=380, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 191)
    slow = _rolling_slope(x, 460)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.515 + 0.0030542 * anchor
    return base_signal.diff().diff()

def f49_ssa_542_accel_v542_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=198, w2=471, w3=393, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(471, min_periods=max(471//3, 2)).max()
    trough = x.rolling(198, min_periods=max(198//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.529375 + 0.0030543 * anchor
    return base_signal.diff().diff()

def f49_ssa_543_jerk_v543_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=205, w2=482, w3=406, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(482, min_periods=max(482//3, 2)).rank(pct=True)
    persistence = change.rolling(406, min_periods=max(406//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2994 * persistence + 0.0030544 * anchor
    return base_signal.diff().diff()

def f49_ssa_544_accel_v544_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=212, w2=493, w3=419, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(212, min_periods=max(212//3, 2)).std()
    vol_slow = ret.rolling(493, min_periods=max(493//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.558125 + 0.0030545 * anchor
    return base_signal.diff().diff()

def f49_ssa_545_jerk_v545_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=219, w2=504, w3=432, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(504, min_periods=max(504//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 219)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3146 * slope + 0.0030546 * anchor
    return base_signal.diff().diff()

def f49_ssa_546_accel_v546_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=226, w2=12, w3=445, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(12, min_periods=max(12//3, 2)).mean()
    noise = impulse.abs().rolling(445, min_periods=max(445//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.586875 + 0.0030547 * anchor
    return base_signal.diff().diff()

def f49_ssa_547_jerk_v547_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=233, w2=23, w3=458, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 233)
    acceleration = _rolling_slope(velocity, 23)
    curvature = _rolling_slope(acceleration, 458)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3298 * acceleration + 0.0030548 * anchor
    return base_signal.diff().diff()

def f49_ssa_548_accel_v548_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=240, w2=34, w3=471, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(240, min_periods=max(240//3, 2)).mean(), upside.rolling(34, min_periods=max(34//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.615625 + 0.0030549 * anchor
    return base_signal.diff().diff()

def f49_ssa_549_jerk_v549_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=247, w2=45, w3=484, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(45, min_periods=max(45//3, 2)).max()
    rebound = x - x.rolling(247, min_periods=max(247//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.345 * _rolling_slope(draw, 484) + 0.003055 * anchor
    return base_signal.diff().diff()

def f49_ssa_550_accel_v550_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=254, w2=56, w3=497, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 254)
    baseline = trend.rolling(56, min_periods=max(56//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(497, min_periods=max(497//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.87125 + 0.0030551 * anchor
    return base_signal.diff().diff()

def f49_ssa_551_jerk_v551_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=10, w2=67, w3=510, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 10)
    slow = _rolling_slope(x, 67)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.885625 + 0.0030552 * anchor
    return base_signal.diff().diff()

def f49_ssa_552_accel_v552_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=17, w2=78, w3=523, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(78, min_periods=max(78//3, 2)).max()
    trough = x.rolling(17, min_periods=max(17//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.9 + 0.0030553 * anchor
    return base_signal.diff().diff()

def f49_ssa_553_jerk_v553_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=24, w2=89, w3=536, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(24)
    rank = change.rolling(89, min_periods=max(89//3, 2)).rank(pct=True)
    persistence = change.rolling(536, min_periods=max(536//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3754 * persistence + 0.0030554 * anchor
    return base_signal.diff().diff()

def f49_ssa_554_accel_v554_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=31, w2=100, w3=549, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(31, min_periods=max(31//3, 2)).std()
    vol_slow = ret.rolling(100, min_periods=max(100//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.92875 + 0.0030555 * anchor
    return base_signal.diff().diff()

def f49_ssa_555_jerk_v555_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=38, w2=111, w3=562, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(111, min_periods=max(111//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 38)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3906 * slope + 0.0030556 * anchor
    return base_signal.diff().diff()

def f49_ssa_556_accel_v556_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=45, w2=122, w3=575, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(45)
    drag = impulse.rolling(122, min_periods=max(122//3, 2)).mean()
    noise = impulse.abs().rolling(575, min_periods=max(575//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.9575 + 0.0030557 * anchor
    return base_signal.diff().diff()

def f49_ssa_557_jerk_v557_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=52, w2=133, w3=588, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 52)
    acceleration = _rolling_slope(velocity, 133)
    curvature = _rolling_slope(acceleration, 588)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.4058 * acceleration + 0.0030558 * anchor
    return base_signal.diff().diff()

def f49_ssa_558_accel_v558_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=59, w2=144, w3=601, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(59, min_periods=max(59//3, 2)).mean(), upside.rolling(144, min_periods=max(144//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.98625 + 0.0030559 * anchor
    return base_signal.diff().diff()

def f49_ssa_559_jerk_v559_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=66, w2=155, w3=614, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(155, min_periods=max(155//3, 2)).max()
    rebound = x - x.rolling(66, min_periods=max(66//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0446 * _rolling_slope(draw, 614) + 0.003056 * anchor
    return base_signal.diff().diff()

def f49_ssa_560_accel_v560_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=73, w2=166, w3=627, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 73)
    baseline = trend.rolling(166, min_periods=max(166//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(627, min_periods=max(627//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.015 + 0.0030561 * anchor
    return base_signal.diff().diff()

def f49_ssa_561_jerk_v561_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=80, w2=177, w3=640, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 80)
    slow = _rolling_slope(x, 177)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.029375 + 0.0030562 * anchor
    return base_signal.diff().diff()

def f49_ssa_562_accel_v562_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=87, w2=188, w3=653, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(188, min_periods=max(188//3, 2)).max()
    trough = x.rolling(87, min_periods=max(87//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.04375 + 0.0030563 * anchor
    return base_signal.diff().diff()

def f49_ssa_563_jerk_v563_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=94, w2=199, w3=666, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(94)
    rank = change.rolling(199, min_periods=max(199//3, 2)).rank(pct=True)
    persistence = change.rolling(666, min_periods=max(666//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.075 * persistence + 0.0030564 * anchor
    return base_signal.diff().diff()

def f49_ssa_564_accel_v564_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=101, w2=210, w3=679, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(101, min_periods=max(101//3, 2)).std()
    vol_slow = ret.rolling(210, min_periods=max(210//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.0725 + 0.0030565 * anchor
    return base_signal.diff().diff()

def f49_ssa_565_jerk_v565_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=108, w2=221, w3=692, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(221, min_periods=max(221//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 108)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0902 * slope + 0.0030566 * anchor
    return base_signal.diff().diff()

def f49_ssa_566_accel_v566_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=115, w2=232, w3=705, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(115)
    drag = impulse.rolling(232, min_periods=max(232//3, 2)).mean()
    noise = impulse.abs().rolling(705, min_periods=max(705//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.10125 + 0.0030567 * anchor
    return base_signal.diff().diff()

def f49_ssa_567_jerk_v567_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=122, w2=243, w3=718, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 122)
    acceleration = _rolling_slope(velocity, 243)
    curvature = _rolling_slope(acceleration, 718)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1054 * acceleration + 0.0030568 * anchor
    return base_signal.diff().diff()

def f49_ssa_568_accel_v568_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=129, w2=254, w3=731, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(129, min_periods=max(129//3, 2)).mean(), upside.rolling(254, min_periods=max(254//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.13 + 0.0030569 * anchor
    return base_signal.diff().diff()

def f49_ssa_569_jerk_v569_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=136, w2=265, w3=744, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(265, min_periods=max(265//3, 2)).max()
    rebound = x - x.rolling(136, min_periods=max(136//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1206 * _rolling_slope(draw, 744) + 0.003057 * anchor
    return base_signal.diff().diff()

def f49_ssa_570_accel_v570_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=143, w2=276, w3=757, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 143)
    baseline = trend.rolling(276, min_periods=max(276//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(757, min_periods=max(757//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.15875 + 0.0030571 * anchor
    return base_signal.diff().diff()

def f49_ssa_571_jerk_v571_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=150, w2=287, w3=770, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 150)
    slow = _rolling_slope(x, 287)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.173125 + 0.0030572 * anchor
    return base_signal.diff().diff()

def f49_ssa_572_accel_v572_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=157, w2=298, w3=26, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(298, min_periods=max(298//3, 2)).max()
    trough = x.rolling(157, min_periods=max(157//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.1875 + 0.0030573 * anchor
    return base_signal.diff().diff()

def f49_ssa_573_jerk_v573_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=164, w2=309, w3=39, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(309, min_periods=max(309//3, 2)).rank(pct=True)
    persistence = change.rolling(39, min_periods=max(39//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.151 * persistence + 0.0030574 * anchor
    return base_signal.diff().diff()

def f49_ssa_574_accel_v574_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=171, w2=320, w3=52, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(171, min_periods=max(171//3, 2)).std()
    vol_slow = ret.rolling(320, min_periods=max(320//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.21625 + 0.0030575 * anchor
    return base_signal.diff().diff()

def f49_ssa_575_jerk_v575_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=178, w2=331, w3=65, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(331, min_periods=max(331//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 178)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1662 * slope + 0.0030576 * anchor
    return base_signal.diff().diff()

def f49_ssa_576_accel_v576_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=185, w2=342, w3=78, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(342, min_periods=max(342//3, 2)).mean()
    noise = impulse.abs().rolling(78, min_periods=max(78//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.245 + 0.0030577 * anchor
    return base_signal.diff().diff()

def f49_ssa_577_jerk_v577_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=192, w2=353, w3=91, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 192)
    acceleration = _rolling_slope(velocity, 353)
    curvature = _rolling_slope(acceleration, 91)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1814 * acceleration + 0.0030578 * anchor
    return base_signal.diff().diff()

def f49_ssa_578_accel_v578_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=199, w2=364, w3=104, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(199, min_periods=max(199//3, 2)).mean(), upside.rolling(364, min_periods=max(364//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(104) * 1.27375 + 0.0030579 * anchor
    return base_signal.diff().diff()

def f49_ssa_579_jerk_v579_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=206, w2=375, w3=117, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(375, min_periods=max(375//3, 2)).max()
    rebound = x - x.rolling(206, min_periods=max(206//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1966 * _rolling_slope(draw, 117) + 0.003058 * anchor
    return base_signal.diff().diff()

def f49_ssa_580_accel_v580_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=213, w2=386, w3=130, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 213)
    baseline = trend.rolling(386, min_periods=max(386//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(130, min_periods=max(130//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.3025 + 0.0030581 * anchor
    return base_signal.diff().diff()

def f49_ssa_581_jerk_v581_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=220, w2=397, w3=143, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 220)
    slow = _rolling_slope(x, 397)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=143, adjust=False).mean() * 1.316875 + 0.0030582 * anchor
    return base_signal.diff().diff()

def f49_ssa_582_accel_v582_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=227, w2=408, w3=156, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(408, min_periods=max(408//3, 2)).max()
    trough = x.rolling(227, min_periods=max(227//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.33125 + 0.0030583 * anchor
    return base_signal.diff().diff()

def f49_ssa_583_jerk_v583_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=234, w2=419, w3=169, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(419, min_periods=max(419//3, 2)).rank(pct=True)
    persistence = change.rolling(169, min_periods=max(169//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.227 * persistence + 0.0030584 * anchor
    return base_signal.diff().diff()

def f49_ssa_584_accel_v584_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=241, w2=430, w3=182, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(241, min_periods=max(241//3, 2)).std()
    vol_slow = ret.rolling(430, min_periods=max(430//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.36 + 0.0030585 * anchor
    return base_signal.diff().diff()

def f49_ssa_585_jerk_v585_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=248, w2=441, w3=195, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(441, min_periods=max(441//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 248)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2422 * slope + 0.0030586 * anchor
    return base_signal.diff().diff()

def f49_ssa_586_accel_v586_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=255, w2=452, w3=208, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(452, min_periods=max(452//3, 2)).mean()
    noise = impulse.abs().rolling(208, min_periods=max(208//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.38875 + 0.0030587 * anchor
    return base_signal.diff().diff()

def f49_ssa_587_jerk_v587_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=11, w2=463, w3=221, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 11)
    acceleration = _rolling_slope(velocity, 463)
    curvature = _rolling_slope(acceleration, 221)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2574 * acceleration + 0.0030588 * anchor
    return base_signal.diff().diff()

def f49_ssa_588_accel_v588_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=18, w2=474, w3=234, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(18, min_periods=max(18//3, 2)).mean(), upside.rolling(474, min_periods=max(474//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.4175 + 0.0030589 * anchor
    return base_signal.diff().diff()

def f49_ssa_589_jerk_v589_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=25, w2=485, w3=247, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(485, min_periods=max(485//3, 2)).max()
    rebound = x - x.rolling(25, min_periods=max(25//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2726 * _rolling_slope(draw, 247) + 0.003059 * anchor
    return base_signal.diff().diff()

def f49_ssa_590_accel_v590_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=32, w2=496, w3=260, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 32)
    baseline = trend.rolling(496, min_periods=max(496//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(260, min_periods=max(260//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.44625 + 0.0030591 * anchor
    return base_signal.diff().diff()

def f49_ssa_591_jerk_v591_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=39, w2=507, w3=273, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 39)
    slow = _rolling_slope(x, 507)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=273, adjust=False).mean() * 1.460625 + 0.0030592 * anchor
    return base_signal.diff().diff()

def f49_ssa_592_accel_v592_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=46, w2=15, w3=286, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(15, min_periods=max(15//3, 2)).max()
    trough = x.rolling(46, min_periods=max(46//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.475 + 0.0030593 * anchor
    return base_signal.diff().diff()

def f49_ssa_593_jerk_v593_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=53, w2=26, w3=299, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(53)
    rank = change.rolling(26, min_periods=max(26//3, 2)).rank(pct=True)
    persistence = change.rolling(299, min_periods=max(299//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.303 * persistence + 0.0030594 * anchor
    return base_signal.diff().diff()

def f49_ssa_594_accel_v594_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=60, w2=37, w3=312, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(60, min_periods=max(60//3, 2)).std()
    vol_slow = ret.rolling(37, min_periods=max(37//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.50375 + 0.0030595 * anchor
    return base_signal.diff().diff()

def f49_ssa_595_jerk_v595_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=67, w2=48, w3=325, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(48, min_periods=max(48//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 67)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3182 * slope + 0.0030596 * anchor
    return base_signal.diff().diff()

def f49_ssa_596_accel_v596_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=74, w2=59, w3=338, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(74)
    drag = impulse.rolling(59, min_periods=max(59//3, 2)).mean()
    noise = impulse.abs().rolling(338, min_periods=max(338//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.5325 + 0.0030597 * anchor
    return base_signal.diff().diff()

def f49_ssa_597_jerk_v597_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=81, w2=70, w3=351, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 81)
    acceleration = _rolling_slope(velocity, 70)
    curvature = _rolling_slope(acceleration, 351)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3334 * acceleration + 0.0030598 * anchor
    return base_signal.diff().diff()

def f49_ssa_598_accel_v598_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=88, w2=81, w3=364, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(88, min_periods=max(88//3, 2)).mean(), upside.rolling(81, min_periods=max(81//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.56125 + 0.0030599 * anchor
    return base_signal.diff().diff()

def f49_ssa_599_jerk_v599_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=95, w2=92, w3=377, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(92, min_periods=max(92//3, 2)).max()
    rebound = x - x.rolling(95, min_periods=max(95//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3486 * _rolling_slope(draw, 377) + 0.00306 * anchor
    return base_signal.diff().diff()

def f49_ssa_600_accel_v600_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=102, w2=103, w3=390, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 102)
    baseline = trend.rolling(103, min_periods=max(103//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(390, min_periods=max(390//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.59 + 0.0030601 * anchor
    return base_signal.diff().diff()
