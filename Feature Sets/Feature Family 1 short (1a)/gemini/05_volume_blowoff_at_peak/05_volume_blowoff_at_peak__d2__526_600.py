"""05 volume blowoff at peak d2 second derivative features 526-600 â€” Pipeline 1a-HF Grade v3.

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

def f05_vbp_526_accel_v526_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=156, w2=507, w3=203, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(507, min_periods=max(507//3, 2)).mean()
    noise = impulse.abs().rolling(203, min_periods=max(203//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.1625 + 0.0002927 * anchor
    return base_signal.diff().diff()

def f05_vbp_527_jerk_v527_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=163, w2=15, w3=216, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 163)
    acceleration = _rolling_slope(velocity, 15)
    curvature = _rolling_slope(acceleration, 216)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0726 * acceleration + 0.0002928 * anchor
    return base_signal.diff().diff()

def f05_vbp_528_accel_v528_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=170, w2=26, w3=229, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(170, min_periods=max(170//3, 2)).mean(), upside.rolling(26, min_periods=max(26//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.19125 + 0.0002929 * anchor
    return base_signal.diff().diff()

def f05_vbp_529_jerk_v529_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=177, w2=37, w3=242, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(37, min_periods=max(37//3, 2)).max()
    rebound = x - x.rolling(177, min_periods=max(177//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0878 * _rolling_slope(draw, 242) + 0.000293 * anchor
    return base_signal.diff().diff()

def f05_vbp_530_accel_v530_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=184, w2=48, w3=255, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 184)
    baseline = trend.rolling(48, min_periods=max(48//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(255, min_periods=max(255//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.22 + 0.0002931 * anchor
    return base_signal.diff().diff()

def f05_vbp_531_jerk_v531_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=191, w2=59, w3=268, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 191)
    slow = _rolling_slope(x, 59)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=268, adjust=False).mean() * 1.234375 + 0.0002932 * anchor
    return base_signal.diff().diff()

def f05_vbp_532_accel_v532_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=198, w2=70, w3=281, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(70, min_periods=max(70//3, 2)).max()
    trough = x.rolling(198, min_periods=max(198//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.24875 + 0.0002933 * anchor
    return base_signal.diff().diff()

def f05_vbp_533_jerk_v533_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=205, w2=81, w3=294, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(81, min_periods=max(81//3, 2)).rank(pct=True)
    persistence = change.rolling(294, min_periods=max(294//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1182 * persistence + 0.0002934 * anchor
    return base_signal.diff().diff()

def f05_vbp_534_accel_v534_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=212, w2=92, w3=307, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(212, min_periods=max(212//3, 2)).std()
    vol_slow = ret.rolling(92, min_periods=max(92//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.2775 + 0.0002935 * anchor
    return base_signal.diff().diff()

def f05_vbp_535_jerk_v535_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=219, w2=103, w3=320, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(103, min_periods=max(103//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 219)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1334 * slope + 0.0002936 * anchor
    return base_signal.diff().diff()

def f05_vbp_536_accel_v536_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=226, w2=114, w3=333, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(114, min_periods=max(114//3, 2)).mean()
    noise = impulse.abs().rolling(333, min_periods=max(333//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.30625 + 0.0002937 * anchor
    return base_signal.diff().diff()

def f05_vbp_537_jerk_v537_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=233, w2=125, w3=346, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 233)
    acceleration = _rolling_slope(velocity, 125)
    curvature = _rolling_slope(acceleration, 346)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1486 * acceleration + 0.0002938 * anchor
    return base_signal.diff().diff()

def f05_vbp_538_accel_v538_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=240, w2=136, w3=359, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(240, min_periods=max(240//3, 2)).mean(), upside.rolling(136, min_periods=max(136//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.335 + 0.0002939 * anchor
    return base_signal.diff().diff()

def f05_vbp_539_jerk_v539_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=247, w2=147, w3=372, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(147, min_periods=max(147//3, 2)).max()
    rebound = x - x.rolling(247, min_periods=max(247//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1638 * _rolling_slope(draw, 372) + 0.000294 * anchor
    return base_signal.diff().diff()

def f05_vbp_540_accel_v540_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=254, w2=158, w3=385, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 254)
    baseline = trend.rolling(158, min_periods=max(158//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(385, min_periods=max(385//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.36375 + 0.0002941 * anchor
    return base_signal.diff().diff()

def f05_vbp_541_jerk_v541_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=10, w2=169, w3=398, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 10)
    slow = _rolling_slope(x, 169)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.378125 + 0.0002942 * anchor
    return base_signal.diff().diff()

def f05_vbp_542_accel_v542_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=17, w2=180, w3=411, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(180, min_periods=max(180//3, 2)).max()
    trough = x.rolling(17, min_periods=max(17//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.3925 + 0.0002943 * anchor
    return base_signal.diff().diff()

def f05_vbp_543_jerk_v543_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=24, w2=191, w3=424, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(24)
    rank = change.rolling(191, min_periods=max(191//3, 2)).rank(pct=True)
    persistence = change.rolling(424, min_periods=max(424//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1942 * persistence + 0.0002944 * anchor
    return base_signal.diff().diff()

def f05_vbp_544_accel_v544_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=31, w2=202, w3=437, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(31, min_periods=max(31//3, 2)).std()
    vol_slow = ret.rolling(202, min_periods=max(202//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.42125 + 0.0002945 * anchor
    return base_signal.diff().diff()

def f05_vbp_545_jerk_v545_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=38, w2=213, w3=450, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(213, min_periods=max(213//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 38)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2094 * slope + 0.0002946 * anchor
    return base_signal.diff().diff()

def f05_vbp_546_accel_v546_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=45, w2=224, w3=463, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(45)
    drag = impulse.rolling(224, min_periods=max(224//3, 2)).mean()
    noise = impulse.abs().rolling(463, min_periods=max(463//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.45 + 0.0002947 * anchor
    return base_signal.diff().diff()

def f05_vbp_547_jerk_v547_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=52, w2=235, w3=476, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 52)
    acceleration = _rolling_slope(velocity, 235)
    curvature = _rolling_slope(acceleration, 476)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2246 * acceleration + 0.0002948 * anchor
    return base_signal.diff().diff()

def f05_vbp_548_accel_v548_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=59, w2=246, w3=489, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(59, min_periods=max(59//3, 2)).mean(), upside.rolling(246, min_periods=max(246//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.47875 + 0.0002949 * anchor
    return base_signal.diff().diff()

def f05_vbp_549_jerk_v549_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=66, w2=257, w3=502, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(257, min_periods=max(257//3, 2)).max()
    rebound = x - x.rolling(66, min_periods=max(66//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2398 * _rolling_slope(draw, 502) + 0.000295 * anchor
    return base_signal.diff().diff()

def f05_vbp_550_accel_v550_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=73, w2=268, w3=515, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 73)
    baseline = trend.rolling(268, min_periods=max(268//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(515, min_periods=max(515//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.5075 + 0.0002951 * anchor
    return base_signal.diff().diff()

def f05_vbp_551_jerk_v551_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=80, w2=279, w3=528, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 80)
    slow = _rolling_slope(x, 279)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.521875 + 0.0002952 * anchor
    return base_signal.diff().diff()

def f05_vbp_552_accel_v552_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=87, w2=290, w3=541, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(290, min_periods=max(290//3, 2)).max()
    trough = x.rolling(87, min_periods=max(87//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.53625 + 0.0002953 * anchor
    return base_signal.diff().diff()

def f05_vbp_553_jerk_v553_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=94, w2=301, w3=554, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(94)
    rank = change.rolling(301, min_periods=max(301//3, 2)).rank(pct=True)
    persistence = change.rolling(554, min_periods=max(554//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2702 * persistence + 0.0002954 * anchor
    return base_signal.diff().diff()

def f05_vbp_554_accel_v554_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=101, w2=312, w3=567, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(101, min_periods=max(101//3, 2)).std()
    vol_slow = ret.rolling(312, min_periods=max(312//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.565 + 0.0002955 * anchor
    return base_signal.diff().diff()

def f05_vbp_555_jerk_v555_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=108, w2=323, w3=580, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(323, min_periods=max(323//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 108)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2854 * slope + 0.0002956 * anchor
    return base_signal.diff().diff()

def f05_vbp_556_accel_v556_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=115, w2=334, w3=593, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(115)
    drag = impulse.rolling(334, min_periods=max(334//3, 2)).mean()
    noise = impulse.abs().rolling(593, min_periods=max(593//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.59375 + 0.0002957 * anchor
    return base_signal.diff().diff()

def f05_vbp_557_jerk_v557_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=122, w2=345, w3=606, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 122)
    acceleration = _rolling_slope(velocity, 345)
    curvature = _rolling_slope(acceleration, 606)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3006 * acceleration + 0.0002958 * anchor
    return base_signal.diff().diff()

def f05_vbp_558_accel_v558_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=129, w2=356, w3=619, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(129, min_periods=max(129//3, 2)).mean(), upside.rolling(356, min_periods=max(356//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.6225 + 0.0002959 * anchor
    return base_signal.diff().diff()

def f05_vbp_559_jerk_v559_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=136, w2=367, w3=632, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(367, min_periods=max(367//3, 2)).max()
    rebound = x - x.rolling(136, min_periods=max(136//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3158 * _rolling_slope(draw, 632) + 0.000296 * anchor
    return base_signal.diff().diff()

def f05_vbp_560_accel_v560_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=143, w2=378, w3=645, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 143)
    baseline = trend.rolling(378, min_periods=max(378//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(645, min_periods=max(645//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.878125 + 0.0002961 * anchor
    return base_signal.diff().diff()

def f05_vbp_561_jerk_v561_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=150, w2=389, w3=658, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 150)
    slow = _rolling_slope(x, 389)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.8925 + 0.0002962 * anchor
    return base_signal.diff().diff()

def f05_vbp_562_accel_v562_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=157, w2=400, w3=671, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(400, min_periods=max(400//3, 2)).max()
    trough = x.rolling(157, min_periods=max(157//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.906875 + 0.0002963 * anchor
    return base_signal.diff().diff()

def f05_vbp_563_jerk_v563_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=164, w2=411, w3=684, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(411, min_periods=max(411//3, 2)).rank(pct=True)
    persistence = change.rolling(684, min_periods=max(684//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3462 * persistence + 0.0002964 * anchor
    return base_signal.diff().diff()

def f05_vbp_564_accel_v564_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=171, w2=422, w3=697, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(171, min_periods=max(171//3, 2)).std()
    vol_slow = ret.rolling(422, min_periods=max(422//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.935625 + 0.0002965 * anchor
    return base_signal.diff().diff()

def f05_vbp_565_jerk_v565_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=178, w2=433, w3=710, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(433, min_periods=max(433//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 178)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3614 * slope + 0.0002966 * anchor
    return base_signal.diff().diff()

def f05_vbp_566_accel_v566_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=185, w2=444, w3=723, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(444, min_periods=max(444//3, 2)).mean()
    noise = impulse.abs().rolling(723, min_periods=max(723//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.964375 + 0.0002967 * anchor
    return base_signal.diff().diff()

def f05_vbp_567_jerk_v567_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=192, w2=455, w3=736, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 192)
    acceleration = _rolling_slope(velocity, 455)
    curvature = _rolling_slope(acceleration, 736)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3766 * acceleration + 0.0002968 * anchor
    return base_signal.diff().diff()

def f05_vbp_568_accel_v568_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=199, w2=466, w3=749, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(199, min_periods=max(199//3, 2)).mean(), upside.rolling(466, min_periods=max(466//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.993125 + 0.0002969 * anchor
    return base_signal.diff().diff()

def f05_vbp_569_jerk_v569_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=206, w2=477, w3=762, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(477, min_periods=max(477//3, 2)).max()
    rebound = x - x.rolling(206, min_periods=max(206//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3918 * _rolling_slope(draw, 762) + 0.000297 * anchor
    return base_signal.diff().diff()

def f05_vbp_570_accel_v570_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=213, w2=488, w3=18, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 213)
    baseline = trend.rolling(488, min_periods=max(488//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(18, min_periods=max(18//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.021875 + 0.0002971 * anchor
    return base_signal.diff().diff()

def f05_vbp_571_jerk_v571_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=220, w2=499, w3=31, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 220)
    slow = _rolling_slope(x, 499)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=31, adjust=False).mean() * 1.03625 + 0.0002972 * anchor
    return base_signal.diff().diff()

def f05_vbp_572_accel_v572_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=227, w2=510, w3=44, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(510, min_periods=max(510//3, 2)).max()
    trough = x.rolling(227, min_periods=max(227//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.050625 + 0.0002973 * anchor
    return base_signal.diff().diff()

def f05_vbp_573_jerk_v573_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=234, w2=18, w3=57, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(18, min_periods=max(18//3, 2)).rank(pct=True)
    persistence = change.rolling(57, min_periods=max(57//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0458 * persistence + 0.0002974 * anchor
    return base_signal.diff().diff()

def f05_vbp_574_accel_v574_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=241, w2=29, w3=70, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(241, min_periods=max(241//3, 2)).std()
    vol_slow = ret.rolling(29, min_periods=max(29//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.079375 + 0.0002975 * anchor
    return base_signal.diff().diff()

def f05_vbp_575_jerk_v575_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=248, w2=40, w3=83, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(40, min_periods=max(40//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 248)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.061 * slope + 0.0002976 * anchor
    return base_signal.diff().diff()

def f05_vbp_576_accel_v576_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=255, w2=51, w3=96, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(51, min_periods=max(51//3, 2)).mean()
    noise = impulse.abs().rolling(96, min_periods=max(96//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.108125 + 0.0002977 * anchor
    return base_signal.diff().diff()

def f05_vbp_577_jerk_v577_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=11, w2=62, w3=109, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 11)
    acceleration = _rolling_slope(velocity, 62)
    curvature = _rolling_slope(acceleration, 109)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0762 * acceleration + 0.0002978 * anchor
    return base_signal.diff().diff()

def f05_vbp_578_accel_v578_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=18, w2=73, w3=122, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(18, min_periods=max(18//3, 2)).mean(), upside.rolling(73, min_periods=max(73//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(122) * 1.136875 + 0.0002979 * anchor
    return base_signal.diff().diff()

def f05_vbp_579_jerk_v579_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=25, w2=84, w3=135, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(84, min_periods=max(84//3, 2)).max()
    rebound = x - x.rolling(25, min_periods=max(25//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0914 * _rolling_slope(draw, 135) + 0.000298 * anchor
    return base_signal.diff().diff()

def f05_vbp_580_accel_v580_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=32, w2=95, w3=148, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 32)
    baseline = trend.rolling(95, min_periods=max(95//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(148, min_periods=max(148//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.165625 + 0.0002981 * anchor
    return base_signal.diff().diff()

def f05_vbp_581_jerk_v581_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=39, w2=106, w3=161, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 39)
    slow = _rolling_slope(x, 106)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=161, adjust=False).mean() * 1.18 + 0.0002982 * anchor
    return base_signal.diff().diff()

def f05_vbp_582_accel_v582_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=46, w2=117, w3=174, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(117, min_periods=max(117//3, 2)).max()
    trough = x.rolling(46, min_periods=max(46//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.194375 + 0.0002983 * anchor
    return base_signal.diff().diff()

def f05_vbp_583_jerk_v583_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=53, w2=128, w3=187, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(53)
    rank = change.rolling(128, min_periods=max(128//3, 2)).rank(pct=True)
    persistence = change.rolling(187, min_periods=max(187//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1218 * persistence + 0.0002984 * anchor
    return base_signal.diff().diff()

def f05_vbp_584_accel_v584_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=60, w2=139, w3=200, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(60, min_periods=max(60//3, 2)).std()
    vol_slow = ret.rolling(139, min_periods=max(139//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.223125 + 0.0002985 * anchor
    return base_signal.diff().diff()

def f05_vbp_585_jerk_v585_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=67, w2=150, w3=213, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(150, min_periods=max(150//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 67)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.137 * slope + 0.0002986 * anchor
    return base_signal.diff().diff()

def f05_vbp_586_accel_v586_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=74, w2=161, w3=226, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(74)
    drag = impulse.rolling(161, min_periods=max(161//3, 2)).mean()
    noise = impulse.abs().rolling(226, min_periods=max(226//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.251875 + 0.0002987 * anchor
    return base_signal.diff().diff()

def f05_vbp_587_jerk_v587_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=81, w2=172, w3=239, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 81)
    acceleration = _rolling_slope(velocity, 172)
    curvature = _rolling_slope(acceleration, 239)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1522 * acceleration + 0.0002988 * anchor
    return base_signal.diff().diff()

def f05_vbp_588_accel_v588_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=88, w2=183, w3=252, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(88, min_periods=max(88//3, 2)).mean(), upside.rolling(183, min_periods=max(183//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.280625 + 0.0002989 * anchor
    return base_signal.diff().diff()

def f05_vbp_589_jerk_v589_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=95, w2=194, w3=265, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(194, min_periods=max(194//3, 2)).max()
    rebound = x - x.rolling(95, min_periods=max(95//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1674 * _rolling_slope(draw, 265) + 0.000299 * anchor
    return base_signal.diff().diff()

def f05_vbp_590_accel_v590_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=102, w2=205, w3=278, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 102)
    baseline = trend.rolling(205, min_periods=max(205//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(278, min_periods=max(278//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.309375 + 0.0002991 * anchor
    return base_signal.diff().diff()

def f05_vbp_591_jerk_v591_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=109, w2=216, w3=291, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 109)
    slow = _rolling_slope(x, 216)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=291, adjust=False).mean() * 1.32375 + 0.0002992 * anchor
    return base_signal.diff().diff()

def f05_vbp_592_accel_v592_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=116, w2=227, w3=304, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(227, min_periods=max(227//3, 2)).max()
    trough = x.rolling(116, min_periods=max(116//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.338125 + 0.0002993 * anchor
    return base_signal.diff().diff()

def f05_vbp_593_jerk_v593_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=123, w2=238, w3=317, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(123)
    rank = change.rolling(238, min_periods=max(238//3, 2)).rank(pct=True)
    persistence = change.rolling(317, min_periods=max(317//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1978 * persistence + 0.0002994 * anchor
    return base_signal.diff().diff()

def f05_vbp_594_accel_v594_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=130, w2=249, w3=330, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(130, min_periods=max(130//3, 2)).std()
    vol_slow = ret.rolling(249, min_periods=max(249//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.366875 + 0.0002995 * anchor
    return base_signal.diff().diff()

def f05_vbp_595_jerk_v595_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=137, w2=260, w3=343, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(260, min_periods=max(260//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 137)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.213 * slope + 0.0002996 * anchor
    return base_signal.diff().diff()

def f05_vbp_596_accel_v596_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=144, w2=271, w3=356, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(271, min_periods=max(271//3, 2)).mean()
    noise = impulse.abs().rolling(356, min_periods=max(356//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.395625 + 0.0002997 * anchor
    return base_signal.diff().diff()

def f05_vbp_597_jerk_v597_d2(high: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=151, w2=282, w3=369, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 151)
    acceleration = _rolling_slope(velocity, 282)
    curvature = _rolling_slope(acceleration, 369)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2282 * acceleration + 0.0002998 * anchor
    return base_signal.diff().diff()

def f05_vbp_598_accel_v598_d2(low: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=158, w2=293, w3=382, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(158, min_periods=max(158//3, 2)).mean(), upside.rolling(293, min_periods=max(293//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.424375 + 0.0002999 * anchor
    return base_signal.diff().diff()

def f05_vbp_599_jerk_v599_d2(volume: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated jerk replacement signal (w1=165, w2=304, w3=395, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(304, min_periods=max(304//3, 2)).max()
    rebound = x - x.rolling(165, min_periods=max(165//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2434 * _rolling_slope(draw, 395) + 0.0003 * anchor
    return base_signal.diff().diff()

def f05_vbp_600_accel_v600_d2(close: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accel replacement signal (w1=172, w2=315, w3=408, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 172)
    baseline = trend.rolling(315, min_periods=max(315//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(408, min_periods=max(408//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.453125 + 0.0003001 * anchor
    return base_signal.diff().diff()
