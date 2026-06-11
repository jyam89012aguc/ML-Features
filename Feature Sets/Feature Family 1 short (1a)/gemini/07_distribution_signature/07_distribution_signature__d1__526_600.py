"""07 distribution signature d1 first derivative features 526-600 â€” Pipeline 1a-HF Grade v3.

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

def f07_dsi_526_accel_v526_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=22, w2=126, w3=663, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(22)
    drag = impulse.rolling(126, min_periods=max(126//3, 2)).mean()
    noise = impulse.abs().rolling(663, min_periods=max(663//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.40375 + 0.0004127 * anchor
    return base_signal.diff()

def f07_dsi_527_jerk_v527_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=29, w2=137, w3=676, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 29)
    acceleration = _rolling_slope(velocity, 137)
    curvature = _rolling_slope(acceleration, 676)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.159 * acceleration + 0.0004128 * anchor
    return base_signal.diff()

def f07_dsi_528_accel_v528_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=36, w2=148, w3=689, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(36, min_periods=max(36//3, 2)).mean(), upside.rolling(148, min_periods=max(148//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.4325 + 0.0004129 * anchor
    return base_signal.diff()

def f07_dsi_529_jerk_v529_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=43, w2=159, w3=702, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(159, min_periods=max(159//3, 2)).max()
    rebound = x - x.rolling(43, min_periods=max(43//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1742 * _rolling_slope(draw, 702) + 0.000413 * anchor
    return base_signal.diff()

def f07_dsi_530_accel_v530_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=50, w2=170, w3=715, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 50)
    baseline = trend.rolling(170, min_periods=max(170//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(715, min_periods=max(715//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.46125 + 0.0004131 * anchor
    return base_signal.diff()

def f07_dsi_531_jerk_v531_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=57, w2=181, w3=728, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 57)
    slow = _rolling_slope(x, 181)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.475625 + 0.0004132 * anchor
    return base_signal.diff()

def f07_dsi_532_accel_v532_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=64, w2=192, w3=741, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(192, min_periods=max(192//3, 2)).max()
    trough = x.rolling(64, min_periods=max(64//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.49 + 0.0004133 * anchor
    return base_signal.diff()

def f07_dsi_533_jerk_v533_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=71, w2=203, w3=754, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(71)
    rank = change.rolling(203, min_periods=max(203//3, 2)).rank(pct=True)
    persistence = change.rolling(754, min_periods=max(754//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2046 * persistence + 0.0004134 * anchor
    return base_signal.diff()

def f07_dsi_534_accel_v534_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=78, w2=214, w3=767, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(78, min_periods=max(78//3, 2)).std()
    vol_slow = ret.rolling(214, min_periods=max(214//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.51875 + 0.0004135 * anchor
    return base_signal.diff()

def f07_dsi_535_jerk_v535_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=85, w2=225, w3=23, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(225, min_periods=max(225//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 85)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2198 * slope + 0.0004136 * anchor
    return base_signal.diff()

def f07_dsi_536_accel_v536_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=92, w2=236, w3=36, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(92)
    drag = impulse.rolling(236, min_periods=max(236//3, 2)).mean()
    noise = impulse.abs().rolling(36, min_periods=max(36//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.5475 + 0.0004137 * anchor
    return base_signal.diff()

def f07_dsi_537_jerk_v537_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=99, w2=247, w3=49, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 99)
    acceleration = _rolling_slope(velocity, 247)
    curvature = _rolling_slope(acceleration, 49)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.235 * acceleration + 0.0004138 * anchor
    return base_signal.diff()

def f07_dsi_538_accel_v538_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=106, w2=258, w3=62, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(106, min_periods=max(106//3, 2)).mean(), upside.rolling(258, min_periods=max(258//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(62) * 1.57625 + 0.0004139 * anchor
    return base_signal.diff()

def f07_dsi_539_jerk_v539_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=113, w2=269, w3=75, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(269, min_periods=max(269//3, 2)).max()
    rebound = x - x.rolling(113, min_periods=max(113//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2502 * _rolling_slope(draw, 75) + 0.000414 * anchor
    return base_signal.diff()

def f07_dsi_540_accel_v540_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=120, w2=280, w3=88, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 120)
    baseline = trend.rolling(280, min_periods=max(280//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(88, min_periods=max(88//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.605 + 0.0004141 * anchor
    return base_signal.diff()

def f07_dsi_541_jerk_v541_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=127, w2=291, w3=101, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 127)
    slow = _rolling_slope(x, 291)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=101, adjust=False).mean() * 1.619375 + 0.0004142 * anchor
    return base_signal.diff()

def f07_dsi_542_accel_v542_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=134, w2=302, w3=114, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(302, min_periods=max(302//3, 2)).max()
    trough = x.rolling(134, min_periods=max(134//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.860625 + 0.0004143 * anchor
    return base_signal.diff()

def f07_dsi_543_jerk_v543_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=141, w2=313, w3=127, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(313, min_periods=max(313//3, 2)).rank(pct=True)
    persistence = change.rolling(127, min_periods=max(127//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2806 * persistence + 0.0004144 * anchor
    return base_signal.diff()

def f07_dsi_544_accel_v544_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=148, w2=324, w3=140, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(148, min_periods=max(148//3, 2)).std()
    vol_slow = ret.rolling(324, min_periods=max(324//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.889375 + 0.0004145 * anchor
    return base_signal.diff()

def f07_dsi_545_jerk_v545_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=155, w2=335, w3=153, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(335, min_periods=max(335//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 155)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2958 * slope + 0.0004146 * anchor
    return base_signal.diff()

def f07_dsi_546_accel_v546_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=162, w2=346, w3=166, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(346, min_periods=max(346//3, 2)).mean()
    noise = impulse.abs().rolling(166, min_periods=max(166//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.918125 + 0.0004147 * anchor
    return base_signal.diff()

def f07_dsi_547_jerk_v547_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=169, w2=357, w3=179, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 169)
    acceleration = _rolling_slope(velocity, 357)
    curvature = _rolling_slope(acceleration, 179)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.311 * acceleration + 0.0004148 * anchor
    return base_signal.diff()

def f07_dsi_548_accel_v548_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=176, w2=368, w3=192, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(176, min_periods=max(176//3, 2)).mean(), upside.rolling(368, min_periods=max(368//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.946875 + 0.0004149 * anchor
    return base_signal.diff()

def f07_dsi_549_jerk_v549_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=183, w2=379, w3=205, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(379, min_periods=max(379//3, 2)).max()
    rebound = x - x.rolling(183, min_periods=max(183//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3262 * _rolling_slope(draw, 205) + 0.000415 * anchor
    return base_signal.diff()

def f07_dsi_550_accel_v550_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=190, w2=390, w3=218, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 190)
    baseline = trend.rolling(390, min_periods=max(390//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(218, min_periods=max(218//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.975625 + 0.0004151 * anchor
    return base_signal.diff()

def f07_dsi_551_jerk_v551_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=197, w2=401, w3=231, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 197)
    slow = _rolling_slope(x, 401)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=231, adjust=False).mean() * 0.99 + 0.0004152 * anchor
    return base_signal.diff()

def f07_dsi_552_accel_v552_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=204, w2=412, w3=244, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(412, min_periods=max(412//3, 2)).max()
    trough = x.rolling(204, min_periods=max(204//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.004375 + 0.0004153 * anchor
    return base_signal.diff()

def f07_dsi_553_jerk_v553_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=211, w2=423, w3=257, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(423, min_periods=max(423//3, 2)).rank(pct=True)
    persistence = change.rolling(257, min_periods=max(257//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3566 * persistence + 0.0004154 * anchor
    return base_signal.diff()

def f07_dsi_554_accel_v554_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=218, w2=434, w3=270, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(218, min_periods=max(218//3, 2)).std()
    vol_slow = ret.rolling(434, min_periods=max(434//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.033125 + 0.0004155 * anchor
    return base_signal.diff()

def f07_dsi_555_jerk_v555_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=225, w2=445, w3=283, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(445, min_periods=max(445//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 225)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3718 * slope + 0.0004156 * anchor
    return base_signal.diff()

def f07_dsi_556_accel_v556_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=232, w2=456, w3=296, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(456, min_periods=max(456//3, 2)).mean()
    noise = impulse.abs().rolling(296, min_periods=max(296//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.061875 + 0.0004157 * anchor
    return base_signal.diff()

def f07_dsi_557_jerk_v557_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=239, w2=467, w3=309, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 239)
    acceleration = _rolling_slope(velocity, 467)
    curvature = _rolling_slope(acceleration, 309)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.387 * acceleration + 0.0004158 * anchor
    return base_signal.diff()

def f07_dsi_558_accel_v558_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=246, w2=478, w3=322, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(246, min_periods=max(246//3, 2)).mean(), upside.rolling(478, min_periods=max(478//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.090625 + 0.0004159 * anchor
    return base_signal.diff()

def f07_dsi_559_jerk_v559_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=253, w2=489, w3=335, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(489, min_periods=max(489//3, 2)).max()
    rebound = x - x.rolling(253, min_periods=max(253//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.4022 * _rolling_slope(draw, 335) + 0.000416 * anchor
    return base_signal.diff()

def f07_dsi_560_accel_v560_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=9, w2=500, w3=348, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 9)
    baseline = trend.rolling(500, min_periods=max(500//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(348, min_periods=max(348//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.119375 + 0.0004161 * anchor
    return base_signal.diff()

def f07_dsi_561_jerk_v561_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=16, w2=511, w3=361, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 16)
    slow = _rolling_slope(x, 511)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.13375 + 0.0004162 * anchor
    return base_signal.diff()

def f07_dsi_562_accel_v562_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=23, w2=19, w3=374, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(19, min_periods=max(19//3, 2)).max()
    trough = x.rolling(23, min_periods=max(23//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.148125 + 0.0004163 * anchor
    return base_signal.diff()

def f07_dsi_563_jerk_v563_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=30, w2=30, w3=387, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(30)
    rank = change.rolling(30, min_periods=max(30//3, 2)).rank(pct=True)
    persistence = change.rolling(387, min_periods=max(387//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0562 * persistence + 0.0004164 * anchor
    return base_signal.diff()

def f07_dsi_564_accel_v564_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=37, w2=41, w3=400, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(37, min_periods=max(37//3, 2)).std()
    vol_slow = ret.rolling(41, min_periods=max(41//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.176875 + 0.0004165 * anchor
    return base_signal.diff()

def f07_dsi_565_jerk_v565_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=44, w2=52, w3=413, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(52, min_periods=max(52//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 44)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0714 * slope + 0.0004166 * anchor
    return base_signal.diff()

def f07_dsi_566_accel_v566_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=51, w2=63, w3=426, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(51)
    drag = impulse.rolling(63, min_periods=max(63//3, 2)).mean()
    noise = impulse.abs().rolling(426, min_periods=max(426//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.205625 + 0.0004167 * anchor
    return base_signal.diff()

def f07_dsi_567_jerk_v567_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=58, w2=74, w3=439, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 58)
    acceleration = _rolling_slope(velocity, 74)
    curvature = _rolling_slope(acceleration, 439)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0866 * acceleration + 0.0004168 * anchor
    return base_signal.diff()

def f07_dsi_568_accel_v568_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=65, w2=85, w3=452, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(65, min_periods=max(65//3, 2)).mean(), upside.rolling(85, min_periods=max(85//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.234375 + 0.0004169 * anchor
    return base_signal.diff()

def f07_dsi_569_jerk_v569_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=72, w2=96, w3=465, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(96, min_periods=max(96//3, 2)).max()
    rebound = x - x.rolling(72, min_periods=max(72//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1018 * _rolling_slope(draw, 465) + 0.000417 * anchor
    return base_signal.diff()

def f07_dsi_570_accel_v570_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=79, w2=107, w3=478, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 79)
    baseline = trend.rolling(107, min_periods=max(107//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(478, min_periods=max(478//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.263125 + 0.0004171 * anchor
    return base_signal.diff()

def f07_dsi_571_jerk_v571_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=86, w2=118, w3=491, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 86)
    slow = _rolling_slope(x, 118)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.2775 + 0.0004172 * anchor
    return base_signal.diff()

def f07_dsi_572_accel_v572_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=93, w2=129, w3=504, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(129, min_periods=max(129//3, 2)).max()
    trough = x.rolling(93, min_periods=max(93//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.291875 + 0.0004173 * anchor
    return base_signal.diff()

def f07_dsi_573_jerk_v573_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=100, w2=140, w3=517, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(100)
    rank = change.rolling(140, min_periods=max(140//3, 2)).rank(pct=True)
    persistence = change.rolling(517, min_periods=max(517//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1322 * persistence + 0.0004174 * anchor
    return base_signal.diff()

def f07_dsi_574_accel_v574_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=107, w2=151, w3=530, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(107, min_periods=max(107//3, 2)).std()
    vol_slow = ret.rolling(151, min_periods=max(151//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.320625 + 0.0004175 * anchor
    return base_signal.diff()

def f07_dsi_575_jerk_v575_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=114, w2=162, w3=543, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(162, min_periods=max(162//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 114)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1474 * slope + 0.0004176 * anchor
    return base_signal.diff()

def f07_dsi_576_accel_v576_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=121, w2=173, w3=556, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(121)
    drag = impulse.rolling(173, min_periods=max(173//3, 2)).mean()
    noise = impulse.abs().rolling(556, min_periods=max(556//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.349375 + 0.0004177 * anchor
    return base_signal.diff()

def f07_dsi_577_jerk_v577_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=128, w2=184, w3=569, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 128)
    acceleration = _rolling_slope(velocity, 184)
    curvature = _rolling_slope(acceleration, 569)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1626 * acceleration + 0.0004178 * anchor
    return base_signal.diff()

def f07_dsi_578_accel_v578_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=135, w2=195, w3=582, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(135, min_periods=max(135//3, 2)).mean(), upside.rolling(195, min_periods=max(195//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.378125 + 0.0004179 * anchor
    return base_signal.diff()

def f07_dsi_579_jerk_v579_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=142, w2=206, w3=595, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(206, min_periods=max(206//3, 2)).max()
    rebound = x - x.rolling(142, min_periods=max(142//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1778 * _rolling_slope(draw, 595) + 0.000418 * anchor
    return base_signal.diff()

def f07_dsi_580_accel_v580_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=149, w2=217, w3=608, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 149)
    baseline = trend.rolling(217, min_periods=max(217//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(608, min_periods=max(608//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.406875 + 0.0004181 * anchor
    return base_signal.diff()

def f07_dsi_581_jerk_v581_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=156, w2=228, w3=621, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 156)
    slow = _rolling_slope(x, 228)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.42125 + 0.0004182 * anchor
    return base_signal.diff()

def f07_dsi_582_accel_v582_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=163, w2=239, w3=634, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(239, min_periods=max(239//3, 2)).max()
    trough = x.rolling(163, min_periods=max(163//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.435625 + 0.0004183 * anchor
    return base_signal.diff()

def f07_dsi_583_jerk_v583_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=170, w2=250, w3=647, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(250, min_periods=max(250//3, 2)).rank(pct=True)
    persistence = change.rolling(647, min_periods=max(647//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2082 * persistence + 0.0004184 * anchor
    return base_signal.diff()

def f07_dsi_584_accel_v584_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=177, w2=261, w3=660, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(177, min_periods=max(177//3, 2)).std()
    vol_slow = ret.rolling(261, min_periods=max(261//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.464375 + 0.0004185 * anchor
    return base_signal.diff()

def f07_dsi_585_jerk_v585_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=184, w2=272, w3=673, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(272, min_periods=max(272//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 184)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2234 * slope + 0.0004186 * anchor
    return base_signal.diff()

def f07_dsi_586_accel_v586_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=191, w2=283, w3=686, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(283, min_periods=max(283//3, 2)).mean()
    noise = impulse.abs().rolling(686, min_periods=max(686//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.493125 + 0.0004187 * anchor
    return base_signal.diff()

def f07_dsi_587_jerk_v587_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=198, w2=294, w3=699, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 198)
    acceleration = _rolling_slope(velocity, 294)
    curvature = _rolling_slope(acceleration, 699)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2386 * acceleration + 0.0004188 * anchor
    return base_signal.diff()

def f07_dsi_588_accel_v588_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=205, w2=305, w3=712, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(205, min_periods=max(205//3, 2)).mean(), upside.rolling(305, min_periods=max(305//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.521875 + 0.0004189 * anchor
    return base_signal.diff()

def f07_dsi_589_jerk_v589_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=212, w2=316, w3=725, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(316, min_periods=max(316//3, 2)).max()
    rebound = x - x.rolling(212, min_periods=max(212//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2538 * _rolling_slope(draw, 725) + 0.000419 * anchor
    return base_signal.diff()

def f07_dsi_590_accel_v590_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=219, w2=327, w3=738, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 219)
    baseline = trend.rolling(327, min_periods=max(327//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(738, min_periods=max(738//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.550625 + 0.0004191 * anchor
    return base_signal.diff()

def f07_dsi_591_jerk_v591_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=226, w2=338, w3=751, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 226)
    slow = _rolling_slope(x, 338)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.565 + 0.0004192 * anchor
    return base_signal.diff()

def f07_dsi_592_accel_v592_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=233, w2=349, w3=764, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(349, min_periods=max(349//3, 2)).max()
    trough = x.rolling(233, min_periods=max(233//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.579375 + 0.0004193 * anchor
    return base_signal.diff()

def f07_dsi_593_jerk_v593_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=240, w2=360, w3=20, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(360, min_periods=max(360//3, 2)).rank(pct=True)
    persistence = change.rolling(20, min_periods=max(20//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2842 * persistence + 0.0004194 * anchor
    return base_signal.diff()

def f07_dsi_594_accel_v594_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=247, w2=371, w3=33, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(247, min_periods=max(247//3, 2)).std()
    vol_slow = ret.rolling(371, min_periods=max(371//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.608125 + 0.0004195 * anchor
    return base_signal.diff()

def f07_dsi_595_jerk_v595_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=254, w2=382, w3=46, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(382, min_periods=max(382//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 254)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2994 * slope + 0.0004196 * anchor
    return base_signal.diff()

def f07_dsi_596_accel_v596_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=10, w2=393, w3=59, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(10)
    drag = impulse.rolling(393, min_periods=max(393//3, 2)).mean()
    noise = impulse.abs().rolling(59, min_periods=max(59//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.86375 + 0.0004197 * anchor
    return base_signal.diff()

def f07_dsi_597_jerk_v597_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=17, w2=404, w3=72, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 17)
    acceleration = _rolling_slope(velocity, 404)
    curvature = _rolling_slope(acceleration, 72)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3146 * acceleration + 0.0004198 * anchor
    return base_signal.diff()

def f07_dsi_598_accel_v598_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=24, w2=415, w3=85, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(24, min_periods=max(24//3, 2)).mean(), upside.rolling(415, min_periods=max(415//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(85) * 0.8925 + 0.0004199 * anchor
    return base_signal.diff()

def f07_dsi_599_jerk_v599_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=31, w2=426, w3=98, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(426, min_periods=max(426//3, 2)).max()
    rebound = x - x.rolling(31, min_periods=max(31//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3298 * _rolling_slope(draw, 98) + 0.00042 * anchor
    return base_signal.diff()

def f07_dsi_600_accel_v600_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=38, w2=437, w3=111, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 38)
    baseline = trend.rolling(437, min_periods=max(437//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(111, min_periods=max(111//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.92125 + 0.0004201 * anchor
    return base_signal.diff()
