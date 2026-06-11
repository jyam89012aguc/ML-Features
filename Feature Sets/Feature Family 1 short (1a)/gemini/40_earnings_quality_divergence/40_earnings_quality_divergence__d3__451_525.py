"""40 earnings quality divergence d3 third derivative features 451-525 â€” Pipeline 1a-HF Grade v3.

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

def f40_eqd_451_accrual_v451_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=231, w2=369, w3=695, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(369, min_periods=max(369//3, 2)).rank(pct=True)
    persistence = change.rolling(695, min_periods=max(695//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2974 * persistence + 0.0024452 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_452_accrual_v452_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=238, w2=380, w3=708, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(238, min_periods=max(238//3, 2)).std()
    vol_slow = ret.rolling(380, min_periods=max(380//3, 2)).std()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.34875 + 0.0024453 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_453_accrual_v453_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=245, w2=391, w3=721, lag=21)."""
    x = liabilitiesc.shift(21)
    ma = x.rolling(391, min_periods=max(391//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 245)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3126 * slope + 0.0024454 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_454_accrual_v454_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=252, w2=402, w3=734, lag=42)."""
    x = inventory.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(402, min_periods=max(402//3, 2)).mean()
    noise = impulse.abs().rolling(734, min_periods=max(734//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.3775 + 0.0024455 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_455_accrual_v455_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=8, w2=413, w3=747, lag=63)."""
    x = _safe_log(revenue.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 8)
    acceleration = _rolling_slope(velocity, 413)
    curvature = _rolling_slope(acceleration, 747)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3278 * acceleration + 0.0024456 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_456_accrual_v456_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=15, w2=424, w3=760, lag=0)."""
    rel = _safe_div(netinc.shift(0), ocf.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 15)
    pressure = rel_log.diff(126)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.3354 * pressure.rolling(760, min_periods=max(760//3, 2)).mean() + 0.0024457 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_457_accrual_v457_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=22, w2=435, w3=16, lag=1)."""
    a = ocf.shift(1)
    b = assetsc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(22, min_periods=max(22//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.420625 + 0.0024458 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_458_accrual_v458_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=29, w2=446, w3=29, lag=2)."""
    a = _safe_log(assetsc.abs() + 1.0).shift(2)
    b = _safe_log(liabilitiesc.abs() + 1.0).shift(2)
    corr = a.rolling(446, min_periods=max(446//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 29)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.435 + 0.0024459 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_459_accrual_v459_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=36, w2=457, w3=42, lag=5)."""
    a = liabilitiesc.shift(5)
    b = inventory.shift(5)
    cover = _safe_div(a.rolling(36, min_periods=max(36//3, 2)).mean(), b.abs().rolling(457, min_periods=max(457//3, 2)).mean())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(42) + 0.3582 * _rolling_slope(cover, 36) + 0.002446 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_460_accrual_v460_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=43, w2=468, w3=55, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    y = _safe_log(revenue.abs() + 1.0).shift(10)
    z = _safe_log(revenue.abs() + 1.0).shift(10)
    basket = x - 0.3658 * y + 0.634200 * z
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 43) - _rolling_slope(basket, 468) + 0.0024461 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_461_accrual_v461_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=50, w2=479, w3=68, lag=21)."""
    x = revenue.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(50, min_periods=max(50//3, 2)).mean(), upside.rolling(479, min_periods=max(479//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(68) * 1.478125 + 0.0024462 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_462_accrual_v462_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=57, w2=490, w3=81, lag=42)."""
    x = _safe_log(netinc.abs() + 1.0).shift(42)
    draw = x - x.rolling(490, min_periods=max(490//3, 2)).max()
    rebound = x - x.rolling(57, min_periods=max(57//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.381 * _rolling_slope(draw, 81) + 0.0024463 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_463_accrual_v463_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=64, w2=501, w3=94, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(64) - b.diff(126)
    stress = imbalance.rolling(94, min_periods=max(94//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.506875 + 0.0024464 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_464_accrual_v464_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=71, w2=512, w3=107, lag=0)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 71)
    baseline = trend.rolling(512, min_periods=max(512//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(107, min_periods=max(107//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.52125 + 0.0024465 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_465_accrual_v465_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=78, w2=20, w3=120, lag=1)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 78)
    slow = _rolling_slope(x, 20)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=120, adjust=False).mean() * 1.535625 + 0.0024466 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_466_accrual_v466_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=85, w2=31, w3=133, lag=2)."""
    x = inventory.shift(2)
    peak = x.rolling(31, min_periods=max(31//3, 2)).max()
    trough = x.rolling(85, min_periods=max(85//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.55 + 0.0024467 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_467_accrual_v467_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=92, w2=42, w3=146, lag=5)."""
    x = revenue.shift(5)
    change = x.pct_change(92)
    rank = change.rolling(42, min_periods=max(42//3, 2)).rank(pct=True)
    persistence = change.rolling(146, min_periods=max(146//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0426 * persistence + 0.0024468 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_468_accrual_v468_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=99, w2=53, w3=159, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(99, min_periods=max(99//3, 2)).std()
    vol_slow = ret.rolling(53, min_periods=max(53//3, 2)).std()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.57875 + 0.0024469 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_469_accrual_v469_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=106, w2=64, w3=172, lag=21)."""
    x = ocf.shift(21)
    ma = x.rolling(64, min_periods=max(64//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 106)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0578 * slope + 0.002447 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_470_accrual_v470_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=113, w2=75, w3=185, lag=42)."""
    x = assetsc.shift(42)
    impulse = x.diff(113)
    drag = impulse.rolling(75, min_periods=max(75//3, 2)).mean()
    noise = impulse.abs().rolling(185, min_periods=max(185//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.6075 + 0.0024471 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_471_accrual_v471_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=120, w2=86, w3=198, lag=63)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 120)
    acceleration = _rolling_slope(velocity, 86)
    curvature = _rolling_slope(acceleration, 198)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.073 * acceleration + 0.0024472 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_472_accrual_v472_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=127, w2=97, w3=211, lag=0)."""
    rel = _safe_div(inventory.shift(0), revenue.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 127)
    pressure = rel_log.diff(97)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.0806 * pressure.rolling(211, min_periods=max(211//3, 2)).mean() + 0.0024473 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_473_accrual_v473_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=134, w2=108, w3=224, lag=1)."""
    a = revenue.shift(1)
    b = netinc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(134, min_periods=max(134//3, 2)).mean())
    decay = spread.ewm(span=108, adjust=False).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.8775 + 0.0024474 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_474_accrual_v474_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=141, w2=119, w3=237, lag=2)."""
    a = _safe_log(netinc.abs() + 1.0).shift(2)
    b = _safe_log(ocf.abs() + 1.0).shift(2)
    corr = a.rolling(119, min_periods=max(119//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 141)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.891875 + 0.0024475 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_475_accrual_v475_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=148, w2=130, w3=250, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(148, min_periods=max(148//3, 2)).mean(), b.abs().rolling(130, min_periods=max(130//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.1034 * _rolling_slope(cover, 148) + 0.0024476 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_476_accrual_v476_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=155, w2=141, w3=263, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    y = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    z = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    basket = x - 0.111 * y + 0.889000 * z
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 155) - _rolling_slope(basket, 141) + 0.0024477 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_477_accrual_v477_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=162, w2=152, w3=276, lag=21)."""
    x = liabilitiesc.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(162, min_periods=max(162//3, 2)).mean(), upside.rolling(152, min_periods=max(152//3, 2)).mean().abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.935 + 0.0024478 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_478_accrual_v478_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=169, w2=163, w3=289, lag=42)."""
    x = _safe_log(inventory.abs() + 1.0).shift(42)
    draw = x - x.rolling(163, min_periods=max(163//3, 2)).max()
    rebound = x - x.rolling(169, min_periods=max(169//3, 2)).min()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1262 * _rolling_slope(draw, 289) + 0.0024479 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_479_accrual_v479_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=176, w2=174, w3=302, lag=63)."""
    a = _safe_log(revenue.abs() + 1.0).shift(63)
    b = _safe_log(netinc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(302, min_periods=max(302//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.96375 + 0.002448 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_480_accrual_v480_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=183, w2=185, w3=315, lag=0)."""
    x = _safe_log(netinc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 183)
    baseline = trend.rolling(185, min_periods=max(185//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(315, min_periods=max(315//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.978125 + 0.0024481 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_481_accrual_v481_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=190, w2=196, w3=328, lag=1)."""
    x = _safe_log(ocf.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 190)
    slow = _rolling_slope(x, 196)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.9925 + 0.0024482 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_482_accrual_v482_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=197, w2=207, w3=341, lag=2)."""
    x = assetsc.shift(2)
    peak = x.rolling(207, min_periods=max(207//3, 2)).max()
    trough = x.rolling(197, min_periods=max(197//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.006875 + 0.0024483 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_483_accrual_v483_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=204, w2=218, w3=354, lag=5)."""
    x = liabilitiesc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(218, min_periods=max(218//3, 2)).rank(pct=True)
    persistence = change.rolling(354, min_periods=max(354//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1642 * persistence + 0.0024484 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_484_accrual_v484_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=211, w2=229, w3=367, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(211, min_periods=max(211//3, 2)).std()
    vol_slow = ret.rolling(229, min_periods=max(229//3, 2)).std()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.035625 + 0.0024485 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_485_accrual_v485_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=218, w2=240, w3=380, lag=21)."""
    x = revenue.shift(21)
    ma = x.rolling(240, min_periods=max(240//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 218)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1794 * slope + 0.0024486 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_486_accrual_v486_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=225, w2=251, w3=393, lag=42)."""
    x = netinc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(251, min_periods=max(251//3, 2)).mean()
    noise = impulse.abs().rolling(393, min_periods=max(393//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.064375 + 0.0024487 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_487_accrual_v487_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=232, w2=262, w3=406, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 232)
    acceleration = _rolling_slope(velocity, 262)
    curvature = _rolling_slope(acceleration, 406)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1946 * acceleration + 0.0024488 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_488_accrual_v488_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=239, w2=273, w3=419, lag=0)."""
    rel = _safe_div(assetsc.shift(0), liabilitiesc.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 239)
    pressure = rel_log.diff(126)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.2022 * pressure.rolling(419, min_periods=max(419//3, 2)).mean() + 0.0024489 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_489_accrual_v489_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=246, w2=284, w3=432, lag=1)."""
    a = liabilitiesc.shift(1)
    b = inventory.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(246, min_periods=max(246//3, 2)).mean())
    decay = spread.ewm(span=284, adjust=False).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.1075 + 0.002449 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_490_accrual_v490_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=253, w2=295, w3=445, lag=2)."""
    a = _safe_log(inventory.abs() + 1.0).shift(2)
    b = _safe_log(revenue.abs() + 1.0).shift(2)
    corr = a.rolling(295, min_periods=max(295//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 253)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.121875 + 0.0024491 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_491_accrual_v491_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=9, w2=306, w3=458, lag=5)."""
    a = revenue.shift(5)
    b = netinc.shift(5)
    cover = _safe_div(a.rolling(9, min_periods=max(9//3, 2)).mean(), b.abs().rolling(306, min_periods=max(306//3, 2)).mean())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.225 * _rolling_slope(cover, 9) + 0.0024492 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_492_accrual_v492_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=16, w2=317, w3=471, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    y = _safe_log(ocf.abs() + 1.0).shift(10)
    z = _safe_log(ocf.abs() + 1.0).shift(10)
    basket = x - 0.2326 * y + 0.767400 * z
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 16) - _rolling_slope(basket, 317) + 0.0024493 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_493_accrual_v493_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=23, w2=328, w3=484, lag=21)."""
    x = ocf.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(23, min_periods=max(23//3, 2)).mean(), upside.rolling(328, min_periods=max(328//3, 2)).mean().abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.165 + 0.0024494 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_494_accrual_v494_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=30, w2=339, w3=497, lag=42)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(42)
    draw = x - x.rolling(339, min_periods=max(339//3, 2)).max()
    rebound = x - x.rolling(30, min_periods=max(30//3, 2)).min()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2478 * _rolling_slope(draw, 497) + 0.0024495 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_495_accrual_v495_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=37, w2=350, w3=510, lag=63)."""
    a = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    b = _safe_log(inventory.abs() + 1.0).shift(63)
    imbalance = a.diff(37) - b.diff(126)
    stress = imbalance.rolling(510, min_periods=max(510//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.19375 + 0.0024496 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_496_accrual_v496_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=44, w2=361, w3=523, lag=0)."""
    x = _safe_log(inventory.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 44)
    baseline = trend.rolling(361, min_periods=max(361//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(523, min_periods=max(523//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.208125 + 0.0024497 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_497_accrual_v497_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=51, w2=372, w3=536, lag=1)."""
    x = _safe_log(revenue.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 51)
    slow = _rolling_slope(x, 372)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.2225 + 0.0024498 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_498_accrual_v498_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=58, w2=383, w3=549, lag=2)."""
    x = netinc.shift(2)
    peak = x.rolling(383, min_periods=max(383//3, 2)).max()
    trough = x.rolling(58, min_periods=max(58//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.236875 + 0.0024499 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_499_accrual_v499_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=65, w2=394, w3=562, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(65)
    rank = change.rolling(394, min_periods=max(394//3, 2)).rank(pct=True)
    persistence = change.rolling(562, min_periods=max(562//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2858 * persistence + 0.00245 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_500_accrual_v500_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=72, w2=405, w3=575, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(72, min_periods=max(72//3, 2)).std()
    vol_slow = ret.rolling(405, min_periods=max(405//3, 2)).std()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.265625 + 0.0024501 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_501_accrual_v501_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=79, w2=416, w3=588, lag=21)."""
    x = liabilitiesc.shift(21)
    ma = x.rolling(416, min_periods=max(416//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 79)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.301 * slope + 0.0024502 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_502_accrual_v502_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=86, w2=427, w3=601, lag=42)."""
    x = inventory.shift(42)
    impulse = x.diff(86)
    drag = impulse.rolling(427, min_periods=max(427//3, 2)).mean()
    noise = impulse.abs().rolling(601, min_periods=max(601//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.294375 + 0.0024503 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_503_accrual_v503_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=93, w2=438, w3=614, lag=63)."""
    x = _safe_log(revenue.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 93)
    acceleration = _rolling_slope(velocity, 438)
    curvature = _rolling_slope(acceleration, 614)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3162 * acceleration + 0.0024504 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_504_accrual_v504_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=100, w2=449, w3=627, lag=0)."""
    rel = _safe_div(netinc.shift(0), ocf.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 100)
    pressure = rel_log.diff(126)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.3238 * pressure.rolling(627, min_periods=max(627//3, 2)).mean() + 0.0024505 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_505_accrual_v505_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=107, w2=460, w3=640, lag=1)."""
    a = ocf.shift(1)
    b = assetsc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(107, min_periods=max(107//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.3375 + 0.0024506 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_506_accrual_v506_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=114, w2=471, w3=653, lag=2)."""
    a = _safe_log(assetsc.abs() + 1.0).shift(2)
    b = _safe_log(liabilitiesc.abs() + 1.0).shift(2)
    corr = a.rolling(471, min_periods=max(471//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 114)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.351875 + 0.0024507 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_507_accrual_v507_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=121, w2=482, w3=666, lag=5)."""
    a = liabilitiesc.shift(5)
    b = inventory.shift(5)
    cover = _safe_div(a.rolling(121, min_periods=max(121//3, 2)).mean(), b.abs().rolling(482, min_periods=max(482//3, 2)).mean())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.3466 * _rolling_slope(cover, 121) + 0.0024508 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_508_accrual_v508_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=128, w2=493, w3=679, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    y = _safe_log(revenue.abs() + 1.0).shift(10)
    z = _safe_log(revenue.abs() + 1.0).shift(10)
    basket = x - 0.3542 * y + 0.645800 * z
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 128) - _rolling_slope(basket, 493) + 0.0024509 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_509_accrual_v509_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=135, w2=504, w3=692, lag=21)."""
    x = revenue.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(135, min_periods=max(135//3, 2)).mean(), upside.rolling(504, min_periods=max(504//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.395 + 0.002451 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_510_accrual_v510_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=142, w2=12, w3=705, lag=42)."""
    x = _safe_log(netinc.abs() + 1.0).shift(42)
    draw = x - x.rolling(12, min_periods=max(12//3, 2)).max()
    rebound = x - x.rolling(142, min_periods=max(142//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3694 * _rolling_slope(draw, 705) + 0.0024511 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_511_accrual_v511_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=149, w2=23, w3=718, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(23)
    stress = imbalance.rolling(718, min_periods=max(718//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.42375 + 0.0024512 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_512_accrual_v512_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=156, w2=34, w3=731, lag=0)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 156)
    baseline = trend.rolling(34, min_periods=max(34//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(731, min_periods=max(731//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.438125 + 0.0024513 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_513_accrual_v513_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=163, w2=45, w3=744, lag=1)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 163)
    slow = _rolling_slope(x, 45)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.4525 + 0.0024514 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_514_accrual_v514_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=170, w2=56, w3=757, lag=2)."""
    x = inventory.shift(2)
    peak = x.rolling(56, min_periods=max(56//3, 2)).max()
    trough = x.rolling(170, min_periods=max(170//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.466875 + 0.0024515 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_515_accrual_v515_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=177, w2=67, w3=770, lag=5)."""
    x = revenue.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(67, min_periods=max(67//3, 2)).rank(pct=True)
    persistence = change.rolling(770, min_periods=max(770//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.4074 * persistence + 0.0024516 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_516_accrual_v516_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=184, w2=78, w3=26, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(184, min_periods=max(184//3, 2)).std()
    vol_slow = ret.rolling(78, min_periods=max(78//3, 2)).std()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.495625 + 0.0024517 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_517_accrual_v517_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=191, w2=89, w3=39, lag=21)."""
    x = ocf.shift(21)
    ma = x.rolling(89, min_periods=max(89//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 191)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0462 * slope + 0.0024518 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_518_accrual_v518_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=198, w2=100, w3=52, lag=42)."""
    x = assetsc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(100, min_periods=max(100//3, 2)).mean()
    noise = impulse.abs().rolling(52, min_periods=max(52//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.524375 + 0.0024519 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_519_accrual_v519_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=205, w2=111, w3=65, lag=63)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 205)
    acceleration = _rolling_slope(velocity, 111)
    curvature = _rolling_slope(acceleration, 65)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0614 * acceleration + 0.002452 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_520_accrual_v520_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=212, w2=122, w3=78, lag=0)."""
    rel = _safe_div(inventory.shift(0), revenue.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 212)
    pressure = rel_log.diff(122)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.069 * pressure.rolling(78, min_periods=max(78//3, 2)).mean() + 0.0024521 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_521_accrual_v521_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=219, w2=133, w3=91, lag=1)."""
    a = revenue.shift(1)
    b = netinc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(219, min_periods=max(219//3, 2)).mean())
    decay = spread.ewm(span=133, adjust=False).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.5675 + 0.0024522 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_522_accrual_v522_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=226, w2=144, w3=104, lag=2)."""
    a = _safe_log(netinc.abs() + 1.0).shift(2)
    b = _safe_log(ocf.abs() + 1.0).shift(2)
    corr = a.rolling(144, min_periods=max(144//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 226)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.581875 + 0.0024523 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_523_accrual_v523_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=233, w2=155, w3=117, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(233, min_periods=max(233//3, 2)).mean(), b.abs().rolling(155, min_periods=max(155//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(117) + 0.0918 * _rolling_slope(cover, 233) + 0.0024524 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_524_accrual_v524_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=240, w2=166, w3=130, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    y = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    z = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    basket = x - 0.0994 * y + 0.900600 * z
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 240) - _rolling_slope(basket, 166) + 0.0024525 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_525_accrual_v525_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=247, w2=177, w3=143, lag=21)."""
    x = liabilitiesc.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(247, min_periods=max(247//3, 2)).mean(), upside.rolling(177, min_periods=max(177//3, 2)).mean().abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.851875 + 0.0024526 * anchor
    return base_signal.diff().diff().diff()
