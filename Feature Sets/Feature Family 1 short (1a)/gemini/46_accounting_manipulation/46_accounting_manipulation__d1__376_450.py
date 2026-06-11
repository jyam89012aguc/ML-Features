"""46 accounting manipulation d1 first derivative features 376-450 â€” Pipeline 1a-HF Grade v3.

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

def f46_aman_376_accrual_v376_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=241, w2=474, w3=573, lag=0)."""
    x = _safe_log(inventory.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 241)
    baseline = trend.rolling(474, min_periods=max(474//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(573, min_periods=max(573//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.100625 + 0.0028577 * anchor
    return base_signal.diff()

def f46_aman_377_accrual_v377_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=248, w2=485, w3=586, lag=1)."""
    x = _safe_log(revenue.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 248)
    slow = _rolling_slope(x, 485)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.115 + 0.0028578 * anchor
    return base_signal.diff()

def f46_aman_378_accrual_v378_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=255, w2=496, w3=599, lag=2)."""
    x = netinc.shift(2)
    peak = x.rolling(496, min_periods=max(496//3, 2)).max()
    trough = x.rolling(255, min_periods=max(255//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.129375 + 0.0028579 * anchor
    return base_signal.diff()

def f46_aman_379_accrual_v379_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=11, w2=507, w3=612, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(11)
    rank = change.rolling(507, min_periods=max(507//3, 2)).rank(pct=True)
    persistence = change.rolling(612, min_periods=max(612//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0526 * persistence + 0.002858 * anchor
    return base_signal.diff()

def f46_aman_380_accrual_v380_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=18, w2=15, w3=625, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(18, min_periods=max(18//3, 2)).std()
    vol_slow = ret.rolling(15, min_periods=max(15//3, 2)).std()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.158125 + 0.0028581 * anchor
    return base_signal.diff()

def f46_aman_381_accrual_v381_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=25, w2=26, w3=638, lag=21)."""
    x = liabilitiesc.shift(21)
    ma = x.rolling(26, min_periods=max(26//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 25)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0678 * slope + 0.0028582 * anchor
    return base_signal.diff()

def f46_aman_382_accrual_v382_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=32, w2=37, w3=651, lag=42)."""
    x = inventory.shift(42)
    impulse = x.diff(32)
    drag = impulse.rolling(37, min_periods=max(37//3, 2)).mean()
    noise = impulse.abs().rolling(651, min_periods=max(651//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.186875 + 0.0028583 * anchor
    return base_signal.diff()

def f46_aman_383_accrual_v383_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=39, w2=48, w3=664, lag=63)."""
    x = _safe_log(revenue.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 39)
    acceleration = _rolling_slope(velocity, 48)
    curvature = _rolling_slope(acceleration, 664)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.083 * acceleration + 0.0028584 * anchor
    return base_signal.diff()

def f46_aman_384_accrual_v384_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=46, w2=59, w3=677, lag=0)."""
    rel = _safe_div(netinc.shift(0), ocf.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 46)
    pressure = rel_log.diff(59)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.0906 * pressure.rolling(677, min_periods=max(677//3, 2)).mean() + 0.0028585 * anchor
    return base_signal.diff()

def f46_aman_385_accrual_v385_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=53, w2=70, w3=690, lag=1)."""
    a = ocf.shift(1)
    b = assetsc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(53, min_periods=max(53//3, 2)).mean())
    decay = spread.ewm(span=70, adjust=False).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.23 + 0.0028586 * anchor
    return base_signal.diff()

def f46_aman_386_accrual_v386_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=60, w2=81, w3=703, lag=2)."""
    a = _safe_log(assetsc.abs() + 1.0).shift(2)
    b = _safe_log(liabilitiesc.abs() + 1.0).shift(2)
    corr = a.rolling(81, min_periods=max(81//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 60)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.244375 + 0.0028587 * anchor
    return base_signal.diff()

def f46_aman_387_accrual_v387_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=67, w2=92, w3=716, lag=5)."""
    a = liabilitiesc.shift(5)
    b = inventory.shift(5)
    cover = _safe_div(a.rolling(67, min_periods=max(67//3, 2)).mean(), b.abs().rolling(92, min_periods=max(92//3, 2)).mean())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.1134 * _rolling_slope(cover, 67) + 0.0028588 * anchor
    return base_signal.diff()

def f46_aman_388_accrual_v388_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=74, w2=103, w3=729, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    y = _safe_log(revenue.abs() + 1.0).shift(10)
    z = _safe_log(revenue.abs() + 1.0).shift(10)
    basket = x - 0.121 * y + 0.879000 * z
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 74) - _rolling_slope(basket, 103) + 0.0028589 * anchor
    return base_signal.diff()

def f46_aman_389_accrual_v389_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=81, w2=114, w3=742, lag=21)."""
    x = revenue.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(81, min_periods=max(81//3, 2)).mean(), upside.rolling(114, min_periods=max(114//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.2875 + 0.002859 * anchor
    return base_signal.diff()

def f46_aman_390_accrual_v390_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=88, w2=125, w3=755, lag=42)."""
    x = _safe_log(netinc.abs() + 1.0).shift(42)
    draw = x - x.rolling(125, min_periods=max(125//3, 2)).max()
    rebound = x - x.rolling(88, min_periods=max(88//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1362 * _rolling_slope(draw, 755) + 0.0028591 * anchor
    return base_signal.diff()

def f46_aman_391_accrual_v391_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=95, w2=136, w3=768, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(95) - b.diff(126)
    stress = imbalance.rolling(768, min_periods=max(768//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.31625 + 0.0028592 * anchor
    return base_signal.diff()

def f46_aman_392_accrual_v392_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=102, w2=147, w3=24, lag=0)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 102)
    baseline = trend.rolling(147, min_periods=max(147//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(24, min_periods=max(24//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.330625 + 0.0028593 * anchor
    return base_signal.diff()

def f46_aman_393_accrual_v393_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=109, w2=158, w3=37, lag=1)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 109)
    slow = _rolling_slope(x, 158)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=37, adjust=False).mean() * 1.345 + 0.0028594 * anchor
    return base_signal.diff()

def f46_aman_394_accrual_v394_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=116, w2=169, w3=50, lag=2)."""
    x = inventory.shift(2)
    peak = x.rolling(169, min_periods=max(169//3, 2)).max()
    trough = x.rolling(116, min_periods=max(116//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.359375 + 0.0028595 * anchor
    return base_signal.diff()

def f46_aman_395_accrual_v395_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=123, w2=180, w3=63, lag=5)."""
    x = revenue.shift(5)
    change = x.pct_change(123)
    rank = change.rolling(180, min_periods=max(180//3, 2)).rank(pct=True)
    persistence = change.rolling(63, min_periods=max(63//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1742 * persistence + 0.0028596 * anchor
    return base_signal.diff()

def f46_aman_396_accrual_v396_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=130, w2=191, w3=76, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(130, min_periods=max(130//3, 2)).std()
    vol_slow = ret.rolling(191, min_periods=max(191//3, 2)).std()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.388125 + 0.0028597 * anchor
    return base_signal.diff()

def f46_aman_397_accrual_v397_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=137, w2=202, w3=89, lag=21)."""
    x = ocf.shift(21)
    ma = x.rolling(202, min_periods=max(202//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 137)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1894 * slope + 0.0028598 * anchor
    return base_signal.diff()

def f46_aman_398_accrual_v398_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=144, w2=213, w3=102, lag=42)."""
    x = assetsc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(213, min_periods=max(213//3, 2)).mean()
    noise = impulse.abs().rolling(102, min_periods=max(102//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.416875 + 0.0028599 * anchor
    return base_signal.diff()

def f46_aman_399_accrual_v399_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=151, w2=224, w3=115, lag=63)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 151)
    acceleration = _rolling_slope(velocity, 224)
    curvature = _rolling_slope(acceleration, 115)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2046 * acceleration + 0.00286 * anchor
    return base_signal.diff()

def f46_aman_400_accrual_v400_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=158, w2=235, w3=128, lag=0)."""
    rel = _safe_div(inventory.shift(0), revenue.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 158)
    pressure = rel_log.diff(126)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.2122 * pressure.rolling(128, min_periods=max(128//3, 2)).mean() + 0.0028601 * anchor
    return base_signal.diff()

def f46_aman_401_accrual_v401_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=165, w2=246, w3=141, lag=1)."""
    a = revenue.shift(1)
    b = netinc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(165, min_periods=max(165//3, 2)).mean())
    decay = spread.ewm(span=246, adjust=False).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.46 + 0.0028602 * anchor
    return base_signal.diff()

def f46_aman_402_accrual_v402_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=172, w2=257, w3=154, lag=2)."""
    a = _safe_log(netinc.abs() + 1.0).shift(2)
    b = _safe_log(ocf.abs() + 1.0).shift(2)
    corr = a.rolling(257, min_periods=max(257//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 172)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.474375 + 0.0028603 * anchor
    return base_signal.diff()

def f46_aman_403_accrual_v403_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=179, w2=268, w3=167, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(179, min_periods=max(179//3, 2)).mean(), b.abs().rolling(268, min_periods=max(268//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.235 * _rolling_slope(cover, 179) + 0.0028604 * anchor
    return base_signal.diff()

def f46_aman_404_accrual_v404_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=186, w2=279, w3=180, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    y = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    z = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    basket = x - 0.2426 * y + 0.757400 * z
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 186) - _rolling_slope(basket, 279) + 0.0028605 * anchor
    return base_signal.diff()

def f46_aman_405_accrual_v405_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=193, w2=290, w3=193, lag=21)."""
    x = liabilitiesc.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(193, min_periods=max(193//3, 2)).mean(), upside.rolling(290, min_periods=max(290//3, 2)).mean().abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.5175 + 0.0028606 * anchor
    return base_signal.diff()

def f46_aman_406_accrual_v406_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=200, w2=301, w3=206, lag=42)."""
    x = _safe_log(inventory.abs() + 1.0).shift(42)
    draw = x - x.rolling(301, min_periods=max(301//3, 2)).max()
    rebound = x - x.rolling(200, min_periods=max(200//3, 2)).min()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2578 * _rolling_slope(draw, 206) + 0.0028607 * anchor
    return base_signal.diff()

def f46_aman_407_accrual_v407_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=207, w2=312, w3=219, lag=63)."""
    a = _safe_log(revenue.abs() + 1.0).shift(63)
    b = _safe_log(netinc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(219, min_periods=max(219//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.54625 + 0.0028608 * anchor
    return base_signal.diff()

def f46_aman_408_accrual_v408_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=214, w2=323, w3=232, lag=0)."""
    x = _safe_log(netinc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 214)
    baseline = trend.rolling(323, min_periods=max(323//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(232, min_periods=max(232//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.560625 + 0.0028609 * anchor
    return base_signal.diff()

def f46_aman_409_accrual_v409_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=221, w2=334, w3=245, lag=1)."""
    x = _safe_log(ocf.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 221)
    slow = _rolling_slope(x, 334)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=245, adjust=False).mean() * 1.575 + 0.002861 * anchor
    return base_signal.diff()

def f46_aman_410_accrual_v410_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=228, w2=345, w3=258, lag=2)."""
    x = assetsc.shift(2)
    peak = x.rolling(345, min_periods=max(345//3, 2)).max()
    trough = x.rolling(228, min_periods=max(228//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.589375 + 0.0028611 * anchor
    return base_signal.diff()

def f46_aman_411_accrual_v411_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=235, w2=356, w3=271, lag=5)."""
    x = liabilitiesc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(356, min_periods=max(356//3, 2)).rank(pct=True)
    persistence = change.rolling(271, min_periods=max(271//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2958 * persistence + 0.0028612 * anchor
    return base_signal.diff()

def f46_aman_412_accrual_v412_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=242, w2=367, w3=284, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(242, min_periods=max(242//3, 2)).std()
    vol_slow = ret.rolling(367, min_periods=max(367//3, 2)).std()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.618125 + 0.0028613 * anchor
    return base_signal.diff()

def f46_aman_413_accrual_v413_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=249, w2=378, w3=297, lag=21)."""
    x = revenue.shift(21)
    ma = x.rolling(378, min_periods=max(378//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 249)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.311 * slope + 0.0028614 * anchor
    return base_signal.diff()

def f46_aman_414_accrual_v414_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=5, w2=389, w3=310, lag=42)."""
    x = netinc.shift(42)
    impulse = x.diff(5)
    drag = impulse.rolling(389, min_periods=max(389//3, 2)).mean()
    noise = impulse.abs().rolling(310, min_periods=max(310//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.87375 + 0.0028615 * anchor
    return base_signal.diff()

def f46_aman_415_accrual_v415_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=12, w2=400, w3=323, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 12)
    acceleration = _rolling_slope(velocity, 400)
    curvature = _rolling_slope(acceleration, 323)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3262 * acceleration + 0.0028616 * anchor
    return base_signal.diff()

def f46_aman_416_accrual_v416_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=19, w2=411, w3=336, lag=0)."""
    rel = _safe_div(assetsc.shift(0), liabilitiesc.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 19)
    pressure = rel_log.diff(126)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.3338 * pressure.rolling(336, min_periods=max(336//3, 2)).mean() + 0.0028617 * anchor
    return base_signal.diff()

def f46_aman_417_accrual_v417_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=26, w2=422, w3=349, lag=1)."""
    a = liabilitiesc.shift(1)
    b = inventory.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(26, min_periods=max(26//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.916875 + 0.0028618 * anchor
    return base_signal.diff()

def f46_aman_418_accrual_v418_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=33, w2=433, w3=362, lag=2)."""
    a = _safe_log(inventory.abs() + 1.0).shift(2)
    b = _safe_log(revenue.abs() + 1.0).shift(2)
    corr = a.rolling(433, min_periods=max(433//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 33)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.93125 + 0.0028619 * anchor
    return base_signal.diff()

def f46_aman_419_accrual_v419_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=40, w2=444, w3=375, lag=5)."""
    a = revenue.shift(5)
    b = netinc.shift(5)
    cover = _safe_div(a.rolling(40, min_periods=max(40//3, 2)).mean(), b.abs().rolling(444, min_periods=max(444//3, 2)).mean())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.3566 * _rolling_slope(cover, 40) + 0.002862 * anchor
    return base_signal.diff()

def f46_aman_420_accrual_v420_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=47, w2=455, w3=388, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    y = _safe_log(ocf.abs() + 1.0).shift(10)
    z = _safe_log(ocf.abs() + 1.0).shift(10)
    basket = x - 0.3642 * y + 0.635800 * z
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 47) - _rolling_slope(basket, 455) + 0.0028621 * anchor
    return base_signal.diff()

def f46_aman_421_accrual_v421_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=54, w2=466, w3=401, lag=21)."""
    x = ocf.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(54, min_periods=max(54//3, 2)).mean(), upside.rolling(466, min_periods=max(466//3, 2)).mean().abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.974375 + 0.0028622 * anchor
    return base_signal.diff()

def f46_aman_422_accrual_v422_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=61, w2=477, w3=414, lag=42)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(42)
    draw = x - x.rolling(477, min_periods=max(477//3, 2)).max()
    rebound = x - x.rolling(61, min_periods=max(61//3, 2)).min()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3794 * _rolling_slope(draw, 414) + 0.0028623 * anchor
    return base_signal.diff()

def f46_aman_423_accrual_v423_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=68, w2=488, w3=427, lag=63)."""
    a = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    b = _safe_log(inventory.abs() + 1.0).shift(63)
    imbalance = a.diff(68) - b.diff(126)
    stress = imbalance.rolling(427, min_periods=max(427//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.003125 + 0.0028624 * anchor
    return base_signal.diff()

def f46_aman_424_accrual_v424_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=75, w2=499, w3=440, lag=0)."""
    x = _safe_log(inventory.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 75)
    baseline = trend.rolling(499, min_periods=max(499//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(440, min_periods=max(440//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.0175 + 0.0028625 * anchor
    return base_signal.diff()

def f46_aman_425_accrual_v425_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=82, w2=510, w3=453, lag=1)."""
    x = _safe_log(revenue.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 82)
    slow = _rolling_slope(x, 510)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.031875 + 0.0028626 * anchor
    return base_signal.diff()

def f46_aman_426_accrual_v426_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=89, w2=18, w3=466, lag=2)."""
    x = netinc.shift(2)
    peak = x.rolling(18, min_periods=max(18//3, 2)).max()
    trough = x.rolling(89, min_periods=max(89//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.04625 + 0.0028627 * anchor
    return base_signal.diff()

def f46_aman_427_accrual_v427_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=96, w2=29, w3=479, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(96)
    rank = change.rolling(29, min_periods=max(29//3, 2)).rank(pct=True)
    persistence = change.rolling(479, min_periods=max(479//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.041 * persistence + 0.0028628 * anchor
    return base_signal.diff()

def f46_aman_428_accrual_v428_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=103, w2=40, w3=492, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(103, min_periods=max(103//3, 2)).std()
    vol_slow = ret.rolling(40, min_periods=max(40//3, 2)).std()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.075 + 0.0028629 * anchor
    return base_signal.diff()

def f46_aman_429_accrual_v429_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=110, w2=51, w3=505, lag=21)."""
    x = liabilitiesc.shift(21)
    ma = x.rolling(51, min_periods=max(51//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 110)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0562 * slope + 0.002863 * anchor
    return base_signal.diff()

def f46_aman_430_accrual_v430_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=117, w2=62, w3=518, lag=42)."""
    x = inventory.shift(42)
    impulse = x.diff(117)
    drag = impulse.rolling(62, min_periods=max(62//3, 2)).mean()
    noise = impulse.abs().rolling(518, min_periods=max(518//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.10375 + 0.0028631 * anchor
    return base_signal.diff()

def f46_aman_431_accrual_v431_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=124, w2=73, w3=531, lag=63)."""
    x = _safe_log(revenue.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 124)
    acceleration = _rolling_slope(velocity, 73)
    curvature = _rolling_slope(acceleration, 531)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0714 * acceleration + 0.0028632 * anchor
    return base_signal.diff()

def f46_aman_432_accrual_v432_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=131, w2=84, w3=544, lag=0)."""
    rel = _safe_div(netinc.shift(0), ocf.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 131)
    pressure = rel_log.diff(84)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.079 * pressure.rolling(544, min_periods=max(544//3, 2)).mean() + 0.0028633 * anchor
    return base_signal.diff()

def f46_aman_433_accrual_v433_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=138, w2=95, w3=557, lag=1)."""
    a = ocf.shift(1)
    b = assetsc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(138, min_periods=max(138//3, 2)).mean())
    decay = spread.ewm(span=95, adjust=False).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.146875 + 0.0028634 * anchor
    return base_signal.diff()

def f46_aman_434_accrual_v434_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=145, w2=106, w3=570, lag=2)."""
    a = _safe_log(assetsc.abs() + 1.0).shift(2)
    b = _safe_log(liabilitiesc.abs() + 1.0).shift(2)
    corr = a.rolling(106, min_periods=max(106//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 145)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.16125 + 0.0028635 * anchor
    return base_signal.diff()

def f46_aman_435_accrual_v435_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=152, w2=117, w3=583, lag=5)."""
    a = liabilitiesc.shift(5)
    b = inventory.shift(5)
    cover = _safe_div(a.rolling(152, min_periods=max(152//3, 2)).mean(), b.abs().rolling(117, min_periods=max(117//3, 2)).mean())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.1018 * _rolling_slope(cover, 152) + 0.0028636 * anchor
    return base_signal.diff()

def f46_aman_436_accrual_v436_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=159, w2=128, w3=596, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    y = _safe_log(revenue.abs() + 1.0).shift(10)
    z = _safe_log(revenue.abs() + 1.0).shift(10)
    basket = x - 0.1094 * y + 0.890600 * z
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 159) - _rolling_slope(basket, 128) + 0.0028637 * anchor
    return base_signal.diff()

def f46_aman_437_accrual_v437_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=166, w2=139, w3=609, lag=21)."""
    x = revenue.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(166, min_periods=max(166//3, 2)).mean(), upside.rolling(139, min_periods=max(139//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.204375 + 0.0028638 * anchor
    return base_signal.diff()

def f46_aman_438_accrual_v438_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=173, w2=150, w3=622, lag=42)."""
    x = _safe_log(netinc.abs() + 1.0).shift(42)
    draw = x - x.rolling(150, min_periods=max(150//3, 2)).max()
    rebound = x - x.rolling(173, min_periods=max(173//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1246 * _rolling_slope(draw, 622) + 0.0028639 * anchor
    return base_signal.diff()

def f46_aman_439_accrual_v439_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=180, w2=161, w3=635, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(635, min_periods=max(635//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.233125 + 0.002864 * anchor
    return base_signal.diff()

def f46_aman_440_accrual_v440_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=187, w2=172, w3=648, lag=0)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 187)
    baseline = trend.rolling(172, min_periods=max(172//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(648, min_periods=max(648//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.2475 + 0.0028641 * anchor
    return base_signal.diff()

def f46_aman_441_accrual_v441_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=194, w2=183, w3=661, lag=1)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 194)
    slow = _rolling_slope(x, 183)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.261875 + 0.0028642 * anchor
    return base_signal.diff()

def f46_aman_442_accrual_v442_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=201, w2=194, w3=674, lag=2)."""
    x = inventory.shift(2)
    peak = x.rolling(194, min_periods=max(194//3, 2)).max()
    trough = x.rolling(201, min_periods=max(201//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.27625 + 0.0028643 * anchor
    return base_signal.diff()

def f46_aman_443_accrual_v443_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=208, w2=205, w3=687, lag=5)."""
    x = revenue.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(205, min_periods=max(205//3, 2)).rank(pct=True)
    persistence = change.rolling(687, min_periods=max(687//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1626 * persistence + 0.0028644 * anchor
    return base_signal.diff()

def f46_aman_444_accrual_v444_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=215, w2=216, w3=700, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(215, min_periods=max(215//3, 2)).std()
    vol_slow = ret.rolling(216, min_periods=max(216//3, 2)).std()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.305 + 0.0028645 * anchor
    return base_signal.diff()

def f46_aman_445_accrual_v445_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=222, w2=227, w3=713, lag=21)."""
    x = ocf.shift(21)
    ma = x.rolling(227, min_periods=max(227//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 222)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1778 * slope + 0.0028646 * anchor
    return base_signal.diff()

def f46_aman_446_accrual_v446_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=229, w2=238, w3=726, lag=42)."""
    x = assetsc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(238, min_periods=max(238//3, 2)).mean()
    noise = impulse.abs().rolling(726, min_periods=max(726//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.33375 + 0.0028647 * anchor
    return base_signal.diff()

def f46_aman_447_accrual_v447_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=236, w2=249, w3=739, lag=63)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 236)
    acceleration = _rolling_slope(velocity, 249)
    curvature = _rolling_slope(acceleration, 739)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.193 * acceleration + 0.0028648 * anchor
    return base_signal.diff()

def f46_aman_448_accrual_v448_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=243, w2=260, w3=752, lag=0)."""
    rel = _safe_div(inventory.shift(0), revenue.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 243)
    pressure = rel_log.diff(126)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.2006 * pressure.rolling(752, min_periods=max(752//3, 2)).mean() + 0.0028649 * anchor
    return base_signal.diff()

def f46_aman_449_accrual_v449_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=250, w2=271, w3=765, lag=1)."""
    a = revenue.shift(1)
    b = netinc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(250, min_periods=max(250//3, 2)).mean())
    decay = spread.ewm(span=271, adjust=False).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.376875 + 0.002865 * anchor
    return base_signal.diff()

def f46_aman_450_accrual_v450_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=6, w2=282, w3=21, lag=2)."""
    a = _safe_log(netinc.abs() + 1.0).shift(2)
    b = _safe_log(ocf.abs() + 1.0).shift(2)
    corr = a.rolling(282, min_periods=max(282//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 6)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.39125 + 0.0028651 * anchor
    return base_signal.diff()
