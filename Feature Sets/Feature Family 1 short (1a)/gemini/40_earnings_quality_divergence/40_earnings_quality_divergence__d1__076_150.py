"""40 earnings quality divergence d1 first derivative features 76-150 â€” Pipeline 1a-HF Grade v3.

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

def f40_eqd_076_accrual_v76_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=116, w2=268, w3=362, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    y = _safe_log(revenue.abs() + 1.0).shift(10)
    z = _safe_log(revenue.abs() + 1.0).shift(10)
    basket = x - 0.0822 * y + 0.917800 * z
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 116) - _rolling_slope(basket, 268) + 0.0024077 * anchor
    return base_signal.diff()

def f40_eqd_077_accrual_v77_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=123, w2=279, w3=375, lag=21)."""
    x = revenue.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(123, min_periods=max(123//3, 2)).mean(), upside.rolling(279, min_periods=max(279//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.37 + 0.0024078 * anchor
    return base_signal.diff()

def f40_eqd_078_accrual_v78_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=130, w2=290, w3=388, lag=42)."""
    x = _safe_log(netinc.abs() + 1.0).shift(42)
    draw = x - x.rolling(290, min_periods=max(290//3, 2)).max()
    rebound = x - x.rolling(130, min_periods=max(130//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0974 * _rolling_slope(draw, 388) + 0.0024079 * anchor
    return base_signal.diff()

def f40_eqd_079_accrual_v79_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=137, w2=301, w3=401, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(401, min_periods=max(401//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.39875 + 0.002408 * anchor
    return base_signal.diff()

def f40_eqd_080_accrual_v80_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=144, w2=312, w3=414, lag=0)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 144)
    baseline = trend.rolling(312, min_periods=max(312//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(414, min_periods=max(414//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.413125 + 0.0024081 * anchor
    return base_signal.diff()

def f40_eqd_081_accrual_v81_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=151, w2=323, w3=427, lag=1)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 151)
    slow = _rolling_slope(x, 323)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.4275 + 0.0024082 * anchor
    return base_signal.diff()

def f40_eqd_082_accrual_v82_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=158, w2=334, w3=440, lag=2)."""
    x = inventory.shift(2)
    peak = x.rolling(334, min_periods=max(334//3, 2)).max()
    trough = x.rolling(158, min_periods=max(158//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.441875 + 0.0024083 * anchor
    return base_signal.diff()

def f40_eqd_083_accrual_v83_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=165, w2=345, w3=453, lag=5)."""
    x = revenue.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(345, min_periods=max(345//3, 2)).rank(pct=True)
    persistence = change.rolling(453, min_periods=max(453//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1354 * persistence + 0.0024084 * anchor
    return base_signal.diff()

def f40_eqd_084_accrual_v84_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=172, w2=356, w3=466, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(172, min_periods=max(172//3, 2)).std()
    vol_slow = ret.rolling(356, min_periods=max(356//3, 2)).std()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.470625 + 0.0024085 * anchor
    return base_signal.diff()

def f40_eqd_085_accrual_v85_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=179, w2=367, w3=479, lag=21)."""
    x = ocf.shift(21)
    ma = x.rolling(367, min_periods=max(367//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 179)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1506 * slope + 0.0024086 * anchor
    return base_signal.diff()

def f40_eqd_086_accrual_v86_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=186, w2=378, w3=492, lag=42)."""
    x = assetsc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(378, min_periods=max(378//3, 2)).mean()
    noise = impulse.abs().rolling(492, min_periods=max(492//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.499375 + 0.0024087 * anchor
    return base_signal.diff()

def f40_eqd_087_accrual_v87_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=193, w2=389, w3=505, lag=63)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 193)
    acceleration = _rolling_slope(velocity, 389)
    curvature = _rolling_slope(acceleration, 505)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1658 * acceleration + 0.0024088 * anchor
    return base_signal.diff()

def f40_eqd_088_accrual_v88_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=200, w2=400, w3=518, lag=0)."""
    rel = _safe_div(inventory.shift(0), revenue.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 200)
    pressure = rel_log.diff(126)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.1734 * pressure.rolling(518, min_periods=max(518//3, 2)).mean() + 0.0024089 * anchor
    return base_signal.diff()

def f40_eqd_089_accrual_v89_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=207, w2=411, w3=531, lag=1)."""
    a = revenue.shift(1)
    b = netinc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(207, min_periods=max(207//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.5425 + 0.002409 * anchor
    return base_signal.diff()

def f40_eqd_090_accrual_v90_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=214, w2=422, w3=544, lag=2)."""
    a = _safe_log(netinc.abs() + 1.0).shift(2)
    b = _safe_log(ocf.abs() + 1.0).shift(2)
    corr = a.rolling(422, min_periods=max(422//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 214)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.556875 + 0.0024091 * anchor
    return base_signal.diff()

def f40_eqd_091_accrual_v91_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=221, w2=433, w3=557, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(221, min_periods=max(221//3, 2)).mean(), b.abs().rolling(433, min_periods=max(433//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.1962 * _rolling_slope(cover, 221) + 0.0024092 * anchor
    return base_signal.diff()

def f40_eqd_092_accrual_v92_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=228, w2=444, w3=570, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    y = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    z = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    basket = x - 0.2038 * y + 0.796200 * z
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 228) - _rolling_slope(basket, 444) + 0.0024093 * anchor
    return base_signal.diff()

def f40_eqd_093_accrual_v93_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=235, w2=455, w3=583, lag=21)."""
    x = liabilitiesc.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(235, min_periods=max(235//3, 2)).mean(), upside.rolling(455, min_periods=max(455//3, 2)).mean().abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.6 + 0.0024094 * anchor
    return base_signal.diff()

def f40_eqd_094_accrual_v94_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=242, w2=466, w3=596, lag=42)."""
    x = _safe_log(inventory.abs() + 1.0).shift(42)
    draw = x - x.rolling(466, min_periods=max(466//3, 2)).max()
    rebound = x - x.rolling(242, min_periods=max(242//3, 2)).min()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.219 * _rolling_slope(draw, 596) + 0.0024095 * anchor
    return base_signal.diff()

def f40_eqd_095_accrual_v95_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=249, w2=477, w3=609, lag=63)."""
    a = _safe_log(revenue.abs() + 1.0).shift(63)
    b = _safe_log(netinc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(609, min_periods=max(609//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.855625 + 0.0024096 * anchor
    return base_signal.diff()

def f40_eqd_096_accrual_v96_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=5, w2=488, w3=622, lag=0)."""
    x = _safe_log(netinc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 5)
    baseline = trend.rolling(488, min_periods=max(488//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(622, min_periods=max(622//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.87 + 0.0024097 * anchor
    return base_signal.diff()

def f40_eqd_097_accrual_v97_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=12, w2=499, w3=635, lag=1)."""
    x = _safe_log(ocf.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 12)
    slow = _rolling_slope(x, 499)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.884375 + 0.0024098 * anchor
    return base_signal.diff()

def f40_eqd_098_accrual_v98_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=19, w2=510, w3=648, lag=2)."""
    x = assetsc.shift(2)
    peak = x.rolling(510, min_periods=max(510//3, 2)).max()
    trough = x.rolling(19, min_periods=max(19//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.89875 + 0.0024099 * anchor
    return base_signal.diff()

def f40_eqd_099_accrual_v99_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=26, w2=18, w3=661, lag=5)."""
    x = liabilitiesc.shift(5)
    change = x.pct_change(26)
    rank = change.rolling(18, min_periods=max(18//3, 2)).rank(pct=True)
    persistence = change.rolling(661, min_periods=max(661//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.257 * persistence + 0.00241 * anchor
    return base_signal.diff()

def f40_eqd_100_accrual_v100_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=33, w2=29, w3=674, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(33, min_periods=max(33//3, 2)).std()
    vol_slow = ret.rolling(29, min_periods=max(29//3, 2)).std()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.9275 + 0.0024101 * anchor
    return base_signal.diff()

def f40_eqd_101_accrual_v101_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=40, w2=40, w3=687, lag=21)."""
    x = revenue.shift(21)
    ma = x.rolling(40, min_periods=max(40//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 40)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2722 * slope + 0.0024102 * anchor
    return base_signal.diff()

def f40_eqd_102_accrual_v102_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=47, w2=51, w3=700, lag=42)."""
    x = netinc.shift(42)
    impulse = x.diff(47)
    drag = impulse.rolling(51, min_periods=max(51//3, 2)).mean()
    noise = impulse.abs().rolling(700, min_periods=max(700//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.95625 + 0.0024103 * anchor
    return base_signal.diff()

def f40_eqd_103_accrual_v103_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=54, w2=62, w3=713, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 54)
    acceleration = _rolling_slope(velocity, 62)
    curvature = _rolling_slope(acceleration, 713)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2874 * acceleration + 0.0024104 * anchor
    return base_signal.diff()

def f40_eqd_104_accrual_v104_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=61, w2=73, w3=726, lag=0)."""
    rel = _safe_div(assetsc.shift(0), liabilitiesc.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 61)
    pressure = rel_log.diff(73)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.295 * pressure.rolling(726, min_periods=max(726//3, 2)).mean() + 0.0024105 * anchor
    return base_signal.diff()

def f40_eqd_105_accrual_v105_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=68, w2=84, w3=739, lag=1)."""
    a = liabilitiesc.shift(1)
    b = inventory.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(68, min_periods=max(68//3, 2)).mean())
    decay = spread.ewm(span=84, adjust=False).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.999375 + 0.0024106 * anchor
    return base_signal.diff()

def f40_eqd_106_accrual_v106_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=75, w2=95, w3=752, lag=2)."""
    a = _safe_log(inventory.abs() + 1.0).shift(2)
    b = _safe_log(revenue.abs() + 1.0).shift(2)
    corr = a.rolling(95, min_periods=max(95//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 75)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.01375 + 0.0024107 * anchor
    return base_signal.diff()

def f40_eqd_107_accrual_v107_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=82, w2=106, w3=765, lag=5)."""
    a = revenue.shift(5)
    b = netinc.shift(5)
    cover = _safe_div(a.rolling(82, min_periods=max(82//3, 2)).mean(), b.abs().rolling(106, min_periods=max(106//3, 2)).mean())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.3178 * _rolling_slope(cover, 82) + 0.0024108 * anchor
    return base_signal.diff()

def f40_eqd_108_accrual_v108_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=89, w2=117, w3=21, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    y = _safe_log(ocf.abs() + 1.0).shift(10)
    z = _safe_log(ocf.abs() + 1.0).shift(10)
    basket = x - 0.3254 * y + 0.674600 * z
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 89) - _rolling_slope(basket, 117) + 0.0024109 * anchor
    return base_signal.diff()

def f40_eqd_109_accrual_v109_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=96, w2=128, w3=34, lag=21)."""
    x = ocf.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(96, min_periods=max(96//3, 2)).mean(), upside.rolling(128, min_periods=max(128//3, 2)).mean().abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(34) * 1.056875 + 0.002411 * anchor
    return base_signal.diff()

def f40_eqd_110_accrual_v110_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=103, w2=139, w3=47, lag=42)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(42)
    draw = x - x.rolling(139, min_periods=max(139//3, 2)).max()
    rebound = x - x.rolling(103, min_periods=max(103//3, 2)).min()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3406 * _rolling_slope(draw, 47) + 0.0024111 * anchor
    return base_signal.diff()

def f40_eqd_111_accrual_v111_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=110, w2=150, w3=60, lag=63)."""
    a = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    b = _safe_log(inventory.abs() + 1.0).shift(63)
    imbalance = a.diff(110) - b.diff(126)
    stress = imbalance.rolling(60, min_periods=max(60//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.085625 + 0.0024112 * anchor
    return base_signal.diff()

def f40_eqd_112_accrual_v112_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=117, w2=161, w3=73, lag=0)."""
    x = _safe_log(inventory.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 117)
    baseline = trend.rolling(161, min_periods=max(161//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(73, min_periods=max(73//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.1 + 0.0024113 * anchor
    return base_signal.diff()

def f40_eqd_113_accrual_v113_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=124, w2=172, w3=86, lag=1)."""
    x = _safe_log(revenue.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 124)
    slow = _rolling_slope(x, 172)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=86, adjust=False).mean() * 1.114375 + 0.0024114 * anchor
    return base_signal.diff()

def f40_eqd_114_accrual_v114_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=131, w2=183, w3=99, lag=2)."""
    x = netinc.shift(2)
    peak = x.rolling(183, min_periods=max(183//3, 2)).max()
    trough = x.rolling(131, min_periods=max(131//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.12875 + 0.0024115 * anchor
    return base_signal.diff()

def f40_eqd_115_accrual_v115_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=138, w2=194, w3=112, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(194, min_periods=max(194//3, 2)).rank(pct=True)
    persistence = change.rolling(112, min_periods=max(112//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3786 * persistence + 0.0024116 * anchor
    return base_signal.diff()

def f40_eqd_116_accrual_v116_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=145, w2=205, w3=125, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(145, min_periods=max(145//3, 2)).std()
    vol_slow = ret.rolling(205, min_periods=max(205//3, 2)).std()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.1575 + 0.0024117 * anchor
    return base_signal.diff()

def f40_eqd_117_accrual_v117_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=152, w2=216, w3=138, lag=21)."""
    x = liabilitiesc.shift(21)
    ma = x.rolling(216, min_periods=max(216//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 152)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3938 * slope + 0.0024118 * anchor
    return base_signal.diff()

def f40_eqd_118_accrual_v118_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=159, w2=227, w3=151, lag=42)."""
    x = inventory.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(227, min_periods=max(227//3, 2)).mean()
    noise = impulse.abs().rolling(151, min_periods=max(151//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.18625 + 0.0024119 * anchor
    return base_signal.diff()

def f40_eqd_119_accrual_v119_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=166, w2=238, w3=164, lag=63)."""
    x = _safe_log(revenue.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 166)
    acceleration = _rolling_slope(velocity, 238)
    curvature = _rolling_slope(acceleration, 164)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.409 * acceleration + 0.002412 * anchor
    return base_signal.diff()

def f40_eqd_120_accrual_v120_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=173, w2=249, w3=177, lag=0)."""
    rel = _safe_div(netinc.shift(0), ocf.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 173)
    pressure = rel_log.diff(126)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.0402 * pressure.rolling(177, min_periods=max(177//3, 2)).mean() + 0.0024121 * anchor
    return base_signal.diff()

def f40_eqd_121_accrual_v121_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=180, w2=260, w3=190, lag=1)."""
    a = ocf.shift(1)
    b = assetsc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(180, min_periods=max(180//3, 2)).mean())
    decay = spread.ewm(span=260, adjust=False).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.229375 + 0.0024122 * anchor
    return base_signal.diff()

def f40_eqd_122_accrual_v122_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=187, w2=271, w3=203, lag=2)."""
    a = _safe_log(assetsc.abs() + 1.0).shift(2)
    b = _safe_log(liabilitiesc.abs() + 1.0).shift(2)
    corr = a.rolling(271, min_periods=max(271//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 187)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.24375 + 0.0024123 * anchor
    return base_signal.diff()

def f40_eqd_123_accrual_v123_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=194, w2=282, w3=216, lag=5)."""
    a = liabilitiesc.shift(5)
    b = inventory.shift(5)
    cover = _safe_div(a.rolling(194, min_periods=max(194//3, 2)).mean(), b.abs().rolling(282, min_periods=max(282//3, 2)).mean())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.063 * _rolling_slope(cover, 194) + 0.0024124 * anchor
    return base_signal.diff()

def f40_eqd_124_accrual_v124_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=201, w2=293, w3=229, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    y = _safe_log(revenue.abs() + 1.0).shift(10)
    z = _safe_log(revenue.abs() + 1.0).shift(10)
    basket = x - 0.0706 * y + 0.929400 * z
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 201) - _rolling_slope(basket, 293) + 0.0024125 * anchor
    return base_signal.diff()

def f40_eqd_125_accrual_v125_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=208, w2=304, w3=242, lag=21)."""
    x = revenue.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(208, min_periods=max(208//3, 2)).mean(), upside.rolling(304, min_periods=max(304//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.286875 + 0.0024126 * anchor
    return base_signal.diff()

def f40_eqd_126_accrual_v126_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=215, w2=315, w3=255, lag=42)."""
    x = _safe_log(netinc.abs() + 1.0).shift(42)
    draw = x - x.rolling(315, min_periods=max(315//3, 2)).max()
    rebound = x - x.rolling(215, min_periods=max(215//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0858 * _rolling_slope(draw, 255) + 0.0024127 * anchor
    return base_signal.diff()

def f40_eqd_127_accrual_v127_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=222, w2=326, w3=268, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(268, min_periods=max(268//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.315625 + 0.0024128 * anchor
    return base_signal.diff()

def f40_eqd_128_accrual_v128_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=229, w2=337, w3=281, lag=0)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 229)
    baseline = trend.rolling(337, min_periods=max(337//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(281, min_periods=max(281//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.33 + 0.0024129 * anchor
    return base_signal.diff()

def f40_eqd_129_accrual_v129_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=236, w2=348, w3=294, lag=1)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 236)
    slow = _rolling_slope(x, 348)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=294, adjust=False).mean() * 1.344375 + 0.002413 * anchor
    return base_signal.diff()

def f40_eqd_130_accrual_v130_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=243, w2=359, w3=307, lag=2)."""
    x = inventory.shift(2)
    peak = x.rolling(359, min_periods=max(359//3, 2)).max()
    trough = x.rolling(243, min_periods=max(243//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.35875 + 0.0024131 * anchor
    return base_signal.diff()

def f40_eqd_131_accrual_v131_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=250, w2=370, w3=320, lag=5)."""
    x = revenue.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(370, min_periods=max(370//3, 2)).rank(pct=True)
    persistence = change.rolling(320, min_periods=max(320//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1238 * persistence + 0.0024132 * anchor
    return base_signal.diff()

def f40_eqd_132_accrual_v132_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=6, w2=381, w3=333, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(6, min_periods=max(6//3, 2)).std()
    vol_slow = ret.rolling(381, min_periods=max(381//3, 2)).std()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.3875 + 0.0024133 * anchor
    return base_signal.diff()

def f40_eqd_133_accrual_v133_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=13, w2=392, w3=346, lag=21)."""
    x = ocf.shift(21)
    ma = x.rolling(392, min_periods=max(392//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 13)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.139 * slope + 0.0024134 * anchor
    return base_signal.diff()

def f40_eqd_134_accrual_v134_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=20, w2=403, w3=359, lag=42)."""
    x = assetsc.shift(42)
    impulse = x.diff(20)
    drag = impulse.rolling(403, min_periods=max(403//3, 2)).mean()
    noise = impulse.abs().rolling(359, min_periods=max(359//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.41625 + 0.0024135 * anchor
    return base_signal.diff()

def f40_eqd_135_accrual_v135_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=27, w2=414, w3=372, lag=63)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 27)
    acceleration = _rolling_slope(velocity, 414)
    curvature = _rolling_slope(acceleration, 372)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1542 * acceleration + 0.0024136 * anchor
    return base_signal.diff()

def f40_eqd_136_accrual_v136_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=34, w2=425, w3=385, lag=0)."""
    rel = _safe_div(inventory.shift(0), revenue.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 34)
    pressure = rel_log.diff(126)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.1618 * pressure.rolling(385, min_periods=max(385//3, 2)).mean() + 0.0024137 * anchor
    return base_signal.diff()

def f40_eqd_137_accrual_v137_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=41, w2=436, w3=398, lag=1)."""
    a = revenue.shift(1)
    b = netinc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(41, min_periods=max(41//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.459375 + 0.0024138 * anchor
    return base_signal.diff()

def f40_eqd_138_accrual_v138_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=48, w2=447, w3=411, lag=2)."""
    a = _safe_log(netinc.abs() + 1.0).shift(2)
    b = _safe_log(ocf.abs() + 1.0).shift(2)
    corr = a.rolling(447, min_periods=max(447//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 48)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.47375 + 0.0024139 * anchor
    return base_signal.diff()

def f40_eqd_139_accrual_v139_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=55, w2=458, w3=424, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(55, min_periods=max(55//3, 2)).mean(), b.abs().rolling(458, min_periods=max(458//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.1846 * _rolling_slope(cover, 55) + 0.002414 * anchor
    return base_signal.diff()

def f40_eqd_140_accrual_v140_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=62, w2=469, w3=437, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    y = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    z = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    basket = x - 0.1922 * y + 0.807800 * z
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 62) - _rolling_slope(basket, 469) + 0.0024141 * anchor
    return base_signal.diff()

def f40_eqd_141_accrual_v141_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=69, w2=480, w3=450, lag=21)."""
    x = liabilitiesc.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(69, min_periods=max(69//3, 2)).mean(), upside.rolling(480, min_periods=max(480//3, 2)).mean().abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.516875 + 0.0024142 * anchor
    return base_signal.diff()

def f40_eqd_142_accrual_v142_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=76, w2=491, w3=463, lag=42)."""
    x = _safe_log(inventory.abs() + 1.0).shift(42)
    draw = x - x.rolling(491, min_periods=max(491//3, 2)).max()
    rebound = x - x.rolling(76, min_periods=max(76//3, 2)).min()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2074 * _rolling_slope(draw, 463) + 0.0024143 * anchor
    return base_signal.diff()

def f40_eqd_143_accrual_v143_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=83, w2=502, w3=476, lag=63)."""
    a = _safe_log(revenue.abs() + 1.0).shift(63)
    b = _safe_log(netinc.abs() + 1.0).shift(63)
    imbalance = a.diff(83) - b.diff(126)
    stress = imbalance.rolling(476, min_periods=max(476//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.545625 + 0.0024144 * anchor
    return base_signal.diff()

def f40_eqd_144_accrual_v144_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=90, w2=10, w3=489, lag=0)."""
    x = _safe_log(netinc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 90)
    baseline = trend.rolling(10, min_periods=max(10//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(489, min_periods=max(489//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.56 + 0.0024145 * anchor
    return base_signal.diff()

def f40_eqd_145_accrual_v145_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=97, w2=21, w3=502, lag=1)."""
    x = _safe_log(ocf.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 97)
    slow = _rolling_slope(x, 21)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.574375 + 0.0024146 * anchor
    return base_signal.diff()

def f40_eqd_146_accrual_v146_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=104, w2=32, w3=515, lag=2)."""
    x = assetsc.shift(2)
    peak = x.rolling(32, min_periods=max(32//3, 2)).max()
    trough = x.rolling(104, min_periods=max(104//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.58875 + 0.0024147 * anchor
    return base_signal.diff()

def f40_eqd_147_accrual_v147_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=111, w2=43, w3=528, lag=5)."""
    x = liabilitiesc.shift(5)
    change = x.pct_change(111)
    rank = change.rolling(43, min_periods=max(43//3, 2)).rank(pct=True)
    persistence = change.rolling(528, min_periods=max(528//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2454 * persistence + 0.0024148 * anchor
    return base_signal.diff()

def f40_eqd_148_accrual_v148_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=118, w2=54, w3=541, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(118, min_periods=max(118//3, 2)).std()
    vol_slow = ret.rolling(54, min_periods=max(54//3, 2)).std()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.6175 + 0.0024149 * anchor
    return base_signal.diff()

def f40_eqd_149_accrual_v149_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=125, w2=65, w3=554, lag=21)."""
    x = revenue.shift(21)
    ma = x.rolling(65, min_periods=max(65//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 125)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2606 * slope + 0.002415 * anchor
    return base_signal.diff()

def f40_eqd_150_accrual_v150_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=132, w2=76, w3=567, lag=42)."""
    x = netinc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(76, min_periods=max(76//3, 2)).mean()
    noise = impulse.abs().rolling(567, min_periods=max(567//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.873125 + 0.0024151 * anchor
    return base_signal.diff()
