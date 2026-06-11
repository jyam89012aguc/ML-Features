"""05 volume blowoff at peak base features 301-375 â€” Pipeline 1a-HF Grade v3.

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

def f05_vbp_301_jerk_v301(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=87, w2=44, w3=306, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 87)
    slow = _rolling_slope(x, 44)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.020625 + 0.0002702 * anchor

def f05_vbp_302_accel_v302(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=94, w2=55, w3=319, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(55, min_periods=max(55//3, 2)).max()
    trough = x.rolling(94, min_periods=max(94//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.035 + 0.0002703 * anchor

def f05_vbp_303_jerk_v303(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=101, w2=66, w3=332, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(101)
    rank = change.rolling(66, min_periods=max(66//3, 2)).rank(pct=True)
    persistence = change.rolling(332, min_periods=max(332//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2522 * persistence + 0.0002704 * anchor

def f05_vbp_304_accel_v304(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=108, w2=77, w3=345, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(108, min_periods=max(108//3, 2)).std()
    vol_slow = ret.rolling(77, min_periods=max(77//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.06375 + 0.0002705 * anchor

def f05_vbp_305_jerk_v305(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=115, w2=88, w3=358, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(88, min_periods=max(88//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 115)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2674 * slope + 0.0002706 * anchor

def f05_vbp_306_accel_v306(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=122, w2=99, w3=371, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(122)
    drag = impulse.rolling(99, min_periods=max(99//3, 2)).mean()
    noise = impulse.abs().rolling(371, min_periods=max(371//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.0925 + 0.0002707 * anchor

def f05_vbp_307_jerk_v307(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=129, w2=110, w3=384, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 129)
    acceleration = _rolling_slope(velocity, 110)
    curvature = _rolling_slope(acceleration, 384)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2826 * acceleration + 0.0002708 * anchor

def f05_vbp_308_accel_v308(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=136, w2=121, w3=397, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(136, min_periods=max(136//3, 2)).mean(), upside.rolling(121, min_periods=max(121//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.12125 + 0.0002709 * anchor

def f05_vbp_309_jerk_v309(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=143, w2=132, w3=410, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(132, min_periods=max(132//3, 2)).max()
    rebound = x - x.rolling(143, min_periods=max(143//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2978 * _rolling_slope(draw, 410) + 0.000271 * anchor

def f05_vbp_310_accel_v310(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=150, w2=143, w3=423, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 150)
    baseline = trend.rolling(143, min_periods=max(143//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(423, min_periods=max(423//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.15 + 0.0002711 * anchor

def f05_vbp_311_jerk_v311(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=157, w2=154, w3=436, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 157)
    slow = _rolling_slope(x, 154)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.164375 + 0.0002712 * anchor

def f05_vbp_312_accel_v312(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=164, w2=165, w3=449, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(165, min_periods=max(165//3, 2)).max()
    trough = x.rolling(164, min_periods=max(164//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.17875 + 0.0002713 * anchor

def f05_vbp_313_jerk_v313(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=171, w2=176, w3=462, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(176, min_periods=max(176//3, 2)).rank(pct=True)
    persistence = change.rolling(462, min_periods=max(462//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3282 * persistence + 0.0002714 * anchor

def f05_vbp_314_accel_v314(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=178, w2=187, w3=475, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(178, min_periods=max(178//3, 2)).std()
    vol_slow = ret.rolling(187, min_periods=max(187//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.2075 + 0.0002715 * anchor

def f05_vbp_315_jerk_v315(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=185, w2=198, w3=488, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(198, min_periods=max(198//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 185)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3434 * slope + 0.0002716 * anchor

def f05_vbp_316_accel_v316(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=192, w2=209, w3=501, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(209, min_periods=max(209//3, 2)).mean()
    noise = impulse.abs().rolling(501, min_periods=max(501//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.23625 + 0.0002717 * anchor

def f05_vbp_317_jerk_v317(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=199, w2=220, w3=514, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 199)
    acceleration = _rolling_slope(velocity, 220)
    curvature = _rolling_slope(acceleration, 514)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3586 * acceleration + 0.0002718 * anchor

def f05_vbp_318_accel_v318(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=206, w2=231, w3=527, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(206, min_periods=max(206//3, 2)).mean(), upside.rolling(231, min_periods=max(231//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.265 + 0.0002719 * anchor

def f05_vbp_319_jerk_v319(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=213, w2=242, w3=540, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(242, min_periods=max(242//3, 2)).max()
    rebound = x - x.rolling(213, min_periods=max(213//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3738 * _rolling_slope(draw, 540) + 0.000272 * anchor

def f05_vbp_320_accel_v320(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=220, w2=253, w3=553, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 220)
    baseline = trend.rolling(253, min_periods=max(253//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(553, min_periods=max(553//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.29375 + 0.0002721 * anchor

def f05_vbp_321_jerk_v321(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=227, w2=264, w3=566, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 227)
    slow = _rolling_slope(x, 264)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.308125 + 0.0002722 * anchor

def f05_vbp_322_accel_v322(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=234, w2=275, w3=579, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(275, min_periods=max(275//3, 2)).max()
    trough = x.rolling(234, min_periods=max(234//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.3225 + 0.0002723 * anchor

def f05_vbp_323_jerk_v323(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=241, w2=286, w3=592, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(286, min_periods=max(286//3, 2)).rank(pct=True)
    persistence = change.rolling(592, min_periods=max(592//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.4042 * persistence + 0.0002724 * anchor

def f05_vbp_324_accel_v324(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=248, w2=297, w3=605, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(248, min_periods=max(248//3, 2)).std()
    vol_slow = ret.rolling(297, min_periods=max(297//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.35125 + 0.0002725 * anchor

def f05_vbp_325_jerk_v325(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=255, w2=308, w3=618, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(308, min_periods=max(308//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 255)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.043 * slope + 0.0002726 * anchor

def f05_vbp_326_accel_v326(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=11, w2=319, w3=631, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(11)
    drag = impulse.rolling(319, min_periods=max(319//3, 2)).mean()
    noise = impulse.abs().rolling(631, min_periods=max(631//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.38 + 0.0002727 * anchor

def f05_vbp_327_jerk_v327(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=18, w2=330, w3=644, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 18)
    acceleration = _rolling_slope(velocity, 330)
    curvature = _rolling_slope(acceleration, 644)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0582 * acceleration + 0.0002728 * anchor

def f05_vbp_328_accel_v328(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=25, w2=341, w3=657, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(25, min_periods=max(25//3, 2)).mean(), upside.rolling(341, min_periods=max(341//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.40875 + 0.0002729 * anchor

def f05_vbp_329_jerk_v329(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=32, w2=352, w3=670, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(352, min_periods=max(352//3, 2)).max()
    rebound = x - x.rolling(32, min_periods=max(32//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0734 * _rolling_slope(draw, 670) + 0.000273 * anchor

def f05_vbp_330_accel_v330(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=39, w2=363, w3=683, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 39)
    baseline = trend.rolling(363, min_periods=max(363//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(683, min_periods=max(683//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.4375 + 0.0002731 * anchor

def f05_vbp_331_jerk_v331(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=46, w2=374, w3=696, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 46)
    slow = _rolling_slope(x, 374)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.451875 + 0.0002732 * anchor

def f05_vbp_332_accel_v332(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=53, w2=385, w3=709, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(385, min_periods=max(385//3, 2)).max()
    trough = x.rolling(53, min_periods=max(53//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.46625 + 0.0002733 * anchor

def f05_vbp_333_jerk_v333(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=60, w2=396, w3=722, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(60)
    rank = change.rolling(396, min_periods=max(396//3, 2)).rank(pct=True)
    persistence = change.rolling(722, min_periods=max(722//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1038 * persistence + 0.0002734 * anchor

def f05_vbp_334_accel_v334(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=67, w2=407, w3=735, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(67, min_periods=max(67//3, 2)).std()
    vol_slow = ret.rolling(407, min_periods=max(407//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.495 + 0.0002735 * anchor

def f05_vbp_335_jerk_v335(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=74, w2=418, w3=748, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(418, min_periods=max(418//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 74)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.119 * slope + 0.0002736 * anchor

def f05_vbp_336_accel_v336(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=81, w2=429, w3=761, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(81)
    drag = impulse.rolling(429, min_periods=max(429//3, 2)).mean()
    noise = impulse.abs().rolling(761, min_periods=max(761//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.52375 + 0.0002737 * anchor

def f05_vbp_337_jerk_v337(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=88, w2=440, w3=17, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 88)
    acceleration = _rolling_slope(velocity, 440)
    curvature = _rolling_slope(acceleration, 17)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1342 * acceleration + 0.0002738 * anchor

def f05_vbp_338_accel_v338(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=95, w2=451, w3=30, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(95, min_periods=max(95//3, 2)).mean(), upside.rolling(451, min_periods=max(451//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(30) * 1.5525 + 0.0002739 * anchor

def f05_vbp_339_jerk_v339(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=102, w2=462, w3=43, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(462, min_periods=max(462//3, 2)).max()
    rebound = x - x.rolling(102, min_periods=max(102//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1494 * _rolling_slope(draw, 43) + 0.000274 * anchor

def f05_vbp_340_accel_v340(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=109, w2=473, w3=56, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 109)
    baseline = trend.rolling(473, min_periods=max(473//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(56, min_periods=max(56//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.58125 + 0.0002741 * anchor

def f05_vbp_341_jerk_v341(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=116, w2=484, w3=69, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 116)
    slow = _rolling_slope(x, 484)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=69, adjust=False).mean() * 1.595625 + 0.0002742 * anchor

def f05_vbp_342_accel_v342(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=123, w2=495, w3=82, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(495, min_periods=max(495//3, 2)).max()
    trough = x.rolling(123, min_periods=max(123//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.61 + 0.0002743 * anchor

def f05_vbp_343_jerk_v343(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=130, w2=506, w3=95, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(506, min_periods=max(506//3, 2)).rank(pct=True)
    persistence = change.rolling(95, min_periods=max(95//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1798 * persistence + 0.0002744 * anchor

def f05_vbp_344_accel_v344(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=137, w2=14, w3=108, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(137, min_periods=max(137//3, 2)).std()
    vol_slow = ret.rolling(14, min_periods=max(14//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.865625 + 0.0002745 * anchor

def f05_vbp_345_jerk_v345(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=144, w2=25, w3=121, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(25, min_periods=max(25//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 144)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.195 * slope + 0.0002746 * anchor

def f05_vbp_346_accel_v346(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=151, w2=36, w3=134, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(36, min_periods=max(36//3, 2)).mean()
    noise = impulse.abs().rolling(134, min_periods=max(134//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.894375 + 0.0002747 * anchor

def f05_vbp_347_jerk_v347(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=158, w2=47, w3=147, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 158)
    acceleration = _rolling_slope(velocity, 47)
    curvature = _rolling_slope(acceleration, 147)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2102 * acceleration + 0.0002748 * anchor

def f05_vbp_348_accel_v348(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=165, w2=58, w3=160, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(165, min_periods=max(165//3, 2)).mean(), upside.rolling(58, min_periods=max(58//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.923125 + 0.0002749 * anchor

def f05_vbp_349_jerk_v349(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=172, w2=69, w3=173, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(69, min_periods=max(69//3, 2)).max()
    rebound = x - x.rolling(172, min_periods=max(172//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2254 * _rolling_slope(draw, 173) + 0.000275 * anchor

def f05_vbp_350_accel_v350(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=179, w2=80, w3=186, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 179)
    baseline = trend.rolling(80, min_periods=max(80//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(186, min_periods=max(186//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.951875 + 0.0002751 * anchor

def f05_vbp_351_jerk_v351(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=186, w2=91, w3=199, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 186)
    slow = _rolling_slope(x, 91)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=199, adjust=False).mean() * 0.96625 + 0.0002752 * anchor

def f05_vbp_352_accel_v352(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=193, w2=102, w3=212, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(102, min_periods=max(102//3, 2)).max()
    trough = x.rolling(193, min_periods=max(193//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.980625 + 0.0002753 * anchor

def f05_vbp_353_jerk_v353(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=200, w2=113, w3=225, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(113, min_periods=max(113//3, 2)).rank(pct=True)
    persistence = change.rolling(225, min_periods=max(225//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2558 * persistence + 0.0002754 * anchor

def f05_vbp_354_accel_v354(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=207, w2=124, w3=238, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(207, min_periods=max(207//3, 2)).std()
    vol_slow = ret.rolling(124, min_periods=max(124//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.009375 + 0.0002755 * anchor

def f05_vbp_355_jerk_v355(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=214, w2=135, w3=251, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(135, min_periods=max(135//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 214)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.271 * slope + 0.0002756 * anchor

def f05_vbp_356_accel_v356(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=221, w2=146, w3=264, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(146, min_periods=max(146//3, 2)).mean()
    noise = impulse.abs().rolling(264, min_periods=max(264//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.038125 + 0.0002757 * anchor

def f05_vbp_357_jerk_v357(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=228, w2=157, w3=277, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 228)
    acceleration = _rolling_slope(velocity, 157)
    curvature = _rolling_slope(acceleration, 277)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2862 * acceleration + 0.0002758 * anchor

def f05_vbp_358_accel_v358(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=235, w2=168, w3=290, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(235, min_periods=max(235//3, 2)).mean(), upside.rolling(168, min_periods=max(168//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.066875 + 0.0002759 * anchor

def f05_vbp_359_jerk_v359(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=242, w2=179, w3=303, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(179, min_periods=max(179//3, 2)).max()
    rebound = x - x.rolling(242, min_periods=max(242//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3014 * _rolling_slope(draw, 303) + 0.000276 * anchor

def f05_vbp_360_accel_v360(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=249, w2=190, w3=316, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 249)
    baseline = trend.rolling(190, min_periods=max(190//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(316, min_periods=max(316//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.095625 + 0.0002761 * anchor

def f05_vbp_361_jerk_v361(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=5, w2=201, w3=329, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 5)
    slow = _rolling_slope(x, 201)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.11 + 0.0002762 * anchor

def f05_vbp_362_accel_v362(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=12, w2=212, w3=342, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(212, min_periods=max(212//3, 2)).max()
    trough = x.rolling(12, min_periods=max(12//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.124375 + 0.0002763 * anchor

def f05_vbp_363_jerk_v363(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=19, w2=223, w3=355, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(19)
    rank = change.rolling(223, min_periods=max(223//3, 2)).rank(pct=True)
    persistence = change.rolling(355, min_periods=max(355//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3318 * persistence + 0.0002764 * anchor

def f05_vbp_364_accel_v364(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=26, w2=234, w3=368, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(26, min_periods=max(26//3, 2)).std()
    vol_slow = ret.rolling(234, min_periods=max(234//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.153125 + 0.0002765 * anchor

def f05_vbp_365_jerk_v365(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=33, w2=245, w3=381, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(245, min_periods=max(245//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 33)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.347 * slope + 0.0002766 * anchor

def f05_vbp_366_accel_v366(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=40, w2=256, w3=394, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(40)
    drag = impulse.rolling(256, min_periods=max(256//3, 2)).mean()
    noise = impulse.abs().rolling(394, min_periods=max(394//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.181875 + 0.0002767 * anchor

def f05_vbp_367_jerk_v367(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=47, w2=267, w3=407, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 47)
    acceleration = _rolling_slope(velocity, 267)
    curvature = _rolling_slope(acceleration, 407)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3622 * acceleration + 0.0002768 * anchor

def f05_vbp_368_accel_v368(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=54, w2=278, w3=420, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(54, min_periods=max(54//3, 2)).mean(), upside.rolling(278, min_periods=max(278//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.210625 + 0.0002769 * anchor

def f05_vbp_369_jerk_v369(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=61, w2=289, w3=433, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(289, min_periods=max(289//3, 2)).max()
    rebound = x - x.rolling(61, min_periods=max(61//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3774 * _rolling_slope(draw, 433) + 0.000277 * anchor

def f05_vbp_370_accel_v370(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=68, w2=300, w3=446, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 68)
    baseline = trend.rolling(300, min_periods=max(300//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(446, min_periods=max(446//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.239375 + 0.0002771 * anchor

def f05_vbp_371_jerk_v371(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=75, w2=311, w3=459, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 75)
    slow = _rolling_slope(x, 311)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.25375 + 0.0002772 * anchor

def f05_vbp_372_accel_v372(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=82, w2=322, w3=472, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(322, min_periods=max(322//3, 2)).max()
    trough = x.rolling(82, min_periods=max(82//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.268125 + 0.0002773 * anchor

def f05_vbp_373_jerk_v373(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=89, w2=333, w3=485, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(89)
    rank = change.rolling(333, min_periods=max(333//3, 2)).rank(pct=True)
    persistence = change.rolling(485, min_periods=max(485//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.4078 * persistence + 0.0002774 * anchor

def f05_vbp_374_accel_v374(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=96, w2=344, w3=498, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(96, min_periods=max(96//3, 2)).std()
    vol_slow = ret.rolling(344, min_periods=max(344//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.296875 + 0.0002775 * anchor

def f05_vbp_375_jerk_v375(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=103, w2=355, w3=511, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(355, min_periods=max(355//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 103)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0466 * slope + 0.0002776 * anchor
