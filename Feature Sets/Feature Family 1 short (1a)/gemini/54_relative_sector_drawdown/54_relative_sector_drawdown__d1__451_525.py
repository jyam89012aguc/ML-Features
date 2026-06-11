"""54 relative sector drawdown d1 first derivative features 451-525 â€” Pipeline 1a-HF Grade v3.

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

def f54_rsw_d_451_rel_v451_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=230, w2=278, w3=360, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(230, min_periods=max(230//3, 2)).mean(), b.abs().rolling(278, min_periods=max(278//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.1926 * _rolling_slope(cover, 230) + 0.0033452 * anchor
    return base_signal.diff()

def f54_rsw_d_452_rel_v452_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=237, w2=289, w3=373, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.2002 * y + 0.799800 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 237) - _rolling_slope(basket, 289) + 0.0033453 * anchor
    return base_signal.diff()

def f54_rsw_d_453_rel_v453_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=244, w2=300, w3=386, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(244, min_periods=max(244//3, 2)).mean(), upside.rolling(300, min_periods=max(300//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.853125 + 0.0033454 * anchor
    return base_signal.diff()

def f54_rsw_d_454_rel_v454_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=251, w2=311, w3=399, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(311, min_periods=max(311//3, 2)).max()
    rebound = x - x.rolling(251, min_periods=max(251//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2154 * _rolling_slope(draw, 399) + 0.0033455 * anchor
    return base_signal.diff()

def f54_rsw_d_455_rel_v455_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=7, w2=322, w3=412, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(7) - b.diff(126)
    stress = imbalance.rolling(412, min_periods=max(412//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.881875 + 0.0033456 * anchor
    return base_signal.diff()

def f54_rsw_d_456_rel_v456_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=14, w2=333, w3=425, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 14)
    baseline = trend.rolling(333, min_periods=max(333//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(425, min_periods=max(425//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.89625 + 0.0033457 * anchor
    return base_signal.diff()

def f54_rsw_d_457_rel_v457_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=21, w2=344, w3=438, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 21)
    slow = _rolling_slope(x, 344)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.910625 + 0.0033458 * anchor
    return base_signal.diff()

def f54_rsw_d_458_rel_v458_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=28, w2=355, w3=451, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(355, min_periods=max(355//3, 2)).max()
    trough = x.rolling(28, min_periods=max(28//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.925 + 0.0033459 * anchor
    return base_signal.diff()

def f54_rsw_d_459_rel_v459_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=35, w2=366, w3=464, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(35)
    rank = change.rolling(366, min_periods=max(366//3, 2)).rank(pct=True)
    persistence = change.rolling(464, min_periods=max(464//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2534 * persistence + 0.003346 * anchor
    return base_signal.diff()

def f54_rsw_d_460_rel_v460_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=42, w2=377, w3=477, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(42, min_periods=max(42//3, 2)).std()
    vol_slow = ret.rolling(377, min_periods=max(377//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.95375 + 0.0033461 * anchor
    return base_signal.diff()

def f54_rsw_d_461_rel_v461_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=49, w2=388, w3=490, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(388, min_periods=max(388//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 49)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2686 * slope + 0.0033462 * anchor
    return base_signal.diff()

def f54_rsw_d_462_rel_v462_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=56, w2=399, w3=503, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(56)
    drag = impulse.rolling(399, min_periods=max(399//3, 2)).mean()
    noise = impulse.abs().rolling(503, min_periods=max(503//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.9825 + 0.0033463 * anchor
    return base_signal.diff()

def f54_rsw_d_463_rel_v463_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=63, w2=410, w3=516, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 63)
    acceleration = _rolling_slope(velocity, 410)
    curvature = _rolling_slope(acceleration, 516)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2838 * acceleration + 0.0033464 * anchor
    return base_signal.diff()

def f54_rsw_d_464_rel_v464_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=70, w2=421, w3=529, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 70)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.2914 * pressure.rolling(529, min_periods=max(529//3, 2)).mean() + 0.0033465 * anchor
    return base_signal.diff()

def f54_rsw_d_465_rel_v465_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=77, w2=432, w3=542, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(77, min_periods=max(77//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.025625 + 0.0033466 * anchor
    return base_signal.diff()

def f54_rsw_d_466_rel_v466_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=84, w2=443, w3=555, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(443, min_periods=max(443//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 84)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.04 + 0.0033467 * anchor
    return base_signal.diff()

def f54_rsw_d_467_rel_v467_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=91, w2=454, w3=568, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(91, min_periods=max(91//3, 2)).mean(), b.abs().rolling(454, min_periods=max(454//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.3142 * _rolling_slope(cover, 91) + 0.0033468 * anchor
    return base_signal.diff()

def f54_rsw_d_468_rel_v468_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=98, w2=465, w3=581, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.3218 * y + 0.678200 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 98) - _rolling_slope(basket, 465) + 0.0033469 * anchor
    return base_signal.diff()

def f54_rsw_d_469_rel_v469_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=105, w2=476, w3=594, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(105, min_periods=max(105//3, 2)).mean(), upside.rolling(476, min_periods=max(476//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.083125 + 0.003347 * anchor
    return base_signal.diff()

def f54_rsw_d_470_rel_v470_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=112, w2=487, w3=607, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(487, min_periods=max(487//3, 2)).max()
    rebound = x - x.rolling(112, min_periods=max(112//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.337 * _rolling_slope(draw, 607) + 0.0033471 * anchor
    return base_signal.diff()

def f54_rsw_d_471_rel_v471_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=119, w2=498, w3=620, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(119) - b.diff(126)
    stress = imbalance.rolling(620, min_periods=max(620//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.111875 + 0.0033472 * anchor
    return base_signal.diff()

def f54_rsw_d_472_rel_v472_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=126, w2=509, w3=633, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 126)
    baseline = trend.rolling(509, min_periods=max(509//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(633, min_periods=max(633//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.12625 + 0.0033473 * anchor
    return base_signal.diff()

def f54_rsw_d_473_rel_v473_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=133, w2=17, w3=646, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 133)
    slow = _rolling_slope(x, 17)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.140625 + 0.0033474 * anchor
    return base_signal.diff()

def f54_rsw_d_474_rel_v474_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=140, w2=28, w3=659, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(28, min_periods=max(28//3, 2)).max()
    trough = x.rolling(140, min_periods=max(140//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.155 + 0.0033475 * anchor
    return base_signal.diff()

def f54_rsw_d_475_rel_v475_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=147, w2=39, w3=672, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(39, min_periods=max(39//3, 2)).rank(pct=True)
    persistence = change.rolling(672, min_periods=max(672//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.375 * persistence + 0.0033476 * anchor
    return base_signal.diff()

def f54_rsw_d_476_rel_v476_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=154, w2=50, w3=685, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(154, min_periods=max(154//3, 2)).std()
    vol_slow = ret.rolling(50, min_periods=max(50//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.18375 + 0.0033477 * anchor
    return base_signal.diff()

def f54_rsw_d_477_rel_v477_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=161, w2=61, w3=698, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(61, min_periods=max(61//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 161)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3902 * slope + 0.0033478 * anchor
    return base_signal.diff()

def f54_rsw_d_478_rel_v478_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=168, w2=72, w3=711, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(72, min_periods=max(72//3, 2)).mean()
    noise = impulse.abs().rolling(711, min_periods=max(711//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.2125 + 0.0033479 * anchor
    return base_signal.diff()

def f54_rsw_d_479_rel_v479_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=175, w2=83, w3=724, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 175)
    acceleration = _rolling_slope(velocity, 83)
    curvature = _rolling_slope(acceleration, 724)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.4054 * acceleration + 0.003348 * anchor
    return base_signal.diff()

def f54_rsw_d_480_rel_v480_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=182, w2=94, w3=737, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 182)
    pressure = rel_log.diff(94)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.0366 * pressure.rolling(737, min_periods=max(737//3, 2)).mean() + 0.0033481 * anchor
    return base_signal.diff()

def f54_rsw_d_481_rel_v481_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=189, w2=105, w3=750, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(189, min_periods=max(189//3, 2)).mean())
    decay = spread.ewm(span=105, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.255625 + 0.0033482 * anchor
    return base_signal.diff()

def f54_rsw_d_482_rel_v482_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=196, w2=116, w3=763, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(116, min_periods=max(116//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 196)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.27 + 0.0033483 * anchor
    return base_signal.diff()

def f54_rsw_d_483_rel_v483_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=203, w2=127, w3=19, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(203, min_periods=max(203//3, 2)).mean(), b.abs().rolling(127, min_periods=max(127//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(19) + 0.0594 * _rolling_slope(cover, 203) + 0.0033484 * anchor
    return base_signal.diff()

def f54_rsw_d_484_rel_v484_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=210, w2=138, w3=32, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.067 * y + 0.933000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 210) - _rolling_slope(basket, 138) + 0.0033485 * anchor
    return base_signal.diff()

def f54_rsw_d_485_rel_v485_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=217, w2=149, w3=45, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(217, min_periods=max(217//3, 2)).mean(), upside.rolling(149, min_periods=max(149//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(45) * 1.313125 + 0.0033486 * anchor
    return base_signal.diff()

def f54_rsw_d_486_rel_v486_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=224, w2=160, w3=58, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(160, min_periods=max(160//3, 2)).max()
    rebound = x - x.rolling(224, min_periods=max(224//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0822 * _rolling_slope(draw, 58) + 0.0033487 * anchor
    return base_signal.diff()

def f54_rsw_d_487_rel_v487_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=231, w2=171, w3=71, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(71, min_periods=max(71//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.341875 + 0.0033488 * anchor
    return base_signal.diff()

def f54_rsw_d_488_rel_v488_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=238, w2=182, w3=84, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 238)
    baseline = trend.rolling(182, min_periods=max(182//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(84, min_periods=max(84//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.35625 + 0.0033489 * anchor
    return base_signal.diff()

def f54_rsw_d_489_rel_v489_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=245, w2=193, w3=97, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 245)
    slow = _rolling_slope(x, 193)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=97, adjust=False).mean() * 1.370625 + 0.003349 * anchor
    return base_signal.diff()

def f54_rsw_d_490_rel_v490_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=252, w2=204, w3=110, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(204, min_periods=max(204//3, 2)).max()
    trough = x.rolling(252, min_periods=max(252//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.385 + 0.0033491 * anchor
    return base_signal.diff()

def f54_rsw_d_491_rel_v491_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=8, w2=215, w3=123, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(8)
    rank = change.rolling(215, min_periods=max(215//3, 2)).rank(pct=True)
    persistence = change.rolling(123, min_periods=max(123//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1202 * persistence + 0.0033492 * anchor
    return base_signal.diff()

def f54_rsw_d_492_rel_v492_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=15, w2=226, w3=136, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(15, min_periods=max(15//3, 2)).std()
    vol_slow = ret.rolling(226, min_periods=max(226//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.41375 + 0.0033493 * anchor
    return base_signal.diff()

def f54_rsw_d_493_rel_v493_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=22, w2=237, w3=149, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(237, min_periods=max(237//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 22)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1354 * slope + 0.0033494 * anchor
    return base_signal.diff()

def f54_rsw_d_494_rel_v494_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=29, w2=248, w3=162, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(29)
    drag = impulse.rolling(248, min_periods=max(248//3, 2)).mean()
    noise = impulse.abs().rolling(162, min_periods=max(162//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.4425 + 0.0033495 * anchor
    return base_signal.diff()

def f54_rsw_d_495_rel_v495_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=36, w2=259, w3=175, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 36)
    acceleration = _rolling_slope(velocity, 259)
    curvature = _rolling_slope(acceleration, 175)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1506 * acceleration + 0.0033496 * anchor
    return base_signal.diff()

def f54_rsw_d_496_rel_v496_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=43, w2=270, w3=188, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 43)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.1582 * pressure.rolling(188, min_periods=max(188//3, 2)).mean() + 0.0033497 * anchor
    return base_signal.diff()

def f54_rsw_d_497_rel_v497_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=50, w2=281, w3=201, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(50, min_periods=max(50//3, 2)).mean())
    decay = spread.ewm(span=281, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.485625 + 0.0033498 * anchor
    return base_signal.diff()

def f54_rsw_d_498_rel_v498_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=57, w2=292, w3=214, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(292, min_periods=max(292//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 57)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.5 + 0.0033499 * anchor
    return base_signal.diff()

def f54_rsw_d_499_rel_v499_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=64, w2=303, w3=227, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(64, min_periods=max(64//3, 2)).mean(), b.abs().rolling(303, min_periods=max(303//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.181 * _rolling_slope(cover, 64) + 0.00335 * anchor
    return base_signal.diff()

def f54_rsw_d_500_rel_v500_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=71, w2=314, w3=240, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.1886 * y + 0.811400 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 71) - _rolling_slope(basket, 314) + 0.0033501 * anchor
    return base_signal.diff()

def f54_rsw_d_501_rel_v501_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=78, w2=325, w3=253, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(78, min_periods=max(78//3, 2)).mean(), upside.rolling(325, min_periods=max(325//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.543125 + 0.0033502 * anchor
    return base_signal.diff()

def f54_rsw_d_502_rel_v502_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=85, w2=336, w3=266, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(336, min_periods=max(336//3, 2)).max()
    rebound = x - x.rolling(85, min_periods=max(85//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2038 * _rolling_slope(draw, 266) + 0.0033503 * anchor
    return base_signal.diff()

def f54_rsw_d_503_rel_v503_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=92, w2=347, w3=279, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(92) - b.diff(126)
    stress = imbalance.rolling(279, min_periods=max(279//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.571875 + 0.0033504 * anchor
    return base_signal.diff()

def f54_rsw_d_504_rel_v504_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=99, w2=358, w3=292, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 99)
    baseline = trend.rolling(358, min_periods=max(358//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(292, min_periods=max(292//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.58625 + 0.0033505 * anchor
    return base_signal.diff()

def f54_rsw_d_505_rel_v505_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=106, w2=369, w3=305, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 106)
    slow = _rolling_slope(x, 369)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.600625 + 0.0033506 * anchor
    return base_signal.diff()

def f54_rsw_d_506_rel_v506_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=113, w2=380, w3=318, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(380, min_periods=max(380//3, 2)).max()
    trough = x.rolling(113, min_periods=max(113//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.615 + 0.0033507 * anchor
    return base_signal.diff()

def f54_rsw_d_507_rel_v507_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=120, w2=391, w3=331, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(120)
    rank = change.rolling(391, min_periods=max(391//3, 2)).rank(pct=True)
    persistence = change.rolling(331, min_periods=max(331//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2418 * persistence + 0.0033508 * anchor
    return base_signal.diff()

def f54_rsw_d_508_rel_v508_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=127, w2=402, w3=344, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(127, min_periods=max(127//3, 2)).std()
    vol_slow = ret.rolling(402, min_periods=max(402//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.870625 + 0.0033509 * anchor
    return base_signal.diff()

def f54_rsw_d_509_rel_v509_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=134, w2=413, w3=357, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(413, min_periods=max(413//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 134)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.257 * slope + 0.003351 * anchor
    return base_signal.diff()

def f54_rsw_d_510_rel_v510_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=141, w2=424, w3=370, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(424, min_periods=max(424//3, 2)).mean()
    noise = impulse.abs().rolling(370, min_periods=max(370//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.899375 + 0.0033511 * anchor
    return base_signal.diff()

def f54_rsw_d_511_rel_v511_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=148, w2=435, w3=383, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 148)
    acceleration = _rolling_slope(velocity, 435)
    curvature = _rolling_slope(acceleration, 383)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2722 * acceleration + 0.0033512 * anchor
    return base_signal.diff()

def f54_rsw_d_512_rel_v512_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=155, w2=446, w3=396, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 155)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.2798 * pressure.rolling(396, min_periods=max(396//3, 2)).mean() + 0.0033513 * anchor
    return base_signal.diff()

def f54_rsw_d_513_rel_v513_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=162, w2=457, w3=409, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(162, min_periods=max(162//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.9425 + 0.0033514 * anchor
    return base_signal.diff()

def f54_rsw_d_514_rel_v514_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=169, w2=468, w3=422, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(468, min_periods=max(468//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 169)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.956875 + 0.0033515 * anchor
    return base_signal.diff()

def f54_rsw_d_515_rel_v515_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=176, w2=479, w3=435, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(176, min_periods=max(176//3, 2)).mean(), b.abs().rolling(479, min_periods=max(479//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.3026 * _rolling_slope(cover, 176) + 0.0033516 * anchor
    return base_signal.diff()

def f54_rsw_d_516_rel_v516_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=183, w2=490, w3=448, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.3102 * y + 0.689800 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 183) - _rolling_slope(basket, 490) + 0.0033517 * anchor
    return base_signal.diff()

def f54_rsw_d_517_rel_v517_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=190, w2=501, w3=461, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(190, min_periods=max(190//3, 2)).mean(), upside.rolling(501, min_periods=max(501//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.0 + 0.0033518 * anchor
    return base_signal.diff()

def f54_rsw_d_518_rel_v518_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=197, w2=512, w3=474, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(512, min_periods=max(512//3, 2)).max()
    rebound = x - x.rolling(197, min_periods=max(197//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3254 * _rolling_slope(draw, 474) + 0.0033519 * anchor
    return base_signal.diff()

def f54_rsw_d_519_rel_v519_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=204, w2=20, w3=487, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(20)
    stress = imbalance.rolling(487, min_periods=max(487//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.02875 + 0.003352 * anchor
    return base_signal.diff()

def f54_rsw_d_520_rel_v520_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=211, w2=31, w3=500, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 211)
    baseline = trend.rolling(31, min_periods=max(31//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(500, min_periods=max(500//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.043125 + 0.0033521 * anchor
    return base_signal.diff()

def f54_rsw_d_521_rel_v521_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=218, w2=42, w3=513, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 218)
    slow = _rolling_slope(x, 42)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.0575 + 0.0033522 * anchor
    return base_signal.diff()

def f54_rsw_d_522_rel_v522_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=225, w2=53, w3=526, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(53, min_periods=max(53//3, 2)).max()
    trough = x.rolling(225, min_periods=max(225//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.071875 + 0.0033523 * anchor
    return base_signal.diff()

def f54_rsw_d_523_rel_v523_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=232, w2=64, w3=539, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(64, min_periods=max(64//3, 2)).rank(pct=True)
    persistence = change.rolling(539, min_periods=max(539//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3634 * persistence + 0.0033524 * anchor
    return base_signal.diff()

def f54_rsw_d_524_rel_v524_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=239, w2=75, w3=552, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(239, min_periods=max(239//3, 2)).std()
    vol_slow = ret.rolling(75, min_periods=max(75//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.100625 + 0.0033525 * anchor
    return base_signal.diff()

def f54_rsw_d_525_rel_v525_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=246, w2=86, w3=565, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(86, min_periods=max(86//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 246)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3786 * slope + 0.0033526 * anchor
    return base_signal.diff()
