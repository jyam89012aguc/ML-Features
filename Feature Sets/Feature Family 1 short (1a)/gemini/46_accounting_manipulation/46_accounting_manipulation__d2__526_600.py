"""46 accounting manipulation d2 second derivative features 526-600 â€” Pipeline 1a-HF Grade v3.

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

def f46_aman_526_accrual_v526_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=36, w2=112, w3=252, lag=42)."""
    x = inventory.shift(42)
    impulse = x.diff(36)
    drag = impulse.rolling(112, min_periods=max(112//3, 2)).mean()
    noise = impulse.abs().rolling(252, min_periods=max(252//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.9375 + 0.0028727 * anchor
    return base_signal.diff().diff()

def f46_aman_527_accrual_v527_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=43, w2=123, w3=265, lag=63)."""
    x = _safe_log(revenue.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 43)
    acceleration = _rolling_slope(velocity, 123)
    curvature = _rolling_slope(acceleration, 265)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0482 * acceleration + 0.0028728 * anchor
    return base_signal.diff().diff()

def f46_aman_528_accrual_v528_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=50, w2=134, w3=278, lag=0)."""
    rel = _safe_div(netinc.shift(0), ocf.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 50)
    pressure = rel_log.diff(126)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.0558 * pressure.rolling(278, min_periods=max(278//3, 2)).mean() + 0.0028729 * anchor
    return base_signal.diff().diff()

def f46_aman_529_accrual_v529_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=57, w2=145, w3=291, lag=1)."""
    a = ocf.shift(1)
    b = assetsc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(57, min_periods=max(57//3, 2)).mean())
    decay = spread.ewm(span=145, adjust=False).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.980625 + 0.002873 * anchor
    return base_signal.diff().diff()

def f46_aman_530_accrual_v530_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=64, w2=156, w3=304, lag=2)."""
    a = _safe_log(assetsc.abs() + 1.0).shift(2)
    b = _safe_log(liabilitiesc.abs() + 1.0).shift(2)
    corr = a.rolling(156, min_periods=max(156//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 64)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.995 + 0.0028731 * anchor
    return base_signal.diff().diff()

def f46_aman_531_accrual_v531_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=71, w2=167, w3=317, lag=5)."""
    a = liabilitiesc.shift(5)
    b = inventory.shift(5)
    cover = _safe_div(a.rolling(71, min_periods=max(71//3, 2)).mean(), b.abs().rolling(167, min_periods=max(167//3, 2)).mean())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.0786 * _rolling_slope(cover, 71) + 0.0028732 * anchor
    return base_signal.diff().diff()

def f46_aman_532_accrual_v532_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=78, w2=178, w3=330, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    y = _safe_log(revenue.abs() + 1.0).shift(10)
    z = _safe_log(revenue.abs() + 1.0).shift(10)
    basket = x - 0.0862 * y + 0.913800 * z
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 78) - _rolling_slope(basket, 178) + 0.0028733 * anchor
    return base_signal.diff().diff()

def f46_aman_533_accrual_v533_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=85, w2=189, w3=343, lag=21)."""
    x = revenue.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(85, min_periods=max(85//3, 2)).mean(), upside.rolling(189, min_periods=max(189//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.038125 + 0.0028734 * anchor
    return base_signal.diff().diff()

def f46_aman_534_accrual_v534_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=92, w2=200, w3=356, lag=42)."""
    x = _safe_log(netinc.abs() + 1.0).shift(42)
    draw = x - x.rolling(200, min_periods=max(200//3, 2)).max()
    rebound = x - x.rolling(92, min_periods=max(92//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1014 * _rolling_slope(draw, 356) + 0.0028735 * anchor
    return base_signal.diff().diff()

def f46_aman_535_accrual_v535_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=99, w2=211, w3=369, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(99) - b.diff(126)
    stress = imbalance.rolling(369, min_periods=max(369//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.066875 + 0.0028736 * anchor
    return base_signal.diff().diff()

def f46_aman_536_accrual_v536_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=106, w2=222, w3=382, lag=0)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 106)
    baseline = trend.rolling(222, min_periods=max(222//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(382, min_periods=max(382//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.08125 + 0.0028737 * anchor
    return base_signal.diff().diff()

def f46_aman_537_accrual_v537_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=113, w2=233, w3=395, lag=1)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 113)
    slow = _rolling_slope(x, 233)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.095625 + 0.0028738 * anchor
    return base_signal.diff().diff()

def f46_aman_538_accrual_v538_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=120, w2=244, w3=408, lag=2)."""
    x = inventory.shift(2)
    peak = x.rolling(244, min_periods=max(244//3, 2)).max()
    trough = x.rolling(120, min_periods=max(120//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.11 + 0.0028739 * anchor
    return base_signal.diff().diff()

def f46_aman_539_accrual_v539_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=127, w2=255, w3=421, lag=5)."""
    x = revenue.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(255, min_periods=max(255//3, 2)).rank(pct=True)
    persistence = change.rolling(421, min_periods=max(421//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1394 * persistence + 0.002874 * anchor
    return base_signal.diff().diff()

def f46_aman_540_accrual_v540_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=134, w2=266, w3=434, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(134, min_periods=max(134//3, 2)).std()
    vol_slow = ret.rolling(266, min_periods=max(266//3, 2)).std()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.13875 + 0.0028741 * anchor
    return base_signal.diff().diff()

def f46_aman_541_accrual_v541_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=141, w2=277, w3=447, lag=21)."""
    x = ocf.shift(21)
    ma = x.rolling(277, min_periods=max(277//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 141)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1546 * slope + 0.0028742 * anchor
    return base_signal.diff().diff()

def f46_aman_542_accrual_v542_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=148, w2=288, w3=460, lag=42)."""
    x = assetsc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(288, min_periods=max(288//3, 2)).mean()
    noise = impulse.abs().rolling(460, min_periods=max(460//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.1675 + 0.0028743 * anchor
    return base_signal.diff().diff()

def f46_aman_543_accrual_v543_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=155, w2=299, w3=473, lag=63)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 155)
    acceleration = _rolling_slope(velocity, 299)
    curvature = _rolling_slope(acceleration, 473)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1698 * acceleration + 0.0028744 * anchor
    return base_signal.diff().diff()

def f46_aman_544_accrual_v544_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=162, w2=310, w3=486, lag=0)."""
    rel = _safe_div(inventory.shift(0), revenue.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 162)
    pressure = rel_log.diff(126)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.1774 * pressure.rolling(486, min_periods=max(486//3, 2)).mean() + 0.0028745 * anchor
    return base_signal.diff().diff()

def f46_aman_545_accrual_v545_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=169, w2=321, w3=499, lag=1)."""
    a = revenue.shift(1)
    b = netinc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(169, min_periods=max(169//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.210625 + 0.0028746 * anchor
    return base_signal.diff().diff()

def f46_aman_546_accrual_v546_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=176, w2=332, w3=512, lag=2)."""
    a = _safe_log(netinc.abs() + 1.0).shift(2)
    b = _safe_log(ocf.abs() + 1.0).shift(2)
    corr = a.rolling(332, min_periods=max(332//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 176)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.225 + 0.0028747 * anchor
    return base_signal.diff().diff()

def f46_aman_547_accrual_v547_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=183, w2=343, w3=525, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(183, min_periods=max(183//3, 2)).mean(), b.abs().rolling(343, min_periods=max(343//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.2002 * _rolling_slope(cover, 183) + 0.0028748 * anchor
    return base_signal.diff().diff()

def f46_aman_548_accrual_v548_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=190, w2=354, w3=538, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    y = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    z = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    basket = x - 0.2078 * y + 0.792200 * z
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 190) - _rolling_slope(basket, 354) + 0.0028749 * anchor
    return base_signal.diff().diff()

def f46_aman_549_accrual_v549_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=197, w2=365, w3=551, lag=21)."""
    x = liabilitiesc.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(197, min_periods=max(197//3, 2)).mean(), upside.rolling(365, min_periods=max(365//3, 2)).mean().abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.268125 + 0.002875 * anchor
    return base_signal.diff().diff()

def f46_aman_550_accrual_v550_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=204, w2=376, w3=564, lag=42)."""
    x = _safe_log(inventory.abs() + 1.0).shift(42)
    draw = x - x.rolling(376, min_periods=max(376//3, 2)).max()
    rebound = x - x.rolling(204, min_periods=max(204//3, 2)).min()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.223 * _rolling_slope(draw, 564) + 0.0028751 * anchor
    return base_signal.diff().diff()

def f46_aman_551_accrual_v551_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=211, w2=387, w3=577, lag=63)."""
    a = _safe_log(revenue.abs() + 1.0).shift(63)
    b = _safe_log(netinc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(577, min_periods=max(577//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.296875 + 0.0028752 * anchor
    return base_signal.diff().diff()

def f46_aman_552_accrual_v552_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=218, w2=398, w3=590, lag=0)."""
    x = _safe_log(netinc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 218)
    baseline = trend.rolling(398, min_periods=max(398//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(590, min_periods=max(590//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.31125 + 0.0028753 * anchor
    return base_signal.diff().diff()

def f46_aman_553_accrual_v553_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=225, w2=409, w3=603, lag=1)."""
    x = _safe_log(ocf.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 225)
    slow = _rolling_slope(x, 409)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.325625 + 0.0028754 * anchor
    return base_signal.diff().diff()

def f46_aman_554_accrual_v554_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=232, w2=420, w3=616, lag=2)."""
    x = assetsc.shift(2)
    peak = x.rolling(420, min_periods=max(420//3, 2)).max()
    trough = x.rolling(232, min_periods=max(232//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.34 + 0.0028755 * anchor
    return base_signal.diff().diff()

def f46_aman_555_accrual_v555_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=239, w2=431, w3=629, lag=5)."""
    x = liabilitiesc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(431, min_periods=max(431//3, 2)).rank(pct=True)
    persistence = change.rolling(629, min_periods=max(629//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.261 * persistence + 0.0028756 * anchor
    return base_signal.diff().diff()

def f46_aman_556_accrual_v556_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=246, w2=442, w3=642, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(246, min_periods=max(246//3, 2)).std()
    vol_slow = ret.rolling(442, min_periods=max(442//3, 2)).std()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.36875 + 0.0028757 * anchor
    return base_signal.diff().diff()

def f46_aman_557_accrual_v557_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=253, w2=453, w3=655, lag=21)."""
    x = revenue.shift(21)
    ma = x.rolling(453, min_periods=max(453//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 253)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2762 * slope + 0.0028758 * anchor
    return base_signal.diff().diff()

def f46_aman_558_accrual_v558_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=9, w2=464, w3=668, lag=42)."""
    x = netinc.shift(42)
    impulse = x.diff(9)
    drag = impulse.rolling(464, min_periods=max(464//3, 2)).mean()
    noise = impulse.abs().rolling(668, min_periods=max(668//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.3975 + 0.0028759 * anchor
    return base_signal.diff().diff()

def f46_aman_559_accrual_v559_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=16, w2=475, w3=681, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 16)
    acceleration = _rolling_slope(velocity, 475)
    curvature = _rolling_slope(acceleration, 681)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2914 * acceleration + 0.002876 * anchor
    return base_signal.diff().diff()

def f46_aman_560_accrual_v560_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=23, w2=486, w3=694, lag=0)."""
    rel = _safe_div(assetsc.shift(0), liabilitiesc.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 23)
    pressure = rel_log.diff(126)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.299 * pressure.rolling(694, min_periods=max(694//3, 2)).mean() + 0.0028761 * anchor
    return base_signal.diff().diff()

def f46_aman_561_accrual_v561_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=30, w2=497, w3=707, lag=1)."""
    a = liabilitiesc.shift(1)
    b = inventory.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(30, min_periods=max(30//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.440625 + 0.0028762 * anchor
    return base_signal.diff().diff()

def f46_aman_562_accrual_v562_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=37, w2=508, w3=720, lag=2)."""
    a = _safe_log(inventory.abs() + 1.0).shift(2)
    b = _safe_log(revenue.abs() + 1.0).shift(2)
    corr = a.rolling(508, min_periods=max(508//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 37)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.455 + 0.0028763 * anchor
    return base_signal.diff().diff()

def f46_aman_563_accrual_v563_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=44, w2=16, w3=733, lag=5)."""
    a = revenue.shift(5)
    b = netinc.shift(5)
    cover = _safe_div(a.rolling(44, min_periods=max(44//3, 2)).mean(), b.abs().rolling(16, min_periods=max(16//3, 2)).mean())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.3218 * _rolling_slope(cover, 44) + 0.0028764 * anchor
    return base_signal.diff().diff()

def f46_aman_564_accrual_v564_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=51, w2=27, w3=746, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    y = _safe_log(ocf.abs() + 1.0).shift(10)
    z = _safe_log(ocf.abs() + 1.0).shift(10)
    basket = x - 0.3294 * y + 0.670600 * z
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 51) - _rolling_slope(basket, 27) + 0.0028765 * anchor
    return base_signal.diff().diff()

def f46_aman_565_accrual_v565_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=58, w2=38, w3=759, lag=21)."""
    x = ocf.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(58, min_periods=max(58//3, 2)).mean(), upside.rolling(38, min_periods=max(38//3, 2)).mean().abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.498125 + 0.0028766 * anchor
    return base_signal.diff().diff()

def f46_aman_566_accrual_v566_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=65, w2=49, w3=15, lag=42)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(42)
    draw = x - x.rolling(49, min_periods=max(49//3, 2)).max()
    rebound = x - x.rolling(65, min_periods=max(65//3, 2)).min()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3446 * _rolling_slope(draw, 15) + 0.0028767 * anchor
    return base_signal.diff().diff()

def f46_aman_567_accrual_v567_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=72, w2=60, w3=28, lag=63)."""
    a = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    b = _safe_log(inventory.abs() + 1.0).shift(63)
    imbalance = a.diff(72) - b.diff(60)
    stress = imbalance.rolling(28, min_periods=max(28//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.526875 + 0.0028768 * anchor
    return base_signal.diff().diff()

def f46_aman_568_accrual_v568_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=79, w2=71, w3=41, lag=0)."""
    x = _safe_log(inventory.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 79)
    baseline = trend.rolling(71, min_periods=max(71//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(41, min_periods=max(41//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.54125 + 0.0028769 * anchor
    return base_signal.diff().diff()

def f46_aman_569_accrual_v569_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=86, w2=82, w3=54, lag=1)."""
    x = _safe_log(revenue.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 86)
    slow = _rolling_slope(x, 82)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=54, adjust=False).mean() * 1.555625 + 0.002877 * anchor
    return base_signal.diff().diff()

def f46_aman_570_accrual_v570_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=93, w2=93, w3=67, lag=2)."""
    x = netinc.shift(2)
    peak = x.rolling(93, min_periods=max(93//3, 2)).max()
    trough = x.rolling(93, min_periods=max(93//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.57 + 0.0028771 * anchor
    return base_signal.diff().diff()

def f46_aman_571_accrual_v571_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=100, w2=104, w3=80, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(100)
    rank = change.rolling(104, min_periods=max(104//3, 2)).rank(pct=True)
    persistence = change.rolling(80, min_periods=max(80//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3826 * persistence + 0.0028772 * anchor
    return base_signal.diff().diff()

def f46_aman_572_accrual_v572_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=107, w2=115, w3=93, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(107, min_periods=max(107//3, 2)).std()
    vol_slow = ret.rolling(115, min_periods=max(115//3, 2)).std()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.59875 + 0.0028773 * anchor
    return base_signal.diff().diff()

def f46_aman_573_accrual_v573_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=114, w2=126, w3=106, lag=21)."""
    x = liabilitiesc.shift(21)
    ma = x.rolling(126, min_periods=max(126//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 114)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3978 * slope + 0.0028774 * anchor
    return base_signal.diff().diff()

def f46_aman_574_accrual_v574_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=121, w2=137, w3=119, lag=42)."""
    x = inventory.shift(42)
    impulse = x.diff(121)
    drag = impulse.rolling(137, min_periods=max(137//3, 2)).mean()
    noise = impulse.abs().rolling(119, min_periods=max(119//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.854375 + 0.0028775 * anchor
    return base_signal.diff().diff()

def f46_aman_575_accrual_v575_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=128, w2=148, w3=132, lag=63)."""
    x = _safe_log(revenue.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 128)
    acceleration = _rolling_slope(velocity, 148)
    curvature = _rolling_slope(acceleration, 132)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0366 * acceleration + 0.0028776 * anchor
    return base_signal.diff().diff()

def f46_aman_576_accrual_v576_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=135, w2=159, w3=145, lag=0)."""
    rel = _safe_div(netinc.shift(0), ocf.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 135)
    pressure = rel_log.diff(126)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.0442 * pressure.rolling(145, min_periods=max(145//3, 2)).mean() + 0.0028777 * anchor
    return base_signal.diff().diff()

def f46_aman_577_accrual_v577_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=142, w2=170, w3=158, lag=1)."""
    a = ocf.shift(1)
    b = assetsc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(142, min_periods=max(142//3, 2)).mean())
    decay = spread.ewm(span=170, adjust=False).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.8975 + 0.0028778 * anchor
    return base_signal.diff().diff()

def f46_aman_578_accrual_v578_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=149, w2=181, w3=171, lag=2)."""
    a = _safe_log(assetsc.abs() + 1.0).shift(2)
    b = _safe_log(liabilitiesc.abs() + 1.0).shift(2)
    corr = a.rolling(181, min_periods=max(181//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 149)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.911875 + 0.0028779 * anchor
    return base_signal.diff().diff()

def f46_aman_579_accrual_v579_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=156, w2=192, w3=184, lag=5)."""
    a = liabilitiesc.shift(5)
    b = inventory.shift(5)
    cover = _safe_div(a.rolling(156, min_periods=max(156//3, 2)).mean(), b.abs().rolling(192, min_periods=max(192//3, 2)).mean())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.067 * _rolling_slope(cover, 156) + 0.002878 * anchor
    return base_signal.diff().diff()

def f46_aman_580_accrual_v580_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=163, w2=203, w3=197, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    y = _safe_log(revenue.abs() + 1.0).shift(10)
    z = _safe_log(revenue.abs() + 1.0).shift(10)
    basket = x - 0.0746 * y + 0.925400 * z
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 163) - _rolling_slope(basket, 203) + 0.0028781 * anchor
    return base_signal.diff().diff()

def f46_aman_581_accrual_v581_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=170, w2=214, w3=210, lag=21)."""
    x = revenue.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(170, min_periods=max(170//3, 2)).mean(), upside.rolling(214, min_periods=max(214//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.955 + 0.0028782 * anchor
    return base_signal.diff().diff()

def f46_aman_582_accrual_v582_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=177, w2=225, w3=223, lag=42)."""
    x = _safe_log(netinc.abs() + 1.0).shift(42)
    draw = x - x.rolling(225, min_periods=max(225//3, 2)).max()
    rebound = x - x.rolling(177, min_periods=max(177//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0898 * _rolling_slope(draw, 223) + 0.0028783 * anchor
    return base_signal.diff().diff()

def f46_aman_583_accrual_v583_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=184, w2=236, w3=236, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(236, min_periods=max(236//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.98375 + 0.0028784 * anchor
    return base_signal.diff().diff()

def f46_aman_584_accrual_v584_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=191, w2=247, w3=249, lag=0)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 191)
    baseline = trend.rolling(247, min_periods=max(247//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(249, min_periods=max(249//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.998125 + 0.0028785 * anchor
    return base_signal.diff().diff()

def f46_aman_585_accrual_v585_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=198, w2=258, w3=262, lag=1)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 198)
    slow = _rolling_slope(x, 258)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=262, adjust=False).mean() * 1.0125 + 0.0028786 * anchor
    return base_signal.diff().diff()

def f46_aman_586_accrual_v586_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=205, w2=269, w3=275, lag=2)."""
    x = inventory.shift(2)
    peak = x.rolling(269, min_periods=max(269//3, 2)).max()
    trough = x.rolling(205, min_periods=max(205//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.026875 + 0.0028787 * anchor
    return base_signal.diff().diff()

def f46_aman_587_accrual_v587_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=212, w2=280, w3=288, lag=5)."""
    x = revenue.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(280, min_periods=max(280//3, 2)).rank(pct=True)
    persistence = change.rolling(288, min_periods=max(288//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1278 * persistence + 0.0028788 * anchor
    return base_signal.diff().diff()

def f46_aman_588_accrual_v588_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=219, w2=291, w3=301, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(219, min_periods=max(219//3, 2)).std()
    vol_slow = ret.rolling(291, min_periods=max(291//3, 2)).std()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.055625 + 0.0028789 * anchor
    return base_signal.diff().diff()

def f46_aman_589_accrual_v589_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=226, w2=302, w3=314, lag=21)."""
    x = ocf.shift(21)
    ma = x.rolling(302, min_periods=max(302//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 226)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.143 * slope + 0.002879 * anchor
    return base_signal.diff().diff()

def f46_aman_590_accrual_v590_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=233, w2=313, w3=327, lag=42)."""
    x = assetsc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(313, min_periods=max(313//3, 2)).mean()
    noise = impulse.abs().rolling(327, min_periods=max(327//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.084375 + 0.0028791 * anchor
    return base_signal.diff().diff()

def f46_aman_591_accrual_v591_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=240, w2=324, w3=340, lag=63)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 240)
    acceleration = _rolling_slope(velocity, 324)
    curvature = _rolling_slope(acceleration, 340)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1582 * acceleration + 0.0028792 * anchor
    return base_signal.diff().diff()

def f46_aman_592_accrual_v592_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=247, w2=335, w3=353, lag=0)."""
    rel = _safe_div(inventory.shift(0), revenue.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 247)
    pressure = rel_log.diff(126)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.1658 * pressure.rolling(353, min_periods=max(353//3, 2)).mean() + 0.0028793 * anchor
    return base_signal.diff().diff()

def f46_aman_593_accrual_v593_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=254, w2=346, w3=366, lag=1)."""
    a = revenue.shift(1)
    b = netinc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(254, min_periods=max(254//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.1275 + 0.0028794 * anchor
    return base_signal.diff().diff()

def f46_aman_594_accrual_v594_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=10, w2=357, w3=379, lag=2)."""
    a = _safe_log(netinc.abs() + 1.0).shift(2)
    b = _safe_log(ocf.abs() + 1.0).shift(2)
    corr = a.rolling(357, min_periods=max(357//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 10)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.141875 + 0.0028795 * anchor
    return base_signal.diff().diff()

def f46_aman_595_accrual_v595_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=17, w2=368, w3=392, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(17, min_periods=max(17//3, 2)).mean(), b.abs().rolling(368, min_periods=max(368//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.1886 * _rolling_slope(cover, 17) + 0.0028796 * anchor
    return base_signal.diff().diff()

def f46_aman_596_accrual_v596_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=24, w2=379, w3=405, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    y = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    z = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    basket = x - 0.1962 * y + 0.803800 * z
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 24) - _rolling_slope(basket, 379) + 0.0028797 * anchor
    return base_signal.diff().diff()

def f46_aman_597_accrual_v597_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=31, w2=390, w3=418, lag=21)."""
    x = liabilitiesc.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(31, min_periods=max(31//3, 2)).mean(), upside.rolling(390, min_periods=max(390//3, 2)).mean().abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.185 + 0.0028798 * anchor
    return base_signal.diff().diff()

def f46_aman_598_accrual_v598_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=38, w2=401, w3=431, lag=42)."""
    x = _safe_log(inventory.abs() + 1.0).shift(42)
    draw = x - x.rolling(401, min_periods=max(401//3, 2)).max()
    rebound = x - x.rolling(38, min_periods=max(38//3, 2)).min()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2114 * _rolling_slope(draw, 431) + 0.0028799 * anchor
    return base_signal.diff().diff()

def f46_aman_599_accrual_v599_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=45, w2=412, w3=444, lag=63)."""
    a = _safe_log(revenue.abs() + 1.0).shift(63)
    b = _safe_log(netinc.abs() + 1.0).shift(63)
    imbalance = a.diff(45) - b.diff(126)
    stress = imbalance.rolling(444, min_periods=max(444//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.21375 + 0.00288 * anchor
    return base_signal.diff().diff()

def f46_aman_600_accrual_v600_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=52, w2=423, w3=457, lag=0)."""
    x = _safe_log(netinc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 52)
    baseline = trend.rolling(423, min_periods=max(423//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(457, min_periods=max(457//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.228125 + 0.0028801 * anchor
    return base_signal.diff().diff()
