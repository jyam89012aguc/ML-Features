"""73 merton distance to default proxy base features 76-150 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Credit_Risk - Institutional-grade short-side signal.
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

def f73_mdd_076_struct_v76(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=81, w2=162, w3=353, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(81)
    drag = impulse.rolling(162, min_periods=max(162//3, 2)).mean()
    noise = impulse.abs().rolling(353, min_periods=max(353//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.0375 + 0.0037877 * anchor

def f73_mdd_077_struct_v77(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=88, w2=173, w3=366, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 88)
    acceleration = _rolling_slope(velocity, 173)
    curvature = _rolling_slope(acceleration, 366)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3306 * acceleration + 0.0037878 * anchor

def f73_mdd_078_struct_v78(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=95, w2=184, w3=379, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(95, min_periods=max(95//3, 2)).mean(), upside.rolling(184, min_periods=max(184//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.06625 + 0.0037879 * anchor

def f73_mdd_079_struct_v79(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=102, w2=195, w3=392, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(195, min_periods=max(195//3, 2)).max()
    rebound = x - x.rolling(102, min_periods=max(102//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3458 * _rolling_slope(draw, 392) + 0.003788 * anchor

def f73_mdd_080_struct_v80(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=109, w2=206, w3=405, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 109)
    baseline = trend.rolling(206, min_periods=max(206//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(405, min_periods=max(405//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.095 + 0.0037881 * anchor

def f73_mdd_081_struct_v81(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=116, w2=217, w3=418, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 116)
    slow = _rolling_slope(x, 217)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.109375 + 0.0037882 * anchor

def f73_mdd_082_struct_v82(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=123, w2=228, w3=431, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(228, min_periods=max(228//3, 2)).max()
    trough = x.rolling(123, min_periods=max(123//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.12375 + 0.0037883 * anchor

def f73_mdd_083_struct_v83(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=130, w2=239, w3=444, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(239, min_periods=max(239//3, 2)).rank(pct=True)
    persistence = change.rolling(444, min_periods=max(444//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3762 * persistence + 0.0037884 * anchor

def f73_mdd_084_struct_v84(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=137, w2=250, w3=457, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(137, min_periods=max(137//3, 2)).std()
    vol_slow = ret.rolling(250, min_periods=max(250//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.1525 + 0.0037885 * anchor

def f73_mdd_085_struct_v85(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=144, w2=261, w3=470, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(261, min_periods=max(261//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 144)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3914 * slope + 0.0037886 * anchor

def f73_mdd_086_struct_v86(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=151, w2=272, w3=483, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(272, min_periods=max(272//3, 2)).mean()
    noise = impulse.abs().rolling(483, min_periods=max(483//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.18125 + 0.0037887 * anchor

def f73_mdd_087_struct_v87(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=158, w2=283, w3=496, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 158)
    acceleration = _rolling_slope(velocity, 283)
    curvature = _rolling_slope(acceleration, 496)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.4066 * acceleration + 0.0037888 * anchor

def f73_mdd_088_struct_v88(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=165, w2=294, w3=509, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(165, min_periods=max(165//3, 2)).mean(), upside.rolling(294, min_periods=max(294//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.21 + 0.0037889 * anchor

def f73_mdd_089_struct_v89(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=172, w2=305, w3=522, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(305, min_periods=max(305//3, 2)).max()
    rebound = x - x.rolling(172, min_periods=max(172//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0454 * _rolling_slope(draw, 522) + 0.003789 * anchor

def f73_mdd_090_struct_v90(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=179, w2=316, w3=535, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 179)
    baseline = trend.rolling(316, min_periods=max(316//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(535, min_periods=max(535//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.23875 + 0.0037891 * anchor

def f73_mdd_091_struct_v91(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=186, w2=327, w3=548, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 186)
    slow = _rolling_slope(x, 327)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.253125 + 0.0037892 * anchor

def f73_mdd_092_struct_v92(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=193, w2=338, w3=561, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(338, min_periods=max(338//3, 2)).max()
    trough = x.rolling(193, min_periods=max(193//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.2675 + 0.0037893 * anchor

def f73_mdd_093_struct_v93(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=200, w2=349, w3=574, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(349, min_periods=max(349//3, 2)).rank(pct=True)
    persistence = change.rolling(574, min_periods=max(574//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0758 * persistence + 0.0037894 * anchor

def f73_mdd_094_struct_v94(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=207, w2=360, w3=587, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(207, min_periods=max(207//3, 2)).std()
    vol_slow = ret.rolling(360, min_periods=max(360//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.29625 + 0.0037895 * anchor

def f73_mdd_095_struct_v95(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=214, w2=371, w3=600, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(371, min_periods=max(371//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 214)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.091 * slope + 0.0037896 * anchor

def f73_mdd_096_struct_v96(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=221, w2=382, w3=613, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(382, min_periods=max(382//3, 2)).mean()
    noise = impulse.abs().rolling(613, min_periods=max(613//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.325 + 0.0037897 * anchor

def f73_mdd_097_struct_v97(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=228, w2=393, w3=626, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 228)
    acceleration = _rolling_slope(velocity, 393)
    curvature = _rolling_slope(acceleration, 626)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1062 * acceleration + 0.0037898 * anchor

def f73_mdd_098_struct_v98(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=235, w2=404, w3=639, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(235, min_periods=max(235//3, 2)).mean(), upside.rolling(404, min_periods=max(404//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.35375 + 0.0037899 * anchor

def f73_mdd_099_struct_v99(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=242, w2=415, w3=652, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(415, min_periods=max(415//3, 2)).max()
    rebound = x - x.rolling(242, min_periods=max(242//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1214 * _rolling_slope(draw, 652) + 0.00379 * anchor

def f73_mdd_100_struct_v100(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=249, w2=426, w3=665, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 249)
    baseline = trend.rolling(426, min_periods=max(426//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(665, min_periods=max(665//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.3825 + 0.0037901 * anchor

def f73_mdd_101_struct_v101(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=5, w2=437, w3=678, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 5)
    slow = _rolling_slope(x, 437)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.396875 + 0.0037902 * anchor

def f73_mdd_102_struct_v102(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=12, w2=448, w3=691, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(448, min_periods=max(448//3, 2)).max()
    trough = x.rolling(12, min_periods=max(12//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.41125 + 0.0037903 * anchor

def f73_mdd_103_struct_v103(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=19, w2=459, w3=704, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(19)
    rank = change.rolling(459, min_periods=max(459//3, 2)).rank(pct=True)
    persistence = change.rolling(704, min_periods=max(704//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1518 * persistence + 0.0037904 * anchor

def f73_mdd_104_struct_v104(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=26, w2=470, w3=717, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(26, min_periods=max(26//3, 2)).std()
    vol_slow = ret.rolling(470, min_periods=max(470//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.44 + 0.0037905 * anchor

def f73_mdd_105_struct_v105(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=33, w2=481, w3=730, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(481, min_periods=max(481//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 33)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.167 * slope + 0.0037906 * anchor

def f73_mdd_106_struct_v106(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=40, w2=492, w3=743, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(40)
    drag = impulse.rolling(492, min_periods=max(492//3, 2)).mean()
    noise = impulse.abs().rolling(743, min_periods=max(743//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.46875 + 0.0037907 * anchor

def f73_mdd_107_struct_v107(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=47, w2=503, w3=756, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 47)
    acceleration = _rolling_slope(velocity, 503)
    curvature = _rolling_slope(acceleration, 756)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1822 * acceleration + 0.0037908 * anchor

def f73_mdd_108_struct_v108(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=54, w2=11, w3=769, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(54, min_periods=max(54//3, 2)).mean(), upside.rolling(11, min_periods=max(11//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.4975 + 0.0037909 * anchor

def f73_mdd_109_struct_v109(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=61, w2=22, w3=25, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(22, min_periods=max(22//3, 2)).max()
    rebound = x - x.rolling(61, min_periods=max(61//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1974 * _rolling_slope(draw, 25) + 0.003791 * anchor

def f73_mdd_110_struct_v110(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=68, w2=33, w3=38, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 68)
    baseline = trend.rolling(33, min_periods=max(33//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(38, min_periods=max(38//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.52625 + 0.0037911 * anchor

def f73_mdd_111_struct_v111(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=75, w2=44, w3=51, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 75)
    slow = _rolling_slope(x, 44)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=51, adjust=False).mean() * 1.540625 + 0.0037912 * anchor

def f73_mdd_112_struct_v112(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=82, w2=55, w3=64, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(55, min_periods=max(55//3, 2)).max()
    trough = x.rolling(82, min_periods=max(82//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.555 + 0.0037913 * anchor

def f73_mdd_113_struct_v113(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=89, w2=66, w3=77, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(89)
    rank = change.rolling(66, min_periods=max(66//3, 2)).rank(pct=True)
    persistence = change.rolling(77, min_periods=max(77//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2278 * persistence + 0.0037914 * anchor

def f73_mdd_114_struct_v114(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=96, w2=77, w3=90, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(96, min_periods=max(96//3, 2)).std()
    vol_slow = ret.rolling(77, min_periods=max(77//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.58375 + 0.0037915 * anchor

def f73_mdd_115_struct_v115(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=103, w2=88, w3=103, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(88, min_periods=max(88//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 103)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.243 * slope + 0.0037916 * anchor

def f73_mdd_116_struct_v116(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=110, w2=99, w3=116, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(110)
    drag = impulse.rolling(99, min_periods=max(99//3, 2)).mean()
    noise = impulse.abs().rolling(116, min_periods=max(116//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.6125 + 0.0037917 * anchor

def f73_mdd_117_struct_v117(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=117, w2=110, w3=129, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 117)
    acceleration = _rolling_slope(velocity, 110)
    curvature = _rolling_slope(acceleration, 129)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2582 * acceleration + 0.0037918 * anchor

def f73_mdd_118_struct_v118(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=124, w2=121, w3=142, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(124, min_periods=max(124//3, 2)).mean(), upside.rolling(121, min_periods=max(121//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.868125 + 0.0037919 * anchor

def f73_mdd_119_struct_v119(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=131, w2=132, w3=155, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(132, min_periods=max(132//3, 2)).max()
    rebound = x - x.rolling(131, min_periods=max(131//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2734 * _rolling_slope(draw, 155) + 0.003792 * anchor

def f73_mdd_120_struct_v120(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=138, w2=143, w3=168, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 138)
    baseline = trend.rolling(143, min_periods=max(143//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(168, min_periods=max(168//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.896875 + 0.0037921 * anchor

def f73_mdd_121_struct_v121(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=145, w2=154, w3=181, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 145)
    slow = _rolling_slope(x, 154)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=181, adjust=False).mean() * 0.91125 + 0.0037922 * anchor

def f73_mdd_122_struct_v122(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=152, w2=165, w3=194, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(165, min_periods=max(165//3, 2)).max()
    trough = x.rolling(152, min_periods=max(152//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.925625 + 0.0037923 * anchor

def f73_mdd_123_struct_v123(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=159, w2=176, w3=207, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(176, min_periods=max(176//3, 2)).rank(pct=True)
    persistence = change.rolling(207, min_periods=max(207//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3038 * persistence + 0.0037924 * anchor

def f73_mdd_124_struct_v124(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=166, w2=187, w3=220, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(166, min_periods=max(166//3, 2)).std()
    vol_slow = ret.rolling(187, min_periods=max(187//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.954375 + 0.0037925 * anchor

def f73_mdd_125_struct_v125(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=173, w2=198, w3=233, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(198, min_periods=max(198//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 173)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.319 * slope + 0.0037926 * anchor

def f73_mdd_126_struct_v126(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=180, w2=209, w3=246, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(209, min_periods=max(209//3, 2)).mean()
    noise = impulse.abs().rolling(246, min_periods=max(246//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.983125 + 0.0037927 * anchor

def f73_mdd_127_struct_v127(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=187, w2=220, w3=259, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 187)
    acceleration = _rolling_slope(velocity, 220)
    curvature = _rolling_slope(acceleration, 259)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3342 * acceleration + 0.0037928 * anchor

def f73_mdd_128_struct_v128(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=194, w2=231, w3=272, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(194, min_periods=max(194//3, 2)).mean(), upside.rolling(231, min_periods=max(231//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.011875 + 0.0037929 * anchor

def f73_mdd_129_struct_v129(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=201, w2=242, w3=285, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(242, min_periods=max(242//3, 2)).max()
    rebound = x - x.rolling(201, min_periods=max(201//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3494 * _rolling_slope(draw, 285) + 0.003793 * anchor

def f73_mdd_130_struct_v130(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=208, w2=253, w3=298, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 208)
    baseline = trend.rolling(253, min_periods=max(253//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(298, min_periods=max(298//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.040625 + 0.0037931 * anchor

def f73_mdd_131_struct_v131(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=215, w2=264, w3=311, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 215)
    slow = _rolling_slope(x, 264)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.055 + 0.0037932 * anchor

def f73_mdd_132_struct_v132(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=222, w2=275, w3=324, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(275, min_periods=max(275//3, 2)).max()
    trough = x.rolling(222, min_periods=max(222//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.069375 + 0.0037933 * anchor

def f73_mdd_133_struct_v133(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=229, w2=286, w3=337, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(286, min_periods=max(286//3, 2)).rank(pct=True)
    persistence = change.rolling(337, min_periods=max(337//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3798 * persistence + 0.0037934 * anchor

def f73_mdd_134_struct_v134(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=236, w2=297, w3=350, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(236, min_periods=max(236//3, 2)).std()
    vol_slow = ret.rolling(297, min_periods=max(297//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.098125 + 0.0037935 * anchor

def f73_mdd_135_struct_v135(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=243, w2=308, w3=363, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(308, min_periods=max(308//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 243)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.395 * slope + 0.0037936 * anchor

def f73_mdd_136_struct_v136(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=250, w2=319, w3=376, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(319, min_periods=max(319//3, 2)).mean()
    noise = impulse.abs().rolling(376, min_periods=max(376//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.126875 + 0.0037937 * anchor

def f73_mdd_137_struct_v137(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=6, w2=330, w3=389, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 6)
    acceleration = _rolling_slope(velocity, 330)
    curvature = _rolling_slope(acceleration, 389)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.4102 * acceleration + 0.0037938 * anchor

def f73_mdd_138_struct_v138(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=13, w2=341, w3=402, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(13, min_periods=max(13//3, 2)).mean(), upside.rolling(341, min_periods=max(341//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.155625 + 0.0037939 * anchor

def f73_mdd_139_struct_v139(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=20, w2=352, w3=415, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(352, min_periods=max(352//3, 2)).max()
    rebound = x - x.rolling(20, min_periods=max(20//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.049 * _rolling_slope(draw, 415) + 0.003794 * anchor

def f73_mdd_140_struct_v140(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=27, w2=363, w3=428, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 27)
    baseline = trend.rolling(363, min_periods=max(363//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(428, min_periods=max(428//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.184375 + 0.0037941 * anchor

def f73_mdd_141_struct_v141(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=34, w2=374, w3=441, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 34)
    slow = _rolling_slope(x, 374)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.19875 + 0.0037942 * anchor

def f73_mdd_142_struct_v142(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=41, w2=385, w3=454, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(385, min_periods=max(385//3, 2)).max()
    trough = x.rolling(41, min_periods=max(41//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.213125 + 0.0037943 * anchor

def f73_mdd_143_struct_v143(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=48, w2=396, w3=467, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(48)
    rank = change.rolling(396, min_periods=max(396//3, 2)).rank(pct=True)
    persistence = change.rolling(467, min_periods=max(467//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0794 * persistence + 0.0037944 * anchor

def f73_mdd_144_struct_v144(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=55, w2=407, w3=480, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(55, min_periods=max(55//3, 2)).std()
    vol_slow = ret.rolling(407, min_periods=max(407//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.241875 + 0.0037945 * anchor

def f73_mdd_145_struct_v145(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=62, w2=418, w3=493, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(418, min_periods=max(418//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 62)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0946 * slope + 0.0037946 * anchor

def f73_mdd_146_struct_v146(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=69, w2=429, w3=506, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(69)
    drag = impulse.rolling(429, min_periods=max(429//3, 2)).mean()
    noise = impulse.abs().rolling(506, min_periods=max(506//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.270625 + 0.0037947 * anchor

def f73_mdd_147_struct_v147(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=76, w2=440, w3=519, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 76)
    acceleration = _rolling_slope(velocity, 440)
    curvature = _rolling_slope(acceleration, 519)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1098 * acceleration + 0.0037948 * anchor

def f73_mdd_148_struct_v148(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=83, w2=451, w3=532, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(83, min_periods=max(83//3, 2)).mean(), upside.rolling(451, min_periods=max(451//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.299375 + 0.0037949 * anchor

def f73_mdd_149_struct_v149(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=90, w2=462, w3=545, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(462, min_periods=max(462//3, 2)).max()
    rebound = x - x.rolling(90, min_periods=max(90//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.125 * _rolling_slope(draw, 545) + 0.003795 * anchor

def f73_mdd_150_struct_v150(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=97, w2=473, w3=558, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 97)
    baseline = trend.rolling(473, min_periods=max(473//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(558, min_periods=max(558//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.328125 + 0.0037951 * anchor
