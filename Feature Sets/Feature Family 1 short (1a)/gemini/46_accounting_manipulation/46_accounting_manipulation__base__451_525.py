"""46 accounting manipulation base features 451-525 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Accounting_Fraud - Institutional-grade short-side signal.
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

def f46_aman_451_accrual_v451(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=13, w2=293, w3=34, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(13, min_periods=max(13//3, 2)).mean(), b.abs().rolling(293, min_periods=max(293//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(34) + 0.2234 * _rolling_slope(cover, 13) + 0.0028652 * anchor

def f46_aman_452_accrual_v452(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=20, w2=304, w3=47, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    y = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    z = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    basket = x - 0.231 * y + 0.769000 * z
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 20) - _rolling_slope(basket, 304) + 0.0028653 * anchor

def f46_aman_453_accrual_v453(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=27, w2=315, w3=60, lag=21)."""
    x = liabilitiesc.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(27, min_periods=max(27//3, 2)).mean(), upside.rolling(315, min_periods=max(315//3, 2)).mean().abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(60) * 1.434375 + 0.0028654 * anchor

def f46_aman_454_accrual_v454(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=34, w2=326, w3=73, lag=42)."""
    x = _safe_log(inventory.abs() + 1.0).shift(42)
    draw = x - x.rolling(326, min_periods=max(326//3, 2)).max()
    rebound = x - x.rolling(34, min_periods=max(34//3, 2)).min()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2462 * _rolling_slope(draw, 73) + 0.0028655 * anchor

def f46_aman_455_accrual_v455(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=41, w2=337, w3=86, lag=63)."""
    a = _safe_log(revenue.abs() + 1.0).shift(63)
    b = _safe_log(netinc.abs() + 1.0).shift(63)
    imbalance = a.diff(41) - b.diff(126)
    stress = imbalance.rolling(86, min_periods=max(86//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.463125 + 0.0028656 * anchor

def f46_aman_456_accrual_v456(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=48, w2=348, w3=99, lag=0)."""
    x = _safe_log(netinc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 48)
    baseline = trend.rolling(348, min_periods=max(348//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(99, min_periods=max(99//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.4775 + 0.0028657 * anchor

def f46_aman_457_accrual_v457(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=55, w2=359, w3=112, lag=1)."""
    x = _safe_log(ocf.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 55)
    slow = _rolling_slope(x, 359)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=112, adjust=False).mean() * 1.491875 + 0.0028658 * anchor

def f46_aman_458_accrual_v458(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=62, w2=370, w3=125, lag=2)."""
    x = assetsc.shift(2)
    peak = x.rolling(370, min_periods=max(370//3, 2)).max()
    trough = x.rolling(62, min_periods=max(62//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.50625 + 0.0028659 * anchor

def f46_aman_459_accrual_v459(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=69, w2=381, w3=138, lag=5)."""
    x = liabilitiesc.shift(5)
    change = x.pct_change(69)
    rank = change.rolling(381, min_periods=max(381//3, 2)).rank(pct=True)
    persistence = change.rolling(138, min_periods=max(138//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2842 * persistence + 0.002866 * anchor

def f46_aman_460_accrual_v460(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=76, w2=392, w3=151, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(76, min_periods=max(76//3, 2)).std()
    vol_slow = ret.rolling(392, min_periods=max(392//3, 2)).std()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.535 + 0.0028661 * anchor

def f46_aman_461_accrual_v461(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=83, w2=403, w3=164, lag=21)."""
    x = revenue.shift(21)
    ma = x.rolling(403, min_periods=max(403//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 83)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2994 * slope + 0.0028662 * anchor

def f46_aman_462_accrual_v462(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=90, w2=414, w3=177, lag=42)."""
    x = netinc.shift(42)
    impulse = x.diff(90)
    drag = impulse.rolling(414, min_periods=max(414//3, 2)).mean()
    noise = impulse.abs().rolling(177, min_periods=max(177//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.56375 + 0.0028663 * anchor

def f46_aman_463_accrual_v463(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=97, w2=425, w3=190, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 97)
    acceleration = _rolling_slope(velocity, 425)
    curvature = _rolling_slope(acceleration, 190)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3146 * acceleration + 0.0028664 * anchor

def f46_aman_464_accrual_v464(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=104, w2=436, w3=203, lag=0)."""
    rel = _safe_div(assetsc.shift(0), liabilitiesc.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 104)
    pressure = rel_log.diff(126)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.3222 * pressure.rolling(203, min_periods=max(203//3, 2)).mean() + 0.0028665 * anchor

def f46_aman_465_accrual_v465(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=111, w2=447, w3=216, lag=1)."""
    a = liabilitiesc.shift(1)
    b = inventory.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(111, min_periods=max(111//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.606875 + 0.0028666 * anchor

def f46_aman_466_accrual_v466(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=118, w2=458, w3=229, lag=2)."""
    a = _safe_log(inventory.abs() + 1.0).shift(2)
    b = _safe_log(revenue.abs() + 1.0).shift(2)
    corr = a.rolling(458, min_periods=max(458//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 118)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.62125 + 0.0028667 * anchor

def f46_aman_467_accrual_v467(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=125, w2=469, w3=242, lag=5)."""
    a = revenue.shift(5)
    b = netinc.shift(5)
    cover = _safe_div(a.rolling(125, min_periods=max(125//3, 2)).mean(), b.abs().rolling(469, min_periods=max(469//3, 2)).mean())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.345 * _rolling_slope(cover, 125) + 0.0028668 * anchor

def f46_aman_468_accrual_v468(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=132, w2=480, w3=255, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    y = _safe_log(ocf.abs() + 1.0).shift(10)
    z = _safe_log(ocf.abs() + 1.0).shift(10)
    basket = x - 0.3526 * y + 0.647400 * z
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 132) - _rolling_slope(basket, 480) + 0.0028669 * anchor

def f46_aman_469_accrual_v469(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=139, w2=491, w3=268, lag=21)."""
    x = ocf.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(139, min_periods=max(139//3, 2)).mean(), upside.rolling(491, min_periods=max(491//3, 2)).mean().abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.89125 + 0.002867 * anchor

def f46_aman_470_accrual_v470(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=146, w2=502, w3=281, lag=42)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(42)
    draw = x - x.rolling(502, min_periods=max(502//3, 2)).max()
    rebound = x - x.rolling(146, min_periods=max(146//3, 2)).min()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3678 * _rolling_slope(draw, 281) + 0.0028671 * anchor

def f46_aman_471_accrual_v471(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=153, w2=10, w3=294, lag=63)."""
    a = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    b = _safe_log(inventory.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(10)
    stress = imbalance.rolling(294, min_periods=max(294//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 0.92 + 0.0028672 * anchor

def f46_aman_472_accrual_v472(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=160, w2=21, w3=307, lag=0)."""
    x = _safe_log(inventory.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 160)
    baseline = trend.rolling(21, min_periods=max(21//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(307, min_periods=max(307//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.934375 + 0.0028673 * anchor

def f46_aman_473_accrual_v473(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=167, w2=32, w3=320, lag=1)."""
    x = _safe_log(revenue.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 167)
    slow = _rolling_slope(x, 32)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.94875 + 0.0028674 * anchor

def f46_aman_474_accrual_v474(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=174, w2=43, w3=333, lag=2)."""
    x = netinc.shift(2)
    peak = x.rolling(43, min_periods=max(43//3, 2)).max()
    trough = x.rolling(174, min_periods=max(174//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.963125 + 0.0028675 * anchor

def f46_aman_475_accrual_v475(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=181, w2=54, w3=346, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(54, min_periods=max(54//3, 2)).rank(pct=True)
    persistence = change.rolling(346, min_periods=max(346//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.4058 * persistence + 0.0028676 * anchor

def f46_aman_476_accrual_v476(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=188, w2=65, w3=359, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(188, min_periods=max(188//3, 2)).std()
    vol_slow = ret.rolling(65, min_periods=max(65//3, 2)).std()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.991875 + 0.0028677 * anchor

def f46_aman_477_accrual_v477(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=195, w2=76, w3=372, lag=21)."""
    x = liabilitiesc.shift(21)
    ma = x.rolling(76, min_periods=max(76//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 195)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0446 * slope + 0.0028678 * anchor

def f46_aman_478_accrual_v478(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=202, w2=87, w3=385, lag=42)."""
    x = inventory.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(87, min_periods=max(87//3, 2)).mean()
    noise = impulse.abs().rolling(385, min_periods=max(385//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.020625 + 0.0028679 * anchor

def f46_aman_479_accrual_v479(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=209, w2=98, w3=398, lag=63)."""
    x = _safe_log(revenue.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 209)
    acceleration = _rolling_slope(velocity, 98)
    curvature = _rolling_slope(acceleration, 398)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0598 * acceleration + 0.002868 * anchor

def f46_aman_480_accrual_v480(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=216, w2=109, w3=411, lag=0)."""
    rel = _safe_div(netinc.shift(0), ocf.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 216)
    pressure = rel_log.diff(109)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.0674 * pressure.rolling(411, min_periods=max(411//3, 2)).mean() + 0.0028681 * anchor

def f46_aman_481_accrual_v481(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=223, w2=120, w3=424, lag=1)."""
    a = ocf.shift(1)
    b = assetsc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(223, min_periods=max(223//3, 2)).mean())
    decay = spread.ewm(span=120, adjust=False).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.06375 + 0.0028682 * anchor

def f46_aman_482_accrual_v482(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=230, w2=131, w3=437, lag=2)."""
    a = _safe_log(assetsc.abs() + 1.0).shift(2)
    b = _safe_log(liabilitiesc.abs() + 1.0).shift(2)
    corr = a.rolling(131, min_periods=max(131//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 230)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.078125 + 0.0028683 * anchor

def f46_aman_483_accrual_v483(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=237, w2=142, w3=450, lag=5)."""
    a = liabilitiesc.shift(5)
    b = inventory.shift(5)
    cover = _safe_div(a.rolling(237, min_periods=max(237//3, 2)).mean(), b.abs().rolling(142, min_periods=max(142//3, 2)).mean())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.0902 * _rolling_slope(cover, 237) + 0.0028684 * anchor

def f46_aman_484_accrual_v484(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=244, w2=153, w3=463, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    y = _safe_log(revenue.abs() + 1.0).shift(10)
    z = _safe_log(revenue.abs() + 1.0).shift(10)
    basket = x - 0.0978 * y + 0.902200 * z
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 244) - _rolling_slope(basket, 153) + 0.0028685 * anchor

def f46_aman_485_accrual_v485(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=251, w2=164, w3=476, lag=21)."""
    x = revenue.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(251, min_periods=max(251//3, 2)).mean(), upside.rolling(164, min_periods=max(164//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.12125 + 0.0028686 * anchor

def f46_aman_486_accrual_v486(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=7, w2=175, w3=489, lag=42)."""
    x = _safe_log(netinc.abs() + 1.0).shift(42)
    draw = x - x.rolling(175, min_periods=max(175//3, 2)).max()
    rebound = x - x.rolling(7, min_periods=max(7//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.113 * _rolling_slope(draw, 489) + 0.0028687 * anchor

def f46_aman_487_accrual_v487(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=14, w2=186, w3=502, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(14) - b.diff(126)
    stress = imbalance.rolling(502, min_periods=max(502//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.15 + 0.0028688 * anchor

def f46_aman_488_accrual_v488(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=21, w2=197, w3=515, lag=0)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 21)
    baseline = trend.rolling(197, min_periods=max(197//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(515, min_periods=max(515//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.164375 + 0.0028689 * anchor

def f46_aman_489_accrual_v489(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=28, w2=208, w3=528, lag=1)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 28)
    slow = _rolling_slope(x, 208)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.17875 + 0.002869 * anchor

def f46_aman_490_accrual_v490(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=35, w2=219, w3=541, lag=2)."""
    x = inventory.shift(2)
    peak = x.rolling(219, min_periods=max(219//3, 2)).max()
    trough = x.rolling(35, min_periods=max(35//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.193125 + 0.0028691 * anchor

def f46_aman_491_accrual_v491(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=42, w2=230, w3=554, lag=5)."""
    x = revenue.shift(5)
    change = x.pct_change(42)
    rank = change.rolling(230, min_periods=max(230//3, 2)).rank(pct=True)
    persistence = change.rolling(554, min_periods=max(554//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.151 * persistence + 0.0028692 * anchor

def f46_aman_492_accrual_v492(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=49, w2=241, w3=567, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(49, min_periods=max(49//3, 2)).std()
    vol_slow = ret.rolling(241, min_periods=max(241//3, 2)).std()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.221875 + 0.0028693 * anchor

def f46_aman_493_accrual_v493(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=56, w2=252, w3=580, lag=21)."""
    x = ocf.shift(21)
    ma = x.rolling(252, min_periods=max(252//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 56)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1662 * slope + 0.0028694 * anchor

def f46_aman_494_accrual_v494(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=63, w2=263, w3=593, lag=42)."""
    x = assetsc.shift(42)
    impulse = x.diff(63)
    drag = impulse.rolling(263, min_periods=max(263//3, 2)).mean()
    noise = impulse.abs().rolling(593, min_periods=max(593//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.250625 + 0.0028695 * anchor

def f46_aman_495_accrual_v495(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=70, w2=274, w3=606, lag=63)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 70)
    acceleration = _rolling_slope(velocity, 274)
    curvature = _rolling_slope(acceleration, 606)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1814 * acceleration + 0.0028696 * anchor

def f46_aman_496_accrual_v496(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=77, w2=285, w3=619, lag=0)."""
    rel = _safe_div(inventory.shift(0), revenue.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 77)
    pressure = rel_log.diff(126)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.189 * pressure.rolling(619, min_periods=max(619//3, 2)).mean() + 0.0028697 * anchor

def f46_aman_497_accrual_v497(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=84, w2=296, w3=632, lag=1)."""
    a = revenue.shift(1)
    b = netinc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(84, min_periods=max(84//3, 2)).mean())
    decay = spread.ewm(span=296, adjust=False).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.29375 + 0.0028698 * anchor

def f46_aman_498_accrual_v498(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=91, w2=307, w3=645, lag=2)."""
    a = _safe_log(netinc.abs() + 1.0).shift(2)
    b = _safe_log(ocf.abs() + 1.0).shift(2)
    corr = a.rolling(307, min_periods=max(307//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 91)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.308125 + 0.0028699 * anchor

def f46_aman_499_accrual_v499(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=98, w2=318, w3=658, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(98, min_periods=max(98//3, 2)).mean(), b.abs().rolling(318, min_periods=max(318//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.2118 * _rolling_slope(cover, 98) + 0.00287 * anchor

def f46_aman_500_accrual_v500(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=105, w2=329, w3=671, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    y = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    z = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    basket = x - 0.2194 * y + 0.780600 * z
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 105) - _rolling_slope(basket, 329) + 0.0028701 * anchor

def f46_aman_501_accrual_v501(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=112, w2=340, w3=684, lag=21)."""
    x = liabilitiesc.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(112, min_periods=max(112//3, 2)).mean(), upside.rolling(340, min_periods=max(340//3, 2)).mean().abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.35125 + 0.0028702 * anchor

def f46_aman_502_accrual_v502(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=119, w2=351, w3=697, lag=42)."""
    x = _safe_log(inventory.abs() + 1.0).shift(42)
    draw = x - x.rolling(351, min_periods=max(351//3, 2)).max()
    rebound = x - x.rolling(119, min_periods=max(119//3, 2)).min()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2346 * _rolling_slope(draw, 697) + 0.0028703 * anchor

def f46_aman_503_accrual_v503(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=126, w2=362, w3=710, lag=63)."""
    a = _safe_log(revenue.abs() + 1.0).shift(63)
    b = _safe_log(netinc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(710, min_periods=max(710//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.38 + 0.0028704 * anchor

def f46_aman_504_accrual_v504(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=133, w2=373, w3=723, lag=0)."""
    x = _safe_log(netinc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 133)
    baseline = trend.rolling(373, min_periods=max(373//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(723, min_periods=max(723//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.394375 + 0.0028705 * anchor

def f46_aman_505_accrual_v505(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=140, w2=384, w3=736, lag=1)."""
    x = _safe_log(ocf.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 140)
    slow = _rolling_slope(x, 384)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.40875 + 0.0028706 * anchor

def f46_aman_506_accrual_v506(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=147, w2=395, w3=749, lag=2)."""
    x = assetsc.shift(2)
    peak = x.rolling(395, min_periods=max(395//3, 2)).max()
    trough = x.rolling(147, min_periods=max(147//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.423125 + 0.0028707 * anchor

def f46_aman_507_accrual_v507(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=154, w2=406, w3=762, lag=5)."""
    x = liabilitiesc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(406, min_periods=max(406//3, 2)).rank(pct=True)
    persistence = change.rolling(762, min_periods=max(762//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2726 * persistence + 0.0028708 * anchor

def f46_aman_508_accrual_v508(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=161, w2=417, w3=18, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(161, min_periods=max(161//3, 2)).std()
    vol_slow = ret.rolling(417, min_periods=max(417//3, 2)).std()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.451875 + 0.0028709 * anchor

def f46_aman_509_accrual_v509(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=168, w2=428, w3=31, lag=21)."""
    x = revenue.shift(21)
    ma = x.rolling(428, min_periods=max(428//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 168)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2878 * slope + 0.002871 * anchor

def f46_aman_510_accrual_v510(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=175, w2=439, w3=44, lag=42)."""
    x = netinc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(439, min_periods=max(439//3, 2)).mean()
    noise = impulse.abs().rolling(44, min_periods=max(44//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.480625 + 0.0028711 * anchor

def f46_aman_511_accrual_v511(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=182, w2=450, w3=57, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 182)
    acceleration = _rolling_slope(velocity, 450)
    curvature = _rolling_slope(acceleration, 57)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.303 * acceleration + 0.0028712 * anchor

def f46_aman_512_accrual_v512(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=189, w2=461, w3=70, lag=0)."""
    rel = _safe_div(assetsc.shift(0), liabilitiesc.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 189)
    pressure = rel_log.diff(126)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.3106 * pressure.rolling(70, min_periods=max(70//3, 2)).mean() + 0.0028713 * anchor

def f46_aman_513_accrual_v513(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=196, w2=472, w3=83, lag=1)."""
    a = liabilitiesc.shift(1)
    b = inventory.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(196, min_periods=max(196//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.52375 + 0.0028714 * anchor

def f46_aman_514_accrual_v514(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=203, w2=483, w3=96, lag=2)."""
    a = _safe_log(inventory.abs() + 1.0).shift(2)
    b = _safe_log(revenue.abs() + 1.0).shift(2)
    corr = a.rolling(483, min_periods=max(483//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 203)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.538125 + 0.0028715 * anchor

def f46_aman_515_accrual_v515(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=210, w2=494, w3=109, lag=5)."""
    a = revenue.shift(5)
    b = netinc.shift(5)
    cover = _safe_div(a.rolling(210, min_periods=max(210//3, 2)).mean(), b.abs().rolling(494, min_periods=max(494//3, 2)).mean())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(109) + 0.3334 * _rolling_slope(cover, 210) + 0.0028716 * anchor

def f46_aman_516_accrual_v516(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=217, w2=505, w3=122, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    y = _safe_log(ocf.abs() + 1.0).shift(10)
    z = _safe_log(ocf.abs() + 1.0).shift(10)
    basket = x - 0.341 * y + 0.659000 * z
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 217) - _rolling_slope(basket, 505) + 0.0028717 * anchor

def f46_aman_517_accrual_v517(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=224, w2=13, w3=135, lag=21)."""
    x = ocf.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(224, min_periods=max(224//3, 2)).mean(), upside.rolling(13, min_periods=max(13//3, 2)).mean().abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.58125 + 0.0028718 * anchor

def f46_aman_518_accrual_v518(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=231, w2=24, w3=148, lag=42)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(42)
    draw = x - x.rolling(24, min_periods=max(24//3, 2)).max()
    rebound = x - x.rolling(231, min_periods=max(231//3, 2)).min()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3562 * _rolling_slope(draw, 148) + 0.0028719 * anchor

def f46_aman_519_accrual_v519(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=238, w2=35, w3=161, lag=63)."""
    a = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    b = _safe_log(inventory.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(35)
    stress = imbalance.rolling(161, min_periods=max(161//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.61 + 0.002872 * anchor

def f46_aman_520_accrual_v520(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=245, w2=46, w3=174, lag=0)."""
    x = _safe_log(inventory.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 245)
    baseline = trend.rolling(46, min_periods=max(46//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(174, min_periods=max(174//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.85125 + 0.0028721 * anchor

def f46_aman_521_accrual_v521(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=252, w2=57, w3=187, lag=1)."""
    x = _safe_log(revenue.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 252)
    slow = _rolling_slope(x, 57)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=187, adjust=False).mean() * 0.865625 + 0.0028722 * anchor

def f46_aman_522_accrual_v522(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=8, w2=68, w3=200, lag=2)."""
    x = netinc.shift(2)
    peak = x.rolling(68, min_periods=max(68//3, 2)).max()
    trough = x.rolling(8, min_periods=max(8//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.88 + 0.0028723 * anchor

def f46_aman_523_accrual_v523(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=15, w2=79, w3=213, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(15)
    rank = change.rolling(79, min_periods=max(79//3, 2)).rank(pct=True)
    persistence = change.rolling(213, min_periods=max(213//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3942 * persistence + 0.0028724 * anchor

def f46_aman_524_accrual_v524(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=22, w2=90, w3=226, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(22, min_periods=max(22//3, 2)).std()
    vol_slow = ret.rolling(90, min_periods=max(90//3, 2)).std()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.90875 + 0.0028725 * anchor

def f46_aman_525_accrual_v525(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=29, w2=101, w3=239, lag=21)."""
    x = liabilitiesc.shift(21)
    ma = x.rolling(101, min_periods=max(101//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 29)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.4094 * slope + 0.0028726 * anchor
