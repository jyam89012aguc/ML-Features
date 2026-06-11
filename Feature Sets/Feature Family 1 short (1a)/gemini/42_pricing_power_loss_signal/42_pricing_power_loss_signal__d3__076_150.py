"""42 pricing power loss signal d3 third derivative features 76-150 â€” Pipeline 1a-HF Grade v3.

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

def f42_ppls_076_struct_v76_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=166, w2=451, w3=295, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(451, min_periods=max(451//3, 2)).mean()
    noise = impulse.abs().rolling(295, min_periods=max(295//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.944375 + 0.0025877 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_077_struct_v77_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=173, w2=462, w3=308, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 173)
    acceleration = _rolling_slope(velocity, 462)
    curvature = _rolling_slope(acceleration, 308)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2194 * acceleration + 0.0025878 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_078_struct_v78_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=180, w2=473, w3=321, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(180, min_periods=max(180//3, 2)).mean(), upside.rolling(473, min_periods=max(473//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.973125 + 0.0025879 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_079_struct_v79_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=187, w2=484, w3=334, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(484, min_periods=max(484//3, 2)).max()
    rebound = x - x.rolling(187, min_periods=max(187//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2346 * _rolling_slope(draw, 334) + 0.002588 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_080_struct_v80_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=194, w2=495, w3=347, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 194)
    baseline = trend.rolling(495, min_periods=max(495//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(347, min_periods=max(347//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.001875 + 0.0025881 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_081_struct_v81_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=201, w2=506, w3=360, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 201)
    slow = _rolling_slope(x, 506)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.01625 + 0.0025882 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_082_struct_v82_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=208, w2=14, w3=373, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(14, min_periods=max(14//3, 2)).max()
    trough = x.rolling(208, min_periods=max(208//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.030625 + 0.0025883 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_083_struct_v83_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=215, w2=25, w3=386, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(25, min_periods=max(25//3, 2)).rank(pct=True)
    persistence = change.rolling(386, min_periods=max(386//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.265 * persistence + 0.0025884 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_084_struct_v84_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=222, w2=36, w3=399, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(222, min_periods=max(222//3, 2)).std()
    vol_slow = ret.rolling(36, min_periods=max(36//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.059375 + 0.0025885 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_085_struct_v85_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=229, w2=47, w3=412, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(47, min_periods=max(47//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 229)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2802 * slope + 0.0025886 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_086_struct_v86_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=236, w2=58, w3=425, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(58, min_periods=max(58//3, 2)).mean()
    noise = impulse.abs().rolling(425, min_periods=max(425//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.088125 + 0.0025887 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_087_struct_v87_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=243, w2=69, w3=438, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 243)
    acceleration = _rolling_slope(velocity, 69)
    curvature = _rolling_slope(acceleration, 438)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2954 * acceleration + 0.0025888 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_088_struct_v88_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=250, w2=80, w3=451, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(250, min_periods=max(250//3, 2)).mean(), upside.rolling(80, min_periods=max(80//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.116875 + 0.0025889 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_089_struct_v89_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=6, w2=91, w3=464, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(91, min_periods=max(91//3, 2)).max()
    rebound = x - x.rolling(6, min_periods=max(6//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3106 * _rolling_slope(draw, 464) + 0.002589 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_090_struct_v90_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=13, w2=102, w3=477, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 13)
    baseline = trend.rolling(102, min_periods=max(102//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(477, min_periods=max(477//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.145625 + 0.0025891 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_091_struct_v91_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=20, w2=113, w3=490, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 20)
    slow = _rolling_slope(x, 113)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.16 + 0.0025892 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_092_struct_v92_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=27, w2=124, w3=503, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(124, min_periods=max(124//3, 2)).max()
    trough = x.rolling(27, min_periods=max(27//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.174375 + 0.0025893 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_093_struct_v93_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=34, w2=135, w3=516, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(34)
    rank = change.rolling(135, min_periods=max(135//3, 2)).rank(pct=True)
    persistence = change.rolling(516, min_periods=max(516//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.341 * persistence + 0.0025894 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_094_struct_v94_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=41, w2=146, w3=529, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(41, min_periods=max(41//3, 2)).std()
    vol_slow = ret.rolling(146, min_periods=max(146//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.203125 + 0.0025895 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_095_struct_v95_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=48, w2=157, w3=542, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(157, min_periods=max(157//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 48)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3562 * slope + 0.0025896 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_096_struct_v96_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=55, w2=168, w3=555, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(55)
    drag = impulse.rolling(168, min_periods=max(168//3, 2)).mean()
    noise = impulse.abs().rolling(555, min_periods=max(555//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.231875 + 0.0025897 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_097_struct_v97_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=62, w2=179, w3=568, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 62)
    acceleration = _rolling_slope(velocity, 179)
    curvature = _rolling_slope(acceleration, 568)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3714 * acceleration + 0.0025898 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_098_struct_v98_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=69, w2=190, w3=581, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(69, min_periods=max(69//3, 2)).mean(), upside.rolling(190, min_periods=max(190//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.260625 + 0.0025899 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_099_struct_v99_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=76, w2=201, w3=594, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(201, min_periods=max(201//3, 2)).max()
    rebound = x - x.rolling(76, min_periods=max(76//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3866 * _rolling_slope(draw, 594) + 0.00259 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_100_struct_v100_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=83, w2=212, w3=607, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 83)
    baseline = trend.rolling(212, min_periods=max(212//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(607, min_periods=max(607//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.289375 + 0.0025901 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_101_struct_v101_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=90, w2=223, w3=620, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 90)
    slow = _rolling_slope(x, 223)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.30375 + 0.0025902 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_102_struct_v102_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=97, w2=234, w3=633, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(234, min_periods=max(234//3, 2)).max()
    trough = x.rolling(97, min_periods=max(97//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.318125 + 0.0025903 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_103_struct_v103_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=104, w2=245, w3=646, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(104)
    rank = change.rolling(245, min_periods=max(245//3, 2)).rank(pct=True)
    persistence = change.rolling(646, min_periods=max(646//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0406 * persistence + 0.0025904 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_104_struct_v104_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=111, w2=256, w3=659, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(111, min_periods=max(111//3, 2)).std()
    vol_slow = ret.rolling(256, min_periods=max(256//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.346875 + 0.0025905 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_105_struct_v105_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=118, w2=267, w3=672, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(267, min_periods=max(267//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 118)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0558 * slope + 0.0025906 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_106_struct_v106_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=125, w2=278, w3=685, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(125)
    drag = impulse.rolling(278, min_periods=max(278//3, 2)).mean()
    noise = impulse.abs().rolling(685, min_periods=max(685//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.375625 + 0.0025907 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_107_struct_v107_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=132, w2=289, w3=698, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 132)
    acceleration = _rolling_slope(velocity, 289)
    curvature = _rolling_slope(acceleration, 698)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.071 * acceleration + 0.0025908 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_108_struct_v108_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=139, w2=300, w3=711, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(139, min_periods=max(139//3, 2)).mean(), upside.rolling(300, min_periods=max(300//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.404375 + 0.0025909 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_109_struct_v109_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=146, w2=311, w3=724, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(311, min_periods=max(311//3, 2)).max()
    rebound = x - x.rolling(146, min_periods=max(146//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0862 * _rolling_slope(draw, 724) + 0.002591 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_110_struct_v110_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=153, w2=322, w3=737, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 153)
    baseline = trend.rolling(322, min_periods=max(322//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(737, min_periods=max(737//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.433125 + 0.0025911 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_111_struct_v111_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=160, w2=333, w3=750, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 160)
    slow = _rolling_slope(x, 333)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.4475 + 0.0025912 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_112_struct_v112_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=167, w2=344, w3=763, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(344, min_periods=max(344//3, 2)).max()
    trough = x.rolling(167, min_periods=max(167//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.461875 + 0.0025913 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_113_struct_v113_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=174, w2=355, w3=19, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(355, min_periods=max(355//3, 2)).rank(pct=True)
    persistence = change.rolling(19, min_periods=max(19//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1166 * persistence + 0.0025914 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_114_struct_v114_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=181, w2=366, w3=32, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(181, min_periods=max(181//3, 2)).std()
    vol_slow = ret.rolling(366, min_periods=max(366//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.490625 + 0.0025915 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_115_struct_v115_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=188, w2=377, w3=45, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(377, min_periods=max(377//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 188)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1318 * slope + 0.0025916 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_116_struct_v116_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=195, w2=388, w3=58, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(388, min_periods=max(388//3, 2)).mean()
    noise = impulse.abs().rolling(58, min_periods=max(58//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.519375 + 0.0025917 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_117_struct_v117_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=202, w2=399, w3=71, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 202)
    acceleration = _rolling_slope(velocity, 399)
    curvature = _rolling_slope(acceleration, 71)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.147 * acceleration + 0.0025918 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_118_struct_v118_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=209, w2=410, w3=84, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(209, min_periods=max(209//3, 2)).mean(), upside.rolling(410, min_periods=max(410//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(84) * 1.548125 + 0.0025919 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_119_struct_v119_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=216, w2=421, w3=97, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(421, min_periods=max(421//3, 2)).max()
    rebound = x - x.rolling(216, min_periods=max(216//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1622 * _rolling_slope(draw, 97) + 0.002592 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_120_struct_v120_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=223, w2=432, w3=110, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 223)
    baseline = trend.rolling(432, min_periods=max(432//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(110, min_periods=max(110//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.576875 + 0.0025921 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_121_struct_v121_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=230, w2=443, w3=123, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 230)
    slow = _rolling_slope(x, 443)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=123, adjust=False).mean() * 1.59125 + 0.0025922 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_122_struct_v122_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=237, w2=454, w3=136, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(454, min_periods=max(454//3, 2)).max()
    trough = x.rolling(237, min_periods=max(237//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.605625 + 0.0025923 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_123_struct_v123_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=244, w2=465, w3=149, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(465, min_periods=max(465//3, 2)).rank(pct=True)
    persistence = change.rolling(149, min_periods=max(149//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1926 * persistence + 0.0025924 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_124_struct_v124_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=251, w2=476, w3=162, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(251, min_periods=max(251//3, 2)).std()
    vol_slow = ret.rolling(476, min_periods=max(476//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.86125 + 0.0025925 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_125_struct_v125_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=7, w2=487, w3=175, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(487, min_periods=max(487//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 7)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2078 * slope + 0.0025926 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_126_struct_v126_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=14, w2=498, w3=188, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(14)
    drag = impulse.rolling(498, min_periods=max(498//3, 2)).mean()
    noise = impulse.abs().rolling(188, min_periods=max(188//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.89 + 0.0025927 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_127_struct_v127_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=21, w2=509, w3=201, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 21)
    acceleration = _rolling_slope(velocity, 509)
    curvature = _rolling_slope(acceleration, 201)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.223 * acceleration + 0.0025928 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_128_struct_v128_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=28, w2=17, w3=214, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(28, min_periods=max(28//3, 2)).mean(), upside.rolling(17, min_periods=max(17//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.91875 + 0.0025929 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_129_struct_v129_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=35, w2=28, w3=227, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(28, min_periods=max(28//3, 2)).max()
    rebound = x - x.rolling(35, min_periods=max(35//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2382 * _rolling_slope(draw, 227) + 0.002593 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_130_struct_v130_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=42, w2=39, w3=240, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 42)
    baseline = trend.rolling(39, min_periods=max(39//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(240, min_periods=max(240//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.9475 + 0.0025931 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_131_struct_v131_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=49, w2=50, w3=253, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 49)
    slow = _rolling_slope(x, 50)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=253, adjust=False).mean() * 0.961875 + 0.0025932 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_132_struct_v132_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=56, w2=61, w3=266, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(61, min_periods=max(61//3, 2)).max()
    trough = x.rolling(56, min_periods=max(56//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.97625 + 0.0025933 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_133_struct_v133_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=63, w2=72, w3=279, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(63)
    rank = change.rolling(72, min_periods=max(72//3, 2)).rank(pct=True)
    persistence = change.rolling(279, min_periods=max(279//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2686 * persistence + 0.0025934 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_134_struct_v134_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=70, w2=83, w3=292, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(70, min_periods=max(70//3, 2)).std()
    vol_slow = ret.rolling(83, min_periods=max(83//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.005 + 0.0025935 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_135_struct_v135_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=77, w2=94, w3=305, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(94, min_periods=max(94//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 77)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2838 * slope + 0.0025936 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_136_struct_v136_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=84, w2=105, w3=318, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(84)
    drag = impulse.rolling(105, min_periods=max(105//3, 2)).mean()
    noise = impulse.abs().rolling(318, min_periods=max(318//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.03375 + 0.0025937 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_137_struct_v137_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=91, w2=116, w3=331, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 91)
    acceleration = _rolling_slope(velocity, 116)
    curvature = _rolling_slope(acceleration, 331)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.299 * acceleration + 0.0025938 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_138_struct_v138_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=98, w2=127, w3=344, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(98, min_periods=max(98//3, 2)).mean(), upside.rolling(127, min_periods=max(127//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.0625 + 0.0025939 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_139_struct_v139_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=105, w2=138, w3=357, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(138, min_periods=max(138//3, 2)).max()
    rebound = x - x.rolling(105, min_periods=max(105//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3142 * _rolling_slope(draw, 357) + 0.002594 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_140_struct_v140_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=112, w2=149, w3=370, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 112)
    baseline = trend.rolling(149, min_periods=max(149//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(370, min_periods=max(370//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.09125 + 0.0025941 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_141_struct_v141_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=119, w2=160, w3=383, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 119)
    slow = _rolling_slope(x, 160)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.105625 + 0.0025942 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_142_struct_v142_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=126, w2=171, w3=396, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(171, min_periods=max(171//3, 2)).max()
    trough = x.rolling(126, min_periods=max(126//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.12 + 0.0025943 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_143_struct_v143_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=133, w2=182, w3=409, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(182, min_periods=max(182//3, 2)).rank(pct=True)
    persistence = change.rolling(409, min_periods=max(409//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3446 * persistence + 0.0025944 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_144_struct_v144_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=140, w2=193, w3=422, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(140, min_periods=max(140//3, 2)).std()
    vol_slow = ret.rolling(193, min_periods=max(193//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.14875 + 0.0025945 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_145_struct_v145_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=147, w2=204, w3=435, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(204, min_periods=max(204//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 147)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3598 * slope + 0.0025946 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_146_struct_v146_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=154, w2=215, w3=448, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(215, min_periods=max(215//3, 2)).mean()
    noise = impulse.abs().rolling(448, min_periods=max(448//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.1775 + 0.0025947 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_147_struct_v147_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=161, w2=226, w3=461, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 161)
    acceleration = _rolling_slope(velocity, 226)
    curvature = _rolling_slope(acceleration, 461)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.375 * acceleration + 0.0025948 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_148_struct_v148_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=168, w2=237, w3=474, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(168, min_periods=max(168//3, 2)).mean(), upside.rolling(237, min_periods=max(237//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.20625 + 0.0025949 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_149_struct_v149_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=175, w2=248, w3=487, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(248, min_periods=max(248//3, 2)).max()
    rebound = x - x.rolling(175, min_periods=max(175//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3902 * _rolling_slope(draw, 487) + 0.002595 * anchor
    return base_signal.diff().diff().diff()

def f42_ppls_150_struct_v150_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=182, w2=259, w3=500, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 182)
    baseline = trend.rolling(259, min_periods=max(259//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(500, min_periods=max(500//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.235 + 0.0025951 * anchor
    return base_signal.diff().diff().diff()
