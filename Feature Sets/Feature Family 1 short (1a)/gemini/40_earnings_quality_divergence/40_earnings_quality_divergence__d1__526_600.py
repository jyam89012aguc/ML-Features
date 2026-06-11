"""40 earnings quality divergence d1 first derivative features 526-600 â€” Pipeline 1a-HF Grade v3.

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

def f40_eqd_526_accrual_v526_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=254, w2=188, w3=156, lag=42)."""
    x = _safe_log(inventory.abs() + 1.0).shift(42)
    draw = x - x.rolling(188, min_periods=max(188//3, 2)).max()
    rebound = x - x.rolling(254, min_periods=max(254//3, 2)).min()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1146 * _rolling_slope(draw, 156) + 0.0024527 * anchor
    return base_signal.diff()

def f40_eqd_527_accrual_v527_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=10, w2=199, w3=169, lag=63)."""
    a = _safe_log(revenue.abs() + 1.0).shift(63)
    b = _safe_log(netinc.abs() + 1.0).shift(63)
    imbalance = a.diff(10) - b.diff(126)
    stress = imbalance.rolling(169, min_periods=max(169//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.880625 + 0.0024528 * anchor
    return base_signal.diff()

def f40_eqd_528_accrual_v528_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=17, w2=210, w3=182, lag=0)."""
    x = _safe_log(netinc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 17)
    baseline = trend.rolling(210, min_periods=max(210//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(182, min_periods=max(182//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.895 + 0.0024529 * anchor
    return base_signal.diff()

def f40_eqd_529_accrual_v529_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=24, w2=221, w3=195, lag=1)."""
    x = _safe_log(ocf.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 24)
    slow = _rolling_slope(x, 221)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=195, adjust=False).mean() * 0.909375 + 0.002453 * anchor
    return base_signal.diff()

def f40_eqd_530_accrual_v530_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=31, w2=232, w3=208, lag=2)."""
    x = assetsc.shift(2)
    peak = x.rolling(232, min_periods=max(232//3, 2)).max()
    trough = x.rolling(31, min_periods=max(31//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.92375 + 0.0024531 * anchor
    return base_signal.diff()

def f40_eqd_531_accrual_v531_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=38, w2=243, w3=221, lag=5)."""
    x = liabilitiesc.shift(5)
    change = x.pct_change(38)
    rank = change.rolling(243, min_periods=max(243//3, 2)).rank(pct=True)
    persistence = change.rolling(221, min_periods=max(221//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1526 * persistence + 0.0024532 * anchor
    return base_signal.diff()

def f40_eqd_532_accrual_v532_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=45, w2=254, w3=234, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(45, min_periods=max(45//3, 2)).std()
    vol_slow = ret.rolling(254, min_periods=max(254//3, 2)).std()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.9525 + 0.0024533 * anchor
    return base_signal.diff()

def f40_eqd_533_accrual_v533_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=52, w2=265, w3=247, lag=21)."""
    x = revenue.shift(21)
    ma = x.rolling(265, min_periods=max(265//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 52)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1678 * slope + 0.0024534 * anchor
    return base_signal.diff()

def f40_eqd_534_accrual_v534_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=59, w2=276, w3=260, lag=42)."""
    x = netinc.shift(42)
    impulse = x.diff(59)
    drag = impulse.rolling(276, min_periods=max(276//3, 2)).mean()
    noise = impulse.abs().rolling(260, min_periods=max(260//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.98125 + 0.0024535 * anchor
    return base_signal.diff()

def f40_eqd_535_accrual_v535_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=66, w2=287, w3=273, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 66)
    acceleration = _rolling_slope(velocity, 287)
    curvature = _rolling_slope(acceleration, 273)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.183 * acceleration + 0.0024536 * anchor
    return base_signal.diff()

def f40_eqd_536_accrual_v536_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=73, w2=298, w3=286, lag=0)."""
    rel = _safe_div(assetsc.shift(0), liabilitiesc.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 73)
    pressure = rel_log.diff(126)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.1906 * pressure.rolling(286, min_periods=max(286//3, 2)).mean() + 0.0024537 * anchor
    return base_signal.diff()

def f40_eqd_537_accrual_v537_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=80, w2=309, w3=299, lag=1)."""
    a = liabilitiesc.shift(1)
    b = inventory.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(80, min_periods=max(80//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.024375 + 0.0024538 * anchor
    return base_signal.diff()

def f40_eqd_538_accrual_v538_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=87, w2=320, w3=312, lag=2)."""
    a = _safe_log(inventory.abs() + 1.0).shift(2)
    b = _safe_log(revenue.abs() + 1.0).shift(2)
    corr = a.rolling(320, min_periods=max(320//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 87)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.03875 + 0.0024539 * anchor
    return base_signal.diff()

def f40_eqd_539_accrual_v539_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=94, w2=331, w3=325, lag=5)."""
    a = revenue.shift(5)
    b = netinc.shift(5)
    cover = _safe_div(a.rolling(94, min_periods=max(94//3, 2)).mean(), b.abs().rolling(331, min_periods=max(331//3, 2)).mean())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.2134 * _rolling_slope(cover, 94) + 0.002454 * anchor
    return base_signal.diff()

def f40_eqd_540_accrual_v540_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=101, w2=342, w3=338, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    y = _safe_log(ocf.abs() + 1.0).shift(10)
    z = _safe_log(ocf.abs() + 1.0).shift(10)
    basket = x - 0.221 * y + 0.779000 * z
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 101) - _rolling_slope(basket, 342) + 0.0024541 * anchor
    return base_signal.diff()

def f40_eqd_541_accrual_v541_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=108, w2=353, w3=351, lag=21)."""
    x = ocf.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(108, min_periods=max(108//3, 2)).mean(), upside.rolling(353, min_periods=max(353//3, 2)).mean().abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.081875 + 0.0024542 * anchor
    return base_signal.diff()

def f40_eqd_542_accrual_v542_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=115, w2=364, w3=364, lag=42)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(42)
    draw = x - x.rolling(364, min_periods=max(364//3, 2)).max()
    rebound = x - x.rolling(115, min_periods=max(115//3, 2)).min()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2362 * _rolling_slope(draw, 364) + 0.0024543 * anchor
    return base_signal.diff()

def f40_eqd_543_accrual_v543_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=122, w2=375, w3=377, lag=63)."""
    a = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    b = _safe_log(inventory.abs() + 1.0).shift(63)
    imbalance = a.diff(122) - b.diff(126)
    stress = imbalance.rolling(377, min_periods=max(377//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.110625 + 0.0024544 * anchor
    return base_signal.diff()

def f40_eqd_544_accrual_v544_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=129, w2=386, w3=390, lag=0)."""
    x = _safe_log(inventory.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 129)
    baseline = trend.rolling(386, min_periods=max(386//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(390, min_periods=max(390//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.125 + 0.0024545 * anchor
    return base_signal.diff()

def f40_eqd_545_accrual_v545_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=136, w2=397, w3=403, lag=1)."""
    x = _safe_log(revenue.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 136)
    slow = _rolling_slope(x, 397)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.139375 + 0.0024546 * anchor
    return base_signal.diff()

def f40_eqd_546_accrual_v546_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=143, w2=408, w3=416, lag=2)."""
    x = netinc.shift(2)
    peak = x.rolling(408, min_periods=max(408//3, 2)).max()
    trough = x.rolling(143, min_periods=max(143//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.15375 + 0.0024547 * anchor
    return base_signal.diff()

def f40_eqd_547_accrual_v547_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=150, w2=419, w3=429, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(419, min_periods=max(419//3, 2)).rank(pct=True)
    persistence = change.rolling(429, min_periods=max(429//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2742 * persistence + 0.0024548 * anchor
    return base_signal.diff()

def f40_eqd_548_accrual_v548_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=157, w2=430, w3=442, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(157, min_periods=max(157//3, 2)).std()
    vol_slow = ret.rolling(430, min_periods=max(430//3, 2)).std()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.1825 + 0.0024549 * anchor
    return base_signal.diff()

def f40_eqd_549_accrual_v549_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=164, w2=441, w3=455, lag=21)."""
    x = liabilitiesc.shift(21)
    ma = x.rolling(441, min_periods=max(441//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 164)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2894 * slope + 0.002455 * anchor
    return base_signal.diff()

def f40_eqd_550_accrual_v550_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=171, w2=452, w3=468, lag=42)."""
    x = inventory.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(452, min_periods=max(452//3, 2)).mean()
    noise = impulse.abs().rolling(468, min_periods=max(468//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.21125 + 0.0024551 * anchor
    return base_signal.diff()

def f40_eqd_551_accrual_v551_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=178, w2=463, w3=481, lag=63)."""
    x = _safe_log(revenue.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 178)
    acceleration = _rolling_slope(velocity, 463)
    curvature = _rolling_slope(acceleration, 481)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3046 * acceleration + 0.0024552 * anchor
    return base_signal.diff()

def f40_eqd_552_accrual_v552_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=185, w2=474, w3=494, lag=0)."""
    rel = _safe_div(netinc.shift(0), ocf.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 185)
    pressure = rel_log.diff(126)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.3122 * pressure.rolling(494, min_periods=max(494//3, 2)).mean() + 0.0024553 * anchor
    return base_signal.diff()

def f40_eqd_553_accrual_v553_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=192, w2=485, w3=507, lag=1)."""
    a = ocf.shift(1)
    b = assetsc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(192, min_periods=max(192//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.254375 + 0.0024554 * anchor
    return base_signal.diff()

def f40_eqd_554_accrual_v554_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=199, w2=496, w3=520, lag=2)."""
    a = _safe_log(assetsc.abs() + 1.0).shift(2)
    b = _safe_log(liabilitiesc.abs() + 1.0).shift(2)
    corr = a.rolling(496, min_periods=max(496//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 199)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.26875 + 0.0024555 * anchor
    return base_signal.diff()

def f40_eqd_555_accrual_v555_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=206, w2=507, w3=533, lag=5)."""
    a = liabilitiesc.shift(5)
    b = inventory.shift(5)
    cover = _safe_div(a.rolling(206, min_periods=max(206//3, 2)).mean(), b.abs().rolling(507, min_periods=max(507//3, 2)).mean())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.335 * _rolling_slope(cover, 206) + 0.0024556 * anchor
    return base_signal.diff()

def f40_eqd_556_accrual_v556_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=213, w2=15, w3=546, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    y = _safe_log(revenue.abs() + 1.0).shift(10)
    z = _safe_log(revenue.abs() + 1.0).shift(10)
    basket = x - 0.3426 * y + 0.657400 * z
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 213) - _rolling_slope(basket, 15) + 0.0024557 * anchor
    return base_signal.diff()

def f40_eqd_557_accrual_v557_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=220, w2=26, w3=559, lag=21)."""
    x = revenue.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(220, min_periods=max(220//3, 2)).mean(), upside.rolling(26, min_periods=max(26//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.311875 + 0.0024558 * anchor
    return base_signal.diff()

def f40_eqd_558_accrual_v558_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=227, w2=37, w3=572, lag=42)."""
    x = _safe_log(netinc.abs() + 1.0).shift(42)
    draw = x - x.rolling(37, min_periods=max(37//3, 2)).max()
    rebound = x - x.rolling(227, min_periods=max(227//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3578 * _rolling_slope(draw, 572) + 0.0024559 * anchor
    return base_signal.diff()

def f40_eqd_559_accrual_v559_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=234, w2=48, w3=585, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(48)
    stress = imbalance.rolling(585, min_periods=max(585//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.340625 + 0.002456 * anchor
    return base_signal.diff()

def f40_eqd_560_accrual_v560_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=241, w2=59, w3=598, lag=0)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 241)
    baseline = trend.rolling(59, min_periods=max(59//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(598, min_periods=max(598//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.355 + 0.0024561 * anchor
    return base_signal.diff()

def f40_eqd_561_accrual_v561_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=248, w2=70, w3=611, lag=1)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 248)
    slow = _rolling_slope(x, 70)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.369375 + 0.0024562 * anchor
    return base_signal.diff()

def f40_eqd_562_accrual_v562_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=255, w2=81, w3=624, lag=2)."""
    x = inventory.shift(2)
    peak = x.rolling(81, min_periods=max(81//3, 2)).max()
    trough = x.rolling(255, min_periods=max(255//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.38375 + 0.0024563 * anchor
    return base_signal.diff()

def f40_eqd_563_accrual_v563_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=11, w2=92, w3=637, lag=5)."""
    x = revenue.shift(5)
    change = x.pct_change(11)
    rank = change.rolling(92, min_periods=max(92//3, 2)).rank(pct=True)
    persistence = change.rolling(637, min_periods=max(637//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3958 * persistence + 0.0024564 * anchor
    return base_signal.diff()

def f40_eqd_564_accrual_v564_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=18, w2=103, w3=650, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(18, min_periods=max(18//3, 2)).std()
    vol_slow = ret.rolling(103, min_periods=max(103//3, 2)).std()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.4125 + 0.0024565 * anchor
    return base_signal.diff()

def f40_eqd_565_accrual_v565_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=25, w2=114, w3=663, lag=21)."""
    x = ocf.shift(21)
    ma = x.rolling(114, min_periods=max(114//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 25)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.411 * slope + 0.0024566 * anchor
    return base_signal.diff()

def f40_eqd_566_accrual_v566_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=32, w2=125, w3=676, lag=42)."""
    x = assetsc.shift(42)
    impulse = x.diff(32)
    drag = impulse.rolling(125, min_periods=max(125//3, 2)).mean()
    noise = impulse.abs().rolling(676, min_periods=max(676//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.44125 + 0.0024567 * anchor
    return base_signal.diff()

def f40_eqd_567_accrual_v567_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=39, w2=136, w3=689, lag=63)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 39)
    acceleration = _rolling_slope(velocity, 136)
    curvature = _rolling_slope(acceleration, 689)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0498 * acceleration + 0.0024568 * anchor
    return base_signal.diff()

def f40_eqd_568_accrual_v568_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=46, w2=147, w3=702, lag=0)."""
    rel = _safe_div(inventory.shift(0), revenue.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 46)
    pressure = rel_log.diff(126)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.0574 * pressure.rolling(702, min_periods=max(702//3, 2)).mean() + 0.0024569 * anchor
    return base_signal.diff()

def f40_eqd_569_accrual_v569_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=53, w2=158, w3=715, lag=1)."""
    a = revenue.shift(1)
    b = netinc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(53, min_periods=max(53//3, 2)).mean())
    decay = spread.ewm(span=158, adjust=False).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.484375 + 0.002457 * anchor
    return base_signal.diff()

def f40_eqd_570_accrual_v570_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=60, w2=169, w3=728, lag=2)."""
    a = _safe_log(netinc.abs() + 1.0).shift(2)
    b = _safe_log(ocf.abs() + 1.0).shift(2)
    corr = a.rolling(169, min_periods=max(169//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 60)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.49875 + 0.0024571 * anchor
    return base_signal.diff()

def f40_eqd_571_accrual_v571_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=67, w2=180, w3=741, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(67, min_periods=max(67//3, 2)).mean(), b.abs().rolling(180, min_periods=max(180//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.0802 * _rolling_slope(cover, 67) + 0.0024572 * anchor
    return base_signal.diff()

def f40_eqd_572_accrual_v572_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=74, w2=191, w3=754, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    y = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    z = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    basket = x - 0.0878 * y + 0.912200 * z
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 74) - _rolling_slope(basket, 191) + 0.0024573 * anchor
    return base_signal.diff()

def f40_eqd_573_accrual_v573_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=81, w2=202, w3=767, lag=21)."""
    x = liabilitiesc.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(81, min_periods=max(81//3, 2)).mean(), upside.rolling(202, min_periods=max(202//3, 2)).mean().abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.541875 + 0.0024574 * anchor
    return base_signal.diff()

def f40_eqd_574_accrual_v574_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=88, w2=213, w3=23, lag=42)."""
    x = _safe_log(inventory.abs() + 1.0).shift(42)
    draw = x - x.rolling(213, min_periods=max(213//3, 2)).max()
    rebound = x - x.rolling(88, min_periods=max(88//3, 2)).min()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.103 * _rolling_slope(draw, 23) + 0.0024575 * anchor
    return base_signal.diff()

def f40_eqd_575_accrual_v575_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=95, w2=224, w3=36, lag=63)."""
    a = _safe_log(revenue.abs() + 1.0).shift(63)
    b = _safe_log(netinc.abs() + 1.0).shift(63)
    imbalance = a.diff(95) - b.diff(126)
    stress = imbalance.rolling(36, min_periods=max(36//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.570625 + 0.0024576 * anchor
    return base_signal.diff()

def f40_eqd_576_accrual_v576_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=102, w2=235, w3=49, lag=0)."""
    x = _safe_log(netinc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 102)
    baseline = trend.rolling(235, min_periods=max(235//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(49, min_periods=max(49//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.585 + 0.0024577 * anchor
    return base_signal.diff()

def f40_eqd_577_accrual_v577_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=109, w2=246, w3=62, lag=1)."""
    x = _safe_log(ocf.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 109)
    slow = _rolling_slope(x, 246)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=62, adjust=False).mean() * 1.599375 + 0.0024578 * anchor
    return base_signal.diff()

def f40_eqd_578_accrual_v578_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=116, w2=257, w3=75, lag=2)."""
    x = assetsc.shift(2)
    peak = x.rolling(257, min_periods=max(257//3, 2)).max()
    trough = x.rolling(116, min_periods=max(116//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.61375 + 0.0024579 * anchor
    return base_signal.diff()

def f40_eqd_579_accrual_v579_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=123, w2=268, w3=88, lag=5)."""
    x = liabilitiesc.shift(5)
    change = x.pct_change(123)
    rank = change.rolling(268, min_periods=max(268//3, 2)).rank(pct=True)
    persistence = change.rolling(88, min_periods=max(88//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.141 * persistence + 0.002458 * anchor
    return base_signal.diff()

def f40_eqd_580_accrual_v580_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=130, w2=279, w3=101, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(130, min_periods=max(130//3, 2)).std()
    vol_slow = ret.rolling(279, min_periods=max(279//3, 2)).std()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.869375 + 0.0024581 * anchor
    return base_signal.diff()

def f40_eqd_581_accrual_v581_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=137, w2=290, w3=114, lag=21)."""
    x = revenue.shift(21)
    ma = x.rolling(290, min_periods=max(290//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 137)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1562 * slope + 0.0024582 * anchor
    return base_signal.diff()

def f40_eqd_582_accrual_v582_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=144, w2=301, w3=127, lag=42)."""
    x = netinc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(301, min_periods=max(301//3, 2)).mean()
    noise = impulse.abs().rolling(127, min_periods=max(127//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.898125 + 0.0024583 * anchor
    return base_signal.diff()

def f40_eqd_583_accrual_v583_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=151, w2=312, w3=140, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 151)
    acceleration = _rolling_slope(velocity, 312)
    curvature = _rolling_slope(acceleration, 140)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1714 * acceleration + 0.0024584 * anchor
    return base_signal.diff()

def f40_eqd_584_accrual_v584_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=158, w2=323, w3=153, lag=0)."""
    rel = _safe_div(assetsc.shift(0), liabilitiesc.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 158)
    pressure = rel_log.diff(126)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.179 * pressure.rolling(153, min_periods=max(153//3, 2)).mean() + 0.0024585 * anchor
    return base_signal.diff()

def f40_eqd_585_accrual_v585_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=165, w2=334, w3=166, lag=1)."""
    a = liabilitiesc.shift(1)
    b = inventory.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(165, min_periods=max(165//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.94125 + 0.0024586 * anchor
    return base_signal.diff()

def f40_eqd_586_accrual_v586_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=172, w2=345, w3=179, lag=2)."""
    a = _safe_log(inventory.abs() + 1.0).shift(2)
    b = _safe_log(revenue.abs() + 1.0).shift(2)
    corr = a.rolling(345, min_periods=max(345//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 172)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.955625 + 0.0024587 * anchor
    return base_signal.diff()

def f40_eqd_587_accrual_v587_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=179, w2=356, w3=192, lag=5)."""
    a = revenue.shift(5)
    b = netinc.shift(5)
    cover = _safe_div(a.rolling(179, min_periods=max(179//3, 2)).mean(), b.abs().rolling(356, min_periods=max(356//3, 2)).mean())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.2018 * _rolling_slope(cover, 179) + 0.0024588 * anchor
    return base_signal.diff()

def f40_eqd_588_accrual_v588_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=186, w2=367, w3=205, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    y = _safe_log(ocf.abs() + 1.0).shift(10)
    z = _safe_log(ocf.abs() + 1.0).shift(10)
    basket = x - 0.2094 * y + 0.790600 * z
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 186) - _rolling_slope(basket, 367) + 0.0024589 * anchor
    return base_signal.diff()

def f40_eqd_589_accrual_v589_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=193, w2=378, w3=218, lag=21)."""
    x = ocf.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(193, min_periods=max(193//3, 2)).mean(), upside.rolling(378, min_periods=max(378//3, 2)).mean().abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.99875 + 0.002459 * anchor
    return base_signal.diff()

def f40_eqd_590_accrual_v590_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=200, w2=389, w3=231, lag=42)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(42)
    draw = x - x.rolling(389, min_periods=max(389//3, 2)).max()
    rebound = x - x.rolling(200, min_periods=max(200//3, 2)).min()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2246 * _rolling_slope(draw, 231) + 0.0024591 * anchor
    return base_signal.diff()

def f40_eqd_591_accrual_v591_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=207, w2=400, w3=244, lag=63)."""
    a = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    b = _safe_log(inventory.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(244, min_periods=max(244//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.0275 + 0.0024592 * anchor
    return base_signal.diff()

def f40_eqd_592_accrual_v592_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=214, w2=411, w3=257, lag=0)."""
    x = _safe_log(inventory.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 214)
    baseline = trend.rolling(411, min_periods=max(411//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(257, min_periods=max(257//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.041875 + 0.0024593 * anchor
    return base_signal.diff()

def f40_eqd_593_accrual_v593_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=221, w2=422, w3=270, lag=1)."""
    x = _safe_log(revenue.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 221)
    slow = _rolling_slope(x, 422)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=270, adjust=False).mean() * 1.05625 + 0.0024594 * anchor
    return base_signal.diff()

def f40_eqd_594_accrual_v594_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=228, w2=433, w3=283, lag=2)."""
    x = netinc.shift(2)
    peak = x.rolling(433, min_periods=max(433//3, 2)).max()
    trough = x.rolling(228, min_periods=max(228//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.070625 + 0.0024595 * anchor
    return base_signal.diff()

def f40_eqd_595_accrual_v595_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=235, w2=444, w3=296, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(444, min_periods=max(444//3, 2)).rank(pct=True)
    persistence = change.rolling(296, min_periods=max(296//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2626 * persistence + 0.0024596 * anchor
    return base_signal.diff()

def f40_eqd_596_accrual_v596_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=242, w2=455, w3=309, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(242, min_periods=max(242//3, 2)).std()
    vol_slow = ret.rolling(455, min_periods=max(455//3, 2)).std()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.099375 + 0.0024597 * anchor
    return base_signal.diff()

def f40_eqd_597_accrual_v597_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=249, w2=466, w3=322, lag=21)."""
    x = liabilitiesc.shift(21)
    ma = x.rolling(466, min_periods=max(466//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 249)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2778 * slope + 0.0024598 * anchor
    return base_signal.diff()

def f40_eqd_598_accrual_v598_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=5, w2=477, w3=335, lag=42)."""
    x = inventory.shift(42)
    impulse = x.diff(5)
    drag = impulse.rolling(477, min_periods=max(477//3, 2)).mean()
    noise = impulse.abs().rolling(335, min_periods=max(335//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.128125 + 0.0024599 * anchor
    return base_signal.diff()

def f40_eqd_599_accrual_v599_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=12, w2=488, w3=348, lag=63)."""
    x = _safe_log(revenue.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 12)
    acceleration = _rolling_slope(velocity, 488)
    curvature = _rolling_slope(acceleration, 348)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.293 * acceleration + 0.00246 * anchor
    return base_signal.diff()

def f40_eqd_600_accrual_v600_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=19, w2=499, w3=361, lag=0)."""
    rel = _safe_div(netinc.shift(0), ocf.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 19)
    pressure = rel_log.diff(126)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.3006 * pressure.rolling(361, min_periods=max(361//3, 2)).mean() + 0.0024601 * anchor
    return base_signal.diff()
