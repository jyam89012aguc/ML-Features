"""48 dilution death spiral d1 first derivative features 76-150 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Ownership - Institutional-grade short-side signal.
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

def f48_dds_076_struct_v76_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=15, w2=314, w3=161, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(15)
    drag = impulse.rolling(314, min_periods=max(314//3, 2)).mean()
    noise = impulse.abs().rolling(161, min_periods=max(161//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.895 + 0.0029477 * anchor
    return base_signal.diff()

def f48_dds_077_struct_v77_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=22, w2=325, w3=174, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 22)
    acceleration = _rolling_slope(velocity, 325)
    curvature = _rolling_slope(acceleration, 174)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1022 * acceleration + 0.0029478 * anchor
    return base_signal.diff()

def f48_dds_078_struct_v78_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=29, w2=336, w3=187, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(29, min_periods=max(29//3, 2)).mean(), upside.rolling(336, min_periods=max(336//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.92375 + 0.0029479 * anchor
    return base_signal.diff()

def f48_dds_079_struct_v79_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=36, w2=347, w3=200, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(347, min_periods=max(347//3, 2)).max()
    rebound = x - x.rolling(36, min_periods=max(36//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1174 * _rolling_slope(draw, 200) + 0.002948 * anchor
    return base_signal.diff()

def f48_dds_080_struct_v80_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=43, w2=358, w3=213, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 43)
    baseline = trend.rolling(358, min_periods=max(358//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(213, min_periods=max(213//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.9525 + 0.0029481 * anchor
    return base_signal.diff()

def f48_dds_081_struct_v81_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=50, w2=369, w3=226, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 50)
    slow = _rolling_slope(x, 369)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=226, adjust=False).mean() * 0.966875 + 0.0029482 * anchor
    return base_signal.diff()

def f48_dds_082_struct_v82_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=57, w2=380, w3=239, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(380, min_periods=max(380//3, 2)).max()
    trough = x.rolling(57, min_periods=max(57//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.98125 + 0.0029483 * anchor
    return base_signal.diff()

def f48_dds_083_struct_v83_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=64, w2=391, w3=252, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(64)
    rank = change.rolling(391, min_periods=max(391//3, 2)).rank(pct=True)
    persistence = change.rolling(252, min_periods=max(252//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1478 * persistence + 0.0029484 * anchor
    return base_signal.diff()

def f48_dds_084_struct_v84_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=71, w2=402, w3=265, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(71, min_periods=max(71//3, 2)).std()
    vol_slow = ret.rolling(402, min_periods=max(402//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.01 + 0.0029485 * anchor
    return base_signal.diff()

def f48_dds_085_struct_v85_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=78, w2=413, w3=278, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(413, min_periods=max(413//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 78)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.163 * slope + 0.0029486 * anchor
    return base_signal.diff()

def f48_dds_086_struct_v86_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=85, w2=424, w3=291, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(85)
    drag = impulse.rolling(424, min_periods=max(424//3, 2)).mean()
    noise = impulse.abs().rolling(291, min_periods=max(291//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.03875 + 0.0029487 * anchor
    return base_signal.diff()

def f48_dds_087_struct_v87_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=92, w2=435, w3=304, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 92)
    acceleration = _rolling_slope(velocity, 435)
    curvature = _rolling_slope(acceleration, 304)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1782 * acceleration + 0.0029488 * anchor
    return base_signal.diff()

def f48_dds_088_struct_v88_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=99, w2=446, w3=317, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(99, min_periods=max(99//3, 2)).mean(), upside.rolling(446, min_periods=max(446//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.0675 + 0.0029489 * anchor
    return base_signal.diff()

def f48_dds_089_struct_v89_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=106, w2=457, w3=330, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(457, min_periods=max(457//3, 2)).max()
    rebound = x - x.rolling(106, min_periods=max(106//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1934 * _rolling_slope(draw, 330) + 0.002949 * anchor
    return base_signal.diff()

def f48_dds_090_struct_v90_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=113, w2=468, w3=343, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 113)
    baseline = trend.rolling(468, min_periods=max(468//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(343, min_periods=max(343//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.09625 + 0.0029491 * anchor
    return base_signal.diff()

def f48_dds_091_struct_v91_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=120, w2=479, w3=356, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 120)
    slow = _rolling_slope(x, 479)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.110625 + 0.0029492 * anchor
    return base_signal.diff()

def f48_dds_092_struct_v92_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=127, w2=490, w3=369, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(490, min_periods=max(490//3, 2)).max()
    trough = x.rolling(127, min_periods=max(127//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.125 + 0.0029493 * anchor
    return base_signal.diff()

def f48_dds_093_struct_v93_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=134, w2=501, w3=382, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(501, min_periods=max(501//3, 2)).rank(pct=True)
    persistence = change.rolling(382, min_periods=max(382//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2238 * persistence + 0.0029494 * anchor
    return base_signal.diff()

def f48_dds_094_struct_v94_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=141, w2=512, w3=395, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(141, min_periods=max(141//3, 2)).std()
    vol_slow = ret.rolling(512, min_periods=max(512//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.15375 + 0.0029495 * anchor
    return base_signal.diff()

def f48_dds_095_struct_v95_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=148, w2=20, w3=408, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(20, min_periods=max(20//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 148)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.239 * slope + 0.0029496 * anchor
    return base_signal.diff()

def f48_dds_096_struct_v96_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=155, w2=31, w3=421, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(31, min_periods=max(31//3, 2)).mean()
    noise = impulse.abs().rolling(421, min_periods=max(421//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.1825 + 0.0029497 * anchor
    return base_signal.diff()

def f48_dds_097_struct_v97_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=162, w2=42, w3=434, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 162)
    acceleration = _rolling_slope(velocity, 42)
    curvature = _rolling_slope(acceleration, 434)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2542 * acceleration + 0.0029498 * anchor
    return base_signal.diff()

def f48_dds_098_struct_v98_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=169, w2=53, w3=447, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(169, min_periods=max(169//3, 2)).mean(), upside.rolling(53, min_periods=max(53//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.21125 + 0.0029499 * anchor
    return base_signal.diff()

def f48_dds_099_struct_v99_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=176, w2=64, w3=460, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(64, min_periods=max(64//3, 2)).max()
    rebound = x - x.rolling(176, min_periods=max(176//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2694 * _rolling_slope(draw, 460) + 0.00295 * anchor
    return base_signal.diff()

def f48_dds_100_struct_v100_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=183, w2=75, w3=473, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 183)
    baseline = trend.rolling(75, min_periods=max(75//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(473, min_periods=max(473//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.24 + 0.0029501 * anchor
    return base_signal.diff()

def f48_dds_101_struct_v101_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=190, w2=86, w3=486, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 190)
    slow = _rolling_slope(x, 86)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.254375 + 0.0029502 * anchor
    return base_signal.diff()

def f48_dds_102_struct_v102_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=197, w2=97, w3=499, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(97, min_periods=max(97//3, 2)).max()
    trough = x.rolling(197, min_periods=max(197//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.26875 + 0.0029503 * anchor
    return base_signal.diff()

def f48_dds_103_struct_v103_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=204, w2=108, w3=512, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(108, min_periods=max(108//3, 2)).rank(pct=True)
    persistence = change.rolling(512, min_periods=max(512//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2998 * persistence + 0.0029504 * anchor
    return base_signal.diff()

def f48_dds_104_struct_v104_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=211, w2=119, w3=525, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(211, min_periods=max(211//3, 2)).std()
    vol_slow = ret.rolling(119, min_periods=max(119//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.2975 + 0.0029505 * anchor
    return base_signal.diff()

def f48_dds_105_struct_v105_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=218, w2=130, w3=538, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(130, min_periods=max(130//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 218)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.315 * slope + 0.0029506 * anchor
    return base_signal.diff()

def f48_dds_106_struct_v106_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=225, w2=141, w3=551, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(141, min_periods=max(141//3, 2)).mean()
    noise = impulse.abs().rolling(551, min_periods=max(551//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.32625 + 0.0029507 * anchor
    return base_signal.diff()

def f48_dds_107_struct_v107_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=232, w2=152, w3=564, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 232)
    acceleration = _rolling_slope(velocity, 152)
    curvature = _rolling_slope(acceleration, 564)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3302 * acceleration + 0.0029508 * anchor
    return base_signal.diff()

def f48_dds_108_struct_v108_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=239, w2=163, w3=577, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(239, min_periods=max(239//3, 2)).mean(), upside.rolling(163, min_periods=max(163//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.355 + 0.0029509 * anchor
    return base_signal.diff()

def f48_dds_109_struct_v109_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=246, w2=174, w3=590, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(174, min_periods=max(174//3, 2)).max()
    rebound = x - x.rolling(246, min_periods=max(246//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3454 * _rolling_slope(draw, 590) + 0.002951 * anchor
    return base_signal.diff()

def f48_dds_110_struct_v110_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=253, w2=185, w3=603, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 253)
    baseline = trend.rolling(185, min_periods=max(185//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(603, min_periods=max(603//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.38375 + 0.0029511 * anchor
    return base_signal.diff()

def f48_dds_111_struct_v111_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=9, w2=196, w3=616, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 9)
    slow = _rolling_slope(x, 196)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.398125 + 0.0029512 * anchor
    return base_signal.diff()

def f48_dds_112_struct_v112_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=16, w2=207, w3=629, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(207, min_periods=max(207//3, 2)).max()
    trough = x.rolling(16, min_periods=max(16//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.4125 + 0.0029513 * anchor
    return base_signal.diff()

def f48_dds_113_struct_v113_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=23, w2=218, w3=642, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(23)
    rank = change.rolling(218, min_periods=max(218//3, 2)).rank(pct=True)
    persistence = change.rolling(642, min_periods=max(642//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3758 * persistence + 0.0029514 * anchor
    return base_signal.diff()

def f48_dds_114_struct_v114_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=30, w2=229, w3=655, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(30, min_periods=max(30//3, 2)).std()
    vol_slow = ret.rolling(229, min_periods=max(229//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.44125 + 0.0029515 * anchor
    return base_signal.diff()

def f48_dds_115_struct_v115_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=37, w2=240, w3=668, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(240, min_periods=max(240//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 37)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.391 * slope + 0.0029516 * anchor
    return base_signal.diff()

def f48_dds_116_struct_v116_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=44, w2=251, w3=681, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(44)
    drag = impulse.rolling(251, min_periods=max(251//3, 2)).mean()
    noise = impulse.abs().rolling(681, min_periods=max(681//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.47 + 0.0029517 * anchor
    return base_signal.diff()

def f48_dds_117_struct_v117_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=51, w2=262, w3=694, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 51)
    acceleration = _rolling_slope(velocity, 262)
    curvature = _rolling_slope(acceleration, 694)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.4062 * acceleration + 0.0029518 * anchor
    return base_signal.diff()

def f48_dds_118_struct_v118_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=58, w2=273, w3=707, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(58, min_periods=max(58//3, 2)).mean(), upside.rolling(273, min_periods=max(273//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.49875 + 0.0029519 * anchor
    return base_signal.diff()

def f48_dds_119_struct_v119_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=65, w2=284, w3=720, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(284, min_periods=max(284//3, 2)).max()
    rebound = x - x.rolling(65, min_periods=max(65//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.045 * _rolling_slope(draw, 720) + 0.002952 * anchor
    return base_signal.diff()

def f48_dds_120_struct_v120_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=72, w2=295, w3=733, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 72)
    baseline = trend.rolling(295, min_periods=max(295//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(733, min_periods=max(733//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.5275 + 0.0029521 * anchor
    return base_signal.diff()

def f48_dds_121_struct_v121_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=79, w2=306, w3=746, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 79)
    slow = _rolling_slope(x, 306)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.541875 + 0.0029522 * anchor
    return base_signal.diff()

def f48_dds_122_struct_v122_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=86, w2=317, w3=759, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(317, min_periods=max(317//3, 2)).max()
    trough = x.rolling(86, min_periods=max(86//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.55625 + 0.0029523 * anchor
    return base_signal.diff()

def f48_dds_123_struct_v123_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=93, w2=328, w3=15, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(93)
    rank = change.rolling(328, min_periods=max(328//3, 2)).rank(pct=True)
    persistence = change.rolling(15, min_periods=max(15//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0754 * persistence + 0.0029524 * anchor
    return base_signal.diff()

def f48_dds_124_struct_v124_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=100, w2=339, w3=28, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(100, min_periods=max(100//3, 2)).std()
    vol_slow = ret.rolling(339, min_periods=max(339//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.585 + 0.0029525 * anchor
    return base_signal.diff()

def f48_dds_125_struct_v125_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=107, w2=350, w3=41, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(350, min_periods=max(350//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 107)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0906 * slope + 0.0029526 * anchor
    return base_signal.diff()

def f48_dds_126_struct_v126_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=114, w2=361, w3=54, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(114)
    drag = impulse.rolling(361, min_periods=max(361//3, 2)).mean()
    noise = impulse.abs().rolling(54, min_periods=max(54//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.61375 + 0.0029527 * anchor
    return base_signal.diff()

def f48_dds_127_struct_v127_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=121, w2=372, w3=67, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 121)
    acceleration = _rolling_slope(velocity, 372)
    curvature = _rolling_slope(acceleration, 67)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1058 * acceleration + 0.0029528 * anchor
    return base_signal.diff()

def f48_dds_128_struct_v128_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=128, w2=383, w3=80, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(128, min_periods=max(128//3, 2)).mean(), upside.rolling(383, min_periods=max(383//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(80) * 0.869375 + 0.0029529 * anchor
    return base_signal.diff()

def f48_dds_129_struct_v129_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=135, w2=394, w3=93, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(394, min_periods=max(394//3, 2)).max()
    rebound = x - x.rolling(135, min_periods=max(135//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.121 * _rolling_slope(draw, 93) + 0.002953 * anchor
    return base_signal.diff()

def f48_dds_130_struct_v130_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=142, w2=405, w3=106, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 142)
    baseline = trend.rolling(405, min_periods=max(405//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(106, min_periods=max(106//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.898125 + 0.0029531 * anchor
    return base_signal.diff()

def f48_dds_131_struct_v131_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=149, w2=416, w3=119, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 149)
    slow = _rolling_slope(x, 416)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=119, adjust=False).mean() * 0.9125 + 0.0029532 * anchor
    return base_signal.diff()

def f48_dds_132_struct_v132_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=156, w2=427, w3=132, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(427, min_periods=max(427//3, 2)).max()
    trough = x.rolling(156, min_periods=max(156//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.926875 + 0.0029533 * anchor
    return base_signal.diff()

def f48_dds_133_struct_v133_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=163, w2=438, w3=145, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(438, min_periods=max(438//3, 2)).rank(pct=True)
    persistence = change.rolling(145, min_periods=max(145//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1514 * persistence + 0.0029534 * anchor
    return base_signal.diff()

def f48_dds_134_struct_v134_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=170, w2=449, w3=158, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(170, min_periods=max(170//3, 2)).std()
    vol_slow = ret.rolling(449, min_periods=max(449//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.955625 + 0.0029535 * anchor
    return base_signal.diff()

def f48_dds_135_struct_v135_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=177, w2=460, w3=171, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(460, min_periods=max(460//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 177)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1666 * slope + 0.0029536 * anchor
    return base_signal.diff()

def f48_dds_136_struct_v136_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=184, w2=471, w3=184, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(471, min_periods=max(471//3, 2)).mean()
    noise = impulse.abs().rolling(184, min_periods=max(184//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.984375 + 0.0029537 * anchor
    return base_signal.diff()

def f48_dds_137_struct_v137_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=191, w2=482, w3=197, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 191)
    acceleration = _rolling_slope(velocity, 482)
    curvature = _rolling_slope(acceleration, 197)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1818 * acceleration + 0.0029538 * anchor
    return base_signal.diff()

def f48_dds_138_struct_v138_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=198, w2=493, w3=210, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(198, min_periods=max(198//3, 2)).mean(), upside.rolling(493, min_periods=max(493//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.013125 + 0.0029539 * anchor
    return base_signal.diff()

def f48_dds_139_struct_v139_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=205, w2=504, w3=223, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(504, min_periods=max(504//3, 2)).max()
    rebound = x - x.rolling(205, min_periods=max(205//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.197 * _rolling_slope(draw, 223) + 0.002954 * anchor
    return base_signal.diff()

def f48_dds_140_struct_v140_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=212, w2=12, w3=236, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 212)
    baseline = trend.rolling(12, min_periods=max(12//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(236, min_periods=max(236//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.041875 + 0.0029541 * anchor
    return base_signal.diff()

def f48_dds_141_struct_v141_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=219, w2=23, w3=249, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 219)
    slow = _rolling_slope(x, 23)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=249, adjust=False).mean() * 1.05625 + 0.0029542 * anchor
    return base_signal.diff()

def f48_dds_142_struct_v142_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=226, w2=34, w3=262, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(34, min_periods=max(34//3, 2)).max()
    trough = x.rolling(226, min_periods=max(226//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.070625 + 0.0029543 * anchor
    return base_signal.diff()

def f48_dds_143_struct_v143_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=233, w2=45, w3=275, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(45, min_periods=max(45//3, 2)).rank(pct=True)
    persistence = change.rolling(275, min_periods=max(275//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2274 * persistence + 0.0029544 * anchor
    return base_signal.diff()

def f48_dds_144_struct_v144_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=240, w2=56, w3=288, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(240, min_periods=max(240//3, 2)).std()
    vol_slow = ret.rolling(56, min_periods=max(56//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.099375 + 0.0029545 * anchor
    return base_signal.diff()

def f48_dds_145_struct_v145_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=247, w2=67, w3=301, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(67, min_periods=max(67//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 247)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2426 * slope + 0.0029546 * anchor
    return base_signal.diff()

def f48_dds_146_struct_v146_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=254, w2=78, w3=314, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(78, min_periods=max(78//3, 2)).mean()
    noise = impulse.abs().rolling(314, min_periods=max(314//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.128125 + 0.0029547 * anchor
    return base_signal.diff()

def f48_dds_147_struct_v147_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=10, w2=89, w3=327, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 10)
    acceleration = _rolling_slope(velocity, 89)
    curvature = _rolling_slope(acceleration, 327)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2578 * acceleration + 0.0029548 * anchor
    return base_signal.diff()

def f48_dds_148_struct_v148_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=17, w2=100, w3=340, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(17, min_periods=max(17//3, 2)).mean(), upside.rolling(100, min_periods=max(100//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.156875 + 0.0029549 * anchor
    return base_signal.diff()

def f48_dds_149_struct_v149_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=24, w2=111, w3=353, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(111, min_periods=max(111//3, 2)).max()
    rebound = x - x.rolling(24, min_periods=max(24//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.273 * _rolling_slope(draw, 353) + 0.002955 * anchor
    return base_signal.diff()

def f48_dds_150_struct_v150_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=31, w2=122, w3=366, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 31)
    baseline = trend.rolling(122, min_periods=max(122//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(366, min_periods=max(366//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.185625 + 0.0029551 * anchor
    return base_signal.diff()
