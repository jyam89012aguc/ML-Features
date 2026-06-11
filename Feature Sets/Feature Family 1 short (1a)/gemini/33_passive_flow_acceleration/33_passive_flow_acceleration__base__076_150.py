"""33 passive flow acceleration base features 76-150 â€” Pipeline 1a-HF Grade v3.

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

def f33_pfa_076_struct_v76(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=83, w2=344, w3=266, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(83)
    drag = impulse.rolling(344, min_periods=max(344//3, 2)).mean()
    noise = impulse.abs().rolling(266, min_periods=max(266//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.284375 + 0.0019877 * anchor

def f33_pfa_077_struct_v77(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=90, w2=355, w3=279, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 90)
    acceleration = _rolling_slope(velocity, 355)
    curvature = _rolling_slope(acceleration, 279)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1638 * acceleration + 0.0019878 * anchor

def f33_pfa_078_struct_v78(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=97, w2=366, w3=292, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(97, min_periods=max(97//3, 2)).mean(), upside.rolling(366, min_periods=max(366//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.313125 + 0.0019879 * anchor

def f33_pfa_079_struct_v79(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=104, w2=377, w3=305, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(377, min_periods=max(377//3, 2)).max()
    rebound = x - x.rolling(104, min_periods=max(104//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.179 * _rolling_slope(draw, 305) + 0.001988 * anchor

def f33_pfa_080_struct_v80(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=111, w2=388, w3=318, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 111)
    baseline = trend.rolling(388, min_periods=max(388//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(318, min_periods=max(318//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.341875 + 0.0019881 * anchor

def f33_pfa_081_struct_v81(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=118, w2=399, w3=331, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 118)
    slow = _rolling_slope(x, 399)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.35625 + 0.0019882 * anchor

def f33_pfa_082_struct_v82(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=125, w2=410, w3=344, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(410, min_periods=max(410//3, 2)).max()
    trough = x.rolling(125, min_periods=max(125//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.370625 + 0.0019883 * anchor

def f33_pfa_083_struct_v83(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=132, w2=421, w3=357, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(421, min_periods=max(421//3, 2)).rank(pct=True)
    persistence = change.rolling(357, min_periods=max(357//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2094 * persistence + 0.0019884 * anchor

def f33_pfa_084_struct_v84(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=139, w2=432, w3=370, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(139, min_periods=max(139//3, 2)).std()
    vol_slow = ret.rolling(432, min_periods=max(432//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.399375 + 0.0019885 * anchor

def f33_pfa_085_struct_v85(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=146, w2=443, w3=383, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(443, min_periods=max(443//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 146)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2246 * slope + 0.0019886 * anchor

def f33_pfa_086_struct_v86(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=153, w2=454, w3=396, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(454, min_periods=max(454//3, 2)).mean()
    noise = impulse.abs().rolling(396, min_periods=max(396//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.428125 + 0.0019887 * anchor

def f33_pfa_087_struct_v87(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=160, w2=465, w3=409, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 160)
    acceleration = _rolling_slope(velocity, 465)
    curvature = _rolling_slope(acceleration, 409)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2398 * acceleration + 0.0019888 * anchor

def f33_pfa_088_struct_v88(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=167, w2=476, w3=422, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(167, min_periods=max(167//3, 2)).mean(), upside.rolling(476, min_periods=max(476//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.456875 + 0.0019889 * anchor

def f33_pfa_089_struct_v89(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=174, w2=487, w3=435, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(487, min_periods=max(487//3, 2)).max()
    rebound = x - x.rolling(174, min_periods=max(174//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.255 * _rolling_slope(draw, 435) + 0.001989 * anchor

def f33_pfa_090_struct_v90(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=181, w2=498, w3=448, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 181)
    baseline = trend.rolling(498, min_periods=max(498//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(448, min_periods=max(448//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.485625 + 0.0019891 * anchor

def f33_pfa_091_struct_v91(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=188, w2=509, w3=461, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 188)
    slow = _rolling_slope(x, 509)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.5 + 0.0019892 * anchor

def f33_pfa_092_struct_v92(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=195, w2=17, w3=474, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(17, min_periods=max(17//3, 2)).max()
    trough = x.rolling(195, min_periods=max(195//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.514375 + 0.0019893 * anchor

def f33_pfa_093_struct_v93(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=202, w2=28, w3=487, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(28, min_periods=max(28//3, 2)).rank(pct=True)
    persistence = change.rolling(487, min_periods=max(487//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2854 * persistence + 0.0019894 * anchor

def f33_pfa_094_struct_v94(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=209, w2=39, w3=500, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(209, min_periods=max(209//3, 2)).std()
    vol_slow = ret.rolling(39, min_periods=max(39//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.543125 + 0.0019895 * anchor

def f33_pfa_095_struct_v95(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=216, w2=50, w3=513, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(50, min_periods=max(50//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 216)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3006 * slope + 0.0019896 * anchor

def f33_pfa_096_struct_v96(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=223, w2=61, w3=526, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(61, min_periods=max(61//3, 2)).mean()
    noise = impulse.abs().rolling(526, min_periods=max(526//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.571875 + 0.0019897 * anchor

def f33_pfa_097_struct_v97(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=230, w2=72, w3=539, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 230)
    acceleration = _rolling_slope(velocity, 72)
    curvature = _rolling_slope(acceleration, 539)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3158 * acceleration + 0.0019898 * anchor

def f33_pfa_098_struct_v98(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=237, w2=83, w3=552, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(237, min_periods=max(237//3, 2)).mean(), upside.rolling(83, min_periods=max(83//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.600625 + 0.0019899 * anchor

def f33_pfa_099_struct_v99(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=244, w2=94, w3=565, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(94, min_periods=max(94//3, 2)).max()
    rebound = x - x.rolling(244, min_periods=max(244//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.331 * _rolling_slope(draw, 565) + 0.00199 * anchor

def f33_pfa_100_struct_v100(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=251, w2=105, w3=578, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 251)
    baseline = trend.rolling(105, min_periods=max(105//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(578, min_periods=max(578//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.85625 + 0.0019901 * anchor

def f33_pfa_101_struct_v101(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=7, w2=116, w3=591, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 7)
    slow = _rolling_slope(x, 116)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.870625 + 0.0019902 * anchor

def f33_pfa_102_struct_v102(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=14, w2=127, w3=604, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(127, min_periods=max(127//3, 2)).max()
    trough = x.rolling(14, min_periods=max(14//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.885 + 0.0019903 * anchor

def f33_pfa_103_struct_v103(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=21, w2=138, w3=617, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(21)
    rank = change.rolling(138, min_periods=max(138//3, 2)).rank(pct=True)
    persistence = change.rolling(617, min_periods=max(617//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3614 * persistence + 0.0019904 * anchor

def f33_pfa_104_struct_v104(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=28, w2=149, w3=630, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(28, min_periods=max(28//3, 2)).std()
    vol_slow = ret.rolling(149, min_periods=max(149//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.91375 + 0.0019905 * anchor

def f33_pfa_105_struct_v105(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=35, w2=160, w3=643, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(160, min_periods=max(160//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 35)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3766 * slope + 0.0019906 * anchor

def f33_pfa_106_struct_v106(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=42, w2=171, w3=656, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(42)
    drag = impulse.rolling(171, min_periods=max(171//3, 2)).mean()
    noise = impulse.abs().rolling(656, min_periods=max(656//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.9425 + 0.0019907 * anchor

def f33_pfa_107_struct_v107(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=49, w2=182, w3=669, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 49)
    acceleration = _rolling_slope(velocity, 182)
    curvature = _rolling_slope(acceleration, 669)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3918 * acceleration + 0.0019908 * anchor

def f33_pfa_108_struct_v108(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=56, w2=193, w3=682, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(56, min_periods=max(56//3, 2)).mean(), upside.rolling(193, min_periods=max(193//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.97125 + 0.0019909 * anchor

def f33_pfa_109_struct_v109(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=63, w2=204, w3=695, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(204, min_periods=max(204//3, 2)).max()
    rebound = x - x.rolling(63, min_periods=max(63//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.407 * _rolling_slope(draw, 695) + 0.001991 * anchor

def f33_pfa_110_struct_v110(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=70, w2=215, w3=708, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 70)
    baseline = trend.rolling(215, min_periods=max(215//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(708, min_periods=max(708//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.0 + 0.0019911 * anchor

def f33_pfa_111_struct_v111(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=77, w2=226, w3=721, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 77)
    slow = _rolling_slope(x, 226)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.014375 + 0.0019912 * anchor

def f33_pfa_112_struct_v112(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=84, w2=237, w3=734, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(237, min_periods=max(237//3, 2)).max()
    trough = x.rolling(84, min_periods=max(84//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.02875 + 0.0019913 * anchor

def f33_pfa_113_struct_v113(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=91, w2=248, w3=747, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(91)
    rank = change.rolling(248, min_periods=max(248//3, 2)).rank(pct=True)
    persistence = change.rolling(747, min_periods=max(747//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.061 * persistence + 0.0019914 * anchor

def f33_pfa_114_struct_v114(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=98, w2=259, w3=760, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(98, min_periods=max(98//3, 2)).std()
    vol_slow = ret.rolling(259, min_periods=max(259//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.0575 + 0.0019915 * anchor

def f33_pfa_115_struct_v115(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=105, w2=270, w3=16, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(270, min_periods=max(270//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 105)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0762 * slope + 0.0019916 * anchor

def f33_pfa_116_struct_v116(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=112, w2=281, w3=29, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(112)
    drag = impulse.rolling(281, min_periods=max(281//3, 2)).mean()
    noise = impulse.abs().rolling(29, min_periods=max(29//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.08625 + 0.0019917 * anchor

def f33_pfa_117_struct_v117(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=119, w2=292, w3=42, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 119)
    acceleration = _rolling_slope(velocity, 292)
    curvature = _rolling_slope(acceleration, 42)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0914 * acceleration + 0.0019918 * anchor

def f33_pfa_118_struct_v118(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=126, w2=303, w3=55, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(126, min_periods=max(126//3, 2)).mean(), upside.rolling(303, min_periods=max(303//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(55) * 1.115 + 0.0019919 * anchor

def f33_pfa_119_struct_v119(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=133, w2=314, w3=68, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(314, min_periods=max(314//3, 2)).max()
    rebound = x - x.rolling(133, min_periods=max(133//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1066 * _rolling_slope(draw, 68) + 0.001992 * anchor

def f33_pfa_120_struct_v120(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=140, w2=325, w3=81, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 140)
    baseline = trend.rolling(325, min_periods=max(325//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(81, min_periods=max(81//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.14375 + 0.0019921 * anchor

def f33_pfa_121_struct_v121(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=147, w2=336, w3=94, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 147)
    slow = _rolling_slope(x, 336)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=94, adjust=False).mean() * 1.158125 + 0.0019922 * anchor

def f33_pfa_122_struct_v122(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=154, w2=347, w3=107, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(347, min_periods=max(347//3, 2)).max()
    trough = x.rolling(154, min_periods=max(154//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.1725 + 0.0019923 * anchor

def f33_pfa_123_struct_v123(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=161, w2=358, w3=120, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(358, min_periods=max(358//3, 2)).rank(pct=True)
    persistence = change.rolling(120, min_periods=max(120//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.137 * persistence + 0.0019924 * anchor

def f33_pfa_124_struct_v124(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=168, w2=369, w3=133, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(168, min_periods=max(168//3, 2)).std()
    vol_slow = ret.rolling(369, min_periods=max(369//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.20125 + 0.0019925 * anchor

def f33_pfa_125_struct_v125(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=175, w2=380, w3=146, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(380, min_periods=max(380//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 175)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1522 * slope + 0.0019926 * anchor

def f33_pfa_126_struct_v126(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=182, w2=391, w3=159, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(391, min_periods=max(391//3, 2)).mean()
    noise = impulse.abs().rolling(159, min_periods=max(159//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.23 + 0.0019927 * anchor

def f33_pfa_127_struct_v127(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=189, w2=402, w3=172, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 189)
    acceleration = _rolling_slope(velocity, 402)
    curvature = _rolling_slope(acceleration, 172)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1674 * acceleration + 0.0019928 * anchor

def f33_pfa_128_struct_v128(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=196, w2=413, w3=185, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(196, min_periods=max(196//3, 2)).mean(), upside.rolling(413, min_periods=max(413//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.25875 + 0.0019929 * anchor

def f33_pfa_129_struct_v129(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=203, w2=424, w3=198, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(424, min_periods=max(424//3, 2)).max()
    rebound = x - x.rolling(203, min_periods=max(203//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1826 * _rolling_slope(draw, 198) + 0.001993 * anchor

def f33_pfa_130_struct_v130(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=210, w2=435, w3=211, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 210)
    baseline = trend.rolling(435, min_periods=max(435//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(211, min_periods=max(211//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.2875 + 0.0019931 * anchor

def f33_pfa_131_struct_v131(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=217, w2=446, w3=224, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 217)
    slow = _rolling_slope(x, 446)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=224, adjust=False).mean() * 1.301875 + 0.0019932 * anchor

def f33_pfa_132_struct_v132(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=224, w2=457, w3=237, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(457, min_periods=max(457//3, 2)).max()
    trough = x.rolling(224, min_periods=max(224//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.31625 + 0.0019933 * anchor

def f33_pfa_133_struct_v133(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=231, w2=468, w3=250, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(468, min_periods=max(468//3, 2)).rank(pct=True)
    persistence = change.rolling(250, min_periods=max(250//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.213 * persistence + 0.0019934 * anchor

def f33_pfa_134_struct_v134(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=238, w2=479, w3=263, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(238, min_periods=max(238//3, 2)).std()
    vol_slow = ret.rolling(479, min_periods=max(479//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.345 + 0.0019935 * anchor

def f33_pfa_135_struct_v135(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=245, w2=490, w3=276, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(490, min_periods=max(490//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 245)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2282 * slope + 0.0019936 * anchor

def f33_pfa_136_struct_v136(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=252, w2=501, w3=289, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(501, min_periods=max(501//3, 2)).mean()
    noise = impulse.abs().rolling(289, min_periods=max(289//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.37375 + 0.0019937 * anchor

def f33_pfa_137_struct_v137(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=8, w2=512, w3=302, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 8)
    acceleration = _rolling_slope(velocity, 512)
    curvature = _rolling_slope(acceleration, 302)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2434 * acceleration + 0.0019938 * anchor

def f33_pfa_138_struct_v138(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=15, w2=20, w3=315, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(15, min_periods=max(15//3, 2)).mean(), upside.rolling(20, min_periods=max(20//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.4025 + 0.0019939 * anchor

def f33_pfa_139_struct_v139(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=22, w2=31, w3=328, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(31, min_periods=max(31//3, 2)).max()
    rebound = x - x.rolling(22, min_periods=max(22//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2586 * _rolling_slope(draw, 328) + 0.001994 * anchor

def f33_pfa_140_struct_v140(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=29, w2=42, w3=341, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 29)
    baseline = trend.rolling(42, min_periods=max(42//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(341, min_periods=max(341//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.43125 + 0.0019941 * anchor

def f33_pfa_141_struct_v141(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=36, w2=53, w3=354, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 36)
    slow = _rolling_slope(x, 53)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.445625 + 0.0019942 * anchor

def f33_pfa_142_struct_v142(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=43, w2=64, w3=367, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(64, min_periods=max(64//3, 2)).max()
    trough = x.rolling(43, min_periods=max(43//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.46 + 0.0019943 * anchor

def f33_pfa_143_struct_v143(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=50, w2=75, w3=380, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(50)
    rank = change.rolling(75, min_periods=max(75//3, 2)).rank(pct=True)
    persistence = change.rolling(380, min_periods=max(380//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.289 * persistence + 0.0019944 * anchor

def f33_pfa_144_struct_v144(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=57, w2=86, w3=393, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(57, min_periods=max(57//3, 2)).std()
    vol_slow = ret.rolling(86, min_periods=max(86//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.48875 + 0.0019945 * anchor

def f33_pfa_145_struct_v145(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=64, w2=97, w3=406, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(97, min_periods=max(97//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 64)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3042 * slope + 0.0019946 * anchor

def f33_pfa_146_struct_v146(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=71, w2=108, w3=419, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(71)
    drag = impulse.rolling(108, min_periods=max(108//3, 2)).mean()
    noise = impulse.abs().rolling(419, min_periods=max(419//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.5175 + 0.0019947 * anchor

def f33_pfa_147_struct_v147(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=78, w2=119, w3=432, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 78)
    acceleration = _rolling_slope(velocity, 119)
    curvature = _rolling_slope(acceleration, 432)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3194 * acceleration + 0.0019948 * anchor

def f33_pfa_148_struct_v148(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=85, w2=130, w3=445, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(85, min_periods=max(85//3, 2)).mean(), upside.rolling(130, min_periods=max(130//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.54625 + 0.0019949 * anchor

def f33_pfa_149_struct_v149(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=92, w2=141, w3=458, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(141, min_periods=max(141//3, 2)).max()
    rebound = x - x.rolling(92, min_periods=max(92//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3346 * _rolling_slope(draw, 458) + 0.001995 * anchor

def f33_pfa_150_struct_v150(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=99, w2=152, w3=471, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 99)
    baseline = trend.rolling(152, min_periods=max(152//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(471, min_periods=max(471//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.575 + 0.0019951 * anchor
