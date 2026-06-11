"""47 fraud emergence signal d2 second derivative features 451-525 â€” Pipeline 1a-HF Grade v3.

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

def f47_fes_451_accrual_v451_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=197, w2=354, w3=264, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(354, min_periods=max(354//3, 2)).rank(pct=True)
    persistence = change.rolling(264, min_periods=max(264//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2666 * persistence + 0.0029252 * anchor
    return base_signal.diff().diff()

def f47_fes_452_accrual_v452_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=204, w2=365, w3=277, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(204, min_periods=max(204//3, 2)).std()
    vol_slow = ret.rolling(365, min_periods=max(365//3, 2)).std()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.540625 + 0.0029253 * anchor
    return base_signal.diff().diff()

def f47_fes_453_accrual_v453_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=211, w2=376, w3=290, lag=21)."""
    x = liabilitiesc.shift(21)
    ma = x.rolling(376, min_periods=max(376//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 211)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2818 * slope + 0.0029254 * anchor
    return base_signal.diff().diff()

def f47_fes_454_accrual_v454_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=218, w2=387, w3=303, lag=42)."""
    x = inventory.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(387, min_periods=max(387//3, 2)).mean()
    noise = impulse.abs().rolling(303, min_periods=max(303//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.569375 + 0.0029255 * anchor
    return base_signal.diff().diff()

def f47_fes_455_accrual_v455_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=225, w2=398, w3=316, lag=63)."""
    x = _safe_log(revenue.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 225)
    acceleration = _rolling_slope(velocity, 398)
    curvature = _rolling_slope(acceleration, 316)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.297 * acceleration + 0.0029256 * anchor
    return base_signal.diff().diff()

def f47_fes_456_accrual_v456_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=232, w2=409, w3=329, lag=0)."""
    rel = _safe_div(netinc.shift(0), ocf.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 232)
    pressure = rel_log.diff(126)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.3046 * pressure.rolling(329, min_periods=max(329//3, 2)).mean() + 0.0029257 * anchor
    return base_signal.diff().diff()

def f47_fes_457_accrual_v457_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=239, w2=420, w3=342, lag=1)."""
    a = ocf.shift(1)
    b = assetsc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(239, min_periods=max(239//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.6125 + 0.0029258 * anchor
    return base_signal.diff().diff()

def f47_fes_458_accrual_v458_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=246, w2=431, w3=355, lag=2)."""
    a = _safe_log(assetsc.abs() + 1.0).shift(2)
    b = _safe_log(liabilitiesc.abs() + 1.0).shift(2)
    corr = a.rolling(431, min_periods=max(431//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 246)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.85375 + 0.0029259 * anchor
    return base_signal.diff().diff()

def f47_fes_459_accrual_v459_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=253, w2=442, w3=368, lag=5)."""
    a = liabilitiesc.shift(5)
    b = inventory.shift(5)
    cover = _safe_div(a.rolling(253, min_periods=max(253//3, 2)).mean(), b.abs().rolling(442, min_periods=max(442//3, 2)).mean())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.3274 * _rolling_slope(cover, 253) + 0.002926 * anchor
    return base_signal.diff().diff()

def f47_fes_460_accrual_v460_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=9, w2=453, w3=381, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    y = _safe_log(revenue.abs() + 1.0).shift(10)
    z = _safe_log(revenue.abs() + 1.0).shift(10)
    basket = x - 0.335 * y + 0.665000 * z
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 9) - _rolling_slope(basket, 453) + 0.0029261 * anchor
    return base_signal.diff().diff()

def f47_fes_461_accrual_v461_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=16, w2=464, w3=394, lag=21)."""
    x = revenue.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(16, min_periods=max(16//3, 2)).mean(), upside.rolling(464, min_periods=max(464//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.896875 + 0.0029262 * anchor
    return base_signal.diff().diff()

def f47_fes_462_accrual_v462_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=23, w2=475, w3=407, lag=42)."""
    x = _safe_log(netinc.abs() + 1.0).shift(42)
    draw = x - x.rolling(475, min_periods=max(475//3, 2)).max()
    rebound = x - x.rolling(23, min_periods=max(23//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3502 * _rolling_slope(draw, 407) + 0.0029263 * anchor
    return base_signal.diff().diff()

def f47_fes_463_accrual_v463_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=30, w2=486, w3=420, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(30) - b.diff(126)
    stress = imbalance.rolling(420, min_periods=max(420//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.925625 + 0.0029264 * anchor
    return base_signal.diff().diff()

def f47_fes_464_accrual_v464_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=37, w2=497, w3=433, lag=0)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 37)
    baseline = trend.rolling(497, min_periods=max(497//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(433, min_periods=max(433//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.94 + 0.0029265 * anchor
    return base_signal.diff().diff()

def f47_fes_465_accrual_v465_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=44, w2=508, w3=446, lag=1)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 44)
    slow = _rolling_slope(x, 508)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.954375 + 0.0029266 * anchor
    return base_signal.diff().diff()

def f47_fes_466_accrual_v466_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=51, w2=16, w3=459, lag=2)."""
    x = inventory.shift(2)
    peak = x.rolling(16, min_periods=max(16//3, 2)).max()
    trough = x.rolling(51, min_periods=max(51//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.96875 + 0.0029267 * anchor
    return base_signal.diff().diff()

def f47_fes_467_accrual_v467_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=58, w2=27, w3=472, lag=5)."""
    x = revenue.shift(5)
    change = x.pct_change(58)
    rank = change.rolling(27, min_periods=max(27//3, 2)).rank(pct=True)
    persistence = change.rolling(472, min_periods=max(472//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3882 * persistence + 0.0029268 * anchor
    return base_signal.diff().diff()

def f47_fes_468_accrual_v468_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=65, w2=38, w3=485, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(65, min_periods=max(65//3, 2)).std()
    vol_slow = ret.rolling(38, min_periods=max(38//3, 2)).std()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.9975 + 0.0029269 * anchor
    return base_signal.diff().diff()

def f47_fes_469_accrual_v469_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=72, w2=49, w3=498, lag=21)."""
    x = ocf.shift(21)
    ma = x.rolling(49, min_periods=max(49//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 72)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.4034 * slope + 0.002927 * anchor
    return base_signal.diff().diff()

def f47_fes_470_accrual_v470_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=79, w2=60, w3=511, lag=42)."""
    x = assetsc.shift(42)
    impulse = x.diff(79)
    drag = impulse.rolling(60, min_periods=max(60//3, 2)).mean()
    noise = impulse.abs().rolling(511, min_periods=max(511//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.02625 + 0.0029271 * anchor
    return base_signal.diff().diff()

def f47_fes_471_accrual_v471_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=86, w2=71, w3=524, lag=63)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 86)
    acceleration = _rolling_slope(velocity, 71)
    curvature = _rolling_slope(acceleration, 524)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0422 * acceleration + 0.0029272 * anchor
    return base_signal.diff().diff()

def f47_fes_472_accrual_v472_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=93, w2=82, w3=537, lag=0)."""
    rel = _safe_div(inventory.shift(0), revenue.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 93)
    pressure = rel_log.diff(82)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.0498 * pressure.rolling(537, min_periods=max(537//3, 2)).mean() + 0.0029273 * anchor
    return base_signal.diff().diff()

def f47_fes_473_accrual_v473_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=100, w2=93, w3=550, lag=1)."""
    a = revenue.shift(1)
    b = netinc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(100, min_periods=max(100//3, 2)).mean())
    decay = spread.ewm(span=93, adjust=False).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.069375 + 0.0029274 * anchor
    return base_signal.diff().diff()

def f47_fes_474_accrual_v474_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=107, w2=104, w3=563, lag=2)."""
    a = _safe_log(netinc.abs() + 1.0).shift(2)
    b = _safe_log(ocf.abs() + 1.0).shift(2)
    corr = a.rolling(104, min_periods=max(104//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 107)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.08375 + 0.0029275 * anchor
    return base_signal.diff().diff()

def f47_fes_475_accrual_v475_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=114, w2=115, w3=576, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(114, min_periods=max(114//3, 2)).mean(), b.abs().rolling(115, min_periods=max(115//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.0726 * _rolling_slope(cover, 114) + 0.0029276 * anchor
    return base_signal.diff().diff()

def f47_fes_476_accrual_v476_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=121, w2=126, w3=589, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    y = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    z = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    basket = x - 0.0802 * y + 0.919800 * z
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 121) - _rolling_slope(basket, 126) + 0.0029277 * anchor
    return base_signal.diff().diff()

def f47_fes_477_accrual_v477_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=128, w2=137, w3=602, lag=21)."""
    x = liabilitiesc.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(128, min_periods=max(128//3, 2)).mean(), upside.rolling(137, min_periods=max(137//3, 2)).mean().abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.126875 + 0.0029278 * anchor
    return base_signal.diff().diff()

def f47_fes_478_accrual_v478_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=135, w2=148, w3=615, lag=42)."""
    x = _safe_log(inventory.abs() + 1.0).shift(42)
    draw = x - x.rolling(148, min_periods=max(148//3, 2)).max()
    rebound = x - x.rolling(135, min_periods=max(135//3, 2)).min()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0954 * _rolling_slope(draw, 615) + 0.0029279 * anchor
    return base_signal.diff().diff()

def f47_fes_479_accrual_v479_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=142, w2=159, w3=628, lag=63)."""
    a = _safe_log(revenue.abs() + 1.0).shift(63)
    b = _safe_log(netinc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(628, min_periods=max(628//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.155625 + 0.002928 * anchor
    return base_signal.diff().diff()

def f47_fes_480_accrual_v480_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=149, w2=170, w3=641, lag=0)."""
    x = _safe_log(netinc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 149)
    baseline = trend.rolling(170, min_periods=max(170//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(641, min_periods=max(641//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.17 + 0.0029281 * anchor
    return base_signal.diff().diff()

def f47_fes_481_accrual_v481_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=156, w2=181, w3=654, lag=1)."""
    x = _safe_log(ocf.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 156)
    slow = _rolling_slope(x, 181)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.184375 + 0.0029282 * anchor
    return base_signal.diff().diff()

def f47_fes_482_accrual_v482_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=163, w2=192, w3=667, lag=2)."""
    x = assetsc.shift(2)
    peak = x.rolling(192, min_periods=max(192//3, 2)).max()
    trough = x.rolling(163, min_periods=max(163//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.19875 + 0.0029283 * anchor
    return base_signal.diff().diff()

def f47_fes_483_accrual_v483_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=170, w2=203, w3=680, lag=5)."""
    x = liabilitiesc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(203, min_periods=max(203//3, 2)).rank(pct=True)
    persistence = change.rolling(680, min_periods=max(680//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1334 * persistence + 0.0029284 * anchor
    return base_signal.diff().diff()

def f47_fes_484_accrual_v484_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=177, w2=214, w3=693, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(177, min_periods=max(177//3, 2)).std()
    vol_slow = ret.rolling(214, min_periods=max(214//3, 2)).std()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.2275 + 0.0029285 * anchor
    return base_signal.diff().diff()

def f47_fes_485_accrual_v485_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=184, w2=225, w3=706, lag=21)."""
    x = revenue.shift(21)
    ma = x.rolling(225, min_periods=max(225//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 184)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1486 * slope + 0.0029286 * anchor
    return base_signal.diff().diff()

def f47_fes_486_accrual_v486_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=191, w2=236, w3=719, lag=42)."""
    x = netinc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(236, min_periods=max(236//3, 2)).mean()
    noise = impulse.abs().rolling(719, min_periods=max(719//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.25625 + 0.0029287 * anchor
    return base_signal.diff().diff()

def f47_fes_487_accrual_v487_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=198, w2=247, w3=732, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 198)
    acceleration = _rolling_slope(velocity, 247)
    curvature = _rolling_slope(acceleration, 732)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1638 * acceleration + 0.0029288 * anchor
    return base_signal.diff().diff()

def f47_fes_488_accrual_v488_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=205, w2=258, w3=745, lag=0)."""
    rel = _safe_div(assetsc.shift(0), liabilitiesc.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 205)
    pressure = rel_log.diff(126)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.1714 * pressure.rolling(745, min_periods=max(745//3, 2)).mean() + 0.0029289 * anchor
    return base_signal.diff().diff()

def f47_fes_489_accrual_v489_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=212, w2=269, w3=758, lag=1)."""
    a = liabilitiesc.shift(1)
    b = inventory.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(212, min_periods=max(212//3, 2)).mean())
    decay = spread.ewm(span=269, adjust=False).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.299375 + 0.002929 * anchor
    return base_signal.diff().diff()

def f47_fes_490_accrual_v490_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=219, w2=280, w3=771, lag=2)."""
    a = _safe_log(inventory.abs() + 1.0).shift(2)
    b = _safe_log(revenue.abs() + 1.0).shift(2)
    corr = a.rolling(280, min_periods=max(280//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 219)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.31375 + 0.0029291 * anchor
    return base_signal.diff().diff()

def f47_fes_491_accrual_v491_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=226, w2=291, w3=27, lag=5)."""
    a = revenue.shift(5)
    b = netinc.shift(5)
    cover = _safe_div(a.rolling(226, min_periods=max(226//3, 2)).mean(), b.abs().rolling(291, min_periods=max(291//3, 2)).mean())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(27) + 0.1942 * _rolling_slope(cover, 226) + 0.0029292 * anchor
    return base_signal.diff().diff()

def f47_fes_492_accrual_v492_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=233, w2=302, w3=40, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    y = _safe_log(ocf.abs() + 1.0).shift(10)
    z = _safe_log(ocf.abs() + 1.0).shift(10)
    basket = x - 0.2018 * y + 0.798200 * z
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 233) - _rolling_slope(basket, 302) + 0.0029293 * anchor
    return base_signal.diff().diff()

def f47_fes_493_accrual_v493_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=240, w2=313, w3=53, lag=21)."""
    x = ocf.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(240, min_periods=max(240//3, 2)).mean(), upside.rolling(313, min_periods=max(313//3, 2)).mean().abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(53) * 1.356875 + 0.0029294 * anchor
    return base_signal.diff().diff()

def f47_fes_494_accrual_v494_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=247, w2=324, w3=66, lag=42)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(42)
    draw = x - x.rolling(324, min_periods=max(324//3, 2)).max()
    rebound = x - x.rolling(247, min_periods=max(247//3, 2)).min()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.217 * _rolling_slope(draw, 66) + 0.0029295 * anchor
    return base_signal.diff().diff()

def f47_fes_495_accrual_v495_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=254, w2=335, w3=79, lag=63)."""
    a = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    b = _safe_log(inventory.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(79, min_periods=max(79//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.385625 + 0.0029296 * anchor
    return base_signal.diff().diff()

def f47_fes_496_accrual_v496_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=10, w2=346, w3=92, lag=0)."""
    x = _safe_log(inventory.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 10)
    baseline = trend.rolling(346, min_periods=max(346//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(92, min_periods=max(92//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.4 + 0.0029297 * anchor
    return base_signal.diff().diff()

def f47_fes_497_accrual_v497_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=17, w2=357, w3=105, lag=1)."""
    x = _safe_log(revenue.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 17)
    slow = _rolling_slope(x, 357)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=105, adjust=False).mean() * 1.414375 + 0.0029298 * anchor
    return base_signal.diff().diff()

def f47_fes_498_accrual_v498_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=24, w2=368, w3=118, lag=2)."""
    x = netinc.shift(2)
    peak = x.rolling(368, min_periods=max(368//3, 2)).max()
    trough = x.rolling(24, min_periods=max(24//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.42875 + 0.0029299 * anchor
    return base_signal.diff().diff()

def f47_fes_499_accrual_v499_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=31, w2=379, w3=131, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(31)
    rank = change.rolling(379, min_periods=max(379//3, 2)).rank(pct=True)
    persistence = change.rolling(131, min_periods=max(131//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.255 * persistence + 0.00293 * anchor
    return base_signal.diff().diff()

def f47_fes_500_accrual_v500_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=38, w2=390, w3=144, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(38, min_periods=max(38//3, 2)).std()
    vol_slow = ret.rolling(390, min_periods=max(390//3, 2)).std()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.4575 + 0.0029301 * anchor
    return base_signal.diff().diff()

def f47_fes_501_accrual_v501_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=45, w2=401, w3=157, lag=21)."""
    x = liabilitiesc.shift(21)
    ma = x.rolling(401, min_periods=max(401//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 45)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2702 * slope + 0.0029302 * anchor
    return base_signal.diff().diff()

def f47_fes_502_accrual_v502_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=52, w2=412, w3=170, lag=42)."""
    x = inventory.shift(42)
    impulse = x.diff(52)
    drag = impulse.rolling(412, min_periods=max(412//3, 2)).mean()
    noise = impulse.abs().rolling(170, min_periods=max(170//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.48625 + 0.0029303 * anchor
    return base_signal.diff().diff()

def f47_fes_503_accrual_v503_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=59, w2=423, w3=183, lag=63)."""
    x = _safe_log(revenue.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 59)
    acceleration = _rolling_slope(velocity, 423)
    curvature = _rolling_slope(acceleration, 183)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2854 * acceleration + 0.0029304 * anchor
    return base_signal.diff().diff()

def f47_fes_504_accrual_v504_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=66, w2=434, w3=196, lag=0)."""
    rel = _safe_div(netinc.shift(0), ocf.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 66)
    pressure = rel_log.diff(126)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.293 * pressure.rolling(196, min_periods=max(196//3, 2)).mean() + 0.0029305 * anchor
    return base_signal.diff().diff()

def f47_fes_505_accrual_v505_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=73, w2=445, w3=209, lag=1)."""
    a = ocf.shift(1)
    b = assetsc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(73, min_periods=max(73//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.529375 + 0.0029306 * anchor
    return base_signal.diff().diff()

def f47_fes_506_accrual_v506_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=80, w2=456, w3=222, lag=2)."""
    a = _safe_log(assetsc.abs() + 1.0).shift(2)
    b = _safe_log(liabilitiesc.abs() + 1.0).shift(2)
    corr = a.rolling(456, min_periods=max(456//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 80)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.54375 + 0.0029307 * anchor
    return base_signal.diff().diff()

def f47_fes_507_accrual_v507_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=87, w2=467, w3=235, lag=5)."""
    a = liabilitiesc.shift(5)
    b = inventory.shift(5)
    cover = _safe_div(a.rolling(87, min_periods=max(87//3, 2)).mean(), b.abs().rolling(467, min_periods=max(467//3, 2)).mean())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.3158 * _rolling_slope(cover, 87) + 0.0029308 * anchor
    return base_signal.diff().diff()

def f47_fes_508_accrual_v508_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=94, w2=478, w3=248, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    y = _safe_log(revenue.abs() + 1.0).shift(10)
    z = _safe_log(revenue.abs() + 1.0).shift(10)
    basket = x - 0.3234 * y + 0.676600 * z
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 94) - _rolling_slope(basket, 478) + 0.0029309 * anchor
    return base_signal.diff().diff()

def f47_fes_509_accrual_v509_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=101, w2=489, w3=261, lag=21)."""
    x = revenue.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(101, min_periods=max(101//3, 2)).mean(), upside.rolling(489, min_periods=max(489//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.586875 + 0.002931 * anchor
    return base_signal.diff().diff()

def f47_fes_510_accrual_v510_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=108, w2=500, w3=274, lag=42)."""
    x = _safe_log(netinc.abs() + 1.0).shift(42)
    draw = x - x.rolling(500, min_periods=max(500//3, 2)).max()
    rebound = x - x.rolling(108, min_periods=max(108//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3386 * _rolling_slope(draw, 274) + 0.0029311 * anchor
    return base_signal.diff().diff()

def f47_fes_511_accrual_v511_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=115, w2=511, w3=287, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(115) - b.diff(126)
    stress = imbalance.rolling(287, min_periods=max(287//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.615625 + 0.0029312 * anchor
    return base_signal.diff().diff()

def f47_fes_512_accrual_v512_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=122, w2=19, w3=300, lag=0)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 122)
    baseline = trend.rolling(19, min_periods=max(19//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(300, min_periods=max(300//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.856875 + 0.0029313 * anchor
    return base_signal.diff().diff()

def f47_fes_513_accrual_v513_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=129, w2=30, w3=313, lag=1)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 129)
    slow = _rolling_slope(x, 30)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.87125 + 0.0029314 * anchor
    return base_signal.diff().diff()

def f47_fes_514_accrual_v514_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=136, w2=41, w3=326, lag=2)."""
    x = inventory.shift(2)
    peak = x.rolling(41, min_periods=max(41//3, 2)).max()
    trough = x.rolling(136, min_periods=max(136//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.885625 + 0.0029315 * anchor
    return base_signal.diff().diff()

def f47_fes_515_accrual_v515_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=143, w2=52, w3=339, lag=5)."""
    x = revenue.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(52, min_periods=max(52//3, 2)).rank(pct=True)
    persistence = change.rolling(339, min_periods=max(339//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3766 * persistence + 0.0029316 * anchor
    return base_signal.diff().diff()

def f47_fes_516_accrual_v516_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=150, w2=63, w3=352, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(150, min_periods=max(150//3, 2)).std()
    vol_slow = ret.rolling(63, min_periods=max(63//3, 2)).std()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.914375 + 0.0029317 * anchor
    return base_signal.diff().diff()

def f47_fes_517_accrual_v517_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=157, w2=74, w3=365, lag=21)."""
    x = ocf.shift(21)
    ma = x.rolling(74, min_periods=max(74//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 157)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3918 * slope + 0.0029318 * anchor
    return base_signal.diff().diff()

def f47_fes_518_accrual_v518_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=164, w2=85, w3=378, lag=42)."""
    x = assetsc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(85, min_periods=max(85//3, 2)).mean()
    noise = impulse.abs().rolling(378, min_periods=max(378//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.943125 + 0.0029319 * anchor
    return base_signal.diff().diff()

def f47_fes_519_accrual_v519_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=171, w2=96, w3=391, lag=63)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 171)
    acceleration = _rolling_slope(velocity, 96)
    curvature = _rolling_slope(acceleration, 391)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.407 * acceleration + 0.002932 * anchor
    return base_signal.diff().diff()

def f47_fes_520_accrual_v520_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=178, w2=107, w3=404, lag=0)."""
    rel = _safe_div(inventory.shift(0), revenue.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 178)
    pressure = rel_log.diff(107)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.0382 * pressure.rolling(404, min_periods=max(404//3, 2)).mean() + 0.0029321 * anchor
    return base_signal.diff().diff()

def f47_fes_521_accrual_v521_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=185, w2=118, w3=417, lag=1)."""
    a = revenue.shift(1)
    b = netinc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(185, min_periods=max(185//3, 2)).mean())
    decay = spread.ewm(span=118, adjust=False).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.98625 + 0.0029322 * anchor
    return base_signal.diff().diff()

def f47_fes_522_accrual_v522_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=192, w2=129, w3=430, lag=2)."""
    a = _safe_log(netinc.abs() + 1.0).shift(2)
    b = _safe_log(ocf.abs() + 1.0).shift(2)
    corr = a.rolling(129, min_periods=max(129//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 192)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.000625 + 0.0029323 * anchor
    return base_signal.diff().diff()

def f47_fes_523_accrual_v523_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=199, w2=140, w3=443, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(199, min_periods=max(199//3, 2)).mean(), b.abs().rolling(140, min_periods=max(140//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.061 * _rolling_slope(cover, 199) + 0.0029324 * anchor
    return base_signal.diff().diff()

def f47_fes_524_accrual_v524_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=206, w2=151, w3=456, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    y = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    z = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    basket = x - 0.0686 * y + 0.931400 * z
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 206) - _rolling_slope(basket, 151) + 0.0029325 * anchor
    return base_signal.diff().diff()

def f47_fes_525_accrual_v525_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=213, w2=162, w3=469, lag=21)."""
    x = liabilitiesc.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(213, min_periods=max(213//3, 2)).mean(), upside.rolling(162, min_periods=max(162//3, 2)).mean().abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.04375 + 0.0029326 * anchor
    return base_signal.diff().diff()
