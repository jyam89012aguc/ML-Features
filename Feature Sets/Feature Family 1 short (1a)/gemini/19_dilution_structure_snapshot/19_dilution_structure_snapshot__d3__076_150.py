"""19 dilution structure snapshot d3 third derivative features 76-150 â€” Pipeline 1a-HF Grade v3.

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

def f19_dilu_076_struct_v76_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=17, w2=496, w3=74, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(17)
    drag = impulse.rolling(496, min_periods=max(496//3, 2)).mean()
    noise = impulse.abs().rolling(74, min_periods=max(74//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.141875 + 0.0011477 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_077_struct_v77_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=24, w2=507, w3=87, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 24)
    acceleration = _rolling_slope(velocity, 507)
    curvature = _rolling_slope(acceleration, 87)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3118 * acceleration + 0.0011478 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_078_struct_v78_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=31, w2=15, w3=100, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(31, min_periods=max(31//3, 2)).mean(), upside.rolling(15, min_periods=max(15//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(100) * 1.170625 + 0.0011479 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_079_struct_v79_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=38, w2=26, w3=113, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(26, min_periods=max(26//3, 2)).max()
    rebound = x - x.rolling(38, min_periods=max(38//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.327 * _rolling_slope(draw, 113) + 0.001148 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_080_struct_v80_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=45, w2=37, w3=126, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 45)
    baseline = trend.rolling(37, min_periods=max(37//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(126, min_periods=max(126//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.199375 + 0.0011481 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_081_struct_v81_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=52, w2=48, w3=139, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 52)
    slow = _rolling_slope(x, 48)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=139, adjust=False).mean() * 1.21375 + 0.0011482 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_082_struct_v82_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=59, w2=59, w3=152, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(59, min_periods=max(59//3, 2)).max()
    trough = x.rolling(59, min_periods=max(59//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.228125 + 0.0011483 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_083_struct_v83_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=66, w2=70, w3=165, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(66)
    rank = change.rolling(70, min_periods=max(70//3, 2)).rank(pct=True)
    persistence = change.rolling(165, min_periods=max(165//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3574 * persistence + 0.0011484 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_084_struct_v84_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=73, w2=81, w3=178, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(73, min_periods=max(73//3, 2)).std()
    vol_slow = ret.rolling(81, min_periods=max(81//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.256875 + 0.0011485 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_085_struct_v85_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=80, w2=92, w3=191, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(92, min_periods=max(92//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 80)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3726 * slope + 0.0011486 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_086_struct_v86_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=87, w2=103, w3=204, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(87)
    drag = impulse.rolling(103, min_periods=max(103//3, 2)).mean()
    noise = impulse.abs().rolling(204, min_periods=max(204//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.285625 + 0.0011487 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_087_struct_v87_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=94, w2=114, w3=217, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 94)
    acceleration = _rolling_slope(velocity, 114)
    curvature = _rolling_slope(acceleration, 217)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3878 * acceleration + 0.0011488 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_088_struct_v88_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=101, w2=125, w3=230, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(101, min_periods=max(101//3, 2)).mean(), upside.rolling(125, min_periods=max(125//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.314375 + 0.0011489 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_089_struct_v89_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=108, w2=136, w3=243, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(136, min_periods=max(136//3, 2)).max()
    rebound = x - x.rolling(108, min_periods=max(108//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.403 * _rolling_slope(draw, 243) + 0.001149 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_090_struct_v90_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=115, w2=147, w3=256, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 115)
    baseline = trend.rolling(147, min_periods=max(147//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(256, min_periods=max(256//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.343125 + 0.0011491 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_091_struct_v91_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=122, w2=158, w3=269, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 122)
    slow = _rolling_slope(x, 158)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=269, adjust=False).mean() * 1.3575 + 0.0011492 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_092_struct_v92_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=129, w2=169, w3=282, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(169, min_periods=max(169//3, 2)).max()
    trough = x.rolling(129, min_periods=max(129//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.371875 + 0.0011493 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_093_struct_v93_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=136, w2=180, w3=295, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(180, min_periods=max(180//3, 2)).rank(pct=True)
    persistence = change.rolling(295, min_periods=max(295//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.057 * persistence + 0.0011494 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_094_struct_v94_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=143, w2=191, w3=308, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(143, min_periods=max(143//3, 2)).std()
    vol_slow = ret.rolling(191, min_periods=max(191//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.400625 + 0.0011495 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_095_struct_v95_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=150, w2=202, w3=321, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(202, min_periods=max(202//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 150)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0722 * slope + 0.0011496 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_096_struct_v96_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=157, w2=213, w3=334, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(213, min_periods=max(213//3, 2)).mean()
    noise = impulse.abs().rolling(334, min_periods=max(334//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.429375 + 0.0011497 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_097_struct_v97_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=164, w2=224, w3=347, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 164)
    acceleration = _rolling_slope(velocity, 224)
    curvature = _rolling_slope(acceleration, 347)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0874 * acceleration + 0.0011498 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_098_struct_v98_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=171, w2=235, w3=360, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(171, min_periods=max(171//3, 2)).mean(), upside.rolling(235, min_periods=max(235//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.458125 + 0.0011499 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_099_struct_v99_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=178, w2=246, w3=373, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(246, min_periods=max(246//3, 2)).max()
    rebound = x - x.rolling(178, min_periods=max(178//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1026 * _rolling_slope(draw, 373) + 0.00115 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_100_struct_v100_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=185, w2=257, w3=386, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 185)
    baseline = trend.rolling(257, min_periods=max(257//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(386, min_periods=max(386//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.486875 + 0.0011501 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_101_struct_v101_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=192, w2=268, w3=399, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 192)
    slow = _rolling_slope(x, 268)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.50125 + 0.0011502 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_102_struct_v102_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=199, w2=279, w3=412, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(279, min_periods=max(279//3, 2)).max()
    trough = x.rolling(199, min_periods=max(199//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.515625 + 0.0011503 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_103_struct_v103_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=206, w2=290, w3=425, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(290, min_periods=max(290//3, 2)).rank(pct=True)
    persistence = change.rolling(425, min_periods=max(425//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.133 * persistence + 0.0011504 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_104_struct_v104_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=213, w2=301, w3=438, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(213, min_periods=max(213//3, 2)).std()
    vol_slow = ret.rolling(301, min_periods=max(301//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.544375 + 0.0011505 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_105_struct_v105_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=220, w2=312, w3=451, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(312, min_periods=max(312//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 220)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1482 * slope + 0.0011506 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_106_struct_v106_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=227, w2=323, w3=464, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(323, min_periods=max(323//3, 2)).mean()
    noise = impulse.abs().rolling(464, min_periods=max(464//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.573125 + 0.0011507 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_107_struct_v107_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=234, w2=334, w3=477, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 234)
    acceleration = _rolling_slope(velocity, 334)
    curvature = _rolling_slope(acceleration, 477)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1634 * acceleration + 0.0011508 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_108_struct_v108_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=241, w2=345, w3=490, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(241, min_periods=max(241//3, 2)).mean(), upside.rolling(345, min_periods=max(345//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.601875 + 0.0011509 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_109_struct_v109_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=248, w2=356, w3=503, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(356, min_periods=max(356//3, 2)).max()
    rebound = x - x.rolling(248, min_periods=max(248//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1786 * _rolling_slope(draw, 503) + 0.001151 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_110_struct_v110_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=255, w2=367, w3=516, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 255)
    baseline = trend.rolling(367, min_periods=max(367//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(516, min_periods=max(516//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.8575 + 0.0011511 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_111_struct_v111_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=11, w2=378, w3=529, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 11)
    slow = _rolling_slope(x, 378)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.871875 + 0.0011512 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_112_struct_v112_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=18, w2=389, w3=542, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(389, min_periods=max(389//3, 2)).max()
    trough = x.rolling(18, min_periods=max(18//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.88625 + 0.0011513 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_113_struct_v113_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=25, w2=400, w3=555, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(25)
    rank = change.rolling(400, min_periods=max(400//3, 2)).rank(pct=True)
    persistence = change.rolling(555, min_periods=max(555//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.209 * persistence + 0.0011514 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_114_struct_v114_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=32, w2=411, w3=568, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(32, min_periods=max(32//3, 2)).std()
    vol_slow = ret.rolling(411, min_periods=max(411//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.915 + 0.0011515 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_115_struct_v115_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=39, w2=422, w3=581, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(422, min_periods=max(422//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 39)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2242 * slope + 0.0011516 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_116_struct_v116_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=46, w2=433, w3=594, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(46)
    drag = impulse.rolling(433, min_periods=max(433//3, 2)).mean()
    noise = impulse.abs().rolling(594, min_periods=max(594//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.94375 + 0.0011517 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_117_struct_v117_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=53, w2=444, w3=607, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 53)
    acceleration = _rolling_slope(velocity, 444)
    curvature = _rolling_slope(acceleration, 607)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2394 * acceleration + 0.0011518 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_118_struct_v118_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=60, w2=455, w3=620, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(60, min_periods=max(60//3, 2)).mean(), upside.rolling(455, min_periods=max(455//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.9725 + 0.0011519 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_119_struct_v119_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=67, w2=466, w3=633, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(466, min_periods=max(466//3, 2)).max()
    rebound = x - x.rolling(67, min_periods=max(67//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2546 * _rolling_slope(draw, 633) + 0.001152 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_120_struct_v120_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=74, w2=477, w3=646, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 74)
    baseline = trend.rolling(477, min_periods=max(477//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(646, min_periods=max(646//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.00125 + 0.0011521 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_121_struct_v121_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=81, w2=488, w3=659, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 81)
    slow = _rolling_slope(x, 488)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.015625 + 0.0011522 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_122_struct_v122_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=88, w2=499, w3=672, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(499, min_periods=max(499//3, 2)).max()
    trough = x.rolling(88, min_periods=max(88//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.03 + 0.0011523 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_123_struct_v123_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=95, w2=510, w3=685, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(95)
    rank = change.rolling(510, min_periods=max(510//3, 2)).rank(pct=True)
    persistence = change.rolling(685, min_periods=max(685//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.285 * persistence + 0.0011524 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_124_struct_v124_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=102, w2=18, w3=698, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(102, min_periods=max(102//3, 2)).std()
    vol_slow = ret.rolling(18, min_periods=max(18//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.05875 + 0.0011525 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_125_struct_v125_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=109, w2=29, w3=711, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(29, min_periods=max(29//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 109)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3002 * slope + 0.0011526 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_126_struct_v126_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=116, w2=40, w3=724, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(116)
    drag = impulse.rolling(40, min_periods=max(40//3, 2)).mean()
    noise = impulse.abs().rolling(724, min_periods=max(724//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.0875 + 0.0011527 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_127_struct_v127_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=123, w2=51, w3=737, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 123)
    acceleration = _rolling_slope(velocity, 51)
    curvature = _rolling_slope(acceleration, 737)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3154 * acceleration + 0.0011528 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_128_struct_v128_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=130, w2=62, w3=750, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(130, min_periods=max(130//3, 2)).mean(), upside.rolling(62, min_periods=max(62//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.11625 + 0.0011529 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_129_struct_v129_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=137, w2=73, w3=763, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(73, min_periods=max(73//3, 2)).max()
    rebound = x - x.rolling(137, min_periods=max(137//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3306 * _rolling_slope(draw, 763) + 0.001153 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_130_struct_v130_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=144, w2=84, w3=19, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 144)
    baseline = trend.rolling(84, min_periods=max(84//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(19, min_periods=max(19//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.145 + 0.0011531 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_131_struct_v131_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=151, w2=95, w3=32, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 151)
    slow = _rolling_slope(x, 95)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=32, adjust=False).mean() * 1.159375 + 0.0011532 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_132_struct_v132_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=158, w2=106, w3=45, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(106, min_periods=max(106//3, 2)).max()
    trough = x.rolling(158, min_periods=max(158//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.17375 + 0.0011533 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_133_struct_v133_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=165, w2=117, w3=58, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(117, min_periods=max(117//3, 2)).rank(pct=True)
    persistence = change.rolling(58, min_periods=max(58//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.361 * persistence + 0.0011534 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_134_struct_v134_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=172, w2=128, w3=71, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(172, min_periods=max(172//3, 2)).std()
    vol_slow = ret.rolling(128, min_periods=max(128//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.2025 + 0.0011535 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_135_struct_v135_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=179, w2=139, w3=84, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(139, min_periods=max(139//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 179)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3762 * slope + 0.0011536 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_136_struct_v136_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=186, w2=150, w3=97, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(150, min_periods=max(150//3, 2)).mean()
    noise = impulse.abs().rolling(97, min_periods=max(97//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.23125 + 0.0011537 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_137_struct_v137_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=193, w2=161, w3=110, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 193)
    acceleration = _rolling_slope(velocity, 161)
    curvature = _rolling_slope(acceleration, 110)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3914 * acceleration + 0.0011538 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_138_struct_v138_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=200, w2=172, w3=123, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(200, min_periods=max(200//3, 2)).mean(), upside.rolling(172, min_periods=max(172//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(123) * 1.26 + 0.0011539 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_139_struct_v139_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=207, w2=183, w3=136, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(183, min_periods=max(183//3, 2)).max()
    rebound = x - x.rolling(207, min_periods=max(207//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.4066 * _rolling_slope(draw, 136) + 0.001154 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_140_struct_v140_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=214, w2=194, w3=149, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 214)
    baseline = trend.rolling(194, min_periods=max(194//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(149, min_periods=max(149//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.28875 + 0.0011541 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_141_struct_v141_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=221, w2=205, w3=162, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 221)
    slow = _rolling_slope(x, 205)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=162, adjust=False).mean() * 1.303125 + 0.0011542 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_142_struct_v142_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=228, w2=216, w3=175, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(216, min_periods=max(216//3, 2)).max()
    trough = x.rolling(228, min_periods=max(228//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.3175 + 0.0011543 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_143_struct_v143_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=235, w2=227, w3=188, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(227, min_periods=max(227//3, 2)).rank(pct=True)
    persistence = change.rolling(188, min_periods=max(188//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0606 * persistence + 0.0011544 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_144_struct_v144_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=242, w2=238, w3=201, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(242, min_periods=max(242//3, 2)).std()
    vol_slow = ret.rolling(238, min_periods=max(238//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.34625 + 0.0011545 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_145_struct_v145_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=249, w2=249, w3=214, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(249, min_periods=max(249//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 249)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0758 * slope + 0.0011546 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_146_struct_v146_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=5, w2=260, w3=227, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(5)
    drag = impulse.rolling(260, min_periods=max(260//3, 2)).mean()
    noise = impulse.abs().rolling(227, min_periods=max(227//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.375 + 0.0011547 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_147_struct_v147_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=12, w2=271, w3=240, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 12)
    acceleration = _rolling_slope(velocity, 271)
    curvature = _rolling_slope(acceleration, 240)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.091 * acceleration + 0.0011548 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_148_struct_v148_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=19, w2=282, w3=253, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(19, min_periods=max(19//3, 2)).mean(), upside.rolling(282, min_periods=max(282//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.40375 + 0.0011549 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_149_struct_v149_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=26, w2=293, w3=266, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(293, min_periods=max(293//3, 2)).max()
    rebound = x - x.rolling(26, min_periods=max(26//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1062 * _rolling_slope(draw, 266) + 0.001155 * anchor
    return base_signal.diff().diff().diff()

def f19_dilu_150_struct_v150_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=33, w2=304, w3=279, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 33)
    baseline = trend.rolling(304, min_periods=max(304//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(279, min_periods=max(279//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.4325 + 0.0011551 * anchor
    return base_signal.diff().diff().diff()
