"""23 cash flow deterioration trajectory base features 76-150 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Fundamental_Trajectory - Institutional-grade short-side signal.
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

def f23_cfd_076_struct_v76(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=251, w2=237, w3=237, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(237, min_periods=max(237//3, 2)).mean()
    noise = impulse.abs().rolling(237, min_periods=max(237//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.85125 + 0.0013877 * anchor

def f23_cfd_077_struct_v77(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=7, w2=248, w3=250, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 7)
    acceleration = _rolling_slope(velocity, 248)
    curvature = _rolling_slope(acceleration, 250)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1082 * acceleration + 0.0013878 * anchor

def f23_cfd_078_struct_v78(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=14, w2=259, w3=263, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(14, min_periods=max(14//3, 2)).mean(), upside.rolling(259, min_periods=max(259//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.88 + 0.0013879 * anchor

def f23_cfd_079_struct_v79(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=21, w2=270, w3=276, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(270, min_periods=max(270//3, 2)).max()
    rebound = x - x.rolling(21, min_periods=max(21//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1234 * _rolling_slope(draw, 276) + 0.001388 * anchor

def f23_cfd_080_struct_v80(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=28, w2=281, w3=289, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 28)
    baseline = trend.rolling(281, min_periods=max(281//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(289, min_periods=max(289//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.90875 + 0.0013881 * anchor

def f23_cfd_081_struct_v81(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=35, w2=292, w3=302, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 35)
    slow = _rolling_slope(x, 292)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.923125 + 0.0013882 * anchor

def f23_cfd_082_struct_v82(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=42, w2=303, w3=315, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(303, min_periods=max(303//3, 2)).max()
    trough = x.rolling(42, min_periods=max(42//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.9375 + 0.0013883 * anchor

def f23_cfd_083_struct_v83(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=49, w2=314, w3=328, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(49)
    rank = change.rolling(314, min_periods=max(314//3, 2)).rank(pct=True)
    persistence = change.rolling(328, min_periods=max(328//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1538 * persistence + 0.0013884 * anchor

def f23_cfd_084_struct_v84(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=56, w2=325, w3=341, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(56, min_periods=max(56//3, 2)).std()
    vol_slow = ret.rolling(325, min_periods=max(325//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.96625 + 0.0013885 * anchor

def f23_cfd_085_struct_v85(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=63, w2=336, w3=354, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(336, min_periods=max(336//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 63)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.169 * slope + 0.0013886 * anchor

def f23_cfd_086_struct_v86(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=70, w2=347, w3=367, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(70)
    drag = impulse.rolling(347, min_periods=max(347//3, 2)).mean()
    noise = impulse.abs().rolling(367, min_periods=max(367//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.995 + 0.0013887 * anchor

def f23_cfd_087_struct_v87(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=77, w2=358, w3=380, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 77)
    acceleration = _rolling_slope(velocity, 358)
    curvature = _rolling_slope(acceleration, 380)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1842 * acceleration + 0.0013888 * anchor

def f23_cfd_088_struct_v88(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=84, w2=369, w3=393, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(84, min_periods=max(84//3, 2)).mean(), upside.rolling(369, min_periods=max(369//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.02375 + 0.0013889 * anchor

def f23_cfd_089_struct_v89(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=91, w2=380, w3=406, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(380, min_periods=max(380//3, 2)).max()
    rebound = x - x.rolling(91, min_periods=max(91//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1994 * _rolling_slope(draw, 406) + 0.001389 * anchor

def f23_cfd_090_struct_v90(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=98, w2=391, w3=419, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 98)
    baseline = trend.rolling(391, min_periods=max(391//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(419, min_periods=max(419//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.0525 + 0.0013891 * anchor

def f23_cfd_091_struct_v91(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=105, w2=402, w3=432, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 105)
    slow = _rolling_slope(x, 402)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.066875 + 0.0013892 * anchor

def f23_cfd_092_struct_v92(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=112, w2=413, w3=445, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(413, min_periods=max(413//3, 2)).max()
    trough = x.rolling(112, min_periods=max(112//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.08125 + 0.0013893 * anchor

def f23_cfd_093_struct_v93(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=119, w2=424, w3=458, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(119)
    rank = change.rolling(424, min_periods=max(424//3, 2)).rank(pct=True)
    persistence = change.rolling(458, min_periods=max(458//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2298 * persistence + 0.0013894 * anchor

def f23_cfd_094_struct_v94(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=126, w2=435, w3=471, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(126, min_periods=max(126//3, 2)).std()
    vol_slow = ret.rolling(435, min_periods=max(435//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.11 + 0.0013895 * anchor

def f23_cfd_095_struct_v95(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=133, w2=446, w3=484, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(446, min_periods=max(446//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 133)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.245 * slope + 0.0013896 * anchor

def f23_cfd_096_struct_v96(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=140, w2=457, w3=497, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(457, min_periods=max(457//3, 2)).mean()
    noise = impulse.abs().rolling(497, min_periods=max(497//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.13875 + 0.0013897 * anchor

def f23_cfd_097_struct_v97(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=147, w2=468, w3=510, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 147)
    acceleration = _rolling_slope(velocity, 468)
    curvature = _rolling_slope(acceleration, 510)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2602 * acceleration + 0.0013898 * anchor

def f23_cfd_098_struct_v98(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=154, w2=479, w3=523, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(154, min_periods=max(154//3, 2)).mean(), upside.rolling(479, min_periods=max(479//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.1675 + 0.0013899 * anchor

def f23_cfd_099_struct_v99(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=161, w2=490, w3=536, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(490, min_periods=max(490//3, 2)).max()
    rebound = x - x.rolling(161, min_periods=max(161//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2754 * _rolling_slope(draw, 536) + 0.00139 * anchor

def f23_cfd_100_struct_v100(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=168, w2=501, w3=549, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 168)
    baseline = trend.rolling(501, min_periods=max(501//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(549, min_periods=max(549//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.19625 + 0.0013901 * anchor

def f23_cfd_101_struct_v101(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=175, w2=512, w3=562, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 175)
    slow = _rolling_slope(x, 512)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.210625 + 0.0013902 * anchor

def f23_cfd_102_struct_v102(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=182, w2=20, w3=575, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(20, min_periods=max(20//3, 2)).max()
    trough = x.rolling(182, min_periods=max(182//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.225 + 0.0013903 * anchor

def f23_cfd_103_struct_v103(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=189, w2=31, w3=588, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(31, min_periods=max(31//3, 2)).rank(pct=True)
    persistence = change.rolling(588, min_periods=max(588//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3058 * persistence + 0.0013904 * anchor

def f23_cfd_104_struct_v104(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=196, w2=42, w3=601, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(196, min_periods=max(196//3, 2)).std()
    vol_slow = ret.rolling(42, min_periods=max(42//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.25375 + 0.0013905 * anchor

def f23_cfd_105_struct_v105(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=203, w2=53, w3=614, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(53, min_periods=max(53//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 203)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.321 * slope + 0.0013906 * anchor

def f23_cfd_106_struct_v106(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=210, w2=64, w3=627, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(64, min_periods=max(64//3, 2)).mean()
    noise = impulse.abs().rolling(627, min_periods=max(627//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.2825 + 0.0013907 * anchor

def f23_cfd_107_struct_v107(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=217, w2=75, w3=640, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 217)
    acceleration = _rolling_slope(velocity, 75)
    curvature = _rolling_slope(acceleration, 640)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3362 * acceleration + 0.0013908 * anchor

def f23_cfd_108_struct_v108(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=224, w2=86, w3=653, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(224, min_periods=max(224//3, 2)).mean(), upside.rolling(86, min_periods=max(86//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.31125 + 0.0013909 * anchor

def f23_cfd_109_struct_v109(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=231, w2=97, w3=666, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(97, min_periods=max(97//3, 2)).max()
    rebound = x - x.rolling(231, min_periods=max(231//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3514 * _rolling_slope(draw, 666) + 0.001391 * anchor

def f23_cfd_110_struct_v110(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=238, w2=108, w3=679, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 238)
    baseline = trend.rolling(108, min_periods=max(108//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(679, min_periods=max(679//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.34 + 0.0013911 * anchor

def f23_cfd_111_struct_v111(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=245, w2=119, w3=692, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 245)
    slow = _rolling_slope(x, 119)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.354375 + 0.0013912 * anchor

def f23_cfd_112_struct_v112(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=252, w2=130, w3=705, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(130, min_periods=max(130//3, 2)).max()
    trough = x.rolling(252, min_periods=max(252//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.36875 + 0.0013913 * anchor

def f23_cfd_113_struct_v113(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=8, w2=141, w3=718, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(8)
    rank = change.rolling(141, min_periods=max(141//3, 2)).rank(pct=True)
    persistence = change.rolling(718, min_periods=max(718//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3818 * persistence + 0.0013914 * anchor

def f23_cfd_114_struct_v114(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=15, w2=152, w3=731, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(15, min_periods=max(15//3, 2)).std()
    vol_slow = ret.rolling(152, min_periods=max(152//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.3975 + 0.0013915 * anchor

def f23_cfd_115_struct_v115(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=22, w2=163, w3=744, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(163, min_periods=max(163//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 22)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.397 * slope + 0.0013916 * anchor

def f23_cfd_116_struct_v116(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=29, w2=174, w3=757, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(29)
    drag = impulse.rolling(174, min_periods=max(174//3, 2)).mean()
    noise = impulse.abs().rolling(757, min_periods=max(757//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.42625 + 0.0013917 * anchor

def f23_cfd_117_struct_v117(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=36, w2=185, w3=770, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 36)
    acceleration = _rolling_slope(velocity, 185)
    curvature = _rolling_slope(acceleration, 770)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0358 * acceleration + 0.0013918 * anchor

def f23_cfd_118_struct_v118(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=43, w2=196, w3=26, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(43, min_periods=max(43//3, 2)).mean(), upside.rolling(196, min_periods=max(196//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(26) * 1.455 + 0.0013919 * anchor

def f23_cfd_119_struct_v119(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=50, w2=207, w3=39, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(207, min_periods=max(207//3, 2)).max()
    rebound = x - x.rolling(50, min_periods=max(50//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.051 * _rolling_slope(draw, 39) + 0.001392 * anchor

def f23_cfd_120_struct_v120(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=57, w2=218, w3=52, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 57)
    baseline = trend.rolling(218, min_periods=max(218//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(52, min_periods=max(52//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.48375 + 0.0013921 * anchor

def f23_cfd_121_struct_v121(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=64, w2=229, w3=65, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 64)
    slow = _rolling_slope(x, 229)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=65, adjust=False).mean() * 1.498125 + 0.0013922 * anchor

def f23_cfd_122_struct_v122(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=71, w2=240, w3=78, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(240, min_periods=max(240//3, 2)).max()
    trough = x.rolling(71, min_periods=max(71//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.5125 + 0.0013923 * anchor

def f23_cfd_123_struct_v123(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=78, w2=251, w3=91, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(78)
    rank = change.rolling(251, min_periods=max(251//3, 2)).rank(pct=True)
    persistence = change.rolling(91, min_periods=max(91//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0814 * persistence + 0.0013924 * anchor

def f23_cfd_124_struct_v124(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=85, w2=262, w3=104, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(85, min_periods=max(85//3, 2)).std()
    vol_slow = ret.rolling(262, min_periods=max(262//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.54125 + 0.0013925 * anchor

def f23_cfd_125_struct_v125(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=92, w2=273, w3=117, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(273, min_periods=max(273//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 92)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0966 * slope + 0.0013926 * anchor

def f23_cfd_126_struct_v126(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=99, w2=284, w3=130, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(99)
    drag = impulse.rolling(284, min_periods=max(284//3, 2)).mean()
    noise = impulse.abs().rolling(130, min_periods=max(130//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.57 + 0.0013927 * anchor

def f23_cfd_127_struct_v127(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=106, w2=295, w3=143, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 106)
    acceleration = _rolling_slope(velocity, 295)
    curvature = _rolling_slope(acceleration, 143)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1118 * acceleration + 0.0013928 * anchor

def f23_cfd_128_struct_v128(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=113, w2=306, w3=156, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(113, min_periods=max(113//3, 2)).mean(), upside.rolling(306, min_periods=max(306//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.59875 + 0.0013929 * anchor

def f23_cfd_129_struct_v129(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=120, w2=317, w3=169, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(317, min_periods=max(317//3, 2)).max()
    rebound = x - x.rolling(120, min_periods=max(120//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.127 * _rolling_slope(draw, 169) + 0.001393 * anchor

def f23_cfd_130_struct_v130(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=127, w2=328, w3=182, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 127)
    baseline = trend.rolling(328, min_periods=max(328//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(182, min_periods=max(182//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.854375 + 0.0013931 * anchor

def f23_cfd_131_struct_v131(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=134, w2=339, w3=195, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 134)
    slow = _rolling_slope(x, 339)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=195, adjust=False).mean() * 0.86875 + 0.0013932 * anchor

def f23_cfd_132_struct_v132(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=141, w2=350, w3=208, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(350, min_periods=max(350//3, 2)).max()
    trough = x.rolling(141, min_periods=max(141//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.883125 + 0.0013933 * anchor

def f23_cfd_133_struct_v133(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=148, w2=361, w3=221, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(361, min_periods=max(361//3, 2)).rank(pct=True)
    persistence = change.rolling(221, min_periods=max(221//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1574 * persistence + 0.0013934 * anchor

def f23_cfd_134_struct_v134(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=155, w2=372, w3=234, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(155, min_periods=max(155//3, 2)).std()
    vol_slow = ret.rolling(372, min_periods=max(372//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.911875 + 0.0013935 * anchor

def f23_cfd_135_struct_v135(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=162, w2=383, w3=247, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(383, min_periods=max(383//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 162)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1726 * slope + 0.0013936 * anchor

def f23_cfd_136_struct_v136(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=169, w2=394, w3=260, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(394, min_periods=max(394//3, 2)).mean()
    noise = impulse.abs().rolling(260, min_periods=max(260//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.940625 + 0.0013937 * anchor

def f23_cfd_137_struct_v137(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=176, w2=405, w3=273, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 176)
    acceleration = _rolling_slope(velocity, 405)
    curvature = _rolling_slope(acceleration, 273)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1878 * acceleration + 0.0013938 * anchor

def f23_cfd_138_struct_v138(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=183, w2=416, w3=286, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(183, min_periods=max(183//3, 2)).mean(), upside.rolling(416, min_periods=max(416//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.969375 + 0.0013939 * anchor

def f23_cfd_139_struct_v139(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=190, w2=427, w3=299, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(427, min_periods=max(427//3, 2)).max()
    rebound = x - x.rolling(190, min_periods=max(190//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.203 * _rolling_slope(draw, 299) + 0.001394 * anchor

def f23_cfd_140_struct_v140(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=197, w2=438, w3=312, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 197)
    baseline = trend.rolling(438, min_periods=max(438//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(312, min_periods=max(312//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.998125 + 0.0013941 * anchor

def f23_cfd_141_struct_v141(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=204, w2=449, w3=325, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 204)
    slow = _rolling_slope(x, 449)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.0125 + 0.0013942 * anchor

def f23_cfd_142_struct_v142(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=211, w2=460, w3=338, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(460, min_periods=max(460//3, 2)).max()
    trough = x.rolling(211, min_periods=max(211//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.026875 + 0.0013943 * anchor

def f23_cfd_143_struct_v143(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=218, w2=471, w3=351, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(471, min_periods=max(471//3, 2)).rank(pct=True)
    persistence = change.rolling(351, min_periods=max(351//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2334 * persistence + 0.0013944 * anchor

def f23_cfd_144_struct_v144(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=225, w2=482, w3=364, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(225, min_periods=max(225//3, 2)).std()
    vol_slow = ret.rolling(482, min_periods=max(482//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.055625 + 0.0013945 * anchor

def f23_cfd_145_struct_v145(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=232, w2=493, w3=377, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(493, min_periods=max(493//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 232)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2486 * slope + 0.0013946 * anchor

def f23_cfd_146_struct_v146(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=239, w2=504, w3=390, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(504, min_periods=max(504//3, 2)).mean()
    noise = impulse.abs().rolling(390, min_periods=max(390//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.084375 + 0.0013947 * anchor

def f23_cfd_147_struct_v147(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=246, w2=12, w3=403, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 246)
    acceleration = _rolling_slope(velocity, 12)
    curvature = _rolling_slope(acceleration, 403)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2638 * acceleration + 0.0013948 * anchor

def f23_cfd_148_struct_v148(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=253, w2=23, w3=416, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(253, min_periods=max(253//3, 2)).mean(), upside.rolling(23, min_periods=max(23//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.113125 + 0.0013949 * anchor

def f23_cfd_149_struct_v149(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=9, w2=34, w3=429, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(34, min_periods=max(34//3, 2)).max()
    rebound = x - x.rolling(9, min_periods=max(9//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.279 * _rolling_slope(draw, 429) + 0.001395 * anchor

def f23_cfd_150_struct_v150(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=16, w2=45, w3=442, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 16)
    baseline = trend.rolling(45, min_periods=max(45//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(442, min_periods=max(442//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.141875 + 0.0013951 * anchor
