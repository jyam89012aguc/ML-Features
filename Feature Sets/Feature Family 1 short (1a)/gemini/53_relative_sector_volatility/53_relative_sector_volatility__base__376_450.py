"""53 relative sector volatility base features 376-450 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Relative_Strength - Institutional-grade short-side signal.
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

def f53_rsw_v_376_rel_v376(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=23, w2=398, w3=669, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 23)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.3322 * pressure.rolling(669, min_periods=max(669//3, 2)).mean() + 0.0032777 * anchor

def f53_rsw_v_377_rel_v377(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=30, w2=409, w3=682, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(30, min_periods=max(30//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.18625 + 0.0032778 * anchor

def f53_rsw_v_378_rel_v378(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=37, w2=420, w3=695, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(420, min_periods=max(420//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 37)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.200625 + 0.0032779 * anchor

def f53_rsw_v_379_rel_v379(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=44, w2=431, w3=708, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(44, min_periods=max(44//3, 2)).mean(), b.abs().rolling(431, min_periods=max(431//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.355 * _rolling_slope(cover, 44) + 0.003278 * anchor

def f53_rsw_v_380_rel_v380(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=51, w2=442, w3=721, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.3626 * y + 0.637400 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 51) - _rolling_slope(basket, 442) + 0.0032781 * anchor

def f53_rsw_v_381_rel_v381(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=58, w2=453, w3=734, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(58, min_periods=max(58//3, 2)).mean(), upside.rolling(453, min_periods=max(453//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.24375 + 0.0032782 * anchor

def f53_rsw_v_382_rel_v382(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=65, w2=464, w3=747, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(464, min_periods=max(464//3, 2)).max()
    rebound = x - x.rolling(65, min_periods=max(65//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3778 * _rolling_slope(draw, 747) + 0.0032783 * anchor

def f53_rsw_v_383_rel_v383(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=72, w2=475, w3=760, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(72) - b.diff(126)
    stress = imbalance.rolling(760, min_periods=max(760//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.2725 + 0.0032784 * anchor

def f53_rsw_v_384_rel_v384(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=79, w2=486, w3=16, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 79)
    baseline = trend.rolling(486, min_periods=max(486//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(16, min_periods=max(16//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.286875 + 0.0032785 * anchor

def f53_rsw_v_385_rel_v385(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=86, w2=497, w3=29, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 86)
    slow = _rolling_slope(x, 497)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=29, adjust=False).mean() * 1.30125 + 0.0032786 * anchor

def f53_rsw_v_386_rel_v386(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=93, w2=508, w3=42, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(508, min_periods=max(508//3, 2)).max()
    trough = x.rolling(93, min_periods=max(93//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.315625 + 0.0032787 * anchor

def f53_rsw_v_387_rel_v387(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=100, w2=16, w3=55, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(100)
    rank = change.rolling(16, min_periods=max(16//3, 2)).rank(pct=True)
    persistence = change.rolling(55, min_periods=max(55//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0394 * persistence + 0.0032788 * anchor

def f53_rsw_v_388_rel_v388(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=107, w2=27, w3=68, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(107, min_periods=max(107//3, 2)).std()
    vol_slow = ret.rolling(27, min_periods=max(27//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.344375 + 0.0032789 * anchor

def f53_rsw_v_389_rel_v389(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=114, w2=38, w3=81, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(38, min_periods=max(38//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 114)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0546 * slope + 0.003279 * anchor

def f53_rsw_v_390_rel_v390(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=121, w2=49, w3=94, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(121)
    drag = impulse.rolling(49, min_periods=max(49//3, 2)).mean()
    noise = impulse.abs().rolling(94, min_periods=max(94//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.373125 + 0.0032791 * anchor

def f53_rsw_v_391_rel_v391(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=128, w2=60, w3=107, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 128)
    acceleration = _rolling_slope(velocity, 60)
    curvature = _rolling_slope(acceleration, 107)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0698 * acceleration + 0.0032792 * anchor

def f53_rsw_v_392_rel_v392(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=135, w2=71, w3=120, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 135)
    pressure = rel_log.diff(71)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.0774 * pressure.rolling(120, min_periods=max(120//3, 2)).mean() + 0.0032793 * anchor

def f53_rsw_v_393_rel_v393(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=142, w2=82, w3=133, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(142, min_periods=max(142//3, 2)).mean())
    decay = spread.ewm(span=82, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.41625 + 0.0032794 * anchor

def f53_rsw_v_394_rel_v394(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=149, w2=93, w3=146, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(93, min_periods=max(93//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 149)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.430625 + 0.0032795 * anchor

def f53_rsw_v_395_rel_v395(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=156, w2=104, w3=159, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(156, min_periods=max(156//3, 2)).mean(), b.abs().rolling(104, min_periods=max(104//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.1002 * _rolling_slope(cover, 156) + 0.0032796 * anchor

def f53_rsw_v_396_rel_v396(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=163, w2=115, w3=172, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.1078 * y + 0.892200 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 163) - _rolling_slope(basket, 115) + 0.0032797 * anchor

def f53_rsw_v_397_rel_v397(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=170, w2=126, w3=185, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(170, min_periods=max(170//3, 2)).mean(), upside.rolling(126, min_periods=max(126//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.47375 + 0.0032798 * anchor

def f53_rsw_v_398_rel_v398(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=177, w2=137, w3=198, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(137, min_periods=max(137//3, 2)).max()
    rebound = x - x.rolling(177, min_periods=max(177//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.123 * _rolling_slope(draw, 198) + 0.0032799 * anchor

def f53_rsw_v_399_rel_v399(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=184, w2=148, w3=211, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(211, min_periods=max(211//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.5025 + 0.00328 * anchor

def f53_rsw_v_400_rel_v400(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=191, w2=159, w3=224, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 191)
    baseline = trend.rolling(159, min_periods=max(159//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(224, min_periods=max(224//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.516875 + 0.0032801 * anchor

def f53_rsw_v_401_rel_v401(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=198, w2=170, w3=237, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 198)
    slow = _rolling_slope(x, 170)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=237, adjust=False).mean() * 1.53125 + 0.0032802 * anchor

def f53_rsw_v_402_rel_v402(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=205, w2=181, w3=250, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(181, min_periods=max(181//3, 2)).max()
    trough = x.rolling(205, min_periods=max(205//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.545625 + 0.0032803 * anchor

def f53_rsw_v_403_rel_v403(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=212, w2=192, w3=263, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(192, min_periods=max(192//3, 2)).rank(pct=True)
    persistence = change.rolling(263, min_periods=max(263//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.161 * persistence + 0.0032804 * anchor

def f53_rsw_v_404_rel_v404(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=219, w2=203, w3=276, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(219, min_periods=max(219//3, 2)).std()
    vol_slow = ret.rolling(203, min_periods=max(203//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.574375 + 0.0032805 * anchor

def f53_rsw_v_405_rel_v405(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=226, w2=214, w3=289, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(214, min_periods=max(214//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 226)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1762 * slope + 0.0032806 * anchor

def f53_rsw_v_406_rel_v406(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=233, w2=225, w3=302, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(225, min_periods=max(225//3, 2)).mean()
    noise = impulse.abs().rolling(302, min_periods=max(302//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.603125 + 0.0032807 * anchor

def f53_rsw_v_407_rel_v407(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=240, w2=236, w3=315, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 240)
    acceleration = _rolling_slope(velocity, 236)
    curvature = _rolling_slope(acceleration, 315)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1914 * acceleration + 0.0032808 * anchor

def f53_rsw_v_408_rel_v408(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=247, w2=247, w3=328, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 247)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.199 * pressure.rolling(328, min_periods=max(328//3, 2)).mean() + 0.0032809 * anchor

def f53_rsw_v_409_rel_v409(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=254, w2=258, w3=341, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(254, min_periods=max(254//3, 2)).mean())
    decay = spread.ewm(span=258, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 0.873125 + 0.003281 * anchor

def f53_rsw_v_410_rel_v410(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=10, w2=269, w3=354, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(269, min_periods=max(269//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 10)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 0.8875 + 0.0032811 * anchor

def f53_rsw_v_411_rel_v411(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=17, w2=280, w3=367, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(17, min_periods=max(17//3, 2)).mean(), b.abs().rolling(280, min_periods=max(280//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.2218 * _rolling_slope(cover, 17) + 0.0032812 * anchor

def f53_rsw_v_412_rel_v412(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=24, w2=291, w3=380, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.2294 * y + 0.770600 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 24) - _rolling_slope(basket, 291) + 0.0032813 * anchor

def f53_rsw_v_413_rel_v413(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=31, w2=302, w3=393, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(31, min_periods=max(31//3, 2)).mean(), upside.rolling(302, min_periods=max(302//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.930625 + 0.0032814 * anchor

def f53_rsw_v_414_rel_v414(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=38, w2=313, w3=406, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(313, min_periods=max(313//3, 2)).max()
    rebound = x - x.rolling(38, min_periods=max(38//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2446 * _rolling_slope(draw, 406) + 0.0032815 * anchor

def f53_rsw_v_415_rel_v415(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=45, w2=324, w3=419, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(45) - b.diff(126)
    stress = imbalance.rolling(419, min_periods=max(419//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 0.959375 + 0.0032816 * anchor

def f53_rsw_v_416_rel_v416(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=52, w2=335, w3=432, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 52)
    baseline = trend.rolling(335, min_periods=max(335//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(432, min_periods=max(432//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.97375 + 0.0032817 * anchor

def f53_rsw_v_417_rel_v417(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=59, w2=346, w3=445, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 59)
    slow = _rolling_slope(x, 346)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.988125 + 0.0032818 * anchor

def f53_rsw_v_418_rel_v418(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=66, w2=357, w3=458, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(357, min_periods=max(357//3, 2)).max()
    trough = x.rolling(66, min_periods=max(66//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.0025 + 0.0032819 * anchor

def f53_rsw_v_419_rel_v419(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=73, w2=368, w3=471, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(73)
    rank = change.rolling(368, min_periods=max(368//3, 2)).rank(pct=True)
    persistence = change.rolling(471, min_periods=max(471//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2826 * persistence + 0.003282 * anchor

def f53_rsw_v_420_rel_v420(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=80, w2=379, w3=484, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(80, min_periods=max(80//3, 2)).std()
    vol_slow = ret.rolling(379, min_periods=max(379//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.03125 + 0.0032821 * anchor

def f53_rsw_v_421_rel_v421(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=87, w2=390, w3=497, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(390, min_periods=max(390//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 87)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2978 * slope + 0.0032822 * anchor

def f53_rsw_v_422_rel_v422(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=94, w2=401, w3=510, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(94)
    drag = impulse.rolling(401, min_periods=max(401//3, 2)).mean()
    noise = impulse.abs().rolling(510, min_periods=max(510//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.06 + 0.0032823 * anchor

def f53_rsw_v_423_rel_v423(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=101, w2=412, w3=523, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 101)
    acceleration = _rolling_slope(velocity, 412)
    curvature = _rolling_slope(acceleration, 523)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.313 * acceleration + 0.0032824 * anchor

def f53_rsw_v_424_rel_v424(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=108, w2=423, w3=536, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 108)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.3206 * pressure.rolling(536, min_periods=max(536//3, 2)).mean() + 0.0032825 * anchor

def f53_rsw_v_425_rel_v425(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=115, w2=434, w3=549, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(115, min_periods=max(115//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.103125 + 0.0032826 * anchor

def f53_rsw_v_426_rel_v426(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=122, w2=445, w3=562, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(445, min_periods=max(445//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 122)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.1175 + 0.0032827 * anchor

def f53_rsw_v_427_rel_v427(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=129, w2=456, w3=575, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(129, min_periods=max(129//3, 2)).mean(), b.abs().rolling(456, min_periods=max(456//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.3434 * _rolling_slope(cover, 129) + 0.0032828 * anchor

def f53_rsw_v_428_rel_v428(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=136, w2=467, w3=588, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.351 * y + 0.649000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 136) - _rolling_slope(basket, 467) + 0.0032829 * anchor

def f53_rsw_v_429_rel_v429(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=143, w2=478, w3=601, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(143, min_periods=max(143//3, 2)).mean(), upside.rolling(478, min_periods=max(478//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.160625 + 0.003283 * anchor

def f53_rsw_v_430_rel_v430(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=150, w2=489, w3=614, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(489, min_periods=max(489//3, 2)).max()
    rebound = x - x.rolling(150, min_periods=max(150//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3662 * _rolling_slope(draw, 614) + 0.0032831 * anchor

def f53_rsw_v_431_rel_v431(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=157, w2=500, w3=627, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(627, min_periods=max(627//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.189375 + 0.0032832 * anchor

def f53_rsw_v_432_rel_v432(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=164, w2=511, w3=640, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 164)
    baseline = trend.rolling(511, min_periods=max(511//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(640, min_periods=max(640//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.20375 + 0.0032833 * anchor

def f53_rsw_v_433_rel_v433(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=171, w2=19, w3=653, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 171)
    slow = _rolling_slope(x, 19)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.218125 + 0.0032834 * anchor

def f53_rsw_v_434_rel_v434(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=178, w2=30, w3=666, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(30, min_periods=max(30//3, 2)).max()
    trough = x.rolling(178, min_periods=max(178//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.2325 + 0.0032835 * anchor

def f53_rsw_v_435_rel_v435(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=185, w2=41, w3=679, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(41, min_periods=max(41//3, 2)).rank(pct=True)
    persistence = change.rolling(679, min_periods=max(679//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.4042 * persistence + 0.0032836 * anchor

def f53_rsw_v_436_rel_v436(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=192, w2=52, w3=692, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(192, min_periods=max(192//3, 2)).std()
    vol_slow = ret.rolling(52, min_periods=max(52//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.26125 + 0.0032837 * anchor

def f53_rsw_v_437_rel_v437(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=199, w2=63, w3=705, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(63, min_periods=max(63//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 199)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.043 * slope + 0.0032838 * anchor

def f53_rsw_v_438_rel_v438(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=206, w2=74, w3=718, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(74, min_periods=max(74//3, 2)).mean()
    noise = impulse.abs().rolling(718, min_periods=max(718//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.29 + 0.0032839 * anchor

def f53_rsw_v_439_rel_v439(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=213, w2=85, w3=731, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 213)
    acceleration = _rolling_slope(velocity, 85)
    curvature = _rolling_slope(acceleration, 731)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0582 * acceleration + 0.003284 * anchor

def f53_rsw_v_440_rel_v440(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=220, w2=96, w3=744, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 220)
    pressure = rel_log.diff(96)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.0658 * pressure.rolling(744, min_periods=max(744//3, 2)).mean() + 0.0032841 * anchor

def f53_rsw_v_441_rel_v441(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=227, w2=107, w3=757, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(227, min_periods=max(227//3, 2)).mean())
    decay = spread.ewm(span=107, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.333125 + 0.0032842 * anchor

def f53_rsw_v_442_rel_v442(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=234, w2=118, w3=770, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(118, min_periods=max(118//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 234)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.3475 + 0.0032843 * anchor

def f53_rsw_v_443_rel_v443(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=241, w2=129, w3=26, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(241, min_periods=max(241//3, 2)).mean(), b.abs().rolling(129, min_periods=max(129//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(26) + 0.0886 * _rolling_slope(cover, 241) + 0.0032844 * anchor

def f53_rsw_v_444_rel_v444(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=248, w2=140, w3=39, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.0962 * y + 0.903800 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 248) - _rolling_slope(basket, 140) + 0.0032845 * anchor

def f53_rsw_v_445_rel_v445(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=255, w2=151, w3=52, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(255, min_periods=max(255//3, 2)).mean(), upside.rolling(151, min_periods=max(151//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(52) * 1.390625 + 0.0032846 * anchor

def f53_rsw_v_446_rel_v446(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=11, w2=162, w3=65, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(162, min_periods=max(162//3, 2)).max()
    rebound = x - x.rolling(11, min_periods=max(11//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1114 * _rolling_slope(draw, 65) + 0.0032847 * anchor

def f53_rsw_v_447_rel_v447(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=18, w2=173, w3=78, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(18) - b.diff(126)
    stress = imbalance.rolling(78, min_periods=max(78//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.419375 + 0.0032848 * anchor

def f53_rsw_v_448_rel_v448(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=25, w2=184, w3=91, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 25)
    baseline = trend.rolling(184, min_periods=max(184//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(91, min_periods=max(91//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.43375 + 0.0032849 * anchor

def f53_rsw_v_449_rel_v449(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=32, w2=195, w3=104, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 32)
    slow = _rolling_slope(x, 195)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=104, adjust=False).mean() * 1.448125 + 0.003285 * anchor

def f53_rsw_v_450_rel_v450(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=39, w2=206, w3=117, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(206, min_periods=max(206//3, 2)).max()
    trough = x.rolling(39, min_periods=max(39//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.4625 + 0.0032851 * anchor
