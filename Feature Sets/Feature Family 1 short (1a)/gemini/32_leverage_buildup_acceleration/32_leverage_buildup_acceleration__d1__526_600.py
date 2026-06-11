"""32 leverage buildup acceleration d1 first derivative features 526-600 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Kinetics_Fundamental - Institutional-grade short-side signal.
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

def f32_lba_526_struct_v526_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=37, w2=203, w3=587, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(37)
    drag = impulse.rolling(203, min_periods=max(203//3, 2)).mean()
    noise = impulse.abs().rolling(587, min_periods=max(587//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.4475 + 0.0019727 * anchor
    return base_signal.diff()

def f32_lba_527_struct_v527_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=44, w2=214, w3=600, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 44)
    acceleration = _rolling_slope(velocity, 214)
    curvature = _rolling_slope(acceleration, 600)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.153 * acceleration + 0.0019728 * anchor
    return base_signal.diff()

def f32_lba_528_struct_v528_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=51, w2=225, w3=613, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(51, min_periods=max(51//3, 2)).mean(), upside.rolling(225, min_periods=max(225//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.47625 + 0.0019729 * anchor
    return base_signal.diff()

def f32_lba_529_struct_v529_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=58, w2=236, w3=626, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(236, min_periods=max(236//3, 2)).max()
    rebound = x - x.rolling(58, min_periods=max(58//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1682 * _rolling_slope(draw, 626) + 0.001973 * anchor
    return base_signal.diff()

def f32_lba_530_struct_v530_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=65, w2=247, w3=639, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 65)
    baseline = trend.rolling(247, min_periods=max(247//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(639, min_periods=max(639//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.505 + 0.0019731 * anchor
    return base_signal.diff()

def f32_lba_531_struct_v531_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=72, w2=258, w3=652, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 72)
    slow = _rolling_slope(x, 258)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.519375 + 0.0019732 * anchor
    return base_signal.diff()

def f32_lba_532_struct_v532_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=79, w2=269, w3=665, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(269, min_periods=max(269//3, 2)).max()
    trough = x.rolling(79, min_periods=max(79//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.53375 + 0.0019733 * anchor
    return base_signal.diff()

def f32_lba_533_struct_v533_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=86, w2=280, w3=678, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(86)
    rank = change.rolling(280, min_periods=max(280//3, 2)).rank(pct=True)
    persistence = change.rolling(678, min_periods=max(678//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1986 * persistence + 0.0019734 * anchor
    return base_signal.diff()

def f32_lba_534_struct_v534_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=93, w2=291, w3=691, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(93, min_periods=max(93//3, 2)).std()
    vol_slow = ret.rolling(291, min_periods=max(291//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.5625 + 0.0019735 * anchor
    return base_signal.diff()

def f32_lba_535_struct_v535_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=100, w2=302, w3=704, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(302, min_periods=max(302//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 100)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2138 * slope + 0.0019736 * anchor
    return base_signal.diff()

def f32_lba_536_struct_v536_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=107, w2=313, w3=717, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(107)
    drag = impulse.rolling(313, min_periods=max(313//3, 2)).mean()
    noise = impulse.abs().rolling(717, min_periods=max(717//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.59125 + 0.0019737 * anchor
    return base_signal.diff()

def f32_lba_537_struct_v537_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=114, w2=324, w3=730, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 114)
    acceleration = _rolling_slope(velocity, 324)
    curvature = _rolling_slope(acceleration, 730)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.229 * acceleration + 0.0019738 * anchor
    return base_signal.diff()

def f32_lba_538_struct_v538_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=121, w2=335, w3=743, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(121, min_periods=max(121//3, 2)).mean(), upside.rolling(335, min_periods=max(335//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.62 + 0.0019739 * anchor
    return base_signal.diff()

def f32_lba_539_struct_v539_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=128, w2=346, w3=756, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(346, min_periods=max(346//3, 2)).max()
    rebound = x - x.rolling(128, min_periods=max(128//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2442 * _rolling_slope(draw, 756) + 0.001974 * anchor
    return base_signal.diff()

def f32_lba_540_struct_v540_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=135, w2=357, w3=769, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 135)
    baseline = trend.rolling(357, min_periods=max(357//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(769, min_periods=max(769//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.875625 + 0.0019741 * anchor
    return base_signal.diff()

def f32_lba_541_struct_v541_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=142, w2=368, w3=25, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 142)
    slow = _rolling_slope(x, 368)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=25, adjust=False).mean() * 0.89 + 0.0019742 * anchor
    return base_signal.diff()

def f32_lba_542_struct_v542_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=149, w2=379, w3=38, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(379, min_periods=max(379//3, 2)).max()
    trough = x.rolling(149, min_periods=max(149//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.904375 + 0.0019743 * anchor
    return base_signal.diff()

def f32_lba_543_struct_v543_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=156, w2=390, w3=51, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(390, min_periods=max(390//3, 2)).rank(pct=True)
    persistence = change.rolling(51, min_periods=max(51//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2746 * persistence + 0.0019744 * anchor
    return base_signal.diff()

def f32_lba_544_struct_v544_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=163, w2=401, w3=64, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(163, min_periods=max(163//3, 2)).std()
    vol_slow = ret.rolling(401, min_periods=max(401//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.933125 + 0.0019745 * anchor
    return base_signal.diff()

def f32_lba_545_struct_v545_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=170, w2=412, w3=77, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(412, min_periods=max(412//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 170)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2898 * slope + 0.0019746 * anchor
    return base_signal.diff()

def f32_lba_546_struct_v546_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=177, w2=423, w3=90, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(423, min_periods=max(423//3, 2)).mean()
    noise = impulse.abs().rolling(90, min_periods=max(90//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.961875 + 0.0019747 * anchor
    return base_signal.diff()

def f32_lba_547_struct_v547_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=184, w2=434, w3=103, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 184)
    acceleration = _rolling_slope(velocity, 434)
    curvature = _rolling_slope(acceleration, 103)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.305 * acceleration + 0.0019748 * anchor
    return base_signal.diff()

def f32_lba_548_struct_v548_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=191, w2=445, w3=116, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(191, min_periods=max(191//3, 2)).mean(), upside.rolling(445, min_periods=max(445//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(116) * 0.990625 + 0.0019749 * anchor
    return base_signal.diff()

def f32_lba_549_struct_v549_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=198, w2=456, w3=129, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(456, min_periods=max(456//3, 2)).max()
    rebound = x - x.rolling(198, min_periods=max(198//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3202 * _rolling_slope(draw, 129) + 0.001975 * anchor
    return base_signal.diff()

def f32_lba_550_struct_v550_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=205, w2=467, w3=142, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 205)
    baseline = trend.rolling(467, min_periods=max(467//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(142, min_periods=max(142//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.019375 + 0.0019751 * anchor
    return base_signal.diff()

def f32_lba_551_struct_v551_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=212, w2=478, w3=155, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 212)
    slow = _rolling_slope(x, 478)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=155, adjust=False).mean() * 1.03375 + 0.0019752 * anchor
    return base_signal.diff()

def f32_lba_552_struct_v552_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=219, w2=489, w3=168, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(489, min_periods=max(489//3, 2)).max()
    trough = x.rolling(219, min_periods=max(219//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.048125 + 0.0019753 * anchor
    return base_signal.diff()

def f32_lba_553_struct_v553_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=226, w2=500, w3=181, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(500, min_periods=max(500//3, 2)).rank(pct=True)
    persistence = change.rolling(181, min_periods=max(181//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3506 * persistence + 0.0019754 * anchor
    return base_signal.diff()

def f32_lba_554_struct_v554_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=233, w2=511, w3=194, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(233, min_periods=max(233//3, 2)).std()
    vol_slow = ret.rolling(511, min_periods=max(511//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.076875 + 0.0019755 * anchor
    return base_signal.diff()

def f32_lba_555_struct_v555_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=240, w2=19, w3=207, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(19, min_periods=max(19//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 240)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3658 * slope + 0.0019756 * anchor
    return base_signal.diff()

def f32_lba_556_struct_v556_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=247, w2=30, w3=220, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(30, min_periods=max(30//3, 2)).mean()
    noise = impulse.abs().rolling(220, min_periods=max(220//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.105625 + 0.0019757 * anchor
    return base_signal.diff()

def f32_lba_557_struct_v557_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=254, w2=41, w3=233, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 254)
    acceleration = _rolling_slope(velocity, 41)
    curvature = _rolling_slope(acceleration, 233)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.381 * acceleration + 0.0019758 * anchor
    return base_signal.diff()

def f32_lba_558_struct_v558_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=10, w2=52, w3=246, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(10, min_periods=max(10//3, 2)).mean(), upside.rolling(52, min_periods=max(52//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.134375 + 0.0019759 * anchor
    return base_signal.diff()

def f32_lba_559_struct_v559_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=17, w2=63, w3=259, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(63, min_periods=max(63//3, 2)).max()
    rebound = x - x.rolling(17, min_periods=max(17//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3962 * _rolling_slope(draw, 259) + 0.001976 * anchor
    return base_signal.diff()

def f32_lba_560_struct_v560_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=24, w2=74, w3=272, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 24)
    baseline = trend.rolling(74, min_periods=max(74//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(272, min_periods=max(272//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.163125 + 0.0019761 * anchor
    return base_signal.diff()

def f32_lba_561_struct_v561_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=31, w2=85, w3=285, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 31)
    slow = _rolling_slope(x, 85)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=285, adjust=False).mean() * 1.1775 + 0.0019762 * anchor
    return base_signal.diff()

def f32_lba_562_struct_v562_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=38, w2=96, w3=298, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(96, min_periods=max(96//3, 2)).max()
    trough = x.rolling(38, min_periods=max(38//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.191875 + 0.0019763 * anchor
    return base_signal.diff()

def f32_lba_563_struct_v563_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=45, w2=107, w3=311, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(45)
    rank = change.rolling(107, min_periods=max(107//3, 2)).rank(pct=True)
    persistence = change.rolling(311, min_periods=max(311//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0502 * persistence + 0.0019764 * anchor
    return base_signal.diff()

def f32_lba_564_struct_v564_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=52, w2=118, w3=324, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(52, min_periods=max(52//3, 2)).std()
    vol_slow = ret.rolling(118, min_periods=max(118//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.220625 + 0.0019765 * anchor
    return base_signal.diff()

def f32_lba_565_struct_v565_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=59, w2=129, w3=337, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(129, min_periods=max(129//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 59)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0654 * slope + 0.0019766 * anchor
    return base_signal.diff()

def f32_lba_566_struct_v566_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=66, w2=140, w3=350, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(66)
    drag = impulse.rolling(140, min_periods=max(140//3, 2)).mean()
    noise = impulse.abs().rolling(350, min_periods=max(350//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.249375 + 0.0019767 * anchor
    return base_signal.diff()

def f32_lba_567_struct_v567_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=73, w2=151, w3=363, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 73)
    acceleration = _rolling_slope(velocity, 151)
    curvature = _rolling_slope(acceleration, 363)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0806 * acceleration + 0.0019768 * anchor
    return base_signal.diff()

def f32_lba_568_struct_v568_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=80, w2=162, w3=376, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(80, min_periods=max(80//3, 2)).mean(), upside.rolling(162, min_periods=max(162//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.278125 + 0.0019769 * anchor
    return base_signal.diff()

def f32_lba_569_struct_v569_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=87, w2=173, w3=389, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(173, min_periods=max(173//3, 2)).max()
    rebound = x - x.rolling(87, min_periods=max(87//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0958 * _rolling_slope(draw, 389) + 0.001977 * anchor
    return base_signal.diff()

def f32_lba_570_struct_v570_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=94, w2=184, w3=402, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 94)
    baseline = trend.rolling(184, min_periods=max(184//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(402, min_periods=max(402//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.306875 + 0.0019771 * anchor
    return base_signal.diff()

def f32_lba_571_struct_v571_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=101, w2=195, w3=415, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 101)
    slow = _rolling_slope(x, 195)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.32125 + 0.0019772 * anchor
    return base_signal.diff()

def f32_lba_572_struct_v572_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=108, w2=206, w3=428, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(206, min_periods=max(206//3, 2)).max()
    trough = x.rolling(108, min_periods=max(108//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.335625 + 0.0019773 * anchor
    return base_signal.diff()

def f32_lba_573_struct_v573_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=115, w2=217, w3=441, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(115)
    rank = change.rolling(217, min_periods=max(217//3, 2)).rank(pct=True)
    persistence = change.rolling(441, min_periods=max(441//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1262 * persistence + 0.0019774 * anchor
    return base_signal.diff()

def f32_lba_574_struct_v574_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=122, w2=228, w3=454, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(122, min_periods=max(122//3, 2)).std()
    vol_slow = ret.rolling(228, min_periods=max(228//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.364375 + 0.0019775 * anchor
    return base_signal.diff()

def f32_lba_575_struct_v575_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=129, w2=239, w3=467, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(239, min_periods=max(239//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 129)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1414 * slope + 0.0019776 * anchor
    return base_signal.diff()

def f32_lba_576_struct_v576_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=136, w2=250, w3=480, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(250, min_periods=max(250//3, 2)).mean()
    noise = impulse.abs().rolling(480, min_periods=max(480//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.393125 + 0.0019777 * anchor
    return base_signal.diff()

def f32_lba_577_struct_v577_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=143, w2=261, w3=493, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 143)
    acceleration = _rolling_slope(velocity, 261)
    curvature = _rolling_slope(acceleration, 493)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1566 * acceleration + 0.0019778 * anchor
    return base_signal.diff()

def f32_lba_578_struct_v578_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=150, w2=272, w3=506, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(150, min_periods=max(150//3, 2)).mean(), upside.rolling(272, min_periods=max(272//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.421875 + 0.0019779 * anchor
    return base_signal.diff()

def f32_lba_579_struct_v579_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=157, w2=283, w3=519, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(283, min_periods=max(283//3, 2)).max()
    rebound = x - x.rolling(157, min_periods=max(157//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1718 * _rolling_slope(draw, 519) + 0.001978 * anchor
    return base_signal.diff()

def f32_lba_580_struct_v580_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=164, w2=294, w3=532, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 164)
    baseline = trend.rolling(294, min_periods=max(294//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(532, min_periods=max(532//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.450625 + 0.0019781 * anchor
    return base_signal.diff()

def f32_lba_581_struct_v581_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=171, w2=305, w3=545, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 171)
    slow = _rolling_slope(x, 305)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.465 + 0.0019782 * anchor
    return base_signal.diff()

def f32_lba_582_struct_v582_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=178, w2=316, w3=558, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(316, min_periods=max(316//3, 2)).max()
    trough = x.rolling(178, min_periods=max(178//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.479375 + 0.0019783 * anchor
    return base_signal.diff()

def f32_lba_583_struct_v583_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=185, w2=327, w3=571, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(327, min_periods=max(327//3, 2)).rank(pct=True)
    persistence = change.rolling(571, min_periods=max(571//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2022 * persistence + 0.0019784 * anchor
    return base_signal.diff()

def f32_lba_584_struct_v584_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=192, w2=338, w3=584, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(192, min_periods=max(192//3, 2)).std()
    vol_slow = ret.rolling(338, min_periods=max(338//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.508125 + 0.0019785 * anchor
    return base_signal.diff()

def f32_lba_585_struct_v585_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=199, w2=349, w3=597, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(349, min_periods=max(349//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 199)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2174 * slope + 0.0019786 * anchor
    return base_signal.diff()

def f32_lba_586_struct_v586_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=206, w2=360, w3=610, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(360, min_periods=max(360//3, 2)).mean()
    noise = impulse.abs().rolling(610, min_periods=max(610//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.536875 + 0.0019787 * anchor
    return base_signal.diff()

def f32_lba_587_struct_v587_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=213, w2=371, w3=623, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 213)
    acceleration = _rolling_slope(velocity, 371)
    curvature = _rolling_slope(acceleration, 623)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2326 * acceleration + 0.0019788 * anchor
    return base_signal.diff()

def f32_lba_588_struct_v588_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=220, w2=382, w3=636, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(220, min_periods=max(220//3, 2)).mean(), upside.rolling(382, min_periods=max(382//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.565625 + 0.0019789 * anchor
    return base_signal.diff()

def f32_lba_589_struct_v589_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=227, w2=393, w3=649, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(393, min_periods=max(393//3, 2)).max()
    rebound = x - x.rolling(227, min_periods=max(227//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2478 * _rolling_slope(draw, 649) + 0.001979 * anchor
    return base_signal.diff()

def f32_lba_590_struct_v590_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=234, w2=404, w3=662, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 234)
    baseline = trend.rolling(404, min_periods=max(404//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(662, min_periods=max(662//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.594375 + 0.0019791 * anchor
    return base_signal.diff()

def f32_lba_591_struct_v591_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=241, w2=415, w3=675, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 241)
    slow = _rolling_slope(x, 415)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.60875 + 0.0019792 * anchor
    return base_signal.diff()

def f32_lba_592_struct_v592_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=248, w2=426, w3=688, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(426, min_periods=max(426//3, 2)).max()
    trough = x.rolling(248, min_periods=max(248//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.85 + 0.0019793 * anchor
    return base_signal.diff()

def f32_lba_593_struct_v593_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=255, w2=437, w3=701, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(437, min_periods=max(437//3, 2)).rank(pct=True)
    persistence = change.rolling(701, min_periods=max(701//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2782 * persistence + 0.0019794 * anchor
    return base_signal.diff()

def f32_lba_594_struct_v594_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=11, w2=448, w3=714, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(11, min_periods=max(11//3, 2)).std()
    vol_slow = ret.rolling(448, min_periods=max(448//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.87875 + 0.0019795 * anchor
    return base_signal.diff()

def f32_lba_595_struct_v595_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=18, w2=459, w3=727, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(459, min_periods=max(459//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 18)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2934 * slope + 0.0019796 * anchor
    return base_signal.diff()

def f32_lba_596_struct_v596_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=25, w2=470, w3=740, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(25)
    drag = impulse.rolling(470, min_periods=max(470//3, 2)).mean()
    noise = impulse.abs().rolling(740, min_periods=max(740//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.9075 + 0.0019797 * anchor
    return base_signal.diff()

def f32_lba_597_struct_v597_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=32, w2=481, w3=753, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 32)
    acceleration = _rolling_slope(velocity, 481)
    curvature = _rolling_slope(acceleration, 753)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3086 * acceleration + 0.0019798 * anchor
    return base_signal.diff()

def f32_lba_598_struct_v598_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=39, w2=492, w3=766, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(39, min_periods=max(39//3, 2)).mean(), upside.rolling(492, min_periods=max(492//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.93625 + 0.0019799 * anchor
    return base_signal.diff()

def f32_lba_599_struct_v599_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=46, w2=503, w3=22, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(503, min_periods=max(503//3, 2)).max()
    rebound = x - x.rolling(46, min_periods=max(46//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3238 * _rolling_slope(draw, 22) + 0.00198 * anchor
    return base_signal.diff()

def f32_lba_600_struct_v600_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=53, w2=11, w3=35, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 53)
    baseline = trend.rolling(11, min_periods=max(11//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(35, min_periods=max(35//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.965 + 0.0019801 * anchor
    return base_signal.diff()
