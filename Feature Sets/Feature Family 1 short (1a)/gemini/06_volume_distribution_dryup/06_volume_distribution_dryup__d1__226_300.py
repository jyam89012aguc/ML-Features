"""06 volume distribution dryup d1 first derivative features 226-300 â€” Pipeline 1a-HF Grade v3.

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

def f06_vdd_226_accel_v226_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=248, w2=286, w3=318, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(286, min_periods=max(286//3, 2)).mean()
    noise = impulse.abs().rolling(318, min_periods=max(318//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.609375 + 0.0003227 * anchor
    return base_signal.diff()

def f06_vdd_227_jerk_v227_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=255, w2=297, w3=331, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 255)
    acceleration = _rolling_slope(velocity, 297)
    curvature = _rolling_slope(acceleration, 331)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0942 * acceleration + 0.0003228 * anchor
    return base_signal.diff()

def f06_vdd_228_accel_v228_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=11, w2=308, w3=344, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(11, min_periods=max(11//3, 2)).mean(), upside.rolling(308, min_periods=max(308//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.865 + 0.0003229 * anchor
    return base_signal.diff()

def f06_vdd_229_jerk_v229_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=18, w2=319, w3=357, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(319, min_periods=max(319//3, 2)).max()
    rebound = x - x.rolling(18, min_periods=max(18//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1094 * _rolling_slope(draw, 357) + 0.000323 * anchor
    return base_signal.diff()

def f06_vdd_230_accel_v230_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=25, w2=330, w3=370, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 25)
    baseline = trend.rolling(330, min_periods=max(330//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(370, min_periods=max(370//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.89375 + 0.0003231 * anchor
    return base_signal.diff()

def f06_vdd_231_jerk_v231_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=32, w2=341, w3=383, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 32)
    slow = _rolling_slope(x, 341)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.908125 + 0.0003232 * anchor
    return base_signal.diff()

def f06_vdd_232_accel_v232_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=39, w2=352, w3=396, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(352, min_periods=max(352//3, 2)).max()
    trough = x.rolling(39, min_periods=max(39//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.9225 + 0.0003233 * anchor
    return base_signal.diff()

def f06_vdd_233_jerk_v233_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=46, w2=363, w3=409, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(46)
    rank = change.rolling(363, min_periods=max(363//3, 2)).rank(pct=True)
    persistence = change.rolling(409, min_periods=max(409//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1398 * persistence + 0.0003234 * anchor
    return base_signal.diff()

def f06_vdd_234_accel_v234_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=53, w2=374, w3=422, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(53, min_periods=max(53//3, 2)).std()
    vol_slow = ret.rolling(374, min_periods=max(374//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.95125 + 0.0003235 * anchor
    return base_signal.diff()

def f06_vdd_235_jerk_v235_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=60, w2=385, w3=435, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(385, min_periods=max(385//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 60)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.155 * slope + 0.0003236 * anchor
    return base_signal.diff()

def f06_vdd_236_accel_v236_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=67, w2=396, w3=448, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(67)
    drag = impulse.rolling(396, min_periods=max(396//3, 2)).mean()
    noise = impulse.abs().rolling(448, min_periods=max(448//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.98 + 0.0003237 * anchor
    return base_signal.diff()

def f06_vdd_237_jerk_v237_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=74, w2=407, w3=461, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 74)
    acceleration = _rolling_slope(velocity, 407)
    curvature = _rolling_slope(acceleration, 461)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1702 * acceleration + 0.0003238 * anchor
    return base_signal.diff()

def f06_vdd_238_accel_v238_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=81, w2=418, w3=474, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(81, min_periods=max(81//3, 2)).mean(), upside.rolling(418, min_periods=max(418//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.00875 + 0.0003239 * anchor
    return base_signal.diff()

def f06_vdd_239_jerk_v239_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=88, w2=429, w3=487, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(429, min_periods=max(429//3, 2)).max()
    rebound = x - x.rolling(88, min_periods=max(88//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1854 * _rolling_slope(draw, 487) + 0.000324 * anchor
    return base_signal.diff()

def f06_vdd_240_accel_v240_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=95, w2=440, w3=500, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 95)
    baseline = trend.rolling(440, min_periods=max(440//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(500, min_periods=max(500//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.0375 + 0.0003241 * anchor
    return base_signal.diff()

def f06_vdd_241_jerk_v241_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=102, w2=451, w3=513, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 102)
    slow = _rolling_slope(x, 451)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.051875 + 0.0003242 * anchor
    return base_signal.diff()

def f06_vdd_242_accel_v242_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=109, w2=462, w3=526, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(462, min_periods=max(462//3, 2)).max()
    trough = x.rolling(109, min_periods=max(109//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.06625 + 0.0003243 * anchor
    return base_signal.diff()

def f06_vdd_243_jerk_v243_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=116, w2=473, w3=539, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(116)
    rank = change.rolling(473, min_periods=max(473//3, 2)).rank(pct=True)
    persistence = change.rolling(539, min_periods=max(539//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2158 * persistence + 0.0003244 * anchor
    return base_signal.diff()

def f06_vdd_244_accel_v244_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=123, w2=484, w3=552, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(123, min_periods=max(123//3, 2)).std()
    vol_slow = ret.rolling(484, min_periods=max(484//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.095 + 0.0003245 * anchor
    return base_signal.diff()

def f06_vdd_245_jerk_v245_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=130, w2=495, w3=565, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(495, min_periods=max(495//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 130)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.231 * slope + 0.0003246 * anchor
    return base_signal.diff()

def f06_vdd_246_accel_v246_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=137, w2=506, w3=578, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(506, min_periods=max(506//3, 2)).mean()
    noise = impulse.abs().rolling(578, min_periods=max(578//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.12375 + 0.0003247 * anchor
    return base_signal.diff()

def f06_vdd_247_jerk_v247_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=144, w2=14, w3=591, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 144)
    acceleration = _rolling_slope(velocity, 14)
    curvature = _rolling_slope(acceleration, 591)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2462 * acceleration + 0.0003248 * anchor
    return base_signal.diff()

def f06_vdd_248_accel_v248_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=151, w2=25, w3=604, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(151, min_periods=max(151//3, 2)).mean(), upside.rolling(25, min_periods=max(25//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.1525 + 0.0003249 * anchor
    return base_signal.diff()

def f06_vdd_249_jerk_v249_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=158, w2=36, w3=617, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(36, min_periods=max(36//3, 2)).max()
    rebound = x - x.rolling(158, min_periods=max(158//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2614 * _rolling_slope(draw, 617) + 0.000325 * anchor
    return base_signal.diff()

def f06_vdd_250_accel_v250_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=165, w2=47, w3=630, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 165)
    baseline = trend.rolling(47, min_periods=max(47//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(630, min_periods=max(630//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.18125 + 0.0003251 * anchor
    return base_signal.diff()

def f06_vdd_251_jerk_v251_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=172, w2=58, w3=643, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 172)
    slow = _rolling_slope(x, 58)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.195625 + 0.0003252 * anchor
    return base_signal.diff()

def f06_vdd_252_accel_v252_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=179, w2=69, w3=656, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(69, min_periods=max(69//3, 2)).max()
    trough = x.rolling(179, min_periods=max(179//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.21 + 0.0003253 * anchor
    return base_signal.diff()

def f06_vdd_253_jerk_v253_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=186, w2=80, w3=669, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(80, min_periods=max(80//3, 2)).rank(pct=True)
    persistence = change.rolling(669, min_periods=max(669//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2918 * persistence + 0.0003254 * anchor
    return base_signal.diff()

def f06_vdd_254_accel_v254_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=193, w2=91, w3=682, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(193, min_periods=max(193//3, 2)).std()
    vol_slow = ret.rolling(91, min_periods=max(91//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.23875 + 0.0003255 * anchor
    return base_signal.diff()

def f06_vdd_255_jerk_v255_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=200, w2=102, w3=695, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(102, min_periods=max(102//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 200)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.307 * slope + 0.0003256 * anchor
    return base_signal.diff()

def f06_vdd_256_accel_v256_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=207, w2=113, w3=708, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(113, min_periods=max(113//3, 2)).mean()
    noise = impulse.abs().rolling(708, min_periods=max(708//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.2675 + 0.0003257 * anchor
    return base_signal.diff()

def f06_vdd_257_jerk_v257_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=214, w2=124, w3=721, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 214)
    acceleration = _rolling_slope(velocity, 124)
    curvature = _rolling_slope(acceleration, 721)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3222 * acceleration + 0.0003258 * anchor
    return base_signal.diff()

def f06_vdd_258_accel_v258_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=221, w2=135, w3=734, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(221, min_periods=max(221//3, 2)).mean(), upside.rolling(135, min_periods=max(135//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.29625 + 0.0003259 * anchor
    return base_signal.diff()

def f06_vdd_259_jerk_v259_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=228, w2=146, w3=747, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(146, min_periods=max(146//3, 2)).max()
    rebound = x - x.rolling(228, min_periods=max(228//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3374 * _rolling_slope(draw, 747) + 0.000326 * anchor
    return base_signal.diff()

def f06_vdd_260_accel_v260_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=235, w2=157, w3=760, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 235)
    baseline = trend.rolling(157, min_periods=max(157//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(760, min_periods=max(760//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.325 + 0.0003261 * anchor
    return base_signal.diff()

def f06_vdd_261_jerk_v261_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=242, w2=168, w3=16, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 242)
    slow = _rolling_slope(x, 168)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=16, adjust=False).mean() * 1.339375 + 0.0003262 * anchor
    return base_signal.diff()

def f06_vdd_262_accel_v262_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=249, w2=179, w3=29, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(179, min_periods=max(179//3, 2)).max()
    trough = x.rolling(249, min_periods=max(249//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.35375 + 0.0003263 * anchor
    return base_signal.diff()

def f06_vdd_263_jerk_v263_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=5, w2=190, w3=42, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(5)
    rank = change.rolling(190, min_periods=max(190//3, 2)).rank(pct=True)
    persistence = change.rolling(42, min_periods=max(42//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3678 * persistence + 0.0003264 * anchor
    return base_signal.diff()

def f06_vdd_264_accel_v264_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=12, w2=201, w3=55, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(12, min_periods=max(12//3, 2)).std()
    vol_slow = ret.rolling(201, min_periods=max(201//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.3825 + 0.0003265 * anchor
    return base_signal.diff()

def f06_vdd_265_jerk_v265_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=19, w2=212, w3=68, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(212, min_periods=max(212//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 19)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.383 * slope + 0.0003266 * anchor
    return base_signal.diff()

def f06_vdd_266_accel_v266_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=26, w2=223, w3=81, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(26)
    drag = impulse.rolling(223, min_periods=max(223//3, 2)).mean()
    noise = impulse.abs().rolling(81, min_periods=max(81//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.41125 + 0.0003267 * anchor
    return base_signal.diff()

def f06_vdd_267_jerk_v267_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=33, w2=234, w3=94, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 33)
    acceleration = _rolling_slope(velocity, 234)
    curvature = _rolling_slope(acceleration, 94)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3982 * acceleration + 0.0003268 * anchor
    return base_signal.diff()

def f06_vdd_268_accel_v268_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=40, w2=245, w3=107, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(40, min_periods=max(40//3, 2)).mean(), upside.rolling(245, min_periods=max(245//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(107) * 1.44 + 0.0003269 * anchor
    return base_signal.diff()

def f06_vdd_269_jerk_v269_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=47, w2=256, w3=120, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(256, min_periods=max(256//3, 2)).max()
    rebound = x - x.rolling(47, min_periods=max(47//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.037 * _rolling_slope(draw, 120) + 0.000327 * anchor
    return base_signal.diff()

def f06_vdd_270_accel_v270_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=54, w2=267, w3=133, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 54)
    baseline = trend.rolling(267, min_periods=max(267//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(133, min_periods=max(133//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.46875 + 0.0003271 * anchor
    return base_signal.diff()

def f06_vdd_271_jerk_v271_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=61, w2=278, w3=146, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 61)
    slow = _rolling_slope(x, 278)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=146, adjust=False).mean() * 1.483125 + 0.0003272 * anchor
    return base_signal.diff()

def f06_vdd_272_accel_v272_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=68, w2=289, w3=159, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(289, min_periods=max(289//3, 2)).max()
    trough = x.rolling(68, min_periods=max(68//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.4975 + 0.0003273 * anchor
    return base_signal.diff()

def f06_vdd_273_jerk_v273_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=75, w2=300, w3=172, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(75)
    rank = change.rolling(300, min_periods=max(300//3, 2)).rank(pct=True)
    persistence = change.rolling(172, min_periods=max(172//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0674 * persistence + 0.0003274 * anchor
    return base_signal.diff()

def f06_vdd_274_accel_v274_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=82, w2=311, w3=185, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(82, min_periods=max(82//3, 2)).std()
    vol_slow = ret.rolling(311, min_periods=max(311//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.52625 + 0.0003275 * anchor
    return base_signal.diff()

def f06_vdd_275_jerk_v275_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=89, w2=322, w3=198, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(322, min_periods=max(322//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 89)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0826 * slope + 0.0003276 * anchor
    return base_signal.diff()

def f06_vdd_276_accel_v276_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=96, w2=333, w3=211, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(96)
    drag = impulse.rolling(333, min_periods=max(333//3, 2)).mean()
    noise = impulse.abs().rolling(211, min_periods=max(211//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.555 + 0.0003277 * anchor
    return base_signal.diff()

def f06_vdd_277_jerk_v277_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=103, w2=344, w3=224, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 103)
    acceleration = _rolling_slope(velocity, 344)
    curvature = _rolling_slope(acceleration, 224)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0978 * acceleration + 0.0003278 * anchor
    return base_signal.diff()

def f06_vdd_278_accel_v278_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=110, w2=355, w3=237, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(110, min_periods=max(110//3, 2)).mean(), upside.rolling(355, min_periods=max(355//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.58375 + 0.0003279 * anchor
    return base_signal.diff()

def f06_vdd_279_jerk_v279_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=117, w2=366, w3=250, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(366, min_periods=max(366//3, 2)).max()
    rebound = x - x.rolling(117, min_periods=max(117//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.113 * _rolling_slope(draw, 250) + 0.000328 * anchor
    return base_signal.diff()

def f06_vdd_280_accel_v280_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=124, w2=377, w3=263, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 124)
    baseline = trend.rolling(377, min_periods=max(377//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(263, min_periods=max(263//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.6125 + 0.0003281 * anchor
    return base_signal.diff()

def f06_vdd_281_jerk_v281_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=131, w2=388, w3=276, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 131)
    slow = _rolling_slope(x, 388)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=276, adjust=False).mean() * 0.85375 + 0.0003282 * anchor
    return base_signal.diff()

def f06_vdd_282_accel_v282_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=138, w2=399, w3=289, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(399, min_periods=max(399//3, 2)).max()
    trough = x.rolling(138, min_periods=max(138//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.868125 + 0.0003283 * anchor
    return base_signal.diff()

def f06_vdd_283_jerk_v283_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=145, w2=410, w3=302, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(410, min_periods=max(410//3, 2)).rank(pct=True)
    persistence = change.rolling(302, min_periods=max(302//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1434 * persistence + 0.0003284 * anchor
    return base_signal.diff()

def f06_vdd_284_accel_v284_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=152, w2=421, w3=315, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(152, min_periods=max(152//3, 2)).std()
    vol_slow = ret.rolling(421, min_periods=max(421//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.896875 + 0.0003285 * anchor
    return base_signal.diff()

def f06_vdd_285_jerk_v285_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=159, w2=432, w3=328, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(432, min_periods=max(432//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 159)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1586 * slope + 0.0003286 * anchor
    return base_signal.diff()

def f06_vdd_286_accel_v286_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=166, w2=443, w3=341, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(443, min_periods=max(443//3, 2)).mean()
    noise = impulse.abs().rolling(341, min_periods=max(341//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.925625 + 0.0003287 * anchor
    return base_signal.diff()

def f06_vdd_287_jerk_v287_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=173, w2=454, w3=354, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 173)
    acceleration = _rolling_slope(velocity, 454)
    curvature = _rolling_slope(acceleration, 354)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1738 * acceleration + 0.0003288 * anchor
    return base_signal.diff()

def f06_vdd_288_accel_v288_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=180, w2=465, w3=367, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(180, min_periods=max(180//3, 2)).mean(), upside.rolling(465, min_periods=max(465//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.954375 + 0.0003289 * anchor
    return base_signal.diff()

def f06_vdd_289_jerk_v289_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=187, w2=476, w3=380, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(476, min_periods=max(476//3, 2)).max()
    rebound = x - x.rolling(187, min_periods=max(187//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.189 * _rolling_slope(draw, 380) + 0.000329 * anchor
    return base_signal.diff()

def f06_vdd_290_accel_v290_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=194, w2=487, w3=393, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 194)
    baseline = trend.rolling(487, min_periods=max(487//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(393, min_periods=max(393//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.983125 + 0.0003291 * anchor
    return base_signal.diff()

def f06_vdd_291_jerk_v291_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=201, w2=498, w3=406, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 201)
    slow = _rolling_slope(x, 498)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.9975 + 0.0003292 * anchor
    return base_signal.diff()

def f06_vdd_292_accel_v292_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=208, w2=509, w3=419, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(509, min_periods=max(509//3, 2)).max()
    trough = x.rolling(208, min_periods=max(208//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.011875 + 0.0003293 * anchor
    return base_signal.diff()

def f06_vdd_293_jerk_v293_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=215, w2=17, w3=432, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(17, min_periods=max(17//3, 2)).rank(pct=True)
    persistence = change.rolling(432, min_periods=max(432//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2194 * persistence + 0.0003294 * anchor
    return base_signal.diff()

def f06_vdd_294_accel_v294_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=222, w2=28, w3=445, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(222, min_periods=max(222//3, 2)).std()
    vol_slow = ret.rolling(28, min_periods=max(28//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.040625 + 0.0003295 * anchor
    return base_signal.diff()

def f06_vdd_295_jerk_v295_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=229, w2=39, w3=458, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(39, min_periods=max(39//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 229)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2346 * slope + 0.0003296 * anchor
    return base_signal.diff()

def f06_vdd_296_accel_v296_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=236, w2=50, w3=471, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(50, min_periods=max(50//3, 2)).mean()
    noise = impulse.abs().rolling(471, min_periods=max(471//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.069375 + 0.0003297 * anchor
    return base_signal.diff()

def f06_vdd_297_jerk_v297_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=243, w2=61, w3=484, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 243)
    acceleration = _rolling_slope(velocity, 61)
    curvature = _rolling_slope(acceleration, 484)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2498 * acceleration + 0.0003298 * anchor
    return base_signal.diff()

def f06_vdd_298_accel_v298_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=250, w2=72, w3=497, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(250, min_periods=max(250//3, 2)).mean(), upside.rolling(72, min_periods=max(72//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.098125 + 0.0003299 * anchor
    return base_signal.diff()

def f06_vdd_299_jerk_v299_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=6, w2=83, w3=510, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(83, min_periods=max(83//3, 2)).max()
    rebound = x - x.rolling(6, min_periods=max(6//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.265 * _rolling_slope(draw, 510) + 0.00033 * anchor
    return base_signal.diff()

def f06_vdd_300_accel_v300_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=13, w2=94, w3=523, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 13)
    baseline = trend.rolling(94, min_periods=max(94//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(523, min_periods=max(523//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.126875 + 0.0003301 * anchor
    return base_signal.diff()
