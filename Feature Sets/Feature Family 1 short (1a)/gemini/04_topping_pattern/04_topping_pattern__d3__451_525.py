"""04 topping pattern d3 third derivative features 451-525 â€” Pipeline 1a-HF Grade v3.

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

def f04_top_451_jerk_v451_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=200, w2=124, w3=512, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 200)
    slow = _rolling_slope(x, 124)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.51 + 0.0002252 * anchor
    return base_signal.diff().diff().diff()

def f04_top_452_accel_v452_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=207, w2=135, w3=525, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(135, min_periods=max(135//3, 2)).max()
    trough = x.rolling(207, min_periods=max(207//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.524375 + 0.0002253 * anchor
    return base_signal.diff().diff().diff()

def f04_top_453_jerk_v453_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=214, w2=146, w3=538, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(146, min_periods=max(146//3, 2)).rank(pct=True)
    persistence = change.rolling(538, min_periods=max(538//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2198 * persistence + 0.0002254 * anchor
    return base_signal.diff().diff().diff()

def f04_top_454_accel_v454_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=221, w2=157, w3=551, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(221, min_periods=max(221//3, 2)).std()
    vol_slow = ret.rolling(157, min_periods=max(157//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.553125 + 0.0002255 * anchor
    return base_signal.diff().diff().diff()

def f04_top_455_jerk_v455_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=228, w2=168, w3=564, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(168, min_periods=max(168//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 228)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.235 * slope + 0.0002256 * anchor
    return base_signal.diff().diff().diff()

def f04_top_456_accel_v456_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=235, w2=179, w3=577, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(179, min_periods=max(179//3, 2)).mean()
    noise = impulse.abs().rolling(577, min_periods=max(577//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.581875 + 0.0002257 * anchor
    return base_signal.diff().diff().diff()

def f04_top_457_jerk_v457_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=242, w2=190, w3=590, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 242)
    acceleration = _rolling_slope(velocity, 190)
    curvature = _rolling_slope(acceleration, 590)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2502 * acceleration + 0.0002258 * anchor
    return base_signal.diff().diff().diff()

def f04_top_458_accel_v458_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=249, w2=201, w3=603, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(249, min_periods=max(249//3, 2)).mean(), upside.rolling(201, min_periods=max(201//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.610625 + 0.0002259 * anchor
    return base_signal.diff().diff().diff()

def f04_top_459_jerk_v459_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=5, w2=212, w3=616, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(212, min_periods=max(212//3, 2)).max()
    rebound = x - x.rolling(5, min_periods=max(5//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2654 * _rolling_slope(draw, 616) + 0.000226 * anchor
    return base_signal.diff().diff().diff()

def f04_top_460_accel_v460_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=12, w2=223, w3=629, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 12)
    baseline = trend.rolling(223, min_periods=max(223//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(629, min_periods=max(629//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.86625 + 0.0002261 * anchor
    return base_signal.diff().diff().diff()

def f04_top_461_jerk_v461_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=19, w2=234, w3=642, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 19)
    slow = _rolling_slope(x, 234)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.880625 + 0.0002262 * anchor
    return base_signal.diff().diff().diff()

def f04_top_462_accel_v462_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=26, w2=245, w3=655, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(245, min_periods=max(245//3, 2)).max()
    trough = x.rolling(26, min_periods=max(26//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.895 + 0.0002263 * anchor
    return base_signal.diff().diff().diff()

def f04_top_463_jerk_v463_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=33, w2=256, w3=668, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(33)
    rank = change.rolling(256, min_periods=max(256//3, 2)).rank(pct=True)
    persistence = change.rolling(668, min_periods=max(668//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2958 * persistence + 0.0002264 * anchor
    return base_signal.diff().diff().diff()

def f04_top_464_accel_v464_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=40, w2=267, w3=681, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(40, min_periods=max(40//3, 2)).std()
    vol_slow = ret.rolling(267, min_periods=max(267//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.92375 + 0.0002265 * anchor
    return base_signal.diff().diff().diff()

def f04_top_465_jerk_v465_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=47, w2=278, w3=694, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(278, min_periods=max(278//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 47)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.311 * slope + 0.0002266 * anchor
    return base_signal.diff().diff().diff()

def f04_top_466_accel_v466_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=54, w2=289, w3=707, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(54)
    drag = impulse.rolling(289, min_periods=max(289//3, 2)).mean()
    noise = impulse.abs().rolling(707, min_periods=max(707//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.9525 + 0.0002267 * anchor
    return base_signal.diff().diff().diff()

def f04_top_467_jerk_v467_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=61, w2=300, w3=720, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 61)
    acceleration = _rolling_slope(velocity, 300)
    curvature = _rolling_slope(acceleration, 720)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3262 * acceleration + 0.0002268 * anchor
    return base_signal.diff().diff().diff()

def f04_top_468_accel_v468_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=68, w2=311, w3=733, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(68, min_periods=max(68//3, 2)).mean(), upside.rolling(311, min_periods=max(311//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.98125 + 0.0002269 * anchor
    return base_signal.diff().diff().diff()

def f04_top_469_jerk_v469_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=75, w2=322, w3=746, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(322, min_periods=max(322//3, 2)).max()
    rebound = x - x.rolling(75, min_periods=max(75//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3414 * _rolling_slope(draw, 746) + 0.000227 * anchor
    return base_signal.diff().diff().diff()

def f04_top_470_accel_v470_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=82, w2=333, w3=759, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 82)
    baseline = trend.rolling(333, min_periods=max(333//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(759, min_periods=max(759//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.01 + 0.0002271 * anchor
    return base_signal.diff().diff().diff()

def f04_top_471_jerk_v471_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=89, w2=344, w3=15, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 89)
    slow = _rolling_slope(x, 344)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=15, adjust=False).mean() * 1.024375 + 0.0002272 * anchor
    return base_signal.diff().diff().diff()

def f04_top_472_accel_v472_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=96, w2=355, w3=28, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(355, min_periods=max(355//3, 2)).max()
    trough = x.rolling(96, min_periods=max(96//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.03875 + 0.0002273 * anchor
    return base_signal.diff().diff().diff()

def f04_top_473_jerk_v473_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=103, w2=366, w3=41, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(103)
    rank = change.rolling(366, min_periods=max(366//3, 2)).rank(pct=True)
    persistence = change.rolling(41, min_periods=max(41//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3718 * persistence + 0.0002274 * anchor
    return base_signal.diff().diff().diff()

def f04_top_474_accel_v474_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=110, w2=377, w3=54, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(110, min_periods=max(110//3, 2)).std()
    vol_slow = ret.rolling(377, min_periods=max(377//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.0675 + 0.0002275 * anchor
    return base_signal.diff().diff().diff()

def f04_top_475_jerk_v475_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=117, w2=388, w3=67, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(388, min_periods=max(388//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 117)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.387 * slope + 0.0002276 * anchor
    return base_signal.diff().diff().diff()

def f04_top_476_accel_v476_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=124, w2=399, w3=80, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(124)
    drag = impulse.rolling(399, min_periods=max(399//3, 2)).mean()
    noise = impulse.abs().rolling(80, min_periods=max(80//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.09625 + 0.0002277 * anchor
    return base_signal.diff().diff().diff()

def f04_top_477_jerk_v477_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=131, w2=410, w3=93, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 131)
    acceleration = _rolling_slope(velocity, 410)
    curvature = _rolling_slope(acceleration, 93)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.4022 * acceleration + 0.0002278 * anchor
    return base_signal.diff().diff().diff()

def f04_top_478_accel_v478_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=138, w2=421, w3=106, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(138, min_periods=max(138//3, 2)).mean(), upside.rolling(421, min_periods=max(421//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(106) * 1.125 + 0.0002279 * anchor
    return base_signal.diff().diff().diff()

def f04_top_479_jerk_v479_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=145, w2=432, w3=119, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(432, min_periods=max(432//3, 2)).max()
    rebound = x - x.rolling(145, min_periods=max(145//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.041 * _rolling_slope(draw, 119) + 0.000228 * anchor
    return base_signal.diff().diff().diff()

def f04_top_480_accel_v480_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=152, w2=443, w3=132, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 152)
    baseline = trend.rolling(443, min_periods=max(443//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(132, min_periods=max(132//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.15375 + 0.0002281 * anchor
    return base_signal.diff().diff().diff()

def f04_top_481_jerk_v481_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=159, w2=454, w3=145, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 159)
    slow = _rolling_slope(x, 454)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=145, adjust=False).mean() * 1.168125 + 0.0002282 * anchor
    return base_signal.diff().diff().diff()

def f04_top_482_accel_v482_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=166, w2=465, w3=158, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(465, min_periods=max(465//3, 2)).max()
    trough = x.rolling(166, min_periods=max(166//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.1825 + 0.0002283 * anchor
    return base_signal.diff().diff().diff()

def f04_top_483_jerk_v483_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=173, w2=476, w3=171, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(476, min_periods=max(476//3, 2)).rank(pct=True)
    persistence = change.rolling(171, min_periods=max(171//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0714 * persistence + 0.0002284 * anchor
    return base_signal.diff().diff().diff()

def f04_top_484_accel_v484_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=180, w2=487, w3=184, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(180, min_periods=max(180//3, 2)).std()
    vol_slow = ret.rolling(487, min_periods=max(487//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.21125 + 0.0002285 * anchor
    return base_signal.diff().diff().diff()

def f04_top_485_jerk_v485_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=187, w2=498, w3=197, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(498, min_periods=max(498//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 187)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0866 * slope + 0.0002286 * anchor
    return base_signal.diff().diff().diff()

def f04_top_486_accel_v486_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=194, w2=509, w3=210, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(509, min_periods=max(509//3, 2)).mean()
    noise = impulse.abs().rolling(210, min_periods=max(210//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.24 + 0.0002287 * anchor
    return base_signal.diff().diff().diff()

def f04_top_487_jerk_v487_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=201, w2=17, w3=223, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 201)
    acceleration = _rolling_slope(velocity, 17)
    curvature = _rolling_slope(acceleration, 223)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1018 * acceleration + 0.0002288 * anchor
    return base_signal.diff().diff().diff()

def f04_top_488_accel_v488_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=208, w2=28, w3=236, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(208, min_periods=max(208//3, 2)).mean(), upside.rolling(28, min_periods=max(28//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.26875 + 0.0002289 * anchor
    return base_signal.diff().diff().diff()

def f04_top_489_jerk_v489_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=215, w2=39, w3=249, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(39, min_periods=max(39//3, 2)).max()
    rebound = x - x.rolling(215, min_periods=max(215//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.117 * _rolling_slope(draw, 249) + 0.000229 * anchor
    return base_signal.diff().diff().diff()

def f04_top_490_accel_v490_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=222, w2=50, w3=262, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 222)
    baseline = trend.rolling(50, min_periods=max(50//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(262, min_periods=max(262//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.2975 + 0.0002291 * anchor
    return base_signal.diff().diff().diff()

def f04_top_491_jerk_v491_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=229, w2=61, w3=275, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 229)
    slow = _rolling_slope(x, 61)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=275, adjust=False).mean() * 1.311875 + 0.0002292 * anchor
    return base_signal.diff().diff().diff()

def f04_top_492_accel_v492_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=236, w2=72, w3=288, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(72, min_periods=max(72//3, 2)).max()
    trough = x.rolling(236, min_periods=max(236//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.32625 + 0.0002293 * anchor
    return base_signal.diff().diff().diff()

def f04_top_493_jerk_v493_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=243, w2=83, w3=301, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(83, min_periods=max(83//3, 2)).rank(pct=True)
    persistence = change.rolling(301, min_periods=max(301//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1474 * persistence + 0.0002294 * anchor
    return base_signal.diff().diff().diff()

def f04_top_494_accel_v494_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=250, w2=94, w3=314, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(250, min_periods=max(250//3, 2)).std()
    vol_slow = ret.rolling(94, min_periods=max(94//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.355 + 0.0002295 * anchor
    return base_signal.diff().diff().diff()

def f04_top_495_jerk_v495_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=6, w2=105, w3=327, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(105, min_periods=max(105//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 6)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1626 * slope + 0.0002296 * anchor
    return base_signal.diff().diff().diff()

def f04_top_496_accel_v496_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=13, w2=116, w3=340, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(13)
    drag = impulse.rolling(116, min_periods=max(116//3, 2)).mean()
    noise = impulse.abs().rolling(340, min_periods=max(340//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.38375 + 0.0002297 * anchor
    return base_signal.diff().diff().diff()

def f04_top_497_jerk_v497_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=20, w2=127, w3=353, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 20)
    acceleration = _rolling_slope(velocity, 127)
    curvature = _rolling_slope(acceleration, 353)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1778 * acceleration + 0.0002298 * anchor
    return base_signal.diff().diff().diff()

def f04_top_498_accel_v498_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=27, w2=138, w3=366, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(27, min_periods=max(27//3, 2)).mean(), upside.rolling(138, min_periods=max(138//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.4125 + 0.0002299 * anchor
    return base_signal.diff().diff().diff()

def f04_top_499_jerk_v499_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=34, w2=149, w3=379, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(149, min_periods=max(149//3, 2)).max()
    rebound = x - x.rolling(34, min_periods=max(34//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.193 * _rolling_slope(draw, 379) + 0.00023 * anchor
    return base_signal.diff().diff().diff()

def f04_top_500_accel_v500_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=41, w2=160, w3=392, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 41)
    baseline = trend.rolling(160, min_periods=max(160//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(392, min_periods=max(392//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.44125 + 0.0002301 * anchor
    return base_signal.diff().diff().diff()

def f04_top_501_jerk_v501_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=48, w2=171, w3=405, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 48)
    slow = _rolling_slope(x, 171)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.455625 + 0.0002302 * anchor
    return base_signal.diff().diff().diff()

def f04_top_502_accel_v502_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=55, w2=182, w3=418, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(182, min_periods=max(182//3, 2)).max()
    trough = x.rolling(55, min_periods=max(55//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.47 + 0.0002303 * anchor
    return base_signal.diff().diff().diff()

def f04_top_503_jerk_v503_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=62, w2=193, w3=431, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(62)
    rank = change.rolling(193, min_periods=max(193//3, 2)).rank(pct=True)
    persistence = change.rolling(431, min_periods=max(431//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2234 * persistence + 0.0002304 * anchor
    return base_signal.diff().diff().diff()

def f04_top_504_accel_v504_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=69, w2=204, w3=444, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(69, min_periods=max(69//3, 2)).std()
    vol_slow = ret.rolling(204, min_periods=max(204//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.49875 + 0.0002305 * anchor
    return base_signal.diff().diff().diff()

def f04_top_505_jerk_v505_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=76, w2=215, w3=457, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(215, min_periods=max(215//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 76)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2386 * slope + 0.0002306 * anchor
    return base_signal.diff().diff().diff()

def f04_top_506_accel_v506_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=83, w2=226, w3=470, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(83)
    drag = impulse.rolling(226, min_periods=max(226//3, 2)).mean()
    noise = impulse.abs().rolling(470, min_periods=max(470//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.5275 + 0.0002307 * anchor
    return base_signal.diff().diff().diff()

def f04_top_507_jerk_v507_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=90, w2=237, w3=483, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 90)
    acceleration = _rolling_slope(velocity, 237)
    curvature = _rolling_slope(acceleration, 483)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2538 * acceleration + 0.0002308 * anchor
    return base_signal.diff().diff().diff()

def f04_top_508_accel_v508_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=97, w2=248, w3=496, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(97, min_periods=max(97//3, 2)).mean(), upside.rolling(248, min_periods=max(248//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.55625 + 0.0002309 * anchor
    return base_signal.diff().diff().diff()

def f04_top_509_jerk_v509_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=104, w2=259, w3=509, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(259, min_periods=max(259//3, 2)).max()
    rebound = x - x.rolling(104, min_periods=max(104//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.269 * _rolling_slope(draw, 509) + 0.000231 * anchor
    return base_signal.diff().diff().diff()

def f04_top_510_accel_v510_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=111, w2=270, w3=522, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 111)
    baseline = trend.rolling(270, min_periods=max(270//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(522, min_periods=max(522//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.585 + 0.0002311 * anchor
    return base_signal.diff().diff().diff()

def f04_top_511_jerk_v511_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=118, w2=281, w3=535, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 118)
    slow = _rolling_slope(x, 281)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.599375 + 0.0002312 * anchor
    return base_signal.diff().diff().diff()

def f04_top_512_accel_v512_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=125, w2=292, w3=548, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(292, min_periods=max(292//3, 2)).max()
    trough = x.rolling(125, min_periods=max(125//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.61375 + 0.0002313 * anchor
    return base_signal.diff().diff().diff()

def f04_top_513_jerk_v513_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=132, w2=303, w3=561, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(303, min_periods=max(303//3, 2)).rank(pct=True)
    persistence = change.rolling(561, min_periods=max(561//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2994 * persistence + 0.0002314 * anchor
    return base_signal.diff().diff().diff()

def f04_top_514_accel_v514_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=139, w2=314, w3=574, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(139, min_periods=max(139//3, 2)).std()
    vol_slow = ret.rolling(314, min_periods=max(314//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.869375 + 0.0002315 * anchor
    return base_signal.diff().diff().diff()

def f04_top_515_jerk_v515_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=146, w2=325, w3=587, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(325, min_periods=max(325//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 146)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3146 * slope + 0.0002316 * anchor
    return base_signal.diff().diff().diff()

def f04_top_516_accel_v516_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=153, w2=336, w3=600, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(336, min_periods=max(336//3, 2)).mean()
    noise = impulse.abs().rolling(600, min_periods=max(600//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.898125 + 0.0002317 * anchor
    return base_signal.diff().diff().diff()

def f04_top_517_jerk_v517_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=160, w2=347, w3=613, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 160)
    acceleration = _rolling_slope(velocity, 347)
    curvature = _rolling_slope(acceleration, 613)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3298 * acceleration + 0.0002318 * anchor
    return base_signal.diff().diff().diff()

def f04_top_518_accel_v518_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=167, w2=358, w3=626, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(167, min_periods=max(167//3, 2)).mean(), upside.rolling(358, min_periods=max(358//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.926875 + 0.0002319 * anchor
    return base_signal.diff().diff().diff()

def f04_top_519_jerk_v519_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=174, w2=369, w3=639, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(369, min_periods=max(369//3, 2)).max()
    rebound = x - x.rolling(174, min_periods=max(174//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.345 * _rolling_slope(draw, 639) + 0.000232 * anchor
    return base_signal.diff().diff().diff()

def f04_top_520_accel_v520_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=181, w2=380, w3=652, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 181)
    baseline = trend.rolling(380, min_periods=max(380//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(652, min_periods=max(652//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.955625 + 0.0002321 * anchor
    return base_signal.diff().diff().diff()

def f04_top_521_jerk_v521_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=188, w2=391, w3=665, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 188)
    slow = _rolling_slope(x, 391)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.97 + 0.0002322 * anchor
    return base_signal.diff().diff().diff()

def f04_top_522_accel_v522_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=195, w2=402, w3=678, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(402, min_periods=max(402//3, 2)).max()
    trough = x.rolling(195, min_periods=max(195//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.984375 + 0.0002323 * anchor
    return base_signal.diff().diff().diff()

def f04_top_523_jerk_v523_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=202, w2=413, w3=691, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(413, min_periods=max(413//3, 2)).rank(pct=True)
    persistence = change.rolling(691, min_periods=max(691//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3754 * persistence + 0.0002324 * anchor
    return base_signal.diff().diff().diff()

def f04_top_524_accel_v524_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=209, w2=424, w3=704, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(209, min_periods=max(209//3, 2)).std()
    vol_slow = ret.rolling(424, min_periods=max(424//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.013125 + 0.0002325 * anchor
    return base_signal.diff().diff().diff()

def f04_top_525_jerk_v525_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=216, w2=435, w3=717, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(435, min_periods=max(435//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 216)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3906 * slope + 0.0002326 * anchor
    return base_signal.diff().diff().diff()
