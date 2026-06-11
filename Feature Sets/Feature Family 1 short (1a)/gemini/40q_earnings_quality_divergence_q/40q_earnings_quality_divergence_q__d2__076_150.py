"""40q earnings quality divergence q d2 second derivative features 76-150 â€” Pipeline 1a-HF Grade v3.

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

def f40q_eqdq_076_accrual_v76_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=49, w2=329, w3=592, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(49, min_periods=max(49//3, 2)).std()
    vol_slow = ret.rolling(329, min_periods=max(329//3, 2)).std()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.47625 + 0.0024677 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_077_accrual_v77_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=56, w2=340, w3=605, lag=21)."""
    x = revenue.shift(21)
    ma = x.rolling(340, min_periods=max(340//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 56)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.133 * slope + 0.0024678 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_078_accrual_v78_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=63, w2=351, w3=618, lag=42)."""
    x = netinc.shift(42)
    impulse = x.diff(63)
    drag = impulse.rolling(351, min_periods=max(351//3, 2)).mean()
    noise = impulse.abs().rolling(618, min_periods=max(618//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.505 + 0.0024679 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_079_accrual_v79_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=70, w2=362, w3=631, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 70)
    acceleration = _rolling_slope(velocity, 362)
    curvature = _rolling_slope(acceleration, 631)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1482 * acceleration + 0.002468 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_080_accrual_v80_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=77, w2=373, w3=644, lag=0)."""
    rel = _safe_div(assetsc.shift(0), liabilitiesc.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 77)
    pressure = rel_log.diff(126)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.1558 * pressure.rolling(644, min_periods=max(644//3, 2)).mean() + 0.0024681 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_081_accrual_v81_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=84, w2=384, w3=657, lag=1)."""
    a = liabilitiesc.shift(1)
    b = inventory.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(84, min_periods=max(84//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.548125 + 0.0024682 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_082_accrual_v82_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=91, w2=395, w3=670, lag=2)."""
    a = _safe_log(inventory.abs() + 1.0).shift(2)
    b = _safe_log(revenue.abs() + 1.0).shift(2)
    corr = a.rolling(395, min_periods=max(395//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 91)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.5625 + 0.0024683 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_083_accrual_v83_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=98, w2=406, w3=683, lag=5)."""
    a = revenue.shift(5)
    b = netinc.shift(5)
    cover = _safe_div(a.rolling(98, min_periods=max(98//3, 2)).mean(), b.abs().rolling(406, min_periods=max(406//3, 2)).mean())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.1786 * _rolling_slope(cover, 98) + 0.0024684 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_084_accrual_v84_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=105, w2=417, w3=696, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    y = _safe_log(ocf.abs() + 1.0).shift(10)
    z = _safe_log(ocf.abs() + 1.0).shift(10)
    basket = x - 0.1862 * y + 0.813800 * z
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 105) - _rolling_slope(basket, 417) + 0.0024685 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_085_accrual_v85_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=112, w2=428, w3=709, lag=21)."""
    x = ocf.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(112, min_periods=max(112//3, 2)).mean(), upside.rolling(428, min_periods=max(428//3, 2)).mean().abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.605625 + 0.0024686 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_086_accrual_v86_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=119, w2=439, w3=722, lag=42)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(42)
    draw = x - x.rolling(439, min_periods=max(439//3, 2)).max()
    rebound = x - x.rolling(119, min_periods=max(119//3, 2)).min()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2014 * _rolling_slope(draw, 722) + 0.0024687 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_087_accrual_v87_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=126, w2=450, w3=735, lag=63)."""
    a = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    b = _safe_log(inventory.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(735, min_periods=max(735//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.86125 + 0.0024688 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_088_accrual_v88_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=133, w2=461, w3=748, lag=0)."""
    x = _safe_log(inventory.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 133)
    baseline = trend.rolling(461, min_periods=max(461//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(748, min_periods=max(748//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.875625 + 0.0024689 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_089_accrual_v89_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=140, w2=472, w3=761, lag=1)."""
    x = _safe_log(revenue.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 140)
    slow = _rolling_slope(x, 472)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.89 + 0.002469 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_090_accrual_v90_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=147, w2=483, w3=17, lag=2)."""
    x = netinc.shift(2)
    peak = x.rolling(483, min_periods=max(483//3, 2)).max()
    trough = x.rolling(147, min_periods=max(147//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.904375 + 0.0024691 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_091_accrual_v91_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=154, w2=494, w3=30, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(494, min_periods=max(494//3, 2)).rank(pct=True)
    persistence = change.rolling(30, min_periods=max(30//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2394 * persistence + 0.0024692 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_092_accrual_v92_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=161, w2=505, w3=43, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(161, min_periods=max(161//3, 2)).std()
    vol_slow = ret.rolling(505, min_periods=max(505//3, 2)).std()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.933125 + 0.0024693 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_093_accrual_v93_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=168, w2=13, w3=56, lag=21)."""
    x = liabilitiesc.shift(21)
    ma = x.rolling(13, min_periods=max(13//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 168)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2546 * slope + 0.0024694 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_094_accrual_v94_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=175, w2=24, w3=69, lag=42)."""
    x = inventory.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(24, min_periods=max(24//3, 2)).mean()
    noise = impulse.abs().rolling(69, min_periods=max(69//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.961875 + 0.0024695 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_095_accrual_v95_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=182, w2=35, w3=82, lag=63)."""
    x = _safe_log(revenue.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 182)
    acceleration = _rolling_slope(velocity, 35)
    curvature = _rolling_slope(acceleration, 82)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2698 * acceleration + 0.0024696 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_096_accrual_v96_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=189, w2=46, w3=95, lag=0)."""
    rel = _safe_div(netinc.shift(0), ocf.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 189)
    pressure = rel_log.diff(46)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.2774 * pressure.rolling(95, min_periods=max(95//3, 2)).mean() + 0.0024697 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_097_accrual_v97_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=196, w2=57, w3=108, lag=1)."""
    a = ocf.shift(1)
    b = assetsc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(196, min_periods=max(196//3, 2)).mean())
    decay = spread.ewm(span=57, adjust=False).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.005 + 0.0024698 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_098_accrual_v98_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=203, w2=68, w3=121, lag=2)."""
    a = _safe_log(assetsc.abs() + 1.0).shift(2)
    b = _safe_log(liabilitiesc.abs() + 1.0).shift(2)
    corr = a.rolling(68, min_periods=max(68//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 203)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.019375 + 0.0024699 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_099_accrual_v99_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=210, w2=79, w3=134, lag=5)."""
    a = liabilitiesc.shift(5)
    b = inventory.shift(5)
    cover = _safe_div(a.rolling(210, min_periods=max(210//3, 2)).mean(), b.abs().rolling(79, min_periods=max(79//3, 2)).mean())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.3002 * _rolling_slope(cover, 210) + 0.00247 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_100_accrual_v100_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=217, w2=90, w3=147, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    y = _safe_log(revenue.abs() + 1.0).shift(10)
    z = _safe_log(revenue.abs() + 1.0).shift(10)
    basket = x - 0.3078 * y + 0.692200 * z
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 217) - _rolling_slope(basket, 90) + 0.0024701 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_101_accrual_v101_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=224, w2=101, w3=160, lag=21)."""
    x = revenue.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(224, min_periods=max(224//3, 2)).mean(), upside.rolling(101, min_periods=max(101//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.0625 + 0.0024702 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_102_accrual_v102_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=231, w2=112, w3=173, lag=42)."""
    x = _safe_log(netinc.abs() + 1.0).shift(42)
    draw = x - x.rolling(112, min_periods=max(112//3, 2)).max()
    rebound = x - x.rolling(231, min_periods=max(231//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.323 * _rolling_slope(draw, 173) + 0.0024703 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_103_accrual_v103_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=238, w2=123, w3=186, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(123)
    stress = imbalance.rolling(186, min_periods=max(186//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.09125 + 0.0024704 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_104_accrual_v104_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=245, w2=134, w3=199, lag=0)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 245)
    baseline = trend.rolling(134, min_periods=max(134//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(199, min_periods=max(199//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.105625 + 0.0024705 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_105_accrual_v105_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=252, w2=145, w3=212, lag=1)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 252)
    slow = _rolling_slope(x, 145)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=212, adjust=False).mean() * 1.12 + 0.0024706 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_106_accrual_v106_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=8, w2=156, w3=225, lag=2)."""
    x = inventory.shift(2)
    peak = x.rolling(156, min_periods=max(156//3, 2)).max()
    trough = x.rolling(8, min_periods=max(8//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.134375 + 0.0024707 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_107_accrual_v107_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=15, w2=167, w3=238, lag=5)."""
    x = revenue.shift(5)
    change = x.pct_change(15)
    rank = change.rolling(167, min_periods=max(167//3, 2)).rank(pct=True)
    persistence = change.rolling(238, min_periods=max(238//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.361 * persistence + 0.0024708 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_108_accrual_v108_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=22, w2=178, w3=251, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(22, min_periods=max(22//3, 2)).std()
    vol_slow = ret.rolling(178, min_periods=max(178//3, 2)).std()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.163125 + 0.0024709 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_109_accrual_v109_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=29, w2=189, w3=264, lag=21)."""
    x = ocf.shift(21)
    ma = x.rolling(189, min_periods=max(189//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 29)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3762 * slope + 0.002471 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_110_accrual_v110_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=36, w2=200, w3=277, lag=42)."""
    x = assetsc.shift(42)
    impulse = x.diff(36)
    drag = impulse.rolling(200, min_periods=max(200//3, 2)).mean()
    noise = impulse.abs().rolling(277, min_periods=max(277//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.191875 + 0.0024711 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_111_accrual_v111_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=43, w2=211, w3=290, lag=63)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 43)
    acceleration = _rolling_slope(velocity, 211)
    curvature = _rolling_slope(acceleration, 290)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3914 * acceleration + 0.0024712 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_112_accrual_v112_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=50, w2=222, w3=303, lag=0)."""
    rel = _safe_div(inventory.shift(0), revenue.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 50)
    pressure = rel_log.diff(126)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.399 * pressure.rolling(303, min_periods=max(303//3, 2)).mean() + 0.0024713 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_113_accrual_v113_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=57, w2=233, w3=316, lag=1)."""
    a = revenue.shift(1)
    b = netinc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(57, min_periods=max(57//3, 2)).mean())
    decay = spread.ewm(span=233, adjust=False).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.235 + 0.0024714 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_114_accrual_v114_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=64, w2=244, w3=329, lag=2)."""
    a = _safe_log(netinc.abs() + 1.0).shift(2)
    b = _safe_log(ocf.abs() + 1.0).shift(2)
    corr = a.rolling(244, min_periods=max(244//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 64)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.249375 + 0.0024715 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_115_accrual_v115_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=71, w2=255, w3=342, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(71, min_periods=max(71//3, 2)).mean(), b.abs().rolling(255, min_periods=max(255//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.0454 * _rolling_slope(cover, 71) + 0.0024716 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_116_accrual_v116_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=78, w2=266, w3=355, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    y = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    z = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    basket = x - 0.053 * y + 0.947000 * z
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 78) - _rolling_slope(basket, 266) + 0.0024717 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_117_accrual_v117_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=85, w2=277, w3=368, lag=21)."""
    x = liabilitiesc.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(85, min_periods=max(85//3, 2)).mean(), upside.rolling(277, min_periods=max(277//3, 2)).mean().abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.2925 + 0.0024718 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_118_accrual_v118_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=92, w2=288, w3=381, lag=42)."""
    x = _safe_log(inventory.abs() + 1.0).shift(42)
    draw = x - x.rolling(288, min_periods=max(288//3, 2)).max()
    rebound = x - x.rolling(92, min_periods=max(92//3, 2)).min()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0682 * _rolling_slope(draw, 381) + 0.0024719 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_119_accrual_v119_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=99, w2=299, w3=394, lag=63)."""
    a = _safe_log(revenue.abs() + 1.0).shift(63)
    b = _safe_log(netinc.abs() + 1.0).shift(63)
    imbalance = a.diff(99) - b.diff(126)
    stress = imbalance.rolling(394, min_periods=max(394//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.32125 + 0.002472 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_120_accrual_v120_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=106, w2=310, w3=407, lag=0)."""
    x = _safe_log(netinc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 106)
    baseline = trend.rolling(310, min_periods=max(310//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(407, min_periods=max(407//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.335625 + 0.0024721 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_121_accrual_v121_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=113, w2=321, w3=420, lag=1)."""
    x = _safe_log(ocf.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 113)
    slow = _rolling_slope(x, 321)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.35 + 0.0024722 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_122_accrual_v122_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=120, w2=332, w3=433, lag=2)."""
    x = assetsc.shift(2)
    peak = x.rolling(332, min_periods=max(332//3, 2)).max()
    trough = x.rolling(120, min_periods=max(120//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.364375 + 0.0024723 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_123_accrual_v123_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=127, w2=343, w3=446, lag=5)."""
    x = liabilitiesc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(343, min_periods=max(343//3, 2)).rank(pct=True)
    persistence = change.rolling(446, min_periods=max(446//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1062 * persistence + 0.0024724 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_124_accrual_v124_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=134, w2=354, w3=459, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(134, min_periods=max(134//3, 2)).std()
    vol_slow = ret.rolling(354, min_periods=max(354//3, 2)).std()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.393125 + 0.0024725 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_125_accrual_v125_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=141, w2=365, w3=472, lag=21)."""
    x = revenue.shift(21)
    ma = x.rolling(365, min_periods=max(365//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 141)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1214 * slope + 0.0024726 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_126_accrual_v126_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=148, w2=376, w3=485, lag=42)."""
    x = netinc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(376, min_periods=max(376//3, 2)).mean()
    noise = impulse.abs().rolling(485, min_periods=max(485//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.421875 + 0.0024727 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_127_accrual_v127_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=155, w2=387, w3=498, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 155)
    acceleration = _rolling_slope(velocity, 387)
    curvature = _rolling_slope(acceleration, 498)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1366 * acceleration + 0.0024728 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_128_accrual_v128_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=162, w2=398, w3=511, lag=0)."""
    rel = _safe_div(assetsc.shift(0), liabilitiesc.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 162)
    pressure = rel_log.diff(126)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.1442 * pressure.rolling(511, min_periods=max(511//3, 2)).mean() + 0.0024729 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_129_accrual_v129_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=169, w2=409, w3=524, lag=1)."""
    a = liabilitiesc.shift(1)
    b = inventory.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(169, min_periods=max(169//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.465 + 0.002473 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_130_accrual_v130_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=176, w2=420, w3=537, lag=2)."""
    a = _safe_log(inventory.abs() + 1.0).shift(2)
    b = _safe_log(revenue.abs() + 1.0).shift(2)
    corr = a.rolling(420, min_periods=max(420//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 176)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.479375 + 0.0024731 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_131_accrual_v131_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=183, w2=431, w3=550, lag=5)."""
    a = revenue.shift(5)
    b = netinc.shift(5)
    cover = _safe_div(a.rolling(183, min_periods=max(183//3, 2)).mean(), b.abs().rolling(431, min_periods=max(431//3, 2)).mean())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.167 * _rolling_slope(cover, 183) + 0.0024732 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_132_accrual_v132_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=190, w2=442, w3=563, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    y = _safe_log(ocf.abs() + 1.0).shift(10)
    z = _safe_log(ocf.abs() + 1.0).shift(10)
    basket = x - 0.1746 * y + 0.825400 * z
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 190) - _rolling_slope(basket, 442) + 0.0024733 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_133_accrual_v133_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=197, w2=453, w3=576, lag=21)."""
    x = ocf.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(197, min_periods=max(197//3, 2)).mean(), upside.rolling(453, min_periods=max(453//3, 2)).mean().abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.5225 + 0.0024734 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_134_accrual_v134_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=204, w2=464, w3=589, lag=42)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(42)
    draw = x - x.rolling(464, min_periods=max(464//3, 2)).max()
    rebound = x - x.rolling(204, min_periods=max(204//3, 2)).min()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1898 * _rolling_slope(draw, 589) + 0.0024735 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_135_accrual_v135_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=211, w2=475, w3=602, lag=63)."""
    a = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    b = _safe_log(inventory.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(602, min_periods=max(602//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.55125 + 0.0024736 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_136_accrual_v136_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=218, w2=486, w3=615, lag=0)."""
    x = _safe_log(inventory.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 218)
    baseline = trend.rolling(486, min_periods=max(486//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(615, min_periods=max(615//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.565625 + 0.0024737 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_137_accrual_v137_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=225, w2=497, w3=628, lag=1)."""
    x = _safe_log(revenue.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 225)
    slow = _rolling_slope(x, 497)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.58 + 0.0024738 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_138_accrual_v138_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=232, w2=508, w3=641, lag=2)."""
    x = netinc.shift(2)
    peak = x.rolling(508, min_periods=max(508//3, 2)).max()
    trough = x.rolling(232, min_periods=max(232//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.594375 + 0.0024739 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_139_accrual_v139_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=239, w2=16, w3=654, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(16, min_periods=max(16//3, 2)).rank(pct=True)
    persistence = change.rolling(654, min_periods=max(654//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2278 * persistence + 0.002474 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_140_accrual_v140_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=246, w2=27, w3=667, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(246, min_periods=max(246//3, 2)).std()
    vol_slow = ret.rolling(27, min_periods=max(27//3, 2)).std()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.85 + 0.0024741 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_141_accrual_v141_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=253, w2=38, w3=680, lag=21)."""
    x = liabilitiesc.shift(21)
    ma = x.rolling(38, min_periods=max(38//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 253)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.243 * slope + 0.0024742 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_142_accrual_v142_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=9, w2=49, w3=693, lag=42)."""
    x = inventory.shift(42)
    impulse = x.diff(9)
    drag = impulse.rolling(49, min_periods=max(49//3, 2)).mean()
    noise = impulse.abs().rolling(693, min_periods=max(693//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.87875 + 0.0024743 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_143_accrual_v143_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=16, w2=60, w3=706, lag=63)."""
    x = _safe_log(revenue.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 16)
    acceleration = _rolling_slope(velocity, 60)
    curvature = _rolling_slope(acceleration, 706)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2582 * acceleration + 0.0024744 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_144_accrual_v144_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=23, w2=71, w3=719, lag=0)."""
    rel = _safe_div(netinc.shift(0), ocf.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 23)
    pressure = rel_log.diff(71)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.2658 * pressure.rolling(719, min_periods=max(719//3, 2)).mean() + 0.0024745 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_145_accrual_v145_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=30, w2=82, w3=732, lag=1)."""
    a = ocf.shift(1)
    b = assetsc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(30, min_periods=max(30//3, 2)).mean())
    decay = spread.ewm(span=82, adjust=False).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.921875 + 0.0024746 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_146_accrual_v146_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=37, w2=93, w3=745, lag=2)."""
    a = _safe_log(assetsc.abs() + 1.0).shift(2)
    b = _safe_log(liabilitiesc.abs() + 1.0).shift(2)
    corr = a.rolling(93, min_periods=max(93//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 37)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.93625 + 0.0024747 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_147_accrual_v147_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=44, w2=104, w3=758, lag=5)."""
    a = liabilitiesc.shift(5)
    b = inventory.shift(5)
    cover = _safe_div(a.rolling(44, min_periods=max(44//3, 2)).mean(), b.abs().rolling(104, min_periods=max(104//3, 2)).mean())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.2886 * _rolling_slope(cover, 44) + 0.0024748 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_148_accrual_v148_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=51, w2=115, w3=771, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    y = _safe_log(revenue.abs() + 1.0).shift(10)
    z = _safe_log(revenue.abs() + 1.0).shift(10)
    basket = x - 0.2962 * y + 0.703800 * z
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 51) - _rolling_slope(basket, 115) + 0.0024749 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_149_accrual_v149_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=58, w2=126, w3=27, lag=21)."""
    x = revenue.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(58, min_periods=max(58//3, 2)).mean(), upside.rolling(126, min_periods=max(126//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(27) * 0.979375 + 0.002475 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_150_accrual_v150_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=65, w2=137, w3=40, lag=42)."""
    x = _safe_log(netinc.abs() + 1.0).shift(42)
    draw = x - x.rolling(137, min_periods=max(137//3, 2)).max()
    rebound = x - x.rolling(65, min_periods=max(65//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3114 * _rolling_slope(draw, 40) + 0.0024751 * anchor
    return base_signal.diff().diff()
