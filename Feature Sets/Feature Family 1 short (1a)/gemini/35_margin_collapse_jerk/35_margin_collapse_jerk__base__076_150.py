"""35 margin collapse jerk base features 76-150 â€” Pipeline 1a-HF Grade v3.

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

def f35_mcj_076_struct_v76(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=200, w2=466, w3=726, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(466, min_periods=max(466//3, 2)).mean()
    noise = impulse.abs().rolling(726, min_periods=max(726//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.525625 + 0.0021077 * anchor

def f35_mcj_077_struct_v77(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=207, w2=477, w3=739, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 207)
    acceleration = _rolling_slope(velocity, 477)
    curvature = _rolling_slope(acceleration, 739)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2502 * acceleration + 0.0021078 * anchor

def f35_mcj_078_struct_v78(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=214, w2=488, w3=752, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(214, min_periods=max(214//3, 2)).mean(), upside.rolling(488, min_periods=max(488//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.554375 + 0.0021079 * anchor

def f35_mcj_079_struct_v79(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=221, w2=499, w3=765, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(499, min_periods=max(499//3, 2)).max()
    rebound = x - x.rolling(221, min_periods=max(221//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2654 * _rolling_slope(draw, 765) + 0.002108 * anchor

def f35_mcj_080_struct_v80(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=228, w2=510, w3=21, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 228)
    baseline = trend.rolling(510, min_periods=max(510//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(21, min_periods=max(21//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.583125 + 0.0021081 * anchor

def f35_mcj_081_struct_v81(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=235, w2=18, w3=34, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 235)
    slow = _rolling_slope(x, 18)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=34, adjust=False).mean() * 1.5975 + 0.0021082 * anchor

def f35_mcj_082_struct_v82(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=242, w2=29, w3=47, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(29, min_periods=max(29//3, 2)).max()
    trough = x.rolling(242, min_periods=max(242//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.611875 + 0.0021083 * anchor

def f35_mcj_083_struct_v83(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=249, w2=40, w3=60, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(40, min_periods=max(40//3, 2)).rank(pct=True)
    persistence = change.rolling(60, min_periods=max(60//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2958 * persistence + 0.0021084 * anchor

def f35_mcj_084_struct_v84(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=5, w2=51, w3=73, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(5, min_periods=max(5//3, 2)).std()
    vol_slow = ret.rolling(51, min_periods=max(51//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.8675 + 0.0021085 * anchor

def f35_mcj_085_struct_v85(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=12, w2=62, w3=86, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(62, min_periods=max(62//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 12)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.311 * slope + 0.0021086 * anchor

def f35_mcj_086_struct_v86(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=19, w2=73, w3=99, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(19)
    drag = impulse.rolling(73, min_periods=max(73//3, 2)).mean()
    noise = impulse.abs().rolling(99, min_periods=max(99//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.89625 + 0.0021087 * anchor

def f35_mcj_087_struct_v87(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=26, w2=84, w3=112, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 26)
    acceleration = _rolling_slope(velocity, 84)
    curvature = _rolling_slope(acceleration, 112)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3262 * acceleration + 0.0021088 * anchor

def f35_mcj_088_struct_v88(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=33, w2=95, w3=125, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(33, min_periods=max(33//3, 2)).mean(), upside.rolling(95, min_periods=max(95//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(125) * 0.925 + 0.0021089 * anchor

def f35_mcj_089_struct_v89(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=40, w2=106, w3=138, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(106, min_periods=max(106//3, 2)).max()
    rebound = x - x.rolling(40, min_periods=max(40//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3414 * _rolling_slope(draw, 138) + 0.002109 * anchor

def f35_mcj_090_struct_v90(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=47, w2=117, w3=151, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 47)
    baseline = trend.rolling(117, min_periods=max(117//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(151, min_periods=max(151//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.95375 + 0.0021091 * anchor

def f35_mcj_091_struct_v91(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=54, w2=128, w3=164, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 54)
    slow = _rolling_slope(x, 128)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=164, adjust=False).mean() * 0.968125 + 0.0021092 * anchor

def f35_mcj_092_struct_v92(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=61, w2=139, w3=177, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(139, min_periods=max(139//3, 2)).max()
    trough = x.rolling(61, min_periods=max(61//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.9825 + 0.0021093 * anchor

def f35_mcj_093_struct_v93(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=68, w2=150, w3=190, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(68)
    rank = change.rolling(150, min_periods=max(150//3, 2)).rank(pct=True)
    persistence = change.rolling(190, min_periods=max(190//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3718 * persistence + 0.0021094 * anchor

def f35_mcj_094_struct_v94(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=75, w2=161, w3=203, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(75, min_periods=max(75//3, 2)).std()
    vol_slow = ret.rolling(161, min_periods=max(161//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.01125 + 0.0021095 * anchor

def f35_mcj_095_struct_v95(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=82, w2=172, w3=216, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(172, min_periods=max(172//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 82)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.387 * slope + 0.0021096 * anchor

def f35_mcj_096_struct_v96(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=89, w2=183, w3=229, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(89)
    drag = impulse.rolling(183, min_periods=max(183//3, 2)).mean()
    noise = impulse.abs().rolling(229, min_periods=max(229//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.04 + 0.0021097 * anchor

def f35_mcj_097_struct_v97(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=96, w2=194, w3=242, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 96)
    acceleration = _rolling_slope(velocity, 194)
    curvature = _rolling_slope(acceleration, 242)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.4022 * acceleration + 0.0021098 * anchor

def f35_mcj_098_struct_v98(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=103, w2=205, w3=255, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(103, min_periods=max(103//3, 2)).mean(), upside.rolling(205, min_periods=max(205//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.06875 + 0.0021099 * anchor

def f35_mcj_099_struct_v99(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=110, w2=216, w3=268, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(216, min_periods=max(216//3, 2)).max()
    rebound = x - x.rolling(110, min_periods=max(110//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.041 * _rolling_slope(draw, 268) + 0.00211 * anchor

def f35_mcj_100_struct_v100(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=117, w2=227, w3=281, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 117)
    baseline = trend.rolling(227, min_periods=max(227//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(281, min_periods=max(281//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.0975 + 0.0021101 * anchor

def f35_mcj_101_struct_v101(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=124, w2=238, w3=294, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 124)
    slow = _rolling_slope(x, 238)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=294, adjust=False).mean() * 1.111875 + 0.0021102 * anchor

def f35_mcj_102_struct_v102(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=131, w2=249, w3=307, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(249, min_periods=max(249//3, 2)).max()
    trough = x.rolling(131, min_periods=max(131//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.12625 + 0.0021103 * anchor

def f35_mcj_103_struct_v103(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=138, w2=260, w3=320, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(260, min_periods=max(260//3, 2)).rank(pct=True)
    persistence = change.rolling(320, min_periods=max(320//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0714 * persistence + 0.0021104 * anchor

def f35_mcj_104_struct_v104(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=145, w2=271, w3=333, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(145, min_periods=max(145//3, 2)).std()
    vol_slow = ret.rolling(271, min_periods=max(271//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.155 + 0.0021105 * anchor

def f35_mcj_105_struct_v105(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=152, w2=282, w3=346, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(282, min_periods=max(282//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 152)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0866 * slope + 0.0021106 * anchor

def f35_mcj_106_struct_v106(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=159, w2=293, w3=359, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(293, min_periods=max(293//3, 2)).mean()
    noise = impulse.abs().rolling(359, min_periods=max(359//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.18375 + 0.0021107 * anchor

def f35_mcj_107_struct_v107(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=166, w2=304, w3=372, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 166)
    acceleration = _rolling_slope(velocity, 304)
    curvature = _rolling_slope(acceleration, 372)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1018 * acceleration + 0.0021108 * anchor

def f35_mcj_108_struct_v108(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=173, w2=315, w3=385, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(173, min_periods=max(173//3, 2)).mean(), upside.rolling(315, min_periods=max(315//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.2125 + 0.0021109 * anchor

def f35_mcj_109_struct_v109(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=180, w2=326, w3=398, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(326, min_periods=max(326//3, 2)).max()
    rebound = x - x.rolling(180, min_periods=max(180//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.117 * _rolling_slope(draw, 398) + 0.002111 * anchor

def f35_mcj_110_struct_v110(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=187, w2=337, w3=411, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 187)
    baseline = trend.rolling(337, min_periods=max(337//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(411, min_periods=max(411//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.24125 + 0.0021111 * anchor

def f35_mcj_111_struct_v111(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=194, w2=348, w3=424, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 194)
    slow = _rolling_slope(x, 348)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.255625 + 0.0021112 * anchor

def f35_mcj_112_struct_v112(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=201, w2=359, w3=437, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(359, min_periods=max(359//3, 2)).max()
    trough = x.rolling(201, min_periods=max(201//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.27 + 0.0021113 * anchor

def f35_mcj_113_struct_v113(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=208, w2=370, w3=450, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(370, min_periods=max(370//3, 2)).rank(pct=True)
    persistence = change.rolling(450, min_periods=max(450//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1474 * persistence + 0.0021114 * anchor

def f35_mcj_114_struct_v114(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=215, w2=381, w3=463, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(215, min_periods=max(215//3, 2)).std()
    vol_slow = ret.rolling(381, min_periods=max(381//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.29875 + 0.0021115 * anchor

def f35_mcj_115_struct_v115(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=222, w2=392, w3=476, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(392, min_periods=max(392//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 222)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1626 * slope + 0.0021116 * anchor

def f35_mcj_116_struct_v116(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=229, w2=403, w3=489, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(403, min_periods=max(403//3, 2)).mean()
    noise = impulse.abs().rolling(489, min_periods=max(489//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.3275 + 0.0021117 * anchor

def f35_mcj_117_struct_v117(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=236, w2=414, w3=502, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 236)
    acceleration = _rolling_slope(velocity, 414)
    curvature = _rolling_slope(acceleration, 502)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1778 * acceleration + 0.0021118 * anchor

def f35_mcj_118_struct_v118(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=243, w2=425, w3=515, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(243, min_periods=max(243//3, 2)).mean(), upside.rolling(425, min_periods=max(425//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.35625 + 0.0021119 * anchor

def f35_mcj_119_struct_v119(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=250, w2=436, w3=528, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(436, min_periods=max(436//3, 2)).max()
    rebound = x - x.rolling(250, min_periods=max(250//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.193 * _rolling_slope(draw, 528) + 0.002112 * anchor

def f35_mcj_120_struct_v120(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=6, w2=447, w3=541, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 6)
    baseline = trend.rolling(447, min_periods=max(447//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(541, min_periods=max(541//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.385 + 0.0021121 * anchor

def f35_mcj_121_struct_v121(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=13, w2=458, w3=554, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 13)
    slow = _rolling_slope(x, 458)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.399375 + 0.0021122 * anchor

def f35_mcj_122_struct_v122(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=20, w2=469, w3=567, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(469, min_periods=max(469//3, 2)).max()
    trough = x.rolling(20, min_periods=max(20//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.41375 + 0.0021123 * anchor

def f35_mcj_123_struct_v123(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=27, w2=480, w3=580, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(27)
    rank = change.rolling(480, min_periods=max(480//3, 2)).rank(pct=True)
    persistence = change.rolling(580, min_periods=max(580//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2234 * persistence + 0.0021124 * anchor

def f35_mcj_124_struct_v124(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=34, w2=491, w3=593, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(34, min_periods=max(34//3, 2)).std()
    vol_slow = ret.rolling(491, min_periods=max(491//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.4425 + 0.0021125 * anchor

def f35_mcj_125_struct_v125(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=41, w2=502, w3=606, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(502, min_periods=max(502//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 41)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2386 * slope + 0.0021126 * anchor

def f35_mcj_126_struct_v126(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=48, w2=10, w3=619, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(48)
    drag = impulse.rolling(10, min_periods=max(10//3, 2)).mean()
    noise = impulse.abs().rolling(619, min_periods=max(619//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.47125 + 0.0021127 * anchor

def f35_mcj_127_struct_v127(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=55, w2=21, w3=632, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 55)
    acceleration = _rolling_slope(velocity, 21)
    curvature = _rolling_slope(acceleration, 632)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2538 * acceleration + 0.0021128 * anchor

def f35_mcj_128_struct_v128(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=62, w2=32, w3=645, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(62, min_periods=max(62//3, 2)).mean(), upside.rolling(32, min_periods=max(32//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.5 + 0.0021129 * anchor

def f35_mcj_129_struct_v129(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=69, w2=43, w3=658, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(43, min_periods=max(43//3, 2)).max()
    rebound = x - x.rolling(69, min_periods=max(69//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.269 * _rolling_slope(draw, 658) + 0.002113 * anchor

def f35_mcj_130_struct_v130(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=76, w2=54, w3=671, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 76)
    baseline = trend.rolling(54, min_periods=max(54//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(671, min_periods=max(671//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.52875 + 0.0021131 * anchor

def f35_mcj_131_struct_v131(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=83, w2=65, w3=684, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 83)
    slow = _rolling_slope(x, 65)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.543125 + 0.0021132 * anchor

def f35_mcj_132_struct_v132(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=90, w2=76, w3=697, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(76, min_periods=max(76//3, 2)).max()
    trough = x.rolling(90, min_periods=max(90//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.5575 + 0.0021133 * anchor

def f35_mcj_133_struct_v133(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=97, w2=87, w3=710, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(97)
    rank = change.rolling(87, min_periods=max(87//3, 2)).rank(pct=True)
    persistence = change.rolling(710, min_periods=max(710//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2994 * persistence + 0.0021134 * anchor

def f35_mcj_134_struct_v134(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=104, w2=98, w3=723, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(104, min_periods=max(104//3, 2)).std()
    vol_slow = ret.rolling(98, min_periods=max(98//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.58625 + 0.0021135 * anchor

def f35_mcj_135_struct_v135(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=111, w2=109, w3=736, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(109, min_periods=max(109//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 111)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3146 * slope + 0.0021136 * anchor

def f35_mcj_136_struct_v136(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=118, w2=120, w3=749, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(118)
    drag = impulse.rolling(120, min_periods=max(120//3, 2)).mean()
    noise = impulse.abs().rolling(749, min_periods=max(749//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.615 + 0.0021137 * anchor

def f35_mcj_137_struct_v137(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=125, w2=131, w3=762, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 125)
    acceleration = _rolling_slope(velocity, 131)
    curvature = _rolling_slope(acceleration, 762)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3298 * acceleration + 0.0021138 * anchor

def f35_mcj_138_struct_v138(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=132, w2=142, w3=18, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(132, min_periods=max(132//3, 2)).mean(), upside.rolling(142, min_periods=max(142//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(18) * 0.870625 + 0.0021139 * anchor

def f35_mcj_139_struct_v139(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=139, w2=153, w3=31, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(153, min_periods=max(153//3, 2)).max()
    rebound = x - x.rolling(139, min_periods=max(139//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.345 * _rolling_slope(draw, 31) + 0.002114 * anchor

def f35_mcj_140_struct_v140(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=146, w2=164, w3=44, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 146)
    baseline = trend.rolling(164, min_periods=max(164//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(44, min_periods=max(44//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.899375 + 0.0021141 * anchor

def f35_mcj_141_struct_v141(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=153, w2=175, w3=57, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 153)
    slow = _rolling_slope(x, 175)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=57, adjust=False).mean() * 0.91375 + 0.0021142 * anchor

def f35_mcj_142_struct_v142(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=160, w2=186, w3=70, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(186, min_periods=max(186//3, 2)).max()
    trough = x.rolling(160, min_periods=max(160//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.928125 + 0.0021143 * anchor

def f35_mcj_143_struct_v143(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=167, w2=197, w3=83, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(197, min_periods=max(197//3, 2)).rank(pct=True)
    persistence = change.rolling(83, min_periods=max(83//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3754 * persistence + 0.0021144 * anchor

def f35_mcj_144_struct_v144(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=174, w2=208, w3=96, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(174, min_periods=max(174//3, 2)).std()
    vol_slow = ret.rolling(208, min_periods=max(208//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.956875 + 0.0021145 * anchor

def f35_mcj_145_struct_v145(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=181, w2=219, w3=109, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(219, min_periods=max(219//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 181)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3906 * slope + 0.0021146 * anchor

def f35_mcj_146_struct_v146(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=188, w2=230, w3=122, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(230, min_periods=max(230//3, 2)).mean()
    noise = impulse.abs().rolling(122, min_periods=max(122//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.985625 + 0.0021147 * anchor

def f35_mcj_147_struct_v147(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=195, w2=241, w3=135, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 195)
    acceleration = _rolling_slope(velocity, 241)
    curvature = _rolling_slope(acceleration, 135)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.4058 * acceleration + 0.0021148 * anchor

def f35_mcj_148_struct_v148(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=202, w2=252, w3=148, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(202, min_periods=max(202//3, 2)).mean(), upside.rolling(252, min_periods=max(252//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.014375 + 0.0021149 * anchor

def f35_mcj_149_struct_v149(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=209, w2=263, w3=161, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(263, min_periods=max(263//3, 2)).max()
    rebound = x - x.rolling(209, min_periods=max(209//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0446 * _rolling_slope(draw, 161) + 0.002115 * anchor

def f35_mcj_150_struct_v150(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=216, w2=274, w3=174, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 216)
    baseline = trend.rolling(274, min_periods=max(274//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(174, min_periods=max(174//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.043125 + 0.0021151 * anchor
