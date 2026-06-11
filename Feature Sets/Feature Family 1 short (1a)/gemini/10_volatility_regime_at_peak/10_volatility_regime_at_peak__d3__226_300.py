"""10 volatility regime at peak d3 third derivative features 226-300 â€” Pipeline 1a-HF Grade v3.

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

def f10_vreg_226_accel_v226_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=164, w2=88, w3=711, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(88, min_periods=max(88//3, 2)).mean()
    noise = impulse.abs().rolling(711, min_periods=max(711//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.439375 + 0.0006227 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_227_jerk_v227_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=171, w2=99, w3=724, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 171)
    acceleration = _rolling_slope(velocity, 99)
    curvature = _rolling_slope(acceleration, 724)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3102 * acceleration + 0.0006228 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_228_accel_v228_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=178, w2=110, w3=737, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(178, min_periods=max(178//3, 2)).mean(), upside.rolling(110, min_periods=max(110//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.468125 + 0.0006229 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_229_jerk_v229_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=185, w2=121, w3=750, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(121, min_periods=max(121//3, 2)).max()
    rebound = x - x.rolling(185, min_periods=max(185//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3254 * _rolling_slope(draw, 750) + 0.000623 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_230_accel_v230_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=192, w2=132, w3=763, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 192)
    baseline = trend.rolling(132, min_periods=max(132//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(763, min_periods=max(763//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.496875 + 0.0006231 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_231_jerk_v231_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=199, w2=143, w3=19, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 199)
    slow = _rolling_slope(x, 143)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=19, adjust=False).mean() * 1.51125 + 0.0006232 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_232_accel_v232_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=206, w2=154, w3=32, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(154, min_periods=max(154//3, 2)).max()
    trough = x.rolling(206, min_periods=max(206//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.525625 + 0.0006233 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_233_jerk_v233_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=213, w2=165, w3=45, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(165, min_periods=max(165//3, 2)).rank(pct=True)
    persistence = change.rolling(45, min_periods=max(45//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3558 * persistence + 0.0006234 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_234_accel_v234_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=220, w2=176, w3=58, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(220, min_periods=max(220//3, 2)).std()
    vol_slow = ret.rolling(176, min_periods=max(176//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.554375 + 0.0006235 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_235_jerk_v235_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=227, w2=187, w3=71, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(187, min_periods=max(187//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 227)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.371 * slope + 0.0006236 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_236_accel_v236_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=234, w2=198, w3=84, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(198, min_periods=max(198//3, 2)).mean()
    noise = impulse.abs().rolling(84, min_periods=max(84//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.583125 + 0.0006237 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_237_jerk_v237_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=241, w2=209, w3=97, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 241)
    acceleration = _rolling_slope(velocity, 209)
    curvature = _rolling_slope(acceleration, 97)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3862 * acceleration + 0.0006238 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_238_accel_v238_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=248, w2=220, w3=110, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(248, min_periods=max(248//3, 2)).mean(), upside.rolling(220, min_periods=max(220//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(110) * 1.611875 + 0.0006239 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_239_jerk_v239_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=255, w2=231, w3=123, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(231, min_periods=max(231//3, 2)).max()
    rebound = x - x.rolling(255, min_periods=max(255//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.4014 * _rolling_slope(draw, 123) + 0.000624 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_240_accel_v240_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=11, w2=242, w3=136, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 11)
    baseline = trend.rolling(242, min_periods=max(242//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(136, min_periods=max(136//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.8675 + 0.0006241 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_241_jerk_v241_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=18, w2=253, w3=149, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 18)
    slow = _rolling_slope(x, 253)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=149, adjust=False).mean() * 0.881875 + 0.0006242 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_242_accel_v242_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=25, w2=264, w3=162, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(264, min_periods=max(264//3, 2)).max()
    trough = x.rolling(25, min_periods=max(25//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.89625 + 0.0006243 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_243_jerk_v243_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=32, w2=275, w3=175, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(32)
    rank = change.rolling(275, min_periods=max(275//3, 2)).rank(pct=True)
    persistence = change.rolling(175, min_periods=max(175//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0554 * persistence + 0.0006244 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_244_accel_v244_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=39, w2=286, w3=188, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(39, min_periods=max(39//3, 2)).std()
    vol_slow = ret.rolling(286, min_periods=max(286//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.925 + 0.0006245 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_245_jerk_v245_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=46, w2=297, w3=201, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(297, min_periods=max(297//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 46)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0706 * slope + 0.0006246 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_246_accel_v246_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=53, w2=308, w3=214, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(53)
    drag = impulse.rolling(308, min_periods=max(308//3, 2)).mean()
    noise = impulse.abs().rolling(214, min_periods=max(214//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.95375 + 0.0006247 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_247_jerk_v247_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=60, w2=319, w3=227, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 60)
    acceleration = _rolling_slope(velocity, 319)
    curvature = _rolling_slope(acceleration, 227)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0858 * acceleration + 0.0006248 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_248_accel_v248_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=67, w2=330, w3=240, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(67, min_periods=max(67//3, 2)).mean(), upside.rolling(330, min_periods=max(330//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.9825 + 0.0006249 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_249_jerk_v249_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=74, w2=341, w3=253, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(341, min_periods=max(341//3, 2)).max()
    rebound = x - x.rolling(74, min_periods=max(74//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.101 * _rolling_slope(draw, 253) + 0.000625 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_250_accel_v250_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=81, w2=352, w3=266, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 81)
    baseline = trend.rolling(352, min_periods=max(352//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(266, min_periods=max(266//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.01125 + 0.0006251 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_251_jerk_v251_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=88, w2=363, w3=279, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 88)
    slow = _rolling_slope(x, 363)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=279, adjust=False).mean() * 1.025625 + 0.0006252 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_252_accel_v252_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=95, w2=374, w3=292, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(374, min_periods=max(374//3, 2)).max()
    trough = x.rolling(95, min_periods=max(95//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.04 + 0.0006253 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_253_jerk_v253_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=102, w2=385, w3=305, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(102)
    rank = change.rolling(385, min_periods=max(385//3, 2)).rank(pct=True)
    persistence = change.rolling(305, min_periods=max(305//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1314 * persistence + 0.0006254 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_254_accel_v254_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=109, w2=396, w3=318, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(109, min_periods=max(109//3, 2)).std()
    vol_slow = ret.rolling(396, min_periods=max(396//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.06875 + 0.0006255 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_255_jerk_v255_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=116, w2=407, w3=331, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(407, min_periods=max(407//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 116)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1466 * slope + 0.0006256 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_256_accel_v256_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=123, w2=418, w3=344, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(123)
    drag = impulse.rolling(418, min_periods=max(418//3, 2)).mean()
    noise = impulse.abs().rolling(344, min_periods=max(344//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.0975 + 0.0006257 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_257_jerk_v257_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=130, w2=429, w3=357, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 130)
    acceleration = _rolling_slope(velocity, 429)
    curvature = _rolling_slope(acceleration, 357)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1618 * acceleration + 0.0006258 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_258_accel_v258_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=137, w2=440, w3=370, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(137, min_periods=max(137//3, 2)).mean(), upside.rolling(440, min_periods=max(440//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.12625 + 0.0006259 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_259_jerk_v259_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=144, w2=451, w3=383, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(451, min_periods=max(451//3, 2)).max()
    rebound = x - x.rolling(144, min_periods=max(144//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.177 * _rolling_slope(draw, 383) + 0.000626 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_260_accel_v260_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=151, w2=462, w3=396, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 151)
    baseline = trend.rolling(462, min_periods=max(462//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(396, min_periods=max(396//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.155 + 0.0006261 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_261_jerk_v261_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=158, w2=473, w3=409, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 158)
    slow = _rolling_slope(x, 473)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.169375 + 0.0006262 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_262_accel_v262_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=165, w2=484, w3=422, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(484, min_periods=max(484//3, 2)).max()
    trough = x.rolling(165, min_periods=max(165//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.18375 + 0.0006263 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_263_jerk_v263_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=172, w2=495, w3=435, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(495, min_periods=max(495//3, 2)).rank(pct=True)
    persistence = change.rolling(435, min_periods=max(435//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2074 * persistence + 0.0006264 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_264_accel_v264_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=179, w2=506, w3=448, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(179, min_periods=max(179//3, 2)).std()
    vol_slow = ret.rolling(506, min_periods=max(506//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.2125 + 0.0006265 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_265_jerk_v265_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=186, w2=14, w3=461, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(14, min_periods=max(14//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 186)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2226 * slope + 0.0006266 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_266_accel_v266_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=193, w2=25, w3=474, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(25, min_periods=max(25//3, 2)).mean()
    noise = impulse.abs().rolling(474, min_periods=max(474//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.24125 + 0.0006267 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_267_jerk_v267_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=200, w2=36, w3=487, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 200)
    acceleration = _rolling_slope(velocity, 36)
    curvature = _rolling_slope(acceleration, 487)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2378 * acceleration + 0.0006268 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_268_accel_v268_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=207, w2=47, w3=500, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(207, min_periods=max(207//3, 2)).mean(), upside.rolling(47, min_periods=max(47//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.27 + 0.0006269 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_269_jerk_v269_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=214, w2=58, w3=513, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(58, min_periods=max(58//3, 2)).max()
    rebound = x - x.rolling(214, min_periods=max(214//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.253 * _rolling_slope(draw, 513) + 0.000627 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_270_accel_v270_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=221, w2=69, w3=526, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 221)
    baseline = trend.rolling(69, min_periods=max(69//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(526, min_periods=max(526//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.29875 + 0.0006271 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_271_jerk_v271_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=228, w2=80, w3=539, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 228)
    slow = _rolling_slope(x, 80)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.313125 + 0.0006272 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_272_accel_v272_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=235, w2=91, w3=552, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(91, min_periods=max(91//3, 2)).max()
    trough = x.rolling(235, min_periods=max(235//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.3275 + 0.0006273 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_273_jerk_v273_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=242, w2=102, w3=565, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(102, min_periods=max(102//3, 2)).rank(pct=True)
    persistence = change.rolling(565, min_periods=max(565//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2834 * persistence + 0.0006274 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_274_accel_v274_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=249, w2=113, w3=578, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(249, min_periods=max(249//3, 2)).std()
    vol_slow = ret.rolling(113, min_periods=max(113//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.35625 + 0.0006275 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_275_jerk_v275_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=5, w2=124, w3=591, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(124, min_periods=max(124//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 5)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2986 * slope + 0.0006276 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_276_accel_v276_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=12, w2=135, w3=604, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(12)
    drag = impulse.rolling(135, min_periods=max(135//3, 2)).mean()
    noise = impulse.abs().rolling(604, min_periods=max(604//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.385 + 0.0006277 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_277_jerk_v277_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=19, w2=146, w3=617, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 19)
    acceleration = _rolling_slope(velocity, 146)
    curvature = _rolling_slope(acceleration, 617)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3138 * acceleration + 0.0006278 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_278_accel_v278_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=26, w2=157, w3=630, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(26, min_periods=max(26//3, 2)).mean(), upside.rolling(157, min_periods=max(157//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.41375 + 0.0006279 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_279_jerk_v279_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=33, w2=168, w3=643, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(168, min_periods=max(168//3, 2)).max()
    rebound = x - x.rolling(33, min_periods=max(33//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.329 * _rolling_slope(draw, 643) + 0.000628 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_280_accel_v280_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=40, w2=179, w3=656, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 40)
    baseline = trend.rolling(179, min_periods=max(179//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(656, min_periods=max(656//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.4425 + 0.0006281 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_281_jerk_v281_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=47, w2=190, w3=669, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 47)
    slow = _rolling_slope(x, 190)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.456875 + 0.0006282 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_282_accel_v282_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=54, w2=201, w3=682, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(201, min_periods=max(201//3, 2)).max()
    trough = x.rolling(54, min_periods=max(54//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.47125 + 0.0006283 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_283_jerk_v283_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=61, w2=212, w3=695, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(61)
    rank = change.rolling(212, min_periods=max(212//3, 2)).rank(pct=True)
    persistence = change.rolling(695, min_periods=max(695//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3594 * persistence + 0.0006284 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_284_accel_v284_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=68, w2=223, w3=708, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(68, min_periods=max(68//3, 2)).std()
    vol_slow = ret.rolling(223, min_periods=max(223//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.5 + 0.0006285 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_285_jerk_v285_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=75, w2=234, w3=721, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(234, min_periods=max(234//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 75)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3746 * slope + 0.0006286 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_286_accel_v286_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=82, w2=245, w3=734, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(82)
    drag = impulse.rolling(245, min_periods=max(245//3, 2)).mean()
    noise = impulse.abs().rolling(734, min_periods=max(734//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.52875 + 0.0006287 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_287_jerk_v287_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=89, w2=256, w3=747, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 89)
    acceleration = _rolling_slope(velocity, 256)
    curvature = _rolling_slope(acceleration, 747)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3898 * acceleration + 0.0006288 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_288_accel_v288_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=96, w2=267, w3=760, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(96, min_periods=max(96//3, 2)).mean(), upside.rolling(267, min_periods=max(267//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.5575 + 0.0006289 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_289_jerk_v289_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=103, w2=278, w3=16, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(278, min_periods=max(278//3, 2)).max()
    rebound = x - x.rolling(103, min_periods=max(103//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.405 * _rolling_slope(draw, 16) + 0.000629 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_290_accel_v290_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=110, w2=289, w3=29, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 110)
    baseline = trend.rolling(289, min_periods=max(289//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(29, min_periods=max(29//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.58625 + 0.0006291 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_291_jerk_v291_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=117, w2=300, w3=42, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 117)
    slow = _rolling_slope(x, 300)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=42, adjust=False).mean() * 1.600625 + 0.0006292 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_292_accel_v292_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=124, w2=311, w3=55, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(311, min_periods=max(311//3, 2)).max()
    trough = x.rolling(124, min_periods=max(124//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.615 + 0.0006293 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_293_jerk_v293_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=131, w2=322, w3=68, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(322, min_periods=max(322//3, 2)).rank(pct=True)
    persistence = change.rolling(68, min_periods=max(68//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.059 * persistence + 0.0006294 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_294_accel_v294_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=138, w2=333, w3=81, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(138, min_periods=max(138//3, 2)).std()
    vol_slow = ret.rolling(333, min_periods=max(333//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.870625 + 0.0006295 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_295_jerk_v295_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=145, w2=344, w3=94, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(344, min_periods=max(344//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 145)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0742 * slope + 0.0006296 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_296_accel_v296_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=152, w2=355, w3=107, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(355, min_periods=max(355//3, 2)).mean()
    noise = impulse.abs().rolling(107, min_periods=max(107//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.899375 + 0.0006297 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_297_jerk_v297_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=159, w2=366, w3=120, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 159)
    acceleration = _rolling_slope(velocity, 366)
    curvature = _rolling_slope(acceleration, 120)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0894 * acceleration + 0.0006298 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_298_accel_v298_d3(low: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=166, w2=377, w3=133, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(166, min_periods=max(166//3, 2)).mean(), upside.rolling(377, min_periods=max(377//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.928125 + 0.0006299 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_299_jerk_v299_d3(volume: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=173, w2=388, w3=146, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(388, min_periods=max(388//3, 2)).max()
    rebound = x - x.rolling(173, min_periods=max(173//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1046 * _rolling_slope(draw, 146) + 0.00063 * anchor
    return base_signal.diff().diff().diff()

def f10_vreg_300_accel_v300_d3(close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accel replacement signal (w1=180, w2=399, w3=159, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 180)
    baseline = trend.rolling(399, min_periods=max(399//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(159, min_periods=max(159//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.956875 + 0.0006301 * anchor
    return base_signal.diff().diff().diff()
