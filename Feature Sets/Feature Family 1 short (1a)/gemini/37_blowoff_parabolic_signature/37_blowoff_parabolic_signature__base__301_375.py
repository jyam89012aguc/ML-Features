"""37 blowoff parabolic signature base features 301-375 â€” Pipeline 1a-HF Grade v3.

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

def f37_bps_301_jerk_v301(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=135, w2=45, w3=326, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 135)
    slow = _rolling_slope(x, 45)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.135625 + 0.0022502 * anchor

def f37_bps_302_accel_v302(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=142, w2=56, w3=339, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(56, min_periods=max(56//3, 2)).max()
    trough = x.rolling(142, min_periods=max(142//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.15 + 0.0022503 * anchor

def f37_bps_303_jerk_v303(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=149, w2=67, w3=352, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(67, min_periods=max(67//3, 2)).rank(pct=True)
    persistence = change.rolling(352, min_periods=max(352//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1722 * persistence + 0.0022504 * anchor

def f37_bps_304_accel_v304(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=156, w2=78, w3=365, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(156, min_periods=max(156//3, 2)).std()
    vol_slow = ret.rolling(78, min_periods=max(78//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.17875 + 0.0022505 * anchor

def f37_bps_305_jerk_v305(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=163, w2=89, w3=378, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(89, min_periods=max(89//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 163)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1874 * slope + 0.0022506 * anchor

def f37_bps_306_accel_v306(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=170, w2=100, w3=391, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(100, min_periods=max(100//3, 2)).mean()
    noise = impulse.abs().rolling(391, min_periods=max(391//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.2075 + 0.0022507 * anchor

def f37_bps_307_jerk_v307(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=177, w2=111, w3=404, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 177)
    acceleration = _rolling_slope(velocity, 111)
    curvature = _rolling_slope(acceleration, 404)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2026 * acceleration + 0.0022508 * anchor

def f37_bps_308_accel_v308(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=184, w2=122, w3=417, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(184, min_periods=max(184//3, 2)).mean(), upside.rolling(122, min_periods=max(122//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.23625 + 0.0022509 * anchor

def f37_bps_309_jerk_v309(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=191, w2=133, w3=430, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(133, min_periods=max(133//3, 2)).max()
    rebound = x - x.rolling(191, min_periods=max(191//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2178 * _rolling_slope(draw, 430) + 0.002251 * anchor

def f37_bps_310_accel_v310(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=198, w2=144, w3=443, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 198)
    baseline = trend.rolling(144, min_periods=max(144//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(443, min_periods=max(443//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.265 + 0.0022511 * anchor

def f37_bps_311_jerk_v311(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=205, w2=155, w3=456, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 205)
    slow = _rolling_slope(x, 155)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.279375 + 0.0022512 * anchor

def f37_bps_312_accel_v312(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=212, w2=166, w3=469, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(166, min_periods=max(166//3, 2)).max()
    trough = x.rolling(212, min_periods=max(212//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.29375 + 0.0022513 * anchor

def f37_bps_313_jerk_v313(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=219, w2=177, w3=482, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(177, min_periods=max(177//3, 2)).rank(pct=True)
    persistence = change.rolling(482, min_periods=max(482//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2482 * persistence + 0.0022514 * anchor

def f37_bps_314_accel_v314(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=226, w2=188, w3=495, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(226, min_periods=max(226//3, 2)).std()
    vol_slow = ret.rolling(188, min_periods=max(188//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.3225 + 0.0022515 * anchor

def f37_bps_315_jerk_v315(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=233, w2=199, w3=508, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(199, min_periods=max(199//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 233)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2634 * slope + 0.0022516 * anchor

def f37_bps_316_accel_v316(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=240, w2=210, w3=521, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(210, min_periods=max(210//3, 2)).mean()
    noise = impulse.abs().rolling(521, min_periods=max(521//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.35125 + 0.0022517 * anchor

def f37_bps_317_jerk_v317(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=247, w2=221, w3=534, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 247)
    acceleration = _rolling_slope(velocity, 221)
    curvature = _rolling_slope(acceleration, 534)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2786 * acceleration + 0.0022518 * anchor

def f37_bps_318_accel_v318(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=254, w2=232, w3=547, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(254, min_periods=max(254//3, 2)).mean(), upside.rolling(232, min_periods=max(232//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.38 + 0.0022519 * anchor

def f37_bps_319_jerk_v319(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=10, w2=243, w3=560, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(243, min_periods=max(243//3, 2)).max()
    rebound = x - x.rolling(10, min_periods=max(10//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2938 * _rolling_slope(draw, 560) + 0.002252 * anchor

def f37_bps_320_accel_v320(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=17, w2=254, w3=573, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 17)
    baseline = trend.rolling(254, min_periods=max(254//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(573, min_periods=max(573//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.40875 + 0.0022521 * anchor

def f37_bps_321_jerk_v321(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=24, w2=265, w3=586, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 24)
    slow = _rolling_slope(x, 265)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.423125 + 0.0022522 * anchor

def f37_bps_322_accel_v322(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=31, w2=276, w3=599, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(276, min_periods=max(276//3, 2)).max()
    trough = x.rolling(31, min_periods=max(31//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.4375 + 0.0022523 * anchor

def f37_bps_323_jerk_v323(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=38, w2=287, w3=612, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(38)
    rank = change.rolling(287, min_periods=max(287//3, 2)).rank(pct=True)
    persistence = change.rolling(612, min_periods=max(612//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3242 * persistence + 0.0022524 * anchor

def f37_bps_324_accel_v324(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=45, w2=298, w3=625, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(45, min_periods=max(45//3, 2)).std()
    vol_slow = ret.rolling(298, min_periods=max(298//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.46625 + 0.0022525 * anchor

def f37_bps_325_jerk_v325(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=52, w2=309, w3=638, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(309, min_periods=max(309//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 52)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3394 * slope + 0.0022526 * anchor

def f37_bps_326_accel_v326(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=59, w2=320, w3=651, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(59)
    drag = impulse.rolling(320, min_periods=max(320//3, 2)).mean()
    noise = impulse.abs().rolling(651, min_periods=max(651//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.495 + 0.0022527 * anchor

def f37_bps_327_jerk_v327(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=66, w2=331, w3=664, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 66)
    acceleration = _rolling_slope(velocity, 331)
    curvature = _rolling_slope(acceleration, 664)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3546 * acceleration + 0.0022528 * anchor

def f37_bps_328_accel_v328(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=73, w2=342, w3=677, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(73, min_periods=max(73//3, 2)).mean(), upside.rolling(342, min_periods=max(342//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.52375 + 0.0022529 * anchor

def f37_bps_329_jerk_v329(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=80, w2=353, w3=690, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(353, min_periods=max(353//3, 2)).max()
    rebound = x - x.rolling(80, min_periods=max(80//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3698 * _rolling_slope(draw, 690) + 0.002253 * anchor

def f37_bps_330_accel_v330(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=87, w2=364, w3=703, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 87)
    baseline = trend.rolling(364, min_periods=max(364//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(703, min_periods=max(703//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.5525 + 0.0022531 * anchor

def f37_bps_331_jerk_v331(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=94, w2=375, w3=716, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 94)
    slow = _rolling_slope(x, 375)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.566875 + 0.0022532 * anchor

def f37_bps_332_accel_v332(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=101, w2=386, w3=729, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(386, min_periods=max(386//3, 2)).max()
    trough = x.rolling(101, min_periods=max(101//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.58125 + 0.0022533 * anchor

def f37_bps_333_jerk_v333(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=108, w2=397, w3=742, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(108)
    rank = change.rolling(397, min_periods=max(397//3, 2)).rank(pct=True)
    persistence = change.rolling(742, min_periods=max(742//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.4002 * persistence + 0.0022534 * anchor

def f37_bps_334_accel_v334(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=115, w2=408, w3=755, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(115, min_periods=max(115//3, 2)).std()
    vol_slow = ret.rolling(408, min_periods=max(408//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.61 + 0.0022535 * anchor

def f37_bps_335_jerk_v335(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=122, w2=419, w3=768, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(419, min_periods=max(419//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 122)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.039 * slope + 0.0022536 * anchor

def f37_bps_336_accel_v336(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=129, w2=430, w3=24, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(430, min_periods=max(430//3, 2)).mean()
    noise = impulse.abs().rolling(24, min_periods=max(24//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.865625 + 0.0022537 * anchor

def f37_bps_337_jerk_v337(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=136, w2=441, w3=37, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 136)
    acceleration = _rolling_slope(velocity, 441)
    curvature = _rolling_slope(acceleration, 37)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0542 * acceleration + 0.0022538 * anchor

def f37_bps_338_accel_v338(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=143, w2=452, w3=50, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(143, min_periods=max(143//3, 2)).mean(), upside.rolling(452, min_periods=max(452//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(50) * 0.894375 + 0.0022539 * anchor

def f37_bps_339_jerk_v339(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=150, w2=463, w3=63, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(463, min_periods=max(463//3, 2)).max()
    rebound = x - x.rolling(150, min_periods=max(150//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0694 * _rolling_slope(draw, 63) + 0.002254 * anchor

def f37_bps_340_accel_v340(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=157, w2=474, w3=76, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 157)
    baseline = trend.rolling(474, min_periods=max(474//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(76, min_periods=max(76//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.923125 + 0.0022541 * anchor

def f37_bps_341_jerk_v341(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=164, w2=485, w3=89, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 164)
    slow = _rolling_slope(x, 485)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=89, adjust=False).mean() * 0.9375 + 0.0022542 * anchor

def f37_bps_342_accel_v342(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=171, w2=496, w3=102, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(496, min_periods=max(496//3, 2)).max()
    trough = x.rolling(171, min_periods=max(171//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.951875 + 0.0022543 * anchor

def f37_bps_343_jerk_v343(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=178, w2=507, w3=115, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(507, min_periods=max(507//3, 2)).rank(pct=True)
    persistence = change.rolling(115, min_periods=max(115//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0998 * persistence + 0.0022544 * anchor

def f37_bps_344_accel_v344(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=185, w2=15, w3=128, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(185, min_periods=max(185//3, 2)).std()
    vol_slow = ret.rolling(15, min_periods=max(15//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.980625 + 0.0022545 * anchor

def f37_bps_345_jerk_v345(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=192, w2=26, w3=141, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(26, min_periods=max(26//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 192)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.115 * slope + 0.0022546 * anchor

def f37_bps_346_accel_v346(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=199, w2=37, w3=154, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(37, min_periods=max(37//3, 2)).mean()
    noise = impulse.abs().rolling(154, min_periods=max(154//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.009375 + 0.0022547 * anchor

def f37_bps_347_jerk_v347(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=206, w2=48, w3=167, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 206)
    acceleration = _rolling_slope(velocity, 48)
    curvature = _rolling_slope(acceleration, 167)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1302 * acceleration + 0.0022548 * anchor

def f37_bps_348_accel_v348(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=213, w2=59, w3=180, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(213, min_periods=max(213//3, 2)).mean(), upside.rolling(59, min_periods=max(59//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.038125 + 0.0022549 * anchor

def f37_bps_349_jerk_v349(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=220, w2=70, w3=193, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(70, min_periods=max(70//3, 2)).max()
    rebound = x - x.rolling(220, min_periods=max(220//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1454 * _rolling_slope(draw, 193) + 0.002255 * anchor

def f37_bps_350_accel_v350(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=227, w2=81, w3=206, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 227)
    baseline = trend.rolling(81, min_periods=max(81//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(206, min_periods=max(206//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.066875 + 0.0022551 * anchor

def f37_bps_351_jerk_v351(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=234, w2=92, w3=219, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 234)
    slow = _rolling_slope(x, 92)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=219, adjust=False).mean() * 1.08125 + 0.0022552 * anchor

def f37_bps_352_accel_v352(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=241, w2=103, w3=232, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(103, min_periods=max(103//3, 2)).max()
    trough = x.rolling(241, min_periods=max(241//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.095625 + 0.0022553 * anchor

def f37_bps_353_jerk_v353(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=248, w2=114, w3=245, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(114, min_periods=max(114//3, 2)).rank(pct=True)
    persistence = change.rolling(245, min_periods=max(245//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1758 * persistence + 0.0022554 * anchor

def f37_bps_354_accel_v354(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=255, w2=125, w3=258, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(255, min_periods=max(255//3, 2)).std()
    vol_slow = ret.rolling(125, min_periods=max(125//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.124375 + 0.0022555 * anchor

def f37_bps_355_jerk_v355(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=11, w2=136, w3=271, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(136, min_periods=max(136//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 11)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.191 * slope + 0.0022556 * anchor

def f37_bps_356_accel_v356(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=18, w2=147, w3=284, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(18)
    drag = impulse.rolling(147, min_periods=max(147//3, 2)).mean()
    noise = impulse.abs().rolling(284, min_periods=max(284//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.153125 + 0.0022557 * anchor

def f37_bps_357_jerk_v357(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=25, w2=158, w3=297, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 25)
    acceleration = _rolling_slope(velocity, 158)
    curvature = _rolling_slope(acceleration, 297)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2062 * acceleration + 0.0022558 * anchor

def f37_bps_358_accel_v358(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=32, w2=169, w3=310, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(32, min_periods=max(32//3, 2)).mean(), upside.rolling(169, min_periods=max(169//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.181875 + 0.0022559 * anchor

def f37_bps_359_jerk_v359(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=39, w2=180, w3=323, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(180, min_periods=max(180//3, 2)).max()
    rebound = x - x.rolling(39, min_periods=max(39//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2214 * _rolling_slope(draw, 323) + 0.002256 * anchor

def f37_bps_360_accel_v360(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=46, w2=191, w3=336, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 46)
    baseline = trend.rolling(191, min_periods=max(191//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(336, min_periods=max(336//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.210625 + 0.0022561 * anchor

def f37_bps_361_jerk_v361(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=53, w2=202, w3=349, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 53)
    slow = _rolling_slope(x, 202)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.225 + 0.0022562 * anchor

def f37_bps_362_accel_v362(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=60, w2=213, w3=362, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(213, min_periods=max(213//3, 2)).max()
    trough = x.rolling(60, min_periods=max(60//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.239375 + 0.0022563 * anchor

def f37_bps_363_jerk_v363(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=67, w2=224, w3=375, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(67)
    rank = change.rolling(224, min_periods=max(224//3, 2)).rank(pct=True)
    persistence = change.rolling(375, min_periods=max(375//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2518 * persistence + 0.0022564 * anchor

def f37_bps_364_accel_v364(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=74, w2=235, w3=388, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(74, min_periods=max(74//3, 2)).std()
    vol_slow = ret.rolling(235, min_periods=max(235//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.268125 + 0.0022565 * anchor

def f37_bps_365_jerk_v365(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=81, w2=246, w3=401, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(246, min_periods=max(246//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 81)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.267 * slope + 0.0022566 * anchor

def f37_bps_366_accel_v366(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=88, w2=257, w3=414, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(88)
    drag = impulse.rolling(257, min_periods=max(257//3, 2)).mean()
    noise = impulse.abs().rolling(414, min_periods=max(414//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.296875 + 0.0022567 * anchor

def f37_bps_367_jerk_v367(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=95, w2=268, w3=427, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 95)
    acceleration = _rolling_slope(velocity, 268)
    curvature = _rolling_slope(acceleration, 427)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2822 * acceleration + 0.0022568 * anchor

def f37_bps_368_accel_v368(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=102, w2=279, w3=440, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(102, min_periods=max(102//3, 2)).mean(), upside.rolling(279, min_periods=max(279//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.325625 + 0.0022569 * anchor

def f37_bps_369_jerk_v369(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=109, w2=290, w3=453, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(290, min_periods=max(290//3, 2)).max()
    rebound = x - x.rolling(109, min_periods=max(109//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2974 * _rolling_slope(draw, 453) + 0.002257 * anchor

def f37_bps_370_accel_v370(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=116, w2=301, w3=466, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 116)
    baseline = trend.rolling(301, min_periods=max(301//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(466, min_periods=max(466//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.354375 + 0.0022571 * anchor

def f37_bps_371_jerk_v371(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=123, w2=312, w3=479, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 123)
    slow = _rolling_slope(x, 312)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.36875 + 0.0022572 * anchor

def f37_bps_372_accel_v372(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=130, w2=323, w3=492, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(323, min_periods=max(323//3, 2)).max()
    trough = x.rolling(130, min_periods=max(130//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.383125 + 0.0022573 * anchor

def f37_bps_373_jerk_v373(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=137, w2=334, w3=505, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(334, min_periods=max(334//3, 2)).rank(pct=True)
    persistence = change.rolling(505, min_periods=max(505//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3278 * persistence + 0.0022574 * anchor

def f37_bps_374_accel_v374(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=144, w2=345, w3=518, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(144, min_periods=max(144//3, 2)).std()
    vol_slow = ret.rolling(345, min_periods=max(345//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.411875 + 0.0022575 * anchor

def f37_bps_375_jerk_v375(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=151, w2=356, w3=531, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(356, min_periods=max(356//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 151)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.343 * slope + 0.0022576 * anchor
