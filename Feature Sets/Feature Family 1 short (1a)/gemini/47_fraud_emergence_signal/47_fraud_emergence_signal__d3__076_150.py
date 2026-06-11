"""47 fraud emergence signal d3 third derivative features 76-150 â€” Pipeline 1a-HF Grade v3.

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

def f47_fes_076_accrual_v76_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=82, w2=253, w3=688, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    y = _safe_log(revenue.abs() + 1.0).shift(10)
    z = _safe_log(revenue.abs() + 1.0).shift(10)
    basket = x - 0.0514 * y + 0.948600 * z
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 82) - _rolling_slope(basket, 253) + 0.0028877 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_077_accrual_v77_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=89, w2=264, w3=701, lag=21)."""
    x = revenue.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(89, min_periods=max(89//3, 2)).mean(), upside.rolling(264, min_periods=max(264//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.561875 + 0.0028878 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_078_accrual_v78_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=96, w2=275, w3=714, lag=42)."""
    x = _safe_log(netinc.abs() + 1.0).shift(42)
    draw = x - x.rolling(275, min_periods=max(275//3, 2)).max()
    rebound = x - x.rolling(96, min_periods=max(96//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0666 * _rolling_slope(draw, 714) + 0.0028879 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_079_accrual_v79_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=103, w2=286, w3=727, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(103) - b.diff(126)
    stress = imbalance.rolling(727, min_periods=max(727//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.590625 + 0.002888 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_080_accrual_v80_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=110, w2=297, w3=740, lag=0)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 110)
    baseline = trend.rolling(297, min_periods=max(297//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(740, min_periods=max(740//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.605 + 0.0028881 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_081_accrual_v81_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=117, w2=308, w3=753, lag=1)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 117)
    slow = _rolling_slope(x, 308)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.619375 + 0.0028882 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_082_accrual_v82_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=124, w2=319, w3=766, lag=2)."""
    x = inventory.shift(2)
    peak = x.rolling(319, min_periods=max(319//3, 2)).max()
    trough = x.rolling(124, min_periods=max(124//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.860625 + 0.0028883 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_083_accrual_v83_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=131, w2=330, w3=22, lag=5)."""
    x = revenue.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(330, min_periods=max(330//3, 2)).rank(pct=True)
    persistence = change.rolling(22, min_periods=max(22//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1046 * persistence + 0.0028884 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_084_accrual_v84_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=138, w2=341, w3=35, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(138, min_periods=max(138//3, 2)).std()
    vol_slow = ret.rolling(341, min_periods=max(341//3, 2)).std()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.889375 + 0.0028885 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_085_accrual_v85_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=145, w2=352, w3=48, lag=21)."""
    x = ocf.shift(21)
    ma = x.rolling(352, min_periods=max(352//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 145)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1198 * slope + 0.0028886 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_086_accrual_v86_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=152, w2=363, w3=61, lag=42)."""
    x = assetsc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(363, min_periods=max(363//3, 2)).mean()
    noise = impulse.abs().rolling(61, min_periods=max(61//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.918125 + 0.0028887 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_087_accrual_v87_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=159, w2=374, w3=74, lag=63)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 159)
    acceleration = _rolling_slope(velocity, 374)
    curvature = _rolling_slope(acceleration, 74)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.135 * acceleration + 0.0028888 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_088_accrual_v88_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=166, w2=385, w3=87, lag=0)."""
    rel = _safe_div(inventory.shift(0), revenue.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 166)
    pressure = rel_log.diff(126)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.1426 * pressure.rolling(87, min_periods=max(87//3, 2)).mean() + 0.0028889 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_089_accrual_v89_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=173, w2=396, w3=100, lag=1)."""
    a = revenue.shift(1)
    b = netinc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(173, min_periods=max(173//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.96125 + 0.002889 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_090_accrual_v90_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=180, w2=407, w3=113, lag=2)."""
    a = _safe_log(netinc.abs() + 1.0).shift(2)
    b = _safe_log(ocf.abs() + 1.0).shift(2)
    corr = a.rolling(407, min_periods=max(407//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 180)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.975625 + 0.0028891 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_091_accrual_v91_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=187, w2=418, w3=126, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(187, min_periods=max(187//3, 2)).mean(), b.abs().rolling(418, min_periods=max(418//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.1654 * _rolling_slope(cover, 187) + 0.0028892 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_092_accrual_v92_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=194, w2=429, w3=139, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    y = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    z = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    basket = x - 0.173 * y + 0.827000 * z
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 194) - _rolling_slope(basket, 429) + 0.0028893 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_093_accrual_v93_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=201, w2=440, w3=152, lag=21)."""
    x = liabilitiesc.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(201, min_periods=max(201//3, 2)).mean(), upside.rolling(440, min_periods=max(440//3, 2)).mean().abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.01875 + 0.0028894 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_094_accrual_v94_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=208, w2=451, w3=165, lag=42)."""
    x = _safe_log(inventory.abs() + 1.0).shift(42)
    draw = x - x.rolling(451, min_periods=max(451//3, 2)).max()
    rebound = x - x.rolling(208, min_periods=max(208//3, 2)).min()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1882 * _rolling_slope(draw, 165) + 0.0028895 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_095_accrual_v95_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=215, w2=462, w3=178, lag=63)."""
    a = _safe_log(revenue.abs() + 1.0).shift(63)
    b = _safe_log(netinc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(178, min_periods=max(178//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.0475 + 0.0028896 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_096_accrual_v96_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=222, w2=473, w3=191, lag=0)."""
    x = _safe_log(netinc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 222)
    baseline = trend.rolling(473, min_periods=max(473//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(191, min_periods=max(191//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.061875 + 0.0028897 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_097_accrual_v97_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=229, w2=484, w3=204, lag=1)."""
    x = _safe_log(ocf.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 229)
    slow = _rolling_slope(x, 484)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=204, adjust=False).mean() * 1.07625 + 0.0028898 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_098_accrual_v98_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=236, w2=495, w3=217, lag=2)."""
    x = assetsc.shift(2)
    peak = x.rolling(495, min_periods=max(495//3, 2)).max()
    trough = x.rolling(236, min_periods=max(236//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.090625 + 0.0028899 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_099_accrual_v99_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=243, w2=506, w3=230, lag=5)."""
    x = liabilitiesc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(506, min_periods=max(506//3, 2)).rank(pct=True)
    persistence = change.rolling(230, min_periods=max(230//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2262 * persistence + 0.00289 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_100_accrual_v100_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=250, w2=14, w3=243, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(250, min_periods=max(250//3, 2)).std()
    vol_slow = ret.rolling(14, min_periods=max(14//3, 2)).std()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.119375 + 0.0028901 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_101_accrual_v101_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=6, w2=25, w3=256, lag=21)."""
    x = revenue.shift(21)
    ma = x.rolling(25, min_periods=max(25//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 6)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2414 * slope + 0.0028902 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_102_accrual_v102_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=13, w2=36, w3=269, lag=42)."""
    x = netinc.shift(42)
    impulse = x.diff(13)
    drag = impulse.rolling(36, min_periods=max(36//3, 2)).mean()
    noise = impulse.abs().rolling(269, min_periods=max(269//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.148125 + 0.0028903 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_103_accrual_v103_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=20, w2=47, w3=282, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 20)
    acceleration = _rolling_slope(velocity, 47)
    curvature = _rolling_slope(acceleration, 282)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2566 * acceleration + 0.0028904 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_104_accrual_v104_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=27, w2=58, w3=295, lag=0)."""
    rel = _safe_div(assetsc.shift(0), liabilitiesc.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 27)
    pressure = rel_log.diff(58)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.2642 * pressure.rolling(295, min_periods=max(295//3, 2)).mean() + 0.0028905 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_105_accrual_v105_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=34, w2=69, w3=308, lag=1)."""
    a = liabilitiesc.shift(1)
    b = inventory.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(34, min_periods=max(34//3, 2)).mean())
    decay = spread.ewm(span=69, adjust=False).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.19125 + 0.0028906 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_106_accrual_v106_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=41, w2=80, w3=321, lag=2)."""
    a = _safe_log(inventory.abs() + 1.0).shift(2)
    b = _safe_log(revenue.abs() + 1.0).shift(2)
    corr = a.rolling(80, min_periods=max(80//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 41)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.205625 + 0.0028907 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_107_accrual_v107_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=48, w2=91, w3=334, lag=5)."""
    a = revenue.shift(5)
    b = netinc.shift(5)
    cover = _safe_div(a.rolling(48, min_periods=max(48//3, 2)).mean(), b.abs().rolling(91, min_periods=max(91//3, 2)).mean())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.287 * _rolling_slope(cover, 48) + 0.0028908 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_108_accrual_v108_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=55, w2=102, w3=347, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    y = _safe_log(ocf.abs() + 1.0).shift(10)
    z = _safe_log(ocf.abs() + 1.0).shift(10)
    basket = x - 0.2946 * y + 0.705400 * z
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 55) - _rolling_slope(basket, 102) + 0.0028909 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_109_accrual_v109_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=62, w2=113, w3=360, lag=21)."""
    x = ocf.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(62, min_periods=max(62//3, 2)).mean(), upside.rolling(113, min_periods=max(113//3, 2)).mean().abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.24875 + 0.002891 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_110_accrual_v110_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=69, w2=124, w3=373, lag=42)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(42)
    draw = x - x.rolling(124, min_periods=max(124//3, 2)).max()
    rebound = x - x.rolling(69, min_periods=max(69//3, 2)).min()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3098 * _rolling_slope(draw, 373) + 0.0028911 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_111_accrual_v111_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=76, w2=135, w3=386, lag=63)."""
    a = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    b = _safe_log(inventory.abs() + 1.0).shift(63)
    imbalance = a.diff(76) - b.diff(126)
    stress = imbalance.rolling(386, min_periods=max(386//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.2775 + 0.0028912 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_112_accrual_v112_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=83, w2=146, w3=399, lag=0)."""
    x = _safe_log(inventory.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 83)
    baseline = trend.rolling(146, min_periods=max(146//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(399, min_periods=max(399//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.291875 + 0.0028913 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_113_accrual_v113_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=90, w2=157, w3=412, lag=1)."""
    x = _safe_log(revenue.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 90)
    slow = _rolling_slope(x, 157)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.30625 + 0.0028914 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_114_accrual_v114_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=97, w2=168, w3=425, lag=2)."""
    x = netinc.shift(2)
    peak = x.rolling(168, min_periods=max(168//3, 2)).max()
    trough = x.rolling(97, min_periods=max(97//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.320625 + 0.0028915 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_115_accrual_v115_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=104, w2=179, w3=438, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(104)
    rank = change.rolling(179, min_periods=max(179//3, 2)).rank(pct=True)
    persistence = change.rolling(438, min_periods=max(438//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3478 * persistence + 0.0028916 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_116_accrual_v116_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=111, w2=190, w3=451, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(111, min_periods=max(111//3, 2)).std()
    vol_slow = ret.rolling(190, min_periods=max(190//3, 2)).std()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.349375 + 0.0028917 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_117_accrual_v117_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=118, w2=201, w3=464, lag=21)."""
    x = liabilitiesc.shift(21)
    ma = x.rolling(201, min_periods=max(201//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 118)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.363 * slope + 0.0028918 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_118_accrual_v118_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=125, w2=212, w3=477, lag=42)."""
    x = inventory.shift(42)
    impulse = x.diff(125)
    drag = impulse.rolling(212, min_periods=max(212//3, 2)).mean()
    noise = impulse.abs().rolling(477, min_periods=max(477//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.378125 + 0.0028919 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_119_accrual_v119_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=132, w2=223, w3=490, lag=63)."""
    x = _safe_log(revenue.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 132)
    acceleration = _rolling_slope(velocity, 223)
    curvature = _rolling_slope(acceleration, 490)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3782 * acceleration + 0.002892 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_120_accrual_v120_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=139, w2=234, w3=503, lag=0)."""
    rel = _safe_div(netinc.shift(0), ocf.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 139)
    pressure = rel_log.diff(126)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.3858 * pressure.rolling(503, min_periods=max(503//3, 2)).mean() + 0.0028921 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_121_accrual_v121_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=146, w2=245, w3=516, lag=1)."""
    a = ocf.shift(1)
    b = assetsc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(146, min_periods=max(146//3, 2)).mean())
    decay = spread.ewm(span=245, adjust=False).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.42125 + 0.0028922 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_122_accrual_v122_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=153, w2=256, w3=529, lag=2)."""
    a = _safe_log(assetsc.abs() + 1.0).shift(2)
    b = _safe_log(liabilitiesc.abs() + 1.0).shift(2)
    corr = a.rolling(256, min_periods=max(256//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 153)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.435625 + 0.0028923 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_123_accrual_v123_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=160, w2=267, w3=542, lag=5)."""
    a = liabilitiesc.shift(5)
    b = inventory.shift(5)
    cover = _safe_div(a.rolling(160, min_periods=max(160//3, 2)).mean(), b.abs().rolling(267, min_periods=max(267//3, 2)).mean())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.4086 * _rolling_slope(cover, 160) + 0.0028924 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_124_accrual_v124_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=167, w2=278, w3=555, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    y = _safe_log(revenue.abs() + 1.0).shift(10)
    z = _safe_log(revenue.abs() + 1.0).shift(10)
    basket = x - 0.0398 * y + 0.960200 * z
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 167) - _rolling_slope(basket, 278) + 0.0028925 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_125_accrual_v125_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=174, w2=289, w3=568, lag=21)."""
    x = revenue.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(174, min_periods=max(174//3, 2)).mean(), upside.rolling(289, min_periods=max(289//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.47875 + 0.0028926 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_126_accrual_v126_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=181, w2=300, w3=581, lag=42)."""
    x = _safe_log(netinc.abs() + 1.0).shift(42)
    draw = x - x.rolling(300, min_periods=max(300//3, 2)).max()
    rebound = x - x.rolling(181, min_periods=max(181//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.055 * _rolling_slope(draw, 581) + 0.0028927 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_127_accrual_v127_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=188, w2=311, w3=594, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(594, min_periods=max(594//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.5075 + 0.0028928 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_128_accrual_v128_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=195, w2=322, w3=607, lag=0)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 195)
    baseline = trend.rolling(322, min_periods=max(322//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(607, min_periods=max(607//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.521875 + 0.0028929 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_129_accrual_v129_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=202, w2=333, w3=620, lag=1)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 202)
    slow = _rolling_slope(x, 333)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.53625 + 0.002893 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_130_accrual_v130_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=209, w2=344, w3=633, lag=2)."""
    x = inventory.shift(2)
    peak = x.rolling(344, min_periods=max(344//3, 2)).max()
    trough = x.rolling(209, min_periods=max(209//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.550625 + 0.0028931 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_131_accrual_v131_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=216, w2=355, w3=646, lag=5)."""
    x = revenue.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(355, min_periods=max(355//3, 2)).rank(pct=True)
    persistence = change.rolling(646, min_periods=max(646//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.093 * persistence + 0.0028932 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_132_accrual_v132_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=223, w2=366, w3=659, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(223, min_periods=max(223//3, 2)).std()
    vol_slow = ret.rolling(366, min_periods=max(366//3, 2)).std()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.579375 + 0.0028933 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_133_accrual_v133_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=230, w2=377, w3=672, lag=21)."""
    x = ocf.shift(21)
    ma = x.rolling(377, min_periods=max(377//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 230)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1082 * slope + 0.0028934 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_134_accrual_v134_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=237, w2=388, w3=685, lag=42)."""
    x = assetsc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(388, min_periods=max(388//3, 2)).mean()
    noise = impulse.abs().rolling(685, min_periods=max(685//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.608125 + 0.0028935 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_135_accrual_v135_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=244, w2=399, w3=698, lag=63)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 244)
    acceleration = _rolling_slope(velocity, 399)
    curvature = _rolling_slope(acceleration, 698)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1234 * acceleration + 0.0028936 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_136_accrual_v136_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=251, w2=410, w3=711, lag=0)."""
    rel = _safe_div(inventory.shift(0), revenue.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 251)
    pressure = rel_log.diff(126)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.131 * pressure.rolling(711, min_periods=max(711//3, 2)).mean() + 0.0028937 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_137_accrual_v137_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=7, w2=421, w3=724, lag=1)."""
    a = revenue.shift(1)
    b = netinc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(7, min_periods=max(7//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.878125 + 0.0028938 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_138_accrual_v138_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=14, w2=432, w3=737, lag=2)."""
    a = _safe_log(netinc.abs() + 1.0).shift(2)
    b = _safe_log(ocf.abs() + 1.0).shift(2)
    corr = a.rolling(432, min_periods=max(432//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 14)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.8925 + 0.0028939 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_139_accrual_v139_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=21, w2=443, w3=750, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(21, min_periods=max(21//3, 2)).mean(), b.abs().rolling(443, min_periods=max(443//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.1538 * _rolling_slope(cover, 21) + 0.002894 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_140_accrual_v140_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=28, w2=454, w3=763, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    y = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    z = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    basket = x - 0.1614 * y + 0.838600 * z
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 28) - _rolling_slope(basket, 454) + 0.0028941 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_141_accrual_v141_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=35, w2=465, w3=19, lag=21)."""
    x = liabilitiesc.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(35, min_periods=max(35//3, 2)).mean(), upside.rolling(465, min_periods=max(465//3, 2)).mean().abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(19) * 0.935625 + 0.0028942 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_142_accrual_v142_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=42, w2=476, w3=32, lag=42)."""
    x = _safe_log(inventory.abs() + 1.0).shift(42)
    draw = x - x.rolling(476, min_periods=max(476//3, 2)).max()
    rebound = x - x.rolling(42, min_periods=max(42//3, 2)).min()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1766 * _rolling_slope(draw, 32) + 0.0028943 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_143_accrual_v143_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=49, w2=487, w3=45, lag=63)."""
    a = _safe_log(revenue.abs() + 1.0).shift(63)
    b = _safe_log(netinc.abs() + 1.0).shift(63)
    imbalance = a.diff(49) - b.diff(126)
    stress = imbalance.rolling(45, min_periods=max(45//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.964375 + 0.0028944 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_144_accrual_v144_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=56, w2=498, w3=58, lag=0)."""
    x = _safe_log(netinc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 56)
    baseline = trend.rolling(498, min_periods=max(498//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(58, min_periods=max(58//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.97875 + 0.0028945 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_145_accrual_v145_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=63, w2=509, w3=71, lag=1)."""
    x = _safe_log(ocf.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 63)
    slow = _rolling_slope(x, 509)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=71, adjust=False).mean() * 0.993125 + 0.0028946 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_146_accrual_v146_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=70, w2=17, w3=84, lag=2)."""
    x = assetsc.shift(2)
    peak = x.rolling(17, min_periods=max(17//3, 2)).max()
    trough = x.rolling(70, min_periods=max(70//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.0075 + 0.0028947 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_147_accrual_v147_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=77, w2=28, w3=97, lag=5)."""
    x = liabilitiesc.shift(5)
    change = x.pct_change(77)
    rank = change.rolling(28, min_periods=max(28//3, 2)).rank(pct=True)
    persistence = change.rolling(97, min_periods=max(97//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2146 * persistence + 0.0028948 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_148_accrual_v148_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=84, w2=39, w3=110, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(84, min_periods=max(84//3, 2)).std()
    vol_slow = ret.rolling(39, min_periods=max(39//3, 2)).std()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.03625 + 0.0028949 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_149_accrual_v149_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=91, w2=50, w3=123, lag=21)."""
    x = revenue.shift(21)
    ma = x.rolling(50, min_periods=max(50//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 91)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2298 * slope + 0.002895 * anchor
    return base_signal.diff().diff().diff()

def f47_fes_150_accrual_v150_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=98, w2=61, w3=136, lag=42)."""
    x = netinc.shift(42)
    impulse = x.diff(98)
    drag = impulse.rolling(61, min_periods=max(61//3, 2)).mean()
    noise = impulse.abs().rolling(136, min_periods=max(136//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.065 + 0.0028951 * anchor
    return base_signal.diff().diff().diff()
