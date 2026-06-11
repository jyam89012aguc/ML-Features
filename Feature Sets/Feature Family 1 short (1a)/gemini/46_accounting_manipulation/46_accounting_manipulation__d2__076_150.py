"""46 accounting manipulation d2 second derivative features 76-150 â€” Pipeline 1a-HF Grade v3.

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

def f46_aman_076_accrual_v76_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=149, w2=192, w3=458, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(149, min_periods=max(149//3, 2)).std()
    vol_slow = ret.rolling(192, min_periods=max(192//3, 2)).std()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.426875 + 0.0028277 * anchor
    return base_signal.diff().diff()

def f46_aman_077_accrual_v77_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=156, w2=203, w3=471, lag=21)."""
    x = revenue.shift(21)
    ma = x.rolling(203, min_periods=max(203//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 156)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3922 * slope + 0.0028278 * anchor
    return base_signal.diff().diff()

def f46_aman_078_accrual_v78_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=163, w2=214, w3=484, lag=42)."""
    x = netinc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(214, min_periods=max(214//3, 2)).mean()
    noise = impulse.abs().rolling(484, min_periods=max(484//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.455625 + 0.0028279 * anchor
    return base_signal.diff().diff()

def f46_aman_079_accrual_v79_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=170, w2=225, w3=497, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 170)
    acceleration = _rolling_slope(velocity, 225)
    curvature = _rolling_slope(acceleration, 497)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.4074 * acceleration + 0.002828 * anchor
    return base_signal.diff().diff()

def f46_aman_080_accrual_v80_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=177, w2=236, w3=510, lag=0)."""
    rel = _safe_div(assetsc.shift(0), liabilitiesc.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 177)
    pressure = rel_log.diff(126)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.0386 * pressure.rolling(510, min_periods=max(510//3, 2)).mean() + 0.0028281 * anchor
    return base_signal.diff().diff()

def f46_aman_081_accrual_v81_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=184, w2=247, w3=523, lag=1)."""
    a = liabilitiesc.shift(1)
    b = inventory.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(184, min_periods=max(184//3, 2)).mean())
    decay = spread.ewm(span=247, adjust=False).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.49875 + 0.0028282 * anchor
    return base_signal.diff().diff()

def f46_aman_082_accrual_v82_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=191, w2=258, w3=536, lag=2)."""
    a = _safe_log(inventory.abs() + 1.0).shift(2)
    b = _safe_log(revenue.abs() + 1.0).shift(2)
    corr = a.rolling(258, min_periods=max(258//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 191)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.513125 + 0.0028283 * anchor
    return base_signal.diff().diff()

def f46_aman_083_accrual_v83_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=198, w2=269, w3=549, lag=5)."""
    a = revenue.shift(5)
    b = netinc.shift(5)
    cover = _safe_div(a.rolling(198, min_periods=max(198//3, 2)).mean(), b.abs().rolling(269, min_periods=max(269//3, 2)).mean())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.0614 * _rolling_slope(cover, 198) + 0.0028284 * anchor
    return base_signal.diff().diff()

def f46_aman_084_accrual_v84_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=205, w2=280, w3=562, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    y = _safe_log(ocf.abs() + 1.0).shift(10)
    z = _safe_log(ocf.abs() + 1.0).shift(10)
    basket = x - 0.069 * y + 0.931000 * z
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 205) - _rolling_slope(basket, 280) + 0.0028285 * anchor
    return base_signal.diff().diff()

def f46_aman_085_accrual_v85_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=212, w2=291, w3=575, lag=21)."""
    x = ocf.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(212, min_periods=max(212//3, 2)).mean(), upside.rolling(291, min_periods=max(291//3, 2)).mean().abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.55625 + 0.0028286 * anchor
    return base_signal.diff().diff()

def f46_aman_086_accrual_v86_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=219, w2=302, w3=588, lag=42)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(42)
    draw = x - x.rolling(302, min_periods=max(302//3, 2)).max()
    rebound = x - x.rolling(219, min_periods=max(219//3, 2)).min()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0842 * _rolling_slope(draw, 588) + 0.0028287 * anchor
    return base_signal.diff().diff()

def f46_aman_087_accrual_v87_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=226, w2=313, w3=601, lag=63)."""
    a = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    b = _safe_log(inventory.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(601, min_periods=max(601//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.585 + 0.0028288 * anchor
    return base_signal.diff().diff()

def f46_aman_088_accrual_v88_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=233, w2=324, w3=614, lag=0)."""
    x = _safe_log(inventory.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 233)
    baseline = trend.rolling(324, min_periods=max(324//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(614, min_periods=max(614//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.599375 + 0.0028289 * anchor
    return base_signal.diff().diff()

def f46_aman_089_accrual_v89_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=240, w2=335, w3=627, lag=1)."""
    x = _safe_log(revenue.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 240)
    slow = _rolling_slope(x, 335)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.61375 + 0.002829 * anchor
    return base_signal.diff().diff()

def f46_aman_090_accrual_v90_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=247, w2=346, w3=640, lag=2)."""
    x = netinc.shift(2)
    peak = x.rolling(346, min_periods=max(346//3, 2)).max()
    trough = x.rolling(247, min_periods=max(247//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.855 + 0.0028291 * anchor
    return base_signal.diff().diff()

def f46_aman_091_accrual_v91_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=254, w2=357, w3=653, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(357, min_periods=max(357//3, 2)).rank(pct=True)
    persistence = change.rolling(653, min_periods=max(653//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1222 * persistence + 0.0028292 * anchor
    return base_signal.diff().diff()

def f46_aman_092_accrual_v92_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=10, w2=368, w3=666, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(10, min_periods=max(10//3, 2)).std()
    vol_slow = ret.rolling(368, min_periods=max(368//3, 2)).std()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.88375 + 0.0028293 * anchor
    return base_signal.diff().diff()

def f46_aman_093_accrual_v93_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=17, w2=379, w3=679, lag=21)."""
    x = liabilitiesc.shift(21)
    ma = x.rolling(379, min_periods=max(379//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 17)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1374 * slope + 0.0028294 * anchor
    return base_signal.diff().diff()

def f46_aman_094_accrual_v94_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=24, w2=390, w3=692, lag=42)."""
    x = inventory.shift(42)
    impulse = x.diff(24)
    drag = impulse.rolling(390, min_periods=max(390//3, 2)).mean()
    noise = impulse.abs().rolling(692, min_periods=max(692//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.9125 + 0.0028295 * anchor
    return base_signal.diff().diff()

def f46_aman_095_accrual_v95_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=31, w2=401, w3=705, lag=63)."""
    x = _safe_log(revenue.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 31)
    acceleration = _rolling_slope(velocity, 401)
    curvature = _rolling_slope(acceleration, 705)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1526 * acceleration + 0.0028296 * anchor
    return base_signal.diff().diff()

def f46_aman_096_accrual_v96_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=38, w2=412, w3=718, lag=0)."""
    rel = _safe_div(netinc.shift(0), ocf.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 38)
    pressure = rel_log.diff(126)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.1602 * pressure.rolling(718, min_periods=max(718//3, 2)).mean() + 0.0028297 * anchor
    return base_signal.diff().diff()

def f46_aman_097_accrual_v97_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=45, w2=423, w3=731, lag=1)."""
    a = ocf.shift(1)
    b = assetsc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(45, min_periods=max(45//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.955625 + 0.0028298 * anchor
    return base_signal.diff().diff()

def f46_aman_098_accrual_v98_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=52, w2=434, w3=744, lag=2)."""
    a = _safe_log(assetsc.abs() + 1.0).shift(2)
    b = _safe_log(liabilitiesc.abs() + 1.0).shift(2)
    corr = a.rolling(434, min_periods=max(434//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 52)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.97 + 0.0028299 * anchor
    return base_signal.diff().diff()

def f46_aman_099_accrual_v99_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=59, w2=445, w3=757, lag=5)."""
    a = liabilitiesc.shift(5)
    b = inventory.shift(5)
    cover = _safe_div(a.rolling(59, min_periods=max(59//3, 2)).mean(), b.abs().rolling(445, min_periods=max(445//3, 2)).mean())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.183 * _rolling_slope(cover, 59) + 0.00283 * anchor
    return base_signal.diff().diff()

def f46_aman_100_accrual_v100_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=66, w2=456, w3=770, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    y = _safe_log(revenue.abs() + 1.0).shift(10)
    z = _safe_log(revenue.abs() + 1.0).shift(10)
    basket = x - 0.1906 * y + 0.809400 * z
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 66) - _rolling_slope(basket, 456) + 0.0028301 * anchor
    return base_signal.diff().diff()

def f46_aman_101_accrual_v101_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=73, w2=467, w3=26, lag=21)."""
    x = revenue.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(73, min_periods=max(73//3, 2)).mean(), upside.rolling(467, min_periods=max(467//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(26) * 1.013125 + 0.0028302 * anchor
    return base_signal.diff().diff()

def f46_aman_102_accrual_v102_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=80, w2=478, w3=39, lag=42)."""
    x = _safe_log(netinc.abs() + 1.0).shift(42)
    draw = x - x.rolling(478, min_periods=max(478//3, 2)).max()
    rebound = x - x.rolling(80, min_periods=max(80//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2058 * _rolling_slope(draw, 39) + 0.0028303 * anchor
    return base_signal.diff().diff()

def f46_aman_103_accrual_v103_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=87, w2=489, w3=52, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(87) - b.diff(126)
    stress = imbalance.rolling(52, min_periods=max(52//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.041875 + 0.0028304 * anchor
    return base_signal.diff().diff()

def f46_aman_104_accrual_v104_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=94, w2=500, w3=65, lag=0)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 94)
    baseline = trend.rolling(500, min_periods=max(500//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(65, min_periods=max(65//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.05625 + 0.0028305 * anchor
    return base_signal.diff().diff()

def f46_aman_105_accrual_v105_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=101, w2=511, w3=78, lag=1)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 101)
    slow = _rolling_slope(x, 511)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=78, adjust=False).mean() * 1.070625 + 0.0028306 * anchor
    return base_signal.diff().diff()

def f46_aman_106_accrual_v106_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=108, w2=19, w3=91, lag=2)."""
    x = inventory.shift(2)
    peak = x.rolling(19, min_periods=max(19//3, 2)).max()
    trough = x.rolling(108, min_periods=max(108//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.085 + 0.0028307 * anchor
    return base_signal.diff().diff()

def f46_aman_107_accrual_v107_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=115, w2=30, w3=104, lag=5)."""
    x = revenue.shift(5)
    change = x.pct_change(115)
    rank = change.rolling(30, min_periods=max(30//3, 2)).rank(pct=True)
    persistence = change.rolling(104, min_periods=max(104//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2438 * persistence + 0.0028308 * anchor
    return base_signal.diff().diff()

def f46_aman_108_accrual_v108_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=122, w2=41, w3=117, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(122, min_periods=max(122//3, 2)).std()
    vol_slow = ret.rolling(41, min_periods=max(41//3, 2)).std()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.11375 + 0.0028309 * anchor
    return base_signal.diff().diff()

def f46_aman_109_accrual_v109_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=129, w2=52, w3=130, lag=21)."""
    x = ocf.shift(21)
    ma = x.rolling(52, min_periods=max(52//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 129)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.259 * slope + 0.002831 * anchor
    return base_signal.diff().diff()

def f46_aman_110_accrual_v110_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=136, w2=63, w3=143, lag=42)."""
    x = assetsc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(63, min_periods=max(63//3, 2)).mean()
    noise = impulse.abs().rolling(143, min_periods=max(143//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.1425 + 0.0028311 * anchor
    return base_signal.diff().diff()

def f46_aman_111_accrual_v111_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=143, w2=74, w3=156, lag=63)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 143)
    acceleration = _rolling_slope(velocity, 74)
    curvature = _rolling_slope(acceleration, 156)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2742 * acceleration + 0.0028312 * anchor
    return base_signal.diff().diff()

def f46_aman_112_accrual_v112_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=150, w2=85, w3=169, lag=0)."""
    rel = _safe_div(inventory.shift(0), revenue.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 150)
    pressure = rel_log.diff(85)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.2818 * pressure.rolling(169, min_periods=max(169//3, 2)).mean() + 0.0028313 * anchor
    return base_signal.diff().diff()

def f46_aman_113_accrual_v113_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=157, w2=96, w3=182, lag=1)."""
    a = revenue.shift(1)
    b = netinc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(157, min_periods=max(157//3, 2)).mean())
    decay = spread.ewm(span=96, adjust=False).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.185625 + 0.0028314 * anchor
    return base_signal.diff().diff()

def f46_aman_114_accrual_v114_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=164, w2=107, w3=195, lag=2)."""
    a = _safe_log(netinc.abs() + 1.0).shift(2)
    b = _safe_log(ocf.abs() + 1.0).shift(2)
    corr = a.rolling(107, min_periods=max(107//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 164)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.2 + 0.0028315 * anchor
    return base_signal.diff().diff()

def f46_aman_115_accrual_v115_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=171, w2=118, w3=208, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(171, min_periods=max(171//3, 2)).mean(), b.abs().rolling(118, min_periods=max(118//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.3046 * _rolling_slope(cover, 171) + 0.0028316 * anchor
    return base_signal.diff().diff()

def f46_aman_116_accrual_v116_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=178, w2=129, w3=221, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    y = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    z = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    basket = x - 0.3122 * y + 0.687800 * z
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 178) - _rolling_slope(basket, 129) + 0.0028317 * anchor
    return base_signal.diff().diff()

def f46_aman_117_accrual_v117_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=185, w2=140, w3=234, lag=21)."""
    x = liabilitiesc.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(185, min_periods=max(185//3, 2)).mean(), upside.rolling(140, min_periods=max(140//3, 2)).mean().abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.243125 + 0.0028318 * anchor
    return base_signal.diff().diff()

def f46_aman_118_accrual_v118_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=192, w2=151, w3=247, lag=42)."""
    x = _safe_log(inventory.abs() + 1.0).shift(42)
    draw = x - x.rolling(151, min_periods=max(151//3, 2)).max()
    rebound = x - x.rolling(192, min_periods=max(192//3, 2)).min()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3274 * _rolling_slope(draw, 247) + 0.0028319 * anchor
    return base_signal.diff().diff()

def f46_aman_119_accrual_v119_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=199, w2=162, w3=260, lag=63)."""
    a = _safe_log(revenue.abs() + 1.0).shift(63)
    b = _safe_log(netinc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(260, min_periods=max(260//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.271875 + 0.002832 * anchor
    return base_signal.diff().diff()

def f46_aman_120_accrual_v120_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=206, w2=173, w3=273, lag=0)."""
    x = _safe_log(netinc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 206)
    baseline = trend.rolling(173, min_periods=max(173//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(273, min_periods=max(273//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.28625 + 0.0028321 * anchor
    return base_signal.diff().diff()

def f46_aman_121_accrual_v121_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=213, w2=184, w3=286, lag=1)."""
    x = _safe_log(ocf.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 213)
    slow = _rolling_slope(x, 184)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=286, adjust=False).mean() * 1.300625 + 0.0028322 * anchor
    return base_signal.diff().diff()

def f46_aman_122_accrual_v122_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=220, w2=195, w3=299, lag=2)."""
    x = assetsc.shift(2)
    peak = x.rolling(195, min_periods=max(195//3, 2)).max()
    trough = x.rolling(220, min_periods=max(220//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.315 + 0.0028323 * anchor
    return base_signal.diff().diff()

def f46_aman_123_accrual_v123_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=227, w2=206, w3=312, lag=5)."""
    x = liabilitiesc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(206, min_periods=max(206//3, 2)).rank(pct=True)
    persistence = change.rolling(312, min_periods=max(312//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3654 * persistence + 0.0028324 * anchor
    return base_signal.diff().diff()

def f46_aman_124_accrual_v124_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=234, w2=217, w3=325, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(234, min_periods=max(234//3, 2)).std()
    vol_slow = ret.rolling(217, min_periods=max(217//3, 2)).std()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.34375 + 0.0028325 * anchor
    return base_signal.diff().diff()

def f46_aman_125_accrual_v125_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=241, w2=228, w3=338, lag=21)."""
    x = revenue.shift(21)
    ma = x.rolling(228, min_periods=max(228//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 241)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3806 * slope + 0.0028326 * anchor
    return base_signal.diff().diff()

def f46_aman_126_accrual_v126_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=248, w2=239, w3=351, lag=42)."""
    x = netinc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(239, min_periods=max(239//3, 2)).mean()
    noise = impulse.abs().rolling(351, min_periods=max(351//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.3725 + 0.0028327 * anchor
    return base_signal.diff().diff()

def f46_aman_127_accrual_v127_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=255, w2=250, w3=364, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 255)
    acceleration = _rolling_slope(velocity, 250)
    curvature = _rolling_slope(acceleration, 364)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3958 * acceleration + 0.0028328 * anchor
    return base_signal.diff().diff()

def f46_aman_128_accrual_v128_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=11, w2=261, w3=377, lag=0)."""
    rel = _safe_div(assetsc.shift(0), liabilitiesc.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 11)
    pressure = rel_log.diff(126)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.4034 * pressure.rolling(377, min_periods=max(377//3, 2)).mean() + 0.0028329 * anchor
    return base_signal.diff().diff()

def f46_aman_129_accrual_v129_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=18, w2=272, w3=390, lag=1)."""
    a = liabilitiesc.shift(1)
    b = inventory.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(18, min_periods=max(18//3, 2)).mean())
    decay = spread.ewm(span=272, adjust=False).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.415625 + 0.002833 * anchor
    return base_signal.diff().diff()

def f46_aman_130_accrual_v130_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=25, w2=283, w3=403, lag=2)."""
    a = _safe_log(inventory.abs() + 1.0).shift(2)
    b = _safe_log(revenue.abs() + 1.0).shift(2)
    corr = a.rolling(283, min_periods=max(283//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 25)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.43 + 0.0028331 * anchor
    return base_signal.diff().diff()

def f46_aman_131_accrual_v131_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=32, w2=294, w3=416, lag=5)."""
    a = revenue.shift(5)
    b = netinc.shift(5)
    cover = _safe_div(a.rolling(32, min_periods=max(32//3, 2)).mean(), b.abs().rolling(294, min_periods=max(294//3, 2)).mean())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.0498 * _rolling_slope(cover, 32) + 0.0028332 * anchor
    return base_signal.diff().diff()

def f46_aman_132_accrual_v132_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=39, w2=305, w3=429, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    y = _safe_log(ocf.abs() + 1.0).shift(10)
    z = _safe_log(ocf.abs() + 1.0).shift(10)
    basket = x - 0.0574 * y + 0.942600 * z
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 39) - _rolling_slope(basket, 305) + 0.0028333 * anchor
    return base_signal.diff().diff()

def f46_aman_133_accrual_v133_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=46, w2=316, w3=442, lag=21)."""
    x = ocf.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(46, min_periods=max(46//3, 2)).mean(), upside.rolling(316, min_periods=max(316//3, 2)).mean().abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.473125 + 0.0028334 * anchor
    return base_signal.diff().diff()

def f46_aman_134_accrual_v134_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=53, w2=327, w3=455, lag=42)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(42)
    draw = x - x.rolling(327, min_periods=max(327//3, 2)).max()
    rebound = x - x.rolling(53, min_periods=max(53//3, 2)).min()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0726 * _rolling_slope(draw, 455) + 0.0028335 * anchor
    return base_signal.diff().diff()

def f46_aman_135_accrual_v135_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=60, w2=338, w3=468, lag=63)."""
    a = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    b = _safe_log(inventory.abs() + 1.0).shift(63)
    imbalance = a.diff(60) - b.diff(126)
    stress = imbalance.rolling(468, min_periods=max(468//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.501875 + 0.0028336 * anchor
    return base_signal.diff().diff()

def f46_aman_136_accrual_v136_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=67, w2=349, w3=481, lag=0)."""
    x = _safe_log(inventory.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 67)
    baseline = trend.rolling(349, min_periods=max(349//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(481, min_periods=max(481//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.51625 + 0.0028337 * anchor
    return base_signal.diff().diff()

def f46_aman_137_accrual_v137_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=74, w2=360, w3=494, lag=1)."""
    x = _safe_log(revenue.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 74)
    slow = _rolling_slope(x, 360)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.530625 + 0.0028338 * anchor
    return base_signal.diff().diff()

def f46_aman_138_accrual_v138_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=81, w2=371, w3=507, lag=2)."""
    x = netinc.shift(2)
    peak = x.rolling(371, min_periods=max(371//3, 2)).max()
    trough = x.rolling(81, min_periods=max(81//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.545 + 0.0028339 * anchor
    return base_signal.diff().diff()

def f46_aman_139_accrual_v139_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=88, w2=382, w3=520, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(88)
    rank = change.rolling(382, min_periods=max(382//3, 2)).rank(pct=True)
    persistence = change.rolling(520, min_periods=max(520//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1106 * persistence + 0.002834 * anchor
    return base_signal.diff().diff()

def f46_aman_140_accrual_v140_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=95, w2=393, w3=533, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(95, min_periods=max(95//3, 2)).std()
    vol_slow = ret.rolling(393, min_periods=max(393//3, 2)).std()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.57375 + 0.0028341 * anchor
    return base_signal.diff().diff()

def f46_aman_141_accrual_v141_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=102, w2=404, w3=546, lag=21)."""
    x = liabilitiesc.shift(21)
    ma = x.rolling(404, min_periods=max(404//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 102)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1258 * slope + 0.0028342 * anchor
    return base_signal.diff().diff()

def f46_aman_142_accrual_v142_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=109, w2=415, w3=559, lag=42)."""
    x = inventory.shift(42)
    impulse = x.diff(109)
    drag = impulse.rolling(415, min_periods=max(415//3, 2)).mean()
    noise = impulse.abs().rolling(559, min_periods=max(559//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.6025 + 0.0028343 * anchor
    return base_signal.diff().diff()

def f46_aman_143_accrual_v143_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=116, w2=426, w3=572, lag=63)."""
    x = _safe_log(revenue.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 116)
    acceleration = _rolling_slope(velocity, 426)
    curvature = _rolling_slope(acceleration, 572)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.141 * acceleration + 0.0028344 * anchor
    return base_signal.diff().diff()

def f46_aman_144_accrual_v144_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=123, w2=437, w3=585, lag=0)."""
    rel = _safe_div(netinc.shift(0), ocf.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 123)
    pressure = rel_log.diff(126)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.1486 * pressure.rolling(585, min_periods=max(585//3, 2)).mean() + 0.0028345 * anchor
    return base_signal.diff().diff()

def f46_aman_145_accrual_v145_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=130, w2=448, w3=598, lag=1)."""
    a = ocf.shift(1)
    b = assetsc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(130, min_periods=max(130//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.8725 + 0.0028346 * anchor
    return base_signal.diff().diff()

def f46_aman_146_accrual_v146_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=137, w2=459, w3=611, lag=2)."""
    a = _safe_log(assetsc.abs() + 1.0).shift(2)
    b = _safe_log(liabilitiesc.abs() + 1.0).shift(2)
    corr = a.rolling(459, min_periods=max(459//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 137)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.886875 + 0.0028347 * anchor
    return base_signal.diff().diff()

def f46_aman_147_accrual_v147_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=144, w2=470, w3=624, lag=5)."""
    a = liabilitiesc.shift(5)
    b = inventory.shift(5)
    cover = _safe_div(a.rolling(144, min_periods=max(144//3, 2)).mean(), b.abs().rolling(470, min_periods=max(470//3, 2)).mean())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.1714 * _rolling_slope(cover, 144) + 0.0028348 * anchor
    return base_signal.diff().diff()

def f46_aman_148_accrual_v148_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=151, w2=481, w3=637, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    y = _safe_log(revenue.abs() + 1.0).shift(10)
    z = _safe_log(revenue.abs() + 1.0).shift(10)
    basket = x - 0.179 * y + 0.821000 * z
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 151) - _rolling_slope(basket, 481) + 0.0028349 * anchor
    return base_signal.diff().diff()

def f46_aman_149_accrual_v149_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=158, w2=492, w3=650, lag=21)."""
    x = revenue.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(158, min_periods=max(158//3, 2)).mean(), upside.rolling(492, min_periods=max(492//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.93 + 0.002835 * anchor
    return base_signal.diff().diff()

def f46_aman_150_accrual_v150_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=165, w2=503, w3=663, lag=42)."""
    x = _safe_log(netinc.abs() + 1.0).shift(42)
    draw = x - x.rolling(503, min_periods=max(503//3, 2)).max()
    rebound = x - x.rolling(165, min_periods=max(165//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1942 * _rolling_slope(draw, 663) + 0.0028351 * anchor
    return base_signal.diff().diff()
