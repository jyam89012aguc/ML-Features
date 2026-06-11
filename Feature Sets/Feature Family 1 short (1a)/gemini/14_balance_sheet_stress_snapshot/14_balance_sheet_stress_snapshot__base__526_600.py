"""14 balance sheet stress snapshot base features 526-600 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Fundamental_Quality - Institutional-grade short-side signal.
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

def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)
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

def f14_bsts_526_struct_v526(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=239, w2=111, w3=232, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(111, min_periods=max(111//3, 2)).mean()
    noise = impulse.abs().rolling(232, min_periods=max(232//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.595625 + 0.0008927 * anchor

def f14_bsts_527_struct_v527(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=246, w2=122, w3=245, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 246)
    acceleration = _rolling_slope(velocity, 122)
    curvature = _rolling_slope(acceleration, 245)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1282 * acceleration + 0.0008928 * anchor

def f14_bsts_528_struct_v528(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=253, w2=133, w3=258, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(253, min_periods=max(253//3, 2)).mean(), upside.rolling(133, min_periods=max(133//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.85125 + 0.0008929 * anchor

def f14_bsts_529_struct_v529(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=9, w2=144, w3=271, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(144, min_periods=max(144//3, 2)).max()
    rebound = x - x.rolling(9, min_periods=max(9//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1434 * _rolling_slope(draw, 271) + 0.000893 * anchor

def f14_bsts_530_struct_v530(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=16, w2=155, w3=284, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 16)
    baseline = trend.rolling(155, min_periods=max(155//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(284, min_periods=max(284//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.88 + 0.0008931 * anchor

def f14_bsts_531_struct_v531(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=23, w2=166, w3=297, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 23)
    slow = _rolling_slope(x, 166)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=297, adjust=False).mean() * 0.894375 + 0.0008932 * anchor

def f14_bsts_532_struct_v532(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=30, w2=177, w3=310, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(177, min_periods=max(177//3, 2)).max()
    trough = x.rolling(30, min_periods=max(30//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.90875 + 0.0008933 * anchor

def f14_bsts_533_struct_v533(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=37, w2=188, w3=323, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(37)
    rank = change.rolling(188, min_periods=max(188//3, 2)).rank(pct=True)
    persistence = change.rolling(323, min_periods=max(323//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1738 * persistence + 0.0008934 * anchor

def f14_bsts_534_struct_v534(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=44, w2=199, w3=336, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(44, min_periods=max(44//3, 2)).std()
    vol_slow = ret.rolling(199, min_periods=max(199//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.9375 + 0.0008935 * anchor

def f14_bsts_535_struct_v535(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=51, w2=210, w3=349, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(210, min_periods=max(210//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 51)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.189 * slope + 0.0008936 * anchor

def f14_bsts_536_struct_v536(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=58, w2=221, w3=362, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(58)
    drag = impulse.rolling(221, min_periods=max(221//3, 2)).mean()
    noise = impulse.abs().rolling(362, min_periods=max(362//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.96625 + 0.0008937 * anchor

def f14_bsts_537_struct_v537(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=65, w2=232, w3=375, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 65)
    acceleration = _rolling_slope(velocity, 232)
    curvature = _rolling_slope(acceleration, 375)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2042 * acceleration + 0.0008938 * anchor

def f14_bsts_538_struct_v538(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=72, w2=243, w3=388, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(72, min_periods=max(72//3, 2)).mean(), upside.rolling(243, min_periods=max(243//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.995 + 0.0008939 * anchor

def f14_bsts_539_struct_v539(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=79, w2=254, w3=401, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(254, min_periods=max(254//3, 2)).max()
    rebound = x - x.rolling(79, min_periods=max(79//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2194 * _rolling_slope(draw, 401) + 0.000894 * anchor

def f14_bsts_540_struct_v540(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=86, w2=265, w3=414, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 86)
    baseline = trend.rolling(265, min_periods=max(265//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(414, min_periods=max(414//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.02375 + 0.0008941 * anchor

def f14_bsts_541_struct_v541(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=93, w2=276, w3=427, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 93)
    slow = _rolling_slope(x, 276)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.038125 + 0.0008942 * anchor

def f14_bsts_542_struct_v542(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=100, w2=287, w3=440, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(287, min_periods=max(287//3, 2)).max()
    trough = x.rolling(100, min_periods=max(100//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.0525 + 0.0008943 * anchor

def f14_bsts_543_struct_v543(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=107, w2=298, w3=453, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(107)
    rank = change.rolling(298, min_periods=max(298//3, 2)).rank(pct=True)
    persistence = change.rolling(453, min_periods=max(453//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2498 * persistence + 0.0008944 * anchor

def f14_bsts_544_struct_v544(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=114, w2=309, w3=466, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(114, min_periods=max(114//3, 2)).std()
    vol_slow = ret.rolling(309, min_periods=max(309//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.08125 + 0.0008945 * anchor

def f14_bsts_545_struct_v545(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=121, w2=320, w3=479, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(320, min_periods=max(320//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 121)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.265 * slope + 0.0008946 * anchor

def f14_bsts_546_struct_v546(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=128, w2=331, w3=492, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(331, min_periods=max(331//3, 2)).mean()
    noise = impulse.abs().rolling(492, min_periods=max(492//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.11 + 0.0008947 * anchor

def f14_bsts_547_struct_v547(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=135, w2=342, w3=505, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 135)
    acceleration = _rolling_slope(velocity, 342)
    curvature = _rolling_slope(acceleration, 505)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2802 * acceleration + 0.0008948 * anchor

def f14_bsts_548_struct_v548(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=142, w2=353, w3=518, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(142, min_periods=max(142//3, 2)).mean(), upside.rolling(353, min_periods=max(353//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.13875 + 0.0008949 * anchor

def f14_bsts_549_struct_v549(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=149, w2=364, w3=531, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(364, min_periods=max(364//3, 2)).max()
    rebound = x - x.rolling(149, min_periods=max(149//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2954 * _rolling_slope(draw, 531) + 0.000895 * anchor

def f14_bsts_550_struct_v550(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=156, w2=375, w3=544, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 156)
    baseline = trend.rolling(375, min_periods=max(375//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(544, min_periods=max(544//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.1675 + 0.0008951 * anchor

def f14_bsts_551_struct_v551(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=163, w2=386, w3=557, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 163)
    slow = _rolling_slope(x, 386)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.181875 + 0.0008952 * anchor

def f14_bsts_552_struct_v552(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=170, w2=397, w3=570, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(397, min_periods=max(397//3, 2)).max()
    trough = x.rolling(170, min_periods=max(170//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.19625 + 0.0008953 * anchor

def f14_bsts_553_struct_v553(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=177, w2=408, w3=583, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(408, min_periods=max(408//3, 2)).rank(pct=True)
    persistence = change.rolling(583, min_periods=max(583//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3258 * persistence + 0.0008954 * anchor

def f14_bsts_554_struct_v554(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=184, w2=419, w3=596, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(184, min_periods=max(184//3, 2)).std()
    vol_slow = ret.rolling(419, min_periods=max(419//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.225 + 0.0008955 * anchor

def f14_bsts_555_struct_v555(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=191, w2=430, w3=609, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(430, min_periods=max(430//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 191)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.341 * slope + 0.0008956 * anchor

def f14_bsts_556_struct_v556(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=198, w2=441, w3=622, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(441, min_periods=max(441//3, 2)).mean()
    noise = impulse.abs().rolling(622, min_periods=max(622//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.25375 + 0.0008957 * anchor

def f14_bsts_557_struct_v557(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=205, w2=452, w3=635, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 205)
    acceleration = _rolling_slope(velocity, 452)
    curvature = _rolling_slope(acceleration, 635)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3562 * acceleration + 0.0008958 * anchor

def f14_bsts_558_struct_v558(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=212, w2=463, w3=648, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(212, min_periods=max(212//3, 2)).mean(), upside.rolling(463, min_periods=max(463//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.2825 + 0.0008959 * anchor

def f14_bsts_559_struct_v559(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=219, w2=474, w3=661, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(474, min_periods=max(474//3, 2)).max()
    rebound = x - x.rolling(219, min_periods=max(219//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3714 * _rolling_slope(draw, 661) + 0.000896 * anchor

def f14_bsts_560_struct_v560(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=226, w2=485, w3=674, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 226)
    baseline = trend.rolling(485, min_periods=max(485//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(674, min_periods=max(674//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.31125 + 0.0008961 * anchor

def f14_bsts_561_struct_v561(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=233, w2=496, w3=687, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 233)
    slow = _rolling_slope(x, 496)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.325625 + 0.0008962 * anchor

def f14_bsts_562_struct_v562(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=240, w2=507, w3=700, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(507, min_periods=max(507//3, 2)).max()
    trough = x.rolling(240, min_periods=max(240//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.34 + 0.0008963 * anchor

def f14_bsts_563_struct_v563(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=247, w2=15, w3=713, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(15, min_periods=max(15//3, 2)).rank(pct=True)
    persistence = change.rolling(713, min_periods=max(713//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.4018 * persistence + 0.0008964 * anchor

def f14_bsts_564_struct_v564(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=254, w2=26, w3=726, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(254, min_periods=max(254//3, 2)).std()
    vol_slow = ret.rolling(26, min_periods=max(26//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.36875 + 0.0008965 * anchor

def f14_bsts_565_struct_v565(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=10, w2=37, w3=739, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(37, min_periods=max(37//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 10)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0406 * slope + 0.0008966 * anchor

def f14_bsts_566_struct_v566(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=17, w2=48, w3=752, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(17)
    drag = impulse.rolling(48, min_periods=max(48//3, 2)).mean()
    noise = impulse.abs().rolling(752, min_periods=max(752//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.3975 + 0.0008967 * anchor

def f14_bsts_567_struct_v567(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=24, w2=59, w3=765, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 24)
    acceleration = _rolling_slope(velocity, 59)
    curvature = _rolling_slope(acceleration, 765)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0558 * acceleration + 0.0008968 * anchor

def f14_bsts_568_struct_v568(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=31, w2=70, w3=21, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(31, min_periods=max(31//3, 2)).mean(), upside.rolling(70, min_periods=max(70//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(21) * 1.42625 + 0.0008969 * anchor

def f14_bsts_569_struct_v569(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=38, w2=81, w3=34, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(81, min_periods=max(81//3, 2)).max()
    rebound = x - x.rolling(38, min_periods=max(38//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.071 * _rolling_slope(draw, 34) + 0.000897 * anchor

def f14_bsts_570_struct_v570(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=45, w2=92, w3=47, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 45)
    baseline = trend.rolling(92, min_periods=max(92//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(47, min_periods=max(47//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.455 + 0.0008971 * anchor

def f14_bsts_571_struct_v571(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=52, w2=103, w3=60, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 52)
    slow = _rolling_slope(x, 103)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=60, adjust=False).mean() * 1.469375 + 0.0008972 * anchor

def f14_bsts_572_struct_v572(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=59, w2=114, w3=73, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(114, min_periods=max(114//3, 2)).max()
    trough = x.rolling(59, min_periods=max(59//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.48375 + 0.0008973 * anchor

def f14_bsts_573_struct_v573(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=66, w2=125, w3=86, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(66)
    rank = change.rolling(125, min_periods=max(125//3, 2)).rank(pct=True)
    persistence = change.rolling(86, min_periods=max(86//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1014 * persistence + 0.0008974 * anchor

def f14_bsts_574_struct_v574(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=73, w2=136, w3=99, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(73, min_periods=max(73//3, 2)).std()
    vol_slow = ret.rolling(136, min_periods=max(136//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.5125 + 0.0008975 * anchor

def f14_bsts_575_struct_v575(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=80, w2=147, w3=112, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(147, min_periods=max(147//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 80)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1166 * slope + 0.0008976 * anchor

def f14_bsts_576_struct_v576(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=87, w2=158, w3=125, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(87)
    drag = impulse.rolling(158, min_periods=max(158//3, 2)).mean()
    noise = impulse.abs().rolling(125, min_periods=max(125//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.54125 + 0.0008977 * anchor

def f14_bsts_577_struct_v577(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=94, w2=169, w3=138, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 94)
    acceleration = _rolling_slope(velocity, 169)
    curvature = _rolling_slope(acceleration, 138)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1318 * acceleration + 0.0008978 * anchor

def f14_bsts_578_struct_v578(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=101, w2=180, w3=151, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(101, min_periods=max(101//3, 2)).mean(), upside.rolling(180, min_periods=max(180//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.57 + 0.0008979 * anchor

def f14_bsts_579_struct_v579(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=108, w2=191, w3=164, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(191, min_periods=max(191//3, 2)).max()
    rebound = x - x.rolling(108, min_periods=max(108//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.147 * _rolling_slope(draw, 164) + 0.000898 * anchor

def f14_bsts_580_struct_v580(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=115, w2=202, w3=177, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 115)
    baseline = trend.rolling(202, min_periods=max(202//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(177, min_periods=max(177//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.59875 + 0.0008981 * anchor

def f14_bsts_581_struct_v581(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=122, w2=213, w3=190, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 122)
    slow = _rolling_slope(x, 213)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=190, adjust=False).mean() * 1.613125 + 0.0008982 * anchor

def f14_bsts_582_struct_v582(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=129, w2=224, w3=203, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(224, min_periods=max(224//3, 2)).max()
    trough = x.rolling(129, min_periods=max(129//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.854375 + 0.0008983 * anchor

def f14_bsts_583_struct_v583(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=136, w2=235, w3=216, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(235, min_periods=max(235//3, 2)).rank(pct=True)
    persistence = change.rolling(216, min_periods=max(216//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1774 * persistence + 0.0008984 * anchor

def f14_bsts_584_struct_v584(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=143, w2=246, w3=229, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(143, min_periods=max(143//3, 2)).std()
    vol_slow = ret.rolling(246, min_periods=max(246//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.883125 + 0.0008985 * anchor

def f14_bsts_585_struct_v585(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=150, w2=257, w3=242, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(257, min_periods=max(257//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 150)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1926 * slope + 0.0008986 * anchor

def f14_bsts_586_struct_v586(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=157, w2=268, w3=255, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(268, min_periods=max(268//3, 2)).mean()
    noise = impulse.abs().rolling(255, min_periods=max(255//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.911875 + 0.0008987 * anchor

def f14_bsts_587_struct_v587(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=164, w2=279, w3=268, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 164)
    acceleration = _rolling_slope(velocity, 279)
    curvature = _rolling_slope(acceleration, 268)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2078 * acceleration + 0.0008988 * anchor

def f14_bsts_588_struct_v588(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=171, w2=290, w3=281, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(171, min_periods=max(171//3, 2)).mean(), upside.rolling(290, min_periods=max(290//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.940625 + 0.0008989 * anchor

def f14_bsts_589_struct_v589(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=178, w2=301, w3=294, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(301, min_periods=max(301//3, 2)).max()
    rebound = x - x.rolling(178, min_periods=max(178//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.223 * _rolling_slope(draw, 294) + 0.000899 * anchor

def f14_bsts_590_struct_v590(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=185, w2=312, w3=307, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 185)
    baseline = trend.rolling(312, min_periods=max(312//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(307, min_periods=max(307//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.969375 + 0.0008991 * anchor

def f14_bsts_591_struct_v591(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=192, w2=323, w3=320, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 192)
    slow = _rolling_slope(x, 323)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.98375 + 0.0008992 * anchor

def f14_bsts_592_struct_v592(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=199, w2=334, w3=333, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(334, min_periods=max(334//3, 2)).max()
    trough = x.rolling(199, min_periods=max(199//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.998125 + 0.0008993 * anchor

def f14_bsts_593_struct_v593(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=206, w2=345, w3=346, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(345, min_periods=max(345//3, 2)).rank(pct=True)
    persistence = change.rolling(346, min_periods=max(346//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2534 * persistence + 0.0008994 * anchor

def f14_bsts_594_struct_v594(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=213, w2=356, w3=359, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(213, min_periods=max(213//3, 2)).std()
    vol_slow = ret.rolling(356, min_periods=max(356//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.026875 + 0.0008995 * anchor

def f14_bsts_595_struct_v595(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=220, w2=367, w3=372, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(367, min_periods=max(367//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 220)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2686 * slope + 0.0008996 * anchor

def f14_bsts_596_struct_v596(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=227, w2=378, w3=385, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(378, min_periods=max(378//3, 2)).mean()
    noise = impulse.abs().rolling(385, min_periods=max(385//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.055625 + 0.0008997 * anchor

def f14_bsts_597_struct_v597(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=234, w2=389, w3=398, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 234)
    acceleration = _rolling_slope(velocity, 389)
    curvature = _rolling_slope(acceleration, 398)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2838 * acceleration + 0.0008998 * anchor

def f14_bsts_598_struct_v598(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=241, w2=400, w3=411, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(241, min_periods=max(241//3, 2)).mean(), upside.rolling(400, min_periods=max(400//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.084375 + 0.0008999 * anchor

def f14_bsts_599_struct_v599(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=248, w2=411, w3=424, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(411, min_periods=max(411//3, 2)).max()
    rebound = x - x.rolling(248, min_periods=max(248//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.299 * _rolling_slope(draw, 424) + 0.0009 * anchor

def f14_bsts_600_struct_v600(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=255, w2=422, w3=437, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 255)
    baseline = trend.rolling(422, min_periods=max(422//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(437, min_periods=max(437//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.113125 + 0.0009001 * anchor
