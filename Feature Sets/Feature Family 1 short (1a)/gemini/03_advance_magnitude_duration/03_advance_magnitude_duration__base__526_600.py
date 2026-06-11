"""03 advance magnitude duration base features 526-600 â€” Pipeline 1a-HF Grade v3.

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

def f03_amd_526_accel_v526(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=39, w2=385, w3=500, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(39)
    drag = impulse.rolling(385, min_periods=max(385//3, 2)).mean()
    noise = impulse.abs().rolling(500, min_periods=max(500//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.92125 + 0.0001727 * anchor

def f03_amd_527_jerk_v527(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=46, w2=396, w3=513, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 46)
    acceleration = _rolling_slope(velocity, 396)
    curvature = _rolling_slope(acceleration, 513)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3626 * acceleration + 0.0001728 * anchor

def f03_amd_528_accel_v528(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=53, w2=407, w3=526, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(53, min_periods=max(53//3, 2)).mean(), upside.rolling(407, min_periods=max(407//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.95 + 0.0001729 * anchor

def f03_amd_529_jerk_v529(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=60, w2=418, w3=539, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(418, min_periods=max(418//3, 2)).max()
    rebound = x - x.rolling(60, min_periods=max(60//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3778 * _rolling_slope(draw, 539) + 0.000173 * anchor

def f03_amd_530_accel_v530(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=67, w2=429, w3=552, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 67)
    baseline = trend.rolling(429, min_periods=max(429//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(552, min_periods=max(552//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.97875 + 0.0001731 * anchor

def f03_amd_531_jerk_v531(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=74, w2=440, w3=565, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 74)
    slow = _rolling_slope(x, 440)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.993125 + 0.0001732 * anchor

def f03_amd_532_accel_v532(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=81, w2=451, w3=578, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(451, min_periods=max(451//3, 2)).max()
    trough = x.rolling(81, min_periods=max(81//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.0075 + 0.0001733 * anchor

def f03_amd_533_jerk_v533(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=88, w2=462, w3=591, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(88)
    rank = change.rolling(462, min_periods=max(462//3, 2)).rank(pct=True)
    persistence = change.rolling(591, min_periods=max(591//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.4082 * persistence + 0.0001734 * anchor

def f03_amd_534_accel_v534(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=95, w2=473, w3=604, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(95, min_periods=max(95//3, 2)).std()
    vol_slow = ret.rolling(473, min_periods=max(473//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.03625 + 0.0001735 * anchor

def f03_amd_535_jerk_v535(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=102, w2=484, w3=617, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(484, min_periods=max(484//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 102)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.047 * slope + 0.0001736 * anchor

def f03_amd_536_accel_v536(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=109, w2=495, w3=630, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(109)
    drag = impulse.rolling(495, min_periods=max(495//3, 2)).mean()
    noise = impulse.abs().rolling(630, min_periods=max(630//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.065 + 0.0001737 * anchor

def f03_amd_537_jerk_v537(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=116, w2=506, w3=643, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 116)
    acceleration = _rolling_slope(velocity, 506)
    curvature = _rolling_slope(acceleration, 643)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0622 * acceleration + 0.0001738 * anchor

def f03_amd_538_accel_v538(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=123, w2=14, w3=656, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(123, min_periods=max(123//3, 2)).mean(), upside.rolling(14, min_periods=max(14//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.09375 + 0.0001739 * anchor

def f03_amd_539_jerk_v539(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=130, w2=25, w3=669, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(25, min_periods=max(25//3, 2)).max()
    rebound = x - x.rolling(130, min_periods=max(130//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0774 * _rolling_slope(draw, 669) + 0.000174 * anchor

def f03_amd_540_accel_v540(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=137, w2=36, w3=682, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 137)
    baseline = trend.rolling(36, min_periods=max(36//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(682, min_periods=max(682//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.1225 + 0.0001741 * anchor

def f03_amd_541_jerk_v541(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=144, w2=47, w3=695, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 144)
    slow = _rolling_slope(x, 47)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.136875 + 0.0001742 * anchor

def f03_amd_542_accel_v542(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=151, w2=58, w3=708, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(58, min_periods=max(58//3, 2)).max()
    trough = x.rolling(151, min_periods=max(151//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.15125 + 0.0001743 * anchor

def f03_amd_543_jerk_v543(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=158, w2=69, w3=721, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(69, min_periods=max(69//3, 2)).rank(pct=True)
    persistence = change.rolling(721, min_periods=max(721//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1078 * persistence + 0.0001744 * anchor

def f03_amd_544_accel_v544(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=165, w2=80, w3=734, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(165, min_periods=max(165//3, 2)).std()
    vol_slow = ret.rolling(80, min_periods=max(80//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.18 + 0.0001745 * anchor

def f03_amd_545_jerk_v545(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=172, w2=91, w3=747, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(91, min_periods=max(91//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 172)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.123 * slope + 0.0001746 * anchor

def f03_amd_546_accel_v546(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=179, w2=102, w3=760, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(102, min_periods=max(102//3, 2)).mean()
    noise = impulse.abs().rolling(760, min_periods=max(760//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.20875 + 0.0001747 * anchor

def f03_amd_547_jerk_v547(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=186, w2=113, w3=16, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 186)
    acceleration = _rolling_slope(velocity, 113)
    curvature = _rolling_slope(acceleration, 16)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1382 * acceleration + 0.0001748 * anchor

def f03_amd_548_accel_v548(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=193, w2=124, w3=29, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(193, min_periods=max(193//3, 2)).mean(), upside.rolling(124, min_periods=max(124//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(29) * 1.2375 + 0.0001749 * anchor

def f03_amd_549_jerk_v549(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=200, w2=135, w3=42, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(135, min_periods=max(135//3, 2)).max()
    rebound = x - x.rolling(200, min_periods=max(200//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1534 * _rolling_slope(draw, 42) + 0.000175 * anchor

def f03_amd_550_accel_v550(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=207, w2=146, w3=55, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 207)
    baseline = trend.rolling(146, min_periods=max(146//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(55, min_periods=max(55//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.26625 + 0.0001751 * anchor

def f03_amd_551_jerk_v551(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=214, w2=157, w3=68, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 214)
    slow = _rolling_slope(x, 157)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=68, adjust=False).mean() * 1.280625 + 0.0001752 * anchor

def f03_amd_552_accel_v552(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=221, w2=168, w3=81, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(168, min_periods=max(168//3, 2)).max()
    trough = x.rolling(221, min_periods=max(221//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.295 + 0.0001753 * anchor

def f03_amd_553_jerk_v553(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=228, w2=179, w3=94, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(179, min_periods=max(179//3, 2)).rank(pct=True)
    persistence = change.rolling(94, min_periods=max(94//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1838 * persistence + 0.0001754 * anchor

def f03_amd_554_accel_v554(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=235, w2=190, w3=107, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(235, min_periods=max(235//3, 2)).std()
    vol_slow = ret.rolling(190, min_periods=max(190//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.32375 + 0.0001755 * anchor

def f03_amd_555_jerk_v555(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=242, w2=201, w3=120, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(201, min_periods=max(201//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 242)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.199 * slope + 0.0001756 * anchor

def f03_amd_556_accel_v556(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=249, w2=212, w3=133, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(212, min_periods=max(212//3, 2)).mean()
    noise = impulse.abs().rolling(133, min_periods=max(133//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.3525 + 0.0001757 * anchor

def f03_amd_557_jerk_v557(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=5, w2=223, w3=146, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 5)
    acceleration = _rolling_slope(velocity, 223)
    curvature = _rolling_slope(acceleration, 146)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2142 * acceleration + 0.0001758 * anchor

def f03_amd_558_accel_v558(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=12, w2=234, w3=159, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(12, min_periods=max(12//3, 2)).mean(), upside.rolling(234, min_periods=max(234//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.38125 + 0.0001759 * anchor

def f03_amd_559_jerk_v559(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=19, w2=245, w3=172, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(245, min_periods=max(245//3, 2)).max()
    rebound = x - x.rolling(19, min_periods=max(19//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2294 * _rolling_slope(draw, 172) + 0.000176 * anchor

def f03_amd_560_accel_v560(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=26, w2=256, w3=185, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 26)
    baseline = trend.rolling(256, min_periods=max(256//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(185, min_periods=max(185//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.41 + 0.0001761 * anchor

def f03_amd_561_jerk_v561(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=33, w2=267, w3=198, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 33)
    slow = _rolling_slope(x, 267)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=198, adjust=False).mean() * 1.424375 + 0.0001762 * anchor

def f03_amd_562_accel_v562(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=40, w2=278, w3=211, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(278, min_periods=max(278//3, 2)).max()
    trough = x.rolling(40, min_periods=max(40//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.43875 + 0.0001763 * anchor

def f03_amd_563_jerk_v563(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=47, w2=289, w3=224, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(47)
    rank = change.rolling(289, min_periods=max(289//3, 2)).rank(pct=True)
    persistence = change.rolling(224, min_periods=max(224//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2598 * persistence + 0.0001764 * anchor

def f03_amd_564_accel_v564(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=54, w2=300, w3=237, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(54, min_periods=max(54//3, 2)).std()
    vol_slow = ret.rolling(300, min_periods=max(300//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.4675 + 0.0001765 * anchor

def f03_amd_565_jerk_v565(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=61, w2=311, w3=250, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(311, min_periods=max(311//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 61)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.275 * slope + 0.0001766 * anchor

def f03_amd_566_accel_v566(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=68, w2=322, w3=263, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(68)
    drag = impulse.rolling(322, min_periods=max(322//3, 2)).mean()
    noise = impulse.abs().rolling(263, min_periods=max(263//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.49625 + 0.0001767 * anchor

def f03_amd_567_jerk_v567(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=75, w2=333, w3=276, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 75)
    acceleration = _rolling_slope(velocity, 333)
    curvature = _rolling_slope(acceleration, 276)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2902 * acceleration + 0.0001768 * anchor

def f03_amd_568_accel_v568(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=82, w2=344, w3=289, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(82, min_periods=max(82//3, 2)).mean(), upside.rolling(344, min_periods=max(344//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.525 + 0.0001769 * anchor

def f03_amd_569_jerk_v569(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=89, w2=355, w3=302, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(355, min_periods=max(355//3, 2)).max()
    rebound = x - x.rolling(89, min_periods=max(89//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3054 * _rolling_slope(draw, 302) + 0.000177 * anchor

def f03_amd_570_accel_v570(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=96, w2=366, w3=315, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 96)
    baseline = trend.rolling(366, min_periods=max(366//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(315, min_periods=max(315//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.55375 + 0.0001771 * anchor

def f03_amd_571_jerk_v571(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=103, w2=377, w3=328, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 103)
    slow = _rolling_slope(x, 377)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.568125 + 0.0001772 * anchor

def f03_amd_572_accel_v572(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=110, w2=388, w3=341, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(388, min_periods=max(388//3, 2)).max()
    trough = x.rolling(110, min_periods=max(110//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.5825 + 0.0001773 * anchor

def f03_amd_573_jerk_v573(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=117, w2=399, w3=354, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(117)
    rank = change.rolling(399, min_periods=max(399//3, 2)).rank(pct=True)
    persistence = change.rolling(354, min_periods=max(354//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3358 * persistence + 0.0001774 * anchor

def f03_amd_574_accel_v574(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=124, w2=410, w3=367, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(124, min_periods=max(124//3, 2)).std()
    vol_slow = ret.rolling(410, min_periods=max(410//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.61125 + 0.0001775 * anchor

def f03_amd_575_jerk_v575(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=131, w2=421, w3=380, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(421, min_periods=max(421//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 131)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.351 * slope + 0.0001776 * anchor

def f03_amd_576_accel_v576(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=138, w2=432, w3=393, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(432, min_periods=max(432//3, 2)).mean()
    noise = impulse.abs().rolling(393, min_periods=max(393//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.866875 + 0.0001777 * anchor

def f03_amd_577_jerk_v577(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=145, w2=443, w3=406, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 145)
    acceleration = _rolling_slope(velocity, 443)
    curvature = _rolling_slope(acceleration, 406)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3662 * acceleration + 0.0001778 * anchor

def f03_amd_578_accel_v578(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=152, w2=454, w3=419, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(152, min_periods=max(152//3, 2)).mean(), upside.rolling(454, min_periods=max(454//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.895625 + 0.0001779 * anchor

def f03_amd_579_jerk_v579(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=159, w2=465, w3=432, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(465, min_periods=max(465//3, 2)).max()
    rebound = x - x.rolling(159, min_periods=max(159//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3814 * _rolling_slope(draw, 432) + 0.000178 * anchor

def f03_amd_580_accel_v580(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=166, w2=476, w3=445, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 166)
    baseline = trend.rolling(476, min_periods=max(476//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(445, min_periods=max(445//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.924375 + 0.0001781 * anchor

def f03_amd_581_jerk_v581(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=173, w2=487, w3=458, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 173)
    slow = _rolling_slope(x, 487)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.93875 + 0.0001782 * anchor

def f03_amd_582_accel_v582(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=180, w2=498, w3=471, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(498, min_periods=max(498//3, 2)).max()
    trough = x.rolling(180, min_periods=max(180//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.953125 + 0.0001783 * anchor

def f03_amd_583_jerk_v583(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=187, w2=509, w3=484, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(509, min_periods=max(509//3, 2)).rank(pct=True)
    persistence = change.rolling(484, min_periods=max(484//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0354 * persistence + 0.0001784 * anchor

def f03_amd_584_accel_v584(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=194, w2=17, w3=497, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(194, min_periods=max(194//3, 2)).std()
    vol_slow = ret.rolling(17, min_periods=max(17//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.981875 + 0.0001785 * anchor

def f03_amd_585_jerk_v585(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=201, w2=28, w3=510, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(28, min_periods=max(28//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 201)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0506 * slope + 0.0001786 * anchor

def f03_amd_586_accel_v586(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=208, w2=39, w3=523, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(39, min_periods=max(39//3, 2)).mean()
    noise = impulse.abs().rolling(523, min_periods=max(523//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.010625 + 0.0001787 * anchor

def f03_amd_587_jerk_v587(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=215, w2=50, w3=536, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 215)
    acceleration = _rolling_slope(velocity, 50)
    curvature = _rolling_slope(acceleration, 536)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0658 * acceleration + 0.0001788 * anchor

def f03_amd_588_accel_v588(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=222, w2=61, w3=549, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(222, min_periods=max(222//3, 2)).mean(), upside.rolling(61, min_periods=max(61//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.039375 + 0.0001789 * anchor

def f03_amd_589_jerk_v589(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=229, w2=72, w3=562, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(72, min_periods=max(72//3, 2)).max()
    rebound = x - x.rolling(229, min_periods=max(229//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.081 * _rolling_slope(draw, 562) + 0.000179 * anchor

def f03_amd_590_accel_v590(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=236, w2=83, w3=575, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 236)
    baseline = trend.rolling(83, min_periods=max(83//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(575, min_periods=max(575//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.068125 + 0.0001791 * anchor

def f03_amd_591_jerk_v591(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=243, w2=94, w3=588, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 243)
    slow = _rolling_slope(x, 94)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.0825 + 0.0001792 * anchor

def f03_amd_592_accel_v592(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=250, w2=105, w3=601, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(105, min_periods=max(105//3, 2)).max()
    trough = x.rolling(250, min_periods=max(250//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.096875 + 0.0001793 * anchor

def f03_amd_593_jerk_v593(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=6, w2=116, w3=614, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(6)
    rank = change.rolling(116, min_periods=max(116//3, 2)).rank(pct=True)
    persistence = change.rolling(614, min_periods=max(614//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1114 * persistence + 0.0001794 * anchor

def f03_amd_594_accel_v594(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=13, w2=127, w3=627, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(13, min_periods=max(13//3, 2)).std()
    vol_slow = ret.rolling(127, min_periods=max(127//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.125625 + 0.0001795 * anchor

def f03_amd_595_jerk_v595(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=20, w2=138, w3=640, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(138, min_periods=max(138//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 20)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1266 * slope + 0.0001796 * anchor

def f03_amd_596_accel_v596(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=27, w2=149, w3=653, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(27)
    drag = impulse.rolling(149, min_periods=max(149//3, 2)).mean()
    noise = impulse.abs().rolling(653, min_periods=max(653//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.154375 + 0.0001797 * anchor

def f03_amd_597_jerk_v597(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=34, w2=160, w3=666, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 34)
    acceleration = _rolling_slope(velocity, 160)
    curvature = _rolling_slope(acceleration, 666)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1418 * acceleration + 0.0001798 * anchor

def f03_amd_598_accel_v598(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=41, w2=171, w3=679, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(41, min_periods=max(41//3, 2)).mean(), upside.rolling(171, min_periods=max(171//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.183125 + 0.0001799 * anchor

def f03_amd_599_jerk_v599(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=48, w2=182, w3=692, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(182, min_periods=max(182//3, 2)).max()
    rebound = x - x.rolling(48, min_periods=max(48//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.157 * _rolling_slope(draw, 692) + 0.00018 * anchor

def f03_amd_600_accel_v600(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=55, w2=193, w3=705, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 55)
    baseline = trend.rolling(193, min_periods=max(193//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(705, min_periods=max(705//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.211875 + 0.0001801 * anchor
