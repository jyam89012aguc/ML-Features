"""06 volume distribution dryup d1 first derivative features 301-375 â€” Pipeline 1a-HF Grade v3.

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

def f06_vdd_301_jerk_v301_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=20, w2=105, w3=536, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 20)
    slow = _rolling_slope(x, 105)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.14125 + 0.0003302 * anchor
    return base_signal.diff()

def f06_vdd_302_accel_v302_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=27, w2=116, w3=549, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(116, min_periods=max(116//3, 2)).max()
    trough = x.rolling(27, min_periods=max(27//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.155625 + 0.0003303 * anchor
    return base_signal.diff()

def f06_vdd_303_jerk_v303_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=34, w2=127, w3=562, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(34)
    rank = change.rolling(127, min_periods=max(127//3, 2)).rank(pct=True)
    persistence = change.rolling(562, min_periods=max(562//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2954 * persistence + 0.0003304 * anchor
    return base_signal.diff()

def f06_vdd_304_accel_v304_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=41, w2=138, w3=575, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(41, min_periods=max(41//3, 2)).std()
    vol_slow = ret.rolling(138, min_periods=max(138//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.184375 + 0.0003305 * anchor
    return base_signal.diff()

def f06_vdd_305_jerk_v305_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=48, w2=149, w3=588, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(149, min_periods=max(149//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 48)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3106 * slope + 0.0003306 * anchor
    return base_signal.diff()

def f06_vdd_306_accel_v306_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=55, w2=160, w3=601, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(55)
    drag = impulse.rolling(160, min_periods=max(160//3, 2)).mean()
    noise = impulse.abs().rolling(601, min_periods=max(601//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.213125 + 0.0003307 * anchor
    return base_signal.diff()

def f06_vdd_307_jerk_v307_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=62, w2=171, w3=614, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 62)
    acceleration = _rolling_slope(velocity, 171)
    curvature = _rolling_slope(acceleration, 614)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3258 * acceleration + 0.0003308 * anchor
    return base_signal.diff()

def f06_vdd_308_accel_v308_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=69, w2=182, w3=627, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(69, min_periods=max(69//3, 2)).mean(), upside.rolling(182, min_periods=max(182//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.241875 + 0.0003309 * anchor
    return base_signal.diff()

def f06_vdd_309_jerk_v309_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=76, w2=193, w3=640, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(193, min_periods=max(193//3, 2)).max()
    rebound = x - x.rolling(76, min_periods=max(76//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.341 * _rolling_slope(draw, 640) + 0.000331 * anchor
    return base_signal.diff()

def f06_vdd_310_accel_v310_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=83, w2=204, w3=653, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 83)
    baseline = trend.rolling(204, min_periods=max(204//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(653, min_periods=max(653//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.270625 + 0.0003311 * anchor
    return base_signal.diff()

def f06_vdd_311_jerk_v311_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=90, w2=215, w3=666, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 90)
    slow = _rolling_slope(x, 215)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.285 + 0.0003312 * anchor
    return base_signal.diff()

def f06_vdd_312_accel_v312_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=97, w2=226, w3=679, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(226, min_periods=max(226//3, 2)).max()
    trough = x.rolling(97, min_periods=max(97//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.299375 + 0.0003313 * anchor
    return base_signal.diff()

def f06_vdd_313_jerk_v313_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=104, w2=237, w3=692, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(104)
    rank = change.rolling(237, min_periods=max(237//3, 2)).rank(pct=True)
    persistence = change.rolling(692, min_periods=max(692//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3714 * persistence + 0.0003314 * anchor
    return base_signal.diff()

def f06_vdd_314_accel_v314_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=111, w2=248, w3=705, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(111, min_periods=max(111//3, 2)).std()
    vol_slow = ret.rolling(248, min_periods=max(248//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.328125 + 0.0003315 * anchor
    return base_signal.diff()

def f06_vdd_315_jerk_v315_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=118, w2=259, w3=718, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(259, min_periods=max(259//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 118)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3866 * slope + 0.0003316 * anchor
    return base_signal.diff()

def f06_vdd_316_accel_v316_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=125, w2=270, w3=731, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(125)
    drag = impulse.rolling(270, min_periods=max(270//3, 2)).mean()
    noise = impulse.abs().rolling(731, min_periods=max(731//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.356875 + 0.0003317 * anchor
    return base_signal.diff()

def f06_vdd_317_jerk_v317_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=132, w2=281, w3=744, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 132)
    acceleration = _rolling_slope(velocity, 281)
    curvature = _rolling_slope(acceleration, 744)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.4018 * acceleration + 0.0003318 * anchor
    return base_signal.diff()

def f06_vdd_318_accel_v318_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=139, w2=292, w3=757, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(139, min_periods=max(139//3, 2)).mean(), upside.rolling(292, min_periods=max(292//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.385625 + 0.0003319 * anchor
    return base_signal.diff()

def f06_vdd_319_jerk_v319_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=146, w2=303, w3=770, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(303, min_periods=max(303//3, 2)).max()
    rebound = x - x.rolling(146, min_periods=max(146//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0406 * _rolling_slope(draw, 770) + 0.000332 * anchor
    return base_signal.diff()

def f06_vdd_320_accel_v320_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=153, w2=314, w3=26, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 153)
    baseline = trend.rolling(314, min_periods=max(314//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(26, min_periods=max(26//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.414375 + 0.0003321 * anchor
    return base_signal.diff()

def f06_vdd_321_jerk_v321_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=160, w2=325, w3=39, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 160)
    slow = _rolling_slope(x, 325)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=39, adjust=False).mean() * 1.42875 + 0.0003322 * anchor
    return base_signal.diff()

def f06_vdd_322_accel_v322_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=167, w2=336, w3=52, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(336, min_periods=max(336//3, 2)).max()
    trough = x.rolling(167, min_periods=max(167//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.443125 + 0.0003323 * anchor
    return base_signal.diff()

def f06_vdd_323_jerk_v323_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=174, w2=347, w3=65, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(347, min_periods=max(347//3, 2)).rank(pct=True)
    persistence = change.rolling(65, min_periods=max(65//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.071 * persistence + 0.0003324 * anchor
    return base_signal.diff()

def f06_vdd_324_accel_v324_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=181, w2=358, w3=78, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(181, min_periods=max(181//3, 2)).std()
    vol_slow = ret.rolling(358, min_periods=max(358//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.471875 + 0.0003325 * anchor
    return base_signal.diff()

def f06_vdd_325_jerk_v325_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=188, w2=369, w3=91, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(369, min_periods=max(369//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 188)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0862 * slope + 0.0003326 * anchor
    return base_signal.diff()

def f06_vdd_326_accel_v326_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=195, w2=380, w3=104, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(380, min_periods=max(380//3, 2)).mean()
    noise = impulse.abs().rolling(104, min_periods=max(104//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.500625 + 0.0003327 * anchor
    return base_signal.diff()

def f06_vdd_327_jerk_v327_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=202, w2=391, w3=117, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 202)
    acceleration = _rolling_slope(velocity, 391)
    curvature = _rolling_slope(acceleration, 117)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1014 * acceleration + 0.0003328 * anchor
    return base_signal.diff()

def f06_vdd_328_accel_v328_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=209, w2=402, w3=130, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(209, min_periods=max(209//3, 2)).mean(), upside.rolling(402, min_periods=max(402//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.529375 + 0.0003329 * anchor
    return base_signal.diff()

def f06_vdd_329_jerk_v329_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=216, w2=413, w3=143, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(413, min_periods=max(413//3, 2)).max()
    rebound = x - x.rolling(216, min_periods=max(216//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1166 * _rolling_slope(draw, 143) + 0.000333 * anchor
    return base_signal.diff()

def f06_vdd_330_accel_v330_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=223, w2=424, w3=156, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 223)
    baseline = trend.rolling(424, min_periods=max(424//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(156, min_periods=max(156//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.558125 + 0.0003331 * anchor
    return base_signal.diff()

def f06_vdd_331_jerk_v331_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=230, w2=435, w3=169, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 230)
    slow = _rolling_slope(x, 435)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=169, adjust=False).mean() * 1.5725 + 0.0003332 * anchor
    return base_signal.diff()

def f06_vdd_332_accel_v332_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=237, w2=446, w3=182, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(446, min_periods=max(446//3, 2)).max()
    trough = x.rolling(237, min_periods=max(237//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.586875 + 0.0003333 * anchor
    return base_signal.diff()

def f06_vdd_333_jerk_v333_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=244, w2=457, w3=195, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(457, min_periods=max(457//3, 2)).rank(pct=True)
    persistence = change.rolling(195, min_periods=max(195//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.147 * persistence + 0.0003334 * anchor
    return base_signal.diff()

def f06_vdd_334_accel_v334_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=251, w2=468, w3=208, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(251, min_periods=max(251//3, 2)).std()
    vol_slow = ret.rolling(468, min_periods=max(468//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.615625 + 0.0003335 * anchor
    return base_signal.diff()

def f06_vdd_335_jerk_v335_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=7, w2=479, w3=221, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(479, min_periods=max(479//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 7)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1622 * slope + 0.0003336 * anchor
    return base_signal.diff()

def f06_vdd_336_accel_v336_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=14, w2=490, w3=234, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(14)
    drag = impulse.rolling(490, min_periods=max(490//3, 2)).mean()
    noise = impulse.abs().rolling(234, min_periods=max(234//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.87125 + 0.0003337 * anchor
    return base_signal.diff()

def f06_vdd_337_jerk_v337_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=21, w2=501, w3=247, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 21)
    acceleration = _rolling_slope(velocity, 501)
    curvature = _rolling_slope(acceleration, 247)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1774 * acceleration + 0.0003338 * anchor
    return base_signal.diff()

def f06_vdd_338_accel_v338_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=28, w2=512, w3=260, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(28, min_periods=max(28//3, 2)).mean(), upside.rolling(512, min_periods=max(512//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.9 + 0.0003339 * anchor
    return base_signal.diff()

def f06_vdd_339_jerk_v339_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=35, w2=20, w3=273, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(20, min_periods=max(20//3, 2)).max()
    rebound = x - x.rolling(35, min_periods=max(35//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1926 * _rolling_slope(draw, 273) + 0.000334 * anchor
    return base_signal.diff()

def f06_vdd_340_accel_v340_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=42, w2=31, w3=286, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 42)
    baseline = trend.rolling(31, min_periods=max(31//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(286, min_periods=max(286//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.92875 + 0.0003341 * anchor
    return base_signal.diff()

def f06_vdd_341_jerk_v341_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=49, w2=42, w3=299, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 49)
    slow = _rolling_slope(x, 42)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=299, adjust=False).mean() * 0.943125 + 0.0003342 * anchor
    return base_signal.diff()

def f06_vdd_342_accel_v342_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=56, w2=53, w3=312, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(53, min_periods=max(53//3, 2)).max()
    trough = x.rolling(56, min_periods=max(56//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.9575 + 0.0003343 * anchor
    return base_signal.diff()

def f06_vdd_343_jerk_v343_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=63, w2=64, w3=325, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(63)
    rank = change.rolling(64, min_periods=max(64//3, 2)).rank(pct=True)
    persistence = change.rolling(325, min_periods=max(325//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.223 * persistence + 0.0003344 * anchor
    return base_signal.diff()

def f06_vdd_344_accel_v344_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=70, w2=75, w3=338, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(70, min_periods=max(70//3, 2)).std()
    vol_slow = ret.rolling(75, min_periods=max(75//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.98625 + 0.0003345 * anchor
    return base_signal.diff()

def f06_vdd_345_jerk_v345_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=77, w2=86, w3=351, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(86, min_periods=max(86//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 77)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2382 * slope + 0.0003346 * anchor
    return base_signal.diff()

def f06_vdd_346_accel_v346_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=84, w2=97, w3=364, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(84)
    drag = impulse.rolling(97, min_periods=max(97//3, 2)).mean()
    noise = impulse.abs().rolling(364, min_periods=max(364//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.015 + 0.0003347 * anchor
    return base_signal.diff()

def f06_vdd_347_jerk_v347_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=91, w2=108, w3=377, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 91)
    acceleration = _rolling_slope(velocity, 108)
    curvature = _rolling_slope(acceleration, 377)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2534 * acceleration + 0.0003348 * anchor
    return base_signal.diff()

def f06_vdd_348_accel_v348_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=98, w2=119, w3=390, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(98, min_periods=max(98//3, 2)).mean(), upside.rolling(119, min_periods=max(119//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.04375 + 0.0003349 * anchor
    return base_signal.diff()

def f06_vdd_349_jerk_v349_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=105, w2=130, w3=403, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(130, min_periods=max(130//3, 2)).max()
    rebound = x - x.rolling(105, min_periods=max(105//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2686 * _rolling_slope(draw, 403) + 0.000335 * anchor
    return base_signal.diff()

def f06_vdd_350_accel_v350_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=112, w2=141, w3=416, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 112)
    baseline = trend.rolling(141, min_periods=max(141//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(416, min_periods=max(416//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.0725 + 0.0003351 * anchor
    return base_signal.diff()

def f06_vdd_351_jerk_v351_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=119, w2=152, w3=429, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 119)
    slow = _rolling_slope(x, 152)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.086875 + 0.0003352 * anchor
    return base_signal.diff()

def f06_vdd_352_accel_v352_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=126, w2=163, w3=442, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(163, min_periods=max(163//3, 2)).max()
    trough = x.rolling(126, min_periods=max(126//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.10125 + 0.0003353 * anchor
    return base_signal.diff()

def f06_vdd_353_jerk_v353_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=133, w2=174, w3=455, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(174, min_periods=max(174//3, 2)).rank(pct=True)
    persistence = change.rolling(455, min_periods=max(455//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.299 * persistence + 0.0003354 * anchor
    return base_signal.diff()

def f06_vdd_354_accel_v354_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=140, w2=185, w3=468, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(140, min_periods=max(140//3, 2)).std()
    vol_slow = ret.rolling(185, min_periods=max(185//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.13 + 0.0003355 * anchor
    return base_signal.diff()

def f06_vdd_355_jerk_v355_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=147, w2=196, w3=481, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(196, min_periods=max(196//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 147)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3142 * slope + 0.0003356 * anchor
    return base_signal.diff()

def f06_vdd_356_accel_v356_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=154, w2=207, w3=494, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(207, min_periods=max(207//3, 2)).mean()
    noise = impulse.abs().rolling(494, min_periods=max(494//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.15875 + 0.0003357 * anchor
    return base_signal.diff()

def f06_vdd_357_jerk_v357_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=161, w2=218, w3=507, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 161)
    acceleration = _rolling_slope(velocity, 218)
    curvature = _rolling_slope(acceleration, 507)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3294 * acceleration + 0.0003358 * anchor
    return base_signal.diff()

def f06_vdd_358_accel_v358_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=168, w2=229, w3=520, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(168, min_periods=max(168//3, 2)).mean(), upside.rolling(229, min_periods=max(229//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.1875 + 0.0003359 * anchor
    return base_signal.diff()

def f06_vdd_359_jerk_v359_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=175, w2=240, w3=533, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(240, min_periods=max(240//3, 2)).max()
    rebound = x - x.rolling(175, min_periods=max(175//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3446 * _rolling_slope(draw, 533) + 0.000336 * anchor
    return base_signal.diff()

def f06_vdd_360_accel_v360_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=182, w2=251, w3=546, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 182)
    baseline = trend.rolling(251, min_periods=max(251//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(546, min_periods=max(546//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.21625 + 0.0003361 * anchor
    return base_signal.diff()

def f06_vdd_361_jerk_v361_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=189, w2=262, w3=559, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 189)
    slow = _rolling_slope(x, 262)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.230625 + 0.0003362 * anchor
    return base_signal.diff()

def f06_vdd_362_accel_v362_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=196, w2=273, w3=572, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(273, min_periods=max(273//3, 2)).max()
    trough = x.rolling(196, min_periods=max(196//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.245 + 0.0003363 * anchor
    return base_signal.diff()

def f06_vdd_363_jerk_v363_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=203, w2=284, w3=585, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(284, min_periods=max(284//3, 2)).rank(pct=True)
    persistence = change.rolling(585, min_periods=max(585//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.375 * persistence + 0.0003364 * anchor
    return base_signal.diff()

def f06_vdd_364_accel_v364_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=210, w2=295, w3=598, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(210, min_periods=max(210//3, 2)).std()
    vol_slow = ret.rolling(295, min_periods=max(295//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.27375 + 0.0003365 * anchor
    return base_signal.diff()

def f06_vdd_365_jerk_v365_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=217, w2=306, w3=611, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(306, min_periods=max(306//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 217)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3902 * slope + 0.0003366 * anchor
    return base_signal.diff()

def f06_vdd_366_accel_v366_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=224, w2=317, w3=624, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(317, min_periods=max(317//3, 2)).mean()
    noise = impulse.abs().rolling(624, min_periods=max(624//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.3025 + 0.0003367 * anchor
    return base_signal.diff()

def f06_vdd_367_jerk_v367_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=231, w2=328, w3=637, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 231)
    acceleration = _rolling_slope(velocity, 328)
    curvature = _rolling_slope(acceleration, 637)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.4054 * acceleration + 0.0003368 * anchor
    return base_signal.diff()

def f06_vdd_368_accel_v368_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=238, w2=339, w3=650, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(238, min_periods=max(238//3, 2)).mean(), upside.rolling(339, min_periods=max(339//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.33125 + 0.0003369 * anchor
    return base_signal.diff()

def f06_vdd_369_jerk_v369_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=245, w2=350, w3=663, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(350, min_periods=max(350//3, 2)).max()
    rebound = x - x.rolling(245, min_periods=max(245//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0442 * _rolling_slope(draw, 663) + 0.000337 * anchor
    return base_signal.diff()

def f06_vdd_370_accel_v370_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=252, w2=361, w3=676, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 252)
    baseline = trend.rolling(361, min_periods=max(361//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(676, min_periods=max(676//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.36 + 0.0003371 * anchor
    return base_signal.diff()

def f06_vdd_371_jerk_v371_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=8, w2=372, w3=689, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 8)
    slow = _rolling_slope(x, 372)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.374375 + 0.0003372 * anchor
    return base_signal.diff()

def f06_vdd_372_accel_v372_d1(close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=15, w2=383, w3=702, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(383, min_periods=max(383//3, 2)).max()
    trough = x.rolling(15, min_periods=max(15//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.38875 + 0.0003373 * anchor
    return base_signal.diff()

def f06_vdd_373_jerk_v373_d1(high: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=22, w2=394, w3=715, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(22)
    rank = change.rolling(394, min_periods=max(394//3, 2)).rank(pct=True)
    persistence = change.rolling(715, min_periods=max(715//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0746 * persistence + 0.0003374 * anchor
    return base_signal.diff()

def f06_vdd_374_accel_v374_d1(low: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accel replacement signal (w1=29, w2=405, w3=728, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(29, min_periods=max(29//3, 2)).std()
    vol_slow = ret.rolling(405, min_periods=max(405//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.4175 + 0.0003375 * anchor
    return base_signal.diff()

def f06_vdd_375_jerk_v375_d1(volume: pd.Series) -> pd.Series:
    """First derivative of de-duplicated jerk replacement signal (w1=36, w2=416, w3=741, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(416, min_periods=max(416//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 36)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0898 * slope + 0.0003376 * anchor
    return base_signal.diff()
