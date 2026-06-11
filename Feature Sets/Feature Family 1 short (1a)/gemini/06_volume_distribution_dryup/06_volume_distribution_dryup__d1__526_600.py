"""06 volume distribution dryup d1 first derivative features 526-600 â€” Pipeline 1a-HF Grade v3.

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

def f06_vdd_526_accel_v526_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=89, w2=65, w3=433, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(89)
    drag = impulse.rolling(65, min_periods=max(65//3, 2)).mean()
    noise = impulse.abs().rolling(433, min_periods=max(433//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.283125 + 0.0003527 * anchor
    return base_signal.diff()

def f06_vdd_527_jerk_v527_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=96, w2=76, w3=446, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 96)
    acceleration = _rolling_slope(velocity, 76)
    curvature = _rolling_slope(acceleration, 446)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1158 * acceleration + 0.0003528 * anchor
    return base_signal.diff()

def f06_vdd_528_accel_v528_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=103, w2=87, w3=459, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(103, min_periods=max(103//3, 2)).mean(), upside.rolling(87, min_periods=max(87//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.311875 + 0.0003529 * anchor
    return base_signal.diff()

def f06_vdd_529_jerk_v529_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=110, w2=98, w3=472, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(98, min_periods=max(98//3, 2)).max()
    rebound = x - x.rolling(110, min_periods=max(110//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.131 * _rolling_slope(draw, 472) + 0.000353 * anchor
    return base_signal.diff()

def f06_vdd_530_accel_v530_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=117, w2=109, w3=485, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 117)
    baseline = trend.rolling(109, min_periods=max(109//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(485, min_periods=max(485//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.340625 + 0.0003531 * anchor
    return base_signal.diff()

def f06_vdd_531_jerk_v531_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=124, w2=120, w3=498, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 124)
    slow = _rolling_slope(x, 120)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.355 + 0.0003532 * anchor
    return base_signal.diff()

def f06_vdd_532_accel_v532_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=131, w2=131, w3=511, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(131, min_periods=max(131//3, 2)).max()
    trough = x.rolling(131, min_periods=max(131//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.369375 + 0.0003533 * anchor
    return base_signal.diff()

def f06_vdd_533_jerk_v533_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=138, w2=142, w3=524, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(142, min_periods=max(142//3, 2)).rank(pct=True)
    persistence = change.rolling(524, min_periods=max(524//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1614 * persistence + 0.0003534 * anchor
    return base_signal.diff()

def f06_vdd_534_accel_v534_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=145, w2=153, w3=537, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(145, min_periods=max(145//3, 2)).std()
    vol_slow = ret.rolling(153, min_periods=max(153//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.398125 + 0.0003535 * anchor
    return base_signal.diff()

def f06_vdd_535_jerk_v535_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=152, w2=164, w3=550, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(164, min_periods=max(164//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 152)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1766 * slope + 0.0003536 * anchor
    return base_signal.diff()

def f06_vdd_536_accel_v536_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=159, w2=175, w3=563, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(175, min_periods=max(175//3, 2)).mean()
    noise = impulse.abs().rolling(563, min_periods=max(563//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.426875 + 0.0003537 * anchor
    return base_signal.diff()

def f06_vdd_537_jerk_v537_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=166, w2=186, w3=576, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 166)
    acceleration = _rolling_slope(velocity, 186)
    curvature = _rolling_slope(acceleration, 576)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1918 * acceleration + 0.0003538 * anchor
    return base_signal.diff()

def f06_vdd_538_accel_v538_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=173, w2=197, w3=589, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(173, min_periods=max(173//3, 2)).mean(), upside.rolling(197, min_periods=max(197//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.455625 + 0.0003539 * anchor
    return base_signal.diff()

def f06_vdd_539_jerk_v539_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=180, w2=208, w3=602, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(208, min_periods=max(208//3, 2)).max()
    rebound = x - x.rolling(180, min_periods=max(180//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.207 * _rolling_slope(draw, 602) + 0.000354 * anchor
    return base_signal.diff()

def f06_vdd_540_accel_v540_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=187, w2=219, w3=615, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 187)
    baseline = trend.rolling(219, min_periods=max(219//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(615, min_periods=max(615//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.484375 + 0.0003541 * anchor
    return base_signal.diff()

def f06_vdd_541_jerk_v541_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=194, w2=230, w3=628, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 194)
    slow = _rolling_slope(x, 230)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.49875 + 0.0003542 * anchor
    return base_signal.diff()

def f06_vdd_542_accel_v542_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=201, w2=241, w3=641, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(241, min_periods=max(241//3, 2)).max()
    trough = x.rolling(201, min_periods=max(201//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.513125 + 0.0003543 * anchor
    return base_signal.diff()

def f06_vdd_543_jerk_v543_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=208, w2=252, w3=654, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(252, min_periods=max(252//3, 2)).rank(pct=True)
    persistence = change.rolling(654, min_periods=max(654//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2374 * persistence + 0.0003544 * anchor
    return base_signal.diff()

def f06_vdd_544_accel_v544_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=215, w2=263, w3=667, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(215, min_periods=max(215//3, 2)).std()
    vol_slow = ret.rolling(263, min_periods=max(263//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.541875 + 0.0003545 * anchor
    return base_signal.diff()

def f06_vdd_545_jerk_v545_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=222, w2=274, w3=680, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(274, min_periods=max(274//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 222)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2526 * slope + 0.0003546 * anchor
    return base_signal.diff()

def f06_vdd_546_accel_v546_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=229, w2=285, w3=693, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(285, min_periods=max(285//3, 2)).mean()
    noise = impulse.abs().rolling(693, min_periods=max(693//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.570625 + 0.0003547 * anchor
    return base_signal.diff()

def f06_vdd_547_jerk_v547_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=236, w2=296, w3=706, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 236)
    acceleration = _rolling_slope(velocity, 296)
    curvature = _rolling_slope(acceleration, 706)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2678 * acceleration + 0.0003548 * anchor
    return base_signal.diff()

def f06_vdd_548_accel_v548_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=243, w2=307, w3=719, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(243, min_periods=max(243//3, 2)).mean(), upside.rolling(307, min_periods=max(307//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.599375 + 0.0003549 * anchor
    return base_signal.diff()

def f06_vdd_549_jerk_v549_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=250, w2=318, w3=732, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(318, min_periods=max(318//3, 2)).max()
    rebound = x - x.rolling(250, min_periods=max(250//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.283 * _rolling_slope(draw, 732) + 0.000355 * anchor
    return base_signal.diff()

def f06_vdd_550_accel_v550_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=6, w2=329, w3=745, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 6)
    baseline = trend.rolling(329, min_periods=max(329//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(745, min_periods=max(745//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.855 + 0.0003551 * anchor
    return base_signal.diff()

def f06_vdd_551_jerk_v551_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=13, w2=340, w3=758, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 13)
    slow = _rolling_slope(x, 340)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.869375 + 0.0003552 * anchor
    return base_signal.diff()

def f06_vdd_552_accel_v552_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=20, w2=351, w3=771, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(351, min_periods=max(351//3, 2)).max()
    trough = x.rolling(20, min_periods=max(20//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.88375 + 0.0003553 * anchor
    return base_signal.diff()

def f06_vdd_553_jerk_v553_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=27, w2=362, w3=27, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(27)
    rank = change.rolling(362, min_periods=max(362//3, 2)).rank(pct=True)
    persistence = change.rolling(27, min_periods=max(27//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3134 * persistence + 0.0003554 * anchor
    return base_signal.diff()

def f06_vdd_554_accel_v554_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=34, w2=373, w3=40, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(34, min_periods=max(34//3, 2)).std()
    vol_slow = ret.rolling(373, min_periods=max(373//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.9125 + 0.0003555 * anchor
    return base_signal.diff()

def f06_vdd_555_jerk_v555_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=41, w2=384, w3=53, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(384, min_periods=max(384//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 41)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3286 * slope + 0.0003556 * anchor
    return base_signal.diff()

def f06_vdd_556_accel_v556_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=48, w2=395, w3=66, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(48)
    drag = impulse.rolling(395, min_periods=max(395//3, 2)).mean()
    noise = impulse.abs().rolling(66, min_periods=max(66//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.94125 + 0.0003557 * anchor
    return base_signal.diff()

def f06_vdd_557_jerk_v557_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=55, w2=406, w3=79, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 55)
    acceleration = _rolling_slope(velocity, 406)
    curvature = _rolling_slope(acceleration, 79)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3438 * acceleration + 0.0003558 * anchor
    return base_signal.diff()

def f06_vdd_558_accel_v558_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=62, w2=417, w3=92, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(62, min_periods=max(62//3, 2)).mean(), upside.rolling(417, min_periods=max(417//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(92) * 0.97 + 0.0003559 * anchor
    return base_signal.diff()

def f06_vdd_559_jerk_v559_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=69, w2=428, w3=105, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(428, min_periods=max(428//3, 2)).max()
    rebound = x - x.rolling(69, min_periods=max(69//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.359 * _rolling_slope(draw, 105) + 0.000356 * anchor
    return base_signal.diff()

def f06_vdd_560_accel_v560_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=76, w2=439, w3=118, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 76)
    baseline = trend.rolling(439, min_periods=max(439//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(118, min_periods=max(118//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.99875 + 0.0003561 * anchor
    return base_signal.diff()

def f06_vdd_561_jerk_v561_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=83, w2=450, w3=131, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 83)
    slow = _rolling_slope(x, 450)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=131, adjust=False).mean() * 1.013125 + 0.0003562 * anchor
    return base_signal.diff()

def f06_vdd_562_accel_v562_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=90, w2=461, w3=144, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(461, min_periods=max(461//3, 2)).max()
    trough = x.rolling(90, min_periods=max(90//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.0275 + 0.0003563 * anchor
    return base_signal.diff()

def f06_vdd_563_jerk_v563_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=97, w2=472, w3=157, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(97)
    rank = change.rolling(472, min_periods=max(472//3, 2)).rank(pct=True)
    persistence = change.rolling(157, min_periods=max(157//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3894 * persistence + 0.0003564 * anchor
    return base_signal.diff()

def f06_vdd_564_accel_v564_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=104, w2=483, w3=170, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(104, min_periods=max(104//3, 2)).std()
    vol_slow = ret.rolling(483, min_periods=max(483//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.05625 + 0.0003565 * anchor
    return base_signal.diff()

def f06_vdd_565_jerk_v565_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=111, w2=494, w3=183, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(494, min_periods=max(494//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 111)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.4046 * slope + 0.0003566 * anchor
    return base_signal.diff()

def f06_vdd_566_accel_v566_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=118, w2=505, w3=196, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(118)
    drag = impulse.rolling(505, min_periods=max(505//3, 2)).mean()
    noise = impulse.abs().rolling(196, min_periods=max(196//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.085 + 0.0003567 * anchor
    return base_signal.diff()

def f06_vdd_567_jerk_v567_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=125, w2=13, w3=209, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 125)
    acceleration = _rolling_slope(velocity, 13)
    curvature = _rolling_slope(acceleration, 209)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0434 * acceleration + 0.0003568 * anchor
    return base_signal.diff()

def f06_vdd_568_accel_v568_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=132, w2=24, w3=222, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(132, min_periods=max(132//3, 2)).mean(), upside.rolling(24, min_periods=max(24//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.11375 + 0.0003569 * anchor
    return base_signal.diff()

def f06_vdd_569_jerk_v569_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=139, w2=35, w3=235, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(35, min_periods=max(35//3, 2)).max()
    rebound = x - x.rolling(139, min_periods=max(139//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0586 * _rolling_slope(draw, 235) + 0.000357 * anchor
    return base_signal.diff()

def f06_vdd_570_accel_v570_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=146, w2=46, w3=248, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 146)
    baseline = trend.rolling(46, min_periods=max(46//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(248, min_periods=max(248//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.1425 + 0.0003571 * anchor
    return base_signal.diff()

def f06_vdd_571_jerk_v571_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=153, w2=57, w3=261, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 153)
    slow = _rolling_slope(x, 57)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=261, adjust=False).mean() * 1.156875 + 0.0003572 * anchor
    return base_signal.diff()

def f06_vdd_572_accel_v572_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=160, w2=68, w3=274, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(68, min_periods=max(68//3, 2)).max()
    trough = x.rolling(160, min_periods=max(160//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.17125 + 0.0003573 * anchor
    return base_signal.diff()

def f06_vdd_573_jerk_v573_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=167, w2=79, w3=287, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(79, min_periods=max(79//3, 2)).rank(pct=True)
    persistence = change.rolling(287, min_periods=max(287//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.089 * persistence + 0.0003574 * anchor
    return base_signal.diff()

def f06_vdd_574_accel_v574_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=174, w2=90, w3=300, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(174, min_periods=max(174//3, 2)).std()
    vol_slow = ret.rolling(90, min_periods=max(90//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.2 + 0.0003575 * anchor
    return base_signal.diff()

def f06_vdd_575_jerk_v575_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=181, w2=101, w3=313, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(101, min_periods=max(101//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 181)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1042 * slope + 0.0003576 * anchor
    return base_signal.diff()

def f06_vdd_576_accel_v576_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=188, w2=112, w3=326, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(112, min_periods=max(112//3, 2)).mean()
    noise = impulse.abs().rolling(326, min_periods=max(326//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.22875 + 0.0003577 * anchor
    return base_signal.diff()

def f06_vdd_577_jerk_v577_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=195, w2=123, w3=339, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 195)
    acceleration = _rolling_slope(velocity, 123)
    curvature = _rolling_slope(acceleration, 339)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1194 * acceleration + 0.0003578 * anchor
    return base_signal.diff()

def f06_vdd_578_accel_v578_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=202, w2=134, w3=352, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(202, min_periods=max(202//3, 2)).mean(), upside.rolling(134, min_periods=max(134//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.2575 + 0.0003579 * anchor
    return base_signal.diff()

def f06_vdd_579_jerk_v579_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=209, w2=145, w3=365, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(145, min_periods=max(145//3, 2)).max()
    rebound = x - x.rolling(209, min_periods=max(209//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1346 * _rolling_slope(draw, 365) + 0.000358 * anchor
    return base_signal.diff()

def f06_vdd_580_accel_v580_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=216, w2=156, w3=378, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 216)
    baseline = trend.rolling(156, min_periods=max(156//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(378, min_periods=max(378//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.28625 + 0.0003581 * anchor
    return base_signal.diff()

def f06_vdd_581_jerk_v581_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=223, w2=167, w3=391, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 223)
    slow = _rolling_slope(x, 167)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.300625 + 0.0003582 * anchor
    return base_signal.diff()

def f06_vdd_582_accel_v582_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=230, w2=178, w3=404, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(178, min_periods=max(178//3, 2)).max()
    trough = x.rolling(230, min_periods=max(230//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.315 + 0.0003583 * anchor
    return base_signal.diff()

def f06_vdd_583_jerk_v583_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=237, w2=189, w3=417, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(189, min_periods=max(189//3, 2)).rank(pct=True)
    persistence = change.rolling(417, min_periods=max(417//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.165 * persistence + 0.0003584 * anchor
    return base_signal.diff()

def f06_vdd_584_accel_v584_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=244, w2=200, w3=430, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(244, min_periods=max(244//3, 2)).std()
    vol_slow = ret.rolling(200, min_periods=max(200//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.34375 + 0.0003585 * anchor
    return base_signal.diff()

def f06_vdd_585_jerk_v585_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=251, w2=211, w3=443, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(211, min_periods=max(211//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 251)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1802 * slope + 0.0003586 * anchor
    return base_signal.diff()

def f06_vdd_586_accel_v586_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=7, w2=222, w3=456, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(7)
    drag = impulse.rolling(222, min_periods=max(222//3, 2)).mean()
    noise = impulse.abs().rolling(456, min_periods=max(456//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.3725 + 0.0003587 * anchor
    return base_signal.diff()

def f06_vdd_587_jerk_v587_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=14, w2=233, w3=469, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 14)
    acceleration = _rolling_slope(velocity, 233)
    curvature = _rolling_slope(acceleration, 469)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1954 * acceleration + 0.0003588 * anchor
    return base_signal.diff()

def f06_vdd_588_accel_v588_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=21, w2=244, w3=482, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(21, min_periods=max(21//3, 2)).mean(), upside.rolling(244, min_periods=max(244//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.40125 + 0.0003589 * anchor
    return base_signal.diff()

def f06_vdd_589_jerk_v589_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=28, w2=255, w3=495, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(255, min_periods=max(255//3, 2)).max()
    rebound = x - x.rolling(28, min_periods=max(28//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2106 * _rolling_slope(draw, 495) + 0.000359 * anchor
    return base_signal.diff()

def f06_vdd_590_accel_v590_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=35, w2=266, w3=508, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 35)
    baseline = trend.rolling(266, min_periods=max(266//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(508, min_periods=max(508//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.43 + 0.0003591 * anchor
    return base_signal.diff()

def f06_vdd_591_jerk_v591_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=42, w2=277, w3=521, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 42)
    slow = _rolling_slope(x, 277)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.444375 + 0.0003592 * anchor
    return base_signal.diff()

def f06_vdd_592_accel_v592_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=49, w2=288, w3=534, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(288, min_periods=max(288//3, 2)).max()
    trough = x.rolling(49, min_periods=max(49//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.45875 + 0.0003593 * anchor
    return base_signal.diff()

def f06_vdd_593_jerk_v593_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=56, w2=299, w3=547, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(56)
    rank = change.rolling(299, min_periods=max(299//3, 2)).rank(pct=True)
    persistence = change.rolling(547, min_periods=max(547//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.241 * persistence + 0.0003594 * anchor
    return base_signal.diff()

def f06_vdd_594_accel_v594_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=63, w2=310, w3=560, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(63, min_periods=max(63//3, 2)).std()
    vol_slow = ret.rolling(310, min_periods=max(310//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.4875 + 0.0003595 * anchor
    return base_signal.diff()

def f06_vdd_595_jerk_v595_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=70, w2=321, w3=573, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(321, min_periods=max(321//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 70)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2562 * slope + 0.0003596 * anchor
    return base_signal.diff()

def f06_vdd_596_accel_v596_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=77, w2=332, w3=586, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(77)
    drag = impulse.rolling(332, min_periods=max(332//3, 2)).mean()
    noise = impulse.abs().rolling(586, min_periods=max(586//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.51625 + 0.0003597 * anchor
    return base_signal.diff()

def f06_vdd_597_jerk_v597_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=84, w2=343, w3=599, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 84)
    acceleration = _rolling_slope(velocity, 343)
    curvature = _rolling_slope(acceleration, 599)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2714 * acceleration + 0.0003598 * anchor
    return base_signal.diff()

def f06_vdd_598_accel_v598_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=91, w2=354, w3=612, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(91, min_periods=max(91//3, 2)).mean(), upside.rolling(354, min_periods=max(354//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.545 + 0.0003599 * anchor
    return base_signal.diff()

def f06_vdd_599_jerk_v599_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=98, w2=365, w3=625, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(365, min_periods=max(365//3, 2)).max()
    rebound = x - x.rolling(98, min_periods=max(98//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2866 * _rolling_slope(draw, 625) + 0.00036 * anchor
    return base_signal.diff()

def f06_vdd_600_accel_v600_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=105, w2=376, w3=638, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 105)
    baseline = trend.rolling(376, min_periods=max(376//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(638, min_periods=max(638//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.57375 + 0.0003601 * anchor
    return base_signal.diff()
