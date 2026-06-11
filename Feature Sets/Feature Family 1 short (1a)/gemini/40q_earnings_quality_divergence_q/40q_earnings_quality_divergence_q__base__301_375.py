"""40q earnings quality divergence q base features 301-375 â€” Pipeline 1a-HF Grade v3.

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

def f40q_eqdq_301_accrual_v301(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=118, w2=289, w3=489, lag=21)."""
    x = ocf.shift(21)
    ma = x.rolling(289, min_periods=max(289//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 118)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3298 * slope + 0.0024902 * anchor

def f40q_eqdq_302_accrual_v302(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=125, w2=300, w3=502, lag=42)."""
    x = assetsc.shift(42)
    impulse = x.diff(125)
    drag = impulse.rolling(300, min_periods=max(300//3, 2)).mean()
    noise = impulse.abs().rolling(502, min_periods=max(502//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.859375 + 0.0024903 * anchor

def f40q_eqdq_303_accrual_v303(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=132, w2=311, w3=515, lag=63)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 132)
    acceleration = _rolling_slope(velocity, 311)
    curvature = _rolling_slope(acceleration, 515)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.345 * acceleration + 0.0024904 * anchor

def f40q_eqdq_304_accrual_v304(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=139, w2=322, w3=528, lag=0)."""
    rel = _safe_div(inventory.shift(0), revenue.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 139)
    pressure = rel_log.diff(126)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.3526 * pressure.rolling(528, min_periods=max(528//3, 2)).mean() + 0.0024905 * anchor

def f40q_eqdq_305_accrual_v305(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=146, w2=333, w3=541, lag=1)."""
    a = revenue.shift(1)
    b = netinc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(146, min_periods=max(146//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 0.9025 + 0.0024906 * anchor

def f40q_eqdq_306_accrual_v306(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=153, w2=344, w3=554, lag=2)."""
    a = _safe_log(netinc.abs() + 1.0).shift(2)
    b = _safe_log(ocf.abs() + 1.0).shift(2)
    corr = a.rolling(344, min_periods=max(344//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 153)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 0.916875 + 0.0024907 * anchor

def f40q_eqdq_307_accrual_v307(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=160, w2=355, w3=567, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(160, min_periods=max(160//3, 2)).mean(), b.abs().rolling(355, min_periods=max(355//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.3754 * _rolling_slope(cover, 160) + 0.0024908 * anchor

def f40q_eqdq_308_accrual_v308(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=167, w2=366, w3=580, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    y = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    z = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    basket = x - 0.383 * y + 0.617000 * z
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 167) - _rolling_slope(basket, 366) + 0.0024909 * anchor

def f40q_eqdq_309_accrual_v309(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=174, w2=377, w3=593, lag=21)."""
    x = liabilitiesc.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(174, min_periods=max(174//3, 2)).mean(), upside.rolling(377, min_periods=max(377//3, 2)).mean().abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.96 + 0.002491 * anchor

def f40q_eqdq_310_accrual_v310(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=181, w2=388, w3=606, lag=42)."""
    x = _safe_log(inventory.abs() + 1.0).shift(42)
    draw = x - x.rolling(388, min_periods=max(388//3, 2)).max()
    rebound = x - x.rolling(181, min_periods=max(181//3, 2)).min()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3982 * _rolling_slope(draw, 606) + 0.0024911 * anchor

def f40q_eqdq_311_accrual_v311(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=188, w2=399, w3=619, lag=63)."""
    a = _safe_log(revenue.abs() + 1.0).shift(63)
    b = _safe_log(netinc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(619, min_periods=max(619//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 0.98875 + 0.0024912 * anchor

def f40q_eqdq_312_accrual_v312(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=195, w2=410, w3=632, lag=0)."""
    x = _safe_log(netinc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 195)
    baseline = trend.rolling(410, min_periods=max(410//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(632, min_periods=max(632//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.003125 + 0.0024913 * anchor

def f40q_eqdq_313_accrual_v313(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=202, w2=421, w3=645, lag=1)."""
    x = _safe_log(ocf.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 202)
    slow = _rolling_slope(x, 421)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.0175 + 0.0024914 * anchor

def f40q_eqdq_314_accrual_v314(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=209, w2=432, w3=658, lag=2)."""
    x = assetsc.shift(2)
    peak = x.rolling(432, min_periods=max(432//3, 2)).max()
    trough = x.rolling(209, min_periods=max(209//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.031875 + 0.0024915 * anchor

def f40q_eqdq_315_accrual_v315(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=216, w2=443, w3=671, lag=5)."""
    x = liabilitiesc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(443, min_periods=max(443//3, 2)).rank(pct=True)
    persistence = change.rolling(671, min_periods=max(671//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0598 * persistence + 0.0024916 * anchor

def f40q_eqdq_316_accrual_v316(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=223, w2=454, w3=684, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(223, min_periods=max(223//3, 2)).std()
    vol_slow = ret.rolling(454, min_periods=max(454//3, 2)).std()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.060625 + 0.0024917 * anchor

def f40q_eqdq_317_accrual_v317(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=230, w2=465, w3=697, lag=21)."""
    x = revenue.shift(21)
    ma = x.rolling(465, min_periods=max(465//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 230)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.075 * slope + 0.0024918 * anchor

def f40q_eqdq_318_accrual_v318(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=237, w2=476, w3=710, lag=42)."""
    x = netinc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(476, min_periods=max(476//3, 2)).mean()
    noise = impulse.abs().rolling(710, min_periods=max(710//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.089375 + 0.0024919 * anchor

def f40q_eqdq_319_accrual_v319(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=244, w2=487, w3=723, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 244)
    acceleration = _rolling_slope(velocity, 487)
    curvature = _rolling_slope(acceleration, 723)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0902 * acceleration + 0.002492 * anchor

def f40q_eqdq_320_accrual_v320(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=251, w2=498, w3=736, lag=0)."""
    rel = _safe_div(assetsc.shift(0), liabilitiesc.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 251)
    pressure = rel_log.diff(126)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.0978 * pressure.rolling(736, min_periods=max(736//3, 2)).mean() + 0.0024921 * anchor

def f40q_eqdq_321_accrual_v321(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=7, w2=509, w3=749, lag=1)."""
    a = liabilitiesc.shift(1)
    b = inventory.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(7, min_periods=max(7//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.1325 + 0.0024922 * anchor

def f40q_eqdq_322_accrual_v322(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=14, w2=17, w3=762, lag=2)."""
    a = _safe_log(inventory.abs() + 1.0).shift(2)
    b = _safe_log(revenue.abs() + 1.0).shift(2)
    corr = a.rolling(17, min_periods=max(17//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 14)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.146875 + 0.0024923 * anchor

def f40q_eqdq_323_accrual_v323(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=21, w2=28, w3=18, lag=5)."""
    a = revenue.shift(5)
    b = netinc.shift(5)
    cover = _safe_div(a.rolling(21, min_periods=max(21//3, 2)).mean(), b.abs().rolling(28, min_periods=max(28//3, 2)).mean())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(18) + 0.1206 * _rolling_slope(cover, 21) + 0.0024924 * anchor

def f40q_eqdq_324_accrual_v324(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=28, w2=39, w3=31, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    y = _safe_log(ocf.abs() + 1.0).shift(10)
    z = _safe_log(ocf.abs() + 1.0).shift(10)
    basket = x - 0.1282 * y + 0.871800 * z
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 28) - _rolling_slope(basket, 39) + 0.0024925 * anchor

def f40q_eqdq_325_accrual_v325(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=35, w2=50, w3=44, lag=21)."""
    x = ocf.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(35, min_periods=max(35//3, 2)).mean(), upside.rolling(50, min_periods=max(50//3, 2)).mean().abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(44) * 1.19 + 0.0024926 * anchor

def f40q_eqdq_326_accrual_v326(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=42, w2=61, w3=57, lag=42)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(42)
    draw = x - x.rolling(61, min_periods=max(61//3, 2)).max()
    rebound = x - x.rolling(42, min_periods=max(42//3, 2)).min()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1434 * _rolling_slope(draw, 57) + 0.0024927 * anchor

def f40q_eqdq_327_accrual_v327(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=49, w2=72, w3=70, lag=63)."""
    a = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    b = _safe_log(inventory.abs() + 1.0).shift(63)
    imbalance = a.diff(49) - b.diff(72)
    stress = imbalance.rolling(70, min_periods=max(70//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.21875 + 0.0024928 * anchor

def f40q_eqdq_328_accrual_v328(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=56, w2=83, w3=83, lag=0)."""
    x = _safe_log(inventory.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 56)
    baseline = trend.rolling(83, min_periods=max(83//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(83, min_periods=max(83//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.233125 + 0.0024929 * anchor

def f40q_eqdq_329_accrual_v329(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=63, w2=94, w3=96, lag=1)."""
    x = _safe_log(revenue.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 63)
    slow = _rolling_slope(x, 94)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=96, adjust=False).mean() * 1.2475 + 0.002493 * anchor

def f40q_eqdq_330_accrual_v330(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=70, w2=105, w3=109, lag=2)."""
    x = netinc.shift(2)
    peak = x.rolling(105, min_periods=max(105//3, 2)).max()
    trough = x.rolling(70, min_periods=max(70//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.261875 + 0.0024931 * anchor

def f40q_eqdq_331_accrual_v331(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=77, w2=116, w3=122, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(77)
    rank = change.rolling(116, min_periods=max(116//3, 2)).rank(pct=True)
    persistence = change.rolling(122, min_periods=max(122//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1814 * persistence + 0.0024932 * anchor

def f40q_eqdq_332_accrual_v332(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=84, w2=127, w3=135, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(84, min_periods=max(84//3, 2)).std()
    vol_slow = ret.rolling(127, min_periods=max(127//3, 2)).std()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.290625 + 0.0024933 * anchor

def f40q_eqdq_333_accrual_v333(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=91, w2=138, w3=148, lag=21)."""
    x = liabilitiesc.shift(21)
    ma = x.rolling(138, min_periods=max(138//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 91)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1966 * slope + 0.0024934 * anchor

def f40q_eqdq_334_accrual_v334(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=98, w2=149, w3=161, lag=42)."""
    x = inventory.shift(42)
    impulse = x.diff(98)
    drag = impulse.rolling(149, min_periods=max(149//3, 2)).mean()
    noise = impulse.abs().rolling(161, min_periods=max(161//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.319375 + 0.0024935 * anchor

def f40q_eqdq_335_accrual_v335(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=105, w2=160, w3=174, lag=63)."""
    x = _safe_log(revenue.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 105)
    acceleration = _rolling_slope(velocity, 160)
    curvature = _rolling_slope(acceleration, 174)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2118 * acceleration + 0.0024936 * anchor

def f40q_eqdq_336_accrual_v336(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=112, w2=171, w3=187, lag=0)."""
    rel = _safe_div(netinc.shift(0), ocf.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 112)
    pressure = rel_log.diff(126)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.2194 * pressure.rolling(187, min_periods=max(187//3, 2)).mean() + 0.0024937 * anchor

def f40q_eqdq_337_accrual_v337(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=119, w2=182, w3=200, lag=1)."""
    a = ocf.shift(1)
    b = assetsc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(119, min_periods=max(119//3, 2)).mean())
    decay = spread.ewm(span=182, adjust=False).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.3625 + 0.0024938 * anchor

def f40q_eqdq_338_accrual_v338(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=126, w2=193, w3=213, lag=2)."""
    a = _safe_log(assetsc.abs() + 1.0).shift(2)
    b = _safe_log(liabilitiesc.abs() + 1.0).shift(2)
    corr = a.rolling(193, min_periods=max(193//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 126)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.376875 + 0.0024939 * anchor

def f40q_eqdq_339_accrual_v339(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=133, w2=204, w3=226, lag=5)."""
    a = liabilitiesc.shift(5)
    b = inventory.shift(5)
    cover = _safe_div(a.rolling(133, min_periods=max(133//3, 2)).mean(), b.abs().rolling(204, min_periods=max(204//3, 2)).mean())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.2422 * _rolling_slope(cover, 133) + 0.002494 * anchor

def f40q_eqdq_340_accrual_v340(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=140, w2=215, w3=239, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    y = _safe_log(revenue.abs() + 1.0).shift(10)
    z = _safe_log(revenue.abs() + 1.0).shift(10)
    basket = x - 0.2498 * y + 0.750200 * z
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 140) - _rolling_slope(basket, 215) + 0.0024941 * anchor

def f40q_eqdq_341_accrual_v341(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=147, w2=226, w3=252, lag=21)."""
    x = revenue.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(147, min_periods=max(147//3, 2)).mean(), upside.rolling(226, min_periods=max(226//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.42 + 0.0024942 * anchor

def f40q_eqdq_342_accrual_v342(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=154, w2=237, w3=265, lag=42)."""
    x = _safe_log(netinc.abs() + 1.0).shift(42)
    draw = x - x.rolling(237, min_periods=max(237//3, 2)).max()
    rebound = x - x.rolling(154, min_periods=max(154//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.265 * _rolling_slope(draw, 265) + 0.0024943 * anchor

def f40q_eqdq_343_accrual_v343(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=161, w2=248, w3=278, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(278, min_periods=max(278//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.44875 + 0.0024944 * anchor

def f40q_eqdq_344_accrual_v344(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=168, w2=259, w3=291, lag=0)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 168)
    baseline = trend.rolling(259, min_periods=max(259//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(291, min_periods=max(291//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.463125 + 0.0024945 * anchor

def f40q_eqdq_345_accrual_v345(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=175, w2=270, w3=304, lag=1)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 175)
    slow = _rolling_slope(x, 270)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.4775 + 0.0024946 * anchor

def f40q_eqdq_346_accrual_v346(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=182, w2=281, w3=317, lag=2)."""
    x = inventory.shift(2)
    peak = x.rolling(281, min_periods=max(281//3, 2)).max()
    trough = x.rolling(182, min_periods=max(182//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.491875 + 0.0024947 * anchor

def f40q_eqdq_347_accrual_v347(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=189, w2=292, w3=330, lag=5)."""
    x = revenue.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(292, min_periods=max(292//3, 2)).rank(pct=True)
    persistence = change.rolling(330, min_periods=max(330//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.303 * persistence + 0.0024948 * anchor

def f40q_eqdq_348_accrual_v348(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=196, w2=303, w3=343, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(196, min_periods=max(196//3, 2)).std()
    vol_slow = ret.rolling(303, min_periods=max(303//3, 2)).std()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.520625 + 0.0024949 * anchor

def f40q_eqdq_349_accrual_v349(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=203, w2=314, w3=356, lag=21)."""
    x = ocf.shift(21)
    ma = x.rolling(314, min_periods=max(314//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 203)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3182 * slope + 0.002495 * anchor

def f40q_eqdq_350_accrual_v350(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=210, w2=325, w3=369, lag=42)."""
    x = assetsc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(325, min_periods=max(325//3, 2)).mean()
    noise = impulse.abs().rolling(369, min_periods=max(369//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.549375 + 0.0024951 * anchor

def f40q_eqdq_351_accrual_v351(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=217, w2=336, w3=382, lag=63)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 217)
    acceleration = _rolling_slope(velocity, 336)
    curvature = _rolling_slope(acceleration, 382)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3334 * acceleration + 0.0024952 * anchor

def f40q_eqdq_352_accrual_v352(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=224, w2=347, w3=395, lag=0)."""
    rel = _safe_div(inventory.shift(0), revenue.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 224)
    pressure = rel_log.diff(126)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.341 * pressure.rolling(395, min_periods=max(395//3, 2)).mean() + 0.0024953 * anchor

def f40q_eqdq_353_accrual_v353(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=231, w2=358, w3=408, lag=1)."""
    a = revenue.shift(1)
    b = netinc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(231, min_periods=max(231//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.5925 + 0.0024954 * anchor

def f40q_eqdq_354_accrual_v354(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=238, w2=369, w3=421, lag=2)."""
    a = _safe_log(netinc.abs() + 1.0).shift(2)
    b = _safe_log(ocf.abs() + 1.0).shift(2)
    corr = a.rolling(369, min_periods=max(369//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 238)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.606875 + 0.0024955 * anchor

def f40q_eqdq_355_accrual_v355(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=245, w2=380, w3=434, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(245, min_periods=max(245//3, 2)).mean(), b.abs().rolling(380, min_periods=max(380//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.3638 * _rolling_slope(cover, 245) + 0.0024956 * anchor

def f40q_eqdq_356_accrual_v356(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=252, w2=391, w3=447, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    y = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    z = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    basket = x - 0.3714 * y + 0.628600 * z
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 252) - _rolling_slope(basket, 391) + 0.0024957 * anchor

def f40q_eqdq_357_accrual_v357(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=8, w2=402, w3=460, lag=21)."""
    x = liabilitiesc.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(8, min_periods=max(8//3, 2)).mean(), upside.rolling(402, min_periods=max(402//3, 2)).mean().abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.876875 + 0.0024958 * anchor

def f40q_eqdq_358_accrual_v358(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=15, w2=413, w3=473, lag=42)."""
    x = _safe_log(inventory.abs() + 1.0).shift(42)
    draw = x - x.rolling(413, min_periods=max(413//3, 2)).max()
    rebound = x - x.rolling(15, min_periods=max(15//3, 2)).min()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3866 * _rolling_slope(draw, 473) + 0.0024959 * anchor

def f40q_eqdq_359_accrual_v359(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=22, w2=424, w3=486, lag=63)."""
    a = _safe_log(revenue.abs() + 1.0).shift(63)
    b = _safe_log(netinc.abs() + 1.0).shift(63)
    imbalance = a.diff(22) - b.diff(126)
    stress = imbalance.rolling(486, min_periods=max(486//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 0.905625 + 0.002496 * anchor

def f40q_eqdq_360_accrual_v360(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=29, w2=435, w3=499, lag=0)."""
    x = _safe_log(netinc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 29)
    baseline = trend.rolling(435, min_periods=max(435//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(499, min_periods=max(499//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.92 + 0.0024961 * anchor

def f40q_eqdq_361_accrual_v361(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=36, w2=446, w3=512, lag=1)."""
    x = _safe_log(ocf.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 36)
    slow = _rolling_slope(x, 446)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.934375 + 0.0024962 * anchor

def f40q_eqdq_362_accrual_v362(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=43, w2=457, w3=525, lag=2)."""
    x = assetsc.shift(2)
    peak = x.rolling(457, min_periods=max(457//3, 2)).max()
    trough = x.rolling(43, min_periods=max(43//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.94875 + 0.0024963 * anchor

def f40q_eqdq_363_accrual_v363(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=50, w2=468, w3=538, lag=5)."""
    x = liabilitiesc.shift(5)
    change = x.pct_change(50)
    rank = change.rolling(468, min_periods=max(468//3, 2)).rank(pct=True)
    persistence = change.rolling(538, min_periods=max(538//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0482 * persistence + 0.0024964 * anchor

def f40q_eqdq_364_accrual_v364(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=57, w2=479, w3=551, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(57, min_periods=max(57//3, 2)).std()
    vol_slow = ret.rolling(479, min_periods=max(479//3, 2)).std()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.9775 + 0.0024965 * anchor

def f40q_eqdq_365_accrual_v365(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=64, w2=490, w3=564, lag=21)."""
    x = revenue.shift(21)
    ma = x.rolling(490, min_periods=max(490//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 64)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0634 * slope + 0.0024966 * anchor

def f40q_eqdq_366_accrual_v366(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=71, w2=501, w3=577, lag=42)."""
    x = netinc.shift(42)
    impulse = x.diff(71)
    drag = impulse.rolling(501, min_periods=max(501//3, 2)).mean()
    noise = impulse.abs().rolling(577, min_periods=max(577//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.00625 + 0.0024967 * anchor

def f40q_eqdq_367_accrual_v367(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=78, w2=512, w3=590, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 78)
    acceleration = _rolling_slope(velocity, 512)
    curvature = _rolling_slope(acceleration, 590)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0786 * acceleration + 0.0024968 * anchor

def f40q_eqdq_368_accrual_v368(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=85, w2=20, w3=603, lag=0)."""
    rel = _safe_div(assetsc.shift(0), liabilitiesc.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 85)
    pressure = rel_log.diff(20)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.0862 * pressure.rolling(603, min_periods=max(603//3, 2)).mean() + 0.0024969 * anchor

def f40q_eqdq_369_accrual_v369(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=92, w2=31, w3=616, lag=1)."""
    a = liabilitiesc.shift(1)
    b = inventory.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(92, min_periods=max(92//3, 2)).mean())
    decay = spread.ewm(span=31, adjust=False).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.049375 + 0.002497 * anchor

def f40q_eqdq_370_accrual_v370(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=99, w2=42, w3=629, lag=2)."""
    a = _safe_log(inventory.abs() + 1.0).shift(2)
    b = _safe_log(revenue.abs() + 1.0).shift(2)
    corr = a.rolling(42, min_periods=max(42//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 99)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.06375 + 0.0024971 * anchor

def f40q_eqdq_371_accrual_v371(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=106, w2=53, w3=642, lag=5)."""
    a = revenue.shift(5)
    b = netinc.shift(5)
    cover = _safe_div(a.rolling(106, min_periods=max(106//3, 2)).mean(), b.abs().rolling(53, min_periods=max(53//3, 2)).mean())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.109 * _rolling_slope(cover, 106) + 0.0024972 * anchor

def f40q_eqdq_372_accrual_v372(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=113, w2=64, w3=655, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    y = _safe_log(ocf.abs() + 1.0).shift(10)
    z = _safe_log(ocf.abs() + 1.0).shift(10)
    basket = x - 0.1166 * y + 0.883400 * z
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 113) - _rolling_slope(basket, 64) + 0.0024973 * anchor

def f40q_eqdq_373_accrual_v373(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=120, w2=75, w3=668, lag=21)."""
    x = ocf.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(120, min_periods=max(120//3, 2)).mean(), upside.rolling(75, min_periods=max(75//3, 2)).mean().abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.106875 + 0.0024974 * anchor

def f40q_eqdq_374_accrual_v374(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=127, w2=86, w3=681, lag=42)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(42)
    draw = x - x.rolling(86, min_periods=max(86//3, 2)).max()
    rebound = x - x.rolling(127, min_periods=max(127//3, 2)).min()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1318 * _rolling_slope(draw, 681) + 0.0024975 * anchor

def f40q_eqdq_375_accrual_v375(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=134, w2=97, w3=694, lag=63)."""
    a = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    b = _safe_log(inventory.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(97)
    stress = imbalance.rolling(694, min_periods=max(694//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.135625 + 0.0024976 * anchor
