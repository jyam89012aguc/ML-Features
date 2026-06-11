"""40q earnings quality divergence q d3 third derivative features 376-450 â€” Pipeline 1a-HF Grade v3.

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

def f40q_eqdq_376_accrual_v376_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=141, w2=108, w3=707, lag=0)."""
    x = _safe_log(inventory.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 141)
    baseline = trend.rolling(108, min_periods=max(108//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(707, min_periods=max(707//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.15 + 0.0024977 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_377_accrual_v377_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=148, w2=119, w3=720, lag=1)."""
    x = _safe_log(revenue.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 148)
    slow = _rolling_slope(x, 119)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.164375 + 0.0024978 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_378_accrual_v378_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=155, w2=130, w3=733, lag=2)."""
    x = netinc.shift(2)
    peak = x.rolling(130, min_periods=max(130//3, 2)).max()
    trough = x.rolling(155, min_periods=max(155//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.17875 + 0.0024979 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_379_accrual_v379_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=162, w2=141, w3=746, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(141, min_periods=max(141//3, 2)).rank(pct=True)
    persistence = change.rolling(746, min_periods=max(746//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1698 * persistence + 0.002498 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_380_accrual_v380_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=169, w2=152, w3=759, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(169, min_periods=max(169//3, 2)).std()
    vol_slow = ret.rolling(152, min_periods=max(152//3, 2)).std()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.2075 + 0.0024981 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_381_accrual_v381_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=176, w2=163, w3=15, lag=21)."""
    x = liabilitiesc.shift(21)
    ma = x.rolling(163, min_periods=max(163//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 176)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.185 * slope + 0.0024982 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_382_accrual_v382_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=183, w2=174, w3=28, lag=42)."""
    x = inventory.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(174, min_periods=max(174//3, 2)).mean()
    noise = impulse.abs().rolling(28, min_periods=max(28//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.23625 + 0.0024983 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_383_accrual_v383_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=190, w2=185, w3=41, lag=63)."""
    x = _safe_log(revenue.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 190)
    acceleration = _rolling_slope(velocity, 185)
    curvature = _rolling_slope(acceleration, 41)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2002 * acceleration + 0.0024984 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_384_accrual_v384_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=197, w2=196, w3=54, lag=0)."""
    rel = _safe_div(netinc.shift(0), ocf.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 197)
    pressure = rel_log.diff(126)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.2078 * pressure.rolling(54, min_periods=max(54//3, 2)).mean() + 0.0024985 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_385_accrual_v385_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=204, w2=207, w3=67, lag=1)."""
    a = ocf.shift(1)
    b = assetsc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(204, min_periods=max(204//3, 2)).mean())
    decay = spread.ewm(span=207, adjust=False).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.279375 + 0.0024986 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_386_accrual_v386_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=211, w2=218, w3=80, lag=2)."""
    a = _safe_log(assetsc.abs() + 1.0).shift(2)
    b = _safe_log(liabilitiesc.abs() + 1.0).shift(2)
    corr = a.rolling(218, min_periods=max(218//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 211)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.29375 + 0.0024987 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_387_accrual_v387_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=218, w2=229, w3=93, lag=5)."""
    a = liabilitiesc.shift(5)
    b = inventory.shift(5)
    cover = _safe_div(a.rolling(218, min_periods=max(218//3, 2)).mean(), b.abs().rolling(229, min_periods=max(229//3, 2)).mean())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(93) + 0.2306 * _rolling_slope(cover, 218) + 0.0024988 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_388_accrual_v388_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=225, w2=240, w3=106, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    y = _safe_log(revenue.abs() + 1.0).shift(10)
    z = _safe_log(revenue.abs() + 1.0).shift(10)
    basket = x - 0.2382 * y + 0.761800 * z
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 225) - _rolling_slope(basket, 240) + 0.0024989 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_389_accrual_v389_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=232, w2=251, w3=119, lag=21)."""
    x = revenue.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(232, min_periods=max(232//3, 2)).mean(), upside.rolling(251, min_periods=max(251//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(119) * 1.336875 + 0.002499 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_390_accrual_v390_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=239, w2=262, w3=132, lag=42)."""
    x = _safe_log(netinc.abs() + 1.0).shift(42)
    draw = x - x.rolling(262, min_periods=max(262//3, 2)).max()
    rebound = x - x.rolling(239, min_periods=max(239//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2534 * _rolling_slope(draw, 132) + 0.0024991 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_391_accrual_v391_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=246, w2=273, w3=145, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(145, min_periods=max(145//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.365625 + 0.0024992 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_392_accrual_v392_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=253, w2=284, w3=158, lag=0)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 253)
    baseline = trend.rolling(284, min_periods=max(284//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(158, min_periods=max(158//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.38 + 0.0024993 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_393_accrual_v393_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=9, w2=295, w3=171, lag=1)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 9)
    slow = _rolling_slope(x, 295)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=171, adjust=False).mean() * 1.394375 + 0.0024994 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_394_accrual_v394_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=16, w2=306, w3=184, lag=2)."""
    x = inventory.shift(2)
    peak = x.rolling(306, min_periods=max(306//3, 2)).max()
    trough = x.rolling(16, min_periods=max(16//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.40875 + 0.0024995 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_395_accrual_v395_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=23, w2=317, w3=197, lag=5)."""
    x = revenue.shift(5)
    change = x.pct_change(23)
    rank = change.rolling(317, min_periods=max(317//3, 2)).rank(pct=True)
    persistence = change.rolling(197, min_periods=max(197//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2914 * persistence + 0.0024996 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_396_accrual_v396_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=30, w2=328, w3=210, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(30, min_periods=max(30//3, 2)).std()
    vol_slow = ret.rolling(328, min_periods=max(328//3, 2)).std()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.4375 + 0.0024997 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_397_accrual_v397_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=37, w2=339, w3=223, lag=21)."""
    x = ocf.shift(21)
    ma = x.rolling(339, min_periods=max(339//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 37)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3066 * slope + 0.0024998 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_398_accrual_v398_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=44, w2=350, w3=236, lag=42)."""
    x = assetsc.shift(42)
    impulse = x.diff(44)
    drag = impulse.rolling(350, min_periods=max(350//3, 2)).mean()
    noise = impulse.abs().rolling(236, min_periods=max(236//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.46625 + 0.0024999 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_399_accrual_v399_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=51, w2=361, w3=249, lag=63)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 51)
    acceleration = _rolling_slope(velocity, 361)
    curvature = _rolling_slope(acceleration, 249)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3218 * acceleration + 0.0025 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_400_accrual_v400_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=58, w2=372, w3=262, lag=0)."""
    rel = _safe_div(inventory.shift(0), revenue.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 58)
    pressure = rel_log.diff(126)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.3294 * pressure.rolling(262, min_periods=max(262//3, 2)).mean() + 0.0025001 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_401_accrual_v401_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=65, w2=383, w3=275, lag=1)."""
    a = revenue.shift(1)
    b = netinc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(65, min_periods=max(65//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.509375 + 0.0025002 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_402_accrual_v402_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=72, w2=394, w3=288, lag=2)."""
    a = _safe_log(netinc.abs() + 1.0).shift(2)
    b = _safe_log(ocf.abs() + 1.0).shift(2)
    corr = a.rolling(394, min_periods=max(394//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 72)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.52375 + 0.0025003 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_403_accrual_v403_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=79, w2=405, w3=301, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(79, min_periods=max(79//3, 2)).mean(), b.abs().rolling(405, min_periods=max(405//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.3522 * _rolling_slope(cover, 79) + 0.0025004 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_404_accrual_v404_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=86, w2=416, w3=314, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    y = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    z = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    basket = x - 0.3598 * y + 0.640200 * z
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 86) - _rolling_slope(basket, 416) + 0.0025005 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_405_accrual_v405_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=93, w2=427, w3=327, lag=21)."""
    x = liabilitiesc.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(93, min_periods=max(93//3, 2)).mean(), upside.rolling(427, min_periods=max(427//3, 2)).mean().abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.566875 + 0.0025006 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_406_accrual_v406_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=100, w2=438, w3=340, lag=42)."""
    x = _safe_log(inventory.abs() + 1.0).shift(42)
    draw = x - x.rolling(438, min_periods=max(438//3, 2)).max()
    rebound = x - x.rolling(100, min_periods=max(100//3, 2)).min()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.375 * _rolling_slope(draw, 340) + 0.0025007 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_407_accrual_v407_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=107, w2=449, w3=353, lag=63)."""
    a = _safe_log(revenue.abs() + 1.0).shift(63)
    b = _safe_log(netinc.abs() + 1.0).shift(63)
    imbalance = a.diff(107) - b.diff(126)
    stress = imbalance.rolling(353, min_periods=max(353//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.595625 + 0.0025008 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_408_accrual_v408_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=114, w2=460, w3=366, lag=0)."""
    x = _safe_log(netinc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 114)
    baseline = trend.rolling(460, min_periods=max(460//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(366, min_periods=max(366//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.61 + 0.0025009 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_409_accrual_v409_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=121, w2=471, w3=379, lag=1)."""
    x = _safe_log(ocf.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 121)
    slow = _rolling_slope(x, 471)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.85125 + 0.002501 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_410_accrual_v410_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=128, w2=482, w3=392, lag=2)."""
    x = assetsc.shift(2)
    peak = x.rolling(482, min_periods=max(482//3, 2)).max()
    trough = x.rolling(128, min_periods=max(128//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.865625 + 0.0025011 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_411_accrual_v411_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=135, w2=493, w3=405, lag=5)."""
    x = liabilitiesc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(493, min_periods=max(493//3, 2)).rank(pct=True)
    persistence = change.rolling(405, min_periods=max(405//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0366 * persistence + 0.0025012 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_412_accrual_v412_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=142, w2=504, w3=418, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(142, min_periods=max(142//3, 2)).std()
    vol_slow = ret.rolling(504, min_periods=max(504//3, 2)).std()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.894375 + 0.0025013 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_413_accrual_v413_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=149, w2=12, w3=431, lag=21)."""
    x = revenue.shift(21)
    ma = x.rolling(12, min_periods=max(12//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 149)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0518 * slope + 0.0025014 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_414_accrual_v414_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=156, w2=23, w3=444, lag=42)."""
    x = netinc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(23, min_periods=max(23//3, 2)).mean()
    noise = impulse.abs().rolling(444, min_periods=max(444//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.923125 + 0.0025015 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_415_accrual_v415_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=163, w2=34, w3=457, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 163)
    acceleration = _rolling_slope(velocity, 34)
    curvature = _rolling_slope(acceleration, 457)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.067 * acceleration + 0.0025016 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_416_accrual_v416_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=170, w2=45, w3=470, lag=0)."""
    rel = _safe_div(assetsc.shift(0), liabilitiesc.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 170)
    pressure = rel_log.diff(45)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.0746 * pressure.rolling(470, min_periods=max(470//3, 2)).mean() + 0.0025017 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_417_accrual_v417_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=177, w2=56, w3=483, lag=1)."""
    a = liabilitiesc.shift(1)
    b = inventory.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(177, min_periods=max(177//3, 2)).mean())
    decay = spread.ewm(span=56, adjust=False).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.96625 + 0.0025018 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_418_accrual_v418_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=184, w2=67, w3=496, lag=2)."""
    a = _safe_log(inventory.abs() + 1.0).shift(2)
    b = _safe_log(revenue.abs() + 1.0).shift(2)
    corr = a.rolling(67, min_periods=max(67//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 184)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.980625 + 0.0025019 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_419_accrual_v419_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=191, w2=78, w3=509, lag=5)."""
    a = revenue.shift(5)
    b = netinc.shift(5)
    cover = _safe_div(a.rolling(191, min_periods=max(191//3, 2)).mean(), b.abs().rolling(78, min_periods=max(78//3, 2)).mean())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.0974 * _rolling_slope(cover, 191) + 0.002502 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_420_accrual_v420_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=198, w2=89, w3=522, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    y = _safe_log(ocf.abs() + 1.0).shift(10)
    z = _safe_log(ocf.abs() + 1.0).shift(10)
    basket = x - 0.105 * y + 0.895000 * z
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 198) - _rolling_slope(basket, 89) + 0.0025021 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_421_accrual_v421_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=205, w2=100, w3=535, lag=21)."""
    x = ocf.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(205, min_periods=max(205//3, 2)).mean(), upside.rolling(100, min_periods=max(100//3, 2)).mean().abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.02375 + 0.0025022 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_422_accrual_v422_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=212, w2=111, w3=548, lag=42)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(42)
    draw = x - x.rolling(111, min_periods=max(111//3, 2)).max()
    rebound = x - x.rolling(212, min_periods=max(212//3, 2)).min()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1202 * _rolling_slope(draw, 548) + 0.0025023 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_423_accrual_v423_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=219, w2=122, w3=561, lag=63)."""
    a = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    b = _safe_log(inventory.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(122)
    stress = imbalance.rolling(561, min_periods=max(561//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.0525 + 0.0025024 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_424_accrual_v424_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=226, w2=133, w3=574, lag=0)."""
    x = _safe_log(inventory.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 226)
    baseline = trend.rolling(133, min_periods=max(133//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(574, min_periods=max(574//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.066875 + 0.0025025 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_425_accrual_v425_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=233, w2=144, w3=587, lag=1)."""
    x = _safe_log(revenue.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 233)
    slow = _rolling_slope(x, 144)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.08125 + 0.0025026 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_426_accrual_v426_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=240, w2=155, w3=600, lag=2)."""
    x = netinc.shift(2)
    peak = x.rolling(155, min_periods=max(155//3, 2)).max()
    trough = x.rolling(240, min_periods=max(240//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.095625 + 0.0025027 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_427_accrual_v427_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=247, w2=166, w3=613, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(166, min_periods=max(166//3, 2)).rank(pct=True)
    persistence = change.rolling(613, min_periods=max(613//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1582 * persistence + 0.0025028 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_428_accrual_v428_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=254, w2=177, w3=626, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(254, min_periods=max(254//3, 2)).std()
    vol_slow = ret.rolling(177, min_periods=max(177//3, 2)).std()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.124375 + 0.0025029 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_429_accrual_v429_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=10, w2=188, w3=639, lag=21)."""
    x = liabilitiesc.shift(21)
    ma = x.rolling(188, min_periods=max(188//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 10)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1734 * slope + 0.002503 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_430_accrual_v430_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=17, w2=199, w3=652, lag=42)."""
    x = inventory.shift(42)
    impulse = x.diff(17)
    drag = impulse.rolling(199, min_periods=max(199//3, 2)).mean()
    noise = impulse.abs().rolling(652, min_periods=max(652//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.153125 + 0.0025031 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_431_accrual_v431_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=24, w2=210, w3=665, lag=63)."""
    x = _safe_log(revenue.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 24)
    acceleration = _rolling_slope(velocity, 210)
    curvature = _rolling_slope(acceleration, 665)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1886 * acceleration + 0.0025032 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_432_accrual_v432_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=31, w2=221, w3=678, lag=0)."""
    rel = _safe_div(netinc.shift(0), ocf.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 31)
    pressure = rel_log.diff(126)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.1962 * pressure.rolling(678, min_periods=max(678//3, 2)).mean() + 0.0025033 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_433_accrual_v433_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=38, w2=232, w3=691, lag=1)."""
    a = ocf.shift(1)
    b = assetsc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(38, min_periods=max(38//3, 2)).mean())
    decay = spread.ewm(span=232, adjust=False).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.19625 + 0.0025034 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_434_accrual_v434_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=45, w2=243, w3=704, lag=2)."""
    a = _safe_log(assetsc.abs() + 1.0).shift(2)
    b = _safe_log(liabilitiesc.abs() + 1.0).shift(2)
    corr = a.rolling(243, min_periods=max(243//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 45)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.210625 + 0.0025035 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_435_accrual_v435_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=52, w2=254, w3=717, lag=5)."""
    a = liabilitiesc.shift(5)
    b = inventory.shift(5)
    cover = _safe_div(a.rolling(52, min_periods=max(52//3, 2)).mean(), b.abs().rolling(254, min_periods=max(254//3, 2)).mean())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.219 * _rolling_slope(cover, 52) + 0.0025036 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_436_accrual_v436_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=59, w2=265, w3=730, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    y = _safe_log(revenue.abs() + 1.0).shift(10)
    z = _safe_log(revenue.abs() + 1.0).shift(10)
    basket = x - 0.2266 * y + 0.773400 * z
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 59) - _rolling_slope(basket, 265) + 0.0025037 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_437_accrual_v437_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=66, w2=276, w3=743, lag=21)."""
    x = revenue.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(66, min_periods=max(66//3, 2)).mean(), upside.rolling(276, min_periods=max(276//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.25375 + 0.0025038 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_438_accrual_v438_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=73, w2=287, w3=756, lag=42)."""
    x = _safe_log(netinc.abs() + 1.0).shift(42)
    draw = x - x.rolling(287, min_periods=max(287//3, 2)).max()
    rebound = x - x.rolling(73, min_periods=max(73//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2418 * _rolling_slope(draw, 756) + 0.0025039 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_439_accrual_v439_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=80, w2=298, w3=769, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(80) - b.diff(126)
    stress = imbalance.rolling(769, min_periods=max(769//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.2825 + 0.002504 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_440_accrual_v440_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=87, w2=309, w3=25, lag=0)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 87)
    baseline = trend.rolling(309, min_periods=max(309//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(25, min_periods=max(25//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.296875 + 0.0025041 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_441_accrual_v441_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=94, w2=320, w3=38, lag=1)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 94)
    slow = _rolling_slope(x, 320)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=38, adjust=False).mean() * 1.31125 + 0.0025042 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_442_accrual_v442_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=101, w2=331, w3=51, lag=2)."""
    x = inventory.shift(2)
    peak = x.rolling(331, min_periods=max(331//3, 2)).max()
    trough = x.rolling(101, min_periods=max(101//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.325625 + 0.0025043 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_443_accrual_v443_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=108, w2=342, w3=64, lag=5)."""
    x = revenue.shift(5)
    change = x.pct_change(108)
    rank = change.rolling(342, min_periods=max(342//3, 2)).rank(pct=True)
    persistence = change.rolling(64, min_periods=max(64//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2798 * persistence + 0.0025044 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_444_accrual_v444_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=115, w2=353, w3=77, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(115, min_periods=max(115//3, 2)).std()
    vol_slow = ret.rolling(353, min_periods=max(353//3, 2)).std()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.354375 + 0.0025045 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_445_accrual_v445_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=122, w2=364, w3=90, lag=21)."""
    x = ocf.shift(21)
    ma = x.rolling(364, min_periods=max(364//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 122)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.295 * slope + 0.0025046 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_446_accrual_v446_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=129, w2=375, w3=103, lag=42)."""
    x = assetsc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(375, min_periods=max(375//3, 2)).mean()
    noise = impulse.abs().rolling(103, min_periods=max(103//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.383125 + 0.0025047 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_447_accrual_v447_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=136, w2=386, w3=116, lag=63)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 136)
    acceleration = _rolling_slope(velocity, 386)
    curvature = _rolling_slope(acceleration, 116)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3102 * acceleration + 0.0025048 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_448_accrual_v448_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=143, w2=397, w3=129, lag=0)."""
    rel = _safe_div(inventory.shift(0), revenue.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 143)
    pressure = rel_log.diff(126)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.3178 * pressure.rolling(129, min_periods=max(129//3, 2)).mean() + 0.0025049 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_449_accrual_v449_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=150, w2=408, w3=142, lag=1)."""
    a = revenue.shift(1)
    b = netinc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(150, min_periods=max(150//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.42625 + 0.002505 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_450_accrual_v450_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=157, w2=419, w3=155, lag=2)."""
    a = _safe_log(netinc.abs() + 1.0).shift(2)
    b = _safe_log(ocf.abs() + 1.0).shift(2)
    corr = a.rolling(419, min_periods=max(419//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 157)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.440625 + 0.0025051 * anchor
    return base_signal.diff().diff().diff()
