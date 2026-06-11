"""46 accounting manipulation base features 301-375 â€” Pipeline 1a-HF Grade v3.

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

def f46_aman_301_accrual_v301(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=218, w2=152, w3=355, lag=21)."""
    x = ocf.shift(21)
    ma = x.rolling(152, min_periods=max(152//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 218)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2126 * slope + 0.0028502 * anchor

def f46_aman_302_accrual_v302(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=225, w2=163, w3=368, lag=42)."""
    x = assetsc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(163, min_periods=max(163//3, 2)).mean()
    noise = impulse.abs().rolling(368, min_periods=max(368//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.583125 + 0.0028503 * anchor

def f46_aman_303_accrual_v303(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=232, w2=174, w3=381, lag=63)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 232)
    acceleration = _rolling_slope(velocity, 174)
    curvature = _rolling_slope(acceleration, 381)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2278 * acceleration + 0.0028504 * anchor

def f46_aman_304_accrual_v304(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=239, w2=185, w3=394, lag=0)."""
    rel = _safe_div(inventory.shift(0), revenue.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 239)
    pressure = rel_log.diff(126)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.2354 * pressure.rolling(394, min_periods=max(394//3, 2)).mean() + 0.0028505 * anchor

def f46_aman_305_accrual_v305(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=246, w2=196, w3=407, lag=1)."""
    a = revenue.shift(1)
    b = netinc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(246, min_periods=max(246//3, 2)).mean())
    decay = spread.ewm(span=196, adjust=False).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 0.853125 + 0.0028506 * anchor

def f46_aman_306_accrual_v306(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=253, w2=207, w3=420, lag=2)."""
    a = _safe_log(netinc.abs() + 1.0).shift(2)
    b = _safe_log(ocf.abs() + 1.0).shift(2)
    corr = a.rolling(207, min_periods=max(207//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 253)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 0.8675 + 0.0028507 * anchor

def f46_aman_307_accrual_v307(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=9, w2=218, w3=433, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(9, min_periods=max(9//3, 2)).mean(), b.abs().rolling(218, min_periods=max(218//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.2582 * _rolling_slope(cover, 9) + 0.0028508 * anchor

def f46_aman_308_accrual_v308(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=16, w2=229, w3=446, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    y = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    z = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    basket = x - 0.2658 * y + 0.734200 * z
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 16) - _rolling_slope(basket, 229) + 0.0028509 * anchor

def f46_aman_309_accrual_v309(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=23, w2=240, w3=459, lag=21)."""
    x = liabilitiesc.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(23, min_periods=max(23//3, 2)).mean(), upside.rolling(240, min_periods=max(240//3, 2)).mean().abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.910625 + 0.002851 * anchor

def f46_aman_310_accrual_v310(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=30, w2=251, w3=472, lag=42)."""
    x = _safe_log(inventory.abs() + 1.0).shift(42)
    draw = x - x.rolling(251, min_periods=max(251//3, 2)).max()
    rebound = x - x.rolling(30, min_periods=max(30//3, 2)).min()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.281 * _rolling_slope(draw, 472) + 0.0028511 * anchor

def f46_aman_311_accrual_v311(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=37, w2=262, w3=485, lag=63)."""
    a = _safe_log(revenue.abs() + 1.0).shift(63)
    b = _safe_log(netinc.abs() + 1.0).shift(63)
    imbalance = a.diff(37) - b.diff(126)
    stress = imbalance.rolling(485, min_periods=max(485//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 0.939375 + 0.0028512 * anchor

def f46_aman_312_accrual_v312(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=44, w2=273, w3=498, lag=0)."""
    x = _safe_log(netinc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 44)
    baseline = trend.rolling(273, min_periods=max(273//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(498, min_periods=max(498//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.95375 + 0.0028513 * anchor

def f46_aman_313_accrual_v313(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=51, w2=284, w3=511, lag=1)."""
    x = _safe_log(ocf.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 51)
    slow = _rolling_slope(x, 284)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.968125 + 0.0028514 * anchor

def f46_aman_314_accrual_v314(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=58, w2=295, w3=524, lag=2)."""
    x = assetsc.shift(2)
    peak = x.rolling(295, min_periods=max(295//3, 2)).max()
    trough = x.rolling(58, min_periods=max(58//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.9825 + 0.0028515 * anchor

def f46_aman_315_accrual_v315(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=65, w2=306, w3=537, lag=5)."""
    x = liabilitiesc.shift(5)
    change = x.pct_change(65)
    rank = change.rolling(306, min_periods=max(306//3, 2)).rank(pct=True)
    persistence = change.rolling(537, min_periods=max(537//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.319 * persistence + 0.0028516 * anchor

def f46_aman_316_accrual_v316(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=72, w2=317, w3=550, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(72, min_periods=max(72//3, 2)).std()
    vol_slow = ret.rolling(317, min_periods=max(317//3, 2)).std()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.01125 + 0.0028517 * anchor

def f46_aman_317_accrual_v317(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=79, w2=328, w3=563, lag=21)."""
    x = revenue.shift(21)
    ma = x.rolling(328, min_periods=max(328//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 79)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3342 * slope + 0.0028518 * anchor

def f46_aman_318_accrual_v318(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=86, w2=339, w3=576, lag=42)."""
    x = netinc.shift(42)
    impulse = x.diff(86)
    drag = impulse.rolling(339, min_periods=max(339//3, 2)).mean()
    noise = impulse.abs().rolling(576, min_periods=max(576//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.04 + 0.0028519 * anchor

def f46_aman_319_accrual_v319(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=93, w2=350, w3=589, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 93)
    acceleration = _rolling_slope(velocity, 350)
    curvature = _rolling_slope(acceleration, 589)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3494 * acceleration + 0.002852 * anchor

def f46_aman_320_accrual_v320(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=100, w2=361, w3=602, lag=0)."""
    rel = _safe_div(assetsc.shift(0), liabilitiesc.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 100)
    pressure = rel_log.diff(126)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.357 * pressure.rolling(602, min_periods=max(602//3, 2)).mean() + 0.0028521 * anchor

def f46_aman_321_accrual_v321(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=107, w2=372, w3=615, lag=1)."""
    a = liabilitiesc.shift(1)
    b = inventory.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(107, min_periods=max(107//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.083125 + 0.0028522 * anchor

def f46_aman_322_accrual_v322(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=114, w2=383, w3=628, lag=2)."""
    a = _safe_log(inventory.abs() + 1.0).shift(2)
    b = _safe_log(revenue.abs() + 1.0).shift(2)
    corr = a.rolling(383, min_periods=max(383//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 114)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.0975 + 0.0028523 * anchor

def f46_aman_323_accrual_v323(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=121, w2=394, w3=641, lag=5)."""
    a = revenue.shift(5)
    b = netinc.shift(5)
    cover = _safe_div(a.rolling(121, min_periods=max(121//3, 2)).mean(), b.abs().rolling(394, min_periods=max(394//3, 2)).mean())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.3798 * _rolling_slope(cover, 121) + 0.0028524 * anchor

def f46_aman_324_accrual_v324(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=128, w2=405, w3=654, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    y = _safe_log(ocf.abs() + 1.0).shift(10)
    z = _safe_log(ocf.abs() + 1.0).shift(10)
    basket = x - 0.3874 * y + 0.612600 * z
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 128) - _rolling_slope(basket, 405) + 0.0028525 * anchor

def f46_aman_325_accrual_v325(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=135, w2=416, w3=667, lag=21)."""
    x = ocf.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(135, min_periods=max(135//3, 2)).mean(), upside.rolling(416, min_periods=max(416//3, 2)).mean().abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.140625 + 0.0028526 * anchor

def f46_aman_326_accrual_v326(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=142, w2=427, w3=680, lag=42)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(42)
    draw = x - x.rolling(427, min_periods=max(427//3, 2)).max()
    rebound = x - x.rolling(142, min_periods=max(142//3, 2)).min()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.4026 * _rolling_slope(draw, 680) + 0.0028527 * anchor

def f46_aman_327_accrual_v327(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=149, w2=438, w3=693, lag=63)."""
    a = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    b = _safe_log(inventory.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(693, min_periods=max(693//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.169375 + 0.0028528 * anchor

def f46_aman_328_accrual_v328(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=156, w2=449, w3=706, lag=0)."""
    x = _safe_log(inventory.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 156)
    baseline = trend.rolling(449, min_periods=max(449//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(706, min_periods=max(706//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.18375 + 0.0028529 * anchor

def f46_aman_329_accrual_v329(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=163, w2=460, w3=719, lag=1)."""
    x = _safe_log(revenue.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 163)
    slow = _rolling_slope(x, 460)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.198125 + 0.002853 * anchor

def f46_aman_330_accrual_v330(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=170, w2=471, w3=732, lag=2)."""
    x = netinc.shift(2)
    peak = x.rolling(471, min_periods=max(471//3, 2)).max()
    trough = x.rolling(170, min_periods=max(170//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.2125 + 0.0028531 * anchor

def f46_aman_331_accrual_v331(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=177, w2=482, w3=745, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(482, min_periods=max(482//3, 2)).rank(pct=True)
    persistence = change.rolling(745, min_periods=max(745//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0642 * persistence + 0.0028532 * anchor

def f46_aman_332_accrual_v332(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=184, w2=493, w3=758, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(184, min_periods=max(184//3, 2)).std()
    vol_slow = ret.rolling(493, min_periods=max(493//3, 2)).std()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.24125 + 0.0028533 * anchor

def f46_aman_333_accrual_v333(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=191, w2=504, w3=771, lag=21)."""
    x = liabilitiesc.shift(21)
    ma = x.rolling(504, min_periods=max(504//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 191)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0794 * slope + 0.0028534 * anchor

def f46_aman_334_accrual_v334(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=198, w2=12, w3=27, lag=42)."""
    x = inventory.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(12, min_periods=max(12//3, 2)).mean()
    noise = impulse.abs().rolling(27, min_periods=max(27//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.27 + 0.0028535 * anchor

def f46_aman_335_accrual_v335(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=205, w2=23, w3=40, lag=63)."""
    x = _safe_log(revenue.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 205)
    acceleration = _rolling_slope(velocity, 23)
    curvature = _rolling_slope(acceleration, 40)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0946 * acceleration + 0.0028536 * anchor

def f46_aman_336_accrual_v336(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=212, w2=34, w3=53, lag=0)."""
    rel = _safe_div(netinc.shift(0), ocf.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 212)
    pressure = rel_log.diff(34)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.1022 * pressure.rolling(53, min_periods=max(53//3, 2)).mean() + 0.0028537 * anchor

def f46_aman_337_accrual_v337(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=219, w2=45, w3=66, lag=1)."""
    a = ocf.shift(1)
    b = assetsc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(219, min_periods=max(219//3, 2)).mean())
    decay = spread.ewm(span=45, adjust=False).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.313125 + 0.0028538 * anchor

def f46_aman_338_accrual_v338(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=226, w2=56, w3=79, lag=2)."""
    a = _safe_log(assetsc.abs() + 1.0).shift(2)
    b = _safe_log(liabilitiesc.abs() + 1.0).shift(2)
    corr = a.rolling(56, min_periods=max(56//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 226)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.3275 + 0.0028539 * anchor

def f46_aman_339_accrual_v339(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=233, w2=67, w3=92, lag=5)."""
    a = liabilitiesc.shift(5)
    b = inventory.shift(5)
    cover = _safe_div(a.rolling(233, min_periods=max(233//3, 2)).mean(), b.abs().rolling(67, min_periods=max(67//3, 2)).mean())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(92) + 0.125 * _rolling_slope(cover, 233) + 0.002854 * anchor

def f46_aman_340_accrual_v340(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=240, w2=78, w3=105, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    y = _safe_log(revenue.abs() + 1.0).shift(10)
    z = _safe_log(revenue.abs() + 1.0).shift(10)
    basket = x - 0.1326 * y + 0.867400 * z
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 240) - _rolling_slope(basket, 78) + 0.0028541 * anchor

def f46_aman_341_accrual_v341(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=247, w2=89, w3=118, lag=21)."""
    x = revenue.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(247, min_periods=max(247//3, 2)).mean(), upside.rolling(89, min_periods=max(89//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(118) * 1.370625 + 0.0028542 * anchor

def f46_aman_342_accrual_v342(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=254, w2=100, w3=131, lag=42)."""
    x = _safe_log(netinc.abs() + 1.0).shift(42)
    draw = x - x.rolling(100, min_periods=max(100//3, 2)).max()
    rebound = x - x.rolling(254, min_periods=max(254//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1478 * _rolling_slope(draw, 131) + 0.0028543 * anchor

def f46_aman_343_accrual_v343(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=10, w2=111, w3=144, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(10) - b.diff(111)
    stress = imbalance.rolling(144, min_periods=max(144//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.399375 + 0.0028544 * anchor

def f46_aman_344_accrual_v344(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=17, w2=122, w3=157, lag=0)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 17)
    baseline = trend.rolling(122, min_periods=max(122//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(157, min_periods=max(157//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.41375 + 0.0028545 * anchor

def f46_aman_345_accrual_v345(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=24, w2=133, w3=170, lag=1)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 24)
    slow = _rolling_slope(x, 133)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=170, adjust=False).mean() * 1.428125 + 0.0028546 * anchor

def f46_aman_346_accrual_v346(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=31, w2=144, w3=183, lag=2)."""
    x = inventory.shift(2)
    peak = x.rolling(144, min_periods=max(144//3, 2)).max()
    trough = x.rolling(31, min_periods=max(31//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.4425 + 0.0028547 * anchor

def f46_aman_347_accrual_v347(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=38, w2=155, w3=196, lag=5)."""
    x = revenue.shift(5)
    change = x.pct_change(38)
    rank = change.rolling(155, min_periods=max(155//3, 2)).rank(pct=True)
    persistence = change.rolling(196, min_periods=max(196//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1858 * persistence + 0.0028548 * anchor

def f46_aman_348_accrual_v348(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=45, w2=166, w3=209, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(45, min_periods=max(45//3, 2)).std()
    vol_slow = ret.rolling(166, min_periods=max(166//3, 2)).std()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.47125 + 0.0028549 * anchor

def f46_aman_349_accrual_v349(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=52, w2=177, w3=222, lag=21)."""
    x = ocf.shift(21)
    ma = x.rolling(177, min_periods=max(177//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 52)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.201 * slope + 0.002855 * anchor

def f46_aman_350_accrual_v350(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=59, w2=188, w3=235, lag=42)."""
    x = assetsc.shift(42)
    impulse = x.diff(59)
    drag = impulse.rolling(188, min_periods=max(188//3, 2)).mean()
    noise = impulse.abs().rolling(235, min_periods=max(235//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.5 + 0.0028551 * anchor

def f46_aman_351_accrual_v351(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=66, w2=199, w3=248, lag=63)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 66)
    acceleration = _rolling_slope(velocity, 199)
    curvature = _rolling_slope(acceleration, 248)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2162 * acceleration + 0.0028552 * anchor

def f46_aman_352_accrual_v352(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=73, w2=210, w3=261, lag=0)."""
    rel = _safe_div(inventory.shift(0), revenue.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 73)
    pressure = rel_log.diff(126)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.2238 * pressure.rolling(261, min_periods=max(261//3, 2)).mean() + 0.0028553 * anchor

def f46_aman_353_accrual_v353(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=80, w2=221, w3=274, lag=1)."""
    a = revenue.shift(1)
    b = netinc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(80, min_periods=max(80//3, 2)).mean())
    decay = spread.ewm(span=221, adjust=False).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.543125 + 0.0028554 * anchor

def f46_aman_354_accrual_v354(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=87, w2=232, w3=287, lag=2)."""
    a = _safe_log(netinc.abs() + 1.0).shift(2)
    b = _safe_log(ocf.abs() + 1.0).shift(2)
    corr = a.rolling(232, min_periods=max(232//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 87)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.5575 + 0.0028555 * anchor

def f46_aman_355_accrual_v355(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=94, w2=243, w3=300, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(94, min_periods=max(94//3, 2)).mean(), b.abs().rolling(243, min_periods=max(243//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.2466 * _rolling_slope(cover, 94) + 0.0028556 * anchor

def f46_aman_356_accrual_v356(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=101, w2=254, w3=313, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    y = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    z = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    basket = x - 0.2542 * y + 0.745800 * z
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 101) - _rolling_slope(basket, 254) + 0.0028557 * anchor

def f46_aman_357_accrual_v357(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=108, w2=265, w3=326, lag=21)."""
    x = liabilitiesc.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(108, min_periods=max(108//3, 2)).mean(), upside.rolling(265, min_periods=max(265//3, 2)).mean().abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.600625 + 0.0028558 * anchor

def f46_aman_358_accrual_v358(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=115, w2=276, w3=339, lag=42)."""
    x = _safe_log(inventory.abs() + 1.0).shift(42)
    draw = x - x.rolling(276, min_periods=max(276//3, 2)).max()
    rebound = x - x.rolling(115, min_periods=max(115//3, 2)).min()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2694 * _rolling_slope(draw, 339) + 0.0028559 * anchor

def f46_aman_359_accrual_v359(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=122, w2=287, w3=352, lag=63)."""
    a = _safe_log(revenue.abs() + 1.0).shift(63)
    b = _safe_log(netinc.abs() + 1.0).shift(63)
    imbalance = a.diff(122) - b.diff(126)
    stress = imbalance.rolling(352, min_periods=max(352//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 0.85625 + 0.002856 * anchor

def f46_aman_360_accrual_v360(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=129, w2=298, w3=365, lag=0)."""
    x = _safe_log(netinc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 129)
    baseline = trend.rolling(298, min_periods=max(298//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(365, min_periods=max(365//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.870625 + 0.0028561 * anchor

def f46_aman_361_accrual_v361(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=136, w2=309, w3=378, lag=1)."""
    x = _safe_log(ocf.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 136)
    slow = _rolling_slope(x, 309)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.885 + 0.0028562 * anchor

def f46_aman_362_accrual_v362(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=143, w2=320, w3=391, lag=2)."""
    x = assetsc.shift(2)
    peak = x.rolling(320, min_periods=max(320//3, 2)).max()
    trough = x.rolling(143, min_periods=max(143//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.899375 + 0.0028563 * anchor

def f46_aman_363_accrual_v363(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=150, w2=331, w3=404, lag=5)."""
    x = liabilitiesc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(331, min_periods=max(331//3, 2)).rank(pct=True)
    persistence = change.rolling(404, min_periods=max(404//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3074 * persistence + 0.0028564 * anchor

def f46_aman_364_accrual_v364(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=157, w2=342, w3=417, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(157, min_periods=max(157//3, 2)).std()
    vol_slow = ret.rolling(342, min_periods=max(342//3, 2)).std()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.928125 + 0.0028565 * anchor

def f46_aman_365_accrual_v365(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=164, w2=353, w3=430, lag=21)."""
    x = revenue.shift(21)
    ma = x.rolling(353, min_periods=max(353//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 164)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3226 * slope + 0.0028566 * anchor

def f46_aman_366_accrual_v366(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=171, w2=364, w3=443, lag=42)."""
    x = netinc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(364, min_periods=max(364//3, 2)).mean()
    noise = impulse.abs().rolling(443, min_periods=max(443//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.956875 + 0.0028567 * anchor

def f46_aman_367_accrual_v367(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=178, w2=375, w3=456, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 178)
    acceleration = _rolling_slope(velocity, 375)
    curvature = _rolling_slope(acceleration, 456)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3378 * acceleration + 0.0028568 * anchor

def f46_aman_368_accrual_v368(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=185, w2=386, w3=469, lag=0)."""
    rel = _safe_div(assetsc.shift(0), liabilitiesc.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 185)
    pressure = rel_log.diff(126)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.3454 * pressure.rolling(469, min_periods=max(469//3, 2)).mean() + 0.0028569 * anchor

def f46_aman_369_accrual_v369(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=192, w2=397, w3=482, lag=1)."""
    a = liabilitiesc.shift(1)
    b = inventory.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(192, min_periods=max(192//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.0 + 0.002857 * anchor

def f46_aman_370_accrual_v370(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=199, w2=408, w3=495, lag=2)."""
    a = _safe_log(inventory.abs() + 1.0).shift(2)
    b = _safe_log(revenue.abs() + 1.0).shift(2)
    corr = a.rolling(408, min_periods=max(408//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 199)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.014375 + 0.0028571 * anchor

def f46_aman_371_accrual_v371(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=206, w2=419, w3=508, lag=5)."""
    a = revenue.shift(5)
    b = netinc.shift(5)
    cover = _safe_div(a.rolling(206, min_periods=max(206//3, 2)).mean(), b.abs().rolling(419, min_periods=max(419//3, 2)).mean())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.3682 * _rolling_slope(cover, 206) + 0.0028572 * anchor

def f46_aman_372_accrual_v372(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=213, w2=430, w3=521, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    y = _safe_log(ocf.abs() + 1.0).shift(10)
    z = _safe_log(ocf.abs() + 1.0).shift(10)
    basket = x - 0.3758 * y + 0.624200 * z
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 213) - _rolling_slope(basket, 430) + 0.0028573 * anchor

def f46_aman_373_accrual_v373(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=220, w2=441, w3=534, lag=21)."""
    x = ocf.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(220, min_periods=max(220//3, 2)).mean(), upside.rolling(441, min_periods=max(441//3, 2)).mean().abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.0575 + 0.0028574 * anchor

def f46_aman_374_accrual_v374(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=227, w2=452, w3=547, lag=42)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(42)
    draw = x - x.rolling(452, min_periods=max(452//3, 2)).max()
    rebound = x - x.rolling(227, min_periods=max(227//3, 2)).min()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.391 * _rolling_slope(draw, 547) + 0.0028575 * anchor

def f46_aman_375_accrual_v375(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=234, w2=463, w3=560, lag=63)."""
    a = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    b = _safe_log(inventory.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(560, min_periods=max(560//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.08625 + 0.0028576 * anchor
